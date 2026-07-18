# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## ON RESUME (2026-07-19 — the 2026-07-18 night loop CLOSED its drainable work; one build stays queued)
The night's loop landed three releases (2.7.1, 2.8.0, 2.8.1), all pushed and deployed. The only queued
BUILD left needs a fresh context by Alexander's word; everything else open is field-gated or owner-held.
Push on green (his grant). Leave every taste/policy fork as an explicit question — do not guess.

1. **Adoption + onboarding movement — BUILD, deferred to a fresh context (his 2026-07-18 word).** Designs
   `docs/design/2026-07-18-adoption-and-resource-model.md` + `2026-07-18-onboarding-design.md`, both carrying
   Alexander's two steers: (a) ask little, default well, reveal the rest — warm welcome + user journey, the
   speed-vs-clarity thread owing a worked "first five minutes" example; (b) his 2026-07-18 ~22:50 steer — the
   welcome explains the whole process in one README-voice paragraph and EARNS TRUST (its language chosen, its
   choices offered as real alternatives "you can do it this way or that"), possibly its OWN sub-skill. Build
   through the full method; guard with SEVERAL clean-context adversarial passes [INV-237]; NO regressions to
   the existing walk. FORKS FOR ALEXANDER (surface, never guess): preset values; default preset (careful vs
   balanced); ask-vs-infer the cost preset; 2 or 3 presets; the one pre-push home; plan-axis scope;
   sub-skill-or-section for the welcome-and-trust layer. Report the onboarding call + the first-five-minutes
   example to Alexander in the morning.

## LIVE STATE (2026-07-19 — three releases pushed + deployed this movement: 2.7.1, 2.8.0 (tag v2.8.0), 2.8.1. origin/main 613f3f8.)

**Landed and released this movement (detail in JOURNAL):**
- **2.7.1 (PATCH, 613f3f8's ancestor 03a4d26)** — product-prover readability: dense lens bullets split into
  nested sub-bullets, de-jargoned README, ARCHITECTURE.md as a valid input. A clean-context skill-creator
  review folded two findings; gate g pins reconciled; gate s satisfied.
- **2.8.0 (MINOR, tag v2.8.0, 06662fb)** — INV-237: the authoring seat does not adversarially certify its own
  work. A release's adversarial pass is authored by a fresh seat, and a new lens/rule is self-applied to its
  own introducing document before release. Base rule 33, wired into build-pipeline's verify station and
  product-prover; owned by the build-pipeline node; M-419. Dogfooded — the release's own adversarial pass ran
  from a clean context and folded four items before the commit. ROADMAP 422.
- **2.8.1 (PATCH, 613f3f8)** — the register judge now holds base rule 2 ("never open a line with a code") on
  chat: a sentence must not LEAD with a bare internal code, the codes trailing as anchors. A second universal
  law in the judge; chat_law() renumbers the joined universal + personal laws into one sequence. ROADMAP 423.

The Formal index is contiguous through INV-237. Full suite green (1589/0). All installed skills + judge
hooks deployed to 2.8.1.

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
- Next free codes: INV-238, E-35, T-24, M-420, next ROADMAP row 424.
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
- Direct-protocol research (scratchpad `research-agent-transport.md` + `research-direct-channel.md`):
  A2A re-invents our card, ACP dead, at-least-once + idempotent the target (401); INV-236's reframe —
  files legitimate as STORE, not TRANSPORT. Prior-art `docs/research/2026-07-17-agent-routing-prior-art.md`:
  Contract Net (1980) is the referral law renamed, carrying the git premise he refused.
