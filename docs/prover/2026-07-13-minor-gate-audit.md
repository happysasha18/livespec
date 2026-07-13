# MINOR-gate preventive audit — FULL pass, 2026-07-13

**Prover skill version this pass ran under:** product-prover **1.0.10 — the installed copy** (`~/.claude/skills/product-prover/SKILL.md`), which predates the INV-138 edge-completeness lens and the INV-140 KIND block. The repo copy (`skills/product-prover/SKILL.md`) carries both additions under the **same version string 1.0.10** — that duplication is itself finding D4 below. The pass read the repo copies of every skill as primary sources and applied the INV-140 finding-kind format the spec under review mandates.

**Documents proven:** `PRODUCT_SPEC.md` (header v1.1.9 — stale, see D4; tree state v1.1.25, commit `e4b1529`) — FULL mode, whole document; `ARCHITECTURE.md` (last reconciled 2026-07-12) — architecture lens, all six checks. Special scope: the four new laws INV-137, INV-138, INV-139, INV-140, each read against the whole existing method.

**Suite at audit time:** 632 passed, 0 failed, 46.5 s (within the ≤ 60 s budget). Matrix rows M-279..M-282 exist for all four laws, each red-proven against the pre-delta tree. A dated prover record exists per landing (gap0–gap3).

## Opening assessment

The four laws are well-chosen, orthogonal to each other, and each carries a matrix row, a dated record, and its born-of incident. INV-138 and INV-140 are cleanly composed: the family prose (spec ↔ prover lens ↔ spec-author facet) is consistent and cross-cited, and the repo prover already practices the kind labelling. What blocks the bump is not the laws' substance but their seams: INV-137 openly contradicts the standing brief law INV-53; INV-140 states an unconditional blocks-rule that re-arms the exact over-sharpening INV-114 was written to correct; the architecture assigns INV-136/139 to a node whose artifact carries no trace of them; and the whole delta shipped under stale version strings (four skills and the spec header unchanged, installed copies unsynced), defeating the freshness machinery the record-version line depends on. Five defects, all cheap folds — a sentence or two each plus a version sweep. Needs one folding iteration, then ready.

## Findings

| id | finding | severity | kind | folded-or-queued |
|---|---|---|---|---|
| D1 | INV-137 / base rule 25 ("the lead never reads a file to brief them") directly contradicts INV-53 ("the brief-writer reads in full every file the work will modify"); neither text cites the other, so a lead writing a brief that edits files cannot obey both | must-fix | defect | open — for the bump session |
| D2 | INV-140's unconditional "a defect blocks / the push gate folds every defect / kind and severity never disagree on whether a finding blocks" contradicts INV-114's delta-scoped merge gate, where a pre-existing must-fix routes to a queue row and never blocks; the same prover skill file carries both rules unreconciled | must-fix | defect | open — for the bump session |
| D3 | ARCHITECTURE.md assigns INV-136 and INV-139 to base-rulebook, but `skills/live-spec-base/SKILL.md` carries no design-principles or legibility text (25 rules, none of them these) and no pin exists or can exist — ownership without backing | must-fix | defect | open — for the bump session |
| D4 | Version homes did not move with the delta: rows 303/304/305 changed product-prover, communicator, spec-author, build-pipeline with no version bump; the spec header still reads v1.1.9, 2026-07-12; all five installed skill copies differ from the repo — M-7 exact-string freshness, A-7's re-read trigger, E-23's old→new report, and the prover-record version line are all blind to the change | must-fix | defect | open — for the bump session |
| D5 | INV-137 names "the chat-law hook's routing-line reminder" a home, and spec line 160 describes the hook as citing base rule 25 / INV-137 — but `scripts/chat-law-hook.sh` cites only "base rule 5 + SPEC INV-69" and carries no dispatch-reads sentence; a named home does not carry its law | must-fix | defect | open — for the bump session |
| R1 | The INV-139 spec clause never states the pre-show lint's verdict semantics; communicator rule 5 says BLOCK, the sibling INV-83 states its block in the spec itself — the spec alone cannot answer whether faint text stands the showing down | should-clarify | recommendation | queued |
| R2 | INV-138's async-slot arm (pending/arrived/failed) overlaps T-13's "empty, error, and loading states" facet with no cross-cite; one sentence naming the per-slot faces as that facet's sharpening keeps one-home clean | worth-considering | recommendation | queued |
| R3 | The product-prover node's "also carries (wiring)" note lists entry-symmetry / declared-laws / norm lenses but none of the newer wired lenses (paired-transition, scenario-edges, interactive-overlap, edge-completeness); update the wiring note once at the bump | worth-considering | recommendation | queued |
| R4 | The base package-defaults table has no `project.design-principles` row (nor `project.layers` / `project.proofs`) while `project.kind` has one — the onboarding card cannot show the setting's rule until a host line exists; add the rows or record host-profile-only as the decided home | worth-considering | recommendation | queued |
| R5 | INV-140 / the prover's KIND block says "say which for every finding", but Phase 3.5's tag format is `acknowledged · label` with no kind; state whether acknowledged gaps take a kind or are exempt by name | should-clarify | recommendation | queued |

## The defects, walked

D1 — The lead cannot both write and not read the brief's files.

> "the lead never reads a file to brief them (rule 5, SPEC INV-69)" — base rule 25, `skills/live-spec-base/SKILL.md:246`; vs "Before writing a brief that edits existing files, the brief-writer reads in full every file the work will modify." — spec, "A brief is born from read files" [INV-53]

A lead following INV-137 at the next delegation writes a brief for an eight-file edit either from memory (breaking INV-53 — "the senior's guess dressed up as fact") or after full reads (breaking base rule 25); a worker or a later audit can call either choice a rule break. Fix: one clause in the INV-137 spec clause and base rule 25 naming the composition — the INV-53 full read is dispatched to the reader worker whose distillation returns the three per-file lines (current state · what changes · what must survive) with the lead verifying the cited anchors, or the brief-drafting read is expressly classed a decide-read that stays with the lead; the author picks, the seam must be written, and both laws cross-cite. `must-fix · direct-contradiction (consistency)`

D2 — INV-140's absolute re-arms the over-sharpening INV-114 corrected.

> "the push gate folds every defect … the kind and the severity never disagree on whether the finding blocks" — spec, the INV-140 clause; vs "Pre-existing findings equal on both sides route to queue rows in the same landing and never block; the merge is not held on debts it did not create." — spec, the merge-gate clause [INV-114]

At the next restructure-merge landing, a session holding INV-140's absolute parks the merge on the old side's pre-existing must-fix findings — the exact failure the owner corrected live on 2026-07-12, which INV-114's born-of records. Both rules sit unreconciled in the spec and in one prover skill file (KIND block at repo line 108 vs merge-gate paragraph at line 175). Fix: one sentence in the INV-140 clause, its index row, and the prover KIND block — "at a delta-scoped gate [INV-114] a pre-existing defect routes to a queue row by that law; the kind names what a finding asks wherever it is in scope." `must-fix · direct-contradiction (consistency)`

D3 — Two facts owned by a node that carries nothing of them.

> "base-rulebook … INV-135, INV-136, INV-139" — ARCHITECTURE.md, Nodes table, line 43

INV-135 is carried (base rule 24); INV-136 and INV-139 are not — a grep of the base skill for design principles, legibility, contrast, or either anchor returns nothing, and the node's pin column has no pin for them. The spec's own homes lists for both laws name no base-rulebook home either. A maintainer resolving "where does the design-principles law live" from the architecture lands in a file that does not state it — a wrong-with-confidence assignment, the class the doc itself calls worse than none. Fix: either (a) add the design-principles rule to the base rulebook in rule 24's pattern and pin it — my preference, it matches INV-135's precedent — or (b) reassign ownership to the carrying nodes (spec-author / build-pipeline / communicator per each law's homes) and update the row; either way the changed row rides an architecture-lens re-prove. `must-fix · boundary-issue (composition)`

D4 — The delta shipped under stale version strings, and the machine still runs the old skills.

> "The freshness check [A-7] compares version against version, exact strings" — spec, "Versions have named homes" [M-7]

Instances of one class: product-prover changed twice (rows 303, 305 — two new lenses) at 1.0.10 unchanged since row 300; communicator changed (row 304, the legibility BLOCK step) at 1.0.9 unchanged since row 280; spec-author changed (row 303, the edge facet) at 1.0.7; build-pipeline changed (rows 301/304) at 1.0.23; the spec header still reads "v1.1.9, 2026-07-12" seven spec-changing landings later. All five skill files differ from their installed copies, so every other session on this machine still runs the pre-INV-137/138/139/140 skills. A done-claim or prover record naming "prover 1.0.10" cannot tell the two lens sets apart — this very audit ran under the old 1.0.10 — which voids the record-opens-with-version rule's purpose ("a prover that grew a lens re-arms the full pass" is read from exactly that line). Fix, before the bump: bump product-prover → 1.0.11, communicator → 1.0.10, spec-author → 1.0.8, build-pipeline → 1.0.24; refresh the spec header's version and date; run `scripts/sync-skills.sh`; confirm every working skill's base pin reads v1.0.10. `must-fix · unenforceable-promise (discharge)`

D5 — A named home of INV-137 does not carry the law.

> "homes — base rule 25 + this clause + the delegation accounting [INV-103] + the chat-law hook's routing-line reminder" — spec, Formal index, INV-137; the shipped hook: "Homes: base rule 5 + the routing rule (SPEC INV-69)." — `scripts/chat-law-hook.sh:10`

The hook's routing line carries the INV-69 half (workers locate their own anchors) but nothing of the dispatch-discovery-reads duty, and cites neither base rule 25 nor INV-137 — while spec line 160 describes the hook as carrying exactly that. The law's whole point is a live channel at the decision moment [INV-108]; the moment a lead is about to read-to-discover, the reminder it gets says nothing about it. Fix: extend the hook's routing echo by one clause (reads to understand or design are dispatched to a reader worker, the lead reads the distillation — base rule 25, SPEC INV-137) — or drop the hook from INV-137's homes and correct spec line 160 to match the artifact. The first is right: the spec already promises it. `must-fix · unbacked-surface (discharge)`

## Family coherence (the audit's third charge)

The composition-lens family — INV-72 (root), INV-125 (space), INV-126 (time), INV-136 (depth), INV-138 (range and lifecycle) — is coherent: each member names the family the same way in the spec, the prover lens text, and its index row; scopes are disjoint (a policy across siblings / a pair's two directions / two layers' controls / a gate's edges); each cites INV-72 as the shared blank-answer class. INV-138 is a proper sibling. Ownership scatters across three nodes (125 → product-prover, 126/127/138 → spec-author, 136/139 → base-rulebook), which D3 partly repairs and R3 tidies.

The design-principles family — INV-136 and INV-139 under the ARCHITECTURE per-kind table — is coherent: both take the same ship-the-law-and-the-script, leave-the-browser-assertion-to-the-adopting-suite split, both run at the verify feel pass, and INV-139 adds the pre-show arm beside the register lint without duplicating it (register = the words are the product's own; legibility = the words can be read — two guards, one instant, stated once). The script's floors match the spec's numbers exactly (4.5:1, 3:1 at ≥ 24 px or ≥ 18.66 px bold, ≥ 12 px), its static-floor boundary is honestly documented, and the suite holds red and green fixtures for it.

The seat-discipline family — INV-69 (output routing), INV-103 (reporting), INV-137 (input hygiene) — is cleanly framed as one seat's discipline from three sides, and INV-137's ownership by build-pipeline matches its siblings. Its one unwritten seam is D1.

INV-140 against the severity axis: the mapping defect = must-fix, recommendation = should-clarify/worth-considering is exact and the repo prover applies it verbatim; the record column and Phase 5 partition are present. Its one unnamed edge is D2; its one loose end is R5.

## What was checked and found sound

- Every spec anchor including the four new ones is owned by exactly one architecture node; no double ownership found (INV-139 appears twice in ARCHITECTURE.md — owns column plus the design-principles table row — one ownership, one scaffold mention).
- All four laws carry matrix rows (M-279..M-282) at stated levels with red-proven notes, and each landing left a dated prover record (gap0–gap3).
- The suite is green whole (632/632, 46.5 s) inside the wall-time budget; the feature-coverage table, seams table, runtime view, placement view, and quality budgets stand as before — no new node, no new seam, so no structural re-prove was owed by the four landings themselves.
- No new contradiction found between INV-137 and INV-69/103 (the three compose as stated), between INV-137 and verify-by-deed / M-6 / INV-116 (gate reads are decide-reads and stay with the lead by the clause's own carve-out), between INV-139 and INV-83 (disjoint guards, one gate), or between INV-138 and INV-50/126/127 (disjoint scopes).

## Verdict

Not sound for the MINOR bump as the tree stands: five defects (D1–D5), each a one-or-two-sentence fold plus a mechanical version sweep. Fold them, re-run the suite, and the pack is ready — the four laws themselves are sound and well-integrated.

---

## Orchestrator resolution (2026-07-13 ~22:25, folded before the MINOR bump)

All five defects FOLDED; the suite is green whole (632 passed) after the folds.

- **D1 — FOLDED.** Rule 25 and INV-137 now compose with INV-53 rather than contradicting it: the phrase changed to "the lead never reads a file merely to hand a worker its anchors", and both the base rule and the INV-137 clause state that the brief's own read of the files it will change [INV-53] is dispatched to the reader whose distillation returns the per-file lines, or is a bounded decide-read for a small edit. INV-53's clause cross-cites INV-137 back.
- **D2 — FOLDED.** INV-140 (clause + index + prover KIND block) now names the delta-scoped exception: at a delta-scoped gate [INV-114] a pre-existing defect queues by that law and never blocks — the fold-every-defect rule is the ordinary push gate's, not an override of the delta-scoped one. This re-aligns with the 2026-07-12 correction the owner made.
- **D3 — FOLDED.** A new base rule 26 states that a project kind declares design principles the verify pass runs (SPEC INV-136, INV-139), giving base-rulebook the text home its ownership of those two invariants requires; ARCHITECTURE's base-rulebook pin now points at rule 26 (`skills/live-spec-base/SKILL.md:262`).
- **D4 — FOLDED.** Version sweep: product-prover 1.0.10→1.1.0, communicator 1.0.9→1.0.10, spec-author 1.0.7→1.0.8, build-pipeline 1.0.23→1.0.24, base-rulebook 1.0.10→1.0.11 (the "(v1.0.x)" pointers swept across all seven skills), the spec header "v1.1.9"→"v1.2.0", VERSION/plugin →1.2.0; the installed copies are refreshed by `install.sh` at the deploy step.
- **D5 — FOLDED.** `scripts/chat-law-hook.sh`'s routing echo gained the dispatch-reads clause and cites base rule 25 / SPEC INV-137, so the hook now carries the law its homes list claims.
- **R1 — FOLDED** (INV-139 clause now states the pre-show red BLOCKS, sibling to INV-83's block). **R5 — FOLDED** (Phase 3.5 acknowledged gaps keep their tag and carry no kind). **R2, R3, R4 — QUEUED** as ROADMAP rows for a later pass (INV-138↔T-13 cross-cite hygiene, the prover node's wiring-note completeness, a `project.design-principles` defaults-table row).
