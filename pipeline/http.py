"""A tiny, polite HTTP helper for the keyless public APIs we use.

Fixed retries with backoff, a descriptive User-Agent (OpenAlex/Crossref reward
this with the "polite pool"), and a hard timeout. No parallelism anywhere in
this project — the daily job has all day, and politeness beats speed.
"""
from __future__ import annotations

import time

import requests

# Contact string for the polite pool. Not a credential.
MAILTO = "clemens.mosig@gmail.com"
USER_AGENT = f"gfm-live-review/0.1 (+https://github.com/; mailto:{MAILTO})"

DEFAULT_TIMEOUT = 30
_SLEEP = 3.0  # fixed courtesy sleep between calls


class HttpError(RuntimeError):
    """An HTTP failure. `transient` is True for retryable conditions (network
    errors, 429/5xx) and False for permanent ones (a 404/410 for a withdrawn or
    wrong id will fail identically forever), so callers can retry the former but
    must not re-fetch the latter every run. `status_code` is the HTTP status
    when the failure carried one, else None."""

    def __init__(self, message: str, *, status_code: int | None = None,
                 transient: bool = False):
        super().__init__(message)
        self.status_code = status_code
        self.transient = transient


def get(url: str, *, params: dict | None = None, accept: str | None = None,
        retries: int = 3, timeout: int = DEFAULT_TIMEOUT) -> requests.Response:
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    last_exc: Exception | None = None
    for attempt in range(retries):
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=timeout)
            if resp.status_code == 200:
                return resp
            # Retry on transient server / rate-limit responses only.
            if resp.status_code in (429, 500, 502, 503, 504):
                last_exc = HttpError(f"{resp.status_code} for {resp.url}",
                                     status_code=resp.status_code, transient=True)
            else:
                raise HttpError(f"{resp.status_code} for {resp.url}",
                                status_code=resp.status_code, transient=False)
        except requests.RequestException as exc:  # network-level failure: retryable
            last_exc = exc
        time.sleep(_SLEEP * (attempt + 1))
    raise HttpError(f"GET failed after {retries} attempts: {url}: {last_exc}",
                    transient=True)


def courtesy_sleep() -> None:
    time.sleep(_SLEEP)
