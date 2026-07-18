# Prover record — rows 402 + 409 (INV-228, INV-229), 2026-07-18

Two touchpoint-frame instances reusing landed machines (INV-205 frame, INV-206 board gate,
publish node). Mode: CROSS-LINK — each new law's seams checked against the named existing
surfaces it consumes, plus an architecture-lens pass over the two owns-list edits. Opened by
checking the previous record's unfolded rows: the most recent records
(`2026-07-18-rows397-383-*`, `2026-07-18-rows386-412-414-*`) carry no unfolded must-fix rows.

## Row 402 — INV-228, a release note may offer next-step choices

The release-note shape in the publish skill gains an OPTIONAL offers section (choices the reader
may take), and the publish walk records the offer-or-none decision. Checker
`guardrails/check-release-note.py` reds a record leaving the decision unrecorded, passes one that
offers or records "none"; report-only, rides the suite not the push chain. Consumes the
`release-note` touchpoint classification already declared in `guardrails/touchpoints.json`
(asynchronous, person-opened, human audience, no answer needed) — the frame is not re-opened.

| # | Finding | Folded / rejected |
|---|---|---|
| 1 | Cross-section: does the new offers section collide with an existing release-note promise? The only prior release-note surface is the mirror release-history section (INV-181), which harvests version/date/story from git history; the offers section is a distinct, optional region the walk records, no seam shared. | Folded — no collision; the two regions are disjoint and the matrix M-339/M-340 fences stand untouched. |
| 2 | Ownership: INV-228 owned by the publish node; the checker artifact pinned in the publish node's pin column. Traceability requires exactly one owning node — verified the anchor appears only in the publish node's third column, cross-refs (INV-205/INV-83/INV-222) kept out of the anchor column and moved to prose/pins. | Folded — `test_architecture_owns_every_anchor_once` green; no dupe, no stale. |
| 3 | Is the checker correctly OFF the push chain? The release note is a process artifact the walk records at runtime; no committed release-note file exists for a push gate to scan (the far-tier sibling, INV-83). `test_checker_not_wired_into_pre_push` asserts it. | Folded — rides the suite; the spec, matrix, and architecture all state the report-only ride. |
| 4 | The kind-split the spec records: keyed by audience (agent/human) and by need of an answer. Does it contradict INV-205's kind axis (synchronous/asynchronous)? No — audience/answer-need is the ORTHOGONAL keying INV-228 introduces to answer the owner's message-types aside; the synchronous/asynchronous kind and the opened-by axis stay INV-205's, unchanged. | Folded — additive, no re-scope of INV-205. |

## Row 409 — INV-229, a parked question carries a default

An arm on the waiting-list board gate `guardrails/check-board.py` (existing gate q): a board item
marked a parked question (`[[park]]`) carrying no `default:` note reds. Consumes the
`parked-feedback-question` classification (asynchronous, person-opened). No new gate letter.

| # | Finding | Folded / rejected |
|---|---|---|
| 1 | Regression fence: the arm scans shown+list region lines for `[[park]]`. Does it change the existing three arms' behaviour (demotion / over-cap / closing-report)? The arm is additive — a separate loop, no shared state with arms (a)/(b)/(c); the real WAITING.md and every existing board fixture carry no `[[park]]` item, so they pass unchanged. | Folded — `test_gate_passes_the_real_board`, `test_gate_passes_a_genuine_board` still green. |
| 2 | Ownership: INV-229 owned by the guardrails node (alongside INV-206, same machine). No new pin needed (extends check-board.py). The new anchor's parenthetical carries no INV cross-ref token, so no dupe/stale. | Folded — traceability green. |
| 3 | Boundary against the decision law (INV-152): does the parked-question default overlap what an agent may not settle without the human? The spec states the distinction explicitly — INV-152 governs what an agent may NOT decide without him; INV-229 governs a question whose value is his input yet the work may proceed on a recommendation. Two different lanes. | Folded — the clause names the distinction; no overlap. |
| 4 | Never-stall / nothing-lost: an unanswered parked question keeps standing (INV-206), its default holding, the record noting it stood unreviewed. Consistent with the board's never-auto-expire law. | Folded — no conflict with INV-206. |

## Open decisions touched

None. Both rows consume classifications already declared in the INV-205 manifest (rows 402, 409);
the frame is not re-opened. No `⟨DECIDE⟩` under the surfaces under change.

## Verdict

0 must-fix. Both laws red-proven against the pre-delta tree (`docs/prover/red-proof-2026-07-18-rows402-409.txt`),
then green. Full suite green after re-freeze of the local `.spec-freeze/` baselines (gate k) and a
redundancy reword (INV-229's closing sentence no longer contained by INV-222's line 605).
