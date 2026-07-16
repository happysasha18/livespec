#!/usr/bin/env bash
# check-config-health.sh — the installed gate is the source gate (SPEC INV-175).
#
# A gate lives twice: its source in guardrails/ travels with the repo; its installed copy in
# .git/hooks/ actually runs. They drift the moment an install is skipped — the worked instance
# (2026-07-16): the installed pre-push was missing gates k and l that the source carried.
# This check reds when an expected hook is missing from .git/hooks/ or differs byte-for-byte
# from its guardrails/ source, and names the one fix. A checkout with no installed hooks by
# design (CI) skips by name. Runs inside the suite, so even a stale pre-push that still runs
# the tests surfaces the drift — the self-healing shape.

set -euo pipefail

if [ "${GITHUB_ACTIONS:-}" = "true" ] || [ "${CI:-}" = "true" ]; then
  echo "config-health: skip (CI checkout installs no local hooks by design)"
  exit 0
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOKS_DIR="$(git -C "$REPO_ROOT" rev-parse --git-path hooks)"
case "$HOOKS_DIR" in
  /*) : ;;
  *) HOOKS_DIR="$REPO_ROOT/$HOOKS_DIR" ;;
esac

fail=0
for name in pre-commit pre-push; do
  src="$REPO_ROOT/guardrails/$name"
  [ -f "$src" ] || continue
  inst="$HOOKS_DIR/$name"
  if [ ! -f "$inst" ]; then
    echo "{\"severity\":\"error\",\"code\":\"config-health\",\"message\":\"installed hook missing: .git/hooks/$name\",\"fix\":\"run guardrails/install.sh\"}"
    fail=1
  elif ! cmp -s "$src" "$inst"; then
    echo "{\"severity\":\"error\",\"code\":\"config-health\",\"message\":\"installed hook drifted from source: $name\",\"fix\":\"run guardrails/install.sh\"}"
    fail=1
  fi
done

if [ "$fail" -eq 0 ]; then
  echo "config-health: OK (installed hooks match guardrails/ source)"
fi
exit "$fail"
