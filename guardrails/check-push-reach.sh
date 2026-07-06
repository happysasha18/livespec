#!/usr/bin/env bash
# check-push-reach.sh — the reach map's deciding script (SPEC INV-45, ROADMAP row 147).
# Answers ONE question for the push gate: can this push's diff reach the python suite?
#   exit 0 = prose-only diff — every changed file matches the explicit prose class below;
#            the suite's checks read none of these files, gate b may stand the suite down BY NAME.
#   exit 1 = full reach — at least one changed file is outside the class (code, spec, matrix,
#            queue, skills, tests, scripts, guardrails — or anything NEW the map never met),
#            or the diff/base cannot be established. Conservative by construction.
#
# The prose class is EXPLICIT and narrow — "just .md" is NOT a class: SPEC.md, TEST_MATRIX.md,
# ARCHITECTURE.md, ROADMAP.md, JOURNAL.md, NEXT_STEPS.md and every SKILL.md are TESTED documents
# (string rows read them) and must never be added below.
#
# Usage: check-push-reach.sh [base-ref]      (default base: origin/main)
#   REACH_FILES (tests only): newline-separated file list replaces the git diff.

set -euo pipefail
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

BASE="${1:-origin/main}"

if [ -n "${REACH_FILES:-}" ]; then
  files="$REACH_FILES"
else
  if ! git rev-parse --verify --quiet "$BASE" >/dev/null; then
    echo "reach: base ref '$BASE' not found — conservative fall-through to FULL."
    exit 1
  fi
  files="$(git diff --name-only "$BASE"..HEAD)"
fi

matches_prose() {
  case "$1" in
    README.md|OVERVIEW.md|MIGRATION.md|LICENSE) return 0 ;;
    docs/research/*|docs/reports/*|docs/audit/*|docs/decisions/*) return 0 ;;
    *) return 1 ;;
  esac
}

seen=0
full=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  seen=$((seen + 1))
  if ! matches_prose "$f"; then
    echo "reach: '$f' is outside the prose class — FULL suite."
    full=1
  fi
done <<< "$files"

if [ "$seen" -eq 0 ]; then
  echo "reach: empty diff — conservative fall-through to FULL."
  exit 1
fi
if [ "$full" -ne 0 ]; then
  exit 1
fi
echo "OK (reach): prose-only diff — the suite's checks read none of the changed files."
exit 0
