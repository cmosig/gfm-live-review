"""Render the static dashboard from the committed cards. Pure Python, no LLM.

Output is deterministic: ``data.json`` contains no wall-clock timestamp (only
corpus-derived facts), so identical cards produce byte-identical output — the
idempotency guarantee. The JSON is ALSO embedded into index.html as an inert
``<script type="application/json">`` blob so the page works from ``file://``
with no network calls. All model-derived strings are escaped by app.js via
``textContent`` (never innerHTML); a strict CSP meta tag is shipped as well.
"""
from __future__ import annotations

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from . import config
from .aggregate import aggregate
from .cards import load_all_cards
from .schema import Card

TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "site" / "templates"


def build_data(cards: list[Card], *, quarantine_count: int = 0) -> dict:
    data = aggregate(cards, quarantine_count=quarantine_count)
    # Deterministic, corpus-derived provenance (no wall clock -> idempotent).
    data["corpus_through"] = max((c.date for c in cards), default=None)
    data["corpus_through"] = data["corpus_through"].isoformat() if data["corpus_through"] else None
    return data


def _canonical_json(data: dict) -> str:
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)


def render_site(data: dict) -> None:
    config.SITE_DIR.mkdir(parents=True, exist_ok=True)

    canonical = _canonical_json(data)
    # 1. Standalone data.json (the "one JSON blob").
    (config.SITE_DIR / "data.json").write_text(canonical + "\n", encoding="utf-8")

    # 2. index.html with the same JSON embedded (autoescape on; the blob is
    #    injected as inert JSON via a dedicated, escaped context var).
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html"]),
    )
    template = env.get_template("index.html.j2")
    # Neutralise every '<' as a JSON-valid < escape so the blob can never
    # break out of the <script> element (no </script>, no <!--). JSON.parse
    # decodes it back to '<'. This is why the blob is passed |safe below.
    embedded = canonical.replace("<", "\\u003c")
    html = template.render(embedded_json=embedded)
    (config.SITE_DIR / "index.html").write_text(html, encoding="utf-8")


def build(*, quarantine_count: int = 0) -> dict:
    cards = load_all_cards()
    data = build_data(cards, quarantine_count=quarantine_count)
    render_site(data)
    return data


if __name__ == "__main__":
    from . import quarantine
    build(quarantine_count=quarantine.count())
    print(f"Built site with {len(load_all_cards())} cards -> {config.SITE_DIR}")
