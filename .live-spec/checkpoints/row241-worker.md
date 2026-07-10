# row 241 worker checkpoint — scaffold/guardrails (four host checks runnable)

Worker: cloud session, briefed by docs/briefs/2026-07-10-row241-guardrails-brief.md.
Branch: `row241-guardrails` (from main @ 9cdd39d). Started 2026-07-10.

## DONE
- Branch created from main.
- Fixture host-clean built (tiny spec+index, matrix citing INV-1/INV-2, registry with
  2 surfaces, dist/index.html, config; fixture host test named smoke.py so the pack's
  own pytest never collects it).
- tests/test_scaffold_guardrails.py written BEFORE any check code; red run recorded below.
- gate_lib.py + the four checks + guardrails.config.example.json + README attach walk.
- `python3 -m pytest tests/test_scaffold_guardrails.py -q` → `22 passed in 1.64s`.
- FULL suite: `CI=true python3 -m pytest -q` → `341 passed in 30.14s`. See ACCEPTANCE
  NOTE below for the bare `python3 -m pytest -q` result (2 PRE-EXISTING environmental
  failures, reproduced on clean main, untouched by this branch).
- Manual runs of all four checks against the clean fixture from the repo root — pasted below.

## IN PROGRESS
- (nothing — pushing)

## NEXT
- Senior session: integration (matrix function-rows, attach the pack repo as first host,
  retire the README Known-issues line, version bump) — explicitly NOT this worker's.

## ACCEPTANCE NOTE — full-suite green, with one environmental caveat
Bare `python3 -m pytest -q` in THIS container: `2 failed, 339 passed in 29.68s`. The 2:
- tests/test_guardrails.py::TestGateG_PinDrift::test_real_repo_passes — red because the
  ARCHITECTURE.md pin `~/.claude/CLAUDE.md:1` is a machine-local pin; the gate skips it
  only when CI=true, and this cloud container is neither the author's machine nor CI.
- tests/test_guardrails.py::TestGateB_Tests::test_real_content_passes — runs the whole
  suite inside a scratch copy, so it reds on the same pin.
Proof it pre-exists: `git checkout main && python3 -m pytest tests/test_guardrails.py::...`
→ SAME 2 failures at 9cdd39d (main), before any row-241 file. With the gate's own
designed escape for non-author machines (`CI=true`), the full suite is green: 341 passed,
including the 22 new. No file this branch touches is involved in either failure; fixing
the pin lives in ARCHITECTURE.md, which is OUTSIDE this worker's write-set.
(Also noted, benign: pin-drift prints DRIFT for `scripts/onboarding-card.py:1 (the
renderer)` — label word not in ±25 lines; report-only unless --strict, likewise pre-existing.)

## RED-FIRST PROOF
Run: `python3 -m pytest tests/test_scaffold_guardrails.py -q` at 2026-07-10, before any
file under scaffold/guardrails/ (beyond the pre-existing prose README) existed. Tail:

```
FAILED tests/test_scaffold_guardrails.py::TestTracesDefects::test_dead_anchor
FAILED tests/test_scaffold_guardrails.py::TestTracesDefects::test_unanchored_surface
FAILED tests/test_scaffold_guardrails.py::TestConflictsDefects::test_duplicate_anchor
FAILED tests/test_scaffold_guardrails.py::TestConflictsDefects::test_invariant_without_row
FAILED tests/test_scaffold_guardrails.py::TestConflictsDefects::test_resolved_but_live
FAILED tests/test_scaffold_guardrails.py::TestConflictsDefects::test_surface_named_twice
FAILED tests/test_scaffold_guardrails.py::TestConfigLadder::test_env_var_config_wins
FAILED tests/test_scaffold_guardrails.py::TestConfigLadder::test_missing_config_is_red_with_attach_me_line
FAILED tests/test_scaffold_guardrails.py::TestConfigLadder::test_waived_check_is_visible_and_green
FAILED tests/test_scaffold_guardrails.py::TestShippedShape::test_example_config_ships_and_parses
FAILED tests/test_scaffold_guardrails.py::TestShippedShape::test_readme_walks_the_attach
22 failed in 1.64s
```
(All 22 fail because the check scripts do not exist yet — subprocess exits 2 /
FileNotFound-shaped output, plus the two shipped-shape tests find no files.)

## MANUAL RUNS (clean fixture, from repo root)
With `GUARDRAILS_CONFIG=tests/fixtures/scaffold_guardrails/host-clean/guardrails.config.json`:

```
$ python3 scaffold/guardrails/check_completeness.py
OK (completeness): 2 registered surface(s) present and non-empty; rendered content exhibits nothing unregistered
$ python3 scaffold/guardrails/check_tests_present.py --base origin/main
OK (tests-present): no user-facing files changed against origin/main
$ python3 scaffold/guardrails/check_traces_to_spec.py
OK (traces): 2 surface(s) trace to 3 live anchor citation(s) in PRODUCT_SPEC.md
$ python3 scaffold/guardrails/check_conflicts.py
OK (conflicts): 2 indexed anchor(s), 2 registered surface(s): no duplicates, no invariant without a matrix row, no resolved-but-live marker
```
(all exit 0)

## WATCHED
- 2026-07-10 `python3 -m pip install pytest` — first attempt ReadTimeoutError from
  files.pythonhosted.org via the agent proxy; second attempt succeeded (pytest 9.1.1).
  Context: container image ships pytest only as a uv tool, not in python3's site-packages.
