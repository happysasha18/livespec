# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## ON RESUME (2026-07-18 night — context was cleared; one loop drives this movement, in order)
All designs are committed; read each, then execute through the method. Push on green (his grant). Leave
every taste/policy fork as an explicit MORNING question — do not guess. Report at each station.
1. **Close product-prover 2.7.1 patch** (content committed c59ed46 — dense-lens-bullet splits + de-jargoned
   README, validated by three clean-context adversarial reviews). Bump to 2.7.1 via `scripts/stamp-versions.py`,
   run skill-creator's review, run the gate chain, push. Pre-existing register-lint on SKILL.md:203/215
   ("say so plainly") is OUTSIDE the delta — it must not block.
2. **Land the clean-context review rule as a MINOR** — design `docs/design/2026-07-18-clean-context-review-rule.md`
   (new INV-237 + base rule + build-pipeline/product-prover reference). Review it FROM A CLEAN CONTEXT (dogfood).
3. **Build the adoption + onboarding movement as a MINOR** — designs `docs/design/2026-07-18-adoption-and-resource-model.md`
   + `2026-07-18-onboarding-design.md`. Principle: ask little, default well, reveal the rest; warm welcome +
   user journey; the speed-vs-clarity thread owes a worked "first five minutes" example (report to Alexander
   in the morning). Build through the full method. Guard with SEVERAL clean-context adversarial passes; NO
   regressions to the existing walk. FORKS FOR ALEXANDER (surface, never guess): preset values; default preset
   (careful vs balanced); ask-vs-infer the cost preset; 2 or 3 presets; the one pre-push home; plan-axis scope.
4. **Also owed:** the bare-code register-judge extension (flag a row/INV number leading a chat sentence — the
   "talking to myself" fix; chat can't be hard-gated, so it's the post-hoc judge). Raw reader results in the
   scratchpad: `adversarial-findings.md`, `adoption-movement-findings.md` (may not survive a fresh session).

## LIVE STATE (2026-07-18 — 2.7.0 released: commit c74b8f2 + tag v2.7.0 both pushed. A 2.7.1 patch + two MINORs are queued in ON RESUME above.)

**2.7.0 is cut (MINOR, per INV-217): the movement since v2.6.0 closed 34 ROADMAP rows and added 39
invariants (INV-198…INV-236, the Formal index contiguous through 236).** VERSION stamped to 2.7.0 across
plugin.json, the spec title, and every skill frontmatter (version-only diff); the dated 2.7.0 MIGRATION.md
chapter names what a host adopts at catch-up; the release prover record
(`docs/prover/2026-07-18-release-2.7.0.md`) certifies the index contiguity, gate w (26 gates each with a
red proof), gate u (CI mirror), the green suite, and the three high-stakes landings' adversarial
corrections. **The release commit (c74b8f2) and the annotated tag `v2.7.0` are both pushed to origin. 2.7.0 is fully released.**

What landed this movement (detail in JOURNAL): the register judge (INV-203, replacing INV-83's retracted
growth duty); the new push gates o…z (cleanup-notice, touchpoint-kind, waiting-list, authority-anchor,
skill-review, doc-rotation, CI-mirror, judges-listed, every-gate-can-fail, index-prose, agent-card,
doc-bound); doc rotation + size bounds (INV-209/233/234); the far tier (INV-222/223); the touchpoint frame
+ waiting list + read-back (INV-205/206/207); the lane-open act (INV-214); worker-teardown reap + the
runaway-child notice (INV-213/230); the reach classes as host config (INV-224); versioned founding
questions (INV-227); the release-tier rule itself (INV-217).

## What REMAINS — the queue's open head

The rows still open are the FIELD-GATED legs (each needs a real machine event the harness has not shipped
or a real cross-machine run) and the FAR tier (held by the owner's word). Nothing here blocks the 2.7.0
push; these are the next movement's work.

- **385 — the first real contract.** The layer's owed arm: an actual cross-agent contract exchanged and
  answered, not a fixture. Field leg — waits on two live agents on the machine.
- **389 — a real cross-machine read.** The remote-read grant (INV-232) is stated and tested; the real
  read across two machines is the field leg that proves it.
- **247 — the remote-deposit field leg.** The inbox remote arm works today via the git store road; the
  live remote deposit across machines is the untaken field leg.
- **396 conversation channel + 405 firing.** The no-answer road (git store) works today [INV-112]; the
  conversation channel's real first use and the listener tripwire firing both WAIT on the harness shipping
  a listener (INV-231). Machine-gated, not design-gated.
- **The far tier — 381 and 411.** Kept, no revisit trigger (INV-222); out of the what's-left answer,
  offered on ask. Held by the owner's word; 382 is their law, 403 their rare self-surfacing line.

## Standing word / OWNER-HELD
- The whole movement solo, push on green; plain English in docs, plain Russian in chat. Gates mandatory.
- **The lane count is the person's plan** (row 414 landed the re-home): the law's "three" moved from the
  spec text to his profile as a plan-and-budget setting.
- **Agents declare themselves** (his 2026-07-17 word): a tree carrying `.live-spec/agent.md` has declared
  itself; discovery is a bounded live scan for cards; five of the machine's six trees carry no card today,
  so a scan now under-reports — row 387's gate (gate y) is the instrument, the cards themselves the field
  work. Real trees, swept 2026-07-17: tlvphotos (instance) · exhibition-engine (engine) · promoter
  (engine) · promoter-alexander (instance) · `~/.claude/skills/track-coach` (the real one; `~/track-coach`
  an inbox-only stub) · tc-cloud-validate (a frozen clone). **Card wishes dropped 2026-07-18** into tlvphotos (folded
  into the 2.7.0-adopt wish), promoter, promoter-alexander, and track-coach's inboxes, each with
  a filled draft card; exhibition-engine has no inbox dir yet, so its channel is unopened and it
  is flagged, not written. Each owning window writes its own card (write-ownership grants it).
- CONCURRENCY: multiple windows share ~/live-spec. Commit narrowly by explicit path, never `git add -A`;
  re-check HEAD before writing (fence). A co-located deposit is the FILE ALONE (INV-174, INV-175).
- **The clock is read, never continued** — read it at each prompt (INV-24).
- Next free codes: INV-237, E-35, T-24, M-419, next ROADMAP row 422.
- **Row 421 (queued 2026-07-18, OPEN DESIGN QUESTION, Alexander's call):** how an open-source engine
  and its instances live as separate repos, and how ONE window rules several instance-agents against
  the one-window law. The two-repo split is verified and justified (exhibition-engine + tlvphotos,
  promoter + N planned instances); the unaddressed part is the single-window orchestrator over many
  instances, to resolve with the far-tier orchestrator view (row 411). Human-only fact: this is a
  POLICY and architectural-taste call — the rule's content is Alexander's to set, the row only holds
  the question. Findings + his stated model captured in `docs/design/2026-07-18-window-model-and-transport.md`
  (window = fluid working set; files = base transport; channels = push into OPEN windows, gated on the
  unverified approved-vendor question; waking an idle window needs the harness).

## Research and records in hand
- `research-agent-transport.md` + `research-direct-channel.md` (scratchpad) — the direct-protocol
  research, done. A2A (Linux Foundation, card at a well-known path, no central registry) re-invents our
  card; ACP dead; exactly-once impossible, at-least-once + idempotent the target (401). The reframe
  INV-236 carries: file-skepticism is right about TRANSPORT, files legitimate as STORE — a receiver that
  is not running is reachable by nothing else.
- `docs/research/2026-07-17-agent-routing-prior-art.md` — Contract Net (1980): its directed contract IS
  this pack's referral law renamed; it carries the git premise he refused, so read it knowing that.
