# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

**LATEST (2026-07-08, session 27) — SPEC readability rework IN PROGRESS; register FOUND, scaling method still OPEN.**
Attempted a full spec humanize. The warm "colleague at a whiteboard" voice read fine on SHORT samples but
DRIFTED on long text. Alexander's diagnosis, the real problem: NOT the register — quality-drift when I rewrite
long, constraint-heavy prose across many sections. On short chat and long ARTICLES my prose is fine; on a spec
it degrades. Root cause I now see: I TRANSFORM old sentences (inherit their contortion, lose the thread)
instead of RE-EXPRESSING each rule fresh.

Kept and worth it (his two clear wins + more, all in the WORKING TREE, uncommitted):
- provenance/history moved OUT of the body into JOURNAL (session-27 entry) — «выпилили рассказики»;
- textual IDs separated (anchors trail as quiet brackets);
- dense law-walls broken into bullets + `###` groups;
- traceability tests RE-POINTED from exact-prose greps to anchors + stable terms (60 asserts / 31 tests) —
  method lesson: a needle keys on the ANCHOR, not the sentence; suite 180 green;
- ARCHITECTURE.md prose lightly humanized (tables untouched); 145 anchors byte-identical to baseline;
  a fidelity prover found + fixed 1 real drift (rhythm date-fence).

REGISTER FOUND + WRITTEN DOWN: `docs/spec-style.md` — Flavor A (declarative / Go-spec), from RFC 2119 +
Diátaxis (reference) + a Fable brief, with warmth-quarantine rules (R7b/c: warmth → a marked informative note,
quotes only when load-bearing + translated, gated by project.kind). His pick.

THE OPEN PROBLEM (unsolved): drift on long text. Current SPEC.md prose is STILL the rejected voice and must be
re-styled to register A. Method to TEST (his «multi-stage / piecewise» + my «re-express, don't transform»):
per section — reduce to a bare rules+anchors list; write each rule FRESH in register A against the
docs/spec-style.md exemplar (never edit the old sentence); re-attach anchors; fidelity-check; tests. TEST on
ONE full dense section in a FRESH context first; scale only if it holds at length. Process lessons: research
the genre FIRST (don't guess-iterate); calibrate on a FULL section, not 2 paragraphs; do prose work in a CLEAN
context.

Baseline / WAY BACK (pushed, clean): pack 0.9.0, main=origin/main HEAD `1cff42b`; INV-70 / INV-28-arm / INV-71
landed (history in JOURNAL). Session-27 SAVEPOINT (local, NOT pushed): commit `1bdf9b1` — anchors separated +
stories cut, VOICE pending (its message says the same). Files: SPEC.md, ARCHITECTURE.md, tests, JOURNAL.md,
docs/spec-style.md.
**SWITCH SIGNAL (how to know to change approach):** if a spec line reads flowery/associative instead of
plain-normative, the voice is wrong → re-style to register A by the re-express method (bare rules list → each
rule written FRESH in register A → re-attach anchors), in a FRESH context. Note the tell: in plain chat the
prose is fine; it is the SPEC that flips me into "associative-poet" mode (Alexander's word). That mode is the
thing to beat — beat it by writing each rule anew, never by editing the ornate original.

**Open — needs a FRESH context or his word:**
- Re-style whole SPEC to register A per `docs/spec-style.md` (the row-148 ask, now with a defined target) — DO IN A FRESH SESSION.
- Bake the humanize/style method into spec-author, referencing stop-slop by NAME (INV-13 across skills), not copying.
- BMAD/Kiro architecture enrichment (what the architecture defines + how to notate).
- Still open from before: remote-seat session (168); no-hooks / no-GitHub (171); thin-loader tidy.

**Terminology (his word 2026-07-08):** to HIM say "live-spec" or "the shared method", never "пакет/the pack"
— he did not parse it. **Push gate:** my-certification (his 19:07 word), generalized by INV-70 — push when
it's sound. Board discipline now law (INV-71): keep NOW/NEXT current in chat + heartbeat on long stretches.

SAFE TO WIPE MEMORY here.

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
