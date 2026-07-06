# Skill-creator walk — all six pack skills, 2026-07-06 (row 130, session 17)

The walk: three read-only analysis agents (two skills each) ran skill-creator's lens — frontmatter
correctness, description triggering quality (use + NOT-use), body structure and scanability, size vs
the ~500-line ideal, concrete examples, stale references, cold-reader clarity — over the REPO copies.
Findings judged and folded by the senior; raw agent evidence in the session's scratchpad checkpoints
(row130-agent-A/B/C.md). The senior's own mini cross-link on the M-1 delta this walk writes: the
re-walk clause joins an existing enumerated checklist (M-1) beside the evals item — the seam with
E-19 is named in the clause itself (evals test behaviour, this lens tests the craft of the file);
no new surface, no composition risk found.

## Sizes (all under the 500-line ideal — row 69's pressure stays eased)

live-spec-base 200 · spec-author 343 · product-prover 382 · build-pipeline 289 · communicator 249 ·
publish 95 (post-fold numbers).

## Findings and their fates

| # | Skill | Finding | Severity | Fate |
|---|---|---|---|---|
| 1 | spec-author | the product-prover link pointed at a second repo (`happysasha18/product-prover`) while the pack repo is the source — two homes for one skill | should | **FOLDED**: repointed to the pack repo's `skills/product-prover` (matches the templates' one-source law) |
| 2 | live-spec-base | description had no NOT-side (the exclusion lived only in the body) | should | **FOLDED**: description now ends with "NOT for sessions outside the pack's work, and never a place to write host- or person-specific values" |
| 3 | live-spec-base | description one ~110-word run-on | nit | **FOLDED** with #2: split at "stated ONCE" |
| 4 | spec-author | dense pack coinages vs the "stands standalone" header claim; suggested a glossary | nit | **REJECTED**: the header is pack-wide boilerplate (one home, INV-13) — softening it in one skill forks it; the coinages (doors, fences, facets) are each defined in the body section that owns them |
| 5 | build-pipeline | PLAYBOOK.md cited three times as if co-located; it lives in the private playbook repo — a fresh agent greps and finds nothing | should | **FOLDED**: all three mentions now say "the private playbook repo's PLAYBOOK.md" |
| 6 | build-pipeline | step-zero bullet ~18 lines of unbroken code-laden prose — scanability | should | **FOLDED via row 137** (landed 2026-07-06 s18, lane B of the first double-lane run: lead line + sub-points, every word kept, pins verbatim, suite green) |
| 7 | build-pipeline | no worked end-to-end example | nit | **REJECTED**: size pressure vs value — the work-kind and excuses tables already anchor concretely; may ride row 137 if its rewrite makes room |
| 8 | build-pipeline | emphatic caps against skill-creator's style guidance | nit | **REJECTED**: deliberate register — the reader is a model and the caps mark law-bearing words; the teeth are mechanical (guardrails), the caps are the pointer to them |
| 9 | product-prover | description lacked the NOT-tail (body-only) | nit | **FOLDED**: "NOT for code or diffs… never a substitute for tests" appended to the description |
| 10 | communicator | description carried self-referential tuning history and bare rule-number pointers; ~180 words | should | **FOLDED**: history clause dropped, rule numbers dropped, the done-claim and feature-map triggers named in reader terms; the row-68 fence held — the pinned NOT-side phrases kept verbatim (suite-checked) |
| 11 | communicator | rules 6/8/9/10/11 are single dense paragraphs — scanability | should | **FOLDED via row 137** (landed 2026-07-06 s18, with #6 — rules 6/8/9/10/11 reshaped, token-equality verified) |
| 12 | publish | no concrete ❌/✅ worked example | should | **FOLDED**: a before/after skill-README example added ahead of When-NOT |
| 13 | both (comm/publish) | body When-NOT duplicates description info | nit | **REJECTED**: deliberate redundancy — the body serves standalone use, the description serves the triggering classifier; recorded here as intentional |

## Verdicts

All six: frontmatter clean, references live (post-#1/#5), sizes under the ideal. Solid; the one
structural debt (dense-paragraph rules) is owned by row 137, not left floating.

## The standing law this walk installs

The milestone gate (SPEC M-1) now carries the re-walk item, and a skill newly joining the pack walks
skill-creator at birth. Matrix M-128, `test_m1_names_skill_creator_rewalk` — the clause and this
record are both machine-checked.
