# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## ON RESUME (2026-07-23 — ROW 445 LANDED at v4.0.0: the spec is now a requirements document)
Row 445 landed. PRODUCT_SPEC.md moved to the requirements genre — a preamble, a 229-entry glossary, and 282
numbered requirements (Context + one User Story + acceptance criteria in named cases, lowercase italic keywords,
codes as trailing anchors, [GAP] lines for source holes), closed by a generated 355-code code-to-location table.
Final size 590,695 bytes against the 783,678-byte pre-format source (a 24.6% reduction), 1,372 criteria, 206.8
bytes per criterion (the size ratchet's seed). The format laws live inside the spec as INV-250..271; the format's
own definition is docs/spec-format.md. Where every record lives: the assembly and every edit past a plain
concatenation in prototype/2026-07-22-spec-format/assembly/DELTA.md; the re-pin sweep (about 303 pins moved, 29
verdict-cited retirements) in that folder's REPIN-LOG.md; the fresh full prover audit (lands-with-fixes, all 8
must-fix folded) in docs/prover/2026-07-22-row445-4.0.0-full-audit.md; the register census in
docs/audit/2026-07-22-register-census.md; the text-audit eval in docs/evals/2026-07-23-text-audit/. Riding the
landing: the eleven pack skills rewritten to the register bar, the new text-audit working skill (row 458, the
pack's tenth), and VERSION 4.0.0 across every frontmatter and the base. Push stands on the suite's own green.

## LIVE STATE (2026-07-23 — landing commit in progress; this session is wipeable after the push)
Root PRODUCT_SPEC.md = the restored 12-unit assembly (590,695 B); freeze re-baselined with --compaction; suite at
the pre-commit run: 3 failed, 1806 passed — the two push gates close at the landing commit itself (the prover
record docs/prover/2026-07-23-row445-4.0.0-fix-verify.md must be committed for gate a; gate b mirrors it), the
third was this file's own missing LIVE STATE block, restored in this edit. Next acts: landing commit → full suite
green → push.

## STANDING ORDER — the format family finishes the live-spec docs first (Alexander 2026-07-22)
The method proves itself on its own documents before any host migrates. Order after the spec:
1. TEST_MATRIX.md gets its format (its own follow-on movement in the row-445 plan).
2. ROADMAP.md movements get their format.
3. ARCHITECTURE.md gets its own format definition in the same family (row 456).
Only then does tlvphotos migrate, on his word from its own window; other projects stand until then.

## Near queue after the landing
- Row 460: the register ratchet over the prose corpus — the public and working doc-tier rewrite plus the per-tier
  violation-count ratchet gate seeded from the census.
- Rows 461–468 (opened at this landing): the prover's seven should-fixes (461 F9/F10, 462 F11–F15), the
  surface-registry status defect (463), three assembly sharpens (464), the text-audit lint-and-vocabulary
  interaction (465), the claim-level-drop method improvement (466), spec-author's size and duplication fold (467),
  and the target-ownership verification record (468, green).
- Row 437 pulled near (his 2026-07-22 word): the axis in-between forcing step + the recursive axis-registry
  similarity sweep.

## FIRST at intake — classify one-time vs standing (Alexander 2026-07-21, ROADMAP 440)
Name every request's persistence class before actioning it, and say it yourself. A standing ask owes a permanent
mechanism inherited by every host; the one-time sweep to floor is only its other half.

## Standing word / OWNER-HELD
- Whole movement solo, push on green; plain English in docs, plain Russian in chat; gates mandatory. Max agentic,
  conserve orchestrator context (delegate reads and drafts; hold briefs and decisions).
- lean-orchestrator: the seat authors nothing long and reads nothing past a glance inline; drafting and non-glance
  reads go to workers. Tunable per person, default strict. Backed by the INV-246 soft signal.
- Push on green is his grant; re-test every "needs his word" by derivability first; re-derive deferred state from
  the code itself (INV-247), setting any stale resume note aside.
- Row 421 (open, Alexander's call): one window ruling several instance-agents against the one-window law.

## CONCURRENCY — multiple windows share ~/live-spec
Commit narrowly by explicit path, never git add -A; re-check HEAD before writing (the fence,
guardrails/fence-refresh.sh to re-arm after accounting for a move). The spec base re-freeze rides the 4.0.0 landing
commit (python3 scripts/spec-freeze.py --freeze PRODUCT_SPEC.md ARCHITECTURE.md TEST_MATRIX.md --compaction).

## Migration readiness
Finish all live-spec docs first (see the standing order); then tlvphotos on his word; other projects stand.
Onboarding (movement 3) stays deferred on ~8 taste forks; framework coexistence and the "superpower" positioning
stay open questions.

## Open movements
CLOSED: row 445 spec format v4.0.0 · conduct audit v3.1.0 (follow-ons 431/432/435) · comms/naming v3.0.0 ·
axes-from-kind v3.2.0 (follow-ons: per-axis forcing step, recursive similarity sweep 437, other kinds' axis sets).
DEFERRED: adoption + onboarding (his 2026-07-18 word; ~8 taste forks; owns the parameters registry, ROADMAP 427).

## Captured future ideas (owner-held for scope)
- Living everything principle — any shared artifact can be living (living description INV-240 + registry 427 the first two).
- After-the-fact user-tell family (ROADMAP 428) — an 11-member class, one clause, on his word.
- Framework coexistence at onboarding + README; evaluate the "superpower" skill as a competitor + README.

## Queue's open head (field-gated + far tier)
- 385 first real contract · 389 cross-machine read · 247 remote-deposit field leg · 396/405 conversation channel +
  listener (wait on the harness listener, INV-231) · far tier 381, 411, 435, 436/437. (438 delivery-separability lens
  LANDED v3.5.0; 439 inbox deposit protocol LANDED v3.6.0.) Runnable head is field-gated (contract/listener) + far tier.

## Inbox — all 2026-07-21 deposits routed and landed (438→INV-248, 430→INV-247, 439→INV-249), left earned in place.

## Next free codes
Next free INV-272, E-36, T-25, M-447; next ROADMAP row 470 (A-12, B-4, C-2, D-8, S-1, ACT-4 also free).

## Research in hand
Direct-protocol research (scratchpad research-agent-transport.md + research-direct-channel.md): A2A re-invents our
card; prior art docs/research/2026-07-17-agent-routing-prior-art.md.
