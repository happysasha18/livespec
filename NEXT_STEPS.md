# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

Sessions 28–29 landings (structure/openers/English/nesting/SPEC.md→PRODUCT_SPEC.md rename; readability sweep;
prover-wish INV-72) are committed history — full detail in JOURNAL.md.

## LIVE STATE (2026-07-09, session 29)
Versions: pack 0.9.5 · base 0.1.25 · communicator 0.1.40 · product-prover 0.1.14 · spec-author 0.1.22 ·
build-pipeline 0.2.42 · publish 0.1.3 · test-author 0.1.1 · PRODUCT_SPEC v0.16.3 · ARCHITECTURE v0.2.4.
**Suite 225 green, 0 red.** Persona = PROJECT MANAGER, plain words. Opus (Fable pulled 2026-07-07).
Minor pre-existing: communicator rule 10 trips `machine-jargon:questionnaire` (not gated; likely false positive).
**RUN items 1-3 PUSHED 2026-07-09 (`1eb7530`)** on his go ("after 3 and 5 you can push") — INV-72
prover-wish · feature-coverage trace E-29/INV-73 · the 7 small holes rows 173-179. Pre-push gate green.
Records: `docs/prover/2026-07-09-feature-coverage-trace.md`, `docs/prover/2026-07-09-small-holes.md`. Rows
173-179 marked landed in ROADMAP (archive at the item-7 milestone). **Next push gate: after item 5** (his
word); items 4-5 land local, push together after 5. Still open, NOT push-blockers: PLAYBOOK profile count "14 rules
+ 8-check" — separate repo, his call to bump. Deployed skills re-sync (`sync-skills.sh`) owed before push.
NEW: a wish arrived from the tlvphoto window into `inbox/2026-07-09-tlvphoto-worker-liveness-across-clear.md`
(bg-worker resume across /clear) — UNHARVESTED, deserves proper intake. The 2026-07-09 FULL re-prove folded
3 real body defects (stray `</content>` tag, two stale skill-count ordinals, stale ARCHITECTURE header) and
queued 7 latent design findings as rows 173-179; record: `docs/prover/2026-07-09-full-reprove-session29-body.md`.

## 1.0 BAR (2026-07-09, his decision this session — the finish line for this push)
**1.0 = everything below done HERE, EXCEPT two field items that ride real windows post-1.0: the
remote/cloud session, and the REAL tlvphoto migration (writing into tlvphoto's tree).** Still IN, before
1.0, all in THIS window: prover-seam-hunt · spec-format-by-type · the 7 small holes (rows 173-179) ·
authoring-terminology · **architecture tiers by type + its READ-ONLY validation over tlvphoto (his words:
"кажется ДО, но это ТУТ, в стороне" — touch nothing)** · **NEW wish: project onboarding — how the user
discovers what they can customize** (`docs/wishes/2026-07-09-project-onboarding-what-can-i-customize.md`;
kind/budget/profiles/skill-fit/settings-ladder). MIGRATION READINESS (his Q): ADOPT.md is mature + proven
once (tlvphoto 2026-07-04), BUT the type-aware format + prover-seam-hunt are prerequisites — build them
here FIRST → read-only sim here → real migration in tlvphoto's OWN window (this window audit-only).

## 1.0 RUN — the loop's charter (ordered; resume COLD from here · project = live-spec · cwd ~/live-spec)
Each item walks the full pipeline (build-pipeline skill). **LOOP** = closeable autonomously here. **PARK** =
build to the named gate, then STOP for his word — never ship past his taste gate. The run is NOT done when the
queue drains: each item's real done-state is the proof, never a green suite alone. Memory may be wiped — all
state lives in this file + `docs/wishes/` + ROADMAP + JOURNAL; the working contract (language, timestamp,
plain-words) lives in his profile + the installed hooks, not memory.

1. **Prover-seam-hunt — DONE** (INV-72, commit `c1ef03b`; detail: JOURNAL 2026-07-09 session 29).
2. **Feature/flow spec format by project type — DONE** (E-29/INV-73; commit below). The format lives in
   spec-author ("primary unit — one per project type"); the two-way check `TestFeatureCoverage` is green
   (M-180/M-181); live-spec's nine scenarios carry `[feature: F-x]` tags mapped in ARCHITECTURE's Feature
   coverage table. Deferred by name: render-time clickable cross-links (render-doc.py has no anchor
   resolution yet — named in spec-author as intended, not claimed built). Detail: JOURNAL 2026-07-09.
3. **The 7 small design holes — DONE** (rows 173-179; commit below). Each landed as a SPEC/ARCHITECTURE
   clause + a string test in `TestSmallDesignHoles`: deferred-trigger re-scan in the milestone gate ·
   T-9 resume re-fence (crit 6) · milestone = indivisible pen-stage vs bug · held-for-milestone state named
   apart from bug-parked · lane-claim tie-breaker (git ancestry / session token) · tight-rung rollback ·
   ARCHITECTURE INV-67 prose. No new anchors; short-form prove. Detail: JOURNAL 2026-07-09.
4. **Authoring terminology + rename — DONE (local, pushes with 5).** Coined "needle" → "traceability
   check-phrase" across live surfaces (the extract tool's `trace_phrases_in`, spec-author, prose-gate design
   doc; test loop-vars left as internal iterators; filename kept for the dated records). Standard-vocabulary
   crosswalk added to spec-author (ISO 29148 · arc42 · C4 · ISO 25010) + a lineage pointer in ARCHITECTURE.
   Test `TestAuthoringTerminology`. Detail: JOURNAL 2026-07-09.
5. **Architecture tiers by project type — DONE (local, pushes with 4).** (b) node structure PROPOSED by
   `project.kind` (INV-36): a per-kind scaffold in the ARCHITECTURE template + build-pipeline step 3 pointer;
   test `TestArchitectureTiers`. (c) ran the method READ-ONLY over tlvphoto (touched nothing; derived doc in
   scratchpad, opened for him) — found + folded two scaffold gaps: a derive-pipeline tier (data/ML) and the
   static-first + edge-backend blend. tlvphoto doc NOT committed (another project's internals stay out of the
   public pack). Detail: JOURNAL 2026-07-09.
6. **Project onboarding — PARK at mockup.** Wish `docs/wishes/2026-07-09-project-onboarding-what-can-i-
   customize.md` (how the user discovers what they can customize: kind/budget/profiles/skill-fit/settings-
   ladder). VISIBLE surface ⇒ mockup-first (prototype-norm): build a labelled mockup on real data, STOP, his
   eye sets the bar before the spec delta.
7. **Then 1.0:** milestone gate (M-1 3-pass audit) → bump 1.0.0 → push on his explicit "go" (never without it).

POST-1.0 (his bar, NOT in the run): remote-seat cloud session · REAL tlvphoto migration (its own window).
His-word backlog, not 1.0 blockers: chat-cleanliness `Stop`-hook backstop (lints my reply + self-scan; touches
his settings) · readability-restructure operation (word-preservation verifier + procedure) · row 171 no-hooks/
no-GitHub · row 148 plainer-spec rewrite · thin-loader tidy in his `~/.claude/CLAUDE.md` · pack orchestration ·
artifact registry.

## Field legs + standing habits (ride real windows / always-on)
- Field legs with him (real windows): 47/96 feedback loop · 54 first-run · 165 first-struggle · 168 remote
  seat · 134/141 zero-drift · 143 · 144 · 140 · 117 · 129 · 133. (ROADMAP holds the full rows.)
- Standing habits: `date` before ANY stamp · NOW/NEXT current + heartbeat past ~10 min (INV-71) · plain
  product words, never a code leading a line (INV-28), say "live-spec" not "пакет" · inbox EMPTY · unharvested
  inbox wish `2026-07-09-tlvphoto-worker-liveness-across-clear.md` awaits proper intake.
