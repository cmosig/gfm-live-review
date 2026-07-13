"""A dead API must never look like a corpus of bad papers.

Regression tests for the failure that quarantined 251 good papers in one run:
`claude -p --output-format json` reports API errors by exiting non-zero with an
EMPTY stderr and the reason on stdout. The old code classified from stderr, so
the quota branch never fired, every error became a generic exception, and
extract.py quarantined the paper — permanently, since run.py then marked it seen.
"""
from __future__ import annotations

import json
import subprocess

import pytest

from pipeline import claude_cli, extract
from pipeline.claude_cli import ClaudeError, QuotaExhausted
from tests.conftest import make_card  # noqa: F401  (keeps fixture import path honest)


class FakeProc:
    def __init__(self, returncode, stdout, stderr=""):
        self.returncode, self.stdout, self.stderr = returncode, stdout, stderr


def _envelope(**kw):
    return json.dumps({"type": "result", "is_error": True, **kw})


def _patch(monkeypatch, proc):
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: proc)


@pytest.mark.parametrize("status,reason", [
    (429, "Claude usage limit reached. Your limit will reset at 3pm."),
    (401, "Unauthenticated: please run /login"),
    (403, "Your credit balance is too low"),
])
def test_quota_errors_on_stdout_raise_quota_exhausted(monkeypatch, status, reason):
    """The exact shape that broke: exit 1, empty stderr, reason on stdout."""
    _patch(monkeypatch, FakeProc(1, _envelope(api_error_status=status, result=reason), ""))
    with pytest.raises(QuotaExhausted):
        claude_cli.call("prompt", model="claude-sonnet-5")


def test_other_api_errors_raise_claude_error_not_a_paper_problem(monkeypatch):
    _patch(monkeypatch, FakeProc(1, _envelope(api_error_status=529, result="Overloaded"), ""))
    with pytest.raises(ClaudeError) as exc:
        claude_cli.call("prompt", model="claude-sonnet-5")
    assert "Overloaded" in str(exc.value)  # the real reason survives, not an empty string


def test_is_error_with_zero_exit_still_raises(monkeypatch):
    """A zero exit with is_error set must not be parsed as a successful result."""
    _patch(monkeypatch, FakeProc(0, _envelope(api_error_status=500, result="boom"), ""))
    with pytest.raises(ClaudeError):
        claude_cli.call("prompt", model="claude-sonnet-5")


def test_transport_failure_never_quarantines_the_paper(monkeypatch):
    """The core invariant: a paper we could not read is NOT a bad paper.

    extract_card must propagate, so run.py leaves it unseen and retries it —
    rather than writing a quarantine file and marking it permanently seen.
    """
    from datetime import date

    meta = extract.PaperMeta(key="x2025y", title="T", date=date(2025, 1, 1),
                             authors=["A"], arxiv_id="1234.5678", doi=None,
                             doi_status="absent", venue=None, self_evaluation=False)

    def dead_api(payload, *, model):
        raise ClaudeError("claude failed (exit 1, api 529): Overloaded")

    with pytest.raises(ClaudeError):
        extract.extract_card(meta, "some paper text", run_fn=dead_api)


def test_quota_still_propagates_from_extract(monkeypatch):
    from datetime import date

    meta = extract.PaperMeta(key="x2025y", title="T", date=date(2025, 1, 1),
                             authors=["A"], arxiv_id="1234.5678", doi=None,
                             doi_status="absent", venue=None, self_evaluation=False)

    def out_of_quota(payload, *, model):
        raise QuotaExhausted("429: usage limit reached")

    with pytest.raises(QuotaExhausted):
        extract.extract_card(meta, "some paper text", run_fn=out_of_quota)
