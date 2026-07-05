# Prover pass — 2026-07-05, the lost layers (row 41, SPEC v0.7)

Mode: FULL (whole spec, all phases) — this is both the push-gate re-check [M-6] and the MINOR gate for
0.1.1 → 0.2.0 (3-pass audit, prover leg). Doc under review: SPEC.md v0.7, with the new section "From the
spec to the tests" [E-14, E-15, INV-15] and the reworded open decisions [D-4, D-5].

Previous record (2026-07-05-base-skill.md) opened first, per the method:
- F4 (personal profile outside git) → queue row 38, still queued — not lost, not due this gate.
- F5 ("base skill" concept vs folder name, re-check at D-4's close) — the NAME half of D-4 closed with
  row 40; E-12 now pins the folder inline (`live-spec-base`). Resolved for the name half; the structure
  half rides row 42. No other unfolded rows.

Evidence base (commands run this pass, not prose trusted): full read of SPEC.md v0.7 + ROADMAP rows 1–49 +
ARCHITECTURE.template.md + TEST_MATRIX.template.md + build-pipeline SKILL.md 0.2.0 + ADOPT.md + the
product-prover SKILL.md triage rules; `ls` of templates/, docs/prover/, `.live-spec/`,
`~/.claude/live-spec/`; `grep -ri livespec` over the repo; `git log`/`status`/`remote`; `grep version:`
over all five SKILL.md files.

Whole-doc checks that came back CLEAN (stated so they are re-checkable):
- **Formal index ↔ prose: zero drift.** E-14/E-15/INV-15 present with one-liners matching their section;
  D-4's line carries the name-half-closed note matching the prose; D-5 matches; every prose anchor has an
  index row and vice versa.
- **Rename aftermath: clean.** Old-name grep hits only dated history (JOURNAL, prover records, decision
  JSONs, ROADMAP row 27's quote, the rename checkpoint) plus NEXT_STEPS' accurate live-state line about
  the pending GitHub rename. Machine paths on disk match the spec's names: `.live-spec/` (host),
  `~/.claude/live-spec/profile.md` (personal, old dir gone), `skills/live-spec-base/`. Remote + clone dir
  still old-name by design (row 40: renamed at the reviewed push).
- **Base-skill pins current.** All four working skills pin `live-spec-base (v0.1.2)`; base frontmatter is
  0.1.2 — the E-12 sweep rule held through the 46-landing.
- **B-1 template list matches disk** — the six named templates are exactly the six files in `templates/`,
  ARCHITECTURE.template.md included.
- **Inbox empty** (README only) — the M-1 unharvested-wish listing has nothing to list.

What is working well: the new section states the WHY of each layer (an implicit layer is a lost layer),
the re-prove-on-change rule reads identically in E-14 and the template header (one voice, no drift), and
reconciliation now has a natural home inside the architecture step (pins from commands run) instead of a
free-floating step — that is a real simplification, not a loss.

## Findings

| # | Finding | Severity | Location | Resolution |
|---|---|---|---|---|
| F1 | INV-15 is unsatisfiable today for every EXISTING host, including live-spec itself. The invariant binds every landing ("no wish lands whose facts lack an owning architecture node and a matrix row at the right level"), unconditionally and effective immediately — but live-spec's own repo has no ARCHITECTURE.md and no TEST_MATRIX.md (ls of repo root, this pass), and no ROADMAP row owns creating them. S-0's own rule says every target is owned by a row; this one is owned by nobody, so the very next landing (row 42 or any other) either violates INV-15 or stalls. Concretely: the senior starts row 42, reaches the matrix step, has no node to cite, and must either freelance an architecture doc mid-wish (unplanned large work) or land in violation of the pack's newest invariant — in its own flagship repo. Fix: open a queue row "live-spec's own ARCHITECTURE.md + derived matrix" AND add one bring-up sentence to INV-15's paragraph — a host without the two docs yet creates them at its first large/surface landing after this spec version, smaller wishes noting the debt in their row (missing-scenario · state-space) | must-fix | "From the spec to the tests", INV-15 + S-0 + M-4 | |
| F2 | Adoption never produces the architecture layer, contradicting the derivation rule it hands the host. A-3 re-engineers docs → spec sections, tests → matrix rows, roadmap → queue rows — no architecture doc anywhere in the A-sequence; ADOPT.md Phase 5 says "Build TEST_MATRIX.md from the proven spec: one row per invariant / transition / cross-section / surface" (straight from spec, flat shape), then Phase 6 line 142 puts the host on the new order (spec → prove → architecture → prove architecture → matrix → …) that its own Phase 5 just bypassed. Concretely: the next adopted host exits adoption with a flat, spec-derived matrix and no ARCHITECTURE.md, and its first wish hits the F1 wall on day one. Fix: add the architecture step to A-3 (between re-engineer-spec and derive-matrix: nodes from the real codebase, pins ARE the reconcile of unverified claims — it slots exactly where A-3 already demands file:line reconciliation) and rewrite ADOPT.md Phase 5 to derive through it, node × fact (undefined-path · transitions) | must-fix | Adoption step 3 [A-3]; evidence adopt/ADOPT.md:120–128, :142 | |
| F3 | T-9's bug lane has no path when the bug's fact has no owning node. E-14: "a bug or small wish cites the existing node it lands in" — cites, never creates; INV-15 forbids landing without one. A bug can surface a fact the architecture never assigned (a seam behaviour both nodes disclaim, or any bug during the F1/F2 bring-up window). Concretely: a critical bug preempts the lane [T-9], the fixer finds no node to cite, and the rule says the CRITICAL fix cannot land — the priority rule and the layer rule collide exactly when speed matters most. Fix: one sentence in E-14 — a bug whose fact has no owning node lands citing the nearest node and leaves a one-line architecture debt note (or assigns the fact to an existing node in the same change); never blocks on a full architecture pass (undefined-path · transitions) | should-clarify | "When a bug cuts the line" [T-9] × E-14/INV-15 | |
| F4 | INV-15 has no enforcement home, even among the target machines. E-6's guardrails check completeness · tests-present · behaviour-traces-to-spec · declared-scope diff; build-pipeline's conflicts check adds "a spec invariant with no matrix row" — none checks that a fact has an owning node or that the coverage validation was walked. Concretely: once guardrails land (row 3), an agent can skip the architecture layer entirely and every mechanical check still shows green — the newest invariant is the only one with no teeth planned. Fix: extend row 3's scope (it already grew once, for the fence + push gate): the conflicts check also fails on a spec anchor absent from every node's "owns" column and on an unchecked coverage-validation box (unenforceable-promise · discharge) | should-clarify | "Machines" [E-6] × INV-15; ROADMAP row 3 scope | |
| F5 | The coverage-validation checklist lives in two places and has already diverged. E-15 enumerates four items; TEST_MATRIX.template.md's checklist has five — the spec's copy omits "no row cites a spec anchor or node that no longer exists (stale rows RETIRED)". Concretely: a derivation walked from the spec's sentence alone passes with stale rows standing — the exact drift class INV-13 kills for skills, reproduced between spec and template on day one of the layer's life. Fix: make the template's checklist the normative home; E-15 keeps the first two items as illustration and points at the template for the walked list ("closes with the template's coverage validation, walked") (one-home-per-fact · consistency) | should-clarify | E-15 checklist sentence vs templates/TEST_MATRIX.template.md:43–54 | |
| F6 | build-pipeline's guardrails paragraph still uses the PRE-insert step numbers. It says "Verify-by-deed (step 7) and push (step 8) both run the guardrails first" — after the two inserted steps, verify is 8 and commit/push is 9 (the refactor bullet's "enter at step 8" WAS swept; this paragraph was missed). Concretely: an agent following the guardrails paragraph by number wires the pre-push run to the Code step. The words carry the meaning today, but a stale number in the pipeline's own spine is the drift the pack exists to prevent. Fix: renumber that one line (and grep the skill for any remaining "step N" against the current list) (internal-conflict · consistency) | should-clarify | skills/build-pipeline/SKILL.md:126 | |
| F7 | B-1 says "the pipeline runs from step 0" — build-pipeline has steps 1–9; no step 0 exists. A bootstrap reader looking for step 0 finds nothing. Fix: "from step 1" or "from the top of the pipeline" (reference integrity) | note | Bootstrap [B-1] | |
| F8 | E-5 says the matrix is "one row per fact"; E-15 says "every fact gets at least one row" — the first reading (exactly one) forbids what the second allows (a fact tested at two levels, e.g. string + browser). Fix: E-5 → "≥ one row per fact" (internal-conflict · consistency) | note | "Machines" [E-5] vs E-15 | |
| F9 | Already-adopted hosts hold matrices in the OLD shape with no stated migration rule. tlvphoto's TEST_MATRIX.md (row 4) is flat, spec-derived; E-15 now defines the shape as node × fact, derived through architecture. The rename got MIGRATION.md; this reshape got nothing. Fix: one sentence (in E-15 or the migration note pattern): an old-shape matrix is regrouped under nodes at the host's first architecture doc (F1's bring-up landing), rows preserved, not re-derived from scratch (persistence-and-versions · state-space) | note | E-15; host tlvphoto's installed matrix | |
| F10 | The template promises the coverage validation is "re-walked at milestones", but M-1's milestone list doesn't name it (nor an architecture re-prove of a doc that changed since the last milestone). "Matrix audit" plausibly covers the first — plausibly is the problem: a duty stated only in a template a host may have copied months ago is a duty the milestone runner never sees. Fix: two words in M-1 — "matrix audit (coverage validation re-walked)" — making the spec the owner and the template the echo (one-home-per-fact · consistency) | note | "Rhythm" [M-1] vs templates/TEST_MATRIX.template.md:43 | |

## Coverage notes (FULL-pass residue)

- CRUD / authorization tables: N/A for this doc — the pack is a single-human method package; the queue's
  row lifecycle (never deleted, named exits) is the only CRUD-like surface and is fully stated [INV-1, T-8].
- Acknowledged gaps: D-1, D-2, D-3 unchanged and correctly parked with revisit triggers; D-4 structure
  half → row 42; D-5 → row 43. No acknowledged gap touches the new layer except D-4 (where the base skill
  lives does not change who owns spec facts — checked, no coupling).
- Lenses that fired nothing real: concurrency on the two new docs (covered by the existing fence
  [INV-11]); bounds on node counts (template scales by table rows); surface authority (the Formal index is
  the only competing registry and it is clean, see the index check above).

## Verdict

Not green yet for the push or the MINOR: **F1 and F2 are must-fix** — the new layer is well stated for
FUTURE work but has no bring-up path for the hosts that already exist, the pack's own repo first among
them. Both fold cheaply (one queue row + one bring-up sentence; one A-3 step + ADOPT.md Phase 5 rewrite).
Per M-6, folds produced by this gate's own pass ship with this same record and do not re-trigger the gate.
F3–F6 should be folded or become queue rows this session; F7–F10 are one-line sweeps safe to batch with
the folds.

## Resolutions (folded 2026-07-05, 12:15–13:05, same session — per M-6 they ship with this record)

| # | Outcome |
|---|---|
| F1 | FOLDED: bring-up sentence in INV-15's paragraph (binds from the landing that creates the docs, never retroactively) + queue row 50 (live-spec's own ARCHITECTURE.md + matrix — the next landing) |
| F2 | FOLDED: A-3 gains the architecture step (inventory pins seed ARCHITECTURE.md; matrix rows land under nodes) + ADOPT.md Phase 5 rewritten "Architecture, then the test matrix" with its own done-when |
| F3 | FOLDED: E-14 — a bug whose fact has no owner ASSIGNS it to the fitting existing node (recorded, no re-prove for an assignment alone); no fix can be the thing the rules forbid to land |
| F4 | FOLDED as queue-row scope: row 3 (guardrails) now includes node-ownership + walked-coverage checks in the conflicts guardrail |
| F5 | FOLDED: the template's checklist is the normative home; E-15 points at it and its list now carries the fifth (no-stale-refs) item |
| F6 | FOLDED: build-pipeline guardrails paragraph renumbered (verify = step 8, commit/push = step 9); skill-wide grep for stale "step N" clean |
| F7 | FOLDED: B-1 now says "the pipeline runs from intake" (the README keeps its own Step 0 = Intake walk; no dangling number in the spec) |
| F8 | FOLDED: E-5 → "at least one row per fact" |
| F9 | FOLDED: MIGRATION.md gains the matrix-reshape note (old flat matrices regroup under nodes at the bring-up landing; rows preserved, never re-derived) |
| F10 | FOLDED: M-1's milestone list names the coverage validation re-walk explicitly (spec owns the duty, the template echoes) |

Verdict after folds: GREEN for the push gate and the 0.2.0 MINOR (matrix-audit leg of the 3-pass gate is
honestly N/A until row 50 creates the pack's own matrix — stated, not skipped silently).
