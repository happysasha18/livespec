#!/usr/bin/env bash
# check-pin-drift.sh — gate (g): architecture pins must not rot (row 90, the
# track-coach lesson: 7 of 17 pins drifted in ONE session, silently).
#
# A pin looks like `path/to/file:123` (label words) in ARCHITECTURE.md's Nodes
# table. The NORMATIVE pin is the named thing; the :line is a cache (SPEC E-14).
# This gate:
#   RED   — pinned file missing, or :line beyond end of file (a hard break);
#   DRIFT — none of the label's words (≥4 chars) found within ±25 lines of the
#           pinned line: reported as drift, and RED when --strict is passed
#           (hosts opt into strict once their pins carry real symbols).
#
# Usage: check-pin-drift.sh [architecture-file] [--strict]

set -euo pipefail

ARCH="${1:-$(git rev-parse --show-toplevel)/ARCHITECTURE.md}"
STRICT=0
[ "${2:-}" = "--strict" ] && STRICT=1
ROOT="$(cd "$(dirname "$ARCH")" && pwd)"

hard_fail=0
drift=0
checked=0

# pins: `path:line` optionally followed by (label)
while IFS=$'\t' read -r path line label; do
  [ -z "$path" ] && continue
  checked=$((checked+1))
  case "$path" in
    "~/"*) full="$HOME/${path#\~/}" ;;
    /*)    full="$path" ;;
    *)     full="$ROOT/$path" ;;
  esac
  if [ ! -f "$full" ]; then
    echo "FAIL (pin drift): $path:$line — pinned file missing"; hard_fail=1; continue
  fi
  total=$(wc -l < "$full")
  if [ "$line" -gt "$total" ]; then
    echo "FAIL (pin drift): $path:$line — beyond end of file ($total lines)"; hard_fail=1; continue
  fi
  [ -z "$label" ] && continue
  lo=$(( line > 25 ? line - 25 : 1 ))
  hi=$(( line + 25 ))
  window="$(sed -n "${lo},${hi}p" "$full")"
  found=0
  for w in $label; do
    w="$(echo "$w" | tr -cd '[:alnum:]-')"
    [ ${#w} -lt 4 ] && continue
    if printf '%s' "$window" | grep -qiF -- "$w"; then found=1; break; fi
    if printf '%s' "$window" | grep -qiF -- "${w%s}"; then found=1; break; fi
  done
  if [ "$found" -eq 0 ]; then
    echo "DRIFT (pin drift): $path:$line ($label) — label not found within ±25 lines"
    drift=1
  fi
done < <(sed -n '/## Nodes/,/## Seams/p' "$ARCH" \
  | grep -oE '`[A-Za-z0-9_./~-]+:[0-9]+`( \([^)]*\))?' \
  | sed -E 's/^`([^:]+):([0-9]+)`( \(([^)]*)\))?/\1\t\2\t\4/')

if [ "$checked" -eq 0 ]; then
  echo "FAIL (pin drift): no pins parsed from $ARCH"; exit 1
fi

if [ "$hard_fail" -ne 0 ]; then
  echo "  Fix: re-run the pin's grep and update the path/line (SPEC E-14)."
  exit 1
fi
if [ "$drift" -ne 0 ] && [ "$STRICT" -eq 1 ]; then
  echo "  Fix (strict): re-resolve each drifted pin's named thing and refresh its cached line."
  exit 1
fi
echo "OK (pin drift): $checked pin(s) checked$( [ "$drift" -ne 0 ] && echo ', drift reported above (non-strict)' )."
exit 0
