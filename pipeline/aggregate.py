"""Deterministic aggregation. Pure functions, no I/O, no LLM, no network.

Everything the dashboard shows is computed here from the committed cards. The
cardinal rule is **never pool numbers across datasets**: grouping always keys on
``dataset`` (and label-ratio regime), so a "consensus" is agreement between
papers measuring the *same thing*, not an average of apples and oranges.

Every group is computed twice — with and without ``self_evaluation`` papers —
so the dashboard's toggle re-renders from a precomputed second view rather than
recomputing client-side.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass

from . import config
from .schema import Card

# Consensus thresholds (see the brief's table).
MIN_PAPERS_FOR_CONSENSUS = 3
CONSENSUS_AGREEMENT = 0.80
TAG_PROMOTION_VOTES = 2


# ---------------------------------------------------------------------------
# Flattening
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ClaimRow:
    task: str
    dataset: str
    model: str
    baseline: str | None
    metric: str
    bucket: str
    direction: str
    axis: str
    value: float
    baseline_value: float | None
    label_ratio: float | None
    locator: str
    span: str
    paper_key: str
    paper_title: str
    arxiv_id: str | None
    doi: str | None
    self_evaluation: bool
    month: str  # YYYY-MM


def bucket_label_ratio(x: float | None) -> str:
    """Label-availability regime. Different regimes are never pooled together."""
    if x is None:
        return "unspecified"
    if x >= 0.75:
        return "label_rich"
    if x >= 0.1:
        return "label_partial"
    return "label_scarce"


def flatten(cards: list[Card]) -> list[ClaimRow]:
    rows: list[ClaimRow] = []
    for card in cards:
        month = f"{card.date.year:04d}-{card.date.month:02d}"
        for c in card.claims:
            rows.append(ClaimRow(
                task=c.task, dataset=c.dataset, model=c.model, baseline=c.baseline,
                metric=c.metric, bucket=bucket_label_ratio(c.label_ratio),
                direction=c.direction, axis=c.axis, value=c.value,
                baseline_value=c.baseline_value, label_ratio=c.label_ratio,
                locator=c.locator, span=c.span, paper_key=card.key,
                paper_title=card.title, arxiv_id=card.arxiv_id, doi=card.doi,
                self_evaluation=card.self_evaluation, month=month,
            ))
    return rows


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------
def _paper_directions(rows: list[ClaimRow]) -> dict[str, str]:
    """One direction per paper = the majority direction of that paper's rows."""
    by_paper: dict[str, list[str]] = defaultdict(list)
    for r in rows:
        by_paper[r.paper_key].append(r.direction)
    out = {}
    for pk, dirs in by_paper.items():
        out[pk] = Counter(dirs).most_common(1)[0][0]
    return out


def classify(rows: list[ClaimRow]) -> dict:
    """Label a bundle of rows: consensus / contested / thin / gap."""
    pdirs = _paper_directions(rows)
    n = len(pdirs)
    if n == 0:
        return {"label": "gap", "n_papers": 0, "direction": None, "agreement": None}
    counts = Counter(pdirs.values())
    dominant, dom_n = counts.most_common(1)[0]
    agreement = dom_n / n
    if n < MIN_PAPERS_FOR_CONSENSUS:
        label = "thin"
    elif agreement >= CONSENSUS_AGREEMENT:
        label = "consensus"
    else:
        label = "contested"
    return {"label": label, "n_papers": n, "direction": dominant,
            "agreement": round(agreement, 3)}


def _paper_link(arxiv_id: str | None, doi: str | None) -> str | None:
    if arxiv_id:
        return f"https://arxiv.org/abs/{arxiv_id}"
    if doi:
        return f"https://doi.org/{doi}"
    return None


def _claim_payload(r: ClaimRow) -> dict:
    return {
        "paper_key": r.paper_key,
        "paper_title": r.paper_title,
        "link": _paper_link(r.arxiv_id, r.doi),
        "model": r.model,
        "baseline": r.baseline,
        "metric": r.metric,
        "value": r.value,
        "baseline_value": r.baseline_value,
        "dataset": r.dataset,
        "label_ratio": r.label_ratio,
        "direction": r.direction,
        "locator": r.locator,
        "span": r.span,
        "self_evaluation": r.self_evaluation,
    }


# ---------------------------------------------------------------------------
# Views
# ---------------------------------------------------------------------------
def _filter_self(rows: list[ClaimRow], include_self: bool) -> list[ClaimRow]:
    if include_self:
        return rows
    return [r for r in rows if not r.self_evaluation]


def group_view(rows: list[ClaimRow]) -> list[dict]:
    """One entry per (task, dataset, model, baseline, metric, bucket) group."""
    groups: dict[tuple, list[ClaimRow]] = defaultdict(list)
    for r in rows:
        key = (r.task, r.dataset, r.model, r.baseline, r.metric, r.bucket)
        groups[key].append(r)
    out = []
    for key, grp in groups.items():
        cls = classify(grp)
        out.append({
            "task": key[0], "dataset": key[1], "model": key[2],
            "baseline": key[3], "metric": key[4], "label_regime": key[5],
            **cls,
            "claims": [_claim_payload(r) for r in grp],
        })
    out.sort(key=lambda g: (g["task"], g["dataset"], g["model"], g["metric"]))
    return out


def matrix_view(rows: list[ClaimRow]) -> dict:
    """Model x task cells, coloured by consensus. Numbers are never pooled;
    the label reflects paper-level agreement, click-through shows the groups."""
    cells: dict[tuple, list[ClaimRow]] = defaultdict(list)
    models, tasks = set(), set()
    for r in rows:
        cells[(r.model, r.task)].append(r)
        models.add(r.model)
        tasks.add(r.task)
    cell_out = {}
    for (model, task), grp in cells.items():
        cls = classify(grp)
        cell_out[f"{model}\t{task}"] = {
            "model": model, "task": task, "n_claims": len(grp), **cls,
            "claims": [_claim_payload(r) for r in grp],
        }
    return {
        "models": sorted(models),
        "tasks": sorted(tasks),
        "cells": cell_out,
    }


def axes_view(rows: list[ClaimRow]) -> list[dict]:
    """Roll claims up per axis G1-G12, with explicit gap rows for empty axes."""
    by_axis: dict[str, list[ClaimRow]] = defaultdict(list)
    for r in rows:
        by_axis[r.axis].append(r)
    out = []
    for axis in config.axes_ordered():
        grp = by_axis.get(axis, [])
        cls = classify(grp)
        out.append({
            "axis": axis,
            "n_claims": len(grp),
            **cls,
            "claims": [_claim_payload(r) for r in grp],
        })
    return out


def build_group_views(cards: list[Card]) -> dict:
    """The full set of dataset-grouped/matrix/axes views, computed both ways."""
    rows_all = flatten(cards)
    out = {}
    for view_name, include_self in (("all", True), ("no_self_eval", False)):
        rows = _filter_self(rows_all, include_self)
        out[view_name] = {
            "groups": group_view(rows),
            "matrix": matrix_view(rows),
            "axes": axes_view(rows),
        }
    return out


# ---------------------------------------------------------------------------
# Limitations time series
# ---------------------------------------------------------------------------
def limitations_timeseries(cards: list[Card]) -> dict:
    """Distinct papers per limitation tag, as a monthly time series."""
    # tag -> month -> set(paper_key)
    acc: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    totals: Counter = Counter()
    for card in cards:
        month = f"{card.date.year:04d}-{card.date.month:02d}"
        for tag in set(card.limitations):
            acc[tag][month].add(card.key)
            totals[tag] += 1
    series = {}
    for tag, months in acc.items():
        series[tag] = {m: len(pk) for m, pk in sorted(months.items())}
    return {"series": series, "totals": dict(totals)}


# ---------------------------------------------------------------------------
# Registry & quarantine
# ---------------------------------------------------------------------------
def registry(cards: list[Card], quarantine_count: int) -> dict:
    papers = []
    status_counts: Counter = Counter()
    for card in sorted(cards, key=lambda c: c.date, reverse=True):
        status_counts[card.doi_status] += 1
        papers.append({
            "key": card.key,
            "title": card.title,
            "date": card.date.isoformat(),
            "arxiv_id": card.arxiv_id,
            "doi": card.doi,
            "doi_status": card.doi_status,
            "venue": card.venue,
            "self_evaluation": card.self_evaluation,
            "n_claims": len(card.claims),
            "link": _paper_link(card.arxiv_id, card.doi),
        })
    return {
        "papers": papers,
        "doi_status_counts": dict(status_counts),
        "quarantine_count": quarantine_count,
        "n_papers": len(cards),
    }


# ---------------------------------------------------------------------------
# Tag promotion (pure computation; run.py persists the decision)
# ---------------------------------------------------------------------------
def compute_tag_promotion(cards: list[Card],
                          pending: dict[str, list[str]]) -> tuple[list[str], dict[str, list[str]]]:
    """Return (tags_to_promote, updated_pending).

    A proposed_tag is promoted once >= TAG_PROMOTION_VOTES *distinct papers* have
    proposed it; below that it accumulates in pending. Existing pending evidence
    is merged so votes persist across runs.
    """
    votes: dict[str, set[str]] = defaultdict(set)
    for tag, keys in pending.items():
        votes[tag].update(keys)
    for card in cards:
        for tag in set(card.proposed_tags):
            votes[tag].add(card.key)

    known = config.axes() | config.tasks() | config.limitations() | config.promoted_tags()
    promote: list[str] = []
    new_pending: dict[str, list[str]] = {}
    for tag, keys in votes.items():
        if tag in known:
            continue
        if len(keys) >= TAG_PROMOTION_VOTES:
            promote.append(tag)
        else:
            new_pending[tag] = sorted(keys)
    return sorted(promote), dict(sorted(new_pending.items()))


# ---------------------------------------------------------------------------
# Top-level
# ---------------------------------------------------------------------------
def aggregate(cards: list[Card], *, quarantine_count: int = 0) -> dict:
    """Assemble the complete data model for the site (minus `generated_at`)."""
    views = build_group_views(cards)
    return {
        "views": views,
        "limitations": limitations_timeseries(cards),
        "registry": registry(cards, quarantine_count),
        "meta": {
            "n_papers": len(cards),
            "axes": sorted(config.axes()),
            "tasks": sorted(config.tasks()),
            "models": sorted(config.model_keys()),
            "consensus_rule": {
                "min_papers": MIN_PAPERS_FOR_CONSENSUS,
                "agreement": CONSENSUS_AGREEMENT,
            },
        },
    }
