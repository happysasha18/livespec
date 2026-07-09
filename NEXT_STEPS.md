# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

**SESSION 28 DONE (2026-07-09) — a big foundation movement, ALL committed local, NOTHING pushed. He approved
each step live.** Landings:
- STRUCTURE: PRODUCT_SPEC (20 flat `##` → 1 opener + 7 named parents) and communicator (22 rules → 6 groups,
  16 register → 5) read as trees; rule numbers kept as trailing `*(rule N)*` anchors (no renumber, a 15/16
  collision between the two lists forbids it).
- POSITIVE OPENERS: every "Not for X" / "You are not" opener across the skills + TEST_MATRIX template leads
  positively, honest exclusions kept. (spec-style.md's R13 definition left as-is — it already leads positive.)
- ENGLISH + one-thought-per-paragraph: communicator + build-pipeline fully de-Russified, run-ons split; both
  coined-metaphor calque examples replaced with clear English (his flag: gibberish outside the project). «покажи
  все фичи» → "show me all the features" everywhere. Traceability check-phrases synced IN LOCKSTEP.
- NESTING: communicator's 7 wall-of-text bullets given an inner level (short lead + sub-bullets), words untouched.
- RENAME: SPEC.md → PRODUCT_SPEC.md (+ its template; title "Product Spec"; pairs with the architecture spec);
  path swept across all live files, dated history left, `SPEC INV-x` anchor namespace unchanged.
Suite 207 green, 1 expected pre-push red (prover-record, M-6). deploy re-sync still owed.

## LIVE STATE (2026-07-09, session 29)
Versions: pack 0.9.0 · base 0.1.25 · communicator 0.1.40 · product-prover 0.1.13 · spec-author 0.1.19 ·
build-pipeline 0.2.41 · publish 0.1.3 · test-author 0.1.1 · PRODUCT_SPEC v0.16.0 · ARCHITECTURE v0.2.
**Suite 208 green, 0 red — the FULL pre-push re-prove (M-6) is DONE and recorded, the prover-record gate is
GREEN.** main HEAD LOCAL, origin behind 71. Persona = PROJECT MANAGER, plain words. Opus (Fable pulled 2026-07-07).
Minor pre-existing: communicator rule 10 trips `machine-jargon:questionnaire` (not gated; likely false positive).
**PUSHED 2026-07-09 ~15:04 on his "go" (HEAD `20a458f`, origin==HEAD, all gates green).** Deployed skills
re-synced from repo (8 skills, `sync-skills.sh`). Pin drift cleaned. Still open, NOT push-blockers: PLAYBOOK
profile count "14 rules + 8-check" — separate repo, his call to bump.
NEW: a wish arrived from the tlvphoto window into `inbox/2026-07-09-tlvphoto-worker-liveness-across-clear.md`
(bg-worker resume across /clear) — UNHARVESTED, deserves proper intake. The 2026-07-09 FULL re-prove folded
3 real body defects (stray `</content>` tag, two stale skill-count ordinals, stale ARCHITECTURE header) and
queued 7 latent design findings as rows 173-179; record: `docs/prover/2026-07-09-full-reprove-session29-body.md`.

## ACTIVE PLAN (2026-07-09 — decisions locked; he approved "все как ты сказал")
Approved order: **finish the English/nesting sweep → the prover-wish (2) → build the feature/flow format (3)
→ tlvphoto migration in ITS window (4) → authoring-terminology.** Task 1 DONE + FULL pre-push re-prove DONE.
INSERTED (his ask, approved): build the safe, gated **readability-restructure operation** (word-preservation
verifier + written procedure, through the pipeline) — his word this session; not a push blocker, build when he says.

1. **DONE (session 29, 2026-07-09).** Readability sweep landed. README + PRODUCT_SPEC run-on paragraphs split
   into one-thought-per-paragraph, long enumerations nested as sub-bullets — STRUCTURE-ONLY, word-token diff
   empty vs HEAD, Formal index (tables) byte-identical, traceability green (commit `afab9b3`). ARCHITECTURE +
   OVERVIEW prose already clean (their long lines are tables, not run-ons). De-Russification of live docs was
   already complete (no Cyrillic in the four docs or any SKILL.md). SKILLS: a responsible review (his call —
   "skills were probably fine") confirmed NO prose work needed — the recent scissors/opener/structure passes
   hold, long instruction-bullets are coherent not bundled. The review DID surface two real staleness bugs,
   both fixed (commit `8923969`): live-spec-base said "six skills"/listed five (→ seven, all listed);
   product-prover "Two depths/Both modes" was stale against three review modes (→ "Three modes"). Copy/count
   fixes only, no rule changed, not test-pinned. OPEN for push-prep: version-bump question on the two edited
   skills (I left versions — no rule changed, so no banner cascade; his convention call if he wants a bump).
2. **PROVER-WISH — from the tlvphoto window, queued here (`docs/wishes/2026-07-09-prover-unwritten-seams.md`).**
   Teach `product-prover` to flag a stateful surface whose behaviour is not stated for every situation it can
   reach — especially "when another surface is present/active" — beyond only the seams an author wrote; plus a
   spec-author counterpart (compose-across-axes gains "every OTHER live surface" as an axis). Motivated by
   tlvphoto's caption-over-finale hole (a seam nobody wrote); bundles the door×viewport-relayout sibling.
   FEATURE, changes product-prover + spec-author. He agreed: do this BEFORE the tlvphoto migration.
3. **Feature/flow spec format (design DECIDED — `docs/spec-format-by-project-type.md`).** Kiro-style ID +
   back-reference; the primary spec UNIT is a per-project-type parameter (feature/command/rule/argument),
   BMAD-style. Single documents, no file sprawl; render generates the hypertext. Coverage check both directions.
4. **tlvphoto MIGRATION — done in tlvphoto's OWN window, NOT here (this window stays audit-only for tlvphoto).**
   Phases: settle the pack (this session) → write the type-aware `adopt/ADOPT.md` procedure → read-only dry run
   over tlvphoto → first real migration in its repo → roll out. Approved forks: reverse-engineer the product
   spec from shipped code (adoption baseline); land the baseline green "as is", file gaps (feature-without-test)
   as queue rows.
5. **Chat cleanliness (decided).** Claude Code cannot gate my outgoing chat (recon: no hook rewrites a reply,
   `Stop` only reads it). PLAN: a `Stop`-hook backstop that lints my reply + forces a visible correction + logs
   it, plus a mandatory self-scan. Migration spreads the RULE everywhere but cannot gate chat by itself.

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
