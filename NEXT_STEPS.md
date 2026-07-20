# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## ON RESUME (2026-07-20 — driving the queue on Alexander's word: whole NEXT_STEPS to victory except the far ideas, max agentic, conserve context, push/deploy as needed)
Push on green (his grant). A taste/policy fork stays an explicit question. Re-test every "needs his word" by
derivability FIRST. **AXES-FROM-KIND movement CLOSED at v3.2.0** (INV-244, pushed) — the full pipeline ran
(spec → prove → design-review → architecture → matrix → red-first tests → wire → compact → verify), records
committed. The next in-loop work is the two movements Alexander named this session: the history/project-refs
cleanup out of the specs (ACTIVE NEXT below), then the lean-orchestrator guard. BEFORE resuming any
deferred/queued item, re-derive its state from the CODE, not this file's words.

## ACTIVE NEXT — history + project-refs cleanup out of the specs, with a gate (Alexander's word 2026-07-20)
His ruling: history and references to other projects belong in side files (JOURNAL, research, fixtures), never
in the specs themselves. Found in the three core specs: PRODUCT_SPEC.md (18), TEST_MATRIX.md (17),
ARCHITECTURE.md (4) mentions of track-coach / tlvphotos / promoter — two kinds: provenance/history ("came from
the tlvphotos bug") that belongs in JOURNAL, and kind-fixture example names. Clean ALL of it (rule already
holds: history → JOURNAL, spec states the RULE not the project). Build a GUARD: a guardrails/ check reds when a
core spec carries a project name or a provenance turn. Runs in the loop; part of migration for all projects.
This is derivable work (his stated rule) — do it, do not park.

## Then — the lean-orchestrator guard (Alexander's word 2026-07-20). Memory [[lean-orchestrator-needs-a-guard-not-more-prose]].
Context keeps leaking because lean-orchestrator is the one load-bearing rule with no mechanical net. Do NOT add
more prose (it is already in the profile). Build a soft signal, like the chat approach: a Stop-hook that counts
raw file content held inline per session without spawning a worker and warns past a threshold. Enters through
spec-author + product-prover (a new INV) like any behaviour.

## Queue — prose-quality debt sweep (derivable, one CLASS)
Pre-existing register-lint debt in PRODUCT_SPEC.md (12 lines: "full rigor", "wish door", self-sincerity) +
whole-file style-lint debt in skills/spec-author, adopt/ADOPT.md, .live-spec/profile.md (caps-shout, second
person, scissors on untouched lines). One class: a prose-quality sweep across pack docs, gated by the register
+ style linters returning to floor. Mine by derivation (INV-83); land as its own small movement.

## Migration readiness (2026-07-20) — when can other projects migrate?
Other projects (track-coach, tlvphotos, promoter) should NOT migrate yet; the block is Alexander's word, not
build work. The pack version is in motion (v2.8.3 → 3.2.0 this session). tlvphotos migrates onto the axes
release (v3.2.0, now shipped) — its concrete vehicle, fixing the live mobile device-parity gap; that migration
is its own next step on his word. The polished on-ramp (movement 3, onboarding) is DEFERRED on ~8 taste forks.
Two open questions bite these projects: framework coexistence and the "superpower" competitor positioning.

## Open movements
2. **Axes-from-kind — CLOSED v3.2.0 (2026-07-20).** INV-244: a surface's composition axes derive from
   project.kind; visual kinds owe input-capability (first member of an open set), owed-vs-covered gap is a
   finding, values are combinable capabilities, per-kind axis set a mandatory flag-if-absent `project.axes`
   declaration. Records: docs/prover/2026-07-20-axes-from-kind.md, docs/skill-review/2026-07-20-spec-author-axes.md.
   Follow-ons (deferred, [target]): the forcing step for the in-between value of every axis; the recursive
   similarity sweep over the axis registry (ROADMAP 437); the other kinds' elementary axis sets, each its own increment.
0. **Conduct audit — CLOSED v3.1.0.** INV-241/242/243. Follow-ons: rows 431, 432, 435 (far).
1. **Comms/naming — CLOSED v3.0.0.**
3. **Adoption + onboarding — DEFERRED (his 2026-07-18 word).** Designs docs/design/2026-07-18-*.md. FORKS:
   preset values; default preset; ask-vs-infer; 2/3 presets; pre-push home; plan-axis scope; welcome shape;
   registry placement. Owns the parameters registry (ROADMAP 427).

## Captured future ideas (owner-held for scope)
- **Living everything principle.** Any shared artifact can be living. Living description (INV-240) + registry (427) are its first two.
- **After-the-fact user-tell family (ROADMAP 428).** An 11-member class; one clause; on his word.
- **Framework coexistence at onboarding + README** — name the boundary if a person already runs another framework.
- **Evaluate the "superpower" skill as a competitor + README.**

## LIVE STATE (2026-07-20 — v3.2.0 pushed; suite 1693 green, redundancy floor 0)
Shipped this session: v2.8.3 (hedge gate) · v2.9.0 (comms machinery) · v3.0.0 (back-describe) · v3.1.0
(conduct audit) · **v3.2.0 (axes-from-kind, INV-244)** — VERSION + 10 skills + plugin.json stamped, spec base
re-frozen, records committed, pushed (3d7f542). Working tree clean. Memory: the axes movement is wipeable.

## Standing word / OWNER-HELD
- Whole movement solo, push on green; plain English in docs, plain Russian in chat; gates mandatory. Max agentic,
  conserve orchestrator context (delegate reads/drafts; hold briefs + decisions).
- **lean-orchestrator:** the seat authors nothing long and reads nothing past a glance inline; drafting and non-glance
  reads go to workers. Tunable per-person, default strict. (Its own guard is a queued movement above.)
- CONCURRENCY: multiple windows share ~/live-spec. Commit narrowly by explicit path, never git add -A; re-check HEAD
  before writing (the fence — `guardrails/fence-refresh.sh` to re-arm after accounting for a move). `.spec-freeze/`
  re-frozen in the landing commit (`python3 scripts/spec-freeze.py --freeze PRODUCT_SPEC.md ARCHITECTURE.md TEST_MATRIX.md --compaction`).
- **Row 421 (open, Alexander's call):** one window ruling several instance-agents against the one-window law.

## Queue's open head (field-gated + far tier)
- 385 first real contract · 389 cross-machine read · 247 remote-deposit field leg · 396/405 conversation channel +
  listener (wait on the harness listener, INV-231) · far tier 381, 411, 435.

## Inbox (2026-07-21)
Row 436's smallest-first slice landed in v3.2.0 (INV-244); 436's rest (value-space forcing, other kinds' sets)
and 437 (recursive sweep) stay deferred. New wish swept to ROADMAP 438 — the delivery-separability prover lens
(the dual of composition), Alexander's tlvphotos catch, scope on his word. The `from-owner-verify-code-state`
deposit (row 430) stays in inbox, un-swept.

## Next free codes
Next free INV-245, E-36, T-25, M-430, next ROADMAP row 439.

## Research in hand
Direct-protocol research (scratchpad research-agent-transport.md + research-direct-channel.md): A2A re-invents our
card; prior art docs/research/2026-07-17-agent-routing-prior-art.md.
