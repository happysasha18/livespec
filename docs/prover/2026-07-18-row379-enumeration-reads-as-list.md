# Prover record — ROADMAP 379: enumerable facts earn bullet structure (INV-215)

Date: 2026-07-18 · Doc version: v2.6.3 (unchanged; the version bumps once at the movement's MINOR gate) ·
Form: SHORT (small delta — a doc-style writing rule, skill/prose kind, no new stateful surface, no
structure change, no new gate) · Mode: CROSS-LINK against spec-author's existing structure rule
("Use lists inside a scenario to break up a wall of prose") and the register cluster [INV-83, INV-166,
INV-203] the clause sits beside.

## Previous records clean

The prior record (docs/prover/2026-07-18-row390-392... and the row-419/420 batch) closed with zero
unfolded must-fix rows. Nothing carried.

## The delta, in one line

INV-215: a prose paragraph carrying an enumeration of three or more distinct, parallel facts earns bullet
or numbered structure; prose stays for the laws, their reasoning, and their boundaries. A stated writing
rule homed in spec-author's structure guidance, read by eye and by the prover's cognitive-load lens.

## The footprint verdict (the row's real question)

The row asked whether the rule also earns a mechanical check or stays a stated doc-style rule. Verdict:
it stays a STATED rule, and earns no mechanical lint of its own. A regex that flagged any prose paragraph
with three-plus comma-separated items would over-flag ordinary rhetorical triads massively — a "neutral,
precise, plain" register triad, or "the rule, its actor, its reason" — and distinguishing a genuine
list-owed enumeration from a rhetorical triad is a MEANING call, not a structural one. That lands it on
build-pipeline's own honest boundary: guardrails catch structure, the prover and the register judge catch
meaning. So the rule lives in two homes — spec-author's structure guidance and the prover's cognitive-load
lens (a reading-load recommendation, never a block) — and touches no push-chain gate: no new gate letter,
no `gate-red-proofs.json` entry, no `gates.yml` step. Nothing in the shared gate chain was edited, so the
lane integrates without colliding with the other lanes' Formal-index or gate-chain writes.

## Cross-link checks

- **Owning node.** INV-215 → spec-author (the structure rule is spec-author's craft). The prover carries
  the cognitive-load reading but does not own the invariant, matching how it carries every other lens whose
  owner is named beside it. One owner, ARCHITECTURE.md spec-author owns-list. PASS.
- **No orphaned anchor.** Formal-index row present; matrix M-396 covers it; the architecture owns-list
  claims it; the two skill homes carry it. The traceability net (every invariant a matrix row, no
  duplicate id) is satisfied. PASS.
- **Register.** The clause and both skill edits avoid the scissors frame, name the owner impersonally
  ("the owner, 2026-07-17, reading the promoter's inter-agent design doc" — no personal name, per INV-120),
  and carry no significance-inflation. PASS.
- **Red-first.** docs/prover/red-proof-2026-07-18-row379.txt: 7 tests red against the pre-delta tree
  (stashed), 7 green after. PASS.

## Findings

None. Zero must-fix.
