#!/usr/bin/env bash
# check-future-times.sh — INV-24's second arm (row 104): an ADDED line that PAIRS
# today's date with a clock time LATER than the commit moment is red. "Pairs"
# means ADJACENT — the stamp shape "YYYY-MM-DD [~]HH:MM" (up to a few punctuation
# characters between) — so a line that legally mixes today's date with QUOTED
# times of other moments (a ledger occurrence list, a deed quote) stays green;
# the first live run proved the line-global reading over-broad (prover F9).
# The commit clock is the reference (not racy). Runs on the STAGED diff.
# CHECK_TODAY / CHECK_NOW override the clock for tests only.
set -euo pipefail

TODAY="${CHECK_TODAY:-$(date +%F)}"
NOW="${CHECK_NOW:-$(date +%H:%M)}"

bad=0
while IFS= read -r line; do
  case "$line" in
    +++*) continue ;;
    +*) ;;
    *) continue ;;
  esac
  [[ "$line" != *"$TODAY"* ]] && continue
  while read -r m; do
    [ -z "$m" ] && continue
    hm="${m: -5}"
    if [[ "$hm" > "$NOW" ]]; then
      if [ "$bad" -eq 0 ]; then
        echo "COMMIT BLOCKED — a staged line stamps today ($TODAY) with a time past the clock ($NOW):"
      fi
      echo "  $line"
      bad=1
      break
    fi
  done < <(printf '%s\n' "$line" | grep -oE "$TODAY[^0-9]{0,4}([01][0-9]|2[0-3]):[0-5][0-9]" || true)
done < <(git diff --cached --unified=0 2>/dev/null || true)

if [ "$bad" -eq 1 ]; then
  echo "  Time is read off the clock, never invented (SPEC INV-24). Fix the stamp, restage, retry."
  exit 1
fi
exit 0
