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
import re
import shutil
import subprocess

ALLOWED_TOOLS = ""  # MUST stay empty. Asserted before every invocation.
_FENCE_RE = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$", re.MULTILINE)


class ClaudeError(RuntimeError):
    pass


class QuotaExhausted(RuntimeError):
    """Subscription quota/auth problem — not a crash. Callers stop cleanly."""


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
    proc = subprocess.run(
        ["claude", "-p", "--output-format", "json", "--model", model,
         "--max-turns", "2", "--allowedTools", ALLOWED_TOOLS],
        input=prompt, capture_output=True, text=True, timeout=timeout,
    )
    if proc.returncode != 0:
        stderr = (proc.stderr or "").lower()
        if any(t in stderr for t in ("unauthenticated", "not logged in", "quota",
                                     "credit", "rate limit", "usage limit")):
            raise QuotaExhausted(proc.stderr[-500:])
        raise ClaudeError(f"claude failed ({proc.returncode}): {proc.stderr[-500:]}")
    envelope = json.loads(proc.stdout)
    if envelope.get("is_error"):
        raise ClaudeError(f"claude reported error: {envelope.get('result')}")
    return extract_json_object(envelope.get("result", ""))


def run_prompt(prompt: str, *, model: str) -> dict:
    """Call the CLI, retrying once with a stricter JSON reminder."""
    try:
        return call(prompt, model=model)
    except (ValueError, json.JSONDecodeError):
        return call(prompt, model=model, strict_reminder=True)
