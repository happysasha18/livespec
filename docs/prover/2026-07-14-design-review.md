# Prover / architecture record — the design-review pass (INV-141/142, `design-reviewer` node)

**Date:** 2026-07-14
**Prover skill version:** product-prover **v1.1.0** (the copy that ran the passes below; bumped to v1.1.1
at this same 1.3.0 landing).
**What this record covers:** the two parts a structure change owes — the spec prove of the two new
clauses (Part 1) and the architecture-lens re-prove of the new node, its seams, and its ownership
(Part 2, the MINOR-gate audit's Pass 2). This is the record ARCHITECTURE.md cites at the design-reviewer
node row and in the prover-record table. Part 3 records that every finding below was folded into the
landed material.

---

## Part 1 — Spec prove of the two clauses (INV-141 / INV-142)

**Mode:** FEATURE-FIT on the two-clause delta, plus the full stress-lens sweep against the neighbours it
cites. **Reviewer:** independent prover — did NOT author the clauses (INV-46 fresh-eyes discipline).
**Under review:** the two prose clauses + two Formal-index rows. **Live tree read, not touched:**
`PRODUCT_SPEC.md` (INV-140, INV-125, INV-126, INV-136, INV-138, INV-59, INV-97/E-10),
`skills/product-prover/SKILL.md`.

### Verdict at the prove: needs iteration (all findings since folded)

The concept is sound and fills a real blind spot — element-level, undeclared siblings living *below* the
page-level registry that INV-125's registry-reading lens is structurally blind to. The
discovery→declaration→enforcement pipeline is clean, the never-blocks property genuinely follows from
INV-140's derivation, and the wish is delivered. The delta shipped with **one must-fix** (the
confident/likely criterion undefined) and a cluster of **should-clarifies**; none cut at the concept.
All were tightened before the clauses landed (Part 3).

### Hypotheses tested (the seven) — outcome

1. **Duplication** — CLEARED. INV-125/126/136/138 all operate on *author-declared* classes/pairs/layers/gates
   read from the registry (surface level). The design review works on *undeclared* role-similarity at the
   *element* level, below the registry. Complementary, not duplicate.
2. **Fusion** — CLEARED. INV-141 = the pass (discover, parity, record, close the loop); INV-142 = how each
   finding is graded and routed. Separable; a legitimate split.
3. **"Never blocks" vs INV-140** — CLEARED. A same-kind divergence over an *undeclared* grouping has no
   stated invariant behind it, so by INV-140's own derivation it is a recommendation, never a defect. The
   claim follows; it is not merely asserted. The clause is safe precisely because it holds to ONE producer
   and omits the missed-edge producer (which would be the INV-72/138 blank-answer class those lenses treat
   as blocking).
4. **Echo channel vs existing "surface to him"** — CLEARED. INV-126/138 surface *declared* pairs'/gates'
   undecidable timing; INV-142 asks a different question about *undeclared* groupings. Both ride INV-30's
   batched-question path — shared infrastructure, no contradiction. The cap of 3 is scoped to design-review
   asks.
5. **Inventory vs registry authorship** — the boundary needed making airtight (DR-F4).
6. **Unwritten edges in the new clauses (dogfood INV-138/INV-72)** — several axes confirmed (DR-F1/2/3/5/6).
7. **Goal miss** — CLEARED. INV-141 discovers, INV-142 echoes the strongest divergence with two objects +
   a recommended default + a cap. The born-of case (polaroid vs gallery photo) resolves to exactly one ask.

### Findings (all folded — see Part 3)

- **DR-F1 (must-fix, missing-rule)** — INV-142 never stated how a finding is judged `confident` vs
  `likely`, so the routing was unrunnable. Fix folded: the clause now defines `confident` = the grouping
  and divergence stand on the spec text alone, `likely` = the deciding fact lives only in the human's intent.
- **DR-F2 (should-clarify, liveness)** — an unanswered echo ask had no stated fate. Fix folded: a raised
  ask is held on the dated record and not re-raised on its own until answered [INV-130].
- **DR-F3 (should-clarify, state-space)** — the cadence named only two modes. Fix folded: the design
  review stands down at FEATURE-FIT intake and the M-6 push re-check; the cadence is complete across every
  mode.
- **DR-F4 (should-clarify, composition)** — the "writes nothing to the registry" boundary was implied. Fix
  folded: the inventory is the pass's own transient working list, never written into the surface registry,
  which stays hand-authored [E-10, INV-97].
- **DR-F5 (worth-considering, abstraction)** — the whole-behaviour/parameter line had no fallback. Fix
  folded: where the call is itself unclear, the finding is below the ask bar.
- **DR-F6 (should-clarify, bounds)** — a named-but-behaviourless element could flood divergences. Fix
  folded: such an element stays out of the group until it carries at least one behaviour clause.
- **DR-F7 (should-clarify, actors)** — the homes lines named product-prover, but the design places the
  pass in a NEW skill. Fix folded: the homes now name the design-reviewer skill and its ARCHITECTURE node.
- **DR-F8 (worth-considering, composition)** — never-blocks was stated twice. Fix folded: INV-142 owns the
  derivation; INV-141 references it.
- **DR-F9 (should-clarify, consistency)** — the boundary against an *already-declared* INV-125 class. Fix
  folded: where a governing class clause exists and under-enumerates a member, that routes through
  INV-125's defect path, not the design review's recommendation path.
- **DR-F10 (worth-considering, abstraction)** — memo/clause scope mismatch on the echo channel's producers.
  Resolved on the record: the clause deliberately narrows to ONE producer; a later producer earns its own
  clause.

### What is working (real, not filler)

The discovery→declaration→enforcement pipeline lands each stage in the skill that already owns it. The
never-blocks safety property is derived from INV-140's own ground, not asserted. The strong-signal bar
(three conditions) + the cap of 3 + the two-objects-in-hand form is a low-noise escalation that reuses
INV-30's road. The Formal-index rows match the house format; INV-141/142 confirmed as the next-free codes.

---

## Part 2 — Architecture-lens re-prove of the node add (the MINOR-gate audit's Pass 2)

A new node is a structure change, so ARCHITECTURE.md was re-proven with the architecture lens in the same
movement. This is the audit's Pass 2 read, recorded here as the node-add re-prove.

**The new `design-reviewer` node — checked clean.**

- **Ownership (one home per fact).** INV-141 and INV-142 are owned once, by the design-reviewer node. No
  other node claims them; the coverage rule (every spec anchor in exactly one node's "owns" column) holds.
  The prover node carries the discovery-side sibling only as a *pointer* with the owner named and no INV
  codes, matching the lens-lending convention it already uses for the eight foreign lenses.
- **Seams.** All three new seams mirror existing shapes: `spec → design review` mirrors `spec → prove`
  (format owner spec-author, the shape both sides speak); `design review → record` mirrors `prove → record`
  (a dated file with a per-finding outcome column, now carrying the `[-suffix]` collision arm its prover
  sibling carries); `design-review ask → human` rides communicator's batched-question path, owner named.
- **The pin resolves.** `skills/design-reviewer/SKILL.md:1` plus the real similarity-lens, confidence-read,
  echo-channel, and record-discipline sections exist and carry the sentences the node row promises.
- **Counts consistent.** Nine skills (eight working + base) across ARCHITECTURE, the base heading, and the
  five pack-whole footers; 18/18 node blocks in the matrix. README and OVERVIEW name design-reviewer.
- **Cross-cut counter.** 24 doc-family pairs at/over threshold — every one the inherent self-hosting
  signal of a method pack (each law lands as spec clause + skill text + matrix row + architecture note).
  No non-inherent pair over threshold. The one real accumulation (the prover node carrying eight foreign
  lenses plus the discovery-side pointer) is exactly what the design-reviewer carve answers: the
  discovery-side check got its own node instead of a ninth carried lens. No boundary move recommended.

**Cross-seam pairs checked clean (Pass 1, tried and held):** INV-141/142 vs INV-140/M-6/INV-114 (all
findings recommendation-kind by construction, so never-blocks agrees with fold-every-defect; the pass
stands down at the push gate so its findings never meet M-6's folding; the delta-scoped gate untouched);
INV-141 vs INV-125/126/136/138 (the declared-class carve is explicit both ways); INV-141 vs INV-97/E-10
(the inventory is transient, never written to the registry, pinned by M-283's never-side); INV-142 vs
INV-59/INV-130 (the decided-sentence kill switch composes with answered-closes-forever; the held-ask
no-re-fire mirrors INV-130); INV-141/142 vs INV-11/INV-105/ACT-3/T-18 (the pass runs inside the
pen-holding lane's prove stage, no new writer, no lane rule touched).

**Verdict of the re-prove:** the node, its seams, and its ownership are sound. The design boundary with
the prover and the declared-class lenses is genuinely clean, and the counter shows nothing but the
self-hosting signal.

---

## Part 3 — Fold status at the 1.3.0 landing

Every Part-1 finding (DR-F1…DR-F10) was folded into the landed clauses, the Formal-index rows, and the
`design-reviewer` SKILL.md before the codes landed. The MINOR-gate audit (`docs/prover/` sibling read of
2026-07-14) added four must-fix folds — this deposited record (D1), the ROADMAP row 310 (D2), the six
skill version bumps + base pin sweep (D3), and design-reviewer added to the spec's roles list (D4) — plus
eight should-clarify folds (R1–R8), all folded at this landing. The suite is green whole apart from
Gate A's `test_real_repo_passes`, which clears at the commit that carries this record.
