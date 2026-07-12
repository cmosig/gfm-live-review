"""Read/write cards as markdown with YAML front-matter.

Front-matter holds the structured fields; the body holds the prose
(``summary`` / ``setup`` / ``caveats``) under stable headings. This keeps a
card human-readable in the GitHub UI and mechanically parseable by the
aggregator. Serialisation is deterministic (sorted keys, fixed section order)
so identical inputs always produce byte-identical files — a prerequisite for
the idempotency guarantee.
"""
from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path

import yaml

from . import config
from .schema import Card

_FM_DELIM = "---"
_BODY_SECTIONS = ("summary", "setup", "caveats")


def _fm_dict(card: Card) -> dict:
    """Structured (non-body) fields as a JSON-round-tripped, sorted dict."""
    data = json.loads(card.model_dump_json())
    for key in _BODY_SECTIONS:
        data.pop(key, None)
    return data


def to_markdown(card: Card) -> str:
    fm = _fm_dict(card)
    front = yaml.safe_dump(fm, sort_keys=True, allow_unicode=True, default_flow_style=False)
    parts = [f"{_FM_DELIM}\n{front}{_FM_DELIM}\n"]
    for section in _BODY_SECTIONS:
        text = getattr(card, section) or ""
        parts.append(f"\n## {section}\n\n{text.strip()}\n")
    return "".join(parts)


def parse_markdown(text: str) -> Card:
    """Inverse of :func:`to_markdown`. Reconstructs and re-validates a Card."""
    if not text.startswith(_FM_DELIM):
        raise ValueError("card missing front-matter delimiter")
    _, fm_block, body = text.split(_FM_DELIM, 2)
    data = yaml.safe_load(fm_block) or {}

    # Recover body sections by their headings.
    sections = {s: "" for s in _BODY_SECTIONS}
    current = None
    buf: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("## ") and stripped[3:].strip() in _BODY_SECTIONS:
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = stripped[3:].strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()

    data.update(sections)
    return Card.model_validate(data)


def card_path(key: str) -> Path:
    """Filesystem path for a card. `key` is schema-validated (no traversal)."""
    # Validate through the schema's key rule before joining into a path.
    if "/" in key or "\\" in key or ".." in key:
        raise ValueError(f"unsafe card key: {key!r}")
    return config.CARDS_DIR / f"{key}.md"


def write_card(card: Card) -> Path:
    config.CARDS_DIR.mkdir(parents=True, exist_ok=True)
    path = card_path(card.key)
    path.write_text(to_markdown(card), encoding="utf-8")
    return path


def load_card(path: Path) -> Card:
    return parse_markdown(path.read_text(encoding="utf-8"))


def load_all_cards() -> list[Card]:
    if not config.CARDS_DIR.exists():
        return []
    cards = []
    for path in sorted(config.CARDS_DIR.glob("*.md")):
        cards.append(load_card(path))
    return cards


# JSON default encoder for date/datetime when we dump state files.
def _json_default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()
    raise TypeError(f"not JSON serialisable: {type(o)}")


def dump_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(obj, indent=2, sort_keys=True, default=_json_default, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )
