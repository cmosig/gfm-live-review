"""Bootstrap host-extractor: run `claude -p` directly on the host (NO container).

This exists ONLY to bootstrap the corpus / verify the pipeline on a machine
where the Docker sandbox is not yet available. It keeps the strongest defence —
an EMPTY tool allowlist, so an injected model can do nothing but emit text — but
drops the container's filesystem/credential/egress isolation. It is opt-in
(`run.py --extractor host`) and prints a warning. Production uses the sandbox.
"""
from __future__ import annotations

import sys

from . import claude_cli


def run_extraction(payload: dict, *, model: str) -> dict:
    """Match the sandbox.run_extraction signature: payload -> extraction JSON."""
    print("WARNING: host extractor active (no container isolation). "
          "Bootstrap use only.", file=sys.stderr)
    return claude_cli.run_prompt(payload["prompt"], model=model)
