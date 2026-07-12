"""Schema contract tests (§10)."""
from __future__ import annotations

from datetime import date, datetime, timezone

import pydantic
import pytest

from pipeline.schema import Card, Claim, ExtractionClaim, ExtractionOutput
from pipeline.textutil import span_sha256


def test_llm_supplied_doi_is_rejected():
    # extra="forbid" means an LLM that smuggles a doi fails validation.
    with pytest.raises(pydantic.ValidationError):
        ExtractionOutput.model_validate({"summary": "x", "doi": "10.1234/abc"})


def test_claim_without_span_is_rejected():
    with pytest.raises(pydantic.ValidationError):
        ExtractionClaim.model_validate({
            "axis": "G1_label_rich_parity", "task": "crop_type_mapping",
            "dataset": "D", "model": "tessera", "metric": "f1", "value": 1.0,
            "direction": "better", "locator": "T1",
        })


def test_out_of_vocab_limitation_is_rejected():
    with pytest.raises(pydantic.ValidationError):
        ExtractionOutput.model_validate({"limitations": ["totally_made_up"]})


def test_out_of_vocab_axis_task_model_rejected():
    base = {"axis": "G1_label_rich_parity", "task": "crop_type_mapping",
            "dataset": "D", "model": "tessera", "metric": "f1", "value": 1.0,
            "direction": "better", "locator": "T1", "span": "x y z"}
    for field, bad in [("axis", "G99"), ("task", "nope"), ("model", "gpt"),
                       ("metric", "bleu")]:
        with pytest.raises(pydantic.ValidationError):
            ExtractionClaim.model_validate({**base, field: bad})


def test_span_over_25_words_rejected():
    long_span = " ".join(["word"] * 26)
    with pytest.raises(pydantic.ValidationError):
        ExtractionClaim.model_validate({
            "axis": "G1_label_rich_parity", "task": "crop_type_mapping",
            "dataset": "D", "model": "tessera", "metric": "f1", "value": 1.0,
            "direction": "better", "locator": "T1", "span": long_span})


def test_path_traversal_key_rejected():
    with pytest.raises(pydantic.ValidationError):
        Card(key="../../.github/workflows/pages", title="x", doi_status="no_doi_found",
             date=date(2025, 1, 1), extractor_version="1",
             ingested_at=datetime.now(timezone.utc))


def test_span_hash_must_match():
    with pytest.raises(pydantic.ValidationError):
        Claim(id="k#c1", axis="G1_label_rich_parity", task="crop_type_mapping",
              dataset="D", model="tessera", baseline=None, metric="f1", value=1.0,
              baseline_value=None, label_ratio=None, direction="better", locator="T1",
              span="a b c", span_sha256="deadbeef")


def test_valid_claim_roundtrips():
    span = "TESSERA reaches 0.9 F1"
    c = Claim(id="k#c1", axis="G1_label_rich_parity", task="crop_type_mapping",
              dataset="D", model="tessera", baseline="task_specific", metric="f1",
              value=0.9, baseline_value=0.8, label_ratio=1.0, direction="better",
              locator="T1", span=span, span_sha256=span_sha256(span))
    assert c.span_sha256 == span_sha256(span)
