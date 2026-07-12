"""Cron entrypoint. Orchestrates one full daily run, crash-safely.

    [host]      ingest -> screen -> verify        (pure Python, no creds)
    [container] extract                            (claude -p, sandboxed)
    [host]      validate -> aggregate -> build     (pure Python)
    [host]      git commit && git push             (creds live here only)

Guarantees:
  * A lockfile prevents overlapping runs.
  * `seen.json` is updated ONLY after a paper is successfully carded, so an
    interrupted or quota-exhausted run resumes cleanly tomorrow.
  * One bad paper never breaks the run (quarantine, continue).
  * Quota exhaustion is not a failure: stop processing, commit what exists,
    exit 0. The process exits non-zero ONLY on an unhandled error.
"""
from __future__ import annotations

import argparse
import os
import sys
import time
import traceback
from datetime import date, datetime, timezone

import yaml

from . import cards as cards_mod
from . import config, extract, ingest, quarantine, screen, state, verify
from .aggregate import compute_tag_promotion
from .build import build
from .claude_cli import QuotaExhausted

# Seed corpus (arXiv ids). 1-2 are the models themselves; the rest downstream.
SEED_ARXIV_IDS = [
    "2507.22291", "2506.20380", "2601.00857", "2601.01558", "2606.20034",
    "2605.18667", "2511.01408", "2602.17250", "2601.07268", "2604.03456",
    "2603.16911", "2606.20697", "2605.10029",
]

LOCK_PATH = config.STATE_DIR / ".lock"
PER_PAPER_SLEEP = 5.0


# ---------------------------------------------------------------------------
# Lockfile
# ---------------------------------------------------------------------------
class _Lock:
    def __enter__(self):
        config.STATE_DIR.mkdir(parents=True, exist_ok=True)
        try:
            self.fd = os.open(LOCK_PATH, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            raise SystemExit(f"another run holds the lock: {LOCK_PATH}")
        os.write(self.fd, f"{os.getpid()}\n".encode())
        return self

    def __exit__(self, *exc):
        os.close(self.fd)
        try:
            LOCK_PATH.unlink()
        except FileNotFoundError:
            pass


# ---------------------------------------------------------------------------
# Git
# ---------------------------------------------------------------------------
def _git(*args: str, check: bool = True) -> int:
    import subprocess
    r = subprocess.run(["git", "-C", str(config.REPO_ROOT), *args],
                       capture_output=True, text=True)
    if r.stdout.strip():
        print(r.stdout.strip(), file=sys.stderr)
    if check and r.returncode != 0:
        print(r.stderr.strip(), file=sys.stderr)
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.returncode


def git_pull() -> None:
    if (config.REPO_ROOT / ".git").exists():
        _git("pull", "--rebase", "--autostash", check=False)


def git_commit_push(msg: str, *, push: bool) -> None:
    if not (config.REPO_ROOT / ".git").exists():
        return
    _git("add", "-A", check=False)
    # Nothing staged -> nothing to do.
    import subprocess
    diff = subprocess.run(["git", "-C", str(config.REPO_ROOT), "diff", "--cached", "--quiet"])
    if diff.returncode == 0:
        return
    _git("commit", "-m", msg, check=False)
    if push:
        _git("push", check=False)


# ---------------------------------------------------------------------------
# Taxonomy growth
# ---------------------------------------------------------------------------
# Everything above this sentinel in taxonomy.yaml is human-curated (with its
# comments) and preserved verbatim; the promoted_tags block below is rewritten.
TAXONOMY_SENTINEL = "# >>> auto-managed below (auto-promoted tags); human edits above are preserved >>>"


def apply_tag_promotion(all_cards) -> tuple[list[str], dict]:
    pending = state.load_pending_tags()
    promote, new_pending = compute_tag_promotion(all_cards, pending)
    text = config.TAXONOMY_PATH.read_text(encoding="utf-8")
    existing = set(yaml.safe_load(text).get("promoted_tags") or [])
    final = sorted(existing | set(promote))

    head = text.split(TAXONOMY_SENTINEL, 1)[0].rstrip()
    block = "\n".join(f"- {t}" for t in final) if final else "[]"
    new_text = f"{head}\n\n{TAXONOMY_SENTINEL}\npromoted_tags:\n{block}\n" if final \
        else f"{head}\n\n{TAXONOMY_SENTINEL}\npromoted_tags: []\n"
    if new_text != text:
        config.TAXONOMY_PATH.write_text(new_text, encoding="utf-8")
        config.reload_vocab()
    state.save_pending_tags(new_pending)
    return promote, new_pending


# ---------------------------------------------------------------------------
# Extractor selection
# ---------------------------------------------------------------------------
def _make_run_fn(mode: str, egress_mode: str):
    if mode == "sandbox":
        from . import sandbox
        sandbox.preflight()
        return lambda payload, model: sandbox.run_extraction(
            payload, model=model, egress_mode=egress_mode)
    if mode == "host":
        from . import hostextract
        return lambda payload, model: hostextract.run_extraction(payload, model=model)
    raise SystemExit(f"unknown extractor mode: {mode}")


# ---------------------------------------------------------------------------
# One paper
# ---------------------------------------------------------------------------
def process_paper(vr: verify.VerifyResult, run_fn, seen: dict,
                  existing_keys: set[str]) -> str:
    """Fetch, extract, and card one paper. Returns a short status string.

    Updates `seen` ONLY on a terminal outcome (carded or quarantined), never on
    a transient/quota failure, so those resume tomorrow.
    """
    from .fetchtext import fetch_arxiv_text, slice_for_extraction
    cand = vr.candidate

    if vr.doi_status == "mismatch":
        quarantine.write(
            state.title_key(cand.title)[:60] or "mismatch",
            title=cand.title, reason="DOI title mismatch (possible metadata error)",
            payload={"candidate": cand.to_dict()})
        state.mark_seen(seen, title=cand.title, key="-", status="quarantined_mismatch")
        return "quarantined:doi_mismatch"

    if not cand.arxiv_id:
        return "skip:no_arxiv_text_source"  # transient: try other sources later

    key = extract.make_card_key(cand.authors, cand.date or date.today(), cand.title,
                                existing=existing_keys)
    meta = extract.PaperMeta(
        key=key, title=cand.title, date=cand.date or date.today(),
        authors=cand.authors, arxiv_id=cand.arxiv_id, doi=vr.doi,
        doi_status=vr.doi_status, venue=cand.venue,
        self_evaluation=vr.self_evaluation,
    )

    text = fetch_arxiv_text(cand.arxiv_id)
    text = slice_for_extraction(text)

    result = extract.extract_card(meta, text, run_fn=run_fn)
    if result.quarantined:
        quarantine.write(key, title=cand.title, reason=result.reason,
                         payload=result.payload, extra={"raw_output": result.raw})
        state.mark_seen(seen, title=cand.title, key=key, status="quarantined")
        return f"quarantined:{result.reason[:40]}"

    cards_mod.write_card(result.card)
    existing_keys.add(key)
    state.mark_seen(seen, title=cand.title, key=key, status="carded",
                    arxiv_id=cand.arxiv_id, dropped_claims=result.dropped_claims)
    return f"carded:{key}({len(result.card.claims)} claims)"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def run(*, seed: bool, extractor: str, egress_mode: str, push: bool,
        use_git: bool, limit: int | None) -> int:
    started = datetime.now(timezone.utc)
    stats = {"ingested": 0, "accepted": 0, "new": 0, "carded": 0,
             "quarantined": 0, "skipped": 0, "quota_stopped": False}

    if use_git:
        git_pull()

    seen = state.load_seen()
    existing_cards = cards_mod.load_all_cards()
    existing_keys = {c.key for c in existing_cards}
    existing_titles = {state.title_key(c.title) for c in existing_cards}

    # --- ingest ---
    if seed:
        candidates = ingest.fetch_arxiv_by_ids(SEED_ARXIV_IDS)
    else:
        candidates = ingest.fetch_arxiv_recent()
        try:
            candidates += ingest.fetch_openalex_recent(_last_run_date())
        except Exception as exc:  # OpenAlex is best-effort
            print(f"openalex ingest failed (continuing): {exc}", file=sys.stderr)
    stats["ingested"] = len(candidates)

    # --- screen ---
    accepted, rejected = screen.screen(candidates)
    stats["accepted"] = len(accepted)
    for r in rejected:
        state.append_run({"event": "rejected", "title": r.candidate.title, "reason": r.reason})

    run_fn = _make_run_fn(extractor, egress_mode)

    # --- per paper ---
    processed = 0
    for sr in accepted:
        cand = sr.candidate
        if not cand.title:
            continue
        vr = verify.verify(cand, seen, existing_titles)
        if vr.is_duplicate:
            stats["skipped"] += 1
            continue
        stats["new"] += 1
        if limit is not None and processed >= limit:
            print(f"reached --limit {limit}, stopping", file=sys.stderr)
            break
        try:
            status = process_paper(vr, run_fn, seen, existing_keys)
        except QuotaExhausted as exc:
            print(f"QUOTA EXHAUSTED, stopping cleanly: {exc}", file=sys.stderr)
            stats["quota_stopped"] = True
            break
        except Exception as exc:  # one bad paper must not break the run
            print(f"paper failed (continuing): {cand.title[:60]}: {exc}", file=sys.stderr)
            traceback.print_exc()
            state.append_run({"event": "paper_error", "title": cand.title, "error": str(exc)})
            continue
        finally:
            # Persist seen after every paper so progress survives a crash.
            state.save_seen(seen)
        processed += 1
        print(f"  {status}", file=sys.stderr)
        if status.startswith("carded"):
            stats["carded"] += 1
        elif status.startswith("quarantined"):
            stats["quarantined"] += 1
        else:
            stats["skipped"] += 1
        existing_titles.add(state.title_key(cand.title))
        time.sleep(PER_PAPER_SLEEP)

    # --- taxonomy growth, aggregate, build ---
    all_cards = cards_mod.load_all_cards()
    promoted, pending = apply_tag_promotion(all_cards)
    if promoted:
        print(f"promoted tags: {promoted}", file=sys.stderr)
    build(quarantine_count=quarantine.count())

    # --- run log & commit ---
    duration = (datetime.now(timezone.utc) - started).total_seconds()
    state.append_run({"event": "run", "seed": seed, "extractor": extractor,
                      "duration_s": round(duration, 1), **stats,
                      "n_cards": len(all_cards), "quarantine": quarantine.count()})
    if use_git:
        msg = (f"run: +{stats['carded']} cards, {stats['quarantined']} quarantined, "
               f"{len(all_cards)} total")
        git_commit_push(msg, push=push)

    print(f"DONE: {stats}", file=sys.stderr)
    return 0


def _last_run_date() -> date:
    """Publication-date floor for the daily OpenAlex sweep: last successful run."""
    if not config.RUNS_PATH.exists():
        return date(2025, 1, 1)
    import json
    last = None
    for line in config.RUNS_PATH.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("event") == "run":
            last = rec.get("ts")
    if not last:
        return date(2025, 1, 1)
    return datetime.fromisoformat(last).date()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="gfm-live-review daily run")
    p.add_argument("--seed", action="store_true", help="ingest the seed corpus")
    p.add_argument("--extractor", choices=["sandbox", "host"], default="sandbox",
                   help="'sandbox' (Docker, production) or 'host' (bootstrap only)")
    p.add_argument("--egress-mode", choices=["proxy", "none"], default="proxy")
    p.add_argument("--no-push", action="store_true", help="commit but do not push")
    p.add_argument("--no-git", action="store_true", help="skip all git operations")
    p.add_argument("--limit", type=int, default=None, help="cap papers processed this run")
    args = p.parse_args(argv)

    try:
        with _Lock():
            return run(seed=args.seed, extractor=args.extractor,
                       egress_mode=args.egress_mode, push=not args.no_push,
                       use_git=not args.no_git, limit=args.limit)
    except SystemExit:
        raise
    except Exception:
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
