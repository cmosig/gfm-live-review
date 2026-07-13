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

import re
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


# ---------------------------------------------------------------------------
# Benchmark grouping
# ---------------------------------------------------------------------------
# `dataset` is free text from the extractor, so the same benchmark arrives in
# many surface forms ("Sen1Floods11", "Sen1Floods11 Bolivia", "CropHarvest Togo
# test set"). Grouping on the raw string yields ~130 groups of one, which
# answers nothing. We fold each name to a canonical benchmark, but keep the
# EXACT original string on every claim as its variant — so the grouping is a
# navigation aid and never destroys what the paper actually said.
_PARENS_RE = re.compile(r"\([^)]*\)")
_YEAR_RE = re.compile(r"\b(?:19|20)\d{2}(?:-\d{2,4})?\b")
_NOISE_RE = re.compile(
    r"\b(?:test|train|training|val|validation|eval|holdout|held-out|split|splits|"
    r"set|subset|sample|samples|dataset|datasets|benchmark|data)\b")
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
_MIN_PREFIX_LEN = 4  # don't let a 2-3 char name swallow unrelated benchmarks


def _strip_qualifiers(s: str) -> str:
    """Drop the "(2018, 5 crops)" / ", 2013-2020" tail that names a split, not a
    benchmark. Parentheses go FIRST: splitting on the comma first would cut
    "JECAM Senegal (2018, 5 crops)" mid-parenthesis and strand "(2018".
    """
    return _PARENS_RE.sub(" ", s).split(",")[0]


def _normalise_dataset(dataset: str) -> str:
    """Fold one raw dataset string to a comparison key (may still be a variant)."""
    s = _strip_qualifiers(dataset)
    s = s.lower()
    s = _YEAR_RE.sub(" ", s)
    s = _NOISE_RE.sub(" ", s)           # drop split/set/dataset noise words
    return _NON_ALNUM_RE.sub(" ", s).strip()


def _benchmark_keys(datasets: set[str]) -> dict[str, str]:
    """raw dataset string -> canonical benchmark key.

    Two-pass: normalise, then fold any name that begins with another *known*
    benchmark name into that shorter parent ("sen1floods11 bolivia" is a split
    of "sen1floods11"). Only names the corpus actually contains can act as
    parents, so this never invents a grouping.
    """
    norm = {d: _normalise_dataset(d) for d in datasets}
    known = {n for n in norm.values() if len(n) >= _MIN_PREFIX_LEN}
    canon: dict[str, str] = {}
    for raw, n in norm.items():
        parent = n
        for cand in known:
            if cand == n or len(cand) >= len(parent):
                continue
            # word-boundary prefix only: "cdl fallow" -> "cdl", but never
            # "eurosat" -> "euro" unless "euro" is itself a dataset in the corpus.
            if n.startswith(cand + " "):
                parent = cand
        canon[raw] = parent or n
    return canon


def _display_name(variants: set[str]) -> str:
    """The benchmark's own name, recovered from its variant spellings.

    The shortest variant is the least qualified one; dropping its split/year
    qualifier turns "JECAM Senegal (2018, 5 crops)" into "JECAM Senegal". Casing
    comes from the paper, never from title-casing (which would wreck acronyms).
    """
    shortest = min(variants, key=lambda v: (len(v), v))
    base = re.sub(r"\s+", " ", _strip_qualifiers(shortest)).strip(" -–—/")
    return base or shortest


def benchmark_view(rows: list[ClaimRow]) -> list[dict]:
    """One entry per benchmark: every claim made on it, across all papers.

    This is the apples-to-apples cut. Within a single benchmark the evaluation
    substrate is held fixed, so disagreement between papers is a real
    disagreement rather than an artefact of different data. Consensus is still
    computed per PAPER and only from vs-task-specific claims, exactly as
    elsewhere — metrics are never averaged across papers.
    """
    if not rows:
        return []
    canon = _benchmark_keys({r.dataset for r in rows})

    groups: dict[str, list[ClaimRow]] = defaultdict(list)
    for r in rows:
        groups[canon[r.dataset]].append(r)

    out = []
    for key, grp in groups.items():
        display = _display_name({r.dataset for r in grp})
        ts = [r for r in grp if r.baseline == config.TASK_SPECIFIC]
        out.append({
            "benchmark": key,
            "name": display,
            "variants": sorted({r.dataset for r in grp}),
            "n_papers": len({r.paper_key for r in grp}),
            "n_claims": len(grp),
            "tasks": sorted({r.task for r in grp}),
            "models": sorted({r.model for r in grp}),
            "metrics": sorted({r.metric for r in grp}),
            # Verdict is vs-task-specific only; a benchmark on which every claim
            # is GFM-vs-GFM has no verdict to give, and says so.
            "verdict": classify(ts) if ts else
                       {"label": "gap", "n_papers": 0, "direction": None,
                        "agreement": None},
            "n_vs_task_specific": len(ts),
            "claims": [_claim_payload(r) for r in grp],
        })
    # Most-evaluated benchmarks first: those are the ones where a cross-paper
    # comparison is actually possible.
    out.sort(key=lambda b: (-b["n_papers"], -b["n_claims"], b["name"].lower()))
    return out


def _vs_task_specific(rows: list[ClaimRow]) -> list[ClaimRow]:
    """The rows whose direction is meaningful for the headline question.

    Direction on the dashboard ALWAYS means "foundation model vs a
    task-specific model". Claims comparing two foundation models, or with no
    baseline at all, stay visible in click-throughs but never drive the
    consensus/direction classification.
    """
    return [r for r in rows if r.baseline == config.TASK_SPECIFIC]


def task_verdicts(rows: list[ClaimRow]) -> list[dict]:
    """The headline view: do geospatial foundation models (as a class) beat
    task-specific models / indices, per task?

    Only vs-task-specific claims count. Direction is compared per PAPER, then
    papers are counted — so pooling across datasets is legitimate (we count
    which way each paper landed, we never average incomparable metrics). A
    per-model breakdown is attached so a reader can see whether the answer
    differs by model.
    """
    ts = [r for r in rows if r.baseline == config.TASK_SPECIFIC]
    by_task: dict[str, list[ClaimRow]] = defaultdict(list)
    for r in ts:
        by_task[r.task].append(r)

    out = []
    for task, grp in by_task.items():
        overall = classify(grp)
        by_model: dict[str, list[ClaimRow]] = defaultdict(list)
        for r in grp:
            by_model[r.model].append(r)
        models = []
        for model, mrows in sorted(by_model.items()):
            mc = classify(mrows)
            models.append({"model": model, "n_claims": len(mrows), **mc})
        model_dirs = {m["direction"] for m in models if m["direction"]}
        out.append({
            "task": task,
            **overall,
            "n_claims": len(grp),
            "n_models": len(by_model),
            "datasets": sorted({r.dataset for r in grp}),
            "models": models,
            "models_differ": len(model_dirs) > 1,
            "claims": [_claim_payload(r) for r in grp],
        })

    order = {"contested": 0, "consensus": 1, "thin": 2, "gap": 3}
    out.sort(key=lambda t: (order.get(t["label"], 9), -t["n_papers"], t["task"]))
    return out


def matrix_view(rows: list[ClaimRow]) -> dict:
    """Model x task cells, coloured by consensus. Numbers are never pooled;
    the label reflects paper-level agreement, click-through shows the groups.

    Classification (direction/label/agreement) is computed ONLY from claims
    whose baseline is a task-specific model; `n_papers_all` counts every paper
    with any claim in the cell, so the UI can show total evidence while
    colouring strictly by the vs-task-specific subset.
    """
    cells: dict[tuple, list[ClaimRow]] = defaultdict(list)
    models, tasks = set(), set()
    for r in rows:
        cells[(r.model, r.task)].append(r)
        models.add(r.model)
        tasks.add(r.task)
    cell_out = {}
    for (model, task), grp in cells.items():
        cls = classify(_vs_task_specific(grp))
        cell_out[f"{model}\t{task}"] = {
            "model": model, "task": task, "n_claims": len(grp),
            "n_papers_all": len({r.paper_key for r in grp}), **cls,
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
        # Direction/consensus only from vs-task-specific claims (see matrix_view);
        # n_papers_all still counts every paper contributing any evidence.
        cls = classify(_vs_task_specific(grp))
        out.append({
            "axis": axis,
            "n_claims": len(grp),
            "n_papers_all": len({r.paper_key for r in grp}),
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
            "task_verdicts": task_verdicts(rows),
            "benchmarks": benchmark_view(rows),
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
