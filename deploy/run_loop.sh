#!/usr/bin/env bash
# Simple daily loop scheduler — an alternative to the systemd timer for a server
# that is rarely restarted and where Docker access comes from the `docker` group
# (no sudo, no user-linger needed). It runs one pipeline pass, sleeps, repeats.
#
# Start it detached and forget it:
#   nohup deploy/run_loop.sh >> "$HOME/gfm-review.log" 2>&1 &
#   disown
# Check it:   tail -f "$HOME/gfm-review.log"
# Stop it:    pkill -f run_loop.sh
#
# Config via env: GFM_INTERVAL (seconds between runs, default 86400),
#                 GFM_PYTHON (interpreter, default python3).
set -u
REPO="$(cd "$(dirname "$0")/.." && pwd)"
INTERVAL="${GFM_INTERVAL:-86400}"
PY="${GFM_PYTHON:-python3}"

cd "$REPO" || exit 1
echo "gfm-review loop started at $(date -Is); repo=$REPO interval=${INTERVAL}s"
while true; do
  echo "=== run start $(date -Is) ==="
  # `sg docker` gives this run the docker group so the extraction sandbox works
  # even if the launching shell lacks it. run.py exits non-zero only on a real
  # unhandled failure (quota/one-off paper errors are handled internally).
  sg docker -c "cd '$REPO' && '$PY' -m pipeline.run" || echo "run exited non-zero ($?)"
  echo "=== run done  $(date -Is); sleeping ${INTERVAL}s ==="
  sleep "$INTERVAL"
done
