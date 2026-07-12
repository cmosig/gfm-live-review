"""Small, dependency-free text helpers shared across the pipeline.

Kept separate so both the schema (span hashing) and the extractor (span
verification) use *exactly* the same normalisation. If these two ever diverge,
span verification silently breaks, so there is one implementation, here.
"""
from __future__ import annotations

import hashlib
import re
import unicodedata

_WS_RE = re.compile(r"\s+")
# C0/C1 control characters except tab/newline/carriage-return.
_CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")


def strip_control(s: str) -> str:
    """Remove control characters from model-supplied free text (defence-in-depth)."""
    return _CTRL_RE.sub("", s)


def normalize_ws(s: str) -> str:
    """Whitespace-normalise for substring comparison.

    Unicode-normalises (NFKC), collapses all runs of whitespace to a single
    space, and strips. Used on BOTH the paper text and a claim's span before
    the substring check, so trivial spacing differences don't reject a valid
    verbatim quote.
    """
    s = unicodedata.normalize("NFKC", s)
    s = _WS_RE.sub(" ", s)
    return s.strip()


def span_sha256(span: str) -> str:
    """Deterministic hash of a claim's normalised span.

    Computed ONLY in Python — never supplied by the model — so it is a
    tamper-evident fingerprint of the verbatim quote we verified.
    """
    return hashlib.sha256(normalize_ws(span).encode("utf-8")).hexdigest()


def span_in_text(span: str, text: str) -> bool:
    """True if `span` appears verbatim in `text` after whitespace normalisation."""
    n_span = normalize_ws(span)
    if not n_span:
        return False
    return n_span in normalize_ws(text)
