# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

**SESSION 27 DONE (2026-07-09) — project-wide SCISSORS SWEEP + a document-structure norm. COMMITTED LOCAL, NOTHING PUSHED.**

He flagged the contrast frame (naming a thing by denying its neighbour) as a bad bug that must appear NOWHERE,
chat replies included. Root cause: the scissors linter caught only the dash form, so the comma appositive and
the Russian forms slipped past — that is why the night's "clean" SPEC still held ~39.

FIXED (all committed local, `git log` this session; origin still at `1cff42b`):
- `scripts/spec-style-lint.py` now catches all four shapes (a denied neighbour after a dash or a comma, and the
  parallel Russian negation-then-replacement forms), guarded against the additive "not only/just/merely" and the
  conditional Russian «а» connectives. Regression tests in `tests/test_prose_gate.py::TestScissorsCoverage`.
- Swept EVERY living reader-facing file to ZERO scissors: SPEC, ARCHITECTURE, README, OVERVIEW, ROADMAP,
  TEST_MATRIX, all 8 skills, templates, adopt, guardrails, docs/spec-style.md, prose-quality-gate-design,
  prior-art. ~250 rewrites over 20+ files by 11 parallel workers, each self-verified by the linter; anchors
  preserved; meaning preserved. His verbatim quote in ROADMAP row 140 was restored after a detector false
  positive on conditional «а если бы».
- Traceability check-phrases (what I wrongly called "иголки" — grep slang for the exact quotes the tests
  search for) re-pointed in lockstep; the negative-side "never" restored on TEST_MATRIX M-039/M-044.
  Suite 207 green; only red = the pre-push prover-record reminder (`TestGateA_ProverRecord`).
- communicator register: rule 15 = scissors ban hardened, chat-scoped, described without writing the frame;
  rule 16 NEW = a document is a tree of grouped topics; checklist grew to 10 (scissors scan + structure check).
  deployed==repo re-synced.
- DATED HISTORY left untouched (JOURNAL, docs/prover, docs/audit, docs/evals, docs/decisions, research) —
  rewriting logged history is itself a defect; sweep it only on his word.
His verdict this session: the spec language is finally right («спеки хорошие по языку наконец то»), and this
runs on every project from now on.

## THE NEXT PASS he wants (after this memory wipe): STRUCTURE. The docs are FLAT.
22 communicator rules sit in one list; ~20 SPEC `##` sections sit in one ribbon. He wants real hierarchy —
related rules and sections grouped under named parents, a tree two to three levels deep, the outline alone
telling a reader the shape. Rule 16 states the norm; APPLYING it is this next pass: restructure the flat SPEC
and the skill rule-lists into grouped trees. Grouping is a taxonomy call — propose a concrete grouping and SHOW
it before mass-restructuring. This ties to queued task (b) architecture-tiers and (a) authoring-terminology.

## LIVE STATE (2026-07-09, session 27)
Versions: pack 0.9.0 · base 0.1.24 · communicator 0.1.39 (register now 16 rules + 10-check) · build-pipeline
0.2.40 · SPEC v0.15.61; suite 207 green (1 expected pre-push red). deployed==repo. main HEAD = this session's
LOCAL scissors-sweep commit; origin still `1cff42b` (push owes a prover pass first, SPEC M-6). Reporting persona
= PROJECT MANAGER, plain product words. Runs on Opus (Fable pulled 2026-07-07).
Open before a push: (1) a product-prover pass on the sweep + its record `docs/prover/2026-07-09-*.md`;
(2) the profile count in the PLAYBOOK repo still reads "14 rules + 8-check" — a separate repo, his window / his
call to bump to "16 + 10".
DECIDED 2026-07-09 (his word): also DO the "Not for X…" negation-opener pass — turn every define-by-exclusion
OPENER across the living docs to a positive first move, the same playbook as scissors (the `negation-opener`
linter is the finder). Keep the honest exclusion facts: a "when NOT to use" section still names what to skip
and a genuine prohibition still stands, they only lead positively. Runs alongside the structure pass named above.

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
