"""One malformed claim must not destroy a whole paper — but it must not sneak
through either.

The extractor sometimes emits a claim with `model: null` / `metric: null`, which
failed the whole card and threw away every good claim alongside it. Bad claims
are now dropped individually (as span verification already does). The guarantees
that must survive: claims are only ever dropped, never repaired; a structural
error still fails the card; and `extra="forbid"` still holds.
"""
from __future__ import annotations

from datetime import date

import pydantic
import pytest

from pipeline import extract
from pipeline.extract import _validate_dropping_bad_claims

SPAN = "the model reaches state of the art performance on this benchmark"
TEXT = "Intro. " + SPAN + " Conclusion."


def _claim(**kw):
    base = dict(axis="G1_label_rich_parity", task="crop_type_mapping", dataset="PASTIS",
                model="tessera", baseline="task_specific", metric="f1", value=0.85,
                baseline_value=0.80, label_ratio=1.0, direction="better",
                locator="Table 1", span=SPAN)
    base.update(kw)
    return base


def _raw(claims, **kw):
    return {"self_evaluation": False, "models": ["tessera"], "tasks": ["crop_type_mapping"],
            "regions": ["global"], "axes": [], "limitations": [], "proposed_tags": [],
            "claims": claims, "summary": "s", "setup": "s", "caveats": "s", **kw}


def _meta():
    return extract.PaperMeta(key="x2025y", title="T", date=date(2025, 1, 1), authors=["A"],
                             arxiv_id="1234.5678", doi=None, doi_status="no_doi_found",
                             venue=None, self_evaluation=False)


def test_null_model_claim_is_dropped_not_the_card():
    """The exact shape seen in the wild: one claim with model=null, one good."""
    out, invalid = _validate_dropping_bad_claims(
        _raw([_claim(model=None), _claim()]))
    assert invalid == 1
    assert len(out.claims) == 1
    assert out.claims[0].model == "tessera"


def test_null_metric_and_value_claims_are_dropped():
    out, invalid = _validate_dropping_bad_claims(
        _raw([_claim(metric=None), _claim(value=None), _claim()]))
    assert invalid == 2
    assert len(out.claims) == 1


def test_extra_field_inside_a_claim_drops_only_that_claim():
    """extra="forbid" still bites — the injected field never reaches the Card."""
    out, invalid = _validate_dropping_bad_claims(
        _raw([_claim(note_ignore=True), _claim()]))
    assert invalid == 1
    assert len(out.claims) == 1
    assert not hasattr(out.claims[0], "note_ignore")


def test_structural_error_still_fails_the_whole_card():
    """An error outside `claims` is NOT salvageable: the card is untrustworthy."""
    with pytest.raises(pydantic.ValidationError):
        _validate_dropping_bad_claims(_raw([_claim()], doi="10.1234/invented"))


def test_bad_enum_outside_claims_still_fails_the_whole_card():
    with pytest.raises(pydantic.ValidationError):
        _validate_dropping_bad_claims(_raw([_claim()], axes=["NOT_AN_AXIS"]))


def test_bad_axis_inside_a_claim_drops_that_claim():
    out, invalid = _validate_dropping_bad_claims(
        _raw([_claim(axis="NOT_AN_AXIS"), _claim()]))
    assert invalid == 1
    assert len(out.claims) == 1


def test_card_survives_a_single_bad_claim_end_to_end():
    result = extract.extract_card(
        _meta(), TEXT, run_fn=lambda p, *, model: _raw([_claim(model=None), _claim()]))
    assert not result.quarantined
    assert len(result.card.claims) == 1
    assert result.dropped_claims == 1


def test_mostly_bad_claims_still_quarantine_the_card():
    """Salvage is not a licence to accept garbage: if most claims fail, the
    extraction is not trustworthy and the card is quarantined as before."""
    claims = [_claim(model=None), _claim(metric=None), _claim(value=None), _claim()]
    result = extract.extract_card(
        _meta(), TEXT, run_fn=lambda p, *, model: _raw(claims))
    assert result.quarantined
    assert "3/4" in result.reason


def test_all_claims_bad_quarantines():
    result = extract.extract_card(
        _meta(), TEXT, run_fn=lambda p, *, model: _raw([_claim(model=None)]))
    assert result.quarantined
