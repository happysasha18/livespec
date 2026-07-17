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

# INV-173 x INV-175 (batch audit 2026-07-16, F3; inverted ROADMAP 417): the pack's session hooks are
# gates living twice too. Rather than a hardcoded basename list — which goes blind to every hook added
# after it was written (it was blind to hook-meter.py and the register-judge arms installed 2026-07-17)
# — DIFF the whole hook SOURCE directory (hooks/) against the installed set. Every file in hooks/ is
# covered automatically: when an installed copy exists it must match its source byte-for-byte; when a
# source hook has NO installed copy that is drift and it reds (source exists, install missing = the
# config is unhealthy, and a missing installed judge goes dark while every other gate stays green —
# corrected 2026-07-17, the earlier form skipped a missing install green). A file living only in the
# installed set (a personal-layer overlay the pack never ships) has no source here and is correctly left
# alone. RESIDUAL for row 420's gate audit: this arm proves the installed FILE exists and matches; it
# does not yet prove settings.json still LISTS the Stop/UserPromptSubmit judge entries — that check is
# harder because settings.json is personal-layer, and it is left for the row 420 gate audit.
HOOK_SRC_DIR="$REPO_ROOT/hooks"
if [ -d "$HOOK_SRC_DIR" ]; then
  for src_hook in "$HOOK_SRC_DIR"/*; do
    [ -f "$src_hook" ] || continue
    hname="$(basename "$src_hook")"
    inst_hook="$HOME/.claude/hooks/$hname"
    if [ ! -f "$inst_hook" ]; then
      echo "{\"severity\":\"error\",\"code\":\"config-health\",\"message\":\"installed hook missing: ~/.claude/hooks/$hname (source exists, install missing)\",\"fix\":\"run scripts/install-pack-hooks.sh or scripts/install-session-hooks.sh\"}"
      fail=1
    elif ! cmp -s "$src_hook" "$inst_hook"; then
      echo "{\"severity\":\"error\",\"code\":\"config-health\",\"message\":\"installed hook drifted from source: $hname\",\"fix\":\"run scripts/install-pack-hooks.sh or scripts/install-session-hooks.sh\"}"
      fail=1
    fi
  done
fi

if [ "$fail" -eq 0 ]; then
  echo "config-health: OK (installed hooks match their sources)"
fi
exit "$fail"
