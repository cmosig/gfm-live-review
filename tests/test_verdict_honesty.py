"""The headline verdict must not claim more than the evidence supports.

Three failure modes this locks down, all of which the corpus actually exhibited:

  * pooling across datasets can manufacture a "consensus" that the one properly
    replicated benchmark contradicts (flood_mapping pooled to consensus while
    Sen1Floods11, its only benchmark with enough papers, was contested);
  * a verdict can rest on papers whose authors built the model they grade
    (change_detection was "consensus" only until self-evaluations were removed);
  * a diagnostic (linear probing) is not the practitioner's alternative, so it
    is not evidence that a foundation model beats one.
"""
from __future__ import annotations

import pytest

from pipeline import aggregate, config
from tests.conftest import make_card, make_claim


@pytest.fixture(autouse=True)
def _taxonomy(iso):
    """All tests here read the real taxonomy (for diagnostic_tasks)."""
    config.reload_vocab()
    yield


def test_diagnostic_tasks_are_excluded_from_the_headline():
    cards = [
        make_card(f"p{i}2025x", claims=[
            make_claim(f"p{i}2025x", 1, task="representation_probing", direction="better")])
        for i in range(5)
    ]
    rows = aggregate.flatten(cards)
    assert "representation_probing" in config.diagnostic_tasks()
    assert not aggregate.task_verdicts(rows), "probing must not produce a verdict"

    # ...but the results are not thrown away.
    diag = aggregate.diagnostics_view(rows)
    assert len(diag) == 1
    assert diag[0]["task"] == "representation_probing"
    assert diag[0]["n_papers"] == 5


def test_diagnostic_tasks_are_excluded_from_the_matrix():
    cards = [make_card("p2025x", claims=[
        make_claim("p2025x", 1, task="representation_probing")])]
    m = aggregate.matrix_view(aggregate.flatten(cards))
    assert not any(c.get("n_papers") for c in m["cells"]), "probing must not colour a cell"


def test_pooled_consensus_is_flagged_when_its_best_benchmark_is_contested():
    """The flood_mapping shape: 4 papers agree overall, but the one benchmark
    they share disagrees. The verdict must say so."""
    cards = [
        # Three papers on the shared benchmark, disagreeing -> contested there
        # (2 of 3 agree = 67%, under the 80% bar).
        make_card("a2025x", claims=[make_claim("a2025x", 1, dataset="Sen1Floods11", direction="better")]),
        make_card("b2025x", claims=[make_claim("b2025x", 1, dataset="Sen1Floods11", direction="better")]),
        make_card("c2025x", claims=[make_claim("c2025x", 1, dataset="Sen1Floods11", direction="worse")]),
        # Two more agreeing on other datasets. Pooled: 4 of 5 agree = 80% ->
        # consensus, even though the only replicated benchmark says otherwise.
        make_card("d2025x", claims=[make_claim("d2025x", 1, dataset="OtherBench", direction="better")]),
        make_card("e2025x", claims=[make_claim("e2025x", 1, dataset="ThirdBench", direction="better")]),
    ]
    v = aggregate.task_verdicts(aggregate.flatten(cards))[0]
    assert v["label"] == "consensus"
    assert v["strongest_benchmark"]["name"] == "Sen1Floods11"
    assert v["strongest_benchmark"]["label"] == "contested"
    assert v["pooling_note"], "a consensus contradicted by its best benchmark must be flagged"
    assert "contested" in v["pooling_note"]


def test_pooled_consensus_flagged_when_no_benchmark_has_enough_papers():
    """Consensus assembled from papers that share no dataset at all."""
    cards = [make_card(f"p{i}2025x", claims=[
        make_claim(f"p{i}2025x", 1, dataset=f"Bench{i}", direction="better")]) for i in range(3)]
    v = aggregate.task_verdicts(aggregate.flatten(cards))[0]
    assert v["label"] == "consensus"
    assert v["pooling_note"] and "no single benchmark" in v["pooling_note"]


def test_genuine_same_dataset_consensus_is_not_flagged():
    """Don't cry wolf: real same-dataset agreement gets no warning."""
    cards = [make_card(f"p{i}2025x", claims=[
        make_claim(f"p{i}2025x", 1, dataset="Sen1Floods11", direction="better")]) for i in range(3)]
    v = aggregate.task_verdicts(aggregate.flatten(cards))[0]
    assert v["label"] == "consensus"
    assert v["pooling_note"] is None


def test_verdict_resting_on_self_evaluation_is_marked_fragile():
    cards = [
        make_card("a2025x", self_evaluation=True,
                  claims=[make_claim("a2025x", 1, direction="better")]),
        make_card("b2025x", self_evaluation=True,
                  claims=[make_claim("b2025x", 1, direction="better")]),
        make_card("c2025x", claims=[make_claim("c2025x", 1, direction="better")]),
        make_card("d2025x", claims=[make_claim("d2025x", 1, direction="better")]),
        make_card("e2025x", claims=[make_claim("e2025x", 1, direction="worse")]),
    ]
    views = aggregate.build_group_views(cards)
    v = views["all"]["task_verdicts"][0]
    assert v["label"] == "consensus"        # 4 of 5 papers say better = 80%
    # Drop the two self-evaluations and it is 2 better / 1 worse = 67% -> contested.
    assert v["fragile"], "a verdict that flips without self-evals must be marked"
    assert "contested" in v["fragile"]

    # And the no-self view must not double-warn about self-evals it already dropped.
    assert all(t["fragile"] is None for t in views["no_self_eval"]["task_verdicts"])


def test_evidence_profile_exposes_the_skew():
    cards = [
        make_card("a2025x", claims=[make_claim("a2025x", 1, direction="better", label_ratio=None)]),
        make_card("b2025x", claims=[make_claim("b2025x", 1, direction="better", label_ratio=None)]),
        make_card("c2025x", claims=[make_claim("c2025x", 1, direction="worse", label_ratio=0.5)]),
        # A model-vs-model claim: no task-specific baseline, so it drives nothing.
        make_card("d2025x", claims=[make_claim("d2025x", 1, baseline="prithvi", direction="better")]),
    ]
    e = aggregate.evidence_profile(aggregate.flatten(cards))
    assert e["n_claims"] == 4
    assert e["n_vs_task_specific"] == 3
    assert e["n_vs_model_or_none"] == 1
    assert e["directions"] == {"better": 2, "worse": 1, "parity": 0}
    assert e["pct_better"] == pytest.approx(66.7, abs=0.1)
    # Two of the four claims carry no label_ratio (the other two default to 1.0).
    assert e["pct_label_ratio_unspecified"] == pytest.approx(50.0, abs=0.1)
