"""DOI resolution paths against saved Crossref-shaped fixtures (§10)."""
from __future__ import annotations

from datetime import date

import pytest

from pipeline import http, verify
from pipeline.ingest import Candidate


def _cand(title="TESSERA: A Foundation Model for Earth Observation", doi="10.1234/tessera"):
    return Candidate(title=title, abstract="", authors=["Feng"], arxiv_id="2506.20380",
                     doi=doi, date=date(2025, 6, 26))


def test_verified_on_title_match():
    def fetch(doi):
        return {"title": ["TESSERA: A Foundation Model for Earth Observation"]}
    doi, status = verify.resolve_doi(_cand(), fetch=fetch)
    assert status == "verified" and doi == "10.1234/tessera"


def test_mismatch_on_title_divergence():
    def fetch(doi):
        return {"title": ["An Unrelated Paper About Cats And Dogs"]}
    _, status = verify.resolve_doi(_cand(), fetch=fetch)
    assert status == "mismatch"


def test_unresolved_on_api_error():
    def fetch(doi):
        raise http.HttpError("503")
    _, status = verify.resolve_doi(_cand(), fetch=fetch)
    assert status == "unresolved"


def test_unresolved_when_crossref_has_no_title():
    def fetch(doi):
        return {"title": []}
    _, status = verify.resolve_doi(_cand(), fetch=fetch)
    assert status == "unresolved"


def test_no_doi_found_when_metadata_lacks_doi():
    doi, status = verify.resolve_doi(_cand(doi=None))
    assert status == "no_doi_found" and doi is None


def test_self_evaluation_detected_for_model_own_paper():
    # TESSERA's own arXiv id is tracked in models.yaml.
    assert verify.detect_self_evaluation(_cand()) is True


def test_self_evaluation_false_for_downstream_paper():
    c = Candidate(title="Downstream use of embeddings", abstract="", arxiv_id="2601.00857",
                  date=date(2026, 1, 1))
    assert verify.detect_self_evaluation(c) is False


def test_verify_marks_duplicates():
    from pipeline import state
    c = _cand()
    seen = {}
    state.mark_seen(seen, title=c.title, key="feng2025tessera", status="carded")
    vr = verify.verify(c, seen, set(), fetch=lambda doi: {"title": [c.title]})
    assert vr.is_duplicate and vr.duplicate_of == "feng2025tessera"
