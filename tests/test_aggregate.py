"""Consensus aggregation, exhaustively (§10)."""
from __future__ import annotations

from pipeline import aggregate
from tests.conftest import make_card, make_claim


def _group(groups, dataset):
    return [g for g in groups if g["dataset"] == dataset]


def test_consensus_three_papers_agree():
    cards = [make_card(f"pap{i}", claims=[make_claim(f"pap{i}", 1, direction="better")])
             for i in range(3)]
    rows = aggregate.flatten(cards)
    groups = aggregate.group_view(rows)
    assert len(groups) == 1
    assert groups[0]["label"] == "consensus"
    assert groups[0]["n_papers"] == 3
    assert groups[0]["direction"] == "better"


def test_contested_three_papers_mixed():
    dirs = ["better", "better", "worse"]  # 2/3 = 0.667 < 0.80
    cards = [make_card(f"pap{i}", claims=[make_claim(f"pap{i}", 1, direction=d)])
             for i, d in enumerate(dirs)]
    groups = aggregate.group_view(aggregate.flatten(cards))
    assert groups[0]["label"] == "contested"


def test_thin_with_two_papers():
    cards = [make_card(f"pap{i}", claims=[make_claim(f"pap{i}", 1)]) for i in range(2)]
    groups = aggregate.group_view(aggregate.flatten(cards))
    assert groups[0]["label"] == "thin"


def test_gap_axis_has_explicit_row():
    cards = [make_card("pap0", axes=["G1_label_rich_parity"],
                       claims=[make_claim("pap0", 1)])]
    axes = aggregate.axes_view(aggregate.flatten(cards))
    labels = {a["axis"]: a["label"] for a in axes}
    # An axis nobody produced claims for is an explicit gap row.
    assert labels["G5_cost"] == "gap"
    assert labels["G1_label_rich_parity"] in {"thin", "consensus", "contested"}


def test_never_pool_across_datasets():
    # Same task/model/metric but two datasets -> two separate groups.
    c = make_card("pap0", claims=[
        make_claim("pap0", 1, dataset="PASTIS"),
        make_claim("pap0", 2, dataset="EuroSAT"),
    ])
    groups = aggregate.group_view(aggregate.flatten([c]))
    datasets = sorted(g["dataset"] for g in groups)
    assert datasets == ["EuroSAT", "PASTIS"]
    for g in groups:
        assert all(cl["dataset"] == g["dataset"] for cl in g["claims"])


def test_label_regime_not_pooled():
    c1 = make_card("pap0", claims=[make_claim("pap0", 1, label_ratio=1.0)])
    c2 = make_card("pap1", claims=[make_claim("pap1", 1, label_ratio=0.01)])
    groups = aggregate.group_view(aggregate.flatten([c1, c2]))
    regimes = sorted(g["label_regime"] for g in groups)
    assert regimes == ["label_rich", "label_scarce"]


def test_self_eval_exclusion_changes_result():
    # 3 papers all "better", but one is self-evaluation.
    cards = [
        make_card("pap0", self_evaluation=True, claims=[make_claim("pap0", 1, direction="better")]),
        make_card("pap1", claims=[make_claim("pap1", 1, direction="better")]),
        make_card("pap2", claims=[make_claim("pap2", 1, direction="better")]),
    ]
    views = aggregate.build_group_views(cards)
    all_groups = views["all"]["groups"]
    no_self = views["no_self_eval"]["groups"]
    assert all_groups[0]["label"] == "consensus" and all_groups[0]["n_papers"] == 3
    # Dropping the self-eval paper leaves 2 -> thin.
    assert no_self[0]["label"] == "thin" and no_self[0]["n_papers"] == 2


def test_matrix_cell_click_through_has_claims():
    cards = [make_card("pap0", claims=[make_claim("pap0", 1)])]
    m = aggregate.matrix_view(aggregate.flatten(cards))
    cell = m["cells"]["tessera\tcrop_type_mapping"]
    assert cell["claims"] and cell["claims"][0]["span"]


def test_direction_only_from_vs_task_specific():
    # Three papers, all "better", but comparing TESSERA to another FOUNDATION
    # model (alphaearth) — not a task-specific model. Direction must NOT be set.
    cards = [make_card(f"pap{i}", claims=[
        make_claim(f"pap{i}", 1, baseline="alphaearth", direction="better")])
        for i in range(3)]
    m = aggregate.matrix_view(aggregate.flatten(cards))
    cell = m["cells"]["tessera\tcrop_type_mapping"]
    assert cell["direction"] is None          # no vs-task-specific evidence
    assert cell["n_papers"] == 0              # vs-task-specific paper count
    assert cell["n_papers_all"] == 3          # but total evidence is visible
    assert cell["n_claims"] == 3
    assert cell["label"] == "gap"


def test_matrix_mixes_baselines_classifies_only_task_specific():
    # Two task-specific claims (one better, one worse) + a model-vs-model claim.
    c = make_card("pap0", claims=[
        make_claim("pap0", 1, baseline="task_specific", direction="better"),
        make_claim("pap0", 2, baseline="alphaearth", direction="worse"),
    ])
    m = aggregate.matrix_view(aggregate.flatten([c]))
    cell = m["cells"]["tessera\tcrop_type_mapping"]
    # Only the task-specific claim's direction counts.
    assert cell["direction"] == "better"
    assert cell["n_papers"] == 1 and cell["n_papers_all"] == 1


def test_axes_view_direction_vs_task_specific_only():
    cards = [make_card("pap0", axes=["G1_label_rich_parity"], claims=[
        make_claim("pap0", 1, baseline="alphaearth", direction="better")])]
    axes = aggregate.axes_view(aggregate.flatten(cards))
    g1 = next(a for a in axes if a["axis"] == "G1_label_rich_parity")
    assert g1["direction"] is None and g1["n_papers"] == 0
    assert g1["n_papers_all"] == 1


def test_tag_promotion_threshold():
    # A proposed tag with 2 distinct papers is promoted; 1 stays pending.
    cards = [
        make_card("pap0", proposed_tags=["cloud_removal", "solo_tag"]),
        make_card("pap1", proposed_tags=["cloud_removal"]),
    ]
    promote, pending = aggregate.compute_tag_promotion(cards, {})
    assert "cloud_removal" in promote
    assert "solo_tag" in pending and "cloud_removal" not in pending


def test_tag_promotion_merges_existing_pending():
    cards = [make_card("pap1", proposed_tags=["cloud_removal"])]
    promote, _ = aggregate.compute_tag_promotion(cards, {"cloud_removal": ["pap0"]})
    assert "cloud_removal" in promote  # p0 (pending) + p1 = 2 votes


def test_limitations_timeseries_counts_distinct_papers():
    cards = [
        make_card("pap0", limitations=["temporal_transfer"]),
        make_card("pap1", limitations=["temporal_transfer"]),
    ]
    ts = aggregate.limitations_timeseries(cards)
    assert ts["totals"]["temporal_transfer"] == 2
    assert ts["series"]["temporal_transfer"]["2025-06"] == 2
