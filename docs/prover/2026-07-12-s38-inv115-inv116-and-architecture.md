# Prover — s38, INV-115 + INV-116 as landed, and the first full architecture pass (2026-07-12)

Prover skill version: product-prover on live-spec-base v1.0.5 (six-check architecture lens). Mode: FULL
over the two amended invariants plus a full architecture pass over ARCHITECTURE.md — the pass INV-116
now mandates at every M-1 and M-6 gate. Both documents read as they stand this session: PRODUCT_SPEC.md
(1869 lines) carrying INV-115 and INV-116, and ARCHITECTURE.md v0.3.0 (192 lines) as the coverage
INV-116 requires.

**State proved:** PRODUCT_SPEC.md's two new invariants and ARCHITECTURE.md as a whole.
- INV-115 — the full-pass doc-compaction discipline, elaborating the M-1 milestone gate's
  doc-compaction step (spec line 701; index line 1857).
- INV-116 — the prover runs over ARCHITECTURE.md beside PRODUCT_SPEC.md at M-1 and M-6, so the
  design-level seams meet the same structured review the spec gets (spec lines 695, 734; index 1858).

**Verdict:** ready — 0 must-fix. One should-clarify, a completeness gap in the architecture doc's own
Seams table opened by INV-116's new crossing; one worth-considering on the architecture doc's Prover
record table; both delta-scoped, neither blocking. The two invariants are sound as landed: correct
home, no new node, no new mechanism, no contradiction with a standing law.

## The two invariants, as landed

**INV-115 is sound.** It refines the existing M-1 compaction step rather than adding a mechanism: a
fact lives once with a pointer from every other home, a pass removes only redundancy and accounts for
each removal (INV-109), a restructure rides the content-preserving layout vehicle only (INV-111), and
nothing grows unboundedly (INV-1). The guard it carries is real and load-bearing — a redundant-looking
second statement can be a fact's sole home, with the traceability-read Formal-index rows as the worked
proof (the 2026-07-12 red when they were flattened). Home is correct: build-pipeline owns M-1, and the
anchor sits in build-pipeline's Owns column. No new seam, no clash.

**INV-116 is sound in mechanism and home.** It points the standing gate at an artifact the prover's own
method already covers — Phase 0 of the skill names ARCHITECTURE.md as valid input and runs the
six-check architecture lens on it — so this adds a cadence, not a review type. Home is correct:
build-pipeline owns the M-1 and M-6 gate walks, product-prover executes the pass; the anchor sits in
build-pipeline's Owns column, mirroring INV-99 (skill-creator review at verify, gate-owned by
build-pipeline, executed elsewhere) and INV-113. The build-pipeline / product-prover ownership line
holds: build-pipeline owns what the gate INCLUDES, product-prover owns the review method (M-6, INV-61,
INV-72). The freshness rule it grafts on — a record predating the last ARCHITECTURE.md change is as
stale as one predating the last spec change — composes cleanly with the M-6 freshness discipline.

## The architecture pass (discharging INV-116 this session)

The architecture was proved this pass, with the six-check lens, each check judged at the pack's scale.

1. **Every spec fact owned by exactly one node** — mechanically green: `test_traceability.py` passes
   163/163, and the two new anchors resolve to build-pipeline alone (no double-ownership).
2. **No node stands without spec backing** — the coverage rule holds; the [target] nodes (guardrails,
   snapshot, design-sync) each own real facts.
3. **Every seam names what crosses it and its format owner** — the Seams table holds, with the one gap
   below (F-arch-1).
4. **Quality budgets carry instrumentation homes** — the budgets table states a number and a reading
   home for each (INV-41).
5. **Runtime view walks every promised flow** — all twelve features (F-wish … F-catchup) have a runtime
   row; the Feature-coverage and Runtime tables agree.
6. **Placement view says where every node runs** — five places, each with its load-bearing technology;
   no-secret line present (INV-75).

## Findings

**F-arch-1 — INV-116 establishes an ARCHITECTURE.md → product-prover crossing that the Seams table
does not name, though the symmetric spec crossing is named.**

> "spec → prove | package-docs · product-prover | PRODUCT_SPEC.md, whole document | spec-author" — ARCHITECTURE.md, Seams table

The Seams table exists to name the places two nodes meet, "because that is where composition bugs
live." INV-116 now sends the whole ARCHITECTURE.md across into product-prover at every M-1 and M-6
gate — the exact analogue of the named `spec → prove` seam — yet no `architecture → prove` row records
it. By the architecture doc's own standard, a law-mandated crossing left off the seam inventory is an
incompleteness in the doc, not in the mechanism: the prover already reviews the doc, so nothing breaks
at runtime; the doc's seam list simply trails the law it now carries. Add one row —
`architecture → prove | build-pipeline · product-prover | ARCHITECTURE.md, whole document | templates
(ARCHITECTURE.template.md shape)` — closing the symmetry with `spec → prove`. The paired
`prove → record` seam already covers the architecture pass's record output, so only the input crossing
is missing.

`should-clarify · boundary-issue (composition)`

**F-arch-2 — the architecture doc's own Prover record table will drift from docs/prover/ unless the
architecture passes are logged in it.**

> "| Date | Doc version proven | Record |" — ARCHITECTURE.md, Prover record section

INV-116 makes an architecture prover pass a standing output at every gate, recorded in docs/prover/
beside the spec's. The architecture doc's own Prover record table (last row 2026-07-09, row 180) is the
place those passes belong, yet nothing in INV-116 or the gate walk says the table gains a row per
architecture pass. Left implicit, the table silently falls behind the docs/prover/ directory it
indexes. Add this pass's row to the table when the record lands, and state — at the M-1/M-6 walk or in
the architecture doc's upkeep note — that an architecture pass appends its row here. Low severity: the
records exist on disk regardless; this keeps the doc's index honest.

`worth-considering · hard-to-operate (ops-ux)`

## The prior seven — already open, not re-argued

The for-fun spec pass earlier this session found seven items, captured and queued in
`.live-spec/checkpoints/2026-07-12-prover-spec-findings.md`: F1 (session-token tie-break), F2
(compute-bound worker false-death), F3 (deferred-trigger cadence), F4 (tag-symmetry reverse
direction), F5 (critical-on-any-door preemption), F6 (withdrawn-decision loop), F7 (mid-work re-door
independence). They stand open against the spec prose and are out of scope for this pass — referenced
here so the next run sees them already carried, and re-derived nowhere.

## Disposition

INV-115 and INV-116 ship as landed. F-arch-1 and F-arch-2 are the only new items, both delta-scoped to
INV-116 and neither blocking; they become queue rows (the Seams-table row and the Prover-record-table
upkeep line), each a one-line ARCHITECTURE.md edit. The architecture was proved this pass, discharging
INV-116 for the current state of both documents.

**FOLDED 2026-07-12 s39 (row 273):** F-arch-1 — the `architecture → prove` Seams-table row now stands.
F-arch-2 — the Prover record section and build-pipeline step 4 (the gate walk) carry the append-duty,
and the table is caught up to the 1.1.0 full pass and this s38 architecture pass. Red-proven by
`tests/test_architecture_prove_seam.py`. Both new items closed; the prior seven remain open (rows 273's
siblings, still queued).
