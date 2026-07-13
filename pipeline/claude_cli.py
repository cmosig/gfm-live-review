"""Shared wrapper around the Claude Code CLI (`claude -p`).

Subscription-only: no API key is read or passed anywhere. The CLI inherits the
local login. Used by the bootstrap host-extractor (pipeline/hostextract.py); the
container's entrypoint carries its own tiny copy of this logic because it cannot
import the `pipeline` package (the repo is deliberately not mounted).

The tool allowlist is EMPTY: even a perfect prompt injection has no tool to act
with, so the model can only emit text.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess

ALLOWED_TOOLS = ""  # MUST stay empty. Asserted before every invocation.
# Reasoning effort for the extraction call. Default "low": paper reading is a
# structured-extraction task, not open-ended reasoning, and the CLI's default
# extended thinking dominates per-paper latency. Override via GFM_EFFORT.
DEFAULT_EFFORT = "low"
_FENCE_RE = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$", re.MULTILINE)

# `claude -p --output-format json` reports API-level failures by exiting non-zero
# with an EMPTY stderr and the human-readable reason on stdout, inside the result
# envelope ({"is_error": true, "api_error_status": 429, "result": "<reason>"}).
# Classification must therefore read stdout; reading stderr sees nothing at all.
_QUOTA_TOKENS = ("unauthenticated", "not logged in", "quota", "credit",
                 "rate limit", "usage limit", "out of", "upgrade")
_QUOTA_STATUSES = (401, 403, 429)


class ClaudeError(RuntimeError):
    """Transport/API failure. NOT the paper's fault — never quarantine on it."""


class QuotaExhausted(RuntimeError):
    """Subscription quota/auth problem — not a crash. Callers stop cleanly."""


# Cumulative USD the CLI has reported for this process. The subscription is not
# billed per call, but the figure is the only usage signal the CLI exposes, so
# run.py uses it as the budget meter.
_cost_usd = 0.0


def cost_usd() -> float:
    return _cost_usd


def extract_json_object(text: str) -> dict:
    """Pull the first balanced JSON object out of (possibly chatty) text."""
    text = _FENCE_RE.sub("", text).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    if start == -1:
        raise ValueError("no JSON object in model output")
    depth, in_str, esc = 0, False, False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        elif ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("unbalanced JSON object in model output")


def call(prompt: str, *, model: str, timeout: int = 300,
         strict_reminder: bool = False) -> dict:
    assert ALLOWED_TOOLS == "", "tool allowlist must be empty"
    if not shutil.which("claude"):
        raise ClaudeError("claude CLI not found; extraction is subscription-only")
    if strict_reminder:
        prompt += ("\n\nIMPORTANT: your previous reply was not valid JSON. "
                   "Reply with ONLY the JSON object, no prose, no fences.")
    effort = os.environ.get("GFM_EFFORT", DEFAULT_EFFORT)
    cmd = ["claude", "-p", "--output-format", "json", "--model", model,
           "--max-turns", "2", "--allowedTools", ALLOWED_TOOLS]
    if effort:
        cmd += ["--effort", effort]
    proc = subprocess.run(
        cmd, input=prompt, capture_output=True, text=True, timeout=timeout,
    )
    try:
        envelope = json.loads(proc.stdout)
    except (json.JSONDecodeError, ValueError):
        envelope = {}

    global _cost_usd
    _cost_usd += float(envelope.get("total_cost_usd") or 0.0)

    if proc.returncode != 0 or envelope.get("is_error"):
        # The reason lives on stdout; stderr is a last resort for a CLI that died
        # before it could emit an envelope at all (e.g. a bad flag).
        reason = str(envelope.get("result") or proc.stderr or "").strip()
        status = envelope.get("api_error_status")
        if status in _QUOTA_STATUSES or any(t in reason.lower() for t in _QUOTA_TOKENS):
            raise QuotaExhausted(f"{status or proc.returncode}: {reason[-500:]}")
        raise ClaudeError(
            f"claude failed (exit {proc.returncode}, api {status}): {reason[-500:]}")
    return extract_json_object(envelope.get("result", ""))


def run_prompt(prompt: str, *, model: str) -> dict:
    """Call the CLI, retrying once with a stricter JSON reminder."""
    try:
        return call(prompt, model=model)
    except (ValueError, json.JSONDecodeError):
        return call(prompt, model=model, strict_reminder=True)
