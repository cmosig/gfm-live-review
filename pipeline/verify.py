"""Deduplication, DOI resolution, and self-evaluation detection. No LLM.

DOIs enter the system ONLY here, from Crossref/OpenAlex metadata, and are
mechanically verified by a fuzzy title match. A DOI that originates from the
model is impossible by construction (the extraction schema forbids the field);
this module never even shows paper metadata to a model.
"""
from __future__ import annotations

from dataclasses import dataclass

from rapidfuzz import fuzz

from . import config, http, state
from .ingest import Candidate

CROSSREF_API = "https://api.crossref.org/works"
TITLE_MATCH_THRESHOLD = 90.0


@dataclass
class VerifyResult:
    candidate: Candidate
    doi: str | None
    doi_status: str  # DoiStatus literal
    is_duplicate: bool
    duplicate_of: str | None
    self_evaluation: bool


def fetch_crossref_work(doi: str) -> dict:
    """Fetch a Crossref work record. Raises http.HttpError on failure."""
    resp = http.get(f"{CROSSREF_API}/{doi}", accept="application/json")
    http.courtesy_sleep()
    return resp.json().get("message", {})


def resolve_doi(cand: Candidate, *, fetch=fetch_crossref_work) -> tuple[str | None, str]:
    """Return (doi, doi_status).

    * no doi in metadata            -> (None, "no_doi_found")
    * Crossref/network error        -> (doi, "unresolved")   [retry another day]
    * title fuzzy-match >= threshold -> (doi, "verified")
    * title mismatch                -> (doi, "mismatch")     [caller quarantines]
    """
    if not cand.doi:
        return None, "no_doi_found"
    doi = cand.doi.strip().lower()
    try:
        work = fetch(doi)
    except http.HttpError:
        return doi, "unresolved"
    titles = work.get("title") or []
    cr_title = titles[0] if titles else ""
    if not cr_title:
        return doi, "unresolved"
    score = fuzz.token_sort_ratio(cand.title.lower(), cr_title.lower())
    if score >= TITLE_MATCH_THRESHOLD:
        return doi, "verified"
    return doi, "mismatch"


def _tracked_arxiv_ids() -> dict[str, str]:
    """arxiv_id -> model key, for models whose own defining paper we know."""
    out = {}
    for m in config.load_models().get("models", []):
        if m.get("arxiv_id"):
            out[m["arxiv_id"]] = m["key"]
    return out


def detect_self_evaluation(cand: Candidate) -> bool:
    """Mechanical self-eval detection.

    A paper that *is* a tracked model's own defining paper is self-evaluation by
    definition. Broader author-overlap detection requires the model papers'
    OpenAlex author ids; where those are unknown the extractor sets the flag
    (see §8), so this returns a conservative False rather than guessing.
    """
    if cand.arxiv_id and cand.arxiv_id in _tracked_arxiv_ids():
        return True
    return False


def verify(cand: Candidate, seen: dict[str, dict], existing_titles: set[str],
           *, fetch=fetch_crossref_work) -> VerifyResult:
    tkey = state.title_key(cand.title)
    is_dup = tkey in seen or tkey in existing_titles
    dup_of = seen.get(tkey, {}).get("key") if tkey in seen else None
    doi, status = resolve_doi(cand, fetch=fetch)
    self_eval = detect_self_evaluation(cand)
    return VerifyResult(
        candidate=cand,
        doi=doi,
        doi_status=status,
        is_duplicate=is_dup,
        duplicate_of=dup_of,
        self_evaluation=self_eval,
    )
