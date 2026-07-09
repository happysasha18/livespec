# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

**SESSION 28 DONE (2026-07-09) — STRUCTURE pass + positive-opener pass. He pre-approved the grouping
(«отличная структура»). COMMITTED LOCAL (`21d9a34`), NOTHING PUSHED.**

The flat docs now read as trees, and every define-by-exclusion opener leads positively. Both were shown as a
grouping proposal first and approved before any restructure.
- PRODUCT_SPEC.md — 20 flat `##` sections became one opener + 7 named parents (the build loop · what the human sends
  back · when something breaks · starting and adopting a project · the rules and who applies them · what holds
  the bounds · reference). Done by a deterministic script: content + every bracket anchor preserved (431→431),
  each parent gained one plain orienting line. Version → v0.16.0.
- communicator — the 22 rules gather under 6 named groups, the 16 register rules under 5; each rule keeps its
  OWN number as a quiet trailing anchor `*(rule N)*` (numbers are stable IDs cross-referenced widely, incl.
  a 15/16 collision between the two lists — so no renumber). Version → 0.1.40.
- positive-opener pass — the "Not for X" / "You are not" openers across product-prover, spec-author,
  build-pipeline, live-spec-base, publish, test-author + the TEST_MATRIX template now lead with what to DO;
  the honest exclusions stay. Borderline lines where the negation IS the content (missing / not-buildable)
  reworded to lead positively without losing the fact. Living SPEC/ARCHITECTURE/README/OVERVIEW were already
  clean. base → 0.1.25 with the pin swept across all 7 working skills; touched skills patch-bumped.
- LEFT clean by design: docs/spec-style.md's own R13 rule DEFINITION ("Open with what a thing IS, never
  define it by exclusion") already leads positively — distorting a definition to appease the linter is wrong.
Suite 207 green, 1 expected pre-push red (prover-record, M-6). deployed NOT re-synced to repo yet (skills
changed) — a `scripts/deploy` refresh is owed before he relies on the installed copy.

## LIVE STATE (2026-07-09, session 28)
Versions: pack 0.9.0 · base 0.1.25 · communicator 0.1.40 (6 groups + register in 5) · product-prover 0.1.13 ·
spec-author 0.1.19 · build-pipeline 0.2.41 · publish 0.1.3 · test-author 0.1.1 · SPEC v0.16.0. Suite 207 green
(1 expected pre-push red). main HEAD = `21d9a34` (this session's restructure, LOCAL); origin behind. Reporting
persona = PROJECT MANAGER, plain product words. Runs on Opus (Fable pulled 2026-07-07).
Open before a push: (1) a product-prover pass covering BOTH the session-27 scissors sweep AND this restructure,
its record `docs/prover/2026-07-09-*.md` (SPEC M-6); (2) re-sync deployed==repo (skills changed); (3) the
profile count in the PLAYBOOK repo still reads "14 rules + 8-check" — separate repo, his window, his call to
bump to "16 + 10".

## ACTIVE PLAN (2026-07-09 afternoon — his ask, delegated to me; decisions locked below)

He wants the whole pack to read in good native English with one complete thought per paragraph — these
are GUIDELINES that every future project will inherit, so they come before terminology and before any
migration. Order he and I agreed: **English + paragraph sweep → product-prover pass → build the
feature/flow format → authoring-terminology corpus.**

1. **English + one-thought-per-paragraph sweep** (ACTIVE). Every reader-facing file to good English, long
   paragraphs split so each holds one thought. DONE: «покажи все фичи» → "show me all the features"
   everywhere; communicator + build-pipeline fully de-Russified + split (both calque examples turned to
   clear English, test check-phrases synced in lockstep). LEFT: paragraph-splitting of the already-English
   docs (SPEC, ARCHITECTURE, README, OVERVIEW, other skills). Rules: (a) prose/glosses → English; (b) his
   dated quotes + ❌/✅ examples → English paraphrase keeping date, a minimal Russian token only where the
   lesson is about a Russian-language pitfall, glossed; (c) FUNCTIONAL Russian STAYS — the detector
   `spec-style-lint.py` + the `tests/test_prose_gate.py` fixtures implement Russian-form detection. CAUTION:
   some doc strings are matched verbatim by the suite (`tests/test_traceability.py`) — translate doc +
   check-phrase IN LOCKSTEP. ROADMAP verbatim quotes (~big) = a separate later call.
2. **Chat cleanliness (decided by me, per his delegation).** Harness recon done: Claude Code cannot edit or
   block my outgoing reply before it shows — no hook rewrites it; the `Stop` hook can only READ
   `last_assistant_message` and force a follow-up correction; clean pre-display gating needs a TypeScript-SDK
   wrapper (`MessageDisplay`), which is outside Claude Code. PLAN: build a `Stop`-hook backstop that lints my
   reply (scissors + honesty-preamble) and forces a visible correction + a defect-log line, PLUS a mandatory
   self-scan before sending. This is why the prover never caught it — the prover and linter read DOCUMENTS,
   chat passes through neither. Migration spreads the RULE to every project but cannot make chat a gated
   surface; the backstop is the strongest available.
3. **Feature/flow spec format (design DECIDED — see `docs/spec-format-by-project-type.md`).** Borrow Kiro's
   ID + back-reference traceability; make the primary spec UNIT a per-project-type parameter (feature ·
   command · rule/guarantee · argument), the way BMAD swaps templates by domain. Keep single documents — NO
   per-feature file sprawl. Source stays plain MD with `[F-x]` codes + one index table; clickable links are
   generated at render, not hand-written. Coverage check (both directions: every unit has an
   implementer + test; every implementer traces to ≥1 unit) generalizes the existing `[target]`↔row and
   M-x↔test checks. Build AFTER the prover. This is queued (b) architecture-tiers realized, ties to (a).

## Forward queue (mirrors ROADMAP.md)

1. **DONE and PUSHED:** humanize movement · 0.9.0 milestone · three laws — INV-70 (agent sets tunable
   parameters and tells) · INV-28 pre-show jargon guard · INV-71 (live NOW/NEXT status in any seat, resolves
   the live-board ask row 166). No autonomous rows remain that don't need his word.
2. **Needs HIS word or a real window:** remote-seat session — this evening/tomorrow (also proves INV-67/71 in
   a real cloud seat) · make live-spec work with NO hooks / NO GitHub (row 171, large) · rewrite the spec as
   an even plainer document (row 148, large) · thin-loader tidy in his personal `~/.claude/CLAUDE.md` (move
   the window-list + stale "Fable only" note to his profile — his file, offered) · pack orchestration
   (2026-07-08, his ask): take independent work while a spawn runs (no idle-block) + spawn-liveness watchdog
   (hung / silent-too-long / alive) — [[pack-orchestration-parallelism-and-spawn-liveness]], ROADMAP rows ·
   artifact registry (2026-07-08, his ask): a per-project index of handed-in artifacts surviving /clear,
   recording WHERE each lives (Keychain name / path), never the secret value — [[artifact-registry-pointers-not-secrets]].
   · **NEW 2026-07-09 (his ask this session):**
   (a) **Authoring terminology + corpus.** Research the accepted vocabulary for authoring specs and architecture
   (requirements engineering, arc42, C4, ISO/IEC/IEEE 29148, plus BMAD and Kiro); build a small glossary-corpus;
   replace coinages (the test check-phrases are called "needles" in code and "иголки" in chat — both grep slang,
   his allergy-kin — rename the code variable to `trace_phrase` and speak of "traceability check-phrases");
   enrich the spec-author and architecture vocabulary from the corpus.
   (b) **Architecture tiers by project type.** ARCHITECTURE now reads as a flat technical reference; BMAD/Kiro
   give architecture explicit layers. Make its structure classifier-driven: a web/app project names frontend /
   backend, template / renderer; a methodology-package like live-spec names skills and nodes. Deliver explicit
   architecture-authoring instructions per project type.
   (c) **Validate (b) by a side test-run on a different project TYPE.** Run the method read-only over tlvphoto
   (a web gallery) as a pack case study — touch nothing in its tree — to see what architecture doc the method
   yields and whether the frontend/backend, template/renderer layers surface. His word: do this AFTER he resets
   my memory.
3. Field legs riding real windows with him: 47/96 feedback loop · 54 first-run · 165 first-struggle · 168
   remote seat (this evening) · 134/141 zero-drift · 143 · 144 · 140 · 117 · 129 · 133.
4. Standing habits: `date` before ANY stamp · NOW/NEXT current + heartbeat past ~10 min (INV-71) · plain
   product words, never a code leading a line (INV-28), say "live-spec" not "пакет" · inbox EMPTY.
