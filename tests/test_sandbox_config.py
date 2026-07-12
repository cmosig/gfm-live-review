"""§6 mitigation-6: assert the docker invocation stays locked down.

Configuration drift is the normal way sandboxes die, so these assertions make
drift fail the build rather than silently weaken isolation.
"""
from __future__ import annotations

from pathlib import Path

from pipeline import sandbox

ROOT = Path(__file__).resolve().parent.parent


def _argv(egress_mode="proxy"):
    return sandbox.build_docker_argv(model="claude-opus-4-8",
                                     container_name="test", egress_mode=egress_mode)


def test_empty_tool_allowlist():
    assert sandbox.ALLOWED_TOOLS == "", "extractor must have NO tools"


def test_hardening_flags_present():
    argv = _argv()
    joined = " ".join(argv)
    assert "--cap-drop" in argv and "ALL" in argv
    assert "--read-only" in argv
    assert "no-new-privileges" in joined
    assert "--pids-limit" in argv
    assert "--memory" in argv
    assert "--cpus" in argv


def test_runs_as_non_root_user():
    argv = _argv()
    i = argv.index("--user")
    uid = argv[i + 1].split(":")[0]
    assert uid.isdigit() and int(uid) != 0, "must run as a non-root UID"


def test_tmpfs_is_noexec():
    argv = _argv()
    i = argv.index("--tmpfs")
    assert "noexec" in argv[i + 1] and "nosuid" in argv[i + 1]


def test_no_forbidden_mounts():
    """No -v mount may expose the repo root, $HOME (beyond the cred files), or
    the docker socket."""
    argv = _argv()
    repo_root = str(ROOT)
    home = str(Path.home())
    for i, tok in enumerate(argv):
        if tok != "-v":
            continue
        src = argv[i + 1].split(":", 1)[0]
        assert "docker.sock" not in src, "docker socket must never be mounted"
        assert src != repo_root and not src.startswith(repo_root + "/"), \
            f"repo must not be mounted: {src}"
        # $HOME is only allowed via the two specific credential files.
        if src.startswith(home):
            assert src in (str(sandbox.CRED_FILE), str(sandbox.CLAUDE_JSON)), \
                f"only credential files may come from $HOME: {src}"


def test_no_bind_mounts_at_all():
    # Credentials are streamed on stdin, not mounted, so there are ZERO -v
    # mounts: not the repo, not $HOME, not the docker socket, not even creds.
    argv = _argv()
    assert "-v" not in argv and "--volume" not in argv


def test_credentials_never_enter_the_quarantinable_payload(monkeypatch, tmp_path):
    # The payload extract.py holds (and may quarantine) must not contain creds;
    # creds are injected only at the docker boundary, onto stdin.
    from pipeline import extract
    from datetime import date
    meta = extract.PaperMeta(key="k1", title="T", date=date(2025, 1, 1), arxiv_id="1")
    payload = extract.build_payload("some paper text", meta)
    assert "_credentials" not in payload
    import json
    assert "credentials" not in json.dumps(payload).lower()


def test_egress_not_host_network():
    argv = _argv("proxy")
    # Must be on the isolated internal network, never host networking.
    assert "host" not in _network_values(argv)
    assert sandbox.EGRESS_NETWORK in argv


def test_egress_none_mode_is_offline():
    argv = _argv("none")
    assert "none" in _network_values(argv)


def _network_values(argv):
    return [argv[i + 1] for i, t in enumerate(argv) if t == "--network"]


def test_allowlist_is_anthropic_only():
    # Every allowlisted host is an anthropic host; nothing else can be reached.
    assert sandbox.ANTHROPIC_ALLOWED_HOSTS
    for host in sandbox.ANTHROPIC_ALLOWED_HOSTS:
        assert host.endswith("anthropic.com")
