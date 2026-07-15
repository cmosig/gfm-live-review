"""A paper whose source 404s forever must be retired, not re-fetched every run.

Backfill accepts ids that turn out to be withdrawn or simply wrong; their arXiv
HTML and PDF both 404. Before this, such a paper was never marked seen, so every
run re-fetched the same dead URL indefinitely. Permanent (non-transient) fetch
failures now mark the paper seen; transient ones (network/429/5xx) still bubble
up unseen so the next run retries them.
"""
from __future__ import annotations

from datetime import date

import pytest

from pipeline import http, run, state, verify
from pipeline.ingest import Candidate


class FakeResp:
    def __init__(self, status_code, url="http://x"):
        self.status_code = status_code
        self.url = url


def test_http_classifies_404_permanent(monkeypatch):
    monkeypatch.setattr(http.time, "sleep", lambda *_: None)
    monkeypatch.setattr(http.requests, "get", lambda *a, **k: FakeResp(404))
    with pytest.raises(http.HttpError) as exc:
        http.get("http://x", retries=2)
    assert exc.value.status_code == 404
    assert exc.value.transient is False


def test_http_classifies_503_transient(monkeypatch):
    monkeypatch.setattr(http.time, "sleep", lambda *_: None)
    monkeypatch.setattr(http.requests, "get", lambda *a, **k: FakeResp(503))
    with pytest.raises(http.HttpError) as exc:
        http.get("http://x", retries=2)
    assert exc.value.transient is True  # retried to exhaustion, still transient


def _vr(arxiv_id="2402.11070"):
    cand = Candidate(title="A withdrawn paper", abstract="", authors=["X"],
                     arxiv_id=arxiv_id, date=date(2024, 2, 1))
    return verify.VerifyResult(candidate=cand, doi=None, doi_status="no_doi_found",
                               is_duplicate=False, duplicate_of=None,
                               self_evaluation=False)


def _boom(transient):
    def _f(_arxiv_id):
        raise http.HttpError("404 for x", status_code=404, transient=transient)
    return _f


def test_permanent_fetch_failure_retires_paper(iso, monkeypatch):
    monkeypatch.setattr("pipeline.fetchtext.fetch_arxiv_text", _boom(transient=False))
    seen: dict = {}
    status = run.process_paper(_vr(), run_fn=lambda *a, **k: None, seen=seen,
                               existing_keys=set(), model="claude-sonnet-5")
    assert status.startswith("skip:source_unavailable")
    assert seen  # the paper was marked seen so it will not be re-fetched
    assert next(iter(seen.values()))["status"] == "source_unavailable"


def test_transient_fetch_failure_leaves_paper_unseen(iso, monkeypatch):
    monkeypatch.setattr("pipeline.fetchtext.fetch_arxiv_text", _boom(transient=True))
    seen: dict = {}
    with pytest.raises(http.HttpError):
        run.process_paper(_vr(), run_fn=lambda *a, **k: None, seen=seen,
                          existing_keys=set(), model="claude-sonnet-5")
    assert seen == {}  # untouched -> retried next run
