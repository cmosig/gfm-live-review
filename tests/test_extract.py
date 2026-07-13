"""Extraction orchestration with the model fully mocked (§10).

No subprocess, no docker, no claude — `run_fn` is injected.
"""
from __future__ import annotations

from datetime import date

import pytest

from pipeline import claude_cli, extract
from pipeline.claude_cli import QuotaExhausted

PAPER = ("TESSERA attains 0.91 F1 on the PASTIS benchmark for crop mapping. "
         "On the EuroSAT dataset it reaches 0.88 accuracy. "
         "Transfer to unseen regions degrades performance noticeably.")

META = extract.PaperMeta(key="feng2025tessera", title="TESSERA", date=date(2025, 6, 26),
                         authors=["Feng"], arxiv_id="2506.20380")


def _claim(span, **kw):
    base = {"axis": "G1_label_rich_parity", "task": "crop_type_mapping",
            "dataset": "PASTIS", "model": "tessera", "baseline": "task_specific",
            "metric": "f1", "value": 0.91, "baseline_value": 0.85, "label_ratio": 1.0,
            "direction": "better", "locator": "Table 1", "span": span}
    base.update(kw)
    return base


def test_fabricated_span_is_dropped():
    def run_fn(payload, model):
        return {"claims": [
            _claim("TESSERA attains 0.91 F1 on the PASTIS benchmark"),       # real
            _claim("TESSERA attains 0.99 F1 on a benchmark that does not exist"),  # fake
        ], "summary": "s"}
    res = extract.extract_card(META, PAPER, run_fn=run_fn)
    assert not res.quarantined
    assert res.dropped_claims == 1
    assert len(res.card.claims) == 1


def test_majority_fabricated_spans_quarantined():
    def run_fn(payload, model):
        return {"claims": [
            _claim("TESSERA attains 0.91 F1 on the PASTIS benchmark"),       # real
            _claim("fabricated one about nothing at all here"),              # fake
            _claim("fabricated two also nowhere in the paper text"),        # fake
        ], "summary": "s"}
    res = extract.extract_card(META, PAPER, run_fn=run_fn)
    assert res.quarantined
    assert "claim verification failed" in res.reason


def test_span_hash_is_computed_in_python():
    def run_fn(payload, model):
        return {"claims": [_claim("On the EuroSAT dataset it reaches 0.88 accuracy",
                                  metric="accuracy", value=0.88, dataset="EuroSAT")],
                "summary": "s"}
    res = extract.extract_card(META, PAPER, run_fn=run_fn)
    from pipeline.textutil import span_sha256
    c = res.card.claims[0]
    assert c.span_sha256 == span_sha256(c.span)
    assert c.id == "feng2025tessera#c1"


def test_chatty_output_with_fences_still_parses():
    chatty = ('Sure! Here is the JSON:\n```json\n'
              '{"summary": "hi", "claims": []}\n```\nHope that helps.')
    obj = claude_cli.extract_json_object(chatty)
    assert obj["summary"] == "hi" and obj["claims"] == []


def test_quota_propagates_and_is_not_swallowed():
    def run_fn(payload, model):
        raise QuotaExhausted("usage limit reached")
    with pytest.raises(QuotaExhausted):
        extract.extract_card(META, PAPER, run_fn=run_fn)


def test_claude_cli_detects_quota(monkeypatch):
    class FakeProc:
        returncode = 1
        stdout = ""
        stderr = "Error: usage limit reached for your plan"
    monkeypatch.setattr(claude_cli.subprocess, "run", lambda *a, **k: FakeProc())
    monkeypatch.setattr(claude_cli.shutil, "which", lambda name: "/usr/bin/claude")
    with pytest.raises(QuotaExhausted):
        claude_cli.call("prompt", model="claude-opus-4-8")


def test_llm_doi_smuggle_quarantines():
    def run_fn(payload, model):
        return {"summary": "s", "doi": "10.1/evil", "claims": []}
    res = extract.extract_card(META, PAPER, run_fn=run_fn)
    assert res.quarantined and "schema validation failed" in res.reason
