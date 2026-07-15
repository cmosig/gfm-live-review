"""The usage gates read REAL subscription percentages — and fail closed.

The pipeline must never fetch usage itself (that would need a credential and the
Anthropic host, which tests/test_no_api.py forbids). It execs an external probe
and reads two numbers. The property that matters most here: if usage cannot be
measured, we REFUSE TO SPEND. "Unknown" must never be optimistically read as
"plenty of headroom left".
"""
from __future__ import annotations

import json

import pytest

from pipeline import usage


@pytest.fixture(autouse=True)
def _no_backoff_sleep(monkeypatch):
    """Make probe-retry backoff instant so failure tests don't wait ~24s each."""
    monkeypatch.setattr(usage.time, "sleep", lambda *_: None)


def _probe(monkeypatch, script: str):
    """Point GFM_USAGE_CMD at an inline python probe."""
    monkeypatch.setenv("GFM_USAGE_CMD", f"python3 -c {json.dumps(script)}")


def test_reads_real_percentages(monkeypatch):
    _probe(monkeypatch, 'print(\'{"session_pct": 34.0, "weekly_pct": 81.5}\')')
    u = usage.fetch()
    assert u.session_pct == 34.0
    assert u.weekly_pct == 81.5


def test_probe_failure_raises_rather_than_returning_zero(monkeypatch):
    """A non-zero exit must NOT come back as 0% used."""
    _probe(monkeypatch, 'import sys; sys.stderr.write("boom"); sys.exit(2)')
    with pytest.raises(usage.UsageUnavailable):
        usage.fetch()


def test_garbage_output_raises(monkeypatch):
    _probe(monkeypatch, 'print("not json")')
    with pytest.raises(usage.UsageUnavailable):
        usage.fetch()


def test_missing_probe_raises(monkeypatch):
    monkeypatch.setenv("GFM_USAGE_CMD", "definitely-not-a-real-binary-xyz")
    with pytest.raises(usage.UsageUnavailable):
        usage.fetch()


def test_transient_failure_is_retried_then_succeeds(monkeypatch, tmp_path):
    """A 429 on the first probe must be retried, not treated as unavailable."""
    counter = tmp_path / "n"
    counter.write_text("0")
    # The probe fails (exit 2) on its first call and succeeds on the second,
    # driven by a counter file so each exec is independent.
    script = (
        "import pathlib,sys;"
        f"p=pathlib.Path({json.dumps(str(counter))});"
        "n=int(p.read_text());p.write_text(str(n+1));"
        "sys.exit(2) if n==0 else print('{\"session_pct\": 12.0, \"weekly_pct\": 20.0}')"
    )
    _probe(monkeypatch, script)
    u = usage.fetch()
    assert u.session_pct == 12.0
    assert counter.read_text() == "2"  # failed once, retried, succeeded


def test_persistent_failure_gives_up_after_retries(monkeypatch):
    _probe(monkeypatch, 'import sys; sys.exit(2)')
    with pytest.raises(usage.UsageUnavailable) as exc:
        usage.fetch(retries=2)
    assert "after 2 attempts" in str(exc.value)


def test_partial_output_raises(monkeypatch):
    _probe(monkeypatch, 'print(\'{"session_pct": 10.0}\')')
    with pytest.raises(usage.UsageUnavailable):
        usage.fetch()


# --- the gates themselves -----------------------------------------------------

def _run(monkeypatch, iso, **kw):
    """Run the pipeline with ingestion stubbed out — we only exercise the gates."""
    from pipeline import ingest, run as run_mod
    monkeypatch.setattr(ingest, "fetch_arxiv_recent", lambda: [])
    monkeypatch.setattr(ingest, "fetch_openalex_recent", lambda *a, **k: [])
    monkeypatch.setattr(run_mod, "publish", lambda **k: 0)
    defaults = dict(seed=False, extractor="host", egress_mode="none", push=False,
                    use_git=False, limit=None)
    return run_mod.run(**{**defaults, **kw})


def test_weekly_gate_refuses_to_start(monkeypatch, iso, capsys):
    _probe(monkeypatch, 'print(\'{"session_pct": 5.0, "weekly_pct": 80.0}\')')
    called = []
    from pipeline import ingest
    monkeypatch.setattr(ingest, "fetch_arxiv_recent", lambda: called.append(1) or [])

    _run(monkeypatch, iso, skip_weekly_above=80.0)
    assert "not running today" in capsys.readouterr().err
    assert not called, "ingestion must not even start when the weekly gate trips"


def test_weekly_gate_allows_below_threshold(monkeypatch, iso, capsys):
    _probe(monkeypatch, 'print(\'{"session_pct": 5.0, "weekly_pct": 79.9}\')')
    _run(monkeypatch, iso, skip_weekly_above=80.0)
    assert "not running today" not in capsys.readouterr().err


def test_session_gate_refuses_when_already_over(monkeypatch, iso, capsys):
    _probe(monkeypatch, 'print(\'{"session_pct": 50.0, "weekly_pct": 10.0}\')')
    _run(monkeypatch, iso, max_session_pct=50.0)
    assert "nothing to do" in capsys.readouterr().err


def test_unreadable_usage_refuses_to_run(monkeypatch, iso, capsys):
    """The fail-closed property, end to end: no usage -> no spending."""
    monkeypatch.setenv("GFM_USAGE_CMD", "definitely-not-a-real-binary-xyz")
    called = []
    from pipeline import ingest
    monkeypatch.setattr(ingest, "fetch_arxiv_recent", lambda: called.append(1) or [])

    _run(monkeypatch, iso, max_session_pct=50.0, skip_weekly_above=80.0)
    assert "REFUSING TO RUN" in capsys.readouterr().err
    assert not called


def test_no_gates_means_no_probe_needed(monkeypatch, iso):
    """Without the flags the probe is never consulted (manual runs stay simple)."""
    monkeypatch.setenv("GFM_USAGE_CMD", "definitely-not-a-real-binary-xyz")
    assert _run(monkeypatch, iso) == 0  # would raise if the probe were called
