"""Real subscription usage, read from an external probe.

The §5 no-API guard (tests/test_no_api.py) forbids this repo from naming the
Anthropic API host or reading credentials — that property is the whole point of
the project. So the pipeline does not fetch usage itself. It execs an operator-
supplied probe (``GFM_USAGE_CMD``, default ``gfm-usage-probe``) whose only
contract is to print one JSON object:

    {"session_pct": 35.0, "weekly_pct": 35.0}

session_pct is the rolling 5-hour window, weekly_pct the 7-day one — the same
numbers the ``/usage`` screen shows. Where the probe gets them is deliberately
none of this repo's business: no credential ever passes through this file.

Usage is a GATE, never a fallback: if the probe fails, callers must refuse to
spend rather than assume there is headroom (`UsageUnavailable`).
"""
from __future__ import annotations

import json
import os
import shlex
import subprocess
from dataclasses import dataclass

DEFAULT_PROBE = "gfm-usage-probe"
PROBE_TIMEOUT = 180  # generous: the probe may refresh a stale token first


class UsageUnavailable(RuntimeError):
    """The probe could not tell us the usage. Never treat this as 'plenty left'."""


@dataclass(frozen=True)
class Usage:
    session_pct: float  # rolling 5-hour window
    weekly_pct: float   # rolling 7-day window

    def __str__(self) -> str:
        return f"session {self.session_pct:.0f}% · weekly {self.weekly_pct:.0f}%"


def probe_cmd() -> list[str]:
    return shlex.split(os.environ.get("GFM_USAGE_CMD") or DEFAULT_PROBE)


def fetch() -> Usage:
    cmd = probe_cmd()
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              timeout=PROBE_TIMEOUT, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise UsageUnavailable(f"usage probe {cmd[0]!r} failed: {exc}") from exc
    if proc.returncode != 0:
        raise UsageUnavailable(
            f"usage probe exited {proc.returncode}: {(proc.stderr or '').strip()[-300:]}")
    try:
        data = json.loads(proc.stdout)
        return Usage(session_pct=float(data["session_pct"]),
                     weekly_pct=float(data["weekly_pct"]))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        raise UsageUnavailable(f"usage probe returned unusable output: {exc}") from exc
