#!/usr/bin/env bash
# check-push-reach.sh — the reach map's deciding script (SPEC INV-45, ROADMAP row 147;
# scoped middle road ROADMAP row 362, SPEC M-344).
# Answers ONE question for the push gate: can this push's diff reach the python suite?
#   exit 0 = prose-only diff — every changed file matches the explicit prose class below;
#            the suite's checks read none of these files, gate b may stand the suite down BY NAME.
#   exit 2 = SCOPED — every changed file is PROSE or INFRA, and at least one is INFRA: the diff is
#            confined to the guardrail scripts, the scaffold checks, the shipped templates, the
#            helper scripts, the hooks, the guardrails config, or the suite's own test files. The
#            scoped test set is printed as `SCOPED <path>` lines (sorted, unique) plus one reason
#            line; gate b runs exactly that set instead of the whole suite.
#   exit 1 = full reach — at least one changed file is outside PROSE ∪ INFRA (code, spec, matrix,
#            queue, skills, scripts the map never met — or anything NEW), or an INFRA file names no
#            test (directly or via one referrer level), or the diff/base cannot be established.
#            Conservative by construction.
#
# The prose class is EXPLICIT and narrow — "just .md" is NOT a class: PRODUCT_SPEC.md, TEST_MATRIX.md,
# ARCHITECTURE.md, ROADMAP.md, JOURNAL.md, NEXT_STEPS.md and every SKILL.md are TESTED documents
# (string rows read them) and must never be added below.
#
# The infra class is EXPLICIT too: guardrails/, scaffold/guardrails/, templates/, scripts/, hooks/,
# adopt/, the file guardrails.config.json, and tests/test_*.py files. A changed infra file's owning
# tests are found mechanically by filename — grep for the changed file's basename over tests/test_*.py
# — plus ONE referrer level: a file under one of the infra dirs that names the changed file's basename
# adds the tests that name THAT referrer's own basename. tests/test_traceability.py (the traceability
# net) always rides along. A changed infra file that no test names (directly or via a referrer) is not
# safely scopable, so the whole diff falls back to FULL — the conservative teeth this road keeps.
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

matches_infra() {
  case "$1" in
    guardrails/*|scaffold/guardrails/*|templates/*|scripts/*|hooks/*|adopt/*) return 0 ;;
    guardrails.config.json) return 0 ;;
    tests/test_*.py) return 0 ;;
    *) return 1 ;;
  esac
}

seen=0
full=0
infra_files=()
while IFS= read -r f; do
  [ -z "$f" ] && continue
  seen=$((seen + 1))
  if matches_prose "$f"; then
    continue
  elif matches_infra "$f"; then
    infra_files+=("$f")
  else
    echo "reach: '$f' is outside the prose/infra classes — FULL suite."
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

if [ "${#infra_files[@]}" -eq 0 ]; then
  echo "OK (reach): prose-only diff — the suite's checks read none of the changed files."
  exit 0
fi

# SCOPED middle road: every changed file is PROSE or INFRA, and at least one is INFRA.
REFERRER_DIRS="guardrails scaffold/guardrails scripts templates hooks adopt"

scoped=()
scoped_has() {
  local needle="$1" x
  for x in "${scoped[@]:-}"; do
    [ "$x" = "$needle" ] && return 0
  done
  return 1
}
add_scoped() {
  scoped_has "$1" || scoped+=("$1")
}

conservative_full=0
for f in "${infra_files[@]}"; do
  case "$f" in
    tests/test_*.py)
      # a changed test file adds itself to the scoped set — it is its own owning test. A DELETED
      # test file must never be handed to pytest (a nonexistent path reds collection, a false red);
      # it falls through to by-name discovery and, unowned, to FULL [2.3.0 audit, finding 6].
      if [ -f "$f" ]; then
        add_scoped "$f"
        continue
      fi
      ;;
  esac

  base="$(basename "$f")"
  owning=0

  while IFS= read -r t; do
    [ -z "$t" ] && continue
    add_scoped "$t"
    owning=1
  done < <(grep -l -F -- "$base" tests/test_*.py 2>/dev/null || true)

  while IFS= read -r r; do
    [ -z "$r" ] && continue
    [ "$r" = "$f" ] && continue
    rbase="$(basename "$r")"
    while IFS= read -r t; do
      [ -z "$t" ] && continue
      add_scoped "$t"
      owning=1
    done < <(grep -l -F -- "$rbase" tests/test_*.py 2>/dev/null || true)
  done < <(grep -rl -F -- "$base" $REFERRER_DIRS 2>/dev/null || true)

  if [ "$owning" -eq 0 ]; then
    echo "reach: '$f' names no test file (directly or via one referrer level) — conservative fall-through to FULL."
    conservative_full=1
  fi
done

if [ "$conservative_full" -ne 0 ]; then
  exit 1
fi

add_scoped "tests/test_traceability.py"

sorted_scoped="$(printf '%s\n' "${scoped[@]}" | sort -u)"
printf '%s\n' "$sorted_scoped" | while IFS= read -r t; do
  [ -z "$t" ] && continue
  echo "SCOPED $t"
done
count="$(printf '%s\n' "$sorted_scoped" | grep -c .)"
echo "OK (reach): infra-class diff — scoped to $count test files (each names a changed file; + the traceability net), SPEC INV-45"
exit 2
