#!/bin/sh
# Installs the canonical scissors-scan Stop hook (SPEC INV-173) on this machine, universal tier
# only. Idempotent: re-running changes nothing once installed. The personal overlay
# (~/.claude/hooks/scissors-personal.json) is owned entirely by the personal layer — this script
# never creates or edits it.
#
# Usage: install-pack-hooks.sh [--dry-run]
#   --dry-run   print what would be done, touch nothing. Honors $HOME as-is (no hardcoded path),
#               so a test can point it at a scratch HOME without ever touching the real one.
set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)"   # pack root (this script lives in <pack>/scripts/)

DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
  esac
done

SRC="$DIR/hooks/scissors-scan.py"
DEST_DIR="$HOME/.claude/hooks"
DEST="$DEST_DIR/scissors-scan.py"
SETTINGS="$HOME/.claude/settings.json"

if [ "$DRY_RUN" = "1" ]; then
  if [ -f "$DEST" ] && cmp -s "$SRC" "$DEST"; then
    echo "DRY-RUN: already present: $DEST"
  else
    echo "DRY-RUN: would copy $SRC -> $DEST"
  fi
  echo "DRY-RUN: would wire Stop hook 'python3 ~/.claude/hooks/scissors-scan.py' into $SETTINGS (if absent)."
  echo "DRY-RUN: scissors-personal.json is never touched by this script."
  exit 0
fi

mkdir -p "$DEST_DIR"
if [ -f "$DEST" ] && cmp -s "$SRC" "$DEST"; then
  echo "already present: $DEST"
else
  cp "$SRC" "$DEST"
  chmod +x "$DEST"
  echo "installed: $DEST"
fi

python3 - "$SETTINGS" << 'PYEOF'
import json, os, sys

p = sys.argv[1]
s = json.load(open(p)) if os.path.exists(p) else {}
stop = s.setdefault("hooks", {}).setdefault("Stop", [])
have = [hk.get("command", "") for e in stop for hk in e.get("hooks", [])]
cmd = "python3 ~/.claude/hooks/scissors-scan.py"
if any("scissors-scan.py" in c for c in have):
    print("already present: Stop hook wired in %s" % p)
else:
    stop.append({"hooks": [{"type": "command", "command": cmd}]})
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(s, open(p, "w"), indent=2, ensure_ascii=False)
    print("installed: Stop hook wired in %s" % p)
PYEOF

echo "note: ~/.claude/hooks/scissors-personal.json is owned by the personal layer — never created or modified here."
