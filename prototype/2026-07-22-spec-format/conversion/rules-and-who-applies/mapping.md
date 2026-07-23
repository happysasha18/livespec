# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite of `## The rules and who applies them` dropped nothing. Part 1 maps every code the source section cites to its new home. Part 2 states which codes carried a consumed Formal-index row. Part 3 maps every behavioural claim of the source to the criterion that now carries it.

`Rn` names Requirement n in `section.md`; a code in several requirements is anchored in each. Zero codes are dropped: all 76 cited codes appear in `section.md` (verified mechanically — the cited-set of the source range minus the present-set of `section.md` is empty, and the reverse difference is empty too, so the section anchors no code the source did not cite).

## Part 1 — every cited code → its new home

| Code | New home | Index row consumed? |
|---|---|:--:|
| A-7 | R5 | yes |
| A-8 | R3 | yes |
| ACT-1 | R3 | yes |
| ACT-2 | R9, R11 | yes |
| ACT-3 | R3, R9, R10, R11, R16, R20 | yes |
| D-2 | R11 | yes |
| D-4 | R1 | yes |
| E-8 | R3, R5 | yes |
| E-12 | R1, R5 | yes |
| E-13 | R1, R3, R5, R10, R22, R23 | yes |
| E-16 | R8 | yes |
| INV-4 | R14, R15 | yes |
| INV-5 | R6, R23 | yes |
| INV-7 | R8 | yes |
| INV-9 | R3, R22, R23 | yes |
| INV-10 | R8, R10 | yes |
| INV-11 | R8, R10 | yes |
| INV-13 | R1, R8 | yes |
| INV-14 | R6, R7 | yes |
| INV-16 | R23 | yes |
| INV-17 | R15 | yes |
| INV-23 | R10 | yes |
| INV-24 | R10 | yes |
| INV-25 | R4 | yes |
| INV-28 | R15 | yes |
| INV-31 | R23 | yes |
| INV-35 | R23 | yes |
| INV-36 | R17, R22 | yes |
| INV-39 | R10, R22, R23 | yes |
| INV-40 | R23 | yes |
| INV-44 | R17 | yes |
| INV-45 | R22, R23 | yes |
| INV-46 | R16, R17, R18 | yes |
| INV-48 | R14 | yes |
| INV-53 | R13, R19 | yes |
| INV-54 | R20 | yes |
| INV-55 | R21 | yes |
| INV-59 | R15 | yes |
| INV-61 | R16 | yes |
| INV-66 | R2 | yes |
| INV-69 | R9, R11, R13, R22 | yes |
| INV-70 | R14 | yes |
| INV-76 | R10 | yes |
| INV-85 | R17 | yes |
| INV-103 | R12, R13 | yes |
| INV-105 | R10 | yes |
| INV-113 | R17 | yes |
| INV-116 | R18 | yes |
| INV-121 | R14, R15 | yes |
| INV-122 | R17 | yes |
| INV-137 | R13, R19 | yes |
| INV-141 | R17 | yes |
| INV-142 | R17 | yes |
| INV-143 | R14, R15, R17 | yes |
| INV-145 | R17, R18 | yes |
| INV-151 | R15 | yes |
| INV-152 | R15, R17 | yes |
| INV-155 | R15 | yes |
| INV-159 | R12 | yes |
| INV-162 | R10 | yes |
| INV-187 | R17 | yes |
| INV-217 | R18 | yes |
| INV-226 | R17 | yes |
| INV-230 | R10 | yes |
| INV-235 | R17 | yes |
| INV-237 | R18 | yes |
| M-1 | R1 | yes |
| M-2 | R7 | yes |
| M-6 | R6, R22, R23 | yes |
| M-7 | R4 | yes |
| T-12 | R23 | yes |
| T-15 | R23 | yes |
| T-16 | R23 | yes |
| T-18 | R10 | yes |
| T-19 | R11, R22, R23 | yes |
| T-22 | R17 | yes |

## Part 2 — consumed Formal-index rows

The section cites 76 distinct codes, and **all 76 carry a Formal-index row** — this section names no inline-only feature code. Each row's meaning now lives at the home named in Part 1; no consumed index row is left without a home.

**Codes owned by this section** (their Formal-index home is `One rulebook`, `One rulebook behind the skills`, `Who decides what`, or `When money or time run short`) are the ones this rewrite fully converts: ACT-1, ACT-2, ACT-3, E-8, E-12, E-13, E-16, INV-9, INV-13, INV-14, INV-25, INV-40, INV-46, INV-53, INV-54, INV-55, INV-66, INV-69, INV-103, INV-137, INV-143, INV-152, INV-235, INV-237, T-19.

**Pure cross-references** — a rule owned by another section that this section leans on rather than restates — are preserved as trailing anchors at the requirement that leans on them; the full behaviour stays defined in the home section, not re-converted here: A-7, A-8, D-2, D-4, INV-4, INV-5, INV-7, INV-10, INV-11, INV-16, INV-17, INV-23, INV-24, INV-28, INV-31, INV-35, INV-36, INV-39, INV-44, INV-45, INV-48, INV-59, INV-61, INV-70, INV-76, INV-85, INV-105, INV-113, INV-116, INV-121, INV-122, INV-141, INV-142, INV-145, INV-151, INV-155, INV-159, INV-162, INV-187, INV-217, INV-226, INV-230, M-1, M-2, M-6, M-7, T-12, T-15, T-16, T-18, T-22.

**Cross-section glossary note.** A handful of domain nouns the section uses are owned by other sections and are defined in their home glossary, not repeated here: *settings ladder*, *personal profile*, *profile*, *host*, *pack*, *session*, *journal*, *attic*, *queue*, *backlog item*, *project kind*, *freshness check*, *net*, *push gate*, *prover record*, *seat*, *pen*, *adversarial read*, *expensive decision*, *design review*, *milestone*, *movement*, *delivery*, *delivery report*. In a whole-document conversion these live once in the shared glossary; this section's `## Glossary additions` block adds only the nouns this section introduces (base skill, working skill, senior agent, worker, tier, brief, checkpoint, routing rule, economy ladder, done-claim, method version, delegation accounting, never-bend list).

## Part 3 — atomic-claim coverage

Every behavioural claim of the source, in source order, mapped to the criterion (or criteria) that now carries it. "R9.3" means Requirement 9, criterion 3.

### One rulebook behind the skills (E-12, D-4, E-13, INV-13, M-1, INV-66)

| # | Source claim | Criterion |
|---|---|---|
| 1 | The five rules every skill works by are ask-never-guess, plain words with the code trailing, one surface one name, one canonical home per fact, and resume-from-checkpoint. | R1 Context (the rule set the base states); each rule owned by its own base-rulebook home, referenced here |
| 2 | The shared rules live once in the base skill, which states each normatively beside the default settings; a working skill references rather than restates. | R1.1 |
| 3 | The package is the source; the standalone repositories are read-only mirrors. | R1.3 |
| 4 | Every working skill opens with one line naming the base skill and the base version, swept in the same session that bumps the base. | R1.4 |
| 5 | A working skill used standalone stands on its own; the opening line reads as plain advice and no domain need requires the base installed. | R1.5 |
| 6 | A shared rule has one normative home; a second full statement is drift to fold back. | R1.2 |
| 7 | The compaction pass prunes restatements older than the base at milestones, one skill at a time. | R1.6 |
| 8 | Every place the pack lists its skills names the same complete set (working-skills sentence, closing lists, README table). | R2.1 |
| 9 | A check at every commit reds a list that misses a skill. | R2.2 |

### Human authority and evidence (INV-9, ACT-1, E-13, A-8, ACT-3, E-8, INV-25, M-7)

| # | Source claim | Criterion |
|---|---|---|
| 10 | The human owns taste, design, irreversible/publish/push gates, domain wording, and the human's working contract. | R3.1 |
| 11 | The personal profile holds the human's lines (proactivity mode, trust, language, domain vocabulary) and follows the human everywhere. | R3.4 |
| 12 | The host profile narrows those lines for one project on the human's word, created at attach and git-tracked beside the adopt artifacts. | R3.5 |
| 13 | Inside `.live-spec/` only the checkpoints stay ignored. | R3.6 |
| 14 | Communicator resolves the whole ladder to the contract before every human-facing exchange, never one file. | R3.2 |
| 15 | Mode and trust are set only on the human's word; the agent proposes and never raises its own. | R3.3 |
| 16 | A done-claim is answered by walking the evidence fresh, apart from what it asserts, carrying the method version. | R4.1 |
| 17 | No done-claim is answered from memory; every claim pins to a checkable artifact walked now. | R4.3 |
| 18 | The method version reads from the host's installed set (the version homes); one line reads claim → artifact → version. | R4.2, R4.4 |
| 19 | An absent installed set is said plainly — an honest answer, never invented. | R4.5 |

### Settings and the ladder (E-13, E-12, E-8, A-7, INV-5, INV-14, M-6, M-2, E-16, INV-13, INV-10, INV-7, INV-11)

| # | Source claim | Criterion |
|---|---|---|
| 20 | Settings climb four nested scopes (package default, personal profile, host profile, session), each setting homed in one. | R5.1 |
| 21 | Resolution reads narrowest out: session over host over personal over package default. | R5.2 |
| 22 | Profiles are re-read at the same freshness points as skills. | R5.3 |
| 23 | A profile line outside the current vocabulary is ignored aloud — a dated journal note plus a line in the next report — the durable journal half standing even if the session dies first. | R5.4 |
| 24 | No override is silent; an override is a written line, journaled in the home it governs (host line → host journal, default → package journal). | R6.1, R6.2 |
| 25 | The push gate's own cadence is the worked example — package default full-prover-before-minor, host contract tightening to before every push, recorded and visible. | R6.3, R6.4 |
| 26 | The session scope is never a file; a session override lives only in the spoken word and the agent never writes it. | R7.1 |
| 27 | A session line that should outlive the session is promoted into its profile on the human's word and journaled. | R7.2 |
| 28 | Announced self-compaction carries live session lines forward; a full wipe ends the sitting and the session lines die by design. | R7.3, R7.4 |
| 29 | The personal layer has one home (the profile); the global file is a thin loader holding only bootstrap lines, and the profile never restates them. | R8.1, R8.2 |
| 30 | Migrating a rule file forks by scope: method rule stays the pack's, personal line to the profile, project line becomes a migration note the project's own session lands. | R8.3 |
| 31 | A rule-by-rule mapping proves the move lossless; the old file stays in the attic so one move rolls back. | R8.4 |
| 32 | A promotion outside any repository fence re-reads the file immediately before appending, its git home the recovery net. | R8.5 |

### Delegation and workers (ACT-2, INV-69, ACT-3, INV-10, T-18, INV-39, INV-11, INV-105, E-13, INV-23, INV-24, INV-76, INV-162, INV-230)

| # | Source claim | Criterion |
|---|---|---|
| 33 | The senior agent owns judgment (spec deltas, matrix levels, findings triage, this document); it never routes down. | R9.1 |
| 34 | Workers own mechanical execution in three tiers (one-shot worker, multi-step worker, senior for judgment); the routing rule proposes before the senior overrules. | R9.2, R9.3 |
| 35 | Each worker keeps a persistent checkpoint under `.live-spec/checkpoints/`, out of git and off the temp directory. | R9.4 |
| 36 | A worker inherits write-ownership narrowed to its brief's files, reading outside and never writing there. | R10.1 |
| 37 | A brief may name an isolated tree copy whose delta integrates only under the pen. | R10.2 |
| 38 | Before spawning another concurrent writer the senior confirms disjoint write-sets or grants a worktree; the fence stays quiet between same-session siblings. | R10.3 |
| 39 | The live setting lines ride into the brief verbatim; a worker cannot resolve the ladder itself. | R10.4 |
| 40 | The brief carries the clock (stamps off the brief's clock, never invented) and the problem-ledger path (noise becomes a ledger line, never a silent retry). | R10.5 |
| 41 | The worker heartbeats its checkpoint on a fixed interval so a compute-bound run is not read as dead. | R10.6 |
| 42 | A failed acceptance escalates one tier with a logged line; never a silent same-tier retry, never a skipped rung. | R10.7 |
| 43 | At teardown the worker reaps only its own process group, reading a stall by the checkpoint's mtime and confirming ownership before any reap, never a kill by name. | R10.8 |
| 44 | The routing rule proposes by step and kind (judgment→senior never down, one-shot→cheapest worker, multi-step→mid worker); size is a coarse prior only. | R11.1, R11.2 |
| 45 | The economy rung moves the threshold: lean rides an airtight brief one tier cheaper and raises the bar; tight proposes the cheapest tier that can pass and keeps the senior on judgment alone. | R11.3, R11.4 |
| 46 | The proposal is advisory; the senior overrides per wish, logged proposed→chosen→why on checkpoint and report, distinct from the failed-acceptance escalation; a silent tier change is the defect. | R11.5, R11.6 |
| 47 | Every delivered row records its delegation accounting in the status cell; a suite check reds a row missing the line; the duty binds the orchestrating seat and binds forward. | R12.1, R12.2 (+ GAP: the saving's unit/baseline) |
| 48 | The senior reads to decide and dispatches discovery reads past a bounded glance to a reader worker, keeping only distillations. | R13.1, R13.2 |
| 49 | A verify/decide read stays with the senior (checking the real artifact, re-reading a primary source). | R13.3 |
| 50 | The brief-owed read composes here — dispatched to the reader whose distillation returns the per-file lines, or a bounded decide-read for a small edit. | R13.4 |
| 51 | The reads dispatched are named in the report's delegation accounting, making the leanness visible. | R13.5 |
| 52 | The senior decides what it can (mechanical step, artifact-determined value, a default it can pick and name) and reports the choice; the posture holds after a memory wipe. | R14.1, R14.2 |
| 53 | It surfaces only what needs the human (taste, a trade-off no artifact settles, a change to correct) and never parks derivable work on the human's queue. | R14.3, R14.4 |
| 54 | A held backlog item is re-tested for derivability on every touch; an artifact-pinned answer makes it the seat's (do, cite, drop the marker). | R15.1 |
| 55 | A fact no artifact holds (taste, policy, irreversible-outside-git) keeps it the human's; the marker must name that human-only fact, and one that cannot defaults to the seat's, the unnamed marker being the finding. | R15.2, R15.3 |
| 56 | Two arms enforce: a mechanical net reds a commit whose parked item names no reason category; a delivery arm re-fires the derivability test when a marker is written or a question opened, reading grammatical shape not a phrasing list. | R15.4, R15.5 |
| 57 | A worker's green gets a second pair of eyes; verify's audit briefs a fresh checker from spec sentences and paths (never the worker's summary or the senior's plan) on the goal-missed hypothesis and walks exists→substantive→wired→flows to rows or red. | R16.1, R16.2 |
| 58 | It fires mandatory when high-stakes (surface-sized delta or a method edit) and the only review is the author's; independence needs a differently-contexted head from primary sources, delegation not counting. | R16.3, R16.4 |
| 59 | One fresh checker covers a delivery batch; the checker is a worker whose verdict rides the report. | R16.5 |
| 60 | An expensive decision (agent birth, node carve/merge, contract shape once pinned, project kind, engine/instance split, repo going public) earns an adversarial read; the closed set is named on the enumerate-versus-ride keying. | R17.1 |
| 61 | No machine tells expensive from ordinary, so the duty is stated for the class and each member carries it at its own point; a traceability test holds this clause names the read and agent birth carries it. | R17.2 |
| 62 | The read is a fresh-context independent audit at the best tier the quality habit sets, set on breaking the case; where the decision turns on one-kind grouping the design review reads with two objects in hand; it closes by bringing the decision to the human with findings and a recommendation, the taste call staying the human's. | R17.3, R17.4, R17.5 (+ GAP: the read's model tier) |
| 63 | The authoring seat drafts and accepts but never certifies its own work; a release's adversarial pass is authored by a fresh differently-contexted seat under the verify freshness. | R18.1, R18.2 |
| 64 | A newly added lens or rule is self-applied to its introducing document before release, the release record naming the result; the release gate may require a dated review record naming a different seat. | R18.3, R18.4 |
| 65 | A brief is born from a full read of the files it edits, recording current/changes/survives per file, every step back-referencing its spec sentence and every claim citing its source. | R19.1, R19.2 |
| 66 | The brief-read composes with the lean-context duty (dispatched to a reader worker or a bounded decide-read). | R19.3 |
| 67 | A worker stops only on the closed halt list (ambiguous requirement, two consecutive unexplained failures, missing config/dependency, acceptance impossible) with evidence, otherwise runs to completion, composing with one-tier escalation. | R20.1, R20.2 |
| 68 | A brief is sized to a bounded share of the worker's context (~300 lines, ~8 files default), splitting above the bound and passing paths never inlined bodies. | R21.1, R21.2 |

### When money or time run short (T-19, E-13, INV-9, INV-36, INV-5, INV-69, INV-39, INV-45, M-6, INV-40, T-12, INV-16, INV-31, INV-35, T-15, T-16)

| # | Source claim | Criterion |
|---|---|---|
| 69 | The economy pressure is one setting `budget.pressure` (default full), moved only on the human's word (session word or profile line); the agent proposes a rung, never sets one; the choice is surfaced at project setup beside the project kind. | R22.1, R22.2 |
| 70 | full runs the full suite at every delivery gate, the prover at its cadence, and routes tiers by the routing rule. | R22.3 |
| 71 | lean scopes mid-work test runs to the touched node's rows while keeping the full suite at every gate and before every push, and writes a deferred full pass as a dated debt line. | R22.4 |
| 72 | tight batches consecutive small deliveries into one full-suite run, keeps one row's delta per commit, and bisects a batch-end red to the last green base. | R22.5 |
| 73 | A push under any rung still requires the reach-scoped gate green at head and the host's recorded prover cadence. | R22.6 |
| 74 | The never-bend list holds at every rung: door law + tripwires, red-before-fix, the human's gates. | R23.1 |
| 75 | The never-bend list holds the delivery report (taken defaults + named sheds), delivery purity (one row's delta), whole narration. | R23.2 |
| 76 | The never-bend list holds the push gate (every reachable check green at head + prover cadence) and the safety net no work-kind or scope cut touches. | R23.3 |
| 77 | An explicit host line outlives any rung (a tighter cadence held even under tight). | R23.4 |
| 78 | `budget.pressure` moves only by the human's word; no automatic rung-switching. | R23.5 |

### Coverage result

78 behavioural claims mapped, covering all 23 requirements. History carried by the source — dated worked-proof narratives (the routing rule's mid-turn breaks, the difflib runaway, the release miscount), row-number cross-references (rows 216/217, 253/254, the ROADMAP row pointers), and the provenance of who asked when — is dropped by law 6; it lives in the journal already, and the mechanical no-history gate confirms none survived in the body. Source non-goal / policy blocks are carried as source policy statements in the requirement contexts rather than converted to `shall` criteria, since they state what the system deliberately does not do: the router's "no numeric budget and no token meter" and "no fourth tier" (folded into R11's context and R22's qualitative-rung criteria), and the economy ladder's "no automatic rung-switching" (converted positively as R23.5). No behavioural `shall`-claim of the source is left uncovered; the two source holes are recorded as `[GAP]` lines at R12.1 and R17.3 and detailed in `GAPS.md`.

### Prover MUST-FIX wave (row 445 audit, F3) — declared sharpen

- **One name for the acting seat**: the unit carried "senior agent" 31 times (glossary entry, R9 heading and throughout R9–R14) while the pooled glossary's `seat` entry declared seat the one kept name. Audit finding F3. Every "senior agent" in this unit is swept to "the seat" / "seat" — the same actor in every occurrence, judged one by one; no occurrence carried a different sense. The unit's own duplicate glossary entry `senior agent` is removed (the pooled `seat` entry, homed in build-loop-b, records the source's other names); the assembly's `ADDITIONS` list drops its duplicate `senior agent` entry in the same stroke. Behaviour unchanged; the codes on every touched criterion (ACT-2, INV-69, INV-103, INV-137, INV-143, INV-121, INV-70, T-18, T-19, INV-11, INV-105, ACT-3, INV-39, D-2) are untouched.

### Final restoration wave (re-pin sweep) — declared additions

- **R16.3 (adversarial verify).** Restores the dropped method-edit carve-out phrase "a rule whose meaning changed". Owed by `test_traceability::TestProblemLedger::test_adversarial_verify_option`. [INV-46]
- **R22.7 (tight-rung batch rollback).** Restores the economy ladder's tight-rung rollback path — the system reverts the batch to its last green base and re-applies the clean landings, so `HEAD` never sits red across a breakpoint. Owed by `TestSmallDesignHoles::test_178`. HEAD is backticked per the caps law (INV-251). [INV-39, T-19]
