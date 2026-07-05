# live-spec — Architecture (v0.1, 2026-07-05)

How the pack is BUILT: the named nodes the spec's facts live in. Written from the proven SPEC v0.7
(record `docs/prover/2026-07-05-lost-layers.md`; the matrix cites v0.7.1 — the same proven spec after
two already-decided questions were reworded to their decided state, no rule delta), proven itself
with the architecture lens before the
test matrix was derived (record: see Prover record below). One node = one name = one responsibility —
the one-surface-one-name rule applied to structure. Kept current through SPEC v0.14.0 by assignment
(E-16 → host-contract; the doors landing 2026-07-05: T-12/INV-16 → build-pipeline, E-17 → base-rulebook,
INV-17 → guardrails, A-10 → attach; the facet-sweep landing 2026-07-05 evening: T-13/INV-18 →
spec-author, the canonical facet list's one home; the fences landing 2026-07-05 night: T-14/INV-19 →
spec-author (the fence-authoring rule); the intake-trio landing 2026-07-05 night: T-15 → build-pipeline
(intake rider), INV-20/INV-21 → spec-author (the delta's closing sentences); the founding/design-sync
landing 2026-07-05 night: B-2 → attach (deliberately apart from templates' B-1: templates own the SHAPES,
attach owns the WALK that asks — the founding ask fires at bootstrap and at orient); the work-kind
landing 2026-07-05 evening, session 8: T-16/INV-22 → build-pipeline (intake classification + the per-kind
step table are its domain) — assignment only, no node or seam change, no re-prove per this doc's own
rule; the row-57 landing 2026-07-05, session 9: E-21 → attach (the installer it already pinned),
E-22 → communicator (rule 10, the seam report → human already carried the page) — assignment only;
E-18 → NEW [target]
node design-sync — a node ADD is a
structure change, its architecture-lens re-prove rides tonight's milestone audit (row 84) — assignments + pins, no node or seam change, so no
re-prove per this doc's own rule); last full architecture-lens prove: v0.1, 2026-07-05. [E-14]

**What "pin" means here.** live-spec is a documentation-and-skills product: its shipped artifact IS the
text. A pin therefore points to the file:line where the node's responsibility is normatively stated or
carried — every pin below comes from a grep/read actually run on 2026-07-05, none from memory. Two nodes
are [target] (spec'd, not yet code); the template allows their pin cells to start empty.

**When this doc changes:** a large or surface-class wish updates it BEFORE the matrix is touched; a bug
or small wish only cites the existing node it lands in — or assigns an orphan fact to a fitting node
(recorded here; an assignment alone triggers no re-prove). Re-proven when structure changes, not on
every landing.

---

## Nodes

Every spec fact (anchor in SPEC.md's Formal index) is OWNED by exactly one node. The one deliberate
split: the wish walk `T-1..T-7` is one index row but two responsibilities — the walk itself (T-1..T-6,
build-pipeline) and the report step (T-7, communicator); both sides are named here and in the matrix.

| Node | Responsibility (one line) | Owns spec facts (anchors) | Pinned to (file:line) |
|---|---|---|---|
| base-rulebook | shared working rules stated once + package defaults + the settings ladder | E-12, E-13, INV-5, INV-9, INV-11, INV-13, INV-14, ACT-1, ACT-2, ACT-3, M-2, M-7, E-17 | `skills/live-spec-base/SKILL.md:19` (rules), `:52` (fence), `:95` (door + work-kind + prototype rules 15-16), `:131` (ladder), `:158` (defaults) |
| spec-author | authoring method for a living, use-case-first, prover-ready SPEC.md | E-4, C-1, T-13, INV-18, T-14, INV-19, INV-20, INV-21 | `skills/spec-author/SKILL.md:82` (spine), `:107` ([target] tag tripwire), `:119` (axes composition), `:163` (fences), `:178` (facet sweep — the canonical facet list) |
| product-prover | formal review of spec and architecture; executes the push-gate re-check | M-6 | `skills/product-prover/SKILL.md:161` (review modes), `.live-spec/profile.md:6` (gate cadence instance) |
| build-pipeline | the wish lifecycle: intake → classify → spec → prove → architecture → matrix → test → code → land | E-2, T-1..T-6, T-8, T-9, T-11, T-12, T-15, T-16, INV-1, INV-2, INV-3, INV-4, INV-12, INV-16, INV-22, E-14, E-15, INV-15, M-1 | `skills/build-pipeline/SKILL.md:32` (step zero: the door + work-kind), `:69` (the work-kind table — per-kind meanings' one home), `:93` (steps), `:204` (gates) |
| communicator | the human-facing exchange: reports, batched questions, decision pages | T-7 (the report step; the walk before it is build-pipeline's), E-22 | `skills/communicator/SKILL.md:33` (ten rules), `:102` (rule 10 — the decision page) |
| templates | the document shapes a host copies at bootstrap; the matrix's coverage checklist | E-3, E-5, INV-6, B-1 | `templates/TEST_MATRIX.template.md:43` (coverage validation), `templates/ROADMAP.template.md:1`, `templates/SPEC.template.md:58` (index) |
| attach | attaching the pack to a host: adoption phases, VCS gate, attic, skill install + version record | E-1, E-9, INV-7, INV-8, B-2, A-0, A-1, A-2, A-3, A-4, A-5, A-7, A-8, A-9, A-10, E-21 | `adopt/ADOPT.md:16` (VCS gate first), `:109` (unbacked-surface verdict), `:42` (attic), `:11` (attach record), `install.sh:2` (E-21 — the installer itself) |
| inbox | parallel-safe intake door for wishes born outside a live-spec session | E-11, T-10, INV-10 | `inbox/README.md:3` (one door, one NEW file), `:9` (file format), `:14` (commit rule) |
| host-contract | the recorded settings instances: this host's profile, the human's personal profile, and the thin loader that boots the personal layer | E-8, E-16 | `.live-spec/profile.md:1` (host), personal: `~/.claude/live-spec/profile.md` (symlink → playbook repo `personal/profile.md`, its git home — row 38 landed 2026-07-05), loader: `~/.claude/CLAUDE.md:1` (thin loader live — row 52 landed 2026-07-05) |
| package-docs | live-spec's own host instance (dogfood): spec, queue, journal, resume file, version, records, dev-machine skill sync | S-0, M-3, M-4, D-1, D-2, D-3, D-4, D-5, E-23 | `SPEC.md:1`, `ROADMAP.md:12` (queue table), `JOURNAL.md:1`, `VERSION:1`, `scripts/sync-skills.sh:1` (E-23) |
| guardrails [target] | mechanical pre-push checks + surface registry + CI mirror; first slice LIVE (the pack's own gates + opt-in fence, hooks installed), host-facing checks + registry + CI still [target] (ROADMAP rows 14, 55) | E-6, E-10, M-5, INV-17 | `guardrails/pre-push:1` (gates), `guardrails/check-prototype-fence.sh:1` (prototype fence, gate e), `guardrails/pre-commit:1` (commit fence), `guardrails/install.sh:1`, `tests/test_guardrails.py:1`; registry/CI: — |
| snapshot [target] | saved baseline of the last accepted run; declared-scope diff (ROADMAP row 55) | E-7, A-6 | — (spec'd, not yet code) |
| design-sync | optional machine, [target: machine; wiring live] — declared components of a landing synced to the team's design project, human-gated (ROADMAP row 93 — pack-side wiring landed session 8; the machine's first real run remains) | E-18 | wiring: `skills/live-spec-base/SKILL.md` (defaults table, `design-sync` row), `skills/communicator/SKILL.md` (rule 5 channel line), `skills/build-pipeline/SKILL.md` (step 9 sync line); machine: — |
| skill-evals | behaviour tests for the pack's own skills: per working skill one scenario, red proven bare, re-run at milestones (added session 8, row 94 — node add re-proven, record `docs/prover/2026-07-05-row94.md`) | E-19 | `evals/README.md:1` (the method + honest boundary), `evals/` (one file per working skill), `tests/test_traceability.py` (`test_skill_evals_present`, self-closing over skills/) |
| publish | the publish-quality gate: per-kind publication checklist (its one home) + the target-plugin seam; runs BEFORE the human's gate, never instead (added session 8, row 98 — node add re-proven, record `docs/prover/2026-07-05-row98.md`) | E-20 | `skills/publish/SKILL.md:1` (frontmatter + when it fires), the kind-checklist table and target-plugin sections in the same file |

## Seams

The places two nodes meet — named, because that is where composition bugs live. Each seam states what
crosses it and which side owns the format.

| Seam | Between | What crosses | Format owner |
|---|---|---|---|
| spec → prove | package-docs · product-prover | SPEC.md, whole document | spec-author (the shape both sides speak) |
| prove → record | product-prover · package-docs | prover record `docs/prover/YYYY-MM-DD[-suffix].md`, folded/rejected column | product-prover |
| pipeline → shapes | build-pipeline · templates | the document shapes the steps produce, incl. the coverage checklist | templates |
| outside wish → queue | inbox · package-docs | one wish file, harvested into a ROADMAP row at sweep | inbox (file naming law) |
| attach → host state | attach · host-contract | `.live-spec/` (profile, installed versions, checkpoints home) | attach |
| base → working skills | base-rulebook · the five working skills | the inherit pin (base name + version each skill opens with) | base-rulebook |
| ladder resolution | host-contract · base-rulebook | the resolved working contract communicator reads before every exchange | base-rulebook (ladder rule); host-contract (the lines) |
| report → human | communicator · the human | plain-language report · decision page + `<project>-decisions-<date>.json` | communicator |
| checks → push [target] | guardrails · build-pipeline | pre-push verdict (red blocks the push) | guardrails |
| baseline → checks [target] | snapshot · guardrails | declared-scope diff vs baseline | snapshot |
| sync → design project [target] | design-sync · the human | a landing's DECLARED components as rendered cards; every sync passes the human's publish gate (base rule 17, ACT-1) | design-sync |
| evals ↔ working skills | skill-evals · the five working skills | each scenario's green-criteria against the SKILL.md's promised behaviour | skill-evals |
| evals → milestone gate | skill-evals · package-docs | the re-run item in M-1's list + dated run records in docs/evals/ | package-docs (the gate list's home is the spec) |
| publish → the human's gate | publish · the human | the prepared deposit (README/listing/cards, checklist walked) handed to the publish/push gate — the gate stays the human's (base rules 12/17, M-6) | publish (the checklist); the human (the gate) |

## Prover record

| Date | Doc version proven | Record |
|---|---|---|
| 2026-07-05 | v0.1 | `docs/prover/2026-07-05-architecture.md` |
| 2026-07-05 night | v0.1 + design-sync node (structure change re-proven; 0.8.0 milestone pass 3) | `docs/audit/2026-07-05-night/composition-architecture.md` |

---

*Coverage rule (walked at matrix derivation): every spec anchor appears in some node's "owns" column —
an orphan fact means a missing node or a missing assignment; a node owning nothing traces to no spec
backing and is itself a finding. Mechanized in `tests/test_traceability.py`.*
