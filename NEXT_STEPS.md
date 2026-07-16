# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-16 morning — a multi-feature movement toward v2.1.0 IS IN PROGRESS)
Local commits are AHEAD of origin and NOT pushed (batching). VERSION is still 2.0.0. The batch-end MINOR
gate + version bump to 2.1.0 + a single push is PENDING. Suite 846 green, tree clean. Resume COLD from
JOURNAL.md + the three prover records under docs/prover/2026-07-16-*.md + this file.

**Landed this session (local main, ahead of origin — each its own commit, one row per landing):**
- **Row 337 / №5 — browser-mute machine gate.** INV-157 third net: `guardrails/check-muted-launch.sh`
  reds a tracked script whose code launches a real headless Chrome with the mute flag nowhere in it;
  wired pre-push gate l + CI. A fresh-eyes audit folded two evasions (comment-only mute, docstring-only
  flag). Inbox note dropped to tlvphotos to adopt the muted harness. Matrix M-315..M-319.
- **Row 338 / INV-166 — style lint two tiers.** `--tier universal` (universal laws as gate, register
  advisory) and `--tier full` (alias `--gate`, unchanged). Universal tier = scissors, negation-opener,
  machine-jargon, provenance-narrative. Declared in docs/spec-style.md. Harvested track-coach wish. M-320.
- **Row 339 / INV-167 — prover entry-state lens.** A re-enterable surface declares the state entry opens
  in (position/focus + reset-or-resume); owned by spec-author, carried by the prover beside entry-symmetry
  (INV-50). Harvested tlvphotos prover wish. M-321. Record docs/prover/2026-07-16-inv166-inv167.md.
- **Row 340 / INV-168 — prover parent transition-payload lens.** From the Fable audit's D1: the prover
  checked the state graph's topology but never a transition's payload (focus, scroll/playback, sound, a
  timer, a fresh-or-stale value). INV-168 enumerates the parameters a person perceives across every stated
  transition; INV-165/167 become its instances, ending the one-invariant-per-bug loop. M-322. Record
  docs/prover/2026-07-16-inv168.md.
- **Fable deep+adversarial audit of the prover DONE** — docs/audit/2026-07-16-prover-fable.md. D1 folded
  (INV-168 above). REMAINING folds queued below (D2-D5, R1-R5).
- **Global scissors Stop-hook** — `~/.claude/hooks/scissors-scan.py` + `~/.claude/settings.json` Stop hook.
  Flags the «X, а не Y» / «X — not Y» frame in an outgoing reply, all windows. Owner's 2026-07-16 word:
  an empty intensifier/contrast enrages him; reformulate, talk human. Memory: no-empty-intensifiers-talk-human.

## ON RESUME — the queue (the adoption spine first, then the rest)
- **RUN NEXT: fold the remaining Fable audit findings** (docs/audit/2026-07-16-prover-fable.md; D1 done):
  D2 — FEATURE-FIT second-sibling blind window (intake question "second member of an existing kind?" →
  scoped design review); D3 — CROSS-LINK never re-checks old quantified claims (mandatory quantifier/
  enumeration re-verify); D4 — surface-authority lens self-disarms (fallback = a stated assumption, never
  silence); D5 — FULL-mode Phase 3e has no coverage record (split mandatory sweeps vs discretionary probes
  + a surface×sweep table). Then R1-R5 (motion-gap boundary, merge the 5 lifecycle lenses under INV-168,
  FEATURE-FIT scope wording, clause currency, [default] accretion sweep).
- **Task 13 — turnkey ratchet-adoption package** (the spine that makes host-update one pass): vendor the
  lint/freeze/debt-cap scripts + source-pin + guard test + install recipe; seed baselines at the host's
  CURRENT size (green at once, ratchets down; no full re-compaction). INCLUDES HOOK PROPAGATION — the pack
  ships canonical hooks, adoption installs them into the host's .claude/; split personal-profile hooks
  (owner's Russian patterns) from universal pack hooks (English scissors). Depends on task 12 (landed).
- **Task 11 — live concurrent-edit detection + config-health gate + LOCAL inbox-notify variant.** Co-located
  sessions share ONE tree + ONE git index; the "notify live-spec" mechanism (built for a remote seat over
  git) collides locally — a neighbour sees a session's staged work. Fix the local variant. Plus: detect
  mid-session another window touching your files; a gate that the hooks/guardrails are actually installed.
- **№4 (task 5)** request→gate extraction + RETROACTIVE MIGRATION (a new gate runs backward over the tree
  at adoption). **№1 (task 6)** upstream update-watcher skill. **№9 (task 9)** version-is-one-fact (every
  skill inherits the pack VERSION, sync stamps it). **№3 (task 4)** remote/teleport → textual, no browser.
  **№2 (task 7)** pin base's scope (pack-internal, owner chose). **Task 10** guardrails/README says 5 gates,
  ~11 exist (docs). **Task 8** compact global MEMORY.md >19KB (owner-side).
- **feedback-collector anonymization** (owner idea): mask a host's real entities before an upstream note
  leaves, consent-first, for enterprise. **Hook tuning:** the scissors Stop-hook false-fires on a
  pattern-demo quoted inside «…» — teach it to skip a quoted demo; fold with hook propagation (task 13/11).

## BATCH CLOSE (when the spine is done)
MINOR gate: full prover on the whole spec + design review + cross-cut counter + code compaction, one fresh
batch audit, bump VERSION → 2.1.0 (+ plugin + spec-header), push ONCE, read the remote CI verdict. THEN drop
one adoption-wish per project (promoter / track-coach / tlvphotos) as the "go" signal.

## CROSS-PROJECT (owner coordinates his own windows; live-spec window is audit-only there)
- Compaction gates NOT adopted in track-coach / tlvphotos / promoter (audited 2026-07-16). Gates are
  MANDATORY (owner's word, rule 30); the pack states mandatory but nothing enforced adoption — the real hole.
- **Promoter:** can wire a gate NOW on DEFAULT mode (its docs pass at 0 errors); upgrade to `--tier universal`
  after 2.1.0. No live-spec update needed for that.
- **track-coach / tlvphotos:** real doc backlog (126 / 79 errors) — adopt via the turnkey freeze-at-current-size
  package after 2.1.0 pushes.

## Standing word / OWNER-HELD
- Do the whole movement solo, push on green; plain English in docs, plain Russian in chat. Fable on his word
  for hard passes. Gates mandatory. NO empty intensifiers/contrast in chat (hook + memory).
- CONCURRENCY: multiple windows share ~/live-spec. Commit narrowly by explicit path, never `git add -A`;
  re-check HEAD before writing (fence). A neighbour committing one inbox file is allowed.
- Next free codes: INV-168, M-322, next ROADMAP row 340. Memory can be wiped — story in JOURNAL + docs/prover/.
