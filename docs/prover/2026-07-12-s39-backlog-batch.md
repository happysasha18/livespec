# Prover record — session 39 backlog batch (2026-07-12)

Pass over PRODUCT_SPEC.md and ARCHITECTURE.md after the s39 backlog-clearing batch: eleven queue rows
landed (263, 273, 269, 264, 265, 266, 267, 268, 270, 260a, 260b). Mode: DELTA-scoped FULL — the new and
changed clauses reviewed against the whole spec, the architecture re-read for ownership and seam
consistency (INV-116: the architecture is proved beside the spec at the push gate). Auditor: Opus
(orchestrator seat, senior). Repo HEAD at pass: post-035c914.

## What changed in the batch

New invariants: **INV-121** (derive from a proven artifact before offering a fork), **INV-122** (a new or
carved node passes a three-question fitness test), **INV-123** (compaction is a scheduled station for code
as well as docs, with a second trigger). Edited: **INV-108** (behavioural-rule breaks route to one home,
PROBLEMS.md). New matrix rows M-261..M-264. Derived-doc header policy (M-261, no new anchor). Skills:
build-pipeline 1.0.14, product-prover 1.0.3, communicator 1.0.5, spec-author 1.0.3, live-spec-base 1.0.6
(all working skills re-pinned to it), guardrails/check-prover-record.sh (inbox carve-out).

## Architecture-lens checks (six, INV-116)

1. **Every spec fact owned by exactly one node** — INV-121, INV-122, INV-123 each added to the
   build-pipeline node's owns-list (they govern the intake/architecture/rhythm the node owns). No orphan
   anchor; `test_architecture_owns_every_anchor_once` green.
2. **No node without spec backing** — no new node; the batch added no structure. Clean.
3. **Every seam names what crosses it** — row 273 added the `architecture → prove` seam; the Seams table
   is complete for the new law. Clean.
4. **Quality budgets with instrumentation homes** — untouched by the batch.
5. **Runtime view walks every promised flow** — no flow changed.
6. **Placement view** — no node placement changed.

## Delta findings — contradiction and composition sweep

- **INV-121 vs INV-4 / INV-60 / INV-31** — complementary, no conflict. INV-121 is the read-the-doc twin of
  ask-never-guess: INV-4 forbids inventing an answer, INV-121 forbids offering a fork the documents already
  settle; taste calls stay askable (INV-60/INV-31 untouched). No hole.
- **INV-122 vs INV-15 / INV-113 / the speculative-node prose (spec line ~637)** — INV-122 extends the
  existing speculative-node flag with the three-question test; consistent, cited both ways. No hole.
- **INV-123 vs INV-115 / INV-13 / INV-109 / INV-98** — INV-123 widens the compaction station to code beside
  the doc half (INV-115), citing INV-109 (list removals), INV-122 (extraction gate), and the convergence
  lock (INV-98, rows 216-218) rather than restating them. One home per fact held. No hole.
- **INV-108 (row 264)** — behavioural-rule breaks now route to one home (PROBLEMS.md); consistent with
  INV-11 (one home) and INV-23 (the ledger). The ROADMAP rows that doubled as break-records now point back.
  No hole.
- **Traceability** — `tests/test_traceability.py` green: every new anchor carries its Formal-index row, its
  owning-node entry, and a matrix row under that owner (the drafter self-verify list, row 263, walked for
  each). Every matrix row cites an existing test.

## Disposition

**Zero must-fix.** The batch is delta-clean: three new invariants, each owned, cited, and non-colliding;
one edited invariant consistent with its family. Three rows carry honestly-flagged forward legs, recorded
in their status cells (266's under-500 size call — owner's word owed; 270's leg 3 — wired into row 259's
Done-when; 260b's first code-compaction pass — fires at the next milestone audit). The full suite reads
489 green with this record committed (gate-a's freshness satisfied for the pushed state). Ready to push.
