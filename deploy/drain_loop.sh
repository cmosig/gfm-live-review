#!/usr/bin/env bash
# Backlog drain loop — run the pipeline back-to-back until the subscription's
# real session usage hits the cap, then wait for the rolling 5-hour window to
# refill and keep going. This is the "run it hard right now" companion to the
# once-a-night systemd timer (deploy/gfm-review.timer); both take the same run
# lock, so they never collide (a killed run no longer wedges the other — see
# _Lock reclaim in pipeline/run.py).
#
# Run it in a tmux window and watch it:
#   tmux new-window -t <session> -n drain 'deploy/drain_loop.sh'
#   tail -f "$HOME/gfm-review.log"
# Stop it:  pkill -f drain_loop.sh
#
# Tunables (env):
#   GFM_SESSION_CAP   stop a cycle once 5h session usage reaches this % (default 90)
#   GFM_WEEKLY_CAP    skip a cycle entirely if weekly usage is >= this %  (default 85)
#   GFM_REFILL_SLEEP  seconds to wait after a cycle before retrying       (default 1800)
set -u

REPO="$(cd "$(dirname "$0")/.." && pwd)"
# claude + gfm-usage-probe live in ~/.local/bin; extraction runs in env_conda.
export PATH="$HOME/.local/bin:$HOME/miniconda3/envs/env_conda/bin:$PATH"
PY="$HOME/miniconda3/envs/env_conda/bin/python"
LOG="$HOME/gfm-review.log"

SESSION_CAP="${GFM_SESSION_CAP:-90}"
WEEKLY_CAP="${GFM_WEEKLY_CAP:-85}"
REFILL_SLEEP="${GFM_REFILL_SLEEP:-1800}"

cd "$REPO" || exit 1
echo "=== drain loop started $(date -Is); session_cap=${SESSION_CAP}% weekly_cap=${WEEKLY_CAP}% ===" | tee -a "$LOG"

while true; do
  echo "=== drain cycle start $(date -Is) ===" | tee -a "$LOG"
  # --extractor host: the Docker sandbox is still blocked on the one-time root
  # uidmap step (see memory docker-needs-root-step); host extractor keeps the
  # empty tool allowlist / no-API-key guarantees but loses container isolation.
  "$PY" -m pipeline.run \
      --backfill \
      --extractor host \
      --max-session-pct "$SESSION_CAP" \
      --skip-weekly-above "$WEEKLY_CAP" \
      --redeploy-every 5 \
      >> "$LOG" 2>&1
  rc=$?
  echo "=== drain cycle done $(date -Is) rc=$rc; sleeping ${REFILL_SLEEP}s ===" | tee -a "$LOG"
  [ "$rc" -ne 0 ] && echo "  (run exited non-zero: $rc)" | tee -a "$LOG"
  sleep "$REFILL_SLEEP"
done
