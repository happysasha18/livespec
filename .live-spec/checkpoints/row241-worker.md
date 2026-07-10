# row 241 worker checkpoint — scaffold/guardrails (four host checks runnable)

Worker: cloud session, briefed by docs/briefs/2026-07-10-row241-guardrails-brief.md.
Branch: `row241-guardrails` (from main @ 9cdd39d). Started 2026-07-10.

## DONE
- Branch created from main.
- Fixture host-clean built (tiny spec+index, matrix citing INV-1/INV-2, registry with
  2 surfaces, dist/index.html, config; fixture host test named smoke.py so the pack's
  own pytest never collects it).
- tests/test_scaffold_guardrails.py written BEFORE any check code; red run recorded below.

## IN PROGRESS
- Implementing gate_lib.py + the four checks + config example + README.

## NEXT
- Green on the new file, then FULL suite, manual runs from repo root, acceptance diff, push.

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
(to be pasted)

## WATCHED
- 2026-07-10 `python3 -m pip install pytest` — first attempt ReadTimeoutError from
  files.pythonhosted.org via the agent proxy; second attempt succeeded (pytest 9.1.1).
  Context: container image ships pytest only as a uv tool, not in python3's site-packages.
