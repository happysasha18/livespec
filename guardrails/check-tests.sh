#!/usr/bin/env bash
# check-tests.sh — gate (b) of the push gate: the test suite must be fully green.
#
# This also covers gate (c), anchor ownership: tests/test_traceability.py already
# asserts every spec anchor is owned by exactly one architecture node
# (TestArchitecture::test_architecture_owns_every_anchor_once). A green suite run
# proves both gates in one pass — no separate anchor-ownership check exists here.
#
# Usage: check-tests.sh [tests-dir]
#   tests-dir defaults to "tests" (relative to the repo root, or an absolute path
#   for testing this gate against a scratch fixture without touching the real suite)

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

TESTS_DIR="${1:-tests}"

# The runner MUST match the CI mirror's (.github/workflows/gates.yml runs `python3 -m pytest -q`);
# the two nets share one runner or the local net is weaker than the second one (SPEC M-5, M-154).
# unittest discover cannot collect the plain-function pytest-style tests (fixtures like monkeypatch/
# tmp_path), so it silently under-runs and false-greens — the exact hole that let a red reach CI.
if python3 -m pytest -q "$TESTS_DIR"; then
  echo "OK (tests): suite green ($TESTS_DIR) — also covers anchor ownership (gate c)."
  exit 0
else
  echo "FAIL (tests): suite is not green ($TESTS_DIR)."
  echo "  Fix: run 'python3 -m pytest -q tests' and repair the failing test(s) before pushing."
  exit 1
fi
