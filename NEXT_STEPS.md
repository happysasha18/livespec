# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

**NIGHT PASS DONE (2026-07-08, autonomous loop, stopped clean).** SPEC lint errors 24 → 4; the 4 remaining
are ALL parked on your word (preamble lines 4/18 = reader-facing second person by design; Formal index scissors
1228/1263 = structured table). Every error a night pass could touch is cleared — one full register conversion
("Asking what the product does") plus fresh-agent surgical fixes across ~9 dense sections; two brittle needles
re-pointed by narrowing (logged in docs/restyle-repoint-log.md). Phase 2 ran: a fresh reviewer read the whole
baseline→now diff, found 7, I fixed the 5 real ones (lost framing, added clause, narrowed word, lost contrast,
dangling em-dash) and re-verified. Full-SPEC anchor multiset IDENTICAL to pre-restyle baseline `ca78876` —
nothing lost. Suite 183 green throughout (only red = TestGateA_ProverRecord, the expected pre-push reminder).
All work LOCAL commits 3665f7b..a9690c4; NOTHING pushed.
WAITS ON YOUR WORD (then prover, then push): (1) full register conversion of the errors-cleared dense sections
— removing their second-person + CAPS collides with ~15 exact-phrase test needles, needs a needle re-point pass
on your say; (2) the preamble + Formal index 4 errors; (3) Phase 3 — ARCHITECTURE.md is already 0 errors (14
warns), its full prose conversion is the same parked class; sealing the method into spec-author + playbook is
premature before you sign off on the SPEC result. Before any push: run the prover pass and commit its record.

**LATEST (2026-07-08, session 28) — SPEC re-style: the drift is SOLVED by a mechanism; grind in progress.**
Root cause of the ornate spec prose, proven with Alexander: the author is marinated in the pack's own
register (doors/kinds/stations/coined metaphor), not the content and not text length. A fresh agent with the
pack NOT loaded writes plain product-spec English from the same facts, consistently, at length. So the fix is
mechanical + a division of labor — and it is SEALED in `docs/spec-style.md`:

THE METHOD (run every section this way; it generalizes to all projects):
- A **fresh spawned agent, pack NOT loaded**, writes the prose from the section's source/facts. Tell it: keep
  every [anchor] verbatim, keep ALL info, keep headings + bold titles, use bullet/numbered lists for any
  sequence, plain present-tense, no second person, no metaphor, do not open by saying what a thing is NOT,
  no ALL-CAPS. Do NOT let the marinated session write the prose — even its chat drifts (his catch this session).
- The marinated session does the mechanical half: gate with `scripts/spec-style-lint.py` to ZERO errors,
  verify the anchor multiset is unchanged (grep `\[...\]` old vs new), splice, run suite, and re-point any
  brittle traceability needle from the old exact phrase to an anchor + a register-invariant term.

CONVERTED so far (register-clean, gated, suite green): "What live-spec is", "Throwing a wish", "Intake",
Naming's first three rules (echo / status board / feature-map placement), "Showing work and asking for
decisions", "Doors, kinds, and craft", "Asking what the product does" (committed 3665f7b, night pass). Gold
exemplars = the decision-page list + intake.

NIGHT-PASS METHOD (kept): hard machine criterion = spec-style-lint 0 ERRORS. Warnings (second-person, CAPS)
are advisory and often collide with exact-phrase test needles, so a section whose needles collide got its
ERRORS cleared surgically and its full register conversion PARKED; a section with no collision got the full
clean-agent conversion.

FULL REGISTER CONVERSION PARKED (errors cleared; removing second-person + CAPS needs a supervised needle
re-point pass on your word): "Specifying and building a feature" (~15 needles incl. facet-sweep headline
"...you know to ask", FACETS tuple, "VISITOR WALK"/"FEEL pass", "AUTHORS the facet sentences"), "Parallel
lanes" ("declined BY NAME"/"RETURNED"/"superseded INTO", PEN prose), "Reuse before reinventing", prototype
promotion, founding-questions, adoption, Human authority, Settings ladder, Delegation and workers, From spec
to tests, push-gate reach, package repo.
STILL-ORNATE, NO NEEDLE COLLISION (full conversion whenever picked up): rest of "Naming" (INV-28/34/35),
"Sending feedback in", "When a bug cuts the line", "One rulebook", "The rhythm", "When money/time run short",
"Publishing", "Composing across axes", "Open decisions".
THEN: same pipeline on ARCHITECTURE.md prose (already 0 errors / 14 warns; tables untouched); then a cross-project migration guide, sealed
into spec-author + the playbook (his word: this is now for ALL projects).

His two goals: (1) human-clear + easy to read + all info present; (2) it also helps the agent build next steps
and communicate better. Do all prose work in a FRESH session (the sealed method) — a loaded session drifts.

TESTS: suite 183 green; the ONLY red is `TestGateA_ProverRecord` — the WIP savepoint changed SPEC.md but
committed no prover record after it. That is a push-gate reminder, NOT a regression. Before any PUSH: run the
prover pass and commit its record (SPEC M-6). New this session: `scripts/spec-style-lint.py` + its tests
(TestSpecStyleLint), rules R13/R14 + the mechanical-gate + clean-agent method in docs/spec-style.md.

Baseline / WAY BACK (pushed, clean): pack 0.9.0, main=origin/main HEAD `1cff42b`. Session-28 work is LOCAL
(uncommitted or WIP savepoint) — SPEC.md, tests/test_traceability.py, tests/test_guardrails.py,
scripts/spec-style-lint.py, docs/spec-style.md. Memory: [[spec-prose-clean-agent-plus-linter]].

SAFE TO WIPE MEMORY here (resume cold from this block + docs/spec-style.md).

## LIVE STATE (2026-07-08, session 26) — humanize + 0.9.0 milestone + three new laws LANDED AND PUSHED.
Versions: pack 0.9.0 (pushed) · base 0.1.24 · communicator 0.1.39 · build-pipeline 0.2.40 · SPEC v0.15.61;
suite 180 green; main = origin/main (HEAD 1cff42b). The writing register (14 rules + 8-item self-check) lives
in communicator; spec-author points to it; deployed==repo. Reporting persona = PROJECT MANAGER, plain product
words (memory [[report-as-project-manager]] + [[plain-language-communication]] + [[parametrize-defaults-and-push-when-ok]]).
Jargon guard is now mechanical (`scripts/preshow-lint.py`, the INV-28 arm). The live board = a chat NOW/NEXT
status + heartbeat (INV-71); the HTML board sketch is dropped by his word. Runs on Opus (Fable pulled 2026-07-07).

## Forward queue (mirrors ROADMAP.md)

1. **DONE and PUSHED:** humanize movement · 0.9.0 milestone · three laws — INV-70 (agent sets tunable
   parameters and tells) · INV-28 pre-show jargon guard · INV-71 (live NOW/NEXT status in any seat, resolves
   the live-board ask row 166). No autonomous rows remain that don't need his word.
2. **Needs HIS word or a real window:** remote-seat session — this evening/tomorrow (also proves INV-67/71 in
   a real cloud seat) · make live-spec work with NO hooks / NO GitHub (row 171, large) · rewrite the spec as
   an even plainer document (row 148, large) · thin-loader tidy in his personal `~/.claude/CLAUDE.md` (move
   the window-list + stale "Fable only" note to his profile — his file, offered).
3. Field legs riding real windows with him: 47/96 feedback loop · 54 first-run · 165 first-struggle · 168
   remote seat (this evening) · 134/141 zero-drift · 143 · 144 · 140 · 117 · 129 · 133.
4. Standing habits: `date` before ANY stamp · keep NOW/NEXT current in chat + a heartbeat past ~10 min
   (INV-71) · plain product words to him, never a code leading a line (INV-28), never "пакет" — say
   "live-spec" · echo speaks door·kind·name·row·map · inbox EMPTY.
