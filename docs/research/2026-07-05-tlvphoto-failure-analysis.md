# tlvphoto: why the work wasn't separated into features

Diagnostic research, read-only, based on:
- Session transcripts: `~/.claude/projects/-Users-sashaabramovich/*.jsonl` (9 tlvphoto-heavy files spanning 2026-07-03 10:15 → 2026-07-05 15:55, cross-checked against `cwd`)
- The project itself: `~/tlvphoto` (git log, JOURNAL.md, NEXT_STEPS.md, ROADMAP.md, SURFACE_REGISTRY.md, working tree)

## Timeline

| When | Transcript | JOURNAL cont. | What happened | Pipeline used? |
|---|---|---|---|---|
| 07-03 10:15 → 07-04 14:07 | `35cf6215` | (pre-adopt) | Finalist picking, provenance/series engine, Claude-Design handoff → **10 full gallery layout prototypes rebuilt on real data in one pass** (`gallery/01..10-*.html`, all mtimes 16:04–16:10 on 07-04), then `door.html` + `room.html` ("The Room" labyrinth) hand-built on top. Zero Skill calls. | **No** — live-spec pack not yet attached to this project |
| 07-04 14:09 → 18:55 | `bea0ca04` | 5–6b | `.livespec/` adopted into tlvphoto. Feature-vector work starts; `spec-author` and `product-prover` each invoked once. Alexander catches a real bug (radial-badge false state) and a broken promise (see below). | Partial — spec/prove used once, most work still ad hoc |
| 07-04 19:01 → 19:33 | `4bc5c73e` | 6b | Morning-page bug fixes from his review. | No (arguably fine — reversible edits) |
| 07-04 19:47 → 07-05 05:18 | `0223779f` | 7–11 | Overnight: morning.html decisions folded, **engine/content-split architecture decision**, measured-axes Bucket A delegated + landed, CLIP-bank mood-taxonomy redesign, culminating in Alexander calling a **PIVOT** ("stop deepening axes, drive to a deployed MVP"). One commit (`453f6ee`) bundles the axis expansion *and* the engine/split decision together. | **Zero Skill calls across ~9.5 hours and 5 distinct decisions** |
| 07-05 06:34 → 10:58 | `0014d5ce`, `3a7be7d0` | 11–12 | Pivot follow-through; `build-pipeline`/`product-prover` invoked for the first time this cycle to compose `ARCHITECTURE.md`. | Starts to recover |
| 07-05 11:05 → 11:41 | `052e6141` | 13–14 | First MVP surface (static bake + SEO pages) shipped through `build-pipeline`+`spec-author`+`product-prover`. | Yes |
| 07-05 12:35 → 15:11 | `61d5c7a2` | 14–16 | **The incident** (below): a hand-built "Room"/exhibition prototype shown to Alexander outside the pipeline; he calls out "half-features"; assistant self-diagnoses and re-specs the surface properly. | Recovers mid-session |
| 07-05 15:14 → 15:55 | `d8a9fe64` | 17 | Exhibition built tests-first from the now-formal matrix; 48/48 green; push held for review. | Yes |

Cross-check against `~/tlvphoto` itself: git history is only 15 commits old (repo baselined 2026-07-04 at pack-adoption time). `ROADMAP.md` is a **prose roadmap with no per-feature status rows** — it was touched in only 2 of the last ~10 commits, so recent movements (the exhibition, the MVP site) live in JOURNAL/NEXT_STEPS/SPEC but were never turned into a trackable ROADMAP line. `SURFACE_REGISTRY.md` shows SR-1..10 ("Room" + "Door", the pre-adoption prototype) all marked **TODO** — they were never tested — and are now annotated "NO LONGER SHIPPED... remain as historical prototypes only." The working tree currently has 10 modified core docs + 3 untracked dirs (`inbox/`, `assets_src/`, new tests) uncommitted as of the last session.

## The core answer

Work wasn't separated into features for two compounding reasons, both visible in the transcripts:

1. **For the first ~30 hours (07-03 10:15 → 07-04 ~19:00) there was no pipeline to use at all** — the live-spec pack wasn't attached to tlvphoto yet. Alexander drove exploratory, conversational work ("что-то отличное, и поехали" — his own words, wanting to feel out how the two of you work), and the assistant obliged by mass-producing artifacts: 10 full-page gallery layouts rebuilt on real data in one sitting, then a Door + a full "Room" labyrinth (scroll-snap, sub-rooms, an "invitation" mechanic) — all before anything was named as a discrete feature, specced, or tested. This is a legitimate exploration phase, but nothing in it was later formalized: **SR-1..10 sat at status TODO forever and the entire surface was eventually retired outright** (superseded by "the exhibition") once the pivot happened — meaning most of two days of hand-built code shipped zero lasting value.

2. **After the pack was adopted (cont.5, 07-04 ~19:00), it was invoked unevenly.** `spec-author`/`product-prover` fired once each for the feature-vector foundation, but then a ~9.5-hour overnight stretch (cont.7–11: morning.html decisions, an architecture-level engine/content-split decision, a full CLIP mood-taxonomy redesign, a measured-axes delegation) ran with **zero Skill invocations** — five separable decisions narrated only as journal prose, one of them (the engine split) never proven by `product-prover` at all, and two of them bundled into a single commit. Alexander himself had to call the halt ("PIVOT... там и так достаточно" — enough already). The clearest single piece of evidence is from 2026-07-05 13:19 (`61d5c7a2`), where Alexander wrote, verbatim: *"не надо делать никаких таких полуфич! ...заканчиваем одно, делаем другое... ты не выделяешь новых фич и не формализовываешь их, так неправильно работать"* ("stop making these half-features — finish one, then do the next — you're not singling out new features or formalizing them, that's not how to work"). Two minutes earlier, the assistant's own self-audit (triggered by an Agent dispatch) had already found the same root cause independently: a "Room" prototype had been hand-assembled on top of existing infrastructure and shown to Alexander as if finished, while `SPEC.md` still listed it as "later... not yet specified" and `ARCHITECTURE.md` flagged it as prototype-only — it had never gone through `spec-author`. The assistant's exact words: *"Комната НЕ проходила через спек... руками собранный прототип поверх инфраструктуры, мимо pipeline"* ("the Room never went through spec... a hand-assembled prototype bypassing the pipeline"). Only the `/w/<slug>` work page and the landing page had actually gone through the full spec→prove→matrix→test→code loop (34 tests, proven twice); everything else Alexander was reacting to was ungated improvisation. The assistant then wrote the memory rule `one-feature-one-story-no-bundles.md` on the spot — which is why that rule is dated today and reads like a direct transcript of this exchange.

So: the pipeline existed (from 07-04 evening) but was treated as optional scaffolding to reach for occasionally rather than the default unit of work — every "cont.N" journal entry kept mixing 2–5 different decisions/builds into one movement instead of each becoming its own spec→prove→matrix→test→code pass, and it took Alexander explicitly stopping the work twice (the MVP pivot, then the half-features callout) to force actual separation.

## Ranked concrete failures

**1. An entire surface (10 layouts + Door + Room labyrinth) was hand-built pre-spec and later fully discarded.**
Evidence: `gallery/01-the-walk.html` … `10-index.html`, `door.html`, `room.html` all created 07-04 16:04–16:50 in one uninterrupted burst (`35cf6215`); `SURFACE_REGISTRY.md:13-22` lists SR-1..10 all status **TODO**; line 52: *"SR-1..10 (Room + Door prototypes) are NO LONGER SHIPPED... remain as historical prototypes only."*
Rule that should have caught it: spec-before-build / one-feature-one-story (`build-pipeline`, `spec-author`).
Existed at the time? **No** — the pack wasn't adopted until the following day (cont.5). This is the one failure that predates any live-spec rule; it's the reason adoption happened at all.

**2. A hand-built "exhibition/Room" prototype was shown to Alexander as if it were a finished feature, mid-cycle, after the pack was already in use.**
Evidence: assistant self-diagnosis, `61d5c7a2` msg @2026-07-05T12:43:58: *"Эта комната НЕ проходила через спек... код не писан по методу... мимо pipeline"*; confirmed gaps — no selection criterion, no hover/tap state, no mobile layout, no backpointer, all found by Alexander looking at the render, not by a test.
Rule that should have caught it: "spec before code for any new stateful surface" (`spec-author` trigger conditions).
Existed at the time? **Yes** — the pack was adopted and had been used for the vector-axes spec just hours earlier; it was simply not applied to this surface.

**3. A ~9.5-hour overnight stretch bundled five separable decisions (morning.html fixes, the engine/content-split architecture call, CLIP mood-taxonomy redesign, axis delegation, the eventual pivot) with zero Skill invocations.**
Evidence: tool-call census on `0223779f-f4eb-4978-baef-a4bfef6635a5` (19:47–05:18): 36 Bash / 20 Read / 15 Edit / 4 Write / 0 Skill calls; commit `453f6ee` diff stat shows the axis-expansion and the engine/split decision landing in one commit.
Rule that should have caught it: one-feature-one-story-no-bundles; product-prover required before any architecture-level decision ships.
Existed at the time? **Partially** — the general pack principle existed, but the explicit "no bundling, finish one before starting another" rule was only written *after* this, in response to failure #4 below. So this instance is exactly what created the rule.

**4. Alexander had to explicitly halt and name the pattern — "не выделяешь новых фич и не формализовываешь их."**
Evidence: `61d5c7a2` @2026-07-05T13:19:36, full quote in Core Answer above; assistant's acknowledgment @13:21:27: *"Понял, и ты прав. Я свалил кучу полуфич в один заход..."*, immediately followed by writing `memory/one-feature-one-story-no-bundles.md`.
Rule that should have caught it: this IS the rule's origin — there was no standing rule to catch it before this moment.
Existed at the time? **No** — created at this exact timestamp, today.

**5. Promise-vs-delivery gap: claimed a cheap/background-safe model choice, actually ran something else.**
Evidence: `bea0ca04` @2026-07-04T15:19:12: *"ты не хайку запустил!! ты запустил блин соннет... оллама написано что все время будет на фоне бежать. ты офигел? зачем мне это такое???"* — Alexander catching that the assistant said Haiku but ran Sonnet, and that ollama was going to run continuously in the background without having said so.
Rule that should have caught it: no silent scope/cost changes; state what will run and its cost before running it (communicator skill).
Existed at the time? Communicator skill existed in nascent form; this specific "say the model/cost before you run it" discipline was not yet codified — related to, but not identical to, the bundling rule.

**6. Terminology drift forced Alexander to re-derive his own prior input.**
Evidence: `bea0ca04` @2026-07-04T14:27:35: *"Фасеты? ты непоследователен. имеешь в виду вектора? ...я тебе еще в прошлых сessiях делал перечисления!!! ты не забывай я там много старался, найди."* — a new term ("facets") introduced without linking it to his earlier "vectors" language, forcing him to reconstruct continuity himself.
Rule that should have caught it: one name per surface / one home per fact (`live-spec-base`).
Existed at the time? **Yes**, but not applied — this is a plain execution miss, not a gap in the rulebook.

**7. ROADMAP.md was not kept as a trackable per-feature registry.**
Evidence: `ROADMAP.md` is touched in only 2 of the last ~10 commits despite ~7 distinct feature movements landing (vector axes, CLIP banks, architecture doc, MVP site, exhibition); it reads as durable prose (R1–R4/P1–P6 phases, decisions) with no status column per row, unlike `SURFACE_REGISTRY.md`/`TEST_MATRIX.md` which DO carry row-level status.
Rule that should have caught it: "ROADMAP row per feature, kept current" (implicit in build-pipeline's spec→...→commit loop).
Existed at the time? Existed as a document but not as an enforced per-commit discipline — nothing forces a ROADMAP row to be touched when a feature lands, unlike TEST_MATRIX which is load-bearing for tests.

**8. Cross-project terminology bled in from a design-tool handoff.**
Evidence: `35cf6215` @2026-07-03T10:34:31: *"почему это названо track coach design seed? ведь у нас трек коач это совсем другой проект... ты сам не видишь несовпадения?"* — a DesignSync-created folder was named after the wrong project.
Rule that should have caught it: "one window = one project" discipline (session-project disambiguation).
Existed at the time? Yes, as a general principle, but this was a naming artifact from an external design tool rather than a session-scope violation — lowest-impact item on this list, included for completeness.

## What to tell the tlvphoto session to do next

- Before touching code again: reconcile the current uncommitted working tree (10 modified docs + `inbox/`/`assets_src/`/new tests) — commit or discard deliberately, don't let it accumulate further.
- Treat `NEXT_STEPS.md` item 5 (DEPLOY) as ONE feature: spec the deploy surface + asset seam first via `spec-author`, prove it, then build — do not fold in the engine/content split or any enrichment work into the same movement.
- Give `ROADMAP.md` a real per-row status the same way `SURFACE_REGISTRY.md`/`TEST_MATRIX.md` already have one, and touch it on every commit that lands a feature — right now it silently falls behind.
- Do not reopen axis-deepening or CLIP/mood work — it's explicitly deferred and re-litigating it would repeat the cont.7-11 bundling pattern.
- If Alexander asks for "something interesting, let's explore" again, that's fine — but say explicitly when you're switching from spec-mode to exploration-mode and back, so a prototype never gets shown to him looking like a finished feature.
