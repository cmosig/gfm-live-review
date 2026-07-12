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


def arxiv_doi(arxiv_id: str) -> str:
    """The DataCite DOI arXiv mints for every paper: 10.48550/arXiv.<id>.

    This is a documented, deterministic 1:1 mapping from the arXiv id (which
    itself comes from the arXiv API, never the LLM), so it counts as verified
    by construction — no fuzzy title match needed.
    """
    return f"10.48550/arxiv.{arxiv_id}"


def resolve_doi(cand: Candidate, *, fetch=fetch_crossref_work) -> tuple[str | None, str]:
    """Return (doi, doi_status).

    * journal DOI + title match      -> (doi, "verified")
    * journal DOI + Crossref error   -> (doi, "unresolved")  [retry another day]
    * journal DOI + title mismatch   -> (doi, "mismatch")    [caller quarantines]
    * no journal DOI, arXiv paper    -> (10.48550/arXiv.<id>, "verified")
    * no DOI derivable at all        -> (None, "no_doi_found")
    """
    if not cand.doi:
        if cand.arxiv_id:
            return arxiv_doi(cand.arxiv_id), "verified"
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


def _norm_author(name: str) -> str:
    """Normalise an author's FULL name for overlap matching.

    Full-name matching, not surname+initial: with common surnames the initial
    scheme collides ("Chenhui Zhang" at DeepMind vs "Chi Zhang" in hydrology
    both become "zhang c"), and a false self-eval flag wrongly discards an
    independent evaluation. Both sides come from the arXiv API, which gives
    consistently formatted full names, so exact full-name equality is reliable.
    """
    return " ".join(name.strip().lower().replace(".", " ").split())


def model_paper_authors(cards) -> dict[str, set[str]]:
    """model key -> normalised author set of that model's own defining paper.

    The defining papers (e.g. AlphaEarth's, TESSERA's) are themselves in the
    corpus, so their author lists are committed data — no extra API call.
    """
    tracked = _tracked_arxiv_ids()  # arxiv_id -> model key
    out: dict[str, set[str]] = {}
    for card in cards:
        if card.arxiv_id and card.arxiv_id in tracked:
            out[tracked[card.arxiv_id]] = {
                a for a in (_norm_author(x) for x in card.authors) if a
            }
    return out


def resolve_self_evaluation(*, arxiv_id: str | None, authors: list[str],
                            evaluated_models: list[str], llm_flag: bool,
                            model_authors: dict[str, set[str]]) -> bool:
    """Decide self_evaluation, mechanically wherever possible (§8).

    Semantics: TRUE means the authors evaluate a tracked FOUNDATION MODEL they
    themselves created — not merely that they built some downstream method.

    * The model's own defining paper -> True.
    * Evaluated model(s) whose defining-paper authors we know -> author overlap
      decides; the LLM's opinion is ignored (the check is computable).
    * Otherwise -> fall back to the extractor's flag.
    """
    if arxiv_id and arxiv_id in _tracked_arxiv_ids():
        return True
    known = [m for m in evaluated_models if m in model_authors]
    if known:
        paper_authors = {a for a in (_norm_author(x) for x in authors) if a}
        return any(paper_authors & model_authors[m] for m in known)
    return llm_flag


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
