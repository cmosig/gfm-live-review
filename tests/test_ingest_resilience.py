"""A transient arXiv failure must never crash a run.

arXiv rate-limits (HTTP 429) the query endpoint. Before, one failing query
raised out of the whole backfill sweep and the exception propagated to a
non-zero exit — which, on the nightly, shows up as a systemd "failed" unit for
what is only a transient upstream hiccup. Ingest is now best-effort per query,
with a clean top-level skip if it fails entirely.
"""
from __future__ import annotations

import pytest

from pipeline import http, ingest, run as run_mod
from pipeline.ingest import Candidate


def test_backfill_skips_a_failing_query_and_keeps_the_rest(monkeypatch):
    monkeypatch.setattr(http, "courtesy_sleep", lambda: None)
    calls = {"n": 0}

    def fake_page(q, *, start, max_results):
        calls["n"] += 1
        if calls["n"] == 1:  # first query 429s
            raise http.HttpError("429 for arxiv", status_code=429, transient=True)
        # one short page (<50) so pagination stops after it
        return [Candidate(title=f"P{calls['n']}", abstract="",
                          arxiv_id=f"2500.{calls['n']:05d}")]

    monkeypatch.setattr(ingest, "_arxiv_search_page", fake_page)
    out = ingest.fetch_arxiv_backfill()
    assert out, "later queries' results must survive one query failing"
    assert calls["n"] > 1  # it did not stop at the first failure


def test_run_survives_total_ingest_failure(iso, monkeypatch):
    def boom():
        raise http.HttpError("arxiv unreachable", transient=True)

    monkeypatch.setattr(ingest, "fetch_arxiv_backfill", boom)
    rc = run_mod.run(seed=False, extractor="host", egress_mode="none", push=False,
                     use_git=False, limit=None, backfill=True)
    assert rc == 0  # clean skip, not a crash / non-zero exit


def test_daily_sweep_skips_a_failing_query(monkeypatch):
    monkeypatch.setattr(http, "courtesy_sleep", lambda: None)
    calls = {"n": 0}

    def fake_search(query, *, max_results):
        calls["n"] += 1
        if calls["n"] == 1:
            raise http.HttpError("429 for arxiv", status_code=429, transient=True)
        return [Candidate(title=f"D{calls['n']}", abstract="",
                          arxiv_id=f"2501.{calls['n']:05d}")]

    monkeypatch.setattr(ingest, "fetch_arxiv_search", fake_search)
    out = ingest.fetch_arxiv_recent()
    assert out
    assert calls["n"] > 1
