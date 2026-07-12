#!/usr/bin/env bash
# check-prover-record.sh — gate (a) of the push gate: a fresh, committed prover record
# dated today must exist before a push, and that record must be fresh for BOTH guarded
# documents — PRODUCT_SPEC.md and ARCHITECTURE.md (SPEC M-6, INV-116: every live-spec push
# is preceded by a fresh re-check recorded in docs/prover/, covering the spec and the
# architecture alike).
#
# Usage: check-prover-record.sh [prover-dir] [YYYY-MM-DD]
#   prover-dir  defaults to docs/prover (relative to the repo root)
#   date        defaults to today
#
# "Present and committed" means: at least one file matching <prover-dir>/<date>*.md
# both exists on disk AND is tracked by git (git ls-files sees it) — not just an
# untracked scratch file sitting in the working tree.
#
# Freshness rule (row 61, SPEC M-6; extended row 271, INV-116): a record dated-today-and-
# committed is not enough on its own — it can be a record for a STALE state if PRODUCT_SPEC.md
# or ARCHITECTURE.md changed again after it landed. So after the tracked-record check above
# passes, also require that the newest commit touching <prover-dir> is at least as new as the
# newest commit touching PRODUCT_SPEC.md, and separately at least as new as the newest commit
# touching ARCHITECTURE.md (equal, or the document's commit is an ancestor of the record's
# commit — a record may ship in the very same commit as the document change it covers).

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

SPEC_COMMIT=$(git log -1 --format=%H -- PRODUCT_SPEC.md)
RECORD_COMMIT=$(git log -1 --format=%H -- "$PROVER_DIR")

if [ -z "$SPEC_COMMIT" ]; then
  echo "OK (freshness): no PRODUCT_SPEC.md in git history — spec freshness check skipped."
else
  fresh=0
  if [ "$SPEC_COMMIT" = "$RECORD_COMMIT" ]; then
    fresh=1
  elif git merge-base --is-ancestor "$SPEC_COMMIT" "$RECORD_COMMIT"; then
    fresh=1
  fi

  if [ "$fresh" -ne 1 ]; then
    echo "FAIL (prover record): the newest committed prover record predates the last PRODUCT_SPEC.md change."
    echo "  PRODUCT_SPEC.md last changed in commit $SPEC_COMMIT; newest docs/prover/ commit is $RECORD_COMMIT."
    echo "  SPEC M-6 wants a re-check record for the PUSHED STATE — re-run the prover pass and commit its record after the SPEC change."
    exit 1
  fi

  echo "OK (freshness): record commit is not older than the last PRODUCT_SPEC.md commit."
fi

ARCH_COMMIT=$(git log -1 --format=%H -- ARCHITECTURE.md)
if [ -n "$ARCH_COMMIT" ]; then
  arch_fresh=0
  if [ "$ARCH_COMMIT" = "$RECORD_COMMIT" ]; then
    arch_fresh=1
  elif git merge-base --is-ancestor "$ARCH_COMMIT" "$RECORD_COMMIT"; then
    arch_fresh=1
  fi
  if [ "$arch_fresh" -ne 1 ]; then
    echo "FAIL (prover record): the newest committed prover record predates the last ARCHITECTURE.md change."
    echo "  ARCHITECTURE.md last changed in commit $ARCH_COMMIT; newest docs/prover/ commit is $RECORD_COMMIT."
    echo "  SPEC M-6/INV-116 wants the prover pass to cover ARCHITECTURE.md too — re-run the prover over the architecture and commit its record."
    exit 1
  fi
  echo "OK (freshness): record commit is not older than the last ARCHITECTURE.md commit."
fi

exit 0
