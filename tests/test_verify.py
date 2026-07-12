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


def test_arxiv_datacite_doi_derived_when_no_journal_doi():
    # Every arXiv paper has a deterministic DataCite DOI: 10.48550/arXiv.<id>.
    doi, status = verify.resolve_doi(_cand(doi=None))
    assert doi == "10.48550/arxiv.2506.20380" and status == "verified"


def test_no_doi_found_when_no_doi_and_no_arxiv():
    c = Candidate(title="A journal-only paper", abstract="", doi=None, arxiv_id=None)
    doi, status = verify.resolve_doi(c)
    assert status == "no_doi_found" and doi is None


def test_self_evaluation_detected_for_model_own_paper():
    # TESSERA's own arXiv id is tracked in models.yaml.
    assert verify.detect_self_evaluation(_cand()) is True


def _model_authors():
    return {"tessera": {verify._norm_author("Clement Atzberger")},
            "alphaearth": {verify._norm_author("Chenhui Zhang")}}


def test_self_eval_resolver_true_on_author_overlap():
    assert verify.resolve_self_evaluation(
        arxiv_id="2611.11111", authors=["Htet Yamin Ko Ko", "Clement Atzberger"],
        evaluated_models=["tessera"], llm_flag=False,
        model_authors=_model_authors()) is True


def test_self_eval_resolver_ignores_llm_flag_when_check_is_computable():
    # LLM said True (e.g. "authors built their own downstream method"), but no
    # author overlap with the model's defining paper -> False wins.
    assert verify.resolve_self_evaluation(
        arxiv_id="2602.17250", authors=["Alireza Hamoudzadeh", "Roberta Ravanelli"],
        evaluated_models=["alphaearth"], llm_flag=True,
        model_authors=_model_authors()) is False


def test_self_eval_resolver_full_name_not_surname_initial():
    # "Chi Zhang" (hydrology) must NOT match "Chenhui Zhang" (model author).
    assert verify.resolve_self_evaluation(
        arxiv_id="2601.01558", authors=["Pengfei Qu", "Chi Zhang"],
        evaluated_models=["alphaearth"], llm_flag=False,
        model_authors=_model_authors()) is False


def test_self_eval_resolver_falls_back_to_llm_for_unknown_models():
    # No defining-paper author list for this model -> the extractor's flag holds.
    assert verify.resolve_self_evaluation(
        arxiv_id="2699.00001", authors=["Someone Else"],
        evaluated_models=["prithvi"], llm_flag=True,
        model_authors=_model_authors()) is True


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
