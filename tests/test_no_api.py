"""The §5 no-API guard: the whole point of the project, enforced mechanically.

Greps the entire source tree and fails if anything reintroduces an API-key code
path or the Anthropic API SDK. The forbidden literals are assembled from
fragments below so THIS file does not itself trip the grep.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

# Needles built from fragments so they don't appear literally in this file.
API_KEY = "ANTHROPIC" + "_API_KEY"
API_HOST = "api." + "anthropic" + ".com"

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".pytest_cache", ".ruff_cache"}
# Generated artefacts may legitimately quote paper text; the egress allowlist is
# the single reviewed exception that must name the Anthropic host.
SKIP_FILES = {
    ROOT / "site" / "data.json",
    ROOT / "site" / "index.html",
    ROOT / "sandbox" / "anthropic_hosts.txt",
}
TEXT_SUFFIXES = {".py", ".toml", ".yaml", ".yml", ".md", ".txt", ".js", ".css",
                 ".html", ".j2", ".service", ".timer", ".sh", ".cfg", ".ini",
                 ".json", "", "Dockerfile"}


def _source_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path in SKIP_FILES:
            continue
        if path.name == "Dockerfile" or path.suffix in TEXT_SUFFIXES:
            yield path


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return ""


def test_no_api_key_anywhere():
    offenders = [p for p in _source_files() if API_KEY in _read(p)]
    assert not offenders, f"{API_KEY} must not appear in: {offenders}"


def test_no_anthropic_api_host_anywhere():
    offenders = [p for p in _source_files() if API_HOST in _read(p)]
    assert not offenders, (
        f"{API_HOST} may only appear in the reviewed egress allowlist; found in: {offenders}")


def test_no_anthropic_sdk_import():
    imp = re.compile(r"^\s*(?:import\s+anthropic|from\s+anthropic\b)", re.MULTILINE)
    offenders = [p for p in _source_files() if p.suffix == ".py" and imp.search(_read(p))]
    assert not offenders, f"the anthropic SDK must not be imported: {offenders}"


def test_pyproject_has_no_anthropic_sdk_dependency():
    text = _read(ROOT / "pyproject.toml")
    # Match a dependency spec like anthropic==x or "anthropic>=" — NOT the
    # explanatory comment that forbids it.
    dep = re.compile(r'["\']?anthropic["\']?\s*[<>=~!]')
    assert not dep.search(text), "pyproject must not depend on the anthropic SDK"


def test_dockerfile_has_no_python_anthropic_sdk():
    text = _read(ROOT / "sandbox" / "Dockerfile")
    # The Claude Code CLI (@anthropic-ai/claude-code, an npm package) is fine;
    # a Python `pip install anthropic` / SDK reference is not.
    assert "pip install anthropic" not in text
    assert not re.search(r"\banthropic==", text)
    # Sanity: the CLI package IS present (extraction depends on it).
    assert "@anthropic-ai/claude-code" in text


def test_no_requests_module_available_in_sandbox_image():
    # The extractor image must not ship a Python HTTP client that could talk to
    # the API directly; it installs no pip packages at all.
    text = _read(ROOT / "sandbox" / "Dockerfile")
    assert "pip install" not in text
