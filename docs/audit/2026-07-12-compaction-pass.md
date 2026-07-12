# Compaction pass — 1.1.0 MINOR gate (code side)

Auditor: Opus. Date: 2026-07-12. Repo HEAD at pass: `8125b2c`, tree clean.
Gate step: the M-1 milestone list's doc-compaction item — "strip redundancy from
spec/matrix/queue/skills/ledger [E-24], and sweep the test suite the same way. Delete a
duplicate or superseded test only when the matrix audit shows its rows still covered by a
live test." (PRODUCT_SPEC.md line 701). This is the first code-side compaction pass; prior
compaction work was recorded as milestone records (docs/queue-archive/2026-07-08-milestone-compaction.md)
and audit notes (docs/audit/2026-07-08/milestone-audit.md).

This is a recorded pass. It names every candidate, classifies it, and routes it. It lands
no edit. Any future landing of a candidate below is bound by the removal-listing law
[INV-109] and the one-row-delta law [INV-39]. The abstraction judgment on each code
candidate uses tonight's three-question test — testability, reuse, parallel-safety — kin to
docs/queue-archive/2026-07-12-from-alexander-design-principles-impact-analysis-and-compaction.md.

## Counts

- SAFE-NOW: 1
- QUEUE: 1
- LEAVE: several (docs precheck candidates + one code note), listed below.

## CODE — scripts/*.py and tests/*.py

### SAFE-NOW

**C1 — shared test-read helper (extract one home).** `read_flat(rel)` is defined
byte-for-byte identically in 20 test files (same body, same docstring: `return " ".join(f.read().split())`).
A non-flat `read(rel)` repeats in 10 more, and the `ROOT = os.path.abspath(...)` line
repeats in 36. Extraction: one home — add `ROOT`, `read`, `read_flat` to `tests/conftest.py`
(it already exists for the suite-hygiene fixture) or a `tests/_helpers.py`, and delete the
local copies. Three-question test: testability — the helpers are pure read-and-normalize
functions the whole suite already exercises, so a mistake fails a test at once; reuse — 20
identical copies prove reuse, not speculation; parallel-safety — read-only file reads with no
shared mutable state and no temp writes, safe under xdist and under the session-scoped
hygiene fixture. All three pass. Mechanical and suite-protected. The one caveat is breadth:
the edit touches 30-plus files. It still lands as ONE refactor row (each edit is delete-local-def
plus one import), so it fits its own lane cleanly. Worth doing: with 20 identical copies, one
change to the normalization (say, also stripping a zero-width char) would otherwise mean 20
edits — real drift risk.

### LEAVE

**C2 — no dead scripts, no dead code.** Every one of the 10 scripts has a live caller,
cross-checked against the CI workflow (.github/workflows/gates.yml), the pre-commit and
pre-push hooks (.git/hooks/), the test suite, other scripts, and the docs. `gate_common.py`
is already the shared home for the four spec-* scripts (spec-style-lint, spec-judge,
spec-redundancy-precheck, spec-done-gate all import it) — the extraction the doc-compaction
law would ask for is already done on the script side. The `assert_green`/`assert_red` pair in
test_scaffold_guardrails.py is local to one file and needs no shared home. Cost of any further
code move here exceeds value.

## DOCS — PRODUCT_SPEC.md / skills bodies

The redundancy precheck ran on PRODUCT_SPEC.md
(`python3 scripts/spec-redundancy-precheck.py PRODUCT_SPEC.md`): 14 candidates, 0 waived. The
precheck surfaces candidates for author judgment; it does not return a verdict of violation
(this matches how prior compaction treated it). On inspection, most candidates are legitimate:
paraphrases of one idea across distinct law contexts (containment 0.86–0.91), or a Formal-index
/ line-law gloss restating prose the index is built to restate (INV-13's one-home law scopes to
a shared rule across skills, not to prose beside its own index). Examples left as-is: echo-name
at line 149 versus the feature-map line-law at 904 (different objects — an echo-name definition
versus what a feature-map line carries); the problem-ledger status lines at 964/972 (adjacent,
one defines the status and one the second-occurrence action).

### QUEUE

**D1 — the "one row's delta" invariant [INV-39] is stated three times** (lines 459, 495,
1481), each in a distinct law (parallel-lanes, several-trains purity, tight-mode batch) and
each carrying the anchor. This is the one candidate that reads as genuine reinforcement worth a
second look rather than clear-cut design. It is a spec-author judgment call, not a mechanical
strip — folding two of the three could weaken a law's local readability. Route as a low-priority
QUEUE row for spec-author to judge whether one home plus two pointers reads better than three
anchored restatements. Not urgent; the suite and the anchor keep it coherent today.

## Gate-wording verdict

The gate step's wording is an action — "strip redundancy … and sweep the test suite the same
way." A recorded pass alone does not fully discharge it. This pass discharges the identification
-and-routing half: it names every candidate, classifies each, and routes the two live ones (C1
to its own SAFE-NOW lane, D1 to a QUEUE row). The one mechanical strip worth doing — C1, the
shared test-read helper — still owes its landing; it is safe to land now as its own row but is
not landed here, because this auditor pass writes one file only and the milestone runs as one
indivisible train [T-18], so landings happen in the gate's own hands. No duplicate or superseded
TEST case was found to delete (C1 is duplicated helper code inside live tests, not duplicate
coverage — extracting it removes no matrix row). So the test-deletion clause has nothing to act
on this pass.

C1 landed `4be5ecb`
