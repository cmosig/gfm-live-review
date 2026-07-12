"""Fetch and slice paper text on the HOST (never in the sandbox).

The host does all network fetching; the container only ever sees the resulting
text on stdin. We prefer arXiv's HTML rendering (clean, tables preserved) and
fall back to the PDF via PyMuPDF. The text is then sliced to the sections that
carry claims — abstract, intro, results/tables, conclusion — and capped, with
the *middle* truncated but numeric/table lines always kept, because that is
where the numbers a claim must cite actually live.
"""
from __future__ import annotations

import re
from html.parser import HTMLParser

from . import http

# ~4 chars/token; 20k token budget -> ~80k char cap.
CHAR_CAP = 80_000
_NUM_RE = re.compile(r"\d")


class _TextExtractor(HTMLParser):
    """Minimal HTML->text: drop script/style, keep block structure as newlines."""

    _SKIP = {"script", "style", "noscript", "head"}
    _BLOCK = {"p", "div", "br", "li", "tr", "table", "h1", "h2", "h3", "h4",
              "section", "figcaption", "caption", "td", "th"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self._SKIP:
            self._skip_depth += 1
        elif tag in self._BLOCK:
            self._chunks.append("\n")

    def handle_endtag(self, tag):
        if tag in self._SKIP and self._skip_depth:
            self._skip_depth -= 1
        elif tag in self._BLOCK:
            self._chunks.append("\n")

    def handle_data(self, data):
        if self._skip_depth == 0:
            self._chunks.append(data)

    def text(self) -> str:
        raw = "".join(self._chunks)
        # collapse >2 newlines, trim trailing spaces per line
        lines = [ln.strip() for ln in raw.splitlines()]
        out, blank = [], False
        for ln in lines:
            if ln:
                out.append(ln)
                blank = False
            elif not blank:
                out.append("")
                blank = True
        return "\n".join(out).strip()


def html_to_text(html: str) -> str:
    p = _TextExtractor()
    p.feed(html)
    return p.text()


def fetch_arxiv_text(arxiv_id: str) -> str:
    """Fetch paper text: arXiv HTML first, PDF (PyMuPDF) as fallback."""
    # 1. HTML rendering.
    try:
        resp = http.get(f"https://arxiv.org/html/{arxiv_id}", retries=2)
        if "html" in resp.headers.get("Content-Type", "") and len(resp.text) > 2000:
            text = html_to_text(resp.text)
            if len(text) > 1000:
                return text
    except http.HttpError:
        pass
    # 2. PDF fallback.
    return fetch_pdf_text(f"https://arxiv.org/pdf/{arxiv_id}")


def fetch_pdf_text(url: str) -> str:
    import fitz  # PyMuPDF, imported lazily

    resp = http.get(url, retries=2)
    doc = fitz.open(stream=resp.content, filetype="pdf")
    try:
        return "\n".join(page.get_text() for page in doc)
    finally:
        doc.close()


def _looks_tabular(line: str) -> bool:
    """Heuristic: a line with several numbers is probably a results/table row."""
    return len(_NUM_RE.findall(line)) >= 3


def slice_for_extraction(text: str, *, cap: int = CHAR_CAP) -> str:
    """Cap the text, truncating the middle but preserving tabular/numeric lines.

    Keeps a generous head (abstract+intro) and tail (results+conclusion). If
    still over budget, the middle is dropped except for lines that look like
    table rows — those carry the numbers a claim's span must quote.
    """
    text = text.strip()
    if len(text) <= cap:
        return text

    head_budget = cap // 2
    tail_budget = cap - head_budget
    head = text[:head_budget]
    tail = text[-tail_budget:]

    # From the dropped middle, salvage tabular lines within a small extra budget.
    middle = text[head_budget:-tail_budget]
    salvage_budget = cap // 4
    salvaged: list[str] = []
    used = 0
    for line in middle.splitlines():
        if _looks_tabular(line):
            if used + len(line) + 1 > salvage_budget:
                break
            salvaged.append(line)
            used += len(line) + 1

    parts = [head, "\n\n[... middle truncated; table rows preserved ...]\n\n"]
    if salvaged:
        parts.append("\n".join(salvaged))
        parts.append("\n\n[... end preserved tables ...]\n\n")
    parts.append(tail)
    return "".join(parts)
