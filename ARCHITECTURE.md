# live-spec — Architecture (v0.2.1, 2026-07-09)

This is how live-spec is built: the named nodes that the spec's facts live in. One node carries one name
and one responsibility — the one-surface-one-name rule, applied to structure. The doc was itself proven
with the architecture lens before the test matrix was derived (see the Prover record below).

The agent keeps this doc up to date by assignment. When a wish lands, its new facts go to the node that already
owns their kind, and the pin is refreshed. A fact with no home yet goes to the node that fits. A large or
surface-class wish updates the doc before the matrix is touched; a bug or small wish just cites the node it
lands in. An assignment changes no structure and triggers no re-prove — only a new node or a new seam
does, and only then is the doc re-proved. The landing-by-landing history lives in JOURNAL.md; this doc
states the structure as it stands today. [E-14]

**What "pin" means here.** live-spec is a documentation-and-skills product: its shipped artifact is the
text. So a pin points to the `file:line` where a node's responsibility is stated or carried. Every pin
below comes from a grep or read actually run, never from memory. Two nodes are marked [target] —
specified, with their code still ahead — and the template lets their pin cells stay empty until the code lands.

---

## Nodes

Every spec fact (anchor in PRODUCT_SPEC.md's Formal index) is OWNED by exactly one node. The one deliberate
split: the wish walk `T-1..T-7` is one index row but two responsibilities — the walk itself (T-1..T-6,
build-pipeline) and the report step (T-7, communicator); both sides are named here and in the matrix.

| Node | Responsibility (one line) | Owns spec facts (anchors) | Pinned to (file:line) |
|---|---|---|---|
| base-rulebook | shared working rules stated once + package defaults + the settings ladder | E-12, E-13, INV-5, INV-9, INV-11, INV-13, INV-14, INV-23, INV-56, INV-65, T-19, INV-40, ACT-1, ACT-2, ACT-3, M-2, M-7, E-17 | `skills/live-spec-base/SKILL.md:17` (rules), `:52` (fence), `:95` (door + work-kind + prototype rules 15-16), `:132` (rule 19, INV-23 — the workshop-noise law), `:150` (rule 20, INV-65 — skill search at setup and struggle), `:152` (ladder), `:179` (defaults incl. `budget.pressure` — the economy ladder's setting; the rungs' one home is the SPEC's economy-ladder section) |
| spec-author | authoring method for a living, use-case-first, prover-ready PRODUCT_SPEC.md | E-4, C-1, T-13, INV-18, INV-29, INV-50, T-14, INV-19, INV-20, INV-21; also carries the prototype-norm pointer's format sentence (`norm: <path>`, frozen copy in `docs/norms/`) — wiring, the invariant's owner is build-pipeline | `skills/spec-author/SKILL.md:109` (spine), `:134` ([target] tag tripwire), `:160` (axes composition), `:200` (fences), `:216` (facet sweep — the canonical facet list) |
| product-prover | formal review of spec and architecture; executes the push-gate re-check | M-6, INV-61, INV-72; also carries the entry-symmetry lens (the law's owner is spec-author) and the prototype-norm lens (prototype-born clause without pointer / text contradicting its artifact = finding) — wiring, the invariant's owner is build-pipeline | `skills/product-prover/SKILL.md:161` (review modes), `skills/product-prover/SKILL.md:271` (unwritten-seam hunt — the stress-lens family, INV-72), `.live-spec/profile.md:6` (gate cadence instance) |
| build-pipeline | the wish lifecycle: intake → classify → spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show → landed | E-2, T-1..T-6, T-8, T-9, T-11, T-12, T-15, T-16, T-17, T-18, INV-1, INV-2, INV-3, INV-4, INV-12, INV-16, INV-22, INV-26, INV-30, INV-31, INV-33, INV-37, INV-39, INV-41, INV-43, INV-46, INV-49, INV-53, INV-54, INV-55, INV-62, INV-63, INV-69, INV-70, E-14, E-15, INV-15, M-1 | `skills/build-pipeline/SKILL.md:41` (step zero: the door + work-kind), `:31` (the craft ladder — step→craft one home), `:83` (the work-kind table — per-kind meanings' one home), `:107` (steps), `:233` (gates) |
| communicator | the human-facing exchange: reports, batched questions, decision pages, done-claim answers, the capture echo + departures board, the feature map on demand, the pre-report walk, working narration | T-7 (the report step; the walk before it is build-pipeline's), E-22, INV-25, INV-27, INV-28, INV-32, INV-34, INV-35, INV-38, INV-42, INV-51, INV-52, INV-57, INV-58, INV-59, INV-60, INV-64, INV-71; also carries the clock law's chat-arm sentence — a wiring pin, the invariant's owner is the guardrails node, INV-67  | `skills/communicator/SKILL.md:33` (the rules), `:112` (rule 10 — the decision page), `:140` (rule 11 — the evidence walk), `:102` (rule 9 — the outcome-leads line shape), `:162` (the pre-report walk), `:82` (rule 7 — the chat-arm clock sentence) |
| templates | the document shapes a host copies at bootstrap; the matrix's coverage checklist | E-3, E-5, INV-6, B-1, E-24, INV-48, E-26 | `templates/TEST_MATRIX.template.md:43` (coverage validation), `templates/ROADMAP.template.md:1`, `templates/PRODUCT_SPEC.template.md:58` (index), `templates/PROBLEMS.template.md:1` (E-24 — the ledger's shape) |
| attach | attaching the pack to a host: adoption phases, VCS gate, attic, skill install + version record + the pack update check, the who-am-I-working-with step | E-1, E-9, INV-7, INV-8, B-2, B-3, INV-36, A-0, A-1, A-2, A-3, A-4, A-5, A-7, A-8, A-9, A-10, E-21, E-25 | `adopt/ADOPT.md:16` (VCS gate first), `:109` (unbacked-surface verdict), `:42` (attic), `:11` (attach record), `:50` (B-3 — who am I working with, first step of orient), `install.sh:2` (E-21 — the installer itself), `scripts/check-pack-update.sh:1` (E-25 — the update check) |
| inbox | parallel-safe intake door for wishes born outside a live-spec session | E-11, T-10, INV-10 | `inbox/README.md:3` (one door, one NEW file), `:9` (file format), `:14` (commit rule) |
| host-contract | the recorded settings instances: this host's profile, the human's personal profile, and the thin loader that boots the personal layer | E-8, E-16 | `.live-spec/profile.md:1` (host), personal: `~/.claude/live-spec/profile.md` (symlink → playbook repo `personal/profile.md`, its git home — row 38 landed 2026-07-05), loader: `~/.claude/CLAUDE.md:1` (thin loader live — row 52 landed 2026-07-05) |
| package-docs | live-spec's own host instance (dogfood): spec, queue, journal, resume file, version, records, dev-machine skill sync, its own problem ledger | S-0, M-3, M-4, D-1, D-2, D-3, D-4, D-5, E-23 | `PRODUCT_SPEC.md:1`, `ROADMAP.md:12` (queue table), `JOURNAL.md:1`, `VERSION:1`, `scripts/sync-skills.sh:1` (E-23), `.live-spec/PROBLEMS.md:1` (E-24's dogfood instance; anchor owned by templates) |
| guardrails [target] | mechanical pre-push checks + surface registry + CI mirror; the pack's own gates + opt-in fence LIVE (hooks installed), the chat clock's mechanical hand, and the CI mirror LIVE (row 14 — `.github/workflows/gates.yml`, the same scripts as a second net); host-facing checks + registry still [target] (row 55) | E-6, E-10, M-5, INV-17, INV-24, INV-45, INV-47 (the chat arm's sentence is carried by communicator as wiring; ownership stays elsewhere), INV-66 | `guardrails/pre-push:1` (gates), `guardrails/check-push-reach.sh:1` (the reach map's deciding script, gate b's scope), `guardrails/check-prototype-fence.sh:1` (prototype fence, gate e), `guardrails/pre-commit:1` (commit fence), `guardrails/install.sh:1`, `scripts/clock-hook.sh:1` (the chat clock's hand), `tests/test_guardrails.py:1`, `.github/workflows/gates.yml:1` (the CI mirror); registry: — |
| snapshot [target] | saved baseline of the last accepted run; declared-scope diff (ROADMAP row 55) | E-7, A-6 | — (spec'd; code still ahead) |
| design-sync | optional machine, [target: machine; wiring live] — declared components of a landing synced to the team's design project, human-gated (ROADMAP row 93 — pack-side wiring landed session 8; the machine's first real run remains) | E-18 | wiring: `skills/live-spec-base/SKILL.md` (defaults table, `design-sync` row), `skills/communicator/SKILL.md` (rule 5 channel line), `skills/build-pipeline/SKILL.md` (step 9 sync line); machine: — |
| skill-evals | behaviour tests for the pack's own skills: per working skill one scenario, red proven bare, re-run at milestones (added session 8, row 94 — node add re-proven, record `docs/prover/2026-07-05-row94.md`) | E-19 | `evals/README.md:1` (the method + honest boundary), `evals/` (one file per working skill), `tests/test_traceability.py` (`test_skill_evals_present`, self-closing over skills/) |
| publish | the publish-quality gate: per-kind publication checklist (its one home) + the target-plugin seam; runs BEFORE the human's gate, never instead (added session 8, row 98 — node add re-proven, record `docs/prover/2026-07-05-row98.md`) | E-20, INV-44 | `skills/publish/SKILL.md:1` (frontmatter + when it fires), the kind-checklist table and target-plugin sections in the same file |
| test-author | the test method's one home: derives TEST_MATRIX.md from the proven spec through the proven architecture and writes the tests — the level ladder, real-artifact assertions, red-first proof, the pinned skip-set, traceability as a standing test (added session 23, row 163 — node add re-proven, record `docs/prover/2026-07-07-row163.md`) | E-27 | `skills/test-author/SKILL.md:1` (name + description), the level-ladder table and the two step sections in the same file |
| feedback-intake | the intake half of the exchange: receives anything handed back through three channels, routes each item to the home its law owns, keeps the feedback ledger's shape, echoes every arrival (added session 24, row 47 — node add re-proven, record `docs/prover/2026-07-07-row47.md`) | E-28, T-20, INV-68 | `skills/feedback-intake/SKILL.md:1` (frontmatter + when it fires), the routing table and ledger-shape sections in the same file |

## Seams

The places two nodes meet — named, because that is where composition bugs live. Each seam states what
crosses it and which side owns the format.

| Seam | Between | What crosses | Format owner |
|---|---|---|---|
| spec → prove | package-docs · product-prover | PRODUCT_SPEC.md, whole document | spec-author (the shape both sides speak) |
| prove → record | product-prover · package-docs | prover record `docs/prover/YYYY-MM-DD[-suffix].md`, folded/rejected column | product-prover |
| pipeline → shapes | build-pipeline · templates | the document shapes the steps produce, incl. the coverage checklist | templates |
| outside item → its home | inbox · package-docs | one item file (wish or feedback), harvested at sweep into the home its route owns — a ROADMAP row, or by the routing law (T-20) | inbox (file naming law); feedback-intake (the routing) |
| handed-in item → its home | feedback-intake · package-docs | the routed landing: a wish row, a ledger line, a harvested answer — the route named in the echo | feedback-intake (the routing law) |
| feedback ↔ the echo | feedback-intake · communicator | the one echo per received item (a wish-shaped item keeps the wish echo, INV-27) | communicator (the echo's shape) |
| attach → host state | attach · host-contract | `.live-spec/` (profile, installed versions, checkpoints home) | attach |
| base → working skills | base-rulebook · the working skills | the inherit pin (base name + version each skill opens with) | base-rulebook |
| ladder resolution | host-contract · base-rulebook | the resolved working contract communicator reads before every exchange | base-rulebook (ladder rule); host-contract (the lines) |
| report → human | communicator · the human | plain-language report · decision page + `<project>-decisions-<date>.json` | communicator |
| checks → push [target] | guardrails · build-pipeline | pre-push verdict (red blocks the push) | guardrails |
| baseline → checks [target] | snapshot · guardrails | declared-scope diff vs baseline | snapshot |
| sync → design project [target] | design-sync · the human | a landing's DECLARED components as rendered cards; every sync passes the human's publish gate (base rule 17, ACT-1) | design-sync |
| evals ↔ working skills | skill-evals · the working skills | each scenario's green-criteria against the SKILL.md's promised behaviour | skill-evals |
| evals → milestone gate | skill-evals · package-docs | the re-run item in M-1's list + dated run records in docs/evals/ | package-docs (the gate list's home is the spec) |
| publish → the human's gate | publish · the human | the prepared deposit (README/listing/cards, checklist walked) handed to the publish/push gate — the gate stays the human's (base rules 12/17, M-6) | publish (the checklist); the human (the gate) |
| matrix & tests derivation | build-pipeline · test-author | the proven spec + architecture in; TEST_MATRIX.md + owning tests out (steps 5–6 invoke the skill the way steps 1–2 invoke theirs) | test-author (the ladder and the assertion shapes) |

## Prover record

| Date | Doc version proven | Record |
|---|---|---|
| 2026-07-05 | v0.1 | `docs/prover/2026-07-05-architecture.md` |
| 2026-07-05 night | v0.1 + design-sync node (structure change re-proven; 0.8.0 milestone pass 3) | `docs/audit/2026-07-05-night/composition-architecture.md` |
| 2026-07-05 | + skill-evals node (row 94) | `docs/prover/2026-07-05-row94.md` |
| 2026-07-05 | + publish node (row 98) | `docs/prover/2026-07-05-row98.md` |
| 2026-07-07 | + test-author node (row 163) | `docs/prover/2026-07-07-row163.md` |
| 2026-07-07 | + feedback-intake node (row 47) | `docs/prover/2026-07-07-row47.md` |
| 2026-07-09 | v0.2 — FULL re-prove of the whole spec for the pre-push M-6 gate (sessions 27–29 body) | `docs/prover/2026-07-09-full-reprove-session29-body.md` |

---

*Coverage rule (walked at matrix derivation): every spec anchor appears in some node's "owns" column. An
orphan fact means a missing node or a missing assignment. A node that owns nothing has no spec backing,
and that is itself a finding. Mechanized in `tests/test_traceability.py`.*
