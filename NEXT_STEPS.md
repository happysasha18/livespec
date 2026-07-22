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
STAGE 2 CONVERSION DONE, PANEL NEARLY DONE (2026-07-22 late evening, committed): ALL NINE units converted
(pilot + agents-together + bounds earlier; today build-loop a/b/c, what-the-human-sends-back, when-something-breaks,
rules-and-who-applies, what-live-spec-is), each with mapping zero-drop proven, GAPS.md, NUMBERS.md, five lints green.
Panel verdicts (two consecutive zero-blocking reads = accepted): ACCEPTED — what-live-spec-is (r6-7),
when-something-breaks (r8-9), what-the-human-sends-back (r10-11), rules (r10-11), build-loop-c (r10-11),
build-loop-a (r16-17). build-loop-b: last fix landed (the `[target]` later-surface gloss), round-17 read was in
flight at session end — NEXT SESSION: read its verdict in the conversion notes, then run clean reads to two
consecutive zero (the reader prompt template is in this file's sibling runs; each read ≈ one opus worker on the one
file). Everything the panels could not settle is in prototype/2026-07-22-spec-format/conversion/ASSEMBLY-NOTES.md
(17 numbered items: renames, one-name merges, source defects → queue rows at landing, per-unit acceptance notes).
Prose-to-prose ratios measured per unit (0.59–1.46; growth in low-history units, shrink in provenance-heavy ones —
whole-file shrink comes from retiring the manual index). THEN: re-pin ~99 content tests from mappings, assemble +
pooled glossary + renumber requirements, retire the manual index via scripts/build-index.py (text to JOURNAL/attic),
arm the seven format gates; (3) freeze re-baseline + fresh prover audit + MIGRATION chapter + VERSION 4.0.0 (major
bump — his word) + push. Order he set 2026-07-22: finish ALL live-spec docs first (spec, then TEST_MATRIX, ROADMAP
movements, architecture format = row 456) as the method's own proof; only then tlvphotos migrates (his word starts
it, from its own window); other projects stand until then.
Push on green (his grant); re-test every "needs his word" by derivability FIRST; re-derive deferred state from CODE
(INV-247). Next free INV-272 / M-435 / row 460.
ALSO TODAY (all committed/pushed): cost audit (row 457: $14.3K API-equiv/week measured, two-thirds cache re-reads at
252k avg context; levers: milestone wipes, batching, sonnet routing, log-to-file) + budget law in the personal profile;
cost deposit → tlvphotos inbox; plain-language method deposit → promoter inbox; rows 455 (transcript audit), 456
(architecture format), 458 (cold-reader audit as pack skill), 459 (bug rows carry axis/class/spec verdicts) queued;
scissors scanner widened to comma-less «а не»/«но не» (all windows inherit); lean-orchestrator warning hook armed
machine-wide; playbook holds the audit script (tools/usage-audit.py) + hook overlays.

## FIRST at intake — classify one-time vs standing (Alexander's word 2026-07-21, ROADMAP 440, memory [[classify-request-onetime-vs-standing-up-front]])
Name every request's persistence class before actioning it, and say it yourself. A standing ask owes a PERMANENT
mechanism (a pack gate/rule/judge inherited by every host); the one-time sweep to floor is only its other half.

## LANDED 2026-07-21 (v3.3.0–v3.6.0, all PUSHED — detail in JOURNAL)
INV-49 sharpened (442) · INV-245 (441) · INV-246 (443) · prose sweep (444) · INV-247 (430) · INV-248 (438) ·
INV-249 inbox deposit protocol (439).

## Migration readiness — his 2026-07-22 order supersedes the 2026-07-21 note
Finish ALL live-spec docs first (see ON RESUME); then tlvphotos on his word; others stand. Onboarding (movement 3)
stays deferred on ~8 taste forks; framework coexistence + "superpower" positioning stay open questions.

## Open movements
CLOSED: conduct audit v3.1.0 (follow-ons rows 431/432/435) · comms/naming v3.0.0 · axes-from-kind v3.2.0 (INV-244;
follow-ons: per-axis forcing step, recursive similarity sweep ROADMAP 437 — his 2026-07-22 word pulls 437+459 into the
near plan after row 445, other kinds' axis sets).
DEFERRED: adoption + onboarding (his 2026-07-18 word; designs docs/design/2026-07-18-*.md; ~8 taste forks; owns the
parameters registry, ROADMAP 427).

## Captured future ideas (owner-held for scope)
- **Living everything principle.** Any shared artifact can be living. Living description (INV-240) + registry (427) are its first two.
- **After-the-fact user-tell family (ROADMAP 428).** An 11-member class; one clause; on his word.
- **Framework coexistence at onboarding + README** — name the boundary if a person already runs another framework.
- **Evaluate the "superpower" skill as a competitor + README.**

## LIVE STATE (2026-07-22 late — row 445 stage 2 committed e9d4eae; this session is wipeable)
Spec base re-freeze rides the 4.0.0 landing commit (`python3 scripts/spec-freeze.py --freeze PRODUCT_SPEC.md
ARCHITECTURE.md TEST_MATRIX.md --compaction`).

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

## Inbox — all 2026-07-21 deposits routed and landed (438→INV-248, 430→INV-247, 439→INV-249), left earned in place.

## Next free codes
Next free INV-272, E-36, T-25, M-435, next ROADMAP row 460.

## Research in hand
Direct-protocol research (scratchpad research-agent-transport.md + research-direct-channel.md): A2A re-invents our
card; prior art docs/research/2026-07-17-agent-routing-prior-art.md.
