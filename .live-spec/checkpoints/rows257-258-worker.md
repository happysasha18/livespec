# Rows 257 + 258 worker checkpoint — INV-113 (architecture redesign) + INV-114 (restructure merge gate)

Briefed 2026-07-12, applier role, mechanical landing from pending-draft-row257.md and
pending-draft-row258.md. Row233-worker.md is the proven walk shape. Covers lane 1 (row 257), lane 2
(row 258), lane 3 (bookkeeping: row 260 split + row 261 add). Write-set fixed by the two drafts.

## Baseline (before any edit, 2026-07-12)

- HEAD 027e009, branch main, tree clean.
- `python3 -m pytest tests/` -> 415 passed in 38.29s.
- VERSION: 1.0.29. plugin.json: "1.0.29". PRODUCT_SPEC.md header: v1.0.21. build-pipeline SKILL.md
  `version:` 1.0.7. product-prover SKILL.md `version:` 1.0.1.
- INV-113/M-252 and INV-114/M-253 both verified free (grep clean across PRODUCT_SPEC.md,
  TEST_MATRIX.md, ROADMAP.md, tests/).

## LANE 1 — row 257 (INV-113/M-252)

### Write-set
- tests/test_architecture_redesign_owes_rework.py (NEW)
- PRODUCT_SPEC.md (2 edits: clause insert after line 634-636 area, formal index row after INV-109;
  version header bump)
- skills/build-pipeline/SKILL.md (2 edits: re-carve paragraph extension ~line 215-217, refactor line
  scope ~line 95; version bump)
- TEST_MATRIX.md (1 insert: M-252 row after M-245)
- VERSION (1.0.29 -> 1.0.30)
- .claude-plugin/plugin.json ("1.0.29" -> "1.0.30")
- ROADMAP.md (row 257 status cell -> landed, delegation line)
- docs/prover/2026-07-12-row257-architecture-rework.md (NEW, short form, row233 shape)
- .live-spec/checkpoints/pending-draft-row257.md (append APPLIED+CLOSED line)

### Anchors confirmed present before editing (2026-07-12)
- PRODUCT_SPEC.md:634-636 — "walks this step, and gets re-proven [E-14]." followed by blank line then
  "**The architecture owes numbers, not just names.**" — present verbatim (same paragraph, not two
  separate lines as the draft's old_string implied; draft's old_string block matches when read as
  running text with the two sentences on adjoining lines — confirmed via grep, both substrings present
  in sequence).
- skills/build-pipeline/SKILL.md:215 "Re-carving the whole node map IS legal: it arrives as a
  restructure placement's own queue row (SPEC" present, continues through line 217 boundary text
  matching the draft's old_string.
- skills/build-pipeline/SKILL.md:95 "if the refactor moves node boundaries, ARCHITECTURE.md's pins
  update in the same change." present verbatim.
- PRODUCT_SPEC.md:1848 "| INV-109 |" row present verbatim, matches draft's old_string exactly.
- TEST_MATRIX.md:234 "| M-245 |" row present verbatim, matches draft's old_string exactly.
- INV-113 / M-252 verified free (grep clean, only mention is ROADMAP's row-242 note that they "stay
  free").

### Live version values read (2026-07-12) — bump +0.0.1 over LIVE per brief step 2
- VERSION: live 1.0.29 -> 1.0.30.
- .claude-plugin/plugin.json: live "1.0.29" -> "1.0.30" (lockstep, house pattern).
- skills/build-pipeline/SKILL.md frontmatter version: live 1.0.7 -> 1.0.8.
- PRODUCT_SPEC.md header: live "v1.0.21, 2026-07-12" -> "v1.0.22, 2026-07-12". Draft's 257.7 states "No
  spec-internal version field exists to bump" but the brief's own step 2 explicitly names "spec header"
  as a value to read live and bump +0.0.1, matching the unbroken precedent (row233, row240 continuation)
  of bumping this header on every spec-touching landing. Following the brief + precedent over the
  draft's stale note (same resolution shape as row233-worker.md's documented deviation).
- Base rulebook NOT touched (draft confirms no live-spec-base edits; the seven skill header pins to
  `` `live-spec-base` (v1.0.5) `` do not move).
- ARCHITECTURE.md NOT edited by row 257 (draft 257.7 confirms; no ARCHITECTURE.md home named).

### Status
STOPPED, 2026-07-12 — unpredicted red the draft did not foresee. Not committed, not pushed.

- RED FIRST: confirmed. `tests/test_architecture_redesign_owes_rework.py` run alone against the
  pre-delta tree failed all 3 tests (needles absent) before any edit.
- All 6 edits (257.2 spec clause, 257.3 build-pipeline re-carve para, 257.4 build-pipeline refactor
  line, 257.5 spec formal-index row, 257.6 matrix row, plus the version bumps: VERSION 1.0.29->1.0.30,
  plugin.json lockstep, build-pipeline SKILL.md 1.0.7->1.0.8, PRODUCT_SPEC.md header v1.0.21->v1.0.22)
  applied exactly as drafted, zero content deviation.
- `tests/test_architecture_redesign_owes_rework.py` run alone after edits: 3 passed.
- FULL SUITE after edits: `python3 -m pytest tests/` -> 3 failed, 415 passed (418 total; the new
  test's 3 are inside the 415 passed).
  - FAILED tests/test_traceability.py::TestArchitecture::test_architecture_owns_every_anchor_once
    — `AssertionError: Lists differ: ['INV-113'] != []` — "index anchors with no owning node".
  - FAILED tests/test_traceability.py::TestMatrix::test_matrix_rows_sit_under_their_owning_node
    — `AssertionError: set() is not true : M-252 sits under 'build-pipeline' but cites only
    ['INV-113'] (owned elsewhere)`.
  - FAILED tests/test_guardrails.py::TestGateB_Tests::test_real_content_passes — downstream echo of
    the same two failures (shells out to run the full suite in a scratch copy; not an independent
    defect).

  Root cause, single: ARCHITECTURE.md's Nodes table requires every Formal-index anchor to be OWNED by
  exactly one node's Owns column (traceability suite, INV-15/E-14/E-15), and every matrix row's cited
  anchor must be owned by the node the row sits under. Draft 257.7 states "ARCHITECTURE.md is NOT
  edited by this row (the row's map names no ARCHITECTURE.md home...)" — but INV-113 now sits in the
  spec's Formal index and M-252 sits in the `[node: build-pipeline]` matrix block citing INV-113, and
  ARCHITECTURE.md's `build-pipeline` node Owns column (line 43) does not list INV-113. This is a real
  drafting gap (the draft's own self-verify section does not mention this test or check), not an
  applier error — same shape as row233-worker.md's INV-109/M-247 gap-density stop.

  This is a design call outside an applier's mandate: the fix is almost certainly a one-line addition
  of `INV-113` to ARCHITECTURE.md:43's `build-pipeline` Owns column (the row's own map does name
  build-pipeline as the owner node: "Owner node = build-pipeline (it owns the architecture step and
  the refactor door)" — draft line 20), but the brief's STOP rule calls for halting rather than
  picking that fix unprompted, since it silently expands the write-set the draft declared. Per the
  brief's explicit STOP rule, halting here.

- Working tree state: all 6 edits + version bumps are LEFT IN PLACE, uncommitted, for the orchestrator
  to inspect/resolve. `tests/test_architecture_redesign_owes_rework.py` (new file) is also left in
  place. ROADMAP.md, the prover short-form doc, and the pending-draft append line were NOT started.
  Lane 2 (row 258) and lane 3 (bookkeeping) NOT started, per the brief's "stop that lane and everything
  after it" rule. Nothing staged, nothing committed, nothing pushed.

### Continuation, 2026-07-12 — the orchestrator's call resolves the lane-1 stop

The orchestrator's call: the draft had a real gap; the fix is the one line the applier already
identified. Added `INV-113` to ARCHITECTURE.md:43's `build-pipeline` node Owns column (the row's own
map already names build-pipeline as owner — "Owner node = build-pipeline"; precedent: row 233's draft
carried the same kind of ARCHITECTURE.md edit for INV-109). Also added a `:215` pin (the re-carve
paragraph) to build-pipeline's pin list alongside the existing four pins, matching the house pattern
of one pin per home. This edit was NOT in the draft's declared write-set; it is recorded here as an
applier-side addition made on the orchestrator's explicit call, not a unilateral judgment.

- **Full suite after the ARCHITECTURE.md fix:** `python3 -m pytest tests/` -> 418 passed in 39.57s,
  0 failed. Both traceability failures and the guardrails echo cleared.
- **Prover short form:** docs/prover/2026-07-12-row257-architecture-rework.md written per the row233
  shape, 0 must-fix, with a line recording the gap and the orchestrator's call, per instruction.

## LANE 2 — row 258 (INV-114/M-253)

### Write-set
- tests/test_restructure_merge_gate.py (NEW)
- PRODUCT_SPEC.md (2 edits: clause insert after INV-111 layout-vehicle clause, formal index row after
  the INV-113 row lane 1 inserts; version header bump)
- skills/product-prover/SKILL.md (1 edit: new paragraph before "## Phase 0 — Triage"; version bump)
- skills/build-pipeline/SKILL.md (1 edit: new bullet after INV-109 restyle bullet; version bump,
  sequential after lane 1's bump)
- TEST_MATRIX.md (1 insert: M-253 row after M-190, `[node: product-prover]` block)
- VERSION (lane-1 result -> +0.0.1)
- .claude-plugin/plugin.json (lockstep)
- ROADMAP.md (row 258 status cell -> landed, delegation line)
- docs/prover/2026-07-12-row258-restructure-merge-gate.md (NEW, short form)
- .live-spec/checkpoints/pending-draft-row258.md (append APPLIED+CLOSED line)

### Anchor note
Row 258's Formal-index anchor (§258.5) sits ON the INV-113 row lane 1 inserts — a genuine cross-draft
dependency, flagged by the draft itself (§258.8) with a fallback (anchor on INV-109 instead, place
after it) if 257 is not yet landed. Since lane 1 lands first in this walk, the intended anchor should
exist; verify post-lane-1 text before applying lane 2's index insert, per the brief.

### Pre-check per the orchestrator's message: does 258's draft carry the same ARCHITECTURE.md gap?

Yes, same shape as lane 1, but NOT ambiguous. The draft's own DELTA section states plainly: "Owner
node = product-prover (it owns the pass whose findings the gate routes), so the matrix row sits in
the `[node: product-prover]` block." No block among 258.1-258.8 edits ARCHITECTURE.md. Following the
orchestrator's instruction, added `INV-114` to ARCHITECTURE.md:42's `product-prover` node Owns column
proactively (before running the full suite), plus a `:168` pin for the new restructure-merge-gate
paragraph, alongside the existing three pins.

### Status
DONE, 2026-07-12 ~03:1x. All five drafted edits (258.2 spec clause, 258.3 product-prover home, 258.4
build-pipeline home, 258.5 formal-index row, 258.6 matrix row) applied exactly as drafted, zero
content deviation. Plus the ARCHITECTURE.md addition above (not in the draft's declared write-set,
added per the orchestrator's instruction).

- RED FIRST: confirmed. `tests/test_restructure_merge_gate.py` run alone against the pre-lane-2 tree
  failed all 4 tests before any edit.
- Version bumps: VERSION 1.0.30->1.0.31, plugin.json lockstep, build-pipeline SKILL.md 1.0.8->1.0.9,
  product-prover SKILL.md 1.0.1->1.0.2, PRODUCT_SPEC.md header v1.0.22->v1.0.23.
- `tests/test_restructure_merge_gate.py` run alone after edits: 4 passed.
- FULL SUITE after edits (ARCHITECTURE.md fix applied proactively, before the first full-suite run):
  `python3 -m pytest tests/` -> 422 passed, 0 failed. No unpredicted red this lane — the traceability
  gap that stopped lane 1 was headed off by adding the owning-node edit alongside the drafted edits.
- Prover short form: docs/prover/2026-07-12-row258-restructure-merge-gate.md, 0 must-fix, with a line
  recording the same-shape gap and the proactive fix.

## LANE 3 — bookkeeping (row 260 split + row 261 add)

Precedent: commit 30a62f9 "Sweep inbox: three wishes into ROADMAP rows 257-260" — pure ROADMAP
bookkeeping, no version bump. This lane follows the same shape: no VERSION/plugin.json/spec-header
bump, ROADMAP.md edits only plus the two draft-file append lines.

### Write-set
- ROADMAP.md (replace row 260 with rows 260a + 260b per pending-draft-row260.md's recommended split;
  add row 261 per pending-row247-analysis.md's DECIDE-split recommendation)
- .live-spec/checkpoints/pending-draft-row260.md (append "SPLIT ACCEPTED + CLOSED 2026-07-12 (rows
  260a/260b queued)")

### Status
DONE, 2026-07-12 ~03:1x. ROADMAP row 260 replaced with rows 260a (abstraction fitness, P7) and 260b
(code compaction with its second trigger, P11), five-cell format matching neighbors, both `queued
2026-07-12`, both born-of pointing to the six-principle wish + the architect draft, per
pending-draft-row260.md's recommended split. Row 261 added (GitHub Issues as a public repo's stranger
door, a DECIDE, no build) per pending-row247-analysis.md's split recommendation. Both draft files
closed with their append lines. No version bump (precedent: commit 30a62f9). Full suite re-run after
the ROADMAP edits: `python3 -m pytest tests/` -> 422 passed, 0 failed (unchanged count — pure
bookkeeping, no new tests).
