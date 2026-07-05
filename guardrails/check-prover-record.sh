#!/usr/bin/env bash
# check-prover-record.sh — gate (a) of the push gate: a fresh, committed prover record
# dated today must exist before a push (SPEC M-6: every live-spec push is preceded by a
# fresh whole-spec prover re-check recorded in docs/prover/).
#
# Usage: check-prover-record.sh [prover-dir] [YYYY-MM-DD]
#   prover-dir  defaults to docs/prover (relative to the repo root)
#   date        defaults to today
#
# "Present and committed" means: at least one file matching <prover-dir>/<date>*.md
# both exists on disk AND is tracked by git (git ls-files sees it) — not just an
# untracked scratch file sitting in the working tree.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

PROVER_DIR="${1:-docs/prover}"
TODAY="${2:-$(date +%Y-%m-%d)}"

shopt -s nullglob
candidates=("$PROVER_DIR"/"$TODAY"*.md)
shopt -u nullglob

if [ ${#candidates[@]} -eq 0 ]; then
  echo "FAIL (prover record): no file matching $PROVER_DIR/$TODAY*.md exists."
  echo "  A fresh whole-spec prover re-check must be recorded before every push (SPEC M-6)."
  echo "  Fix: run the product-prover pass and save its record as $PROVER_DIR/$TODAY-<slug>.md, then commit it."
  exit 1
fi

tracked=()
untracked=()
for f in "${candidates[@]}"; do
  if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then
    tracked+=("$f")
  else
    untracked+=("$f")
  fi
done

if [ ${#tracked[@]} -eq 0 ]; then
  echo "FAIL (prover record): found today's prover record(s) but none are committed to git:"
  printf '  %s\n' "${untracked[@]}"
  echo "  Fix: git add the file(s) and commit before pushing."
  exit 1
fi

echo "OK (prover record): committed record(s) for $TODAY found:"
printf '  %s\n' "${tracked[@]}"
exit 0
