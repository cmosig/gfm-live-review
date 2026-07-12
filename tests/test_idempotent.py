"""Two runs over the same cards -> byte-identical data.json, zero new cards (§10)."""
from __future__ import annotations

from pipeline import cards as cards_mod
from pipeline.build import build
from tests.conftest import make_card, make_claim


def _seed_cards():
    for i in range(3):
        cards_mod.write_card(make_card(
            f"paper{i}", claims=[make_claim(f"paper{i}", 1, direction="better")]))


def test_data_json_is_byte_identical_across_runs(iso):
    _seed_cards()
    n_before = len(list(iso.glob("cards/*.md")))

    build(quarantine_count=0)
    first = (iso / "site" / "data.json").read_bytes()

    build(quarantine_count=0)
    second = (iso / "site" / "data.json").read_bytes()

    assert first == second, "data.json must be deterministic across runs"
    assert len(list(iso.glob("cards/*.md"))) == n_before, "build must not create cards"


def test_index_html_is_byte_identical_across_runs(iso):
    _seed_cards()
    build(quarantine_count=0)
    first = (iso / "site" / "index.html").read_bytes()
    build(quarantine_count=0)
    second = (iso / "site" / "index.html").read_bytes()
    assert first == second
