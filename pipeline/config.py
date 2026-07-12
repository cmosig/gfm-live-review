"""Repository paths and vocabulary loading.

Everything the pipeline needs to know about *where things live* and *what the
controlled vocabularies are* is centralised here. Paths are all relative to the
repository root so the whole system is relocatable and `git clone`-restorable.
"""
from __future__ import annotations

import functools
from pathlib import Path

import yaml

# Repo root = parent of the `pipeline/` package directory.
REPO_ROOT = Path(__file__).resolve().parent.parent

TAXONOMY_PATH = REPO_ROOT / "taxonomy.yaml"
MODELS_PATH = REPO_ROOT / "models.yaml"

CARDS_DIR = REPO_ROOT / "cards"
QUARANTINE_DIR = REPO_ROOT / "quarantine"
STATE_DIR = REPO_ROOT / "state"
SITE_DIR = REPO_ROOT / "site"

SEEN_PATH = STATE_DIR / "seen.json"
PENDING_TAGS_PATH = STATE_DIR / "pending_tags.json"
RUNS_PATH = STATE_DIR / "runs.jsonl"
DATA_JSON_PATH = SITE_DIR / "data.json"

# Fixed metric vocabulary (never grows automatically).
METRICS = (
    "f1",
    "miou",
    "r2",
    "rmse",
    "nse",
    "accuracy",
    "auc",
    "balanced_accuracy",
)

# Metrics where a LOWER value is better (used to sanity-check `direction`).
LOWER_IS_BETTER = frozenset({"rmse"})

# Reserved baseline value: a bespoke, task-specific supervised model.
TASK_SPECIFIC = "task_specific"


def _read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


@functools.lru_cache(maxsize=1)
def load_taxonomy() -> dict:
    """Load taxonomy.yaml (cached). Call ``load_taxonomy.cache_clear()`` in tests."""
    return _read_yaml(TAXONOMY_PATH)


@functools.lru_cache(maxsize=1)
def load_models() -> dict:
    """Load models.yaml (cached)."""
    return _read_yaml(MODELS_PATH)


def axes() -> set[str]:
    return set(load_taxonomy().get("axes", []))


def tasks() -> set[str]:
    return set(load_taxonomy().get("tasks", []))


def limitations() -> set[str]:
    return set(load_taxonomy().get("limitations", []))


def promoted_tags() -> set[str]:
    return set(load_taxonomy().get("promoted_tags") or [])


def model_keys() -> set[str]:
    return {m["key"] for m in load_models().get("models", [])}


def valid_baselines() -> set[str]:
    """Legal values for Claim.baseline (besides None): model keys + task_specific."""
    return model_keys() | {TASK_SPECIFIC}


def model_aliases() -> dict[str, list[str]]:
    """Map model key -> list of lowercase aliases for screening."""
    out: dict[str, list[str]] = {}
    for m in load_models().get("models", []):
        out[m["key"]] = [a.lower() for a in m.get("aliases", [])]
    return out


def reload_vocab() -> None:
    """Drop cached taxonomy/models. Used after auto-promoting tags, and in tests."""
    load_taxonomy.cache_clear()
    load_models.cache_clear()
