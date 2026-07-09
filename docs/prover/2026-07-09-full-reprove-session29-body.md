# Prover record — FULL re-prove for the pre-push M-6 gate (2026-07-09)

**Mode:** FULL (whole-spec re-check). **Trigger:** the M-6 pre-push gate over the entire unpushed body
(origin/main..HEAD — sessions 27, 28, 29: de-Russification/translation, positive-opener pass, scissors-frame
removal, structure grouping into named trees, `SPEC.md`→`PRODUCT_SPEC.md` rename, session-29 readability
restructure of README + PRODUCT_SPEC, and the new gate/guardrail machinery).

**Documents proven:** PRODUCT_SPEC.md (v0.16.0) + ARCHITECTURE.md (v0.2).

**How this pass was run:** the prover read the whole spec, and three independent fresh-context reviewers ran
in parallel — a regression hunt (meaning damage from translation/restructure/rename), an adversarial formal
hole-hunt, and a cross-document consistency check. Findings below are the union, triaged.

## Regression verdict (the human's certainty question)

The restructure did **not** regress meaning. Evidence:

- **README + PRODUCT_SPEC readability restructure (session 29):** the ordered word-token sequence is
  byte-identical to the pre-restructure state (README 2243 tokens, PRODUCT_SPEC 29796 tokens); the only
  punctuation delta is added list markers plus seven commas removed exactly where one inline enumeration
  became a bulleted list; the Formal index (tables) is byte-identical. Meaning-preserving, mechanically.
- **Rename `SPEC.md`→`PRODUCT_SPEC.md`:** no dangling active reference remains; every surviving `SPEC.md`
  mention is dated history (ROADMAP/JOURNAL) or a generic prior-art reference.
- **Translation / regrouping (sessions 27–28):** carried green through the suite (traceability, prose gates,
  guardrails) and the fresh read; no broken or contradictory sentence found.

The pass DID surface three real defects sitting in the unpushed body (not introduced by the session-29
restructure) plus latent design questions. The defects are folded; the design questions are queued.

## Findings

| # | Finding | Severity | Disposition |
|---|---|---|---|
| F1 | Stray `</content>` tag leaked into the spec body at the end of the adoption section (would render as literal text). Entered at commit `91badd5` (session 28), absent from origin — never pushed. | must-fix | **FOLDED** — tag removed. |
| F2 | Stale skill counts inside the authority doc: "the pack's five skills" (§ work-kinds vocabulary) and "the pack's fifth working skill" (publish). Same class already fixed in `live-spec-base` this session (commit `8923969`); these two in-spec instances were missed. | must-fix | **FOLDED** — fragile ordinals removed (per the 2026-07-05-row98 precedent: don't re-count, drop the count). |
| F3 | ARCHITECTURE.md header frozen at "v0.1, 2026-07-06" while carrying four nodes added later; the Prover-record table omitted the four node-add re-proofs (all four record files exist). | should-clarify | **FOLDED** — header → v0.2/2026-07-09; the four rows + this pass added to the table. |
| F4 | ARCHITECTURE.md:33 comma-splice reads as if the guardrails node owns INV-67 (mechanically clean — traceability parses it to communicator; prose only misleading). | worth-considering | **QUEUED** — low severity; editing this ownership line risks the green `owns-every-anchor-once` check, so it goes through a proper row, not a hurried fix. |
| F5 | Deferred rows have no defined evaluation point: nothing re-scans a deferred row's revisit trigger, so a fired trigger can go unnoticed (soft dead-end; tension with INV-1). | must-fix (design) | **QUEUED** — pre-existing design hole, not a regression; ROADMAP row (add a deferred-trigger evaluation point, cleanest at the milestone gate M-1). |
| F6 | A feature parked by a bug resumes "in original order" with no analogue of INV-39's re-fence/re-prove against the changed truth — can integrate a delta proven against stale law. | must-fix (design) | **QUEUED** — pre-existing; ROADMAP row (T-9 resume re-fences like INV-39's later lane). |
| F7 | A critical bug arriving during a running milestone is an undefined transition (T-18 covers opening lanes mid-milestone, not bug preemption of a running one). | should-clarify (design) | **QUEUED** — ROADMAP row. |
| F8 | "Land or park first" for a milestone (T-18) reuses the bug-only "parked" state (T-9) without a defined milestone-quiesce transition/resume. | should-clarify (design) | **QUEUED** — ROADMAP row. |
| F9 | The concurrent lane-claim back-off (two sessions, one repo) names no tie-breaker for "later claimant" — mutual back-off / double-claim reachable on a genuine collision. | should-clarify (design) | **QUEUED** — ROADMAP row (define the total order the back-off reads). |
| F10 | The `tight`-rung batched-gate recovery on a batch-end red is unspecified (bisects the culprit but states no revert/re-apply path; HEAD sits red locally — never pushed, so bounded). | worth-considering (design) | **QUEUED** — ROADMAP row. |

## What was probed hardest and found sound

Harvest/inbox atomicity (one-commit harvest, interrupted-harvest-leaves-file, T-10); supersession-on-decline
transitivity (T-8); the wordless-drop route landing as a ledger line (INV-68); INV-70 vs. the never-bend
publishing gate (reconciled by the standing human grant); every cross-reference anchor resolves against the
Formal index; anchor ownership is exactly-once (the mechanical `test_architecture_owns_every_anchor_once`
passes); pipeline step names/order and skill-set names agree across spec, README, OVERVIEW, and the skills.

## Gate

Folds F1–F3 land in this session's commits. F4–F10 are queued as ROADMAP rows (design improvements and one
low-severity prose nit — none is a regression, none blocks the push). Suite green after the folds authorizes
the pre-push gate; the human's explicit "go" and a deployed==repo re-sync remain owed before any push.
