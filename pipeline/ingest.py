"""Ingest candidate papers from keyless public APIs (arXiv, OpenAlex).

No scraping, no headless browsers, no Google Scholar. Just the official Atom /
JSON endpoints, queried serially with a courtesy sleep. Produces a list of
``Candidate`` dicts; screening (screen.py) decides which survive. DOIs captured
here come *only* from provider metadata and are the sole source of DOIs in the
system — the LLM never sees or supplies one.
"""
from __future__ import annotations

import sys
from dataclasses import asdict, dataclass, field
from datetime import date, datetime

import feedparser

from . import config, http

ARXIV_API = "http://export.arxiv.org/api/query"
OPENALEX_API = "https://api.openalex.org/works"

# arXiv categories we watch on the daily sweep.
ARXIV_CATEGORIES = ("cs.CV", "cs.LG", "eess.IV")


@dataclass
class Candidate:
    title: str
    abstract: str
    authors: list[str] = field(default_factory=list)
    author_ids: list[str] = field(default_factory=list)  # OpenAlex author ids
    arxiv_id: str | None = None
    doi: str | None = None            # from provider metadata only
    venue: str | None = None
    date: date | None = None
    openalex_id: str | None = None
    source: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        d["date"] = self.date.isoformat() if self.date else None
        return d


def _parse_arxiv_id(entry) -> str | None:
    # entry.id looks like http://arxiv.org/abs/2506.20380v1
    raw = getattr(entry, "id", "") or ""
    tail = raw.rsplit("/abs/", 1)[-1]
    if not tail:
        return None
    # strip version suffix
    return tail.split("v")[0] if tail[0].isdigit() else tail


def _arxiv_entries_to_candidates(feed) -> list[Candidate]:
    out: list[Candidate] = []
    for e in feed.entries:
        pub = getattr(e, "published_parsed", None)
        d = date(pub.tm_year, pub.tm_mon, pub.tm_mday) if pub else None
        doi = getattr(e, "arxiv_doi", None)
        out.append(
            Candidate(
                title=" ".join((getattr(e, "title", "") or "").split()),
                abstract=" ".join((getattr(e, "summary", "") or "").split()),
                authors=[a.get("name", "") for a in getattr(e, "authors", [])],
                arxiv_id=_parse_arxiv_id(e),
                doi=doi,
                venue="arXiv",
                date=d,
                source="arxiv",
            )
        )
    return out


def fetch_arxiv_by_ids(ids: list[str]) -> list[Candidate]:
    """Fetch specific arXiv papers by id (used for the seed corpus)."""
    if not ids:
        return []
    resp = http.get(ARXIV_API, params={"id_list": ",".join(ids), "max_results": len(ids)})
    return _arxiv_entries_to_candidates(feedparser.parse(resp.text))


def fetch_arxiv_search(query: str, *, max_results: int = 50) -> list[Candidate]:
    """Full-text arXiv search (used for daily model-name sweeps)."""
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    resp = http.get(ARXIV_API, params=params)
    http.courtesy_sleep()
    return _arxiv_entries_to_candidates(feedparser.parse(resp.text))


def fetch_arxiv_recent(*, max_results: int = 50) -> list[Candidate]:
    """Daily sweep: category firehose + one full-text query per model name."""
    cats = " OR ".join(f"cat:{c}" for c in ARXIV_CATEGORIES)
    out: list[Candidate] = []
    # Each query is best-effort: a transient arXiv failure on one must not sink
    # the whole daily sweep (which would crash the nightly run).
    def _try(query: str, *, max_results: int) -> None:
        try:
            http.courtesy_sleep()
            out.extend(fetch_arxiv_search(query, max_results=max_results))
        except http.HttpError as exc:
            print(f"daily query skipped ({query!r}): {exc}", file=sys.stderr)

    # A broad category query, filtered later by screen.py.
    _try(f"({cats}) AND (all:foundation model AND all:remote sensing)",
         max_results=max_results)
    for aliases in config.model_aliases().values():
        if not aliases:
            continue
        _try(f'all:"{aliases[0]}"', max_results=25)
    return out


def fetch_arxiv_backfill(*, per_query: int = 100) -> list[Candidate]:
    """Exhaustive one-off sweep to grow the corpus: every model alias + topical
    queries, paginated, deduplicated by arXiv id. Screening decides relevance.
    """
    queries: list[str] = []
    for aliases in config.model_aliases().values():
        for alias in aliases[:2]:  # the two most specific aliases per model
            queries.append(f'all:"{alias}"')
    queries += [
        'all:"geospatial foundation model"',
        'all:"earth observation foundation model"',
        'all:"remote sensing foundation model"',
        'all:"satellite embeddings"',
        'all:"earth embeddings"',
        'abs:"foundation model" AND abs:"remote sensing"',
        'abs:"pretrained" AND abs:"earth observation"',
    ]
    seen_ids: set[str] = set()
    out: list[Candidate] = []
    for q in queries:
        # arXiv rate-limits (HTTP 429) if hit too fast; one query's failure must
        # not sink the whole sweep, so skip a transiently-failing query and keep
        # what the others returned. A courtesy pause between pages keeps us under
        # arXiv's ~1-request-per-3s guidance and avoids tripping the limit at all.
        try:
            for start in range(0, per_query, 50):
                http.courtesy_sleep()
                batch = _arxiv_search_page(q, start=start, max_results=50)
                new = [c for c in batch if c.arxiv_id and c.arxiv_id not in seen_ids]
                for c in new:
                    seen_ids.add(c.arxiv_id)
                out += new
                if len(batch) < 50:
                    break  # no more pages for this query
        except http.HttpError as exc:
            print(f"backfill query skipped ({q!r}): {exc}", file=sys.stderr)
            continue
    return out


def _arxiv_search_page(query: str, *, start: int, max_results: int) -> list[Candidate]:
    params = {
        "search_query": query, "start": start, "max_results": max_results,
        "sortBy": "submittedDate", "sortOrder": "descending",
    }
    resp = http.get(ARXIV_API, params=params)
    http.courtesy_sleep()
    return _arxiv_entries_to_candidates(feedparser.parse(resp.text))


def fetch_openalex_recent(since: date, *, per_page: int = 50) -> list[Candidate]:
    """OpenAlex works published since `since`, in the polite pool."""
    params = {
        "filter": f"from_publication_date:{since.isoformat()},title.search:foundation model",
        "per-page": per_page,
        "mailto": http.MAILTO,
    }
    try:
        resp = http.get(OPENALEX_API, params=params)
    except http.HttpError:
        return []
    http.courtesy_sleep()
    data = resp.json()
    out: list[Candidate] = []
    for w in data.get("results", []):
        pub = w.get("publication_date")
        d = datetime.strptime(pub, "%Y-%m-%d").date() if pub else None
        authors, author_ids = [], []
        for auth in w.get("authorships", []):
            a = auth.get("author", {})
            if a.get("display_name"):
                authors.append(a["display_name"])
            if a.get("id"):
                author_ids.append(a["id"])
        out.append(
            Candidate(
                title=" ".join((w.get("title") or "").split()),
                abstract=_reconstruct_abstract(w.get("abstract_inverted_index")),
                authors=authors,
                author_ids=author_ids,
                doi=(w.get("doi") or "").replace("https://doi.org/", "") or None,
                venue=(w.get("host_venue") or {}).get("display_name"),
                date=d,
                openalex_id=w.get("id"),
                source="openalex",
            )
        )
    return out


def _reconstruct_abstract(inv_index: dict | None) -> str:
    if not inv_index:
        return ""
    positions: list[tuple[int, str]] = []
    for word, idxs in inv_index.items():
        for i in idxs:
            positions.append((i, word))
    positions.sort()
    return " ".join(w for _, w in positions)
