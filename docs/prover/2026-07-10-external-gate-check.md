# External gate-check — adversarial push-gate probe (2026-07-10)

An invited adversarial tester tried to prove this repo's push gates physically block a
broken state — or prove they don't. Every break-test push went to a throwaway decoy
remote (`/tmp/fake-remote.git`), never to origin. The finding that matters is the last
one: **one planted break sailed through green.**

## Verdict at a glance

| Test | Planted break | Expected | Result |
|---|---|---|---|
| 0 · control | none (clean tree) | pass all gates | **PASS** — all gates green, push allowed |
| 1 · traceability | delete a test a BUILT matrix row names | block | **BLOCKED** ✓ |
| 2 · desync | reword a skill fact a pinned test asserts | block | **BLOCKED** ✓ |
| 3 · host checks (gate h) | invented `<section id>` in a rendered artifact | block (red + typed line) | **NOT BLOCKED** ✗ — gate stayed green, break landed on the decoy |

Plus two setup findings (below): the hooks do not self-install on a clone, and a fresh
container's local gate is red out of the box for reasons unrelated to any break.

## Setup and how the run was isolated

- **Decoy remote.** `git init --bare /tmp/fake-remote.git`; `git remote add fake …`. The
  working clone is *shallow*, so the bare remote needed
  `git config receive.shallowUpdate true` before any push (of any kind) could be received
  — a mechanical detail, unrelated to the gates.
- **Hooks were not installed on the clone.** `.git/hooks/` held only `pre-commit.sample`
  and `pre-push.sample`. A push attempted *before* `guardrails/install.sh` ran produced
  **zero gate output** — nothing gated it (see finding S-1). Then `bash guardrails/install.sh`
  installed both hooks; every test below ran against the installed `pre-push`.
- **`CI=true` on every push.** In a fresh container two things make even a clean local
  push red for reasons that have nothing to do with a planted break: the architecture pin
  `~/.claude/CLAUDE.md` is a machine-local file that does not exist here, and `pytest` is
  not preinstalled. `check-pin-drift.sh` skips machine-local pins only when `CI=true`
  (exactly as this repo's own CI mirror runs — see `guardrails/README.md`). Setting
  `CI=true` silences that noise so the **only** variable under test is the planted break.
  This is the honest way to run the gate here, not a bypass: the missing pin genuinely
  belongs to the author's machine, and `CI=true` is how the second net evaluates it.

## Test 0 — control (clean tree)

`CI=true git push fake HEAD:refs/heads/main` on the committed clean tree. Every gate green:

```
-- gate a: fresh prover record for today --
OK (prover record): committed record(s) for 2026-07-10 found: …
OK (freshness): record commit is not older than the last PRODUCT_SPEC.md commit.
-- gate b: test suite green … --
Ran 315 tests … OK
OK (tests): suite green (tests) — also covers anchor ownership (gate c).
-- gate d … --  OK (matrix): all coverage-validation checkboxes are checked …
-- gate g: pin drift --
note (pin drift): ~/.claude/CLAUDE.md:1 — machine-local pin, absent in CI; skipped.
OK (pin drift): 38 pin(s) checked, drift reported above (non-strict).
-- gate f … --  OK (loadability): 8 skill(s) load, named, versioned, negative-scoped.
-- gate e … --  OK (prototype fence): 1 fenced file(s), no prod references.
-- gate h: the four host checks … --
OK (completeness): 4 registered surface(s) present and non-empty; rendered content exhibits nothing unregistered
OK (tests-present): …   OK (traces): …   OK (conflicts): …
All gates green — push allowed.
* [new branch]      HEAD -> main   (PUSH EXIT 0)
```

**Verdict: PASS.** The control lands, so a later block is attributable to the break, not
to a chronically red gate.

## Test 1 — traceability (delete a test a BUILT matrix row names)

Deleted `test_dead_anchor` (`tests/test_scaffold_guardrails.py`), which BUILT row **M-230**
in `TEST_MATRIX.md` names by name. Committed, pushed to `fake`. The gate that fired was
`test_traceability.TestMatrix.test_matrix_built_rows_name_real_tests`. Verbatim:

```
M-230: BUILT row cites missing test test_dead_anchor
FAIL (tests): suite is not green (tests).
FAILED (failures=2)
PUSH BLOCKED — one or more gates above failed. Fix them and try again.
```

`PUSH EXIT 1`; the branch `break-test1` never appeared on the decoy remote.
**Verdict: BLOCKED as expected — the gate held.** Reverted.

## Test 2 — desync (reword a fact a pinned test asserts)

Changed `skills/communicator/SKILL.md` line 397 from the literal `"what can I customize"`
to `"which options can I change"`. The pinned test `test_onboarding_card_wiring`
(`tests/test_onboarding_card.py`) asserts the exact phrase. Committed, pushed to `fake`:

```
AssertionError: 'what can I customize' not found in '…communicator SKILL.md…'
  : communicator lost the standing-question line
FAIL (tests): suite is not green (tests).
FAILED (failures=2)
PUSH BLOCKED — one or more gates above failed. Fix them and try again.
```

`PUSH EXIT 1`; `break-test2` never appeared on the decoy remote.
**Verdict: BLOCKED as expected — the gate held.** Reverted.

## Test 3 — host checks, gate h completeness (HEADLINE)

Appended an invented, unregistered surface to `README.md` (a `rendered_artifacts` entry in
`guardrails.config.json`):

```html
<section id="phantom-surface">This surface is invented and registered nowhere in SURFACES.md.</section>
```

Committed, pushed to `fake`. **The gate stayed green and the broken state landed:**

```
OK (completeness): 4 registered surface(s) present and non-empty; rendered content exhibits nothing unregistered
All gates green — push allowed.
* [new branch]      break-test3   (PUSH EXIT 0)
```

The break pushed clean. Worse, the green line *asserts* "rendered content exhibits nothing
unregistered" — a claim the check never verified.

**Root cause.** `guardrails.config.json` sets `"surface_discovery_pattern": null`. In
`scaffold/guardrails/check_completeness.py` the self-closing direction — the branch that
catches a rendered surface absent from the registry — is guarded by `if discovery:`. With
the pattern null, that branch never runs. Gate h checks only that every *registered*
surface is *present* (registry → DOM); it never checks DOM → registry on this host, so an
invented surface is invisible to it.

**The machinery is sound; the host simply never armed it.** With the *same* broken README,
setting the pattern to the value the test fixture already uses
(`"<section id=\"([^\"]+)\""`) turns the same push red with exactly the typed line Test 3
expected:

```
FAIL (completeness): rendered content exhibits surface id(s) phantom-surface absent from the registry SURFACES.md
GUARDRAIL-FAIL {"severity": "error", "code": "completeness.rendered-but-unregistered", "message": "rendered content exhibits surface id(s) phantom-surface absent from the registry SURFACES.md", "fix": "add a registry row for each rendered surface — the DOM is the source of truth, the registry must keep up"}
```

The unit suite even exercises this branch (`test_rendered_but_unregistered` in
`tests/test_scaffold_guardrails.py`) — but against a *fixture* config that sets the
pattern. The repo's own attached config leaves it null, so the repo is the one host where
the check is a no-op.

**Verdict: NOT BLOCKED.** A green gate on a planted break is the headline: gate h
completeness does not catch an unregistered rendered surface as this repo is configured.
Fix: set `surface_discovery_pattern` in `guardrails.config.json` to the artifacts' actual
surface marker (e.g. `<section id="([^"]+)"`), or state in the host profile that the
DOM→registry direction is deliberately unenforced and why. Reverted.

## Setup findings

- **S-1 · Hooks do not self-install on a clone.** Until `guardrails/install.sh` is run,
  `.git/hooks/` carries only the samples and a push is ungated — a fresh clone can push
  anything. This is documented behaviour (`guardrails/README.md`), and CI is the declared
  second net (SPEC M-5), but nothing in the clone *forces* the local hook to exist; the
  first push after a clone is on the honour system.
- **S-2 · The fresh-container local gate is red for non-break reasons.** Out of the box a
  clean tree fails gate g (`FAIL (pin drift): ~/.claude/CLAUDE.md:1 — pinned file missing`)
  and gate b (`test_pytest_collects_clean_from_root` — `No module named pytest`; and the
  pin-drift meta-tests). All resolve to environment, not defect: `CI=true` skips the
  machine-local pin, and `pip install pytest` supplies the missing collector. Worth
  recording because it means the local gate is not self-contained — a first-time local run
  needs `CI=true` and `pytest` before the control can go green.

## Physical ledger

The decoy remote is its own record. After the run, `/tmp/fake-remote.git` holds:

- `main` — Test 0 control (landed, as intended)
- `probe-preinstall` — the pre-install probe (landed; no hook existed)
- `break-test3` — Test 3's broken README (**landed — the gate that should have blocked it did not**)

Absent, because they were physically blocked: `break-test1`, `break-test2`.

## Bottom line

Two of the three planted breaks were physically blocked at push with the exact typed gate
lines above. The third — an unregistered rendered surface — pushed clean, because this
repo's `guardrails.config.json` leaves `surface_discovery_pattern` null and thereby
disables the one branch of gate h that would catch it. The check is real and the fixture
proves it works; the host just isn't wired to run it.
