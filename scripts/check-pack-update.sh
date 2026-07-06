#!/bin/bash
# check-pack-update.sh — once a day, ask the public repo whether the pack moved past this machine (SPEC E-25).
# PROPOSES only — never installs (the human's gate, ACT-1). Offline or unreadable remote = one honest
# skip line naming the address, exit 0, stamp left unwritten so the next session retries.
# Forward only: a machine ahead of the public repo reads as up to date, never a downgrade proposal.
# Test/override flags: --remote-file <path> (bypass network) · --installed-file <path> · --stamp-file <path> · --force (ignore today's stamp)
set -u

REMOTE_URL="https://raw.githubusercontent.com/happysasha18/live-spec/main/VERSION"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INSTALLED_FILE="$ROOT/VERSION"
STAMP_FILE="$HOME/.claude/live-spec/update-check-stamp"
REMOTE_FILE=""
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --remote-file)    REMOTE_FILE="$2";    shift 2 ;;
    --installed-file) INSTALLED_FILE="$2"; shift 2 ;;
    --stamp-file)     STAMP_FILE="$2";     shift 2 ;;
    --force)          FORCE=1;             shift ;;
    *) echo "check-pack-update: unknown flag $1" >&2; exit 2 ;;
  esac
done

today="$(date +%Y-%m-%d)"
if [ "$FORCE" -eq 0 ] && [ -f "$STAMP_FILE" ] && [ "$(cat "$STAMP_FILE" 2>/dev/null)" = "$today" ]; then
  echo "pack update check: already ran today ($today) — skipped"
  exit 0
fi

if [ -n "$REMOTE_FILE" ]; then
  src="$REMOTE_FILE"
  remote="$(cat "$REMOTE_FILE" 2>/dev/null)"
else
  src="$REMOTE_URL"
  remote="$(curl -fsS --max-time 10 "$REMOTE_URL" 2>/dev/null)"
fi

if ! printf '%s' "$remote" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "pack update check: skipped — offline or unreadable remote ($src)"
  exit 0
fi

installed="$(cat "$INSTALLED_FILE" 2>/dev/null)"
if ! printf '%s' "$installed" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "pack update check: skipped — no readable installed version at $INSTALLED_FILE"
  exit 0
fi

mkdir -p "$(dirname "$STAMP_FILE")" && printf '%s' "$today" > "$STAMP_FILE"

newest="$(printf '%s\n%s\n' "$installed" "$remote" | sort -V | tail -1)"
if [ "$remote" = "$installed" ] || [ "$newest" = "$installed" ]; then
  echo "pack update check: up to date ($installed)"
  exit 0
fi

echo "PACK UPDATE AVAILABLE: $remote (this machine runs $installed)"
echo "  what changed: https://github.com/happysasha18/live-spec/blob/main/JOURNAL.md"
echo "  update road: install.sh (attic-backed) — or a plain 'git pull' where the repo itself runs the pack"
echo "  PROPOSAL ONLY — nothing installed; updating is the human's word."
exit 0
