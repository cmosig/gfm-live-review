"""Benchmark grouping: fold dataset spellings, never fold away the evidence."""
from __future__ import annotations

from pipeline import aggregate
from tests.conftest import make_card, make_claim


def _bench(view, name):
    return next(b for b in view if b["name"] == name)


def test_variants_of_one_benchmark_are_grouped():
    """Splits/sensors of the same benchmark must land in one group, so that two
    papers running Sen1Floods11 are actually comparable."""
    cards = [
        make_card("a2025x", claims=[make_claim("a2025x", 1, dataset="Sen1Floods11")]),
        make_card("b2025x", claims=[make_claim("b2025x", 1, dataset="Sen1Floods11 Bolivia")]),
        make_card("c2025x", claims=[make_claim("c2025x", 1, dataset="Sen1Floods11 (unseen Bolivia)")]),
    ]
    view = aggregate.benchmark_view(aggregate.flatten(cards))
    assert len(view) == 1
    b = view[0]
    assert b["name"] == "Sen1Floods11"
    assert b["n_papers"] == 3
    # The exact strings the papers used are preserved, never rewritten.
    assert len(b["variants"]) == 3
    assert "Sen1Floods11 Bolivia" in b["variants"]


def test_unrelated_benchmarks_are_not_merged():
    cards = [
        make_card("a2025x", claims=[make_claim("a2025x", 1, dataset="EuroSAT")]),
        make_card("b2025x", claims=[make_claim("b2025x", 1, dataset="EuroCrops")]),
    ]
    view = aggregate.benchmark_view(aggregate.flatten(cards))
    assert {b["name"] for b in view} == {"EuroSAT", "EuroCrops"}


def test_display_name_drops_qualifiers():
    cards = [make_card("a2025x", claims=[
        make_claim("a2025x", 1, dataset="JECAM Senegal (2018, 5 crops)"),
        make_claim("a2025x", 2, dataset="JECAM Senegal (2019, 5 crops)"),
    ])]
    view = aggregate.benchmark_view(aggregate.flatten(cards))
    assert view[0]["name"] == "JECAM Senegal"


def test_verdict_uses_only_vs_task_specific_claims():
    """A benchmark where every claim is model-vs-model has no verdict to give."""
    cards = [make_card("a2025x", claims=[
        make_claim("a2025x", 1, dataset="EuroSAT", baseline="prithvi", direction="better")])]
    view = aggregate.benchmark_view(aggregate.flatten(cards))
    b = _bench(view, "EuroSAT")
    assert b["n_vs_task_specific"] == 0
    assert b["verdict"]["label"] == "gap"
    assert b["verdict"]["direction"] is None
    assert b["n_claims"] == 1  # but the claim is still shown


def test_contested_within_one_benchmark():
    """Same dataset, papers disagree -> a real disagreement, not a data artefact."""
    dirs = ["better", "better", "worse", "worse"]
    cards = [make_card(f"p{i}2025x", claims=[
        make_claim(f"p{i}2025x", 1, dataset="Sen1Floods11", direction=d)])
        for i, d in enumerate(dirs)]
    view = aggregate.benchmark_view(aggregate.flatten(cards))
    assert view[0]["verdict"]["label"] == "contested"
    assert view[0]["n_papers"] == 4


def test_most_evaluated_benchmark_sorts_first():
    cards = [
        make_card("a2025x", claims=[make_claim("a2025x", 1, dataset="Sen1Floods11")]),
        make_card("b2025x", claims=[make_claim("b2025x", 1, dataset="Sen1Floods11")]),
        make_card("c2025x", claims=[make_claim("c2025x", 1, dataset="EuroSAT")]),
    ]
    view = aggregate.benchmark_view(aggregate.flatten(cards))
    assert view[0]["name"] == "Sen1Floods11"
    assert view[0]["n_papers"] == 2
