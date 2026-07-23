# test-author — register rewrite notes (2026-07-22)

Register-only rewrite of the test-author skill. Write set: `skills/test-author/SKILL.md`,
`skills/test-author/README.md`. Every rule/step kept its exact meaning, scope, force; all code
anchors (INV-x, P8/P9) and the frontmatter trigger semantics were preserved. README was already
clean and needed no change (its only watch-list hit, "not enough here", is a lawful instructional
boundary).

## Counts

- Contrast-by-denial ("scissors") fixed in SKILL.md: **11**
- Inflation / drama / coined-metaphor fixed: **2**
- Redundancy / clarity fixes from the cold reads: **2** (skip-machinery topic clause; matrix-projection restatement)
- Register-lint (`scripts/preshow-register-lint.py`) findings fixed: **0** — the lint returned OK
  on both files on every run (no coined-metaphor / calque / transliteration pattern was ever hit).
  The scissors and drama fixes were driven by the manual grep + judgment pass, not by the lint.

### Scissors fixed (each now a positive statement; a named boundary gets its own plain clause)

1. `the matrix is a projection, never a second authority` → folded into `the spec keeps sole authority over what is true`
2. `the look itself stays the human's eye at the feel gate, never a pixel row's claim` → `... and no pixel row claims it`
3. `the row asserts the module's contract, not its internals or a neighbour's render` → `... the row asserts the module's contract. It leaves the module's internals and any neighbour's render out of scope.`
4. `a derivation rule rather than a judgment call each time` → `a derivation rule, so the level stops being a fresh judgment call each time`
5. `each module's tests assert its declared interface rather than its internals or a neighbour's render` → `... assert its declared interface, and they leave its internals and a neighbour's render alone`
6. `so a leak turns the run red instead of waiting for a human eye` → `so a leak turns the run red at once, before a human eye would catch it`
7. `it asserts an invariant rather than a recomputed value` → `it asserts an invariant.` (following sentence already scopes the ban)
8. `bounds each command with a real per-command deadline rather than a blanket timeout that reads a slow machine as a failure` → `bounds each command with a real per-command deadline. A blanket timeout would misread a slow machine as a failure.`
9. `Clean teardown means EVERY exit, not just the tidy one` → `Clean teardown covers EVERY exit, the abrupt ones as much as the tidy one`
10. `a wrapper's exit 0 is the wrapper's, never the tests'` → `a wrapper's exit 0 reports the wrapper finishing and says nothing about the tests`
11. `is red on every machine instead of a silent pass on the one that needed it` → `goes red on every machine. Without that early import, a broken skip would pass silently on the one machine that needed it`

### Drama / metaphor fixed

- `the exact defect the ladder was born to kill` → `the exact defect the ladder exists to catch`
- `is a failure wearing a quieter color` → `is a failure in a quieter color`

### Clarity fixes from cold reads

- Skip bullet topic clause (self-contradictory: "A skip path executes even when never taken") →
  `The skip machinery must load even on a run that never takes the skip:` (pinned fragment
  `import the skip helper at module load` preserved intact).
- Matrix-projection sentence tightened to remove a triple restatement of "spec is authoritative".

## Pins (grepped in `tests/` and `guardrails/` before any change)

No pinned sentence was altered. Every pinned string is a FRAGMENT of a sentence; where a sentence
carrying a pinned fragment was reworded, the pinned fragment itself was preserved **verbatim**
(OLD == NEW), so no pinning file needed editing. Pinned fragments confirmed still present after the
rewrite:

| Pinned fragment (OLD == NEW, unchanged) | Pinning file |
|---|---|
| `the look itself stays the human's eye` | tests/test_norm_conformance_law.py:38 |
| `never a render inventing its own structure shipped green` | tests/test_norm_conformance_law.py:30 |
| `norm-conformance row`, `every norm section and row name present in the render`, `plan-vs-prototype diff line` | tests/test_norm_conformance_law.py:25,26,34 |
| `a mirror that can never catch the formula being wrong` | tests/test_mirror_assertion_ban.py:23 |
| `derives independently of the code under test`; `a hand-computed constant, an independent derivation, or a recorded real output` | tests/test_mirror_assertion_ban.py:22,29 |
| `the test level follows the layer the change touches`; `presentation change is asserted at browser-computed`; `single-module change is asserted at its module's interface`; `a cross-cutting law` | tests/test_interface_coverage.py:99-102 |
| `each module's tests assert its declared interface`; `one interface-level row per architecture-node block`; `one test per surface it governs`; `interface-level row`; `layer` | tests/test_interface_coverage.py:107-117 |
| `import the skip helper at module load`; `plumbing must not lie`; `re-export completeness test`; `suite log`; `background or delegated run` | tests/test_traceability.py (INV-80 block) |
| `--mute-audio`; `INV-157` | tests/test_harness_template.py:257-258 |
| `removes what it creates`; `leaves the machine as it found it`; `a leak is a defect of the test`; `never a test's workspace`; `download directory is pointed at the temp home` | tests/test_suite_hygiene.py |
| INV-77/78/79 fragments (`real-device walk row`, `relative, wide, and long`, `engine-shaped fixtures`, `never as the only one`, `works-without-it test`, …) | tests/test_traceability.py |

Verification: the six directly-affected pinned test files all pass (54 tests) after the rewrite.

Note: `workshop noise` + `problem ledger` are pinned in tests/test_traceability.py:975 — but for the
**feedback-intake** skill's route table, not for test-author. In test-author these are the same
defined pack routing terms, so they were left verbatim for vocabulary consistency (see unchanged list).

## Cold-read rounds

Two fresh zero-context reader rounds.

- Round 1 flagged 5 "blocking" stops. Judgment: 3 were pack cross-references grounded in other pack
  documents by design — `norm` (grounded at first use by the `norm: <path>` INV-43 pointer), `the
  three-question fitness test [INV-122]`, `spec anchors ... the parent` (a defined pack term, unpacked
  in the paragraph body). Defining those here would be scope creep that changes the skill's meaning,
  so they were left. 1 (`kind-abstract shape`) was left because `kind-abstract` is established pack
  vocabulary (used in PRODUCT_SPEC and tests/fixtures/specformat). 1 genuine local defect fixed: the
  self-contradictory skip-machinery topic clause.
- Round 2 (confirming) found **no** blocking stops. It noted one non-blocking redundancy in the
  matrix-projection sentence, which was then tightened.

## Sentences left unchanged because a rewrite risked meaning or vocabulary

1. `The never side: never a render inventing its own structure shipped green.` — pinned verbatim
   (test_norm_conformance_law) AND is the regression-fence law statement, not a definition-by-denial.
2. `such an assertion is a mirror that can never catch the formula being wrong, since the code is only
   ever asserted equal to itself.` — the "mirror" phrasing is pinned verbatim (test_mirror_assertion_ban);
   it is also grounded inline by the trailing clause. Left as-is.
3. `The ladder is a kind-abstract shape ...` — `kind-abstract` is established pack vocabulary; changing
   it would break pack-wide consistency. Grounded by the cited INV-135 and the sentences that follow.
4. `... it is workshop noise on the problem ledger [SPEC INV-23] instead.` — `workshop noise` is a
   defined pack routing category; kept verbatim for vocabulary consistency. The `instead` is a lawful
   routing contrast, not a definitional denial.
5. Frontmatter description (`NOT for a project with no proven spec or matrix`; `never a substitute for
   product-prover`) — trigger/boundary semantics, left per the task's constraint.
6. Substantive prohibition/fact statements using "never" that are NOT contrast-by-denial definitions,
   left as lawful: `what it must never do` (the never-side rule); `never a test's workspace` (pinned);
   `never a retry, a rerun-until-green, or a raised timeout`; `never a live concurrent run`; `exit code
   is never the verdict`; `never as the only one`; `the suite can never turn green` / `never shipped off
   green alone`. Each states a rule or fact rather than defining a thing by its denied neighbour.

## Pre-existing failure (NOT caused by this rewrite, out of write set)

`tests/test_traceability.py::TestPackListParity::test_real_repo_lists_complete` and
`::TestSkillEvals::test_skill_evals_present` fail on repo HEAD: a new `skills/text-audit` skill exists
but has not yet been wired into any pack's closing list, SPEC, README, or OVERVIEW. The parity check
flags all nine pack surfaces, not just test-author. test-author contains no `text-audit` reference and
its closing list was not touched. Adding the skill name is a content/scope change outside a register
rewrite and outside the write set, so it was left alone.
