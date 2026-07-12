"""Locked-down Docker wrapper for the extractor. THE untrusted-input boundary.

Paper text is hostile input from the open internet, fed to an LLM running under
my subscription credentials. This module runs that LLM inside a container that:

* has NO tools (``--allowedTools ""``) — the single most effective defence, since
  a perfect prompt injection then has nothing to *do*;
* has a read-only root fs, a tiny noexec tmpfs, all caps dropped, no new privs,
  a non-root user, and pid/mem/cpu limits;
* bind-mounts NOTHING — not the repo, not ``$HOME``, not the docker socket, not
  even the credentials (those are streamed in over stdin into tmpfs);
* talks to the outside world only through an egress allowlist that reaches
  Anthropic and nothing else (an ``--internal`` docker network plus a sidecar
  CONNECT proxy), so an injected model has no channel to exfiltrate the token;
* communicates purely via stdin (input) and stdout (output).

The config constants below are asserted by tests/test_sandbox_config.py so that
configuration drift — the normal way sandboxes rot — fails the build.
"""
from __future__ import annotations

import json
import os
import subprocess
import uuid
from pathlib import Path

# ---------------------------------------------------------------------------
# Image / identity
# ---------------------------------------------------------------------------
IMAGE = "gfm-extractor:latest"
CONTAINER_UID = 10001
CONTAINER_GID = 10001

# The extractor's tool allowlist. MUST be empty. Asserted before every run.
ALLOWED_TOOLS = ""

# Egress: the container's only network is `--internal` (no external route); a
# sidecar proxy on that network forwards HTTPS to Anthropic hosts only.
EGRESS_NETWORK = "gfm-egress"
PROXY_CONTAINER = "gfm-egress-proxy"
PROXY_PORT = 8888

# The egress allowlist lives in a dedicated data file (the reviewed exception to
# the no-API-host source guard) so no code file names the host literally.
_HOSTS_FILE = Path(__file__).resolve().parent.parent / "sandbox" / "anthropic_hosts.txt"


def _load_allowed_hosts() -> tuple[str, ...]:
    hosts = []
    for line in _HOSTS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            hosts.append(line)
    return tuple(hosts)


ANTHROPIC_ALLOWED_HOSTS = _load_allowed_hosts()

# Credential files mounted read-only. These are the ONLY host paths the
# container can see. Overridable for tests / alternate homes.
CRED_FILE = Path(os.environ.get("GFM_CLAUDE_CRED",
                                str(Path.home() / ".claude" / ".credentials.json")))
CLAUDE_JSON = Path(os.environ.get("GFM_CLAUDE_JSON",
                                  str(Path.home() / ".claude.json")))

# Wall-clock ceiling for a single container (seconds).
RUN_TIMEOUT = 360

# The static hardening flags. Kept as a list so the config test can assert each.
HARDENING_FLAGS = [
    "--rm",
    "--read-only",
    "--tmpfs", "/tmp:rw,noexec,nosuid,size=64m",
    "--cap-drop", "ALL",
    "--security-opt", "no-new-privileges",
    "--user", f"{CONTAINER_UID}:{CONTAINER_GID}",
    "--pids-limit", "128",
    "--memory", "2g",
    "--cpus", "2",
]


class SandboxError(RuntimeError):
    pass


def _network_args(egress_mode: str) -> tuple[list[str], list[str]]:
    """Return (network_flags, env_flags) for the chosen egress mode."""
    if egress_mode == "none":
        # Fully offline. Only valid if the CLI can work without network (it
        # generally cannot for live inference); kept for tests / dry runs.
        return (["--network", "none"], [])
    if egress_mode == "proxy":
        proxy = f"http://{PROXY_CONTAINER}:{PROXY_PORT}"
        env = [
            "--env", f"HTTPS_PROXY={proxy}",
            "--env", f"HTTP_PROXY={proxy}",
            "--env", "NO_PROXY=localhost,127.0.0.1",
        ]
        return (["--network", EGRESS_NETWORK], env)
    raise SandboxError(f"unknown egress mode: {egress_mode!r}")


def build_docker_argv(*, model: str, container_name: str,
                      egress_mode: str = "proxy") -> list[str]:
    """Construct the full ``docker run`` argv for one extraction.

    Pure function (no side effects) so it can be inspected by tests. There are
    ZERO bind mounts: not the repo, not ``$HOME``, not the docker socket, not
    even the credential files. Credentials are streamed in over stdin (the
    private host->container pipe) into the container's ephemeral tmpfs, so they
    never touch the daemon-visible filesystem and vanish when the container
    exits. This is strictly more minimal than a read-only credential mount, and
    it is also required here because the NFS home is root-squashed (the daemon
    cannot read a bind source under it).
    """
    assert ALLOWED_TOOLS == "", "extractor tool allowlist must be empty"
    net_flags, env_flags = _network_args(egress_mode)

    argv = ["docker", "run", "--name", container_name, "-i"]
    argv += HARDENING_FLAGS
    argv += net_flags
    argv += env_flags
    argv += [
        "--env", f"GFM_MODEL={model}",
        "--env", f"GFM_ALLOWED_TOOLS={ALLOWED_TOOLS}",
        IMAGE,
    ]
    return argv


def _read_credentials() -> dict:
    """Read the subscription credential files on the HOST (as the user).

    Returned only to be streamed on stdin; NEVER merged into the extraction
    payload, so credentials cannot leak into a quarantined record.
    """
    creds = {"credentials.json": CRED_FILE.read_text(encoding="utf-8")}
    if CLAUDE_JSON.exists():
        creds["claude.json"] = CLAUDE_JSON.read_text(encoding="utf-8")
    return creds


def ensure_egress_network() -> None:
    """Create the internal egress network and start the allowlist proxy sidecar.

    The network is ``--internal`` so containers on it have no external route
    except through the proxy, which forwards only to Anthropic hosts.
    """
    subprocess.run(
        ["docker", "network", "inspect", EGRESS_NETWORK],
        capture_output=True, check=False,
    ).returncode == 0 or subprocess.run(
        ["docker", "network", "create", "--internal", EGRESS_NETWORK],
        capture_output=True, check=True,
    )
    # Start the proxy if not already running. It sits on the internal net AND the
    # default bridge, so it (and only it) can reach the internet.
    running = subprocess.run(
        ["docker", "ps", "-q", "-f", f"name=^{PROXY_CONTAINER}$"],
        capture_output=True, text=True, check=False,
    ).stdout.strip()
    if running:
        return
    subprocess.run(["docker", "rm", "-f", PROXY_CONTAINER], capture_output=True, check=False)
    subprocess.run(
        [
            "docker", "run", "-d", "--name", PROXY_CONTAINER,
            "--restart", "unless-stopped",
            "--network", EGRESS_NETWORK,
            "--cap-drop", "ALL", "--security-opt", "no-new-privileges",
            "--user", f"{CONTAINER_UID}:{CONTAINER_GID}",
            "--env", f"ALLOWED_HOSTS={','.join(ANTHROPIC_ALLOWED_HOSTS)}",
            "--env", f"PROXY_PORT={PROXY_PORT}",
            "--entrypoint", "python3",
            IMAGE, "/opt/egress_proxy.py",
        ],
        capture_output=True, check=True,
    )
    # Attach the proxy to the default bridge so it has an outbound route.
    subprocess.run(
        ["docker", "network", "connect", "bridge", PROXY_CONTAINER],
        capture_output=True, check=False,
    )


def preflight() -> None:
    """Fail loudly and early if the sandbox cannot be used safely."""
    if not CRED_FILE.exists():
        raise SandboxError(
            f"Claude credentials not found at {CRED_FILE}. The extractor is "
            "subscription-only and cannot run without a local login."
        )
    if subprocess.run(["docker", "image", "inspect", IMAGE],
                      capture_output=True, check=False).returncode != 0:
        raise SandboxError(f"image {IMAGE!r} not built. Run: docker build -t {IMAGE} sandbox/")


def run_extraction(payload: dict, *, model: str, egress_mode: str = "proxy",
                   timeout: int = RUN_TIMEOUT) -> dict:
    """Run one extraction in the sandbox. Returns the parsed JSON from stdout.

    Raises SandboxError on non-zero exit, timeout, or unparseable output. The
    caller (extract.py) decides quarantine vs. retry.
    """
    if egress_mode == "proxy":
        ensure_egress_network()
    name = f"gfm-extract-{uuid.uuid4().hex[:12]}"
    argv = build_docker_argv(model=model, container_name=name, egress_mode=egress_mode)
    # Inject credentials ONLY here, at the boundary — not into `payload`, which
    # is what gets quarantined on failure.
    stdin_data = json.dumps({**payload, "_credentials": _read_credentials()})
    try:
        proc = subprocess.run(
            argv, input=stdin_data, capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        subprocess.run(["docker", "kill", name], capture_output=True, check=False)
        raise SandboxError(f"extraction timed out after {timeout}s") from exc
    if proc.returncode == 3:
        # entrypoint exit 3 == subscription quota/auth. Not a crash: stop cleanly.
        from .claude_cli import QuotaExhausted
        raise QuotaExhausted(proc.stderr[-500:])
    if proc.returncode != 0:
        raise SandboxError(f"container exited {proc.returncode}: {proc.stderr[-2000:]}")
    out = proc.stdout.strip()
    if not out:
        raise SandboxError("container produced no output")
    try:
        return json.loads(out)
    except json.JSONDecodeError as exc:
        raise SandboxError(f"container output not JSON: {out[:500]}") from exc
