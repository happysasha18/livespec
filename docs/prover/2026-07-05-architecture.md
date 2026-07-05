# Prover pass — ARCHITECTURE.md v0.1, architecture lens (2026-07-05, ~13:45)

**Scope:** the new `ARCHITECTURE.md` (row 50 bring-up) against SPEC v0.7. Lens: every spec fact has an
owning node · no node stands without spec backing · every seam names what crosses it and who owns the
format. **Previous record check:** `2026-07-05-lost-layers.md` — all 10 findings folded same session,
no unfolded rows carried over. **Whole-spec freshness:** SPEC.md entered this pass byte-identical to the
state proven green this morning; the pass itself then produced two stale-claim folds inside it (F7 below,
plus the version bump to v0.7.1) — folds produced by the gate's own pass ship with the same record and do
not re-trigger the gate (M-6). The ownership walk below touched every one of the spec's 69 anchors, so
this record serves as the push-gate re-check for the pushed state.

**Mechanical walk (command run, output pasted):** anchor-ownership check over the Formal index vs the
Nodes table — `index: 69 | owned: 69, MISSING: [], DUPES: [], EXTRA: []`. Two earlier hits (A-6/E-7
missing, T-1..T-6 duplicated) were checker artifacts fixed by rewording communicator's owns-cell so no
range token hides in a parenthetical; re-run clean. The walk is mechanized in
`tests/test_traceability.py` so it re-runs at every commit, not once.

## Findings

| # | Severity | Finding | Status |
|---|---|---|---|
| F1 | must-fix | SPEC S-0 states every [target] machine is owned by a ROADMAP row — true for guardrails (row 3), registry (row 3 scope), CI mirror (row 14), self-enforcement (row 3), but FALSE for the snapshot machinery (E-7/A-6) and the model router (ACT-3): neither had a queue row. The class was swept across all six targets, not just the reported two. | **folded** — rows 55 (snapshot) + 56 (router) added; ARCHITECTURE snapshot node cites row 55 |
| F2 | should-clarify | `install.sh` is real and shipped but no SPEC sentence names an installer; the attach node carries it via A-7's attach-record clause. A host reading the spec cannot learn how skills arrive. | **queued** — row 57 (spec sentence + anchor at next spec touch) |
| F3 | should-clarify | The decision page is communicator law (rule 10) but has no spec anchor; its backing today is the batched-questions clause inside the wish walk. Same class as F2: a live mechanism without a spec sentence. | **queued** — row 57 (one row, both mechanisms) |
| F4 | note | product-prover owns a single anchor (M-6); the prove transitions themselves live inside E-14/M-1 clauses owned by build-pipeline. Accepted: one-owner discipline holds, the node's backing is real, and splitting E-14 would create two owners for one fact. | **recorded** — noted in the node table's design |
| F5 | note | The index row `T-1..T-7` is deliberately split across two nodes (walk → build-pipeline, report step T-7 → communicator). Both sides are named in ARCHITECTURE and must both carry matrix rows. | **recorded** — matrix covers both blocks |
| F6 | note | Test-level vocabulary adapted for a text-only product: live-spec ships no browser surface, so no fact requires ≥ browser-computed; the "rendered level" equivalent is a string assertion against the SHIPPED file (never a source fragment). This is a recorded interpretation, stated in the matrix header and surfaced in the session report — not a silent call. | **recorded** — matrix header states it |
| F7 | must-fix | SPEC's D-4 and D-5 entries still read "a worked-examples decision page is out" — but both pages came back DECIDED 2026-07-05 (rows 42/43 → execution rows 51–54). The spec's stated truth lagged the queue's: a reader would think two decisions still pend that Alexander already made. | **folded** — both entries rewritten to their decided state (SPEC v0.7.1), index one-liners updated; open ⟨DECIDE⟩ markers now exactly D-1..D-3 |
| F8 | must-fix | SPEC M-3 promises "the queue and this spec carry dated versions" — the spec header does, ROADMAP.md's header carried no date at all. | **folded** — ROADMAP header now carries a dated version line, updated at every edit |

## Verdict

GREEN for matrix derivation: the must-fix folded in-session, the two should-clarifys are queued rows
with owners, the notes are recorded where they bind. Open ⟨DECIDE⟩ count unchanged: D-1, D-2, D-3 remain
open (D-4/D-5 closed as directions 2026-07-05); none of them is touched by this landing — D-3 will be
resolved by row 55, D-2 by row 56.
