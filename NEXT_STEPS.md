# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## ON RESUME (2026-07-21 — v3.4.0 LANDED and PUSHED; tails closed)
v3.3.0 (four movements) and then v3.4.0 are both PUSHED (HEAD 0846edb, tree clean, origin synced). Closing tails,
this session BUILT one small movement at **v3.4.0**: **INV-247 + base rule 34** — before resuming a deferred/queued
item, re-derive its state from the CODE (ROADMAP 430, Alexander's word). Delta: PRODUCT_SPEC clause + Formal-index
row, base rule 34 (count 33→34), ARCHITECTURE build-pipeline ownership, M-432, tests/test_resume_rederive.py
(4 tests, red-proven), a fresh-context prover record and a live-spec-base skill-review record. Two prover follow-on
notes landed inside INV-245 and INV-246; the tlvphotos inbox wish's section 3 (dual-as-discovery-heuristic) folded
into ROADMAP 438. ROADMAP 430 flipped to landed. Suite 1723 green; all push gates green.
Push on green (his grant); a taste/policy fork stays an explicit question; re-test every "needs his word" by
derivability FIRST. BEFORE resuming any deferred/queued item, re-derive its state from the CODE, not this file (INV-247).

## FIRST at intake — classify one-time vs standing (Alexander's word 2026-07-21, ROADMAP 440, memory [[classify-request-onetime-vs-standing-up-front]])
Name every request's persistence class before actioning it, and say it yourself. A standing ask owes a PERMANENT
mechanism (a pack gate/rule/judge inherited by every host); the one-time sweep to floor is only its other half.

## LANDED this session (v3.3.0)
- **M0 — INV-49 sharpened (ROADMAP 442).** The edge rule draws an edge only on a true dependency or a same-section /
  same-behaviour collision; co-location in the shared living docs draws none (the docs reconcile at integration).
  Over-broad "doc region" wording replaced across spec + both skill copies + INV-214's reason list; enforcement is a
  new product-prover lens (false-serialization / over-broad independence edge). M-147 + test_lanes_by_graph strengthened.
- **M1 — INV-245 project-name gate (ROADMAP 441).** An ARM on the shipped-language gate (gate i, INV-120): a core spec
  reds on a bare foreign project name or a name beside a calendar date; forbidden names live as allowlist DATA. 7 red-first
  tests; the one-time sweep reworded 45 provenance lines + 5 fixture labels to floor, history preserved in JOURNAL.
- **M2 — INV-246 lean-orchestrator arm (ROADMAP 443).** A Stop-hook soft signal summing raw file content read inline per
  session and counting worker dispatches; warns only at/over threshold with zero dispatches. Whole-transcript scan,
  threshold default 50 KiB tunable, off by default / opt-in / library-classified. hooks/lean-orchestrator-scan.py + 19 tests.
- **M3 — prose-quality sweep (ROADMAP 444).** No invariant, no behaviour change; linters to floor on every swept file —
  PRODUCT_SPEC register lines, spec-author SKILL (102→0), adopt/ADOPT.md (34→0), .live-spec/profile.md caps lowered.
  Three recorded-word lines stay verbatim as a deliberate exemption (meaning-bearing).

## Follow-ons (later, non-blocking)
- INV-245: non-coverage of skills/README as a deliberate boundary — DONE (note added inside the clause 2026-07-21).
- INV-246: six-verb Bash-dump escape a documented boundary — DONE (note added inside the clause 2026-07-21).

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
  listener (wait on the harness listener, INV-231) · 438 delivery-separability prover lens · 439 inbox deposit protocol
  · far tier 381, 411, 435, 436/437.

## Inbox (2026-07-21) — both deposits routed, left earned in place (row-430 precedent, no delete under a live writer)
- tlvphotos delivery-separability wish → ROADMAP 438; Alexander 2026-07-21: 438 and this whole file are one and the
  same, so section 3 (dual-as-discovery-heuristic) was FOLDED into row 438 (no separate row). Scope/greenlight on his word.
- `from-owner-verify-code-state` (row 430) → BUILT this session as INV-247 (awaiting the landing push). Left in inbox.
ROADMAP 439 (inbox deposit protocol for concurrent windows) still queued, open design fork his (completeness signal).

## Next free codes
Next free INV-247, E-36, T-25, M-432, next ROADMAP row 445.

## Research in hand
Direct-protocol research (scratchpad research-agent-transport.md + research-direct-channel.md): A2A re-invents our
card; prior art docs/research/2026-07-17-agent-routing-prior-art.md.
