#!/usr/bin/env bash
# Prove the extraction sandbox is actually isolated (DoD §11.3). Run after
# `docker build -t gfm-extractor:latest sandbox/`. Each check FAILS LOUDLY if the
# container can do something it must not.
set -u
IMG=gfm-extractor:latest
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail() { echo "FAIL: $1"; exit 1; }
pass() { echo "PASS: $1"; }

echo "== 1. The container cannot see the repo =="
# We never mount the repo. Prove cards/ is invisible from inside the container.
if docker run --rm --entrypoint python3 "$IMG" -c \
     "import os,sys; sys.exit(0 if not os.path.exists('/cards') and not os.path.exists('$REPO_ROOT') else 1)"; then
  pass "repo path and /cards are not visible inside the container"
else
  fail "container can see the repo"
fi

echo "== 2. The container cannot write outside /tmp (read-only rootfs) =="
if docker run --rm --read-only --tmpfs /tmp:rw,noexec,nosuid,size=64m \
     --cap-drop ALL --security-opt no-new-privileges --user 10001:10001 \
     --entrypoint python3 "$IMG" -c \
     "open('/home/extractor/x','w')" 2>/dev/null; then
  fail "container wrote outside /tmp"
else
  pass "root filesystem is read-only; writes outside /tmp are refused"
fi
# ... and /tmp IS writable:
docker run --rm --read-only --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --entrypoint python3 "$IMG" -c "open('/tmp/ok','w').write('ok')" \
  && pass "/tmp is writable (as intended)" || fail "/tmp should be writable"

echo "== 3. The container cannot reach a non-Anthropic host =="
# On the internal egress network the ONLY route out is the allowlist proxy.
# Reaching a non-allowlisted host must fail. (example.com is not on the list.)
docker network inspect gfm-egress >/dev/null 2>&1 || \
  docker network create --internal gfm-egress >/dev/null
if docker run --rm --network gfm-egress \
     --env HTTPS_PROXY=http://gfm-egress-proxy:8888 \
     --entrypoint python3 "$IMG" -c \
     "import urllib.request,sys
try:
    urllib.request.urlopen('https://example.com', timeout=8); sys.exit(1)
except Exception as e:
    print('blocked:', type(e).__name__); sys.exit(0)"; then
  pass "egress to a non-Anthropic host is blocked"
else
  fail "container reached a non-Anthropic host"
fi

echo "== 4. No docker socket is mounted by pipeline/sandbox.py =="
python3 - <<'PY'
from pipeline import sandbox
argv = sandbox.build_docker_argv(model="m", container_name="c")
mounts = [argv[i+1] for i,t in enumerate(argv) if t == "-v"]
assert not any("docker.sock" in m for m in mounts), mounts
print("PASS: docker socket is never mounted")
PY

echo
echo "ALL SANDBOX CHECKS PASSED"
