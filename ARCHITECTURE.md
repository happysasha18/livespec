# live-spec — Architecture

Derived from PRODUCT_SPEC.md; the package version has one home, the VERSION file, and is not pinned
here where it would read stale (row 265). Last reconciled with the spec: 2026-07-12.

This is how live-spec is built: the named nodes that the spec's facts live in. One node carries one name
and one responsibility — the one-surface-one-name rule, applied to structure. The doc was itself proven
with the architecture lens before the test matrix was derived (see the Prover record below). In the
field's vocabulary the nodes are the C4 model's building blocks and the arc42 building-block view (§5); the
seams below are their relationships, the runtime view is arc42's §6, the placement view its
deployment view (§7), and the quality budgets are arc42 quality scenarios (§10).

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

## The shape at a glance

live-spec is a skill pack: eight skills (text a model reads) plus templates, guardrails, and its own
dogfood documents, all in one repo. Everything EXECUTES inside an agent session on the host machine;
the repo is the source of truth, the installed copies under `~/.claude/skills/` are what a session
actually loads, git hooks and CI re-run the same gates, and the human reads rendered pages in a
browser. No server, no runtime of its own.

## Nodes

Every spec fact (anchor in PRODUCT_SPEC.md's Formal index) is OWNED by exactly one node. The one deliberate
split: the wish walk `T-1..T-7` is one index row but two responsibilities — the walk itself (T-1..T-6,
build-pipeline) and the report step (T-7, communicator); both sides are named here and in the matrix.

| Node | Responsibility (one line) | Owns spec facts (anchors) | Pinned to (file:line) |
|---|---|---|---|
| base-rulebook | shared working rules stated once + package defaults + the settings ladder | E-12, E-13, INV-5, INV-9, INV-11, INV-13, INV-14, INV-23, INV-56, INV-65, INV-76, INV-84, INV-98, INV-108, T-19, INV-40, ACT-1, ACT-2, ACT-3, M-2, M-7, E-17, INV-105, INV-107, INV-117 | `skills/live-spec-base/SKILL.md:17` (rules), `:52` (fence + rule 6's closing half, INV-107), `:95` (door + work-kind + prototype rules 15-16), `:132` (rule 19, INV-23 — the workshop-noise law), `:150` (rule 20, INV-65 — skill search at setup and struggle), `:166` (rule 21, INV-84 — the clean-writer road), `:178` (rule 22, INV-98 — the convergence principle), `:191` (rule 23, INV-108 — the live-channel law), `:152` (ladder), `:179` (defaults incl. `budget.pressure` — the economy ladder's setting; the rungs' one home is the SPEC's economy-ladder section) |
| spec-author | authoring method for a living, use-case-first, prover-ready PRODUCT_SPEC.md | E-4, C-1, T-13, INV-18, INV-29, INV-50, T-14, INV-19, INV-20, INV-21, INV-101, INV-118, INV-126, INV-127; also carries the prototype-norm pointer's format sentence (`norm: <path>`, frozen copy in `docs/norms/`) — wiring, the invariant's owner is build-pipeline | `skills/spec-author/SKILL.md:109` (spine), `:134` ([target] tag tripwire), `:160` (axes composition), `:200` (fences), `:216` (facet sweep — the canonical facet list) |
| product-prover | formal review of spec and architecture; executes the push-gate re-check | M-6, INV-61, INV-72, INV-114, INV-125; also carries the entry-symmetry lens (the law's owner is spec-author), the declared-laws station (the law's owner is spec-author), and the prototype-norm lens (prototype-born clause without pointer / text contradicting its artifact = finding) — wiring, the invariant's owner is build-pipeline | `skills/product-prover/SKILL.md:161` (review modes), `skills/product-prover/SKILL.md:271` (unwritten-seam hunt — the stress-lens family, INV-72), `.live-spec/profile.md:6` (gate cadence instance), `skills/product-prover/SKILL.md:168` (restructure-merge gate — INV-114 delta-judging) |
| build-pipeline | the wish lifecycle: intake → classify → spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show → landed | E-2, T-1..T-6, T-8, T-9, T-11, T-12, T-15, T-16, T-17, T-18, INV-1, INV-2, INV-3, INV-4, INV-12, INV-16, INV-22, INV-26, INV-30, INV-31, INV-33, INV-37, INV-39, INV-41, INV-43, INV-46, INV-49, INV-53, INV-54, INV-55, INV-62, INV-63, INV-69, INV-70, INV-74, INV-75, INV-82, INV-99, INV-103, INV-104, INV-106, INV-113, E-14, E-15, INV-15, M-1, INV-115, INV-116, INV-121, INV-122, INV-123, INV-124 | `skills/build-pipeline/SKILL.md:41` (step zero: the door + work-kind), `:31` (the craft ladder — step→craft one home), `:83` (the work-kind table — per-kind meanings' one home), `:107` (steps), `:233` (gates), `:215` (re-carve paragraph — INV-113 redesign-owes-rework) |
| communicator | the human-facing exchange: reports, batched questions, decision pages, done-claim answers, the capture echo + departures board, the feature map on demand, the pre-report walk, working narration | T-7 (the report step; the walk before it is build-pipeline's), E-22, INV-25, INV-27, INV-28, INV-32, INV-34, INV-35, INV-38, INV-93, INV-94, INV-95, INV-109, INV-42, INV-51, INV-52, INV-57, INV-58, INV-59, INV-60, INV-64, INV-71, INV-81, INV-83, INV-67 (the showing channel matches the session's seat); also carries the clock law's chat-arm sentence as a wiring pin — that clock invariant's owner is the guardrails node | `skills/communicator/SKILL.md:33` (the rules), `:112` (rule 10 — the decision page), `:140` (rule 11 — the evidence walk), `:102` (rule 9 — the outcome-leads line shape), `:162` (the pre-report walk), `:82` (rule 7 — the chat-arm clock sentence) |
| templates | the document shapes a host copies at bootstrap; the matrix's coverage checklist | E-3, E-5, INV-6, B-1, E-24, INV-48, E-26 | `templates/TEST_MATRIX.template.md:43` (coverage validation), `templates/ROADMAP.template.md:1`, `templates/PRODUCT_SPEC.template.md:58` (index), `templates/PROBLEMS.template.md:1` (E-24 — the ledger's shape) |
| attach | attaching the pack to a host: adoption phases, VCS gate, attic, skill install + version record + the pack update check, the who-am-I-working-with step; also the catch-up walk that brings an already-adopted host onto the current pack | E-1, E-9, INV-7, INV-8, B-2, B-3, INV-36, A-0, A-1, A-2, A-3, A-4, A-5, A-7, A-8, A-9, A-10, A-11, INV-89, INV-90, INV-91, INV-92, INV-110, INV-111, E-21, E-25, INV-85, INV-86 | `adopt/ADOPT.md:16` (VCS gate first), `:109` (unbacked-surface verdict), `:42` (attic), `:11` (attach record), `:50` (B-3 — who am I working with, first step of orient), `MIGRATION.md:1` (A-11 — the catch-up walk's operating guide), `install.sh:2` (E-21 — the installer itself), `scripts/check-pack-update.sh:1` (E-25 — the update check) |
| inbox | parallel-safe intake door for wishes born outside a live-spec session | E-11, T-10, INV-10, INV-112 | `inbox/README.md:3` (one door, one NEW file), `:9` (file format), `:14` (commit rule), `:19` (remote arm) |
| host-contract | the recorded settings instances: this host's profile, the human's personal profile, and the thin loader that boots the personal layer | E-8, E-16 | `.live-spec/profile.md:1` (host), personal: `~/.claude/live-spec/profile.md` (symlink → playbook repo `personal/profile.md`, its git home — row 38 landed 2026-07-05), loader: `~/.claude/CLAUDE.md:1` (thin loader live — row 52 landed 2026-07-05) |
| package-docs | live-spec's own host instance (dogfood): spec, queue, journal, resume file, version, records, dev-machine skill sync, its own problem ledger | S-0, M-3, M-4, D-1, D-2, D-3, D-4, D-5, D-6, D-7, E-23 | `PRODUCT_SPEC.md:1`, `ROADMAP.md:12` (queue table), `JOURNAL.md:1`, `VERSION:1`, `scripts/sync-skills.sh:1` (E-23), `.live-spec/PROBLEMS.md:1` (E-24's dogfood instance; anchor owned by templates) |
| guardrails [target] | mechanical pre-push checks + surface registry + CI mirror; the pack's own gates + opt-in fence LIVE (hooks installed), the chat clock's mechanical hand, and the CI mirror LIVE (row 14 — `.github/workflows/gates.yml`, the same scripts as a second net); host-facing checks + registry still [target] (row 55) | E-6, E-10, M-5, INV-17, INV-24, INV-45, INV-47, INV-97 (the four host checks' shipping contract; code pin lands with row 241, [target]) (the chat arm's sentence is carried by communicator as wiring; ownership stays elsewhere), INV-66, E-29, INV-73, INV-120 (the shipped-language gate, proven on fixtures only — row 279) | `guardrails/pre-push:1` (gates), `guardrails/check-push-reach.sh:1` (the reach map's deciding script, gate b's scope), `guardrails/check-prototype-fence.sh:1` (prototype fence, gate e), `guardrails/check-shipped-language.sh:1` (shipped-language gate, INV-120), `scripts/check-shipped-language.py:1` (its engine), `guardrails/pre-commit:1` (commit fence), `guardrails/install.sh:1`, `scripts/clock-hook.sh:1` (the chat clock's hand), `tests/test_guardrails.py:1`, `tests/test_traceability.py:1` (the feature-coverage trace, E-29/INV-73), `.github/workflows/gates.yml:1` (the CI mirror); registry: — |
| snapshot [target] | saved baseline of the last accepted run; declared-scope diff (ROADMAP row 55) | E-7, A-6 | — (spec'd; code still ahead) |
| design-sync | optional machine, [target: machine; wiring live] — declared components of a landing synced to the team's design project, human-gated (ROADMAP row 93 — pack-side wiring landed session 8; the machine's first real run remains) | E-18 | wiring: `skills/live-spec-base/SKILL.md` (defaults table, `design-sync` row), `skills/communicator/SKILL.md` (rule 5 channel line), `skills/build-pipeline/SKILL.md` (step 9 sync line); machine: — |
| skill-evals | behaviour tests for the pack's own skills: per working skill one scenario, red proven bare, re-run at milestones (added session 8, row 94 — node add re-proven, record `docs/prover/2026-07-05-row94.md`) | E-19 | `evals/README.md:1` (the method + honest boundary), `evals/` (one file per working skill), `tests/test_traceability.py` (`test_skill_evals_present`, self-closing over skills/) |
| publish | the publish-quality gate: per-kind publication checklist (its one home) + the target-plugin seam; runs BEFORE the human's gate, never instead (added session 8, row 98 — node add re-proven, record `docs/prover/2026-07-05-row98.md`) | E-20, INV-44, INV-96, INV-119 | `skills/publish/SKILL.md:1` (frontmatter + when it fires), the kind-checklist table and target-plugin sections in the same file |
| test-author | the test method's one home: derives TEST_MATRIX.md from the proven spec through the proven architecture and writes the tests — the level ladder, real-artifact assertions, red-first proof, the pinned skip-set, traceability as a standing test (added session 23, row 163 — node add re-proven, record `docs/prover/2026-07-07-row163.md`) | E-27, INV-77, INV-78, INV-79, INV-80, INV-100, INV-102 | `skills/test-author/SKILL.md:1` (name + description), the level-ladder table and the two step sections in the same file |
| feedback-intake | the intake half of the exchange: receives anything handed back through three channels, routes each item to the home its law owns, keeps the feedback ledger's shape, echoes every arrival (added session 24, row 47 — node add re-proven, record `docs/prover/2026-07-07-row47.md`) | E-28, T-20, INV-68 | `skills/feedback-intake/SKILL.md:1` (frontmatter + when it fires), the routing table and ledger-shape sections in the same file |
| onboarding-card | the settings card: a build-time renderer parsing the base's package-defaults table + the profile files into the card page per the frozen norm; shown at founding/adoption end and on the standing "what can I customize?" question (added session 32, F-onboarding) | INV-87, INV-88 | `scripts/onboarding-card.py:1` (renders the card), `docs/norms/onboarding-card-2026-07-10.html` (the frozen norm), trigger wiring: `adopt/ADOPT.md` (setup-end line) + `skills/communicator/SKILL.md` (standing-question line) — wiring pins, ownership stays here |

## Seams

The places two nodes meet — named, because that is where composition bugs live. Each seam states what
crosses it and which side owns the format. Where a crossing has a real schema, the row names the schema's home — for this pack the shapes ARE the templates (the templates node owns them).

| Seam | Between | What crosses | Format owner |
|---|---|---|---|
| spec → prove | package-docs · product-prover | PRODUCT_SPEC.md, whole document | spec-author (the shape both sides speak) |
| architecture → prove | package-docs · product-prover | ARCHITECTURE.md, whole document — sent into the prover at every M-1 and M-6 gate beside the spec (INV-116) | build-pipeline (the architecture step's shape, `ARCHITECTURE.template.md`) |
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
| unit → coverage | package-docs · guardrails | each `[feature: F-x]` tag on a scenario heading, mapped to its implementer node(s) + a test in the Feature coverage table below (E-29, INV-73) | guardrails (the two-way check); spec-author (the tag format) |
| catalog → card | base-rulebook · onboarding-card | the package-defaults table (with the per-row card-visible/internal mark) read at render time | base-rulebook (the table and the mark) |
| profiles → card | host-contract · onboarding-card | the personal and host profile lines the card renders as the reader's own values and the project's rules | host-contract (the line format) |
| card → human | onboarding-card · communicator | the rendered card page, through the pre-show register lint and the seat's showing channel (INV-83, INV-67) | communicator (the showing walk) |

## Feature coverage

The feature layer above the anchor matrix (SPEC E-29, INV-73). live-spec's primary unit is its
person-facing scenario; each such heading in PRODUCT_SPEC.md carries an inline `[feature: F-x]` tag, and
the table below maps every unit to the node(s) that implement it and a test that exercises it. The check
runs both ways (`tests/test_traceability.py`, `TestFeatureCoverage`): every tag is a row here and every
row is a tagged scenario, every named node is real, every named test exists. The infra machines
(guardrails, host-contract, package-docs) implement guarantees rather than user features, and sit outside
this layer by the project type's own definition.

| feature | implemented by | test |
|---|---|---|
| F-wish | build-pipeline, communicator | test_capture_echo_and_board |
| F-prototype | guardrails, build-pipeline | test_prod_reference_fails |
| F-publish | publish | test_publish_skill_carries_checklist |
| F-feedback | feedback-intake, communicator | test_feedback_routes_have_homes |
| F-feature-map | communicator | test_feature_map_on_demand |
| F-bug | build-pipeline | test_gap4_recurring_bug_escalates |
| F-problem-ledger | base-rulebook, templates | test_problems_template_shape |
| F-bootstrap | attach, templates | test_scaffold_bootstrap_runs |
| F-adoption | attach | test_adopt_phases_cite_spec |
| F-pair | attach | test_pair_leadership_law |
| F-onboarding | onboarding-card, attach | test_onboarding_card_completeness |
| F-catchup | attach | test_catchup_walk |

## Runtime view

How each promised flow runs through the nodes [INV-74]. live-spec's kind is a skill pack, so its flow
unit is a wish (or a handed-in item) walking through the skills; each hop below crosses a seam named in
the Seams table, and the payload stays that table's fact. One line per flow: the walk, then where it
can fail.

| Flow | The walk through the nodes | Where it can fail | If it fails |
|---|---|---|---|
| F-wish | the human speaks → build-pipeline (door, intake) → communicator (capture echo) → spec-author (delta) → product-prover (prove → record) → build-pipeline (architecture step, this doc) → test-author (matrix + tests) → build-pipeline (code, verify) → communicator (landing report, show) | a misread door (the tripwires outrank labels); an unfolded must-fix (the record's folded column); a red suite at the gate | the tripwires re-door it mid-work; an unfolded must-fix blocks the landing until folded or rejected in the record; a red suite blocks the commit (the gate, not the narrator, says no) |
| F-bug | build-pipeline (bug door, queue-cut) → test-author (red-on-bug row + test) → build-pipeline (fix, class sweep) → guardrails (gate) | a fix without its red test; a class fixed at one instance only | the traceability test goes red until the row and test exist; the class sweep is checked at review — a point fix reopens |
| F-feedback | any session receives → feedback-intake (routing table) → the item's home (a queue row · the fixing commit · the decision archive · FEEDBACK.md · PROBLEMS.md) → communicator (the one echo) | an item routed to two homes; an arrival with no echo | the routing table has a home for every route by construction; an unroutable item gets one plain question, never a guess |
| F-prototype | a SEE/TRY ask → build-pipeline (prototype home, fenced) → guardrails (prototype fence) → promotion re-enters at F-wish's spec step | a sketch wired into a prod surface (the fence goes red) | the fence turns the push red; the sketch stays in its home until promoted through the spec step |
| F-publish | a push intent → publish (kind checklist) → guardrails (pre-push, reach map) → the human's gate | a stale shopfront claim; a gate skipped on a "just docs" diff | the reach map is conservative — an unmapped file runs the FULL suite; a stale claim blocks the push until fixed |
| F-feature-map | the human asks → communicator reads the spec's scenario headings + the queue's open rows → the answer in chat | an answer from memory rather than the read documents | a host with nothing to read is answered honestly with the bootstrap/adoption pointer |
| F-problem-ledger | workshop noise fires → base-rulebook (the ledger walk) → PROBLEMS.md (WATCHED → OWNED → SOLVED) | a silent retry with no line; a third unowned recurrence | a third unowned recurrence escalates to the pack's own queue — the method, not the day, owns it |
| F-bootstrap | scaffold → templates (copies) → attach (founding questions, B-3 profile step) | a founding question guessed rather than asked | a founding question with no answer parks as an open decision marker, asked, never invented |
| F-adoption | attach (orient → VCS gate → attic → attach record) → host-contract (profile, installed versions) | a host file overwritten with no attic line; an unbacked surface passed silently | the attic keeps every superseded file restorable; an unbacked surface goes red at the gate until specced or fenced |
| F-pair | attach (founding/adoption orient proposes the engine/instance split, human's word decides) → the two repos, each a full host (own spec/queue/journal/inbox) → the instance's inbox (lessons travel only through this door) | the split imposed rather than proposed; a third document across the seam; a window writing the pair's other tree beyond one inbox file | the human's word is the only decider, both outcomes recorded; each repo stays a full host with no third document; a window unsure of which repo it serves asks rather than writes |
| F-onboarding | setup's end (founding or adoption's orient) or the standing question → onboarding-card reads the base table + profiles → the card page → the pre-show register lint → shown by the seat's channel | a malformed table row; a missing personal profile; a register-lint block on the showing; a card row with no source | a malformed row fails the render loudly (never a silently dropped row); a missing profile renders package defaults with a plain absence notice naming the founding offer; a lint-blocked card is not shown until the flagged text is fixed; the completeness test goes red on any card/table mismatch |
| F-catchup | the owner's ask at an adopted host → attach (MIGRATION.md routing: never-adopted → adoption; adopted → catch-up) → orient on the delta (record + tree + pack VERSION) → the plan document → the owner's gate → execute (baseline commit, checkpointed steps, merges per the half-done-state law) → host gates re-run → host-contract (installed-set re-record, profile lines re-homed) | a step run on an assumed precondition; a merge nesting the old dir into the new; a walk interrupted mid-execute; a pair window writing the other half's tree | every step re-reads its precondition from the tree (a done step skips); the merge law forbids nesting and old-over-new overwrites; the checkpoint resumes the walk under the already-given gate; the pair's other half gets one inbox wish and its own window walks it |

## Placement view

Where everything runs [INV-75], secrets included. A skill pack executes nowhere by itself: the skills are text a model
reads, so the "runtime" is the agent session that loads them. Five places carry the pack:

| Place | What runs or lives there | Load-bearing technology |
|---|---|---|
| the agent session on the host machine | every skill EXECUTES here — the pipeline, the prover, the exchange are behaviours of the model reading the installed SKILL.md text; session hooks (clock, chat laws) fire here | Claude Code; the pack's skills as markdown |
| the installed skills dir `~/.claude/skills/` | the copies any session actually loads; synced from the repo | `scripts/sync-skills.sh` |
| the pack repo `~/live-spec` (source: github.com/happysasha18/live-spec) | the source of truth: skills, templates, guardrails, docs, tests; the suite and gates run here at commit/push time | python3 + pytest; bash git hooks |
| the host project's repo | the documents the method writes for that host: spec, queue, journal, checkpoints, ledgers | plain markdown in the host's tree |
| GitHub + CI · the human's browser | the remote copy and the gates' second net; rendered artifacts, decision pages, and the settings card open here | `.github/workflows/gates.yml`; `scripts/render-doc.py`; `scripts/onboarding-card.py` (runs in the agent session on the host machine, output opens in the browser) |

No secret lives in this pack: the repo, the templates, and the installed skills carry none, and a HOST's secrets stay in that host's own keychain or platform bindings — its placement table names the holder (the pack's own validation derivations model this).

## Quality budgets

What quality means for a skill pack, in numbers [INV-41]. Numbers proposed by the agent, tunable on
the human's word [INV-70]; each is asserted by a matrix row, and its instrumentation home is where the
real number is read.

| Budget | Number | Instrumentation home |
|---|---|---|
| full suite wall-time | ≤ 60 s on the dev machine [default] | the pytest tail line in the suite log |
| skill evals | every per-skill scenario green at each milestone | dated run records in `docs/evals/` |
| resume-file size | `NEXT_STEPS.md` ≤ 100 lines (INV-48, already asserted) | the suite's own check |
| spec prose register | style lint: 0 errors on PRODUCT_SPEC.md | `scripts/spec-style-lint.py` JSON tail |
| settings card render | ≤ 1 s on a pack-sized catalog [default] | the render script's own run, asserted by its matrix row |

A skill's judgment quality beyond the evals has no honest number; it is said by name here and judged
by the human's eye on real landings, never given a vanity metric.

## Decisions — where they live

The pack's decisions live in three homes already: the queue's dated rows (each landing's verdicts
inline), JOURNAL.md's chapters (the why), and the spec's open decision marks (the D-x rows of the
Formal index — attic layout, snapshot retention, and kin). This section is the doc's one entry point
to them; it holds pointers, never the decisions themselves. Structure-changing decisions also appear
in the Prover record below, one line each. And every full pass at an M-1 milestone gate or an M-6 push
gate that proves this document beside the spec (INV-116) appends its dated row to the Prover record — the
gate walk carries the duty, so this table stays current with the architecture's freshness rule rather
than trailing it.

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
| 2026-07-09 evening | v0.3.0 — runtime view + placement view + budgets added (row 180; CROSS-LINK on INV-74/75, findings F1-F5 folded) | `docs/prover/2026-07-09-row180.md` |
| 2026-07-10 | v1.0.x — M-1 milestone audit, architecture swept beside the spec | `docs/prover/2026-07-10-m1-audit.md` |
| 2026-07-12 | v1.1.0 — FULL pre-1.1.0 milestone pass (M-1), architecture proved beside the whole spec | `docs/prover/2026-07-12-full-pass-pre-1.1.0.md` |
| 2026-07-12 s38 | v1.1.0 — architecture proved at the push gate beside the spec, discharging INV-115/INV-116 (findings F-arch-1/F-arch-2 → row 273) | `docs/prover/2026-07-12-s38-inv115-inv116-and-architecture.md` |

---

*Coverage rule (walked at matrix derivation): every spec anchor appears in some node's "owns" column. An
orphan fact means a missing node or a missing assignment. A node that owns nothing has no spec backing,
and that is itself a finding. Mechanized in `tests/test_traceability.py`.*
