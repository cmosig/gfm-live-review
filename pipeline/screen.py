"""Cheap, auditable relevance screening. No LLM.

A candidate is accepted if its title/abstract names a tracked model, or matches
the geospatial-foundation-model regex. Every rejection is returned with a
reason so recall stays auditable — we can grep the run log to see what we threw
away and why.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from . import config
from .ingest import Candidate

# (geospatial|earth observation|remote sensing|satellite) ... (foundation model|embedding)
_TOPIC_RE = re.compile(
    r"(geospatial|earth observation|remote sensing|satellite|earth embedding)"
    r".{0,40}(foundation model|embedding)",
    re.IGNORECASE | re.DOTALL,
)


@dataclass
class ScreenResult:
    candidate: Candidate
    accepted: bool
    reason: str
    matched_models: list[str]


def _matched_models(text: str) -> list[str]:
    text_l = text.lower()
    hits = []
    for key, aliases in config.model_aliases().items():
        for alias in aliases:
            # Word-ish boundary so "clay" doesn't match "clayey".
            if re.search(rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])", text_l):
                hits.append(key)
                break
    return hits


def screen_one(cand: Candidate) -> ScreenResult:
    text = f"{cand.title}\n{cand.abstract}"
    models = _matched_models(text)
    if models:
        return ScreenResult(cand, True, f"matched models: {','.join(models)}", models)
    if _TOPIC_RE.search(text):
        return ScreenResult(cand, True, "matched geospatial-foundation-model regex", [])
    return ScreenResult(cand, False, "no model name and no topic-regex match", [])


def screen(candidates: list[Candidate]) -> tuple[list[ScreenResult], list[ScreenResult]]:
    """Return (accepted, rejected) ScreenResults."""
    accepted, rejected = [], []
    for c in candidates:
        r = screen_one(c)
        (accepted if r.accepted else rejected).append(r)
    return accepted, rejected
