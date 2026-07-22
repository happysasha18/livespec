# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## ON RESUME (2026-07-22 — ROW 445 IN-WORK: spec format migration; Alexander approved the genre)
**Row 445 (big, in-work):** the spec moves to a requirements genre — glossary + requirements (Context, User Story,
acceptance criteria grouped in NAMED CASES, lowercase italic keywords, codes as trailing anchors, [GAP] lines for
source holes) — plus a delta classifier (new/sharpen/retire/scenario, enforced by parser diff), a bytes-per-rule
ratchet that only tightens, and a cold-reader panel gate (fresh readers until two consecutive zero-blocking reads).
Alexander's words 2026-07-22: genre approved («гораздо лучше»); named cases and lowercase italics his edits; LAW 4
(every relational word fills its slots — weak-word list + reader questions) his formulation; spec register = the
chat-answer register (write each section as if answering a stranger's question).
DONE today: baseline tag `spec-format-before-2026-07-22` + verbatim copies in docs/attic/2026-07-22-pre-format/;
format definition prototype/2026-07-22-spec-format/genre3/FORMAT.md (six laws, two-layer gate); approved sample
(sample.md, 8 cold-read rounds recorded); PILOT of one full section (pilot/, ratio measured: prose-to-prose 1.003,
whole-file honest projection ~540 KB = −31% ONLY IF the manual Formal index is retired for a generated code→location
lookup — the 130–180 KB morning estimate is REVISED by measurement, do not re-promise it); census: 32 shape-readers
(17 tests + 15 gates) must be rebuilt with the format, ~99 content-reader tests pin verbatim sentences and get
re-pinned mechanically from each section's mapping.md (code → new text). Rows 446-452 queued (gate reach, axes
catch-up, five spec holes). Inbox swept (3 deposits routed).
STAGE 1 DONE (2026-07-22 evening, PUSHED, suite 1798 green): spec-delta v2 proven (INV-250..271, prover verdict
lands-with-fixes, all applied; record docs/prover/2026-07-22-row445-spec-format-delta.md); seven format gates +
scripts/build-index.py landed UNARMED, 59 tests red-proven both ways; format definition promoted to docs/spec-format.md.
STAGE 2 RUNNING — converted so far (each: mapping zero-drop + reader panel to low/zero blocking, final clean read at
assembly): adopting-a-project (pilot/, 96 codes), agents-together (76 codes, ratio 0.59), bounds (113 codes, ratio
0.68). Remaining six: the build loop (207 KB — split by subsections), what-the-human-sends-back, when-something-breaks,
rules-and-who-applies, header/what-is, Reference (becomes the generated index). Then: re-pin content tests from
mappings, assemble + pooled glossary, retire the manual index (text to JOURNAL/attic);
(3) freeze re-baseline + fresh prover audit + MIGRATION chapter + VERSION 4.0.0 (major bump — his word) + push. Then
TEST_MATRIX and ROADMAP get their own movements; then the host migration chapter (tlvphotos 434 KB, track-coach 247 KB
specs) driven by script in each project's own window.
Push on green (his grant); re-test every "needs his word" by derivability FIRST; re-derive deferred state from CODE
(INV-247). Next free INV-250 / M-435 / row 453.

## FIRST at intake — classify one-time vs standing (Alexander's word 2026-07-21, ROADMAP 440, memory [[classify-request-onetime-vs-standing-up-front]])
Name every request's persistence class before actioning it, and say it yourself. A standing ask owes a PERMANENT
mechanism (a pack gate/rule/judge inherited by every host); the one-time sweep to floor is only its other half.

## LANDED 2026-07-21 (v3.3.0–v3.6.0, all PUSHED — detail in JOURNAL)
INV-49 sharpened (442) · INV-245 (441) · INV-246 (443) · prose sweep (444) · INV-247 (430) · INV-248 (438) ·
INV-249 inbox deposit protocol (439). Follow-on boundary notes for INV-245/246: DONE inside the clauses.

## Migration readiness (2026-07-21) — when can other projects migrate?
Other projects (track-coach, tlvphotos, promoter) should NOT migrate yet; the block is Alexander's word, not build
work. The pack version is in motion (v2.8.3 → 3.3.0 this session). tlvphotos migrates onto the axes release (v3.2.0),
its concrete vehicle for the live mobile device-parity gap; that migration is its own next step on his word. The polished
on-ramp (movement 3, onboarding) is DEFERRED on ~8 taste forks. Two open questions bite these projects: framework
coexistence and the "superpower" competitor positioning.

## Open movements
2. **Axes-from-kind — CLOSED v3.2.0.** INV-244: a surface's composition axes derive from project.kind; visual kinds owe
   input-capability (first member of an open set), owed-vs-covered gap is a finding, per-kind axis set a mandatory
   flag-if-absent `project.axes` declaration. Records under docs/prover/ and docs/skill-review/. Follow-ons (deferred):
   the forcing step for each axis's in-between value; the recursive similarity sweep over the axis registry (ROADMAP 437);
   the other kinds' elementary axis sets.
0. **Conduct audit — CLOSED v3.1.0.** INV-241/242/243. Follow-ons: rows 431, 432, 435 (far).
1. **Comms/naming — CLOSED v3.0.0.**
3. **Adoption + onboarding — DEFERRED (his 2026-07-18 word).** Designs docs/design/2026-07-18-*.md. FORKS: preset values;
   default preset; ask-vs-infer; 2/3 presets; pre-push home; plan-axis scope; welcome shape; registry placement. Owns the
   parameters registry (ROADMAP 427).

## Captured future ideas (owner-held for scope)
- **Living everything principle.** Any shared artifact can be living. Living description (INV-240) + registry (427) are its first two.
- **After-the-fact user-tell family (ROADMAP 428).** An 11-member class; one clause; on his word.
- **Framework coexistence at onboarding + README** — name the boundary if a person already runs another framework.
- **Evaluate the "superpower" skill as a competitor + README.**

## LIVE STATE (2026-07-21 — v3.3.0 integrated on main, four movements, suite green)
Shipped this session: INV-49 sharpened (ROADMAP 442) · INV-245 project-name gate (441) · INV-246 lean-orchestrator arm
(443) · prose-quality sweep (444) — built as parallel lanes under one pen, reconciled at integration. VERSION + 10 skills
+ plugin.json stamped to 3.3.0; spec base to be re-frozen in the landing commit
(`python3 scripts/spec-freeze.py --freeze PRODUCT_SPEC.md ARCHITECTURE.md TEST_MATRIX.md --compaction`). Pushing on green.
Memory: this whole session is wipeable.

## Standing word / OWNER-HELD
- Whole movement solo, push on green; plain English in docs, plain Russian in chat; gates mandatory. Max agentic,
  conserve orchestrator context (delegate reads/drafts; hold briefs + decisions).
- **lean-orchestrator:** the seat authors nothing long and reads nothing past a glance inline; drafting and non-glance
  reads go to workers. Tunable per-person, default strict. Now backed by the INV-246 soft signal.
- CONCURRENCY: multiple windows share ~/live-spec. Commit narrowly by explicit path, never git add -A; re-check HEAD
  before writing (the fence — `guardrails/fence-refresh.sh` to re-arm after accounting for a move). `.spec-freeze/`
  re-frozen in the landing commit.
- **Row 421 (open, Alexander's call):** one window ruling several instance-agents against the one-window law.

## Queue's open head (field-gated + far tier)
- 385 first real contract · 389 cross-machine read · 247 remote-deposit field leg · 396/405 conversation channel +
  listener (wait on the harness listener, INV-231) · far tier 381, 411, 435, 436/437. (438 delivery-separability lens
  LANDED v3.5.0; 439 inbox deposit protocol LANDED v3.6.0.) Runnable head is field-gated (contract/listener) + far tier.

## Inbox (2026-07-21) — both deposits routed, left earned in place (row-430 precedent, no delete under a live writer)
- tlvphotos delivery-separability wish → ROADMAP 438; Alexander 2026-07-21: 438 and this whole file are one and the
  same, so section 3 (dual-as-discovery-heuristic) was FOLDED into row 438 (no separate row). Scope/greenlight on his word.
- `from-owner-verify-code-state` (row 430) → LANDED as INV-247 (v3.4.0, pushed). Left earned in place (INV-249 precedent).
ROADMAP 439 (inbox deposit protocol) → LANDED as INV-249 (v3.6.0); the `.draft` protocol now governs future deposits.

## Next free codes
Next free INV-250, E-36, T-25, M-435, next ROADMAP row 445. (INV-248/M-433 were v3.5.0's; INV-249/M-434 were v3.6.0's.)

## Research in hand
Direct-protocol research (scratchpad research-agent-transport.md + research-direct-channel.md): A2A re-invents our
card; prior art docs/research/2026-07-17-agent-routing-prior-art.md.
