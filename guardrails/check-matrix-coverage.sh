#!/usr/bin/env bash
# check-matrix-coverage.sh — gate (d) of the push gate: TEST_MATRIX.md's
# coverage-validation checklist must have no unchecked box.
#
# Usage: check-matrix-coverage.sh [path-to-TEST_MATRIX.md]
#   defaults to TEST_MATRIX.md at the repo root; pass a scratch copy's path to
#   test this gate without mutating the real file.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
MATRIX="${1:-$REPO_ROOT/TEST_MATRIX.md}"

if [ ! -f "$MATRIX" ]; then
  echo "FAIL (matrix): file not found: $MATRIX"
  exit 1
fi

# Section runs from the "## Coverage validation" heading to the next "## " heading
# (or EOF), matching TEST_MATRIX.template.md's shape.
section="$(awk '/^## Coverage validation/{flag=1; next} /^## /{flag=0} flag' "$MATRIX")"

if [ -z "$section" ]; then
  echo "FAIL (matrix): no '## Coverage validation' section found in $MATRIX"
  exit 1
fi

unchecked="$(printf '%s\n' "$section" | grep '^- \[ \]' || true)"

if [ -n "$unchecked" ]; then
  echo "FAIL (matrix): unchecked coverage-validation item(s) in $MATRIX:"
  printf '%s\n' "$unchecked" | sed 's/^/  /'
  echo "  Fix: walk the coverage-validation checklist and check each box (or retire the row it belongs to) before pushing."
  exit 1
fi

echo "OK (matrix): all coverage-validation checkboxes are checked in $MATRIX"
exit 0
