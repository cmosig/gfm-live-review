"""Quarantine failed extractions WITH the offending payload, for forensics.

A quarantined paper is the outside-visible signature of a failed extraction —
schema violation, span-verification collapse, key sanitisation failure. The
payload is committed alongside the error so a spike in quarantines (what an
attack looks like from the outside) is inspectable, not just a number.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from . import config

_SAFE = re.compile(r"[^a-z0-9_-]")


def _safe_name(key: str) -> str:
    """Sanitise ANY string into a path-safe quarantine filename.

    Quarantine can be triggered by adversarial data, so we never trust the key
    here: strip everything but [a-z0-9_-], collapse, and bound length. A
    `../../x` key becomes `x`; an empty result becomes `unknown`.
    """
    name = _SAFE.sub("", key.lower().replace("/", "").replace("..", ""))
    return name[:64] or "unknown"


def write(key: str, *, title: str, reason: str, payload: dict,
          extra: dict | None = None) -> Path:
    config.QUARANTINE_DIR.mkdir(parents=True, exist_ok=True)
    record = {
        "key": key,
        "title": title,
        "reason": reason,
        "quarantined_at": datetime.now(timezone.utc).isoformat(),
        "payload": payload,
        **(extra or {}),
    }
    path = config.QUARANTINE_DIR / f"{_safe_name(key)}.json"
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def count() -> int:
    if not config.QUARANTINE_DIR.exists():
        return 0
    return sum(1 for _ in config.QUARANTINE_DIR.glob("*.json"))


def load_all() -> list[dict]:
    if not config.QUARANTINE_DIR.exists():
        return []
    out = []
    for p in sorted(config.QUARANTINE_DIR.glob("*.json")):
        try:
            out.append(json.loads(p.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            continue
    return out
