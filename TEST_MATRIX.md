# live-spec — Test Matrix (v0.1, 2026-07-05)

Derived from the proven SPEC v0.7.1 **through the proven ARCHITECTURE.md v0.1** (records:
`docs/prover/2026-07-05-lost-layers.md`, `docs/prover/2026-07-05-architecture.md`); kept current through
SPEC v0.10.0 by assignment + the 2026-07-05 audit folds + the doors landing (rows 70-71: five new anchors
T-12/INV-16/E-17/INV-17/A-10, rows M-067..M-071 below; headers re-pin at each milestone per M-1). Rows are organized
**architecture node × spec fact**: every index anchor sits in ≥ 1 row under its owning node, every row
pins a test level, and the derivation closes with the coverage validation at the bottom — walked, and
mechanized in `tests/test_traceability.py` so it re-walks at every run, not once. [E-15]

**Test levels, adapted honestly to a text product** (recorded interpretation — prover record F6):
live-spec ships documents and skills, no browser surface, so no fact here requires ≥ `browser-computed`.
The "rendered level" for a text artifact is a `string` assertion **against the SHIPPED file on disk**
(never a source fragment or a memory of it). Two kinds of fact get two honest treatments:
- **structural facts** (a doc exists, carries its sections, cites its law) — level `string`, testable now;
- **behavioral facts** (a discipline holds during work: one landing at a time over time, attic on a real
  adopt run) — the row names its future mechanical owner (guardrails row 3, snapshot row 55, the next
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
| Adoption procedure | `adopt/ADOPT.md` | shipped text | `test_artifact_inventory` |
| Installer | `install.sh` | shipped script | `test_artifact_inventory` |
| Migration note (rename) | `MIGRATION.md` | shipped text | `test_artifact_inventory` |
| Front door | `README.md` | shipped text | `test_artifact_inventory` |
| The one-page map | `OVERVIEW.md` | shipped text | `test_artifact_inventory` |
| Inbox door + law | `inbox/README.md` | shipped text | `test_artifact_inventory` |
| Guardrails scaffold text | `scaffold/guardrails/README.md` | shipped text | `test_artifact_inventory` |
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

---

## Matrix rows — grouped by architecture node

### [node: base-rulebook]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-001 | Every working skill opens with the base-inherit pin (base name + the base version it was written against); never a working skill without its pin | E-12 | string | `test_skills_inherit_base_pin` | BUILT |
| M-002 | Settings live in four nested scopes and resolve narrowest-out: session > host > personal > package default, broader values inherited until overridden on the human's word; an unrecognized profile line is ignored ALOUD, never silently dropped and never an error | E-13 | string | `test_settings_ladder_documented` (structural clause: ladder + resolution order stated in the base skill); behavioral resolution: milestone audit (M-1) + guardrails row 3 | BUILT |
| M-003 | Every choice not in the wish is asked or recorded-and-surfaced; never decided-and-buried | INV-5 | string | snapshot declared-scope diff (row 55) — the mechanical fence | TODO |
| M-004 | Proactivity mode and trust are written only on the human's word; the agent never raises its own level | INV-9 | string | milestone audit (M-1) | TODO |
| M-005 | Before every write and commit: re-check `git status` + HEAD; never write over changes you did not make | INV-11 | string | `guardrails/pre-commit` (opt-in fence): `test_armed_stale_head_blocks_commit`, `test_unarmed_fence_passes_silently` | BUILT |
| M-006 | A shared rule has exactly one normative home (the base skill); never two full statements | INV-13 | string | milestone compaction pass (M-1) | TODO |
| M-007 | An override exists only as a written profile line + a dated journal note in the home it governs; never an unwritten divergence | INV-14 | string | `test_host_profile_recorded_override` | BUILT |
| M-008 | The human owns taste, design, irreversible calls, push gates, domain wording, their contract; never the agent | ACT-1 | string | process — every decision page + milestone gate-list (M-1) | TODO |
| M-009 | The senior agent owns judgment (spec deltas, levels, triage); never delegated to a worker | ACT-2 | string | process — journal audit at milestones (M-1) | TODO |
| M-010 | Workers run mechanical execution with persistent checkpoints in `.live-spec/checkpoints/`; never in a system temp dir | ACT-3 | string | router design (row 56) makes it mechanical | TODO |
| M-011 | A safe breakpoint = LIVE STATE replaced (one block, never stacked) + dated journal entry + commit | M-2 | string | `test_next_steps_live_state` (shape; the discipline audits at M-1) | BUILT |
| M-012 | Versions have named homes: VERSION file, a version line under `metadata:` in its SKILL.md frontmatter, host record; never scattered or absent | M-7 | string | `test_version_homes` | BUILT |
| M-066 | The base skill states each shared rule once and no working skill restates one normatively; never a second normative home for a shared rule | E-12 | string | milestone compaction pass (M-1) | TODO |
| M-069 | A prototype lives fenced (own home) with a PROTOTYPE label per artifact kind, opened only by the assigned senior, shown only as a sketch; never wired into or presented as the product | E-17 | string | `test_base_rules_door_and_prototype`, `test_working_skills_carry_the_door` | BUILT |

### [node: spec-author]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-013 | The spec is the living truth, use-case-first, one surface = one name; never two synced copies | E-4 | string | prover FULL pass at milestones (M-1) | TODO |
| M-014 | Every stateful surface composes across the canonical axes + the provenance axis at adoption; never only its own axis | C-1 | string | prover FULL pass at milestones (M-1) | TODO |
| M-072 | A feature-doored spec-delta walks the standard-facet sweep (phone/narrow · touch-vs-hover · empty/error/loading · accessibility · performance envelope); the canonical list has ONE home (spec-author); a mid-work re-door re-runs the sweep; a fenced prototype is never swept | T-13 | string | `test_spec_states_facet_sweep`, `test_skills_carry_facet_sweep` | BUILT |
| M-077 | Every feature's delta closes with a non-goals sentence, ALWAYS written ("nothing deliberately left out this time" is valid); a scope-narrowing non-goal rides the batched report; never a missing sentence passing as fine | INV-20 | string | `test_spec_states_intake_trio`, `test_skills_carry_intake_trio` | BUILT |
| M-078 | Every feature states one success measure, decided or `[default]`-tagged (provenance only — no derived test row while the reading machinery is [target]); binds forward, adopted features owe theirs at first touch (A-3); never a measure claimed as machine-checked before the machinery lands | INV-21 | string | `test_spec_states_intake_trio`, `test_skills_carry_intake_trio` | BUILT |
| M-074 | A feature-delta touching a live surface opens with regression fences BEFORE the facet sweep; each fence cites the clause it guards; a fact is fenced xor re-authored; a prototype fences nothing; never a live surface touched without its fences authored first | T-14 | string | `test_spec_states_regression_fences`, `test_skills_carry_regression_fences` | BUILT |
| M-075 | A fence earns NO new matrix row — it discharges through the cited clause's never-side; an unwritten or unverified promise reconciles first (A-3) and becomes its own fact; fences named by anchor in the wish's row | INV-19 | string | `test_spec_states_regression_fences`, `test_skills_carry_regression_fences` | BUILT |
| M-073 | Every facet ends as a spec sentence — decided, or `[default]`-tagged + reported as a plain-words tradeoff, batched; adopted/promoted surfaces reconcile defaults from shipped truth; never a facet silently absent | INV-18 | string | `test_spec_states_facet_sweep`, `test_skills_carry_facet_sweep` | BUILT |

### [node: product-prover]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-079 | Founding questions asked or profile-read at bootstrap AND owed at adopt orient (A-1 pointer); personal-vs-reusable first; never a founding answer inferred from examples | B-2 | string | `test_spec_states_founding_and_designsync` | BUILT |
| M-015 | Every live-spec push is preceded, same session, by fence + a whole-spec re-check recorded in `docs/prover/`; never a push without its record | M-6 | string | `guardrails/pre-push` gate a: `test_real_repo_passes`, `test_missing_record_fails` | BUILT |

### [node: build-pipeline]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-076 | Appetite: optional rider on size in the ONE intake line; bends scope only — a trim proceeds on the recommended option and is surfaced in the batched report; never lane order moved by appetite, never a silent trim | T-15 | string | `test_spec_states_intake_trio`, `test_skills_carry_intake_trio` | BUILT |
| M-016 | A wish is one request in plain words, any size, any moment; never lost for being informal | E-2 | string | process — inbox + intake discipline; milestone re-listing (M-1) | TODO |
| M-017 | The wish walks arrived → classified → spec-delta → validated → queued → in-work → landed; never skipping the spec-delta or validation step | T-1..T-6 | string | guardrails row 3 (bounds check: behaviour traces to spec) | TODO |
| M-018 | A wish may exit declined / deferred / superseded — the row stays in the table; never deleted | T-8 | string | queue archive rule (row 30) + milestone audit | TODO |
| M-019 | A bug preempts: the wish parks with a checkpoint, nothing red is committed; never two wishes parked | T-9 | string | process — next real preemption journals it; guardrails row 3 | TODO |
| M-020 | Priority bends the lane visibly: critical heads the line, a quick win may bubble once, then the queue head; never a silent jump and never starvation | T-11 | string | queue audit at milestones (M-1) | TODO |
| M-021 | No wish is ever lost: the row exists the minute it is spoken; never an intake that leaves no trace | INV-1 | string | milestone re-listing of gates + inbox files (M-1) | TODO |
| M-022 | One landing at a time; never two rows in-work at once | INV-2 | string | `test_roadmap_single_in_work` | BUILT |
| M-023 | Every landing cites its wish row in commit or journal; never an unexplained change | INV-3 | string | pre-push hook (guardrails row 3) | TODO |
| M-024 | A pending human question never stops the lane — work proceeds on the recommended option, marked in the row | INV-4 | string | queue audit at milestones (M-1) | TODO |
| M-025 | Ambiguous size or priority is asked at intake, never guessed; the class column speaks the four-word vocabulary + priority marks only | INV-12 | string | `test_roadmap_class_vocabulary` | BUILT |
| M-026 | ARCHITECTURE.md exists, every node pinned to a real file:line, proven before the matrix derives; never an unproven architecture under a matrix | E-14 | string | `test_architecture_owns_every_anchor_once`, `test_architecture_no_orphan_nodes` | BUILT |
| M-027 | The matrix is DERIVED node × fact with the coverage validation walked; never just filled | E-15 | string | `test_matrix_covers_every_anchor`, `test_matrix_blocks_match_architecture_nodes` | BUILT |
| M-028 | No wish lands whose facts lack an owning node and a right-level matrix row (binds from this landing, never retroactively) | INV-15 | string | `test_matrix_covers_every_anchor` (re-runs at every commit) | BUILT |
| M-029 | The milestone gate runs: full re-prove + matrix audit + composition check + compaction + gate/inbox re-listing + index re-check; never a MINOR without it | M-1 | string | next MINOR walks it; journal records the walk | TODO |
| M-067 | The door is named before any code: every wish states size · priority · door in ONE intake line; never code before the door is said | T-12 | string | `test_spec_states_door_procedure`, `test_working_skills_carry_the_door` | BUILT |
| M-068 | Feature tripwires are hard and ordered (surface/state/interaction/[target]/unbacked behaviour ⇒ feature); the verdict outranks a casual label, a re-doored wish takes no preemption, the door re-fires mid-work; never a wish hand-built past the pipeline for sounding small | INV-16 | string | `test_spec_states_door_procedure`, `test_base_rules_door_and_prototype` | BUILT |

### [node: communicator]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-030 | A landing is reported in one plain-language line (position · what landed · what remains); never a report that only points at internal rows | T-7 | string | process — communicator rules 8/9; milestone audit | TODO |

### [node: templates]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-031 | The queue is one table: wish · class · status · acceptance, one row per wish; never a second scale or format | E-3 | string | `test_roadmap_class_vocabulary` (columns + vocabulary) | BUILT |
| M-032 | The matrix shape: inventory + node blocks + coverage validation; never a bare row bucket | E-5 | string | `test_matrix_blocks_match_architecture_nodes` | BUILT |
| M-033 | Every matrix row states the DO and the NEVER side; never a row without its regression fence | INV-6 | string | `test_matrix_rows_have_level_and_negative_side` | BUILT |
| M-034 | Bootstrap = copy the six templates → version-control gate → first wish through the pipeline; never landing before the gate | B-1 | string | `test_templates_ship` (the set exists; gate behavior = next bootstrap run) | BUILT |

### [node: attach]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-035 | The host owns its docs and a `.live-spec/` folder (profile, checkpoints, installed versions); never pack state scattered into host folders | E-1 | string | `test_host_profile_recorded_override` (dogfood instance) | BUILT |
| M-036 | The attic archives superseded host files with a manifest line; never deletion | E-9 | string | `test_adopt_phases_cite_spec` (procedure text; behavior = next adopt run) | BUILT |
| M-037 | No adopt or rework run deletes a host file; authored content never bypasses the attic | INV-7 | string | next real adopt run journals it; guardrails row 3 long-term | TODO |
| M-038 | No landing into an unversioned host: git + (remote exists OR explicitly declined, recorded); never a mere recommendation | INV-8 | string | next bootstrap/adopt run journals the gate outcome | TODO |
| M-039 | Adoption codes name meanings, not order; the VCS gate runs FIRST — never an irreversible touch before it | A-0 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-040 | Orient: every existing document is read before anything is touched; never a blank-slate assumption | A-1 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-041 | Inventory: code, surfaces (seeding the registry), docs — with owners; never an unlisted surface | A-2 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-042 | Existing docs re-engineer into live-spec shapes, claims marked unverified until reconciled; never trusted unreconciled | A-3 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-043 | Superseded files move to the attic during adoption; never silently replaced | A-4 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-044 | The version-control gate: init, .gitignore, pristine baseline, remote settled as a named deliverable — never closed on a mere recommendation | A-5 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-045 | On any version change the agent re-reads the changed SKILL.md + journals old → new; re-stats at every breakpoint; never coasts on a stale copy | A-7 | string | `test_adopt_phases_cite_spec` (text; behavior audits at M-1) | BUILT |
| M-046 | Adopt working artifacts live tracked in `.live-spec/adopt/`; never scattered into the host's own folders | A-8 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-047 | A cruft sweep is offered, listed, human-gated, regenerable-only; never silent and never authored content | A-9 | string | `test_adopt_phases_cite_spec` | BUILT |
| M-071 | Adoption gives every unbacked live surface a human verdict — promote / quarantine / attic; never an unbacked surface silently registered as product | A-10 | string | `test_adopt_phases_cite_spec` (A-10 citation + verdict wording) | BUILT |

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
| M-065 | The personal layer has ONE home (the profile); the global instruction file is a thin loader carrying only the pointer + bootstrap lines (their one home — never restated in the profile); a session line is never written by the agent; the migration fork never writes a foreign repo | E-16 | string | row 52 migration landing: diff-proven fork map + loader shown to the human before flipping | TODO |

### [node: package-docs]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-052 | Shipped vs target is marked honestly; every [target] machine is owned by a queue row; never a claimed-shipped target | S-0 | string | milestone audit (caught by hand in prover F1 this pass) | TODO |
| M-053 | The queue and the spec carry dated versions; never an undated truth | M-3 | string | `test_roadmap_header_dated` | BUILT |
| M-054 | live-spec eats its own cooking — this repo works by its own spec and queue; the pack's own push gates run mechanically on the installed hooks; never a claim of mechanical enforcement beyond what is actually wired | M-4 | string | `test_hooks_and_scripts_exist_and_executable` (+ `guardrails/install.sh` run for real, journaled) | BUILT |
| M-055 | Attic layout choice stays open with a named revisit trigger; never silently resolved | D-1 | string | `test_spec_decide_markers_match_open` | BUILT |
| M-056 | Tier-routing override choice stays open (closes via row 56); never silently resolved | D-2 | string | `test_spec_decide_markers_match_open` | BUILT |
| M-057 | Snapshot retention choice stays open (closes via row 55); never silently resolved | D-3 | string | `test_spec_decide_markers_match_open` | BUILT |
| M-058 | D-4 records its decided state (package-is-source, row 51 executes); never re-litigated silently | D-4 | string | `test_spec_decide_markers_match_open` | BUILT |
| M-059 | D-5 records its decided state (all-into-profile, rows 52–54 execute); never re-litigated silently | D-5 | string | `test_spec_decide_markers_match_open` | BUILT |

### [node: guardrails [target]]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-060 | The guardrails run on the pre-push hook: completeness, tests-present, behaviour-traces-to-spec, declared-scope diff; never a red push | E-6 | string | first slice BUILT (pack gates: prover record · green suite · anchor ownership · matrix coverage — `guardrails/pre-push` + `test_guardrails.py`); the four host-facing checks await the surface registry + snapshot (rows 55+) | TODO |
| M-061 | The surface registry is self-closing: a rendered-but-unregistered surface is RED; never a trusted hand-list | E-10 | string | machine lands at row 3 | TODO |
| M-062 | A host may mirror the same checks in CI — one source of truth, CI never redefines them | M-5 | string | lands at row 14 | TODO |
| M-070 | The prototype fence is mechanical: a prod file referencing anything inside a prototype home turns the push gate RED; never a green push with such a reference | INV-17 | string | `test_prod_reference_fails`, `test_real_repo_passes`, `test_narrative_mention_passes` | BUILT |

### [node: snapshot [target]]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-063 | The snapshot is the last accepted baseline; it advances only at *landed* and only for DECLARED surfaces; never an undeclared advance | E-7 | string | machine lands at row 55 | TODO |
| M-064 | Adoption saves a baseline snapshot of current artifacts as the first diff base; never a first landing diffed against nothing | A-6 | string | lands at row 55 (with the machinery) | TODO |

### [node: design-sync [target]]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-080 | Design-sync: optional machine — declared-scope footprint, supplements the render (which stays the gate authority), human-gated publish; never a sync without the human's word, never on without a recorded profile line | E-18 | string | machine lands at row 93; clause presence: `test_spec_states_founding_and_designsync` | BUILT |

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
