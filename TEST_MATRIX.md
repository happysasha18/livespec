# live-spec — Test Matrix (v0.1, 2026-07-05)

Derived from the proven SPEC v0.7.1 **through the proven ARCHITECTURE.md v0.1** (records:
`docs/prover/2026-07-05-lost-layers.md`, `docs/prover/2026-07-05-architecture.md`); kept current through
SPEC v0.14.0 by assignment + the 2026-07-05 audit folds + the doors landing (rows 70-71, M-067..M-071)
+ the night-of-2026-07-05 landings (rows 72-92: facets/fences/intake-trio/founding/design-sync —
anchors T-13..T-15, INV-18..INV-21, B-2, E-18, rows M-072..M-083) + the work-kind landing (SPEC v0.15.0,
session 8: T-16/INV-22, rows M-084/M-085; headers re-pin at each milestone per M-1) + the row-57 landing
(SPEC v0.15.1, session 9: E-21/E-22, rows M-091/M-092). Rows are organized
**architecture node × spec fact**: every index anchor sits in ≥ 1 row under its owning node, every row
pins a test level, and the derivation closes with the coverage validation at the bottom — walked, and
mechanized in `tests/test_traceability.py` so it re-walks at every run, not once. [E-15]

**Test levels, adapted honestly to a text product** (recorded interpretation — prover record F6):
live-spec ships documents and skills, no browser surface, so no fact here requires ≥ `browser-computed`.
The "rendered level" for a text artifact is a `string` assertion **against the SHIPPED file on disk**
(never a source fragment or a memory of it). Two kinds of fact get two honest treatments:
- **structural facts** (a doc exists, carries its sections, cites its law) — level `string`, testable now;
- **behavioral facts** (a discipline holds during work: one landing at a time over time, attic on a real
  adopt run) — the row names its future mechanical owner (the E-6 host-facing gates (rows 55+), snapshot row 55, the next
  adopt run, or the milestone audit) and stays TODO until that owner exists. A TODO row is a named debt,
  never a silent one.

**Status vocabulary:** BUILT (test exists and runs green) · TODO (owner named in the row) · RETIRED (kept, never deleted).

---

## Artifact inventory

Every file a host (or this flagship repo's reader) receives. Each entry is checked shipped-and-non-empty
by `test_artifact_inventory` — the test parses THIS table, so adding an entry auto-extends the check.

| Artifact | Path | Type | Owning test |
|---|---|---|---|
| Base rulebook skill | `skills/live-spec-base/SKILL.md` | shipped text | `test_artifact_inventory` |
| Spec-author skill | `skills/spec-author/SKILL.md` | shipped text | `test_artifact_inventory` |
| Product-prover skill | `skills/product-prover/SKILL.md` | shipped text | `test_artifact_inventory` |
| Build-pipeline skill | `skills/build-pipeline/SKILL.md` | shipped text | `test_artifact_inventory` |
| Communicator skill | `skills/communicator/SKILL.md` | shipped text | `test_artifact_inventory` |
| Spec template | `templates/SPEC.template.md` | shipped text | `test_artifact_inventory` |
| Architecture template | `templates/ARCHITECTURE.template.md` | shipped text | `test_artifact_inventory` |
| Matrix template | `templates/TEST_MATRIX.template.md` | shipped text | `test_artifact_inventory` |
| Roadmap template | `templates/ROADMAP.template.md` | shipped text | `test_artifact_inventory` |
| Journal template | `templates/JOURNAL.template.md` | shipped text | `test_artifact_inventory` |
| Next-steps template | `templates/NEXT_STEPS.template.md` | shipped text | `test_artifact_inventory` |
| Problem-ledger template | `templates/PROBLEMS.template.md` | shipped text | `test_artifact_inventory` + `test_problems_template_shape` |
| Bootstrap suite scaffold | `templates/test_scaffold.template.py` | shipped script | `test_artifact_inventory` + `test_scaffold_bootstrap_runs` (real simulated bootstrap, both ways) |
| Dev-machine skill sync | `scripts/sync-skills.sh` | shipped script | `test_artifact_inventory` + `test_sync_skills_script` (real run, twice) |
| Adoption procedure | `adopt/ADOPT.md` | shipped text | `test_artifact_inventory` |
| Installer | `install.sh` | shipped script | `test_artifact_inventory` |
| Migration note (rename) | `MIGRATION.md` | shipped text | `test_artifact_inventory` |
| Front door | `README.md` | shipped text | `test_artifact_inventory` |
| The one-page map | `OVERVIEW.md` | shipped text | `test_artifact_inventory` |
| Plugin manifest | `.claude-plugin/plugin.json` | shipped config | `test_artifact_inventory` |
| Plugin marketplace ref | `.claude-plugin/marketplace.json` | shipped config | `test_artifact_inventory` |
| Plugin icon | `.claude-plugin/icon.png` | shipped image | `test_artifact_inventory` |
| Mirror sync script | `scripts/sync-mirrors.sh` | shipped script | `test_artifact_inventory` |
| Doc renderer | `scripts/render-doc.py` | shipped script | `test_artifact_inventory`, `test_render_doc_smoke` |
| Base skill README | `skills/live-spec-base/README.md` | shipped text | `test_artifact_inventory` |
| Base skill license | `skills/live-spec-base/LICENSE` | legal | `test_artifact_inventory` |
| Spec-author README | `skills/spec-author/README.md` | shipped text | `test_artifact_inventory` |
| Spec-author license | `skills/spec-author/LICENSE` | legal | `test_artifact_inventory` |
| Product-prover README | `skills/product-prover/README.md` | shipped text | `test_artifact_inventory` |
| Product-prover license | `skills/product-prover/LICENSE` | legal | `test_artifact_inventory` |
| Build-pipeline README | `skills/build-pipeline/README.md` | shipped text | `test_artifact_inventory` |
| Build-pipeline license | `skills/build-pipeline/LICENSE` | legal | `test_artifact_inventory` |
| Communicator README | `skills/communicator/README.md` | shipped text | `test_artifact_inventory` |
| Communicator license | `skills/communicator/LICENSE` | legal | `test_artifact_inventory` |
| Inbox door + law | `inbox/README.md` | shipped text | `test_artifact_inventory` |
| Guardrails scaffold text | `scaffold/guardrails/README.md` | shipped text | `test_artifact_inventory` |
| CI mirror workflow | `.github/workflows/gates.yml` | shipped config | `test_artifact_inventory` + `TestCIMirror` |
| The pack's own spec | `SPEC.md` | flagship doc | `test_artifact_inventory` |
| The pack's own architecture | `ARCHITECTURE.md` | flagship doc | `test_artifact_inventory` |
| The pack's own matrix | `TEST_MATRIX.md` | flagship doc | `test_artifact_inventory` |
| The queue | `ROADMAP.md` | flagship doc | `test_artifact_inventory` |
| The journal | `JOURNAL.md` | flagship doc | `test_artifact_inventory` |
| The resume file | `NEXT_STEPS.md` | flagship doc | `test_artifact_inventory` |
| Package version | `VERSION` | version home | `test_artifact_inventory` |
| Host profile (dogfood) | `.live-spec/profile.md` | settings instance | `test_artifact_inventory` |
| License | `LICENSE` | legal | `test_artifact_inventory` |
| Prover records | `docs/prover/` | records dir (non-empty) | `test_artifact_inventory` |
| Guardrails (pack gates + fence) | `guardrails/` | scripts dir (non-empty) | `test_artifact_inventory` |
| Decision archives | `docs/decisions/` | records dir (non-empty) | `test_artifact_inventory` |
| Research reports | `docs/research/` | records dir (non-empty) | `test_artifact_inventory` |
| Queue archives | `docs/queue-archive/` | records dir (non-empty) | `test_artifact_inventory` |
| Audit records | `docs/audit/` | records dir (non-empty) | `test_artifact_inventory` |
| Prior-art survey | `docs/prior-art.md` | shipped text | `test_artifact_inventory` |
| Publish skill | `skills/publish/SKILL.md` | shipped text | `test_artifact_inventory` |
| Publish README | `skills/publish/README.md` | shipped text | `test_artifact_inventory` |
| Publish license | `skills/publish/LICENSE` | legal | `test_artifact_inventory` |
| Skill evals — method + honest boundary | `evals/README.md` | shipped text | `test_artifact_inventory`, `test_eval_readme_states_honest_boundary` |
| Skill evals — one per working skill | `evals/` | shipped text dir | `test_skill_evals_present` (self-closing over skills/) |
| Eval run records | `docs/evals/` | records dir (non-empty) | `test_artifact_inventory` |

---

## Matrix rows — grouped by architecture node

### [node: base-rulebook]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-001 | Every working skill opens with the base-inherit pin (base name + the base version it was written against); never a working skill without its pin | E-12 | string | `test_skills_inherit_base_pin` | BUILT |
| M-093 | One name-collision law, stated once (base rule 18): semantic mark first, then numeric ordinal -2/-3; concurrent homes add a session token; the attic, the inbox and ADOPT all CITE the law rather than restate half of it; never overwrite, never a third scheme, never a lost file | E-12 | string | `test_collision_law_one_home` | BUILT |
| M-002 | Settings live in four nested scopes and resolve narrowest-out: session > host > personal > package default, broader values inherited until overridden on the human's word; an unrecognized profile line is ignored ALOUD, never silently dropped and never an error | E-13 | string | `test_settings_ladder_documented` (structural clause: ladder + resolution order stated in the base skill); behavioral resolution: milestone audit (M-1) + the E-6 host-facing gates (rows 55+) | BUILT |
| M-003 | Every choice not in the wish is asked or recorded-and-surfaced; never decided-and-buried | INV-5 | string | snapshot declared-scope diff (row 55) — the mechanical fence | TODO |
| M-004 | Proactivity mode and trust are written only on the human's word; the agent never raises its own level | INV-9 | string | milestone audit (M-1) | TODO |
| M-005 | Before every write and commit: re-check `git status` + HEAD; never write over changes you did not make | INV-11 | string | `guardrails/pre-commit` (opt-in fence): `test_armed_stale_head_blocks_commit`, `test_unarmed_fence_passes_silently` | BUILT |
| M-006 | A shared rule has exactly one normative home (the base skill); never two full statements | INV-13 | string | milestone compaction pass (M-1) | TODO |
| M-007 | An override exists only as a written profile line + a dated journal note in the home it governs; never an unwritten divergence | INV-14 | string | `test_host_profile_recorded_override` | BUILT |
| M-008 | The human owns taste, design, irreversible calls, push gates, domain wording, their contract; never the agent | ACT-1 | string | process — every decision page + milestone gate-list (M-1) | TODO |
| M-009 | The senior agent owns judgment (spec deltas, levels, triage); never delegated to a worker | ACT-2 | string | process — journal audit at milestones (M-1) | TODO |
| M-010 | Workers run mechanical execution with persistent checkpoints in `.live-spec/checkpoints/`; never in a system temp dir | ACT-3 | string | router design (row 56) makes it mechanical | TODO |
| M-095 | The worker contract: write-ownership narrowed to the brief's named files; same-session sibling files fence-benign (fence alarms on FOREIGN sessions); live session-scope lines ride into the brief verbatim; failed acceptance escalates one tier, logged; never a silent same-tier retry, never a worker resolving the ladder itself | ACT-3 | string | `test_worker_contract_stated` (SPEC clause + pipeline elaboration) | BUILT |
| M-119 | The brief arms the worker for the workshop: it carries the host's problem-ledger path with the WATCHED-line duty (worker noise lands in its checkpoint as a ledger line; the senior carries it into the ledger at verify) AND the clock read at briefing (a worker's stamps come off the brief's clock); never a worker silently retrying workshop noise, never a worker inventing an hour | ACT-3 | string | `test_brief_carries_ledger_and_clock` | BUILT |
| M-102 | Every delegation's landing report carries the savings line (what went to the worker, roughly what senior work it saved); never a delegation that lands unreported — the missing line is the habit dying | ACT-3 | string | `test_gap6_delegation_savings_line` | BUILT |
| M-104 | The workshop-noise law (base rule): first sight of operational noise = one WATCHED ledger line, never a silent retry; the SECOND occurrence gets an owner that moment — a queue row or the human's dated agreed non-problem (his word alone, INV-9); a third unowned recurrence is a METHOD defect that goes to the pack's queue; never ledger noise preempting the bug lane | INV-23 | string | `test_base_rule_problem_ledger` | BUILT |
| M-011 | A safe breakpoint = LIVE STATE replaced (one block, never stacked) + dated journal entry + commit | M-2 | string | `test_next_steps_live_state` (shape; the discipline audits at M-1) | BUILT |
| M-012 | Versions have named homes: VERSION file, a version line under `metadata:` in its SKILL.md frontmatter, host record; never scattered or absent | M-7 | string | `test_version_homes` | BUILT |
| M-066 | The base skill states each shared rule once and no working skill restates one normatively; never a second normative home for a shared rule | E-12 | string | milestone compaction pass (M-1) | TODO |
| M-069 | A prototype lives fenced (own home) with a PROTOTYPE label per artifact kind, opened only by the assigned senior, shown only as a sketch; never wired into or presented as the product | E-17 | string | `test_base_rules_door_and_prototype`, `test_working_skills_carry_the_door` | BUILT |
| M-134 | The economy ladder: SPEC names `budget.pressure` (full [default] · lean · tight) moved only by the human's word and asked — or the default told — at a project's setup (founding/adoption) alongside project.kind, each rung's legal sheds (node-scoped mid-work test runs with the full suite kept at landing gates; CROSS-LINK with an owed FULL deferrable as a dated debt line; batched landing gates whose batch-end red bisects by landing order; cheaper worker tiers), and the base skill's settings table carries the `budget.pressure` row; never a rung moved by the agent's own word, never a shed taken silently — every taken shed named in the landing report | T-19 | string | `test_economy_ladder` | BUILT |
| M-135 | The never-bend list at every rung, stated once: the door law + tripwires, red-before-fix, the human's gates, the landing report with named sheds, landing purity, the push gate at full rigor, the safety net, narration whole, and an explicit host line outliving any rung; never a rung that sheds the push gate, the door law, or a host profile's tighter line | INV-40 | string | `test_economy_ladder` | BUILT |

### [node: spec-author]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-013 | The spec is the living truth, use-case-first, one surface = one name; never two synced copies | E-4 | string | prover FULL pass at milestones (M-1) | TODO |
| M-148 | A conditionally-entered face (first visit, empty state, onboarding, one-time banner) states its deliberate re-entry path or names the one-way as a decision; trigger wording ("only on first visit/run", "until dismissed") owes its return sentence; the fit walk's journey lens carries the question, the prover's stress list the entry-symmetry lens (wiring); never a get without a set unless the one-way is written by name | INV-50 | string | `test_entry_symmetry` | BUILT |
| M-097 | spec-author's template pointer resolves for a standalone install: the skill names the pack repo as the templates' home; never an in-skill template copy (a copy forks the truth, D-4) | E-4 | string | `test_standalone_template_pointers` | BUILT |
| M-014 | Every stateful surface composes across the canonical axes + the provenance axis at adoption; never only its own axis | C-1 | string | prover FULL pass at milestones (M-1) | TODO |
| M-072 | A feature-doored spec-delta walks the standard-facet sweep (phone/narrow · touch-vs-hover · empty/error/loading · accessibility · performance envelope); the canonical list has ONE home (spec-author); a mid-work re-door re-runs the sweep; a fenced prototype is never swept | T-13 | string | `test_spec_states_facet_sweep`, `test_skills_carry_facet_sweep` | BUILT |
| M-077 | Every feature's delta closes with a non-goals sentence, ALWAYS written ("nothing deliberately left out this time" is valid); a scope-narrowing non-goal rides the batched report; never a missing sentence passing as fine | INV-20 | string | `test_spec_states_intake_trio`, `test_skills_carry_intake_trio` | BUILT |
| M-078 | Every feature states one success measure, decided or `[default]`-tagged (provenance only — no derived test row while the reading machinery is [target]); binds forward, adopted features owe theirs at first touch (A-3); never a measure claimed as machine-checked before the machinery lands | INV-21 | string | `test_spec_states_intake_trio`, `test_skills_carry_intake_trio` | BUILT |
| M-074 | A feature-delta touching a live surface opens with regression fences BEFORE the facet sweep; each fence cites the clause it guards; a fact is fenced xor re-authored; a prototype fences nothing; never a live surface touched without its fences authored first | T-14 | string | `test_spec_states_regression_fences`, `test_skills_carry_regression_fences` | BUILT |
| M-075 | A fence earns NO new matrix row — it discharges through the cited clause's never-side; an unwritten or unverified promise reconciles first (A-3) and becomes its own fact; fences named by anchor in the wish's row | INV-19 | string | `test_spec_states_regression_fences`, `test_skills_carry_regression_fences` | BUILT |
| M-073 | Every facet ends as a spec sentence — decided, or `[default]`-tagged + TOLD on the landing report's defaults list as a plain-words tradeoff, never confirmed (INV-31); adopted/promoted surfaces reconcile defaults from shipped truth; never a facet silently absent | INV-18 | string | `test_spec_states_facet_sweep`, `test_skills_carry_facet_sweep` | BUILT |
| M-114 | The fit walk: a feature-doored wish is interrogated for product fit at intake, kind-scaled (product: journey/return/cross-entry/implied state/feel/invited-next; infra: flows/data lifecycle/failure paths; skill: trigger/correction/not-fire); trivially-closable holes are closed by the walker AND written how; only genuine taste calls go out, batched; never a fit question left unwalked, never the person interrogated | INV-29 | string | `test_fit_walk_law` | BUILT |

### [node: product-prover]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-015 | Every live-spec push is preceded, same session, by fence + a whole-spec re-check recorded in `docs/prover/` — and the record is for the PUSHED STATE: the newest record commit is never older than the last SPEC.md commit (row 61); never a push without its record, never a today-dated-but-stale record passing | M-6 | string | `guardrails/pre-push` gate a: `test_real_repo_passes`, `test_missing_record_fails`, `test_stale_record_fails`, `test_record_with_spec_same_commit_passes` | BUILT |

### [node: build-pipeline]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-076 | Scope, never time: a too-big wish is cut (fewer surfaces, plainer defaults) or split into stages; a time budget/estimate is never an input; the proposal proceeds on the recommended option, surfaced in the batched report; never a silent cut, never lane order moved, never the safety net touched | T-15 | string | `test_spec_states_intake_trio`, `test_skills_carry_intake_trio` | BUILT |
| M-098 | build-pipeline's template pointers (architecture + matrix steps) resolve for a standalone install: the pack repo named as their home; never an in-skill template copy | E-14 | string | `test_standalone_template_pointers` | BUILT |
| M-100 | A second bug in the same area within ~30 days re-doors to FEATURE — the area is missing an invariant; the journal grep is the detector; never a second patch on the same spot inside the window | T-9 | string | `test_gap4_recurring_bug_escalates` | BUILT |
| M-101 | The CHANGELOG speaks to the user (what changed for them + one real example); internal names/ids/rows stay in the journal; and no doc pins a drifting version number in prose — the version's one home is pointed at, never copied; never a user-facing entry in mechanism words | T-6 | string | `test_gaps5_8_docs_discipline` | BUILT |
| M-016 | A wish is one request in plain words, any size, any moment; never lost for being informal | E-2 | string | process — inbox + intake discipline; milestone re-listing (M-1) | TODO |
| M-017 | The wish walks arrived → classified → spec-delta → validated → queued → in-work → landed; never skipping the spec-delta or validation step | T-1..T-6 | string | the E-6 host-facing gates (rows 55+) (bounds check: behaviour traces to spec) | TODO |
| M-018 | A wish may exit declined / deferred / superseded — the row stays in the table; never deleted | T-8 | string | queue archive rule + milestone audit | TODO |
| M-094 | Declining an absorber lists the rows superseded into it; each listed row is declined by name or returned to the queue; never a superseded wish dying by pointer | T-8 | string | `test_spec_states_decline_absorbed` (clause in SPEC + template; the behavioural side audits at M-1 — no declined absorber exists yet to check) | BUILT |
| M-019 | A bug preempts: every rolling wish parks with its own checkpoint (at most one parked per lane), nothing red is committed, parked wishes resume in landing order; never a bug itself interrupted | T-9 | string | process — next real preemption journals it; the E-6 host-facing gates (rows 55+) | TODO |
| M-020 | Priority bends the lane visibly: critical heads the line, a quick win may bubble once, then the queue head; never a silent jump and never starvation | T-11 | string | queue audit at milestones (M-1) | TODO |
| M-021 | No wish is ever lost: the row exists the minute it is spoken; never an intake that leaves no trace | INV-1 | string | milestone re-listing of gates + inbox files (M-1) | TODO |
| M-022 | One landing at a time per repo under one pen; in-work rows never exceed T-18's lane cap (three [default] — the number's ONE home is T-18) and claiming stays an atomic committed flip; never a fourth row in-work unasked, never two foreign sessions sharing a repo's pen | INV-2 | string | `test_roadmap_in_work_cap` | BUILT |
| M-129 | Parallel lanes: one session may roll up to three INDEPENDENT build lanes without asking (T-18's [default] cap, his 2026-07-06 word; a fourth only on the human's asked word) — opening narrated, every train on the departures board, a waiting lane naming whom it waits behind; penless stages overlap (later trains' code and tests each in its own isolated tree only; disjoint-file workers within one lane; read-only analysis free); pen-stages serialize (every shared doc — spec, architecture, matrix, queue, journal, resume file — plus integration and row close), a pen-stage never cut mid-edit; never a fourth build lane unasked, never parallel lanes across sessions, never mid-milestone, never a spec-delta proven against another lane's half-written draft | T-18 | string | `test_parallel_lanes_law` | BUILT |
| M-130 | Landing purity under several trains: a landing commit carries exactly one row's delta and its gate (full suite + guardrails) runs on a tree holding nothing of any other lane's unfinished work; after a landing the waiting lanes re-check the fence and re-run their gates on the new truth — landed-first wins; never half of another train riding a landing, never a later lane landing unre-verified | INV-39 | string | `test_landing_purity` | BUILT |
| M-136 | The architecture owes numbers: measurable quality budgets plus each budget's instrumentation home (numbers measured and human-readable), the project's KIND proposing the dimensions (product: paint/interaction times; backend: latency/throughput/errors; CLI/pipeline: run time, per-unit cost; skill pack: eval pass rate, suite time; prose: what honestly has a number) with a no-honest-number quality said by name; each budget asserted by a matrix-row acceptance; spec-author's performance facet ends as a budget sentence and build-pipeline's architecture step demands the kind-derived budget line; never a surface passing derivation with no budgets and no instrumentation home, never a vanity metric standing in for an unmeasurable quality, never a budget living only as prose hope | INV-41 | string | `test_architecture_owes_budgets` | BUILT |
| M-140 | An approved prototype is the norm, four arms in four homes: spec-author states the pointer format (`norm: <path>` at the clause's line end, approval freezing the artifact into `docs/norms/` with a dated provenance line — never a pointer into a live prototype home); build-pipeline's code step OPENS a norm-pointered surface's artifact before building and the landing records a one-line plan-vs-prototype diff, the verify feel bar reading the same pointer; build-pipeline's door step honours a row-recorded mockup-first entry condition, cancelled only by the human naming it; product-prover carries the norm lens (prototype-born clause without pointer / text contradicting its own artifact = finding); never a general "go build" cancelling a named entry condition, never a norm-pointered surface built without the artifact opened, never the pointer format living in a second home | INV-43 | string | `test_prototype_norm_pointer` | BUILT |
| M-144 | Verify's adversarial option: a fresh-context checker briefed with the landing's SPEC sentences + artifact paths (never the worker's summary), hypothesis "tasks completed, goal missed", ladder exists → substantive (stub-grep list in step 8) → wired → flows; MANDATORY when the code step was delegated AND the delta is surface-sized; kind-scaled for skill/prose; the checker under the worker contract, verdict in the landing report; never the checker briefed with the worker's summary (spec sentences + artifact paths only), never findings closed with a nod | INV-46 | string | `test_adversarial_verify_option` | BUILT |
| M-147 | Lanes are picked by a dependency graph at queue-take (edge = shared surface / spec section / skill file / doc region), opened on a pairwise-independent set up to the T-18 cap, integration-only collisions pre-rolling with the landing order DECLARED at claim; tiny rows ride serial (parallel pays only when build stages dominate) and the choice is narrated on the board; never lanes picked by mood, never an undeclared integration order, never the cap read as counting one lane's serial rows | INV-49 | string | `test_lanes_by_graph` | BUILT |
| M-151 | A brief editing existing files is born from reading them in full: three recorded lines per file (current state · what changes · what must survive), every step back-referencing its spec sentence, every technical claim citing a source; never a brief written from memory of a file | INV-53 | string | `test_brief_trio_laws` | BUILT |
| M-152 | The worker HALT list is closed and short: ambiguous requirement · two consecutive unexplained failures · missing config/dependency · acceptance impossible as briefed — stop WITH evidence, otherwise run to completion; never an open-ended "ask if unsure", never a silent stop outside the list | INV-54 | string | `test_brief_trio_laws` | BUILT |
| M-153 | A brief is sized: text ~300 lines, ~8 files to edit [default], splits above either; paths, never inlined file bodies; never a brief inlining a file body | INV-55 | string | `test_brief_trio_laws` | BUILT |
| M-023 | Every landing cites its wish row in commit or journal; never an unexplained change | INV-3 | string | pre-push hook (the E-6 host-facing gates (rows 55+)) | TODO |
| M-024 | A pending human question never stops the lane — work proceeds on the recommended option, marked in the row | INV-4 | string | queue audit at milestones (M-1) | TODO |
| M-025 | Ambiguous size, priority, or work-kind is asked at intake, never guessed; the class column speaks the four-word vocabulary + priority marks only | INV-12 | string | `test_roadmap_class_vocabulary` | BUILT |
| M-026 | ARCHITECTURE.md exists, every node pinned to a real file:line, proven before the matrix derives; never an unproven architecture under a matrix | E-14 | string | `test_architecture_owns_every_anchor_once`, `test_architecture_no_orphan_nodes` | BUILT |
| M-027 | The matrix is DERIVED node × fact with the coverage validation walked; never just filled | E-15 | string | `test_matrix_covers_every_anchor`, `test_matrix_blocks_match_architecture_nodes` | BUILT |
| M-028 | No wish lands whose facts lack an owning node and a right-level matrix row (binds from this landing, never retroactively) | INV-15 | string | `test_matrix_covers_every_anchor` (re-runs at every commit) | BUILT |
| M-029 | The milestone gate runs: full re-prove + matrix audit + composition check + compaction (docs AND the test suite — a duplicate/superseded test dies only with its rows shown still covered) + gate/inbox re-listing + index re-check + the loader-stays-thin walk (line count stated; a line failing the must-hold-before-pack-loads test migrates to its real home); never a MINOR without it | M-1 | string | clause presence: `test_m1_names_loader_thin_item`; the walk itself: next MINOR walks it; journal records the walk (first walk journaled 2026-07-05, session 9: 16 non-empty lines, all pass) | TODO |
| M-128 | The milestone gate also re-walks the pack's skills through the standard skill-making skill (skill-creator's format/frontmatter/description-triggering lens — evals test behaviour, this lens tests the craft of the skill file); findings folded or rejected with a written reason in a dated record; a skill newly joining the pack walks it at birth; never a milestone without the re-walk item, never a walk whose findings vanish unrecorded | M-1 | string | clause presence: `test_m1_names_skill_creator_rewalk`; the walk itself: dated record in docs/audit/ (first full walk 2026-07-06, session 17) | BUILT |
| M-067 | The door is named before any code: every wish states size · priority · door · work-kind in ONE intake line; never code before the door is said | T-12 | string | `test_spec_states_door_procedure`, `test_working_skills_carry_the_door` | BUILT |
| M-068 | Feature tripwires are hard and ordered (surface/state/interaction/[target]/unbacked behaviour ⇒ feature); the verdict outranks a casual label, a re-doored wish takes no preemption, the door re-fires mid-work; never a wish hand-built past the pipeline for sounding small | INV-16 | string | `test_spec_states_door_procedure`, `test_base_rules_door_and_prototype` | BUILT |
| M-084 | The work-kind is named at intake: product · infra · skill · prose, one kind per wish, called from what the wish PRODUCES; a host with ONE usual kind may record a profile default; the vocabulary is curated — a fifth joins only with a named mis-served wish; never a guessed kind (uncallable ⇒ asked, like size) | T-16 | string | `test_spec_states_work_kind`, `test_skills_carry_work_kind` | BUILT |
| M-108 | One wish = one user story: a multi-story wish splits at intake, each story its own row citing the one spoken wish it came from; sub-behaviours (hover face, phone face, backpointer) are the story's acceptance, not new stories; unclear count asked at intake; never two stories fused into one new row, never a split that loses the origin | T-17 | string | `test_one_story_close_whole` | BUILT |
| M-109 | A row closes only whole: a multi-leg row's Done-when enumerates per-leg acceptance; no landing report closes a row with an unmet leg (half-done is a status); the resume file's LIVE-STATE restates an open leg at every supersession; never "COMPLETE" beside an unmet enumerated leg, never a leg compressed out of the resume file | INV-26 | string | `test_one_story_close_whole` | BUILT |
| M-085 | The kind scales each running step's FORM (per-kind table's one home: build-pipeline SKILL.md); at landing every door-granted step has APPLIED or STOOD DOWN by name in the report; an unresolved kind scales nothing down; never a silent skip, and never the safety net (door law, mandatory sentences, ask-at-intake) touched by a kind | INV-22 | string | `test_spec_states_work_kind`, `test_skills_carry_work_kind` | BUILT |
| M-115 | Product-kind verify includes the VISITOR WALK (first visit · return · cross-entry · from-any-point navigation · exits) and the FEEL pass (motion quality, affordance craft) against the approved prototype's bar, in the medium's own form (a text product walks its reading path, not animations); findings become rows or red; never "renders and clicks" alone passing a product-kind verify, never findings kept as vibes | INV-30 | string | `test_visitor_walk_feel_pass` | BUILT |
| M-116 | A taste choice made without asking is TOLD at landing: the report names each open `[default]` in plain words with an example and a tweakable mark; no confirmation requested, silence is consent, never re-asked — the person asks when they want a change; never a choice accumulating untold, never a forced confirmation loop | INV-31 | string | `test_default_expiry_law` | BUILT |
| M-120 | Every pipeline step is worked in its craft's mindset — the step→craft ladder (product manager at spec · formal reviewer at both prove steps · architect at architecture · QA automation at matrix and tests · senior developer at code · the visitor's own eyes at verify · release hand at commit & show) lives in ONE home, build-pipeline's step list, and artifacts are judged by their craft's standards; never a second full ladder statement elsewhere, never a generalist head excused by habit | INV-33 | string | `test_craft_ladder` | BUILT |
| M-126 | Every wish is placed on the feature map at intake: the placement spoken with the echo and written in the row's `map:` note — changes feature X · new feature · restructure; the map is the spec's scenarios + the architecture's nodes, no third document; a restructure verdict queues its own row and re-carves only through the architecture step's re-prove; never a silent placement, never a re-carve in passing | INV-37 | string | `test_feature_map_placement` | BUILT |

### [node: publish]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-089 | Publishing owes the artifact's kind its checklist — the per-kind table's ONE home is the publish skill (floor: what/who/how-to-start, claims true today, license explicit; skill → install+commands+when-NOT; tool → real runs; visual product → fresh screenshots; prose → reading path); never a deposit past the checklist | E-20 | string | `test_publish_skill_carries_checklist` | BUILT |
| M-141 | A version push re-opens the shopfront: publish's fire-list includes any push shipping a new version; the walk checks README claims against the pushed truth + kind-owed visuals (skill pack: diagrams; visual product: fresh screenshots; tool: example runs); the commit-and-show step points at the walk and the landing report carries its outcome ("shopfront checked — current" when untouched); never a version push past a stale claim, never the checklist's home moving out of the publish skill | INV-44 | string | `test_shopfront_fresh_at_push` | BUILT |
| M-090 | Publish targets are PLUGINS embedding their steps (GitHub · plugin directory · design project), never removing the kind's owed minimum; the walk runs BEFORE the human's gate and never sends anything itself; never a publish bypassing base rules 12/17 or a host push gate (M-6) | E-20 | string | `test_publish_skill_carries_checklist`; behaviour: first real use = our own next public push, journaled | BUILT |

### [node: skill-evals]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-086 | Every working skill owns an eval file: scenario · criteria · dated bare-run record (red PROVEN, never asserted) · re-run instructions; the required set derives from skills/ itself, so a fifth working skill is red until its eval exists; never a skill without its eval | E-19 | string | `test_skill_evals_present` | BUILT |
| M-087 | The eval method states its honest boundary (bare = bare-of-the-SKILL, the machine loader still feeds method) and the authoring rule (the scenario speaks like the human — no enumerated facet hints); run records are dated and append-only; evals re-run at milestones (M-1 list) and at behaviour-changing skill landings; never a contaminated red sold as clean | E-19 | string | `test_eval_readme_states_honest_boundary`; re-run discipline: milestone audit (M-1) | BUILT |

### [node: communicator]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-030 | A landing is reported in one plain-language line (position · what landed · what remains); never a report that only points at internal rows | T-7 | string | process — communicator rules 8/9; milestone audit | TODO |
| M-092 | Batched questions arrive as ONE decision page (one card per pick, recommendation named, free-form room), answers archived in docs/decisions/ and harvested the same session; never a serialized chat questionnaire, never an answer left un-harvested | E-22 | string | `test_spec_names_decision_page` (SPEC clause + rule-10 mechanics in the shipped communicator SKILL.md) | BUILT |
| M-099 | Communicator's trigger is narrowed: decisions, landing/milestone reports, problems needing the human's word — with a stated NOT-side (mid-work status lines, internal notes, plain factual answers); never a description that fires on every passing report | T-7 | string | `test_communicator_trigger_narrowed` | BUILT |
| M-107 | A done-claim ("did we do X?") is answered as an evidence walk: each claim pinned to a checkable artifact walked NOW (adoption/prover record, suite run, commit, matrix row), verified vs asserted said apart, and the answer names the method version from the host's installed set — or says plainly that none exists; never a narrative answer standing alone, never "done by live-spec" without its version, never an invented version for an unadopted host | INV-25 | string | `test_done_claim_evidence_walk` | BUILT |
| M-111 | The capture echo: the moment a wish is intaken the human hears ONE plain sentence — what was heard, the door called, the name the work will answer to, its row number; a silent arrival (inbox file, harvest) echoes in the next report, never as an interruption; never a wish intaken without its echo, never the echo replacing the written row | INV-27 | string | `test_capture_echo_and_board` | BUILT |
| M-112 | The departures board: every status report names each in-flight feature by its echo-name with its pipeline station (all nine steps: spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show, plus the terminal landed), the station vocabulary being the pipeline's own step names, one station per step; never progress reported as prose archaeology, never a station name drifting from the pipeline's step names, never a pipeline step left without its own station | INV-27 | string | `test_capture_echo_and_board` | BUILT |
| M-113 | The outcome does the talking: echo-names are short descriptive phrases in the product's words (never a private metaphor); a human-facing report/board line opens with what changed for the reader; spec codes, row/session numbers, and coined names only TRAIL in parentheses; one fact = one standalone sentence; never a line led by a nickname the reader never chose to learn, never riddle-compression | INV-28 | string | `test_outcome_leads_law` | BUILT |
| M-117 | A decision card opens with what the choice CHANGES for the person under each option, in the product's words; mechanism only after, only if it helps; never a card answerable only by understanding the mechanism | INV-32 | string | `test_decision_card_consequences` | BUILT |
| M-121 | The bookkeeping NEVER-list: rule 8 names the tokens that are never message content (a test count, a suite size, a version string, a check tally) with the translation the message says instead ("tested clean", "saved") and a worked before/after example; the carve-out stands — a direct question about the number, or the done-claim evidence walk (INV-25), gets the number as the answer; never bookkeeping doing the talking in a human-facing message, never the carve-out lost | INV-28 | string | `test_bookkeeping_never_list` | BUILT |
| M-133 | The chat laws' mechanical voice: `scripts/chat-law-hook.sh` exists, is executable, and its one line carries both laws' teeth — "plain product words" doing the talking with codes only allowed to "trail in parentheses", and narration naming the wish and station, digesting station ends, owing a heartbeat past ~10 minutes; `scripts/install-session-hooks.sh` covers BOTH session hooks (clock + laws, UserPromptSubmit wiring) and is the human's hand to run; the skills stay the laws' homes; never the hook line legislating law the skills don't hold, never a silent install by the agent's own hand | INV-28 | string | `test_output_carries_both_laws` (with `test_script_exists_and_executable` + `test_installer_covers_both_hooks`; red-proven on the absent scripts first) | BUILT |
| M-122 | The pre-report walk: communicator states the walked step — before any movement-end or milestone report goes to the human, the rules are re-read and the draft passes phrase by phrase through "does this sentence stand for a reader outside the pack" (a pack surface named is explained in the reader's words or dropped; quiet trailing anchors stay legal); never a movement-end report sent unwalked, never the walk becoming a confirmation request | INV-34 | string | `test_pre_report_walk` | BUILT |
| M-124 | Working narration: while work runs, beats are narrated as they happen — a pipeline station passed, a load-bearing find, a change of direction — one-two plain sentences in the roadmap's terms, the reports' voice, the mechanical grind quiet; the three teeth stand in both homes (SPEC INV-35 + communicator rule 13): IDENTITY — every beat names the wish and station in hand (the work's own name outside the pipeline) and whether it mends or builds; DIGEST — a station's completion is a beat whose line digests what the station produced in the work's own words, a worker-closed station becoming the senior's beat when its result lands; HEARTBEAT — a beatless stretch past ~10 minutes [default] gets a line naming what grinds; a narration line is chat, not a report — it walks no pre-report walk, asks no questions, and the plain-language + bookkeeping laws still bind it; never a beat-worth stretch left silent between echo and report, never a station closed silently, never a digest pasting the artifact or speaking in counters, never narration replacing the milestone report or triggering the walk | INV-35 | string | `test_working_narration` | BUILT |
| M-138 | The heartbeat's offline-window face: when a coming stretch needs nothing from the human — a local suite run, a worker batch, a long render — narration says BEFORE it starts that he may step away, an honest range for how long (unknown said as unknown, never a guess dressed as a promise), and what he is needed for at its end; the needed-again moment is its own beat — a chat line awaiting his return, never a summons; beats keep landing inside the window (a read, never a dismissal), its questions batch to its end, an off-range end says itself (overrun, done sooner, blocked on his word alone); the clause stands in both homes (SPEC INV-35 + communicator rule 13's heartbeat tooth); never an offline sentence when the very next beat needs the human, never the superseded row-138 fence sentence left standing in either home | INV-35 | string | `test_offline_window` | BUILT |
| M-139 | His word on a shown artifact is read as meant, in both homes (SPEC INV-42 + communicator): a phrasing the human killed in a review round stays killed in every later draft of that artifact — the kill-list written where the artifact's project keeps its records (journal or notes file), never only in session memory; a vivid phrase of his is adopted only as meant — mockery of a bad draft is not guidance, intent read from context or asked (INV-4); never a cut phrasing resurfacing in a later draft, never a wipe resurrecting a cut, never his sarcasm earnestly baked in as prescription | INV-42 | string | `test_his_word_read_right` | BUILT |
| M-149 | Anything handed/opened to the human leads with its passport: the project's NAME in the visible content (never only the URL) + the read contract ("needs your word: what, by when" or "just an update, no action"); the announcing chat line carries the same two facts; never an anonymous page opened at him, never an artifact silent about whether it wants him | INV-51 | string | `test_artifact_passport` | BUILT |
| M-150 | During an away-stretch (the offline window is the trigger) no browser window opens mid-stretch: artifacts accumulate on ONE page, opened once at the stretch's end; mid-stretch re-open only as the same page refreshed in place; precedence stated: INV-52 governs WHEN, the show rule HOW, the passport WHAT; never a window per artifact at an away human | INV-52 | string | `test_windows_accumulate` | BUILT |
| M-127 | The feature map on demand: on the human's ask («покажи все фичи» and kin) the WHOLE map is read at ask-time off the spec's scenario sections, the current-vs-target header (statuses at the [target] tag's own granularity — a mixed scenario reads "shipped, with promised parts", never one blanket status), and the queue's open rows (stations for in-flight, queued NEW-verdict wishes included); answer lines obey the line law; chat by default, rendered page on the human's word; a host with nothing to read is answered honestly (bootstrap/adoption pointer); never a third document created or cached, never fired uninvited (routine reports keep the board's in-flight scope), never a queued wish missing from the map | INV-38 | string | `test_feature_map_on_demand` | BUILT |

| M-137 | The session's task list is a language-law surface: task subjects and spinner lines speak plain product ENGLISH (the docs language) — understandable at a glance, what is being done for which feature — with codes, row numbers, and internal step names only trailing; never a subject that is a bare code chain, never task titles in jargon the human must decode | INV-28 | string | `test_task_list_plain_words` | BUILT |

### [node: templates]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-031 | The queue is one table: wish · class · status · acceptance, one row per wish; never a second scale or format | E-3 | string | `test_roadmap_class_vocabulary` (columns + vocabulary) | BUILT |
| M-032 | The matrix shape: inventory + node blocks + coverage validation; never a bare row bucket | E-5 | string | `test_matrix_blocks_match_architecture_nodes` | BUILT |
| M-033 | Every matrix row states the DO and the NEVER side; never a row without its regression fence | INV-6 | string | `test_matrix_rows_have_level_and_negative_side` + `test_gap10_step5_both_sides` (the derivation step TEACHES it, row 12 gap 10) | BUILT |
| M-034 | Bootstrap = VCS gate FIRST → copy the six templates + the suite scaffold (which DEFINES green for landing #1: docs present, headers filled, no surviving placeholder) → hooks offered as at adoption → first wish through the pipeline; never landing before the gate, never a bootstrap without a runnable suite | B-1 | string | `test_templates_ship` + `test_scaffold_bootstrap_runs` (simulated bootstrap BY DEED: filled → green, placeholder → red) + `test_spec_states_bootstrap_order` | BUILT |
| M-103 | The problem-ledger template ships the shape: signature + dated occurrences + the full status vocabulary (WATCHED · OWNED · AGREED NON-PROBLEM · SOLVED) + a dated ARCHIVED tail; never a shape missing a status or the archive home | E-24 | string | `test_problems_template_shape` | BUILT |
| M-146 | The resume file is a digest with a hard cap: the whole file ≤ 100 lines [default], the check red-proven on a synthetic bloated file and green on the pack's own NEXT_STEPS; the template states the cap; open legs restate as one terse line each (INV-26 by form); never a cap satisfied by dropping an open leg; the number's normative home is the law, template and check restating it | INV-48 | string | `test_resume_digest_cap` + `test_resume_cap_catches_synthetic_bloat` (tests/test_resume_digest.py) | BUILT |

### [node: attach]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-079 | Founding questions asked or profile-read at bootstrap AND owed at adopt orient (A-1 pointer); personal-vs-reusable first; never a founding answer inferred from examples | B-2 | string | `test_spec_states_founding_and_designsync` | BUILT |
| M-035 | The host owns its docs and a `.live-spec/` folder (profile, checkpoints, installed versions); never pack state scattered into host folders | E-1 | string | `test_host_profile_recorded_override` (dogfood instance) | BUILT |
| M-036 | The attic archives superseded host files with a manifest line; never deletion | E-9 | string | `test_adopt_phases_cite_spec` (procedure text; behavior = next adopt run) | BUILT |
| M-037 | No adopt or rework run deletes a host file; authored content never bypasses the attic | INV-7 | string | next real adopt run journals it; the E-6 host-facing gates (rows 55+) long-term | TODO |
| M-038 | No landing into an unversioned host: git + (remote exists OR explicitly declined, recorded); never a mere recommendation | INV-8 | string | next bootstrap/adopt run journals the gate outcome | TODO |
| M-039 | Adoption codes name meanings, not order; the VCS gate runs FIRST — never an irreversible touch before it | A-0 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-040 | Orient: every existing document is read before anything is touched; never a blank-slate assumption | A-1 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-041 | Inventory: code, surfaces (seeding the registry), docs — with owners; never an unlisted surface | A-2 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-042 | Existing docs re-engineer into live-spec shapes, claims marked unverified until reconciled; never trusted unreconciled | A-3 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-043 | Superseded files move to the attic during adoption; never silently replaced | A-4 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-044 | The version-control gate: init, .gitignore, pristine baseline, remote settled as a named deliverable — never closed on a mere recommendation | A-5 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-045 | On any version change the agent re-reads the changed SKILL.md + journals old → new; re-stats at every breakpoint; never coasts on a stale copy | A-7 | string | `test_adopt_phases_cite_spec` (text; behavior audits at M-1) | BUILT |
| M-091 | install.sh copies every pack skill into the skills home, idempotently — an existing copy is backed up with a timestamp before overwrite; never a skill deleted, never a second run destroying the first | E-21 | string | `test_install_sh_installs_and_backs_up` (a REAL run against a temp home, twice) | BUILT |
| M-118 | install.sh backs up a replaced skill OUTSIDE the live skills directory (an attic folder beside it), so the harness never lists stale duplicates as loadable skills; never a backup landing inside ~/.claude/skills | E-21 | string | `test_install_backup_home` | BUILT |
| M-131 | The pack update check (a REAL run against fixture files): a newer remote yields the spoken proposal — both versions, the what-changed pointer, the install.sh/pull road, the PROPOSAL-ONLY sentence; an equal or OLDER remote reads "up to date" (forward only, never a downgrade); an unreadable remote reads one honest skip line NAMING the address, stamp left unwritten; a same-day stamp skips quietly; never an install performed, never a block on no network | E-25 | string | `test_pack_update_check` (REAL script runs against temp stamp/remote/installed files) | BUILT |
| M-046 | Adopt working artifacts live tracked in `.live-spec/adopt/`; never scattered into the host's own folders | A-8 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-047 | A cruft sweep is offered, listed, human-gated, regenerable-only; never silent and never authored content | A-9 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-071 | Adoption gives every unbacked live surface a human verdict — promote / quarantine / attic; never an unbacked surface silently registered as product | A-10 | string | `test_adopt_phases_cite_spec` (A-10 citation + verdict wording) | BUILT |
| M-125 | The project knows its own kind: `project.kind` asked at founding and at adoption's orient — always the human's answer, never profile-seeded — recorded in the host profile, seeding project-wide defaults without overriding an explicit line, updated on the human's word the moment evolution is noticed, journaled; never inferred from examples, never a founding fossil an audit has to catch | INV-36 | string | `test_project_kind` | BUILT |

### [node: inbox]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-048 | An outside wish = one NEW committed file, named by the law; never an edit to an existing file | E-11 | string | `test_inbox_states_write_rule` | BUILT |
| M-049 | A live-spec session sweeps the inbox FIRST and harvests each file into a queue row; never a wish durably recorded but operationally invisible | T-10 | string | milestone re-listing of unharvested files (M-1) | TODO |
| M-050 | Only a session assigned to live-spec writes this repo; an outsider never writes spec/queue/journal/skills — the inbox file is the whole exception | INV-10 | string | `test_inbox_states_write_rule` | BUILT |

### [node: host-contract]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-051 | The host profile narrows the human's contract for one project, every line a recorded override; never a silent divergence | E-8 | string | `test_host_profile_recorded_override` | BUILT |
| M-065 | The personal layer has ONE home (the profile); the global instruction file is a thin loader carrying only the pointer + bootstrap lines (their one home — never restated in the profile); a session line is never written by the agent; the migration fork never writes a foreign repo | E-16 | string | milestone audit (M-1) — loader live since row 52; asserted at audits | TODO |

### [node: package-docs]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-052 | Shipped vs target is marked honestly; every [target] machine is owned by a STILL-OPEN queue row (declared map, self-closing both directions); a [target] node names its missing pin, a fully-pinned node carries no tag; never a claimed-shipped target, never a target orphaned by its row landing or vanishing | S-0 | string | `test_targets_owned_by_open_rows`, `test_target_nodes_pin_honesty` (row 64 mechanized what prover F1 caught by hand) | BUILT |
| M-053 | The queue and the spec carry dated versions; never an undated truth | M-3 | string | `test_roadmap_header_dated` | BUILT |
| M-096 | Dev-machine skill sync goes through the named script: installed copies overwritten from the repo source, every version change REPORTED old → new (the A-7 trigger line); idempotent — a fresh dest fills, an unchanged one says so; never a silent hand-copy as the sync path | E-23 | string | `test_sync_skills_script` (a REAL run against a temp dest, twice) | BUILT |
| M-054 | live-spec eats its own cooking — this repo works by its own spec and queue; the pack's own push gates run mechanically on the installed hooks; never a claim of mechanical enforcement beyond what is actually wired | M-4 | string | `test_hooks_and_scripts_exist_and_executable` (+ `guardrails/install.sh` run for real, journaled) | BUILT |
| M-143 | A stranger's first minute is clean: `python3 -m pytest` from the repo root collects and runs the real suite (pytest.ini pins testpaths to tests/) — the scaffold template is never collected, never executed, and stays a template; never a shipped file whose NAME makes a standard tool trip in the repo's first minute | M-4 | string | `test_pytest_collects_clean_from_root` (real `pytest --collect-only` run from ROOT; red-proven on the pre-fix tree) | BUILT |
| M-055 | Attic layout choice stays open with a named revisit trigger; never silently resolved | D-1 | string | `test_spec_decide_markers_match_open` | BUILT |
| M-056 | Tier-routing override choice stays open (closes via row 56); never silently resolved | D-2 | string | `test_spec_decide_markers_match_open` | BUILT |
| M-057 | Snapshot retention choice stays open (closes via row 55); never silently resolved | D-3 | string | `test_spec_decide_markers_match_open` | BUILT |
| M-058 | D-4 records its decided state (package-is-source, row 51 executes); never re-litigated silently | D-4 | string | `test_spec_decide_markers_match_open` | BUILT |
| M-059 | D-5 records its decided state (all-into-profile, rows 52–54 execute); never re-litigated silently | D-5 | string | `test_spec_decide_markers_match_open` | BUILT |
| M-105 | The pack keeps its own problem ledger (dogfood — E-24's shape applied to itself): `.live-spec/PROBLEMS.md` exists, every entry carries a signature, ≥1 date, and a legal status; never an empty ledger claiming entries, never an entry without date or status | M-4 | string | `test_pack_own_ledger` | BUILT |

### [node: guardrails [target]]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-082 | Architecture pins are names first, the :line a cache (E-14); the drift gate (g) turns file-missing/beyond-EOF RED and reports label drift (strict mode blocks); never a rotten pin trusted silently | E-6 | string | `test_real_repo_passes` (gate g), `test_missing_file_fails`, `test_label_drift_strict_fails` | BUILT |
| M-083 | The surface registry's PREFERRED form is executable (a declared map inside a completeness-gate test, red both directions); the .md is the doc-only fallback; adoption never asks an executable registry to step back into a document | E-10 | string | clause presence: `test_spec_states_registry_and_pins`; machine rides row 55 | BUILT |
| M-081 | Every shipped skill loads: frontmatter parses, name = folder, description + version present, a "when NOT to use" section scopes it; a broken skill turns the push gate RED; never an unloadable or unscoped skill shipped | E-6 | string | `test_real_repo_passes` (gate f), `test_broken_skill_fails`, `test_missing_skills_dir_fails` | BUILT |
| M-060 | The guardrails run on the pre-push hook: completeness, tests-present, behaviour-traces-to-spec, declared-scope diff; never a red push | E-6 | string | first slice BUILT (pack gates: prover record · green suite · anchor ownership · matrix coverage — `guardrails/pre-push` + `test_guardrails.py`); the four host-facing checks await the surface registry + snapshot (rows 55+) | TODO |
| M-061 | The surface registry is self-closing: a rendered-but-unregistered surface is RED; never a trusted hand-list | E-10 | string | rides row 55 (registry executable form travels with the snapshot/guardrails family; the stale row-3 cite caught by row 64's mechanization — row 3 landed its pack slice and archived) | TODO |
| M-062 | A host may mirror the same checks in CI — one source of truth, CI never redefines them | M-5 | string | lands at row 14 | TODO |
| M-070 | The prototype fence is mechanical: a prod file referencing anything inside a prototype home turns the push gate RED; never a green push with such a reference | INV-17 | string | `test_prod_reference_fails`, `test_real_repo_passes`, `test_narrative_mention_passes` | BUILT |
| M-142 | The push gate scales to the diff's reach: a declared reach map (guardrails/check-push-reach.sh) decides gate b's scope mechanically from the diff's file list — prose-only diff (README/OVERVIEW/MIGRATION/LICENSE/docs research-reports-audit-decisions) stands the suite down by name, ANY other file (SPEC, matrix, architecture, queue, skills, tests, scripts — or anything new/unmapped) runs it whole, empty diff and missing base fall to full by construction; the cheap gates never scope; never a fast path for a tested document, never the script deciding by judgment | INV-45 | string | `TestGateReachMap` (the script RUN by deed on 3 fixture file-lists — red proven bare) + `test_push_gate_reach_law` | BUILT |
| M-145 | Gate hygiene: every BLOCKING gate on red emits one typed failure line {severity, code, message, fix} beside its human lines; every check declares blocking or advisory (advisory never flips the exit); artifact-rebuilding scripts validate all outputs before writing any; home guardrails README, applied by deed to ≥1 shipped gate (the prototype fence); the reach decider exempt by name (a verdict, not a defect); never a blocking red without its typed line on the converted gates | INV-47 | string | `TestGateHygieneContract` (`test_readme_states_contract` + `test_prototype_fence_emits_typed_failure` — the converted gate's real FAIL output parsed as JSON) | BUILT |
| M-154 | The CI mirror is live and honest: `.github/workflows/gates.yml` runs the SAME gate scripts as the local pre-push (a second net; full set — the reach map stays a local optimization; fetch-depth 0 + author-day TZ so gate (a) reads real history and the real day); the guardrails README carries the host guidance (copy, swap the test command, never redefine a check); never CI redefining a check, never the second net scoped by reach, never a false red on a machine-local pin in CI (noted + skipped there; strict locally) | M-5 | string | `TestCIMirror` (`test_workflow_ships_and_mirrors_the_gates` + `test_readme_carries_the_mirror_guidance` + `test_machine_local_pins_skip_in_ci_only`, red proven bare + by the first live run) + the real run watched on the landing push | BUILT |
| M-106 | Time is read off the clock: no repo file NAME, journal entry heading, or ledger date sits later than the current clock — a future-dated stamp turns the suite (and so the push walk) RED; prose quoting a past incident's wrong date stays legal; never an invented tomorrow shipped | INV-24 | string | `test_no_future_dated_stamps` (red proven by deed on a synthetic future-named file) | BUILT |
| M-110 | INV-24's second arm at pre-commit: an ADDED line carrying the ADJACENT stamp shape (today's date [~]time) with a time later than the commit moment goes red (commit clock the reference; CHECK_TODAY/CHECK_NOW only for tests); a past time today, any time on another day's date, and a line mixing today's date with quoted other-moment times (F9, the fence's own first live run) all stay green; never a same-day future stamp reaching a commit, never the fence blocking a quoted past | INV-24 | string | `test_future_time_today_goes_red` (with `test_past_time_today_stays_green` + `test_other_day_time_stays_green` — the script run by deed on a staged synthetic repo) | BUILT |
| M-123 | The chat face of the clock law — no fence can reach chat, so the arm is stated as law where the exchange shapes live (the sentence is carried by communicator rule 7): a human-facing timestamp — the [HH:MM] a reply leads with, any moment spoken to the human — is read off the clock at write time, never continued or extrapolated from an earlier stamp; quoting a past moment's recorded time stays legal; never an extrapolated stamp presented as the current time | INV-24 | string | `test_chat_timestamp_at_write_time` | BUILT |
| M-132 | The chat clock's mechanical hand: `scripts/clock-hook.sh` exists, is executable, and when run emits the CURRENT machine time (HH:MM within a minute of now, plus today's date) together with the read-off-this-clock instruction — the output names "[HH:MM]" and says "never a continued or extrapolated stamp"; installed per machine as a prompt hook (a copy under ~/.claude/hooks + a UserPromptSubmit entry in the host's settings); never an invented or cached time in its output, never a silent install on a machine the human didn't put it on | INV-24 | string | `test_output_carries_current_machine_time` (with `test_script_exists_and_executable` + `test_output_carries_the_law` — the script run by deed; red-proven on the absent script first) | BUILT |

### [node: snapshot [target]]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-063 | The snapshot is the last accepted baseline; it advances only at *landed* and only for DECLARED surfaces; never an undeclared advance | E-7 | string | machine lands at row 55 | TODO |
| M-064 | Adoption saves a baseline snapshot of current artifacts as the first diff base; never a first landing diffed against nothing | A-6 | string | lands at row 55 (with the machinery) | TODO |

### [node: design-sync]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-080 | Design-sync: optional machine — declared-scope footprint, supplements the render (which stays the gate authority), human-gated publish; never a sync without the human's word, never on without a recorded profile line | E-18 | string | machine's first real run = row 93's remainder; clause presence: `test_spec_states_founding_and_designsync` | TODO |
| M-088 | Design-sync WIRING is live: the `design-sync` switch off-by-default in base defaults, the channel line in communicator (cards after the gate, render stays authority) and in the pipeline's commit-and-show step; never a wired line contradicting the machine's [target] honesty | E-18 | string | `test_designsync_wiring` | BUILT |

---

## Coverage validation — walked 2026-07-05 at derivation; re-walked mechanically by `tests/test_traceability.py` at every run

- [x] Every spec anchor (invariant / state / transition) appears in ≥ 1 row — 70/70 (E-16 added 2026-07-05, rows 52–53), mechanized in `test_matrix_covers_every_anchor`.
- [x] Every architecture node has ≥ 1 block, and its negative-side rows exist — 12/12 blocks, every row carries a NEVER clause (`test_matrix_rows_have_level_and_negative_side`).
- [x] Every artifact-inventory entry is asserted shipped-and-non-empty (`test_artifact_inventory`) — the text-product rendered level (prover F6).
- [x] Every visibility / layout / colour / interaction fact sits at level ≥ `browser-computed` — vacuously true: the pack ships no browser surface (prover F6); the clause re-arms the day one exists.
- [x] No row cites a spec anchor or node that no longer exists — mechanized in `test_matrix_covers_every_anchor` (stale refs fail the suite; retirement, never deletion).

A fact with no row, or a row at a too-weak level, is a **derivation defect** — fix it here, before it is
a production bug.

---

*Add rows as the spec grows. Retire rows (mark RETIRED, do not delete) when a feature is removed — so the removal is auditable.*
