"""Committed pipeline state: the seen-list, pending tags, and the run log.

All state is plain JSON in ``state/`` so a ``git clone`` fully restores the
system. ``seen.json`` maps a normalised-title key -> minimal record, and is the
crash-safety linchpin: it is only updated *after* a paper is successfully
carded, so an interrupted or quota-exhausted run resumes cleanly tomorrow.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from . import config

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def title_key(title: str) -> str:
    """Normalised dedup key for a title: lowercase, alnum-only, collapsed."""
    return _NON_ALNUM.sub(" ", title.lower()).strip()


def load_seen() -> dict[str, dict]:
    if config.SEEN_PATH.exists():
        return json.loads(config.SEEN_PATH.read_text(encoding="utf-8"))
    return {}


def save_seen(seen: dict[str, dict]) -> None:
    config.STATE_DIR.mkdir(parents=True, exist_ok=True)
    config.SEEN_PATH.write_text(
        json.dumps(seen, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def mark_seen(seen: dict[str, dict], *, title: str, key: str, status: str, **extra) -> None:
    seen[title_key(title)] = {"key": key, "status": status, **extra}


def is_seen(seen: dict[str, dict], title: str) -> bool:
    return title_key(title) in seen


def load_pending_tags() -> dict[str, list[str]]:
    """proposed_tag -> list of paper keys that proposed it (dedup evidence)."""
    if config.PENDING_TAGS_PATH.exists():
        return json.loads(config.PENDING_TAGS_PATH.read_text(encoding="utf-8"))
    return {}


def save_pending_tags(pending: dict[str, list[str]]) -> None:
    config.STATE_DIR.mkdir(parents=True, exist_ok=True)
    config.PENDING_TAGS_PATH.write_text(
        json.dumps(pending, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def append_run(record: dict) -> None:
    """Append one JSON line to the committed run log."""
    config.STATE_DIR.mkdir(parents=True, exist_ok=True)
    record = {"ts": datetime.now(timezone.utc).isoformat(), **record}
    with config.RUNS_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
