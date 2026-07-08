# SPEC re-style — traceability needle re-point log

When a section's prose is re-styled (clean-agent rewrite, linter-gated), a brittle traceability
needle keyed to an old exact phrase is re-pointed to an anchor plus a register-invariant domain
term that survives in the new prose and names the same law. Re-points narrow (a more specific
phrase for the same law), never weaken. One line per re-point.

| Date | Section | Test | Old needle | New needle | Why |
|------|---------|------|-----------|-----------|-----|
| 2026-07-08 | Asking what the product does | test_traceability.py::TestProblemLedger::test_feature_map_on_demand | `the whole map comes only when` | `the whole map only on request` | Clean-agent rewrite phrased the "map returned only when asked, never uninvited" law as "The ask returns the whole map only on request." New needle is a narrower phrase naming the same INV-38 law and present verbatim in the new prose. Anchor `[INV-38]` and `Asking what the product does` heading still gate the same law. |
| 2026-07-08 | Reuse before reinventing | test_traceability.py (INV-65 borrow-license) | `with the notice kept — never republish unlicensed text` | `Unlicensed text is never republished` | Old needle pinned the scissors construction itself. Removing the em-dash contrast split it into two statements; new needle is the prohibition sentence, register-invariant and narrower, present verbatim in new prose. Anchor `[INV-65]` still gates the same borrow-license law. |

## Phase 2 — whole-diff validation (2026-07-08 night pass, iteration 1)

A fresh reviewer read the full pre-restyle baseline (`ca78876`) → HEAD diff of SPEC.md. It reported 7 items;
5 were real and fixed in commit a9690c4: reinstated the "three standing questions, two answered elsewhere"
framing in the feature-map ask; dropped an added "otherwise the ask proceeds" clause; restored "what the
feature gives its person" (a rewrite had narrowed it to "value"); restored the "knob rather than a taste
call" contrast without a negation opener; fixed a dangling em-dash that made "never a silent retry" read as a
list item. Two minor notes (aloud→directly; wording) left as-is. Full-SPEC anchor multiset verified IDENTICAL
to the baseline. A confirming iteration 2 and full 0-errors convergence wait on the parked errors (preamble +
Formal index), which need Alexander's word.

## Stage 5 chunk 2 — economy ladder (2026-07-09)

Section "When money or time run short" converted through --gate (second person → named actor, caps
lowercased, 19 gate-errors → 0). Linter refined: CAPS_RE now captures hyphenated all-caps compounds whole
and CROSS-LINK/FEATURE-FIT/RE-ENTRY join the caps allowlist (defined mode names, not shout). Three needles
re-pointed by narrowing to the register-clean phrase in the new prose (test_traceability.py::test_economy_ladder):
`the economy rung is asked, or the standing default told` → `the pack asks the economy rung, or tells the standing default`;
`What NEVER bends, at any rung` → `What never bends at any rung`;
`a push still requires the full gate green at HEAD` → `a push still requires the full gate green at head`.

## Stage 5 chunk 3 — Naming and reporting (2026-07-09)

Section "Naming and reporting the work" driven to 0 gate-errors surgically (partly clean already): future-narration "will go by"/"will be called"→present; second person (agent) → named actor/passive on the preshow-lint, report-walk, and narration lines; inline caps IS/STEP/OPENS/OFFLINE WINDOW lowercased. Linter: IDENTITY/DIGEST/HEARTBEAT added to the caps allowlist (defined bold law-part labels of INV-35, kept caps). One needle re-pointed: `OFFLINE WINDOW` → `offline window` (test_traceability narration test).

## Stage 5 chunk 7 — Package repo + HEAD normalization (2026-07-09)

Section "The package repo" driven to 0 gate-errors (emphasis caps lowercased, one second-person removed). Linter: `HEAD` added to the caps allowlist (git ref, a technical term, not shout). Consequent fix: the economy-ladder needle re-pointed BACK from `green at head` to `green at HEAD` (SPEC + test), so the git term reads HEAD consistently.

## Stage 5 chunk 8 — Breakpoints/resume/milestones (2026-07-09)

Section driven to 0 gate-errors (emphasis caps lowercased, two second-person → the agent). One needle re-pointed (test_traceability TestLoaderStaysThin): `must this hold BEFORE any pack file loads?` → `must this hold before any pack file loads?` (same M-1 loader-thin law, register-clean).

## Stage 5 chunk 9 — Parallel lanes, one pen (2026-07-09)

Giant section (~48 lines) fresh-agent rewrite: second person → named actors, ~21 emphasis caps lowercased (PEN→pen defined term, CLAIMING/FOREIGN/DEPENDENCY GRAPH/INTEGRATION/ORDER DECLARED/NARRATED/etc.), region 25 gate-errors → 0. Two needles re-pointed by narrowing (TestDeclineListsAbsorbed): `declined BY NAME` → `declined by name`; `RETURNED to the queue as its own row again` → `returned to the queue as its own row again`. Anchors identical vs b05e199.
Additional re-points same chunk: `DEPENDENCY GRAPH`→`dependency graph` (test_lanes_by_graph); `a FOURTH lane opens only on the human's asked word`→`a fourth lane...`, `waiting for the pen SAYS so...`→`...says so...`, `a pen-stage is never cut mid-edit`→`pen-stage is never cut mid-edit` (test_parallel_lanes_law).

## Stage 5 chunk 10 — Specifying and building a feature (giant, 2026-07-09)

Densest section fresh-agent rewrite (~64 lines): second person → the human/the agent, reassurance dropped, ~30 emphasis caps lowercased; FEATURE-FIT/CROSS-LINK kept, KPI/UX allowlisted. Seven needles re-pointed by narrowing (SPEC-facing only; build-pipeline SKILL VISITOR WALK/FEEL pass left caps, its own restyle): `A feature is specified past what you know to ask`→`…the human knows to ask`; `What already works is promised before you touch it`→`…before the agent touches it`; `A feature also says what it is NOT doing`→`…is not doing`; `TOLD, never confirmed`→`told, never confirmed`; `deliberate RE-ENTRY path`→`deliberate re-entry path`; `VISITOR WALK`→`visitor walk`, `FEEL pass`→`feel pass`; `AUTHORS the facet sentences`→`authors the facet sentences`. Anchors identical vs b05e199.
Two more same chunk: `earns NO new matrix row`→`earns no new matrix row`; `A fenced prototype is NOT swept`→`A fenced prototype is not swept`.

## Stage 5 chunk 11 — Delegation and workers (last giant, 2026-07-09)

~74-line fresh-agent rewrite: second person → named actors, ~29 emphasis caps lowercased (the verify ladder EXISTS/SUBSTANTIVE/WIRED/FLOWS + ADVERSARIAL/MANDATORY/HALT were not test-needles, lowercased free); FRESH-context + tier names haiku/sonnet/senior kept; FIXME allowlisted (literal grep token). Region 31 gate-errors → 0. Four SPEC needles re-pointed by narrowing (build-pipeline SKILL copies left caps for its own restyle): `brief ARMS the worker for the workshop`→`brief arms…`; `escalates ONE tier with a logged line`→`escalates one tier…`; `propose the cheapest tier that can pass the brief`→`proposes the cheapest tier…`; `carries the CLOCK`→`carries the clock`. Anchors identical vs b05e199.

## Stage 5 chunk 13 — remaining small/moderate sections + rhythm/publishing (2026-07-09)

Cleared the last actionable gate-errors across the bug section, the rhythm subsections (versioning/time-discipline/push-CI/scaling), publishing, and open-decisions. DECIDE allowlisted (literal open-decision marker). Emphasis caps lowercased + second person → named actors. Six needles re-pointed by narrowing (all SPEC-facing, test_traceability): `Each publish TARGET is a plugin`→`…target…`; `AT WRITE TIME`→`at write time`; `Find a stale claim and fix it BEFORE the push`→`…before…`; `SHORT-FORM record of three lines`→`short-form record…`; `checklist runs BEFORE the gate`→`…before…`. BODY of SPEC now 0 gate-errors; only the Formal index remains (parked by his word). Anchors identical vs b05e199.

## Stage 5 step 1-2 — whole-doc judge pass + content tests (2026-07-09)

Fresh Opus whole-doc judge (self-test canary passed, 0 hallucinated quotes): 11 surviving definite/likely findings, all fixed via a fresh writer — 4 local redundancies (guardrails-every-step, scope/mandatory restatement, status-report title restatement, no-third-document double), 2 C5 metaphor/narration (live-spec "eats its own cooking" + "taught us"; "the Room shipped through"), 1 persona ("the senior's hand"), 3 mild title-restatements (decision page, echo, away-stretch window). One needle re-pointed (does not touch → No cut touches the delta's mandatory sentences). Added TestNeedleRegisterClean (every live BODY needle lints clean, Formal index excluded as parked) + TestAnchorInBlockquoteGuard. Suite now 203 green.
