"""Shared fixtures. All tests are fully offline: no docker, no claude, no network."""
from __future__ import annotations

from datetime import date, datetime, timezone

import pytest

from pipeline import config
from pipeline.schema import Card, Claim
from pipeline.textutil import span_sha256


@pytest.fixture
def iso(tmp_path, monkeypatch):
    """Redirect all committed-state paths to a temp dir so tests don't touch the repo."""
    cards = tmp_path / "cards"
    quarantine = tmp_path / "quarantine"
    state = tmp_path / "state"
    site = tmp_path / "site"
    monkeypatch.setattr(config, "CARDS_DIR", cards)
    monkeypatch.setattr(config, "QUARANTINE_DIR", quarantine)
    monkeypatch.setattr(config, "STATE_DIR", state)
    monkeypatch.setattr(config, "SITE_DIR", site)
    monkeypatch.setattr(config, "SEEN_PATH", state / "seen.json")
    monkeypatch.setattr(config, "PENDING_TAGS_PATH", state / "pending_tags.json")
    monkeypatch.setattr(config, "RUNS_PATH", state / "runs.jsonl")
    monkeypatch.setattr(config, "DATA_JSON_PATH", site / "data.json")
    for d in (cards, quarantine, state, site):
        d.mkdir(parents=True, exist_ok=True)
    config.reload_vocab()
    return tmp_path


def make_claim(key: str, n: int, *, axis="G1_label_rich_parity", task="crop_type_mapping",
               dataset="PASTIS", model="tessera", baseline="task_specific", metric="f1",
               value=0.85, baseline_value=0.80, label_ratio=1.0, direction="better",
               span="the model reaches state of the art performance on this benchmark"):
    return Claim(
        id=f"{key}#c{n}", axis=axis, task=task, dataset=dataset, model=model,
        baseline=baseline, metric=metric, value=value, baseline_value=baseline_value,
        label_ratio=label_ratio, direction=direction, locator=f"Table {n}",
        span=span, span_sha256=span_sha256(span),
    )


def make_card(key: str, *, title=None, pub_date=date(2025, 6, 1), self_evaluation=False,
              claims=None, models=("tessera",), tasks=("crop_type_mapping",),
              axes=("G1_label_rich_parity",), limitations=(), proposed_tags=(),
              doi=None, doi_status="no_doi_found", arxiv_id="2506.20380"):
    return Card(
        key=key, title=title or f"Paper {key}", arxiv_id=arxiv_id, doi=doi,
        doi_status=doi_status, date=pub_date, authors=["Author"],
        self_evaluation=self_evaluation, models=list(models), tasks=list(tasks),
        regions=["global"], axes=list(axes), limitations=list(limitations),
        proposed_tags=list(proposed_tags),
        claims=claims if claims is not None else [make_claim(key, 1)],
        summary="Summary.", setup="Setup.", caveats="Caveat.",
        extractor_version="1", ingested_at=datetime(2025, 6, 1, tzinfo=timezone.utc),
    )
