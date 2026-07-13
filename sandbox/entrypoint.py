#!/usr/bin/env python3
"""Runs INSIDE the extraction container. Reads a payload on stdin, prints JSON.

The interface is deliberately tiny: stdin in (a pre-built prompt), stdout out
(one JSON object), nothing else. The host builds the prompt; this process only
shells out to the Claude Code CLI (`claude -p`) with an EMPTY tool allowlist, so
the model can only emit text — no Bash/Read/Write/WebFetch to act on any
injected instruction. Credentials arrive read-only under /creds and are copied
into a writable tmpfs HOME so the CLI can run.

No API key is read anywhere. Self-contained by necessity: the `pipeline` package
is deliberately NOT mounted, so this cannot import it.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

MODEL = os.environ.get("GFM_MODEL", "claude-opus-4-8")
ALLOWED_TOOLS = os.environ.get("GFM_ALLOWED_TOOLS", "")  # must be empty
_FENCE_RE = re.compile(r"^\s*```(?:json)?\s*|\s*```\s*$", re.MULTILINE)


def _die(msg: str, code: int = 2) -> None:
    print(msg, file=sys.stderr)
    sys.exit(code)


def _setup_home(credentials: dict) -> None:
    """Write subscription credentials (received on stdin) into a tmpfs HOME.

    Nothing is mounted; the credentials arrived over the private stdin pipe and
    live only in this container's ephemeral tmpfs.
    """
    home = Path("/tmp/home")
    claude_dir = home / ".claude"
    claude_dir.mkdir(parents=True, exist_ok=True)
    if "credentials.json" not in credentials:
        _die("FATAL: no Claude credentials provided on stdin", code=3)
    cred_path = claude_dir / ".credentials.json"
    cred_path.write_text(credentials["credentials.json"], encoding="utf-8")
    cred_path.chmod(0o600)
    if "claude.json" in credentials:
        (home / ".claude.json").write_text(credentials["claude.json"], encoding="utf-8")
    os.environ["HOME"] = str(home)


def _extract_json_object(text: str) -> dict:
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


def _call_claude(prompt: str, *, strict_reminder: bool = False) -> dict:
    if strict_reminder:
        prompt += ("\n\nIMPORTANT: your previous reply was not valid JSON. "
                   "Reply with ONLY the JSON object, no prose, no fences.")
    cmd = ["claude", "-p", "--output-format", "json", "--model", MODEL,
           "--max-turns", "2", "--allowedTools", ALLOWED_TOOLS]
    effort = os.environ.get("GFM_EFFORT", "low")
    if effort:
        cmd += ["--effort", effort]
    proc = subprocess.run(
        cmd, input=prompt, capture_output=True, text=True, timeout=300,
    )
    # The CLI reports API failures by exiting non-zero with an EMPTY stderr and
    # the reason on stdout in the result envelope. Classify from stdout; stderr
    # only carries a CLI that died before emitting an envelope (e.g. a bad flag).
    try:
        envelope = json.loads(proc.stdout)
    except (json.JSONDecodeError, ValueError):
        envelope = {}
    if proc.returncode != 0 or envelope.get("is_error"):
        reason = str(envelope.get("result") or proc.stderr or "").strip()
        status = envelope.get("api_error_status")
        if status in (401, 403, 429) or any(
            t in reason.lower() for t in ("unauthenticated", "login", "quota",
                                          "credit", "usage limit", "rate limit",
                                          "out of", "upgrade")):
            _die(f"QUOTA/AUTH: {status or proc.returncode}: {reason[-500:]}", code=3)
        _die(f"FATAL: claude CLI failed (exit {proc.returncode}, api {status}): "
             f"{reason[-500:]}", code=4)
    return _extract_json_object(envelope.get("result", ""))


def main() -> None:
    if ALLOWED_TOOLS != "":
        _die("FATAL: extractor tool allowlist is not empty; refusing to run.")
    if not shutil.which("claude"):
        _die("FATAL: claude CLI not found in container.", code=4)

    payload = json.load(sys.stdin)
    _setup_home(payload.pop("_credentials", {}))
    prompt = payload["prompt"]
    try:
        obj = _call_claude(prompt)
    except (ValueError, json.JSONDecodeError):
        obj = _call_claude(prompt, strict_reminder=True)
    print(json.dumps(obj))


if __name__ == "__main__":
    main()
