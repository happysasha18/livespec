---
name: test-author
description: Derive TEST_MATRIX.md from a proven spec through a proven architecture, then write the tests — the level ladder (string / DOM-text / browser-computed / pixel), real-artifact assertions, red-first proof, the pinned skip-set, and traceability as a standing test. Normally invoked by build-pipeline at its matrix and test steps (5–6). Use it directly when the user asks to "derive the test matrix", "pin test levels", "why did green tests miss this bug", or "rebuild the suite by the method". NOT for a project with no proven spec or matrix — "write tests for X" alone routes to build-pipeline first (the spec and architecture steps come before tests); and never a substitute for product-prover — this skill covers facts with tests, the prover finds holes in what documents claim.
metadata:
  version: 0.1.0
---

# test-author — from a proven spec to tests that would have caught the bug

> Part of the **live-spec pack** — the shared working rules (ask-never-guess · plain words, anchors trail ·
> one surface = one name · one home per fact · junior/senior split · checkpoints · the concurrent-edit
> fence · freshness · journal discipline · attic-never-delete · verify by deed · the human's gates · claims
> need primary sources · fix the class, sweep look-alikes · the door before code · prototype ≠ product) live ONCE in the pack's base skill, `live-spec-base` (v0.1.23), together with the
> settings ladder — this skill references them and elaborates only its own domain. Used standalone, this
> note is plain advice.

The method was born on a real project: two user-visible bugs shipped past ~660 green tests, because
the facts those tests covered were pinned at the wrong LEVEL — string checks proved the code SAYS the
right thing while the page showed the wrong one. The rebuild that followed (the track-coach test
overhaul, 2026-07-02..04) produced the level ladder, the state-space walk, and the traceability
enforcement this skill carries. Worked patterns are paraphrased from track-coach's matrix (MIT,
credited); the pack's own matrix template is the shipped shape.

## What this skill owns

Two artifacts, in order. **TEST_MATRIX.md** — the spec projected into a checkable grid: derived from
the proven spec THROUGH the proven architecture, one block per architecture node, and the spec stays
the source of truth (the matrix is a projection, never a second authority). Then **the tests** — one
owning test per matrix row, asserting the real shipped artifact. build-pipeline keeps the order and
the gates; product-prover keeps semantic review; the guardrails keep mechanical enforcement. This
skill owns the JUDGMENT in between: which facts, at which level, asserted how.

## Deriving the matrix (the pipeline's step 5)

1. **Open with the artifact inventory** — every file the user receives, each owning at least one
   rendered-level row. An artifact nobody renders in a test can ship broken with the suite green.
2. **Blocks per architecture node; every spec fact ≥ 1 row.** A fact with no row is a derivation
   defect, found here, fixed here — never discovered later by a user.
3. **Every row states BOTH sides** — what the fact does, and what it must never do. The never side is
   the regression fence: a row without it proves the happy path and nothing else.
4. **Every row pins a LEVEL** — the ladder below. The level is the row's most important judgment.
5. **Name the state space before filling cells.** Axes first: view states (mode, toggles), data
   states (present / absent / empty per source). A cell is element × view-state × data-state; a fact
   that must hold in EVERY state is an invariant and owns its own test. A flat element-by-view grid
   hides the data axis — the classic home of "empty shell shipped" bugs.
6. **Matrix-local row ids are legal, spec anchors stay the parent.** One spec fact may project into
   several separately-testable rows (sub-variant suffixes), and node-level mechanics (a decoder
   table, a gate mechanism) may carry their own contract rows. The spec anchor cited is the parent
   fact; an audit finding "matrix id absent from the spec" for these two kinds is expected.
7. **Close by walking the coverage checklist** (the template ships it): every anchor covered · every
   node's never-side rows present · no stale references. Walked, not checked off from memory.

## The level ladder — where green suites lie

| Level | Proves | Lies about |
|---|---|---|
| string | the source or output text contains X | everything the user actually sees |
| DOM-text | the rendered document says X | position, visibility, color, interaction |
| browser-computed | real layout/style/behaviour in a real engine | subjective look and feel |
| pixel | the rendered look matches a frozen norm | nothing — but brittle; reserve it |

Pinning rules: any fact about visibility, layout, color, or interaction takes browser-computed or
higher — a string test on such a fact is the exact class that shipped the two bugs. Content facts
take DOM-text. Wiring and config facts may take string, legally. Pixel is reserved for look-and-feel
against a frozen, approved norm. When in doubt, ask what the USER would see broken — the level must
be able to see the same thing.

## Writing the tests (the pipeline's step 6)

- **Assert the real shipped artifact**: render the page, produce the file, call the function — then
  inspect the output. A source-string match on such a fact is a matrix defect, not a test.
- **Red first, proven.** A new test runs against the pre-change state (or the bug) and FAILS before
  the implementation makes it pass; the red run is recorded. A test born green proves nothing.
- **Never edit a test to make a change pass.** A red test means the change or the matrix cell is
  wrong; the cell is corrected first, and the test follows the corrected cell.
- **Pin the skip-set.** Green means zero failures AND the skip list is exactly the expected, pinned
  set. An unexpected skip (a browser missing, a fixture absent) is a failure wearing a quieter color.
- **Traceability is a standing test, not a vow**: a test in the suite fails on a matrix row citing a
  missing test, a duplicate id, a spec fact with no row, or a resolved-but-live decision marker — so
  drift is caught at every commit.
- **The bug protocol:** a bug fixes the matrix cell (or adds the missing invariant row) first, then a
  test proven red on the bug, then the code. Code chases the matrix.

## When NOT to use it

Not without a proven spec and architecture — the derivation has nothing sound to derive from, and
"write tests for X" alone routes to build-pipeline (the earlier steps first). Not for reviewing
documents (product-prover's job). Not for the mechanical gates themselves (the guardrails' job —
this skill DERIVES what they later enforce).

> The pack, whole: **live-spec-base** holds the shared rules and defaults · **spec-author** writes the spec ·
> **product-prover** reviews it · **build-pipeline** ships the change · **test-author** derives the matrix
> and writes the tests · **communicator** makes the human exchange land · **publish** sees the work out
> the door, owing its kind's checklist.

Credits: the level ladder, the state-space walk, and the bug protocol were proven on track-coach
(github.com/happysasha18/track-coach, MIT) during its 2026-07 test overhaul; the enforcement pattern
follows its `test_traceability.py`. Paraphrased with thanks, per the pack's borrowing practice.
