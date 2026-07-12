"""Pydantic v2 data model — the single source of truth for the whole system.

Two families of models live here:

* ``Extraction*`` — the *untrusted* output the LLM is allowed to return. These
  use ``extra="forbid"`` so a model that tries to smuggle a ``doi`` (or any
  other field it must not author) fails validation loudly. There is no ``doi``,
  no ``span_sha256``, no ``id`` here: those are added in Python.

* ``Claim`` / ``Card`` — the *trusted* committed objects, assembled in Python
  from host-collected metadata + a validated extraction. ``doi`` appears only
  here and is written only from Crossref/OpenAlex metadata.

All vocabulary constraints (axes, tasks, models, limitations) are validated
against ``config`` at construction time, so an out-of-vocab tag can never reach
a committed card.
"""
from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)

from . import config
from .textutil import normalize_ws, span_sha256, strip_control

Direction = Literal["better", "worse", "parity"]
DoiStatus = Literal["verified", "no_doi_found", "unresolved", "mismatch"]

# ^ Card.key: lowercase alnum start, then 2-63 more of [a-z0-9_-]. This is the
# gate that makes `../../.github/workflows/pages` impossible as a key.
KEY_PATTERN = r"^[a-z0-9][a-z0-9_-]{2,63}$"

# Free-text length caps (defence against a model dumping a huge payload).
_MAX_SPAN_WORDS = 25
_MAX_TITLE = 400
_MAX_SUMMARY = 1200
_MAX_SETUP = 2000
_MAX_CAVEATS = 2000
_MAX_FREETEXT = 400  # generic short fields (locator, dataset, metric names …)


def _clean_text(v: str, *, max_len: int) -> str:
    """Strip control chars, collapse nothing else, and enforce a length cap."""
    v = strip_control(v)
    if len(v) > max_len:
        raise ValueError(f"text exceeds {max_len} characters")
    return v


# ---------------------------------------------------------------------------
# Untrusted LLM output
# ---------------------------------------------------------------------------
class ExtractionClaim(BaseModel):
    """One quantitative claim as returned by the extractor (pre-verification)."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    axis: str
    task: str
    dataset: str
    model: str
    baseline: str | None = None
    metric: str
    value: float
    baseline_value: float | None = None
    label_ratio: float | None = None
    direction: Direction
    locator: str
    span: str

    @field_validator("axis")
    @classmethod
    def _axis_in_vocab(cls, v: str) -> str:
        if v not in config.axes():
            raise ValueError(f"axis {v!r} not in taxonomy.axes")
        return v

    @field_validator("task")
    @classmethod
    def _task_in_vocab(cls, v: str) -> str:
        if v not in config.tasks():
            raise ValueError(f"task {v!r} not in taxonomy.tasks")
        return v

    @field_validator("model")
    @classmethod
    def _model_in_vocab(cls, v: str) -> str:
        if v not in config.model_keys():
            raise ValueError(f"model {v!r} not in models.yaml")
        return v

    @field_validator("baseline")
    @classmethod
    def _baseline_ok(cls, v: str | None) -> str | None:
        if v is None:
            return v
        if v not in config.valid_baselines():
            raise ValueError(f"baseline {v!r} not a model key or {config.TASK_SPECIFIC!r}")
        return v

    @field_validator("metric")
    @classmethod
    def _metric_ok(cls, v: str) -> str:
        if v not in config.METRICS:
            raise ValueError(f"metric {v!r} not in {config.METRICS}")
        return v

    @field_validator("dataset", "locator")
    @classmethod
    def _short_freetext(cls, v: str) -> str:
        v = _clean_text(v, max_len=_MAX_FREETEXT)
        if not v:
            raise ValueError("must not be empty")
        return v

    @field_validator("span")
    @classmethod
    def _span_ok(cls, v: str) -> str:
        v = strip_control(v).strip()
        if not v:
            raise ValueError("span is required and must be non-empty")
        if len(normalize_ws(v).split()) > _MAX_SPAN_WORDS:
            raise ValueError(f"span exceeds {_MAX_SPAN_WORDS} words")
        return v

    @field_validator("label_ratio")
    @classmethod
    def _label_ratio_range(cls, v: float | None) -> float | None:
        if v is None:
            return v
        if not (0.0 < v <= 1.0):
            raise ValueError("label_ratio must be in (0, 1]")
        return v


class ExtractionOutput(BaseModel):
    """The complete JSON object the LLM is permitted to return for one paper.

    Note the deliberate ABSENCE of ``doi``, ``key``, ``title``, ``date``,
    ``authors``, ``arxiv_id`` — all host-supplied. ``extra="forbid"`` means an
    LLM that emits a ``doi`` (or anything else off-contract) fails validation,
    which is the mechanical guarantee behind "the LLM never invents a DOI".
    """

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    self_evaluation: bool = False
    models: list[str] = Field(default_factory=list)
    tasks: list[str] = Field(default_factory=list)
    regions: list[str] = Field(default_factory=list)
    axes: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    proposed_tags: list[str] = Field(default_factory=list)
    claims: list[ExtractionClaim] = Field(default_factory=list)
    summary: str = ""
    setup: str = ""
    caveats: str = ""

    @field_validator("models")
    @classmethod
    def _models_vocab(cls, v: list[str]) -> list[str]:
        bad = [m for m in v if m not in config.model_keys()]
        if bad:
            raise ValueError(f"unknown models: {bad}")
        return v

    @field_validator("tasks")
    @classmethod
    def _tasks_vocab(cls, v: list[str]) -> list[str]:
        bad = [t for t in v if t not in config.tasks()]
        if bad:
            raise ValueError(f"unknown tasks: {bad}")
        return v

    @field_validator("axes")
    @classmethod
    def _axes_vocab(cls, v: list[str]) -> list[str]:
        bad = [a for a in v if a not in config.axes()]
        if bad:
            raise ValueError(f"unknown axes: {bad}")
        return v

    @field_validator("limitations")
    @classmethod
    def _limitations_vocab(cls, v: list[str]) -> list[str]:
        # Controlled vocabulary ONLY. Anything else belongs in proposed_tags.
        bad = [x for x in v if x not in config.limitations()]
        if bad:
            raise ValueError(f"limitations not in controlled vocab: {bad}")
        return v

    @field_validator("regions")
    @classmethod
    def _regions_ok(cls, v: list[str]) -> list[str]:
        out = []
        for r in v:
            r = strip_control(r).strip()
            if r == "global" or (len(r) == 2 and r.isalpha()):
                out.append(r.lower() if r != "global" else r)
            else:
                raise ValueError(f"region {r!r} must be ISO-3166 alpha-2 or 'global'")
        return out

    @field_validator("proposed_tags")
    @classmethod
    def _proposed_ok(cls, v: list[str]) -> list[str]:
        return [strip_control(x).strip()[:64] for x in v if strip_control(x).strip()]

    @field_validator("summary")
    @classmethod
    def _summary_ok(cls, v: str) -> str:
        return _clean_text(v, max_len=_MAX_SUMMARY)

    @field_validator("setup")
    @classmethod
    def _setup_ok(cls, v: str) -> str:
        return _clean_text(v, max_len=_MAX_SETUP)

    @field_validator("caveats")
    @classmethod
    def _caveats_ok(cls, v: str) -> str:
        return _clean_text(v, max_len=_MAX_CAVEATS)


# ---------------------------------------------------------------------------
# Trusted committed objects
# ---------------------------------------------------------------------------
class Claim(ExtractionClaim):
    """A verified claim, with a stable id and a Python-computed span hash."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    id: str  # "{paper_key}#c{n}"
    span_sha256: str

    @model_validator(mode="after")
    def _hash_matches_span(self) -> "Claim":
        # The hash must be exactly what Python computes from the span. This makes
        # it impossible to commit a claim whose span_sha256 was fabricated or
        # drifted from its span.
        expected = span_sha256(self.span)
        if self.span_sha256 != expected:
            raise ValueError("span_sha256 does not match span (must be computed in Python)")
        return self


class Card(BaseModel):
    """The committed record of one paper. Serialises to markdown+front-matter."""

    model_config = ConfigDict(extra="forbid")

    key: str = Field(pattern=KEY_PATTERN)
    title: str
    arxiv_id: str | None = None
    doi: str | None = None  # NEVER written by the LLM; Crossref/OpenAlex only.
    doi_status: DoiStatus
    venue: str | None = None
    date: date
    authors: list[str] = Field(default_factory=list)
    self_evaluation: bool = False
    models: list[str] = Field(default_factory=list)
    tasks: list[str] = Field(default_factory=list)
    regions: list[str] = Field(default_factory=list)
    axes: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    proposed_tags: list[str] = Field(default_factory=list)
    claims: list[Claim] = Field(default_factory=list)
    summary: str = ""
    setup: str = ""
    caveats: str = ""
    extractor_version: str
    ingested_at: datetime

    @field_validator("title")
    @classmethod
    def _title_ok(cls, v: str) -> str:
        v = strip_control(v).strip()
        if not v:
            raise ValueError("title required")
        if len(v) > _MAX_TITLE:
            raise ValueError("title too long")
        return v

    @field_validator("key")
    @classmethod
    def _key_ok(cls, v: str) -> str:
        # Belt-and-braces: the Field(pattern=...) already enforces this, but we
        # reject any path separators explicitly so a future refactor can't widen
        # the pattern and reintroduce traversal.
        if "/" in v or "\\" in v or ".." in v:
            raise ValueError("key must not contain path separators")
        return v
