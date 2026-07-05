# live-spec Journal

Edit history lives here — the WHY behind every change. The spec and README state current truth; this file explains how we got there.

---

## 2026-07-04 — Package born

**What:** Created the livespec skeleton repo — directory structure, four bundled skills, templates, adopt procedure, guardrails outline, install script.

**Why:** The method (spec → prove → reconcile → matrix → test → code → verify → commit) has been running in production on track-coach for over a year and is proven. It lives scattered: CLAUDE.md rules, four skill repos, a playbook, and a habit. The goal of livespec is to make the whole thing one attachable package — clone it, run `./install.sh`, and the skills land in `~/.claude/skills/` ready for any project. One home, not four.

**Why "livespec":** Alexander's coinage (2026-07-04). Working name; a better name may emerge (queued in ROADMAP).

**Status:** Skeleton only. Skills are read-only copies (source repos unchanged). No SPEC authored yet — that waits for Alexander's signal to publish, so spec-author runs on the full intended scope, not a moving target. Unpublished; local only.

**Decided:** Local-only for now. No GitHub creation, no push. When Alexander says publish, that is ROADMAP item 1 — create the repo, push, wire the skill install to the real source.

## 2026-07-04 — SPEC v0.1: the first self-application run
Alexander caught a real hole in ADOPT (it inventoried code but not existing DOCUMENTS) and added two more
wishes (attic-not-delete; version-control gate). Instead of patching ADOPT.md pointwise, livespec was run
on itself: three wishes → queue rows 8-10 → SPEC.md v0.1 authored covering the whole package (wish
lifecycle, both entry modes, actors, milestones, self-application invariant M-4). ADOPT.md and README will
be updated AFTER the prover pass (row 7) — spec before docs, by the book.

## 2026-07-04 — prover pass (row 7) + the honesty correction
FULL product-prover pass over SPEC v0.1: 11 findings (wish exit states; preemption path; surface-registry
entity; current-vs-target marking; profile owner+trust rule; provenance reconcile transition; baseline
advance timing; INV homes; human-gate re-listing; skill-version drift; checkpoint home). All folded → v0.2.
Alexander then challenged the "pioneers / no prior art" claim as possible people-pleasing. He is partly
right: artifact-baseline diffing is MATURE prior art in testing tooling (Jest snapshots, Percy, Chromatic
visual regression). Our narrower true claim: declared-scope diff as an agent pre-push guardrail + the
continuous-intake combination. README rewritten to credit lineage and link BMAD; long-tail search of the
skill ecosystem launched before publish.

## 2026-07-04 — first REAL adopt run (tlvphoto) + dogfood fix to ADOPT.md (row 4)
The adopt procedure ran end-to-end on a live host for the first time. The run's own story lives where it
belongs — in the HOST's journal (tlvphoto JOURNAL.md, entry "2026-07-04 — livespec adopt"); this entry keeps
only what changed LIVESPEC. (Trimmed 2026-07-04 late: the host story was originally written here too —
that duplication is exactly what the write-ownership rule now forbids.)

**Why this changed livespec itself:** the run proved `adopt/ADOPT.md` was STALE vs SPEC (it still had the old
inventory→reverse-spec→snapshot order, missing orient/attic/VCS-gate). Rewrote ADOPT.md to the SPEC A-0…A-7
sequence. One genuine refinement the run surfaced and I folded: the **version-control gate belongs FIRST**
(before orient touches anything) so the whole run is reversible — annotated SPEC A-0/A-5 (codes name
meanings, not a frozen order). A re-prove of the adopt section is due at the next milestone (minor reorder,
not blocking). Closes ROADMAP row 4; completes the "update ADOPT.md to the proven spec" tail of row 7.
Note: livespec repo was concurrently edited by another session (publish + rows 12-15) — this entry touched
only ADOPT.md, SPEC A-0/A-5, ROADMAP row 4, and this journal.

## 2026-07-04 — parallel-session protection (row 16) + codes-never-speak (row 17)
Two sessions edited this repo the same evening: one publishing (rows 1, 12–15), one running the tlvphoto
adopt (row 4) — the adopt session edited ADOPT.md/SPEC/ROADMAP/JOURNAL directly and avoided a collision only
by NOTICING the foreign commits and being surgical. Alexander: that must be mechanics, not luck — and a host
run's story belongs in the HOST's docs, not here.

Landed (SPEC v0.3): **INV-10 write-ownership** — only a session the human assigned to livespec itself writes
this repo; every other session is read-only except creating one new `inbox/` file. **INV-11 concurrent-edit
fence** — re-check HEAD/`git status` before every write and every commit; foreign changes ⇒ stop, re-read,
proceed surgically or back off; never push while another session is live (push coordination is the human's);
applies to host repos too. **E-11/T-10 inbox/** — one new file per outside wish; file-creation cannot collide,
so no-wish-is-lost holds without outsiders touching shared files. ADOPT.md now states the host-session
read-only rule. The row-4 entry above stays (it documents a real livespec change); under the new rule that
change would have arrived as an inbox wish.

Same evening, second leak of the same class (row 17): a session told Alexander "INV-8 рекомендует
GitHub-бэкап" — a spec handle spoken to the human. communicator rule 6 hardened from a soft "translate
internal ids" to a hard gate: spec handles (INV-x, E-x, A-x, T-x, row numbers, ⟨DECIDE⟩) are machine anchors
that never appear in a sentence addressed to the human; the leak itself is the rule's ❌ example now.

## 2026-07-04 — late refinements: anchors-in-parens, journal cleanup, push gate + its first run
Three refinements from Alexander the same night, all landed before the v0.3 push:
1. **Anchors in parentheses are allowed — with the WHY recorded** (row 17 refined): the plain sentence
   carries the meaning for the human; the trailing code serves the MODEL — transcripts are what it greps
   and self-monitors against, so a stable anchor makes past reasoning findable. Rule 6 rewritten from
   "codes never appear" to "a code never does the talking"; installed copy synced.
2. **Journal cleanup by the new ownership rule:** the row-4 entry held the tlvphoto run's full story — a
   HOST's story in the package's journal, the exact duplication the write-ownership rule forbids. Trimmed
   to the livespec-only part with a pointer to tlvphoto's JOURNAL (verified present there first).
3. **Push gate (M-6, row 18):** Alexander — livespec specifically gets a fresh whole-spec re-check before
   EVERY push. Spec'd and enforced immediately: prover pass docs/prover/2026-07-04-v03-push.md over v0.3
   found 7 findings in the new seams — the gate could regress on itself (fold→re-prove forever), an
   outsider's uncommitted inbox file would trip the very fence built to receive it, an inbox wish could
   wait durably-recorded but invisible, plus name-collision/record-naming/standing-routine edges. Six
   folded into SPEC same session (gate no-regress rule; outsider commits its inbox file + fence treats
   inbox files as benign; sessions sweep inbox first + milestone lists unharvested files; `-2` counter;
   dated record naming; standing routines count as assignment). Seventh recorded onto row 3's scope
   (guardrails scaffold also mechanizes the fence and the push gate). First push of v0.3 follows this entry.

## 2026-07-04 — first real inbox harvest + four wishes from Alexander (rows 19–26)
The inbox worked on its first night: the tlvphoto session dropped one committed wish file (three adopt
gaps, each with a primary source — remote never actually made to happen; adopt artifacts polluting the
host's data/; pre-existing gitignored cruft left on disk) and touched nothing else. Harvested → rows 19–21,
file removed in this commit per the inbox contract.

Alexander's four wishes the same hour:
- **Use-case-first spec (row 22, the big one):** the spec must read as a PRODUCT document — scenarios of
  what the human does and sees lead, codes only trail as anchors; explicitly ONE document, not a human copy
  and a model copy in sync (he named that alternative and prefers one readable doc). Held for his OK on a
  sample section shown in chat; guard for the restructure: the anchor SET before/after must be identical
  (grep-diff) so nothing formal is lost, then full prover + push gate. Propagation to the template and
  spec-author is row 23, strictly after.
- **Skill freshness is not event-only (row 25, landed):** at every safe breakpoint, re-stat installed
  skills + package on disk and re-read what changed — a parallel session may have shipped an update.
- **Base skill, the "Object class" (row 24, queued):** the rules every skill inherits (re-read-on-change,
  write-ownership/fence, anchors, checkpoints) stated once, referenced everywhere — also serves milestone
  compaction.
- **Context hygiene for long work (row 26, landed):** at a safe breakpoint the context may be compacted or
  cleared — the breakpoint's whole point is that disk holds the resume.
Push deferred: bundling with row 22's landing so the push-gate prover run covers both.

## 2026-07-04 — SPEC v0.4: the spec now reads as a product document (row 22)
Alexander OK'd the sample shape the same night ("давай полный прогон, потом пуш"). The whole spec
restructured use-case-first: sections are now scenarios ("Throwing a wish", "When a bug cuts the line",
"The package repo: who may write", "Attaching to a live project") — the prose talks to the human, every
code only trails in parentheses/brackets, and a Formal index closes the doc as the machine map. Explicitly
ONE document, not a human copy and a model copy in sync — the index is declared a derived map, and the
milestone now re-checks it against the prose so it can never become a second truth.

The guard held: anchor set v0.3 → v0.4 byte-identical (49 anchors, grep-extract diff). Push-gate prover
pass (docs/prover/2026-07-04-v04-push.md): 4 findings, all folded — package-governance section moved out
of the product story's path; index-drift check added to the milestone; D-1's expired "first adopt run"
trigger refreshed to "next"; README got the one sentence naming the new shape (full propagation to the
template + spec-author is row 23, its own landing).

Also folded from Alexander the same hour (row 26 refined): at a safe breakpoint the agent compacts its own
context to keep working and SAYS so — never silently; a full wipe/clear of the conversation is the human's
move. And row 27 opened: he floated renaming to "live-spec" (hyphen) — recommendation recorded (keep the
unbroken token), his call, awaiting his word; if renamed, the adopted host projects must be told.

## 2026-07-04 — communicator rule 8: retell, don't reference (row 28)
End of the same night, a live communication failure taught the last rule: the report "the inbox worked —
harvested into rows 19–21" meant nothing to Alexander until retold as a story (the other project's session
found three adoption gaps; before tonight it would have edited the package directly; instead it left one
inbox file and touched nothing else; the findings became queue rows). Same fact, only the second telling
communicated. Landed as communicator rule 8 (seven rules → eight): an event is REPORTED as a story that
stands on its own; internal bookkeeping (row numbers, file names) may only trail as an anchor, never
substitute. The failed/working pair is the skill's live example. Installed copy synced; the general
principle also recorded in the playbook. Old three skill repos: Alexander deleted them tonight — the
package is now the skills' only public home.
Push note: SPEC.md is byte-unchanged since the v0.4 push-gate record (2026-07-04-v04-push.md), so that
record covers this push's spec state per the gate's own terms.

## 2026-07-05 — the use-case-first shape propagated to the template + spec-author (row 23)
Row 22 proved the shape on livespec's own spec (v0.4); today the shape became the DEFAULT every future
spec is born with. `templates/SPEC.template.md` rewritten from a structure-first skeleton (Purpose /
Entities / States / Actors / Invariants / Composition / Glossary chapters) to a use-case-first one:
scenario sections lead ("what the person does" is the section name), entities are defined in bold where
the walk first meets them, invariants read as "always true while this runs" sentences, anchors trail at
line-ends, and a Formal index closes the doc — with all 11 sample anchors in the body covered by the
sample index, so the template models its own rule. `skills/spec-author/SKILL.md` updated to teach it: the
spine reframed from a section ORDER to a completeness CHECKLIST that lives inside the scenarios; two new
"How it reads" rules (scenarios lead · the index is a derived map, never a second truth); the anchor-set
guard for restructures written down as method (diff the sorted anchor list before/after — identical sets
prove no rule was lost); shape questions added to the completeness pass; two new anti-patterns
(structure-first layout, index drift). WHY the glossary changed: the proven v0.4 exemplar defines terms in
place (bold at first use) and has no glossary section, so the checklist now says exactly that, with a
separate glossary only when in-place stops scaling. Sibling skills swept for old-shape assumptions
(product-prover / build-pipeline reference no section order) — clean. Installed spec-author copy synced.

Session note (the morning's near-miss, cross-project): the session began with a wrong-project resume — I
picked up track-coach's NEXT_STEPS instead of livespec's (home-launched sessions share one memory; volume
of old track-coach notes ≠ assignment) and spawned two workers toward track-coach's tests before Alexander
stopped it. Both killed before a single write landed (git status clean, no files created — verified).
Rule saved to memory: cwd=home + no project named ⇒ ask which project, listing the NEXT_STEPS files on
disk; never infer from memory volume. Mechanical fix offered: launch each project session from its own
directory.

## 2026-07-05 — push-gate prover pass (fresh, on Alexander's word) + the push
Alexander cleared the push and asked for a fresh spec check first. Full prover pass over SPEC.md v0.4
(docs/prover/2026-07-05.md): 5 findings, 0 must-fix. One folded with the record per the gate's own-fold
rule — when a second bug arrives while one already holds the lane, the spec now says bugs take the lane
in arrival order and the parked wish waits until no bug does (T-9; before, two rules both claimed the
next slot and the agent would have picked silently). The other four became queue rows 29–32: one size
vocabulary for wishes (spec's four classes vs the queue column's S/M) · closed rows ARCHIVE at milestones
(reconciles "never deleted" with "nothing grows unboundedly") · versions need a disk home before A-7's
old→new note is writable · the global-default profile path is still unnamed. Anchor-set guard: byte-set
identical before/after the fold (checked against HEAD). Pushed: row 23 (use-case-first template +
spec-author) + this gate's record + the fold.

Also today, on Alexander's word, the working setup became a standing global rule (playbook 79d45a1 —
CLAUDE.md lives in the playbook repo via symlink, hence that commit): one window = one project (livespec ·
track-coach · tlvphoto), ask when the project is unsure, never infer from memory; livespec runs on Fable
only, as the package that will rule the other projects.

## 2026-07-05 — the three adoption fixes from the first real adopt run (rows 19–21) + row 33 opened
The tlvphoto pilot's inbox wishes became rules. (1) The remote is now a NAMED deliverable, not a
recommendation: by the first landing it exists or the human explicitly declined it, outcome recorded in
the run's journal — the pilot had ended local-only on a mere "recommended"; the bootstrap sentence carried
the same weakness and was fixed as the same class (A-5, INV-8). (2) Adoption's working artifacts (orient
digest, inventory, reconcile notes) got a home: `.livespec/adopt/`, TRACKED in git as the run's audit
trail — recommended pick recorded in row 20, Alexander may flip to gitignored; the pilot had polluted the
host's data/ (A-8). (3) The optional cruft sweep is spec'd as the ONE gated exception to never-delete:
regenerable junk only, listed with counts and sizes, human's explicit OK, authored content always via the
attic — INV-7 reworded to "never bends for anything authored" so the exception is a gate, not a buried
contradiction (A-9; ADOPT Phase 0.5). Push gate: CROSS-LINK prover pass over the three seams
(docs/prover/2026-07-05-adopt.md) — one drift found and folded (INV-7's index line), 0 must-fix.
Anchors: deliberate add of exactly A-8/A-9, indexed. Row 33 opened: Alexander asks whether the playbook
repo + CLAUDE.md symlink are still needed — recommendation recorded (keep as the thin private layer;
audit/shrink after rows 12 and 24), his call.

## 2026-07-05 — the classifier learns priority, the queue speaks one language (rows 29+34), the roadmap gets a face (row 35); rows 34–36 opened
Alexander asked for two things in passing and both landed as one classification scheme. First, priority
(row 34): a wish is now classed by size AND priority — critical (the shipped product is broken for its
user) lands before everything, a quick win may bubble up between landings with the jump marked in its row,
and an ambiguous call is ASKED at intake, never guessed — until answered the wish carries normal and the
lane keeps moving (INV-12, T-11, T-9 graded). The starvation edge is fenced: after one bubbled landing the
queue head goes next. Second, the size vocabulary unified (row 29, queued since the morning prover pass):
the queue's S/M column swept to the spec's four words — bug / small / surface / large — as a Class column
that also carries the priority mark. SPEC v0.4 → v0.5; anchors: deliberate add of exactly T-11 + INV-12.
Push-gate CROSS-LINK pass (docs/prover/2026-07-05-classes.md): 3 findings, all folded before push — order
among two waiting critical bugs (by arrival) · a bug in the lane is never itself interrupted, so at most
one wish is ever parked · the real catch: ROADMAP.template.md still TAUGHT the old S/M/L scale, so every
future host would have contradicted the one-vocabulary rule on day one — template rewritten (the
never-patch-pointwise rule earning its keep). Row 35 landed the same hour: when reporting where-we-are,
the roadmap renders as a bulleted icon list (✅🔨⬜🙋), current item marked, finished stretches collapsed —
communicator rule 9, installed copy synced. This landing itself ran as a quick win bubbling ahead of
row 24 — on Alexander's explicit word, and marked in the rows. Mid-landing Alexander threw row 36
(package defaults a host overrides — e.g. full prover pass per push for livespec vs big-versions-only for
track-coach; refined minutes later: some settings are personal and global, like docs-English /
chat-Russian): recorded as a three-layer design (package defaults → global personal profile → per-host
override), to be designed with row 24's base skill.

## 2026-07-05 — roadmap list lines gain substance (row 37)
Alexander's read on row 35's first use: the icon list reads fine, but the lines are bare titles — he
wants each a bit more informative. Refined communicator rule 9: every line now carries one clause of
substance matched to its status — a landed item says what it changed, an in-work item what is happening
now, a queued item what it will give, a waiting item exactly what is asked. The WHY is quoted in the rule
so the refinement survives a memory wipe. Installed copy synced; landed as a quick win inside the same
report exchange (row 37). Push gate: SPEC unchanged since the same-day green pass, verified by blob hash
(docs/prover/2026-07-05-rule9-detail.md).

## 2026-07-05 — the base skill + the settings ladder (rows 24+36, with debts 31+32; SPEC v0.6)
The pack grew its fifth skill and its spine. Until today every working skill carried its own near-copy of
the shared working rules, and copies drift — the evidence sweep that opened this landing (a junior read of
all four SKILL.md files + templates + ADOPT.md, raw greps kept in the session scratchpad, spot-checked by
re-running one) caught the anchor convention told two ways and the concurrent-edit fence stated only in
the adoption text while every writing skill needs it. So the shared rules now live ONCE, in
`skills/livespec-base/` — twelve of them, the list derived from what the sweep actually found repeated,
not from memory — and each working skill opens with a one-line inherit note instead of restating them;
pruning the old restatements is deliberately deferred to milestone compaction, skill by skill, never one
risky rewrite (SPEC E-12, INV-13).

Settings became a three-step ladder (SPEC E-13, INV-14): package defaults (a table in the base skill) →
personal profile at `~/.claude/livespec/profile.md` (about the human, follows him everywhere — his
language split, max-proactive mode, written from his recorded standing words) → host profile in
`.livespec/` (about the project). Host beats personal beats default; an override exists only as a written,
dated line; an unknown line is ignored aloud, never silently. livespec's own push gate turned out to BE
the worked example — the every-push prover re-check is now also recorded as this repo's host-profile
override of the "before MINOR bumps" default, one fact with M-6 as its normative home.

Two queued debts landed on the way, as their rows had planned: versions got homes (root VERSION 0.1.0 +
`version:` frontmatter in all five skills — row 31, SPEC M-7) and the global profile path got its name
(row 32, open pick D-5). The prover's cross-link pass (docs/prover/2026-07-05-base-skill.md) folded three
must-fixes before push — the sharpest: the inherit notes pin the base version as four literal copies, so
the spec now obliges the landing that bumps the base to sweep the pins the same session — and opened row
38 (the personal profile has no git home yet). Open picks for Alexander, lane not blocked: base folder
name (D-4, `livespec-base` current) and personal-profile home (D-5).

## 2026-07-05 — decision page prototype + the first mined gap folded (rows 39, 12; skills → 0.1.1)
Alexander proposed a better way to be asked: instead of reading an MD questionnaire, an interactive local
HTML page in the browser — radio options, a note field per question, a Download JSON button — the way he
already tunes images in tlvphoto; the agent then reads the downloaded JSON. Taken as row 39 (quick win,
jumped the queue inside the same exchange) and used immediately for real: the five standing open picks
(base folder name, personal-profile home, livespec vs live-spec, playbook fate, adopt artifacts in git)
became the first page, headless-render gate before showing (6 cards + live counter). The page is a session
artifact; the durable record is the downloaded JSON folded back into this queue. Folding the mechanism
into communicator is queued as its own landing.

Row 12 folding began with gaps 1+2 taken as one class — primary-source discipline. The rule existed only
in the private playbook; now it is base rule 13 (a claim about what code does / what happened / who
decided rests on a citation — file:line, commit, a command just run; memory, a worker's summary, a doc's
prose are leads, not evidence), with its two working faces referenced where they bite: build-pipeline's
reconcile step (the reconcile note cites primary sources, never the doc's own prose) and a product-prover
meta-rule (claims about the shipped system key on the reconciliation note's citations — prose that outran
the code would otherwise "prove" dead behaviour). Base bump 0.1.0 → 0.1.1 swept the four inherit-note pins
the same session, as the spec obliges (E-12); all five skills and the package VERSION now read 0.1.1. The
mining map itself moved from /tmp to the private playbook repo (it quotes the private rules — not public
material), commit 05b13af there; row 12 pointer updated. No test suite exists in this repo yet to extend
(guardrails are row 3) — the folded rule's verification stays the prover's push-gate pass for now.

Also answered aloud: other project windows already receive pack updates by themselves — install.sh copies
the skills to the global ~/.claude/skills, every session loads from there, and base rule 8 (freshness)
makes long-running sessions re-stat and re-read on change; the livespec session's only duty is to sync
installed copies after each landing. What is NOT automatic yet is formal adoption (the .livespec/ attach)
— track-coach is queued as the first formal adopt-host.

## 2026-07-05, 11:50–12:20 — The lost layers return; the package becomes live-spec

The morning decision page came back as JSON (answered 08:49; archived in docs/decisions/) — the first
full round-trip of the mechanism, five picks harvested the same session. Three of them landed today's
movements; two grew into new design work.

**The lost layers (row 41, Alexander: "очень важный момент").** When the method was distilled from
track-coach practice into the pack, the layers between the proven spec and the tests silently dropped
out — a matrix TEMPLATE shipped, but not the method that produces a matrix, and no architecture document
at all. Both are now first-class pipeline steps no wish may jump: an ARCHITECTURE.md written from the
proven spec (named nodes, one responsibility each, every spec fact owned by exactly one node, named
seams; in live code every node pinned to its owning file:line — which is where the old standalone
"reconcile" step now lives), proven by product-prover with an architecture lens whenever it changes; then
the matrix DERIVED node × fact, closing with a coverage-validation checklist that is actually walked
(SPEC v0.7: E-14, E-15, INV-15; new ARCHITECTURE template; build-pipeline 0.2.0; prover + spec-author
0.1.2 for the lens and the pointer). Decided by delegation ("или как сам решишь"): the architecture
prover pass fires when the doc CHANGES, not on every landing — a bug cites its node and moves.

**Decision page becomes law; time enters the records (rows 39/45/46).** Communicator rule 10 now states
the mechanism: several open picks → one interactive page, radio + recommendation + free-form per card,
JSON filename carrying the PROJECT name (several projects share one Downloads folder — Alexander caught
it this morning), answers archived and harvested same session. Base rule 9 now requires date AND time on
journal entries and harvested records — "вчера вечером ты написал X" must be answerable from the record
(communicator 0.1.2, base 0.1.2, four inherit pins swept).

**The rename (rows 27/40).** Alexander picked live-spec over the keep-recommendation. One name
everywhere, so the sweep took the machine tokens too: 97 occurrences across 14 files (a sonnet junior ran
it; senior re-ran the verification grep), the base skill folder is live-spec-base (closing the name half
of D-4), the host folder .live-spec/, the profile home ~/.claude/live-spec/. Dated history — this
journal's older entries, prover records, decision JSONs — intentionally keeps the old spelling; MIGRATION.md
tells each adopted host what its own session runs at the next update. GitHub repo + local clone dir
rename wait for the reviewed push, so the outward move is one atomic step.

**New in the queue from midday messages:** feedback-collection as a pack skill (row 47), a maintenance
skill with measurement plugins — analytics per user story/axis (row 48), A/B experiments for software
hosts (row 49), learning from other frameworks as its own version bump (row 44). Rows 42 (pack
structure) and 43 (personal-settings split) went out as today's second decision page, worked examples
included, gate-checked before showing.

**Status:** three commits today before this entry; VERSION goes 0.1.1 → 0.2.0 with the whole-spec prover
pass that closes the session (MINOR gate: this pack has no matrix yet — guardrails are row 3 — so the
audit is the prover pass + the queue re-listing, said honestly). Push held for Alexander's review.

## 2026-07-05, 12:40–13:10 — Gate green, 0.2.0, and the afternoon answers

The session's prover gate ran as a FULL pass over SPEC v0.7 (record: docs/prover/2026-07-05-lost-layers.md)
and did its job: 10 findings, the sharpest being that the new layer invariant was unsatisfiable for every
EXISTING host — live-spec's own repo first — because nothing owned creating the two new documents, and
adoption still produced the old flat matrix. All ten folded the same session (bring-up rule + queue row 50;
adoption Phase 5 rewritten "architecture, then the matrix"; a bug may now ASSIGN an orphan fact to a node
so no critical fix is ever the thing the rules forbid; the template owns the coverage checklist; stale step
numbers and one-vs-at-least-one wording swept). VERSION 0.1.1 → 0.2.0 — the MINOR gate's matrix-audit leg
is honestly N/A until row 50 exists; said, not skipped.

The afternoon decision page came back at 12:48 (archived docs/decisions/2026-07-05-decisions-2.json):
**package-is-source** — the pack repo is the single truth, standalone repos become per-skill mirrors
(Alexander's note about reusable parts staying findable alone is exactly what mirrors give; row 51), and
**all-into-profile** — against the recommendation: everything personal moves into live-spec settings with
servlet-style scopes (nested, inherited), CLAUDE.md shrinks to a thin loader, and setup gains an
"understand who you're working with" onboarding step (rows 52–54). The mid-session interruption cost
nothing: three commits were already on disk, the uncommitted folds survived in the tree, and the resume
file told the truth — the discipline paid for itself the first time it was tested.

## 2026-07-05, ~13:30 — Push released (session 4)

Alexander's steady-state call came in plain words: nothing left to review at a green gate — push. Fence
re-check passed (clean tree, no inbox deposits, remote unmoved), and the five held commits went out
(b6e2827..70b71f9): the lost layers, the decision-page law, the rename-in-content, the 0.2.0 gate. The
one piece the harness would not let this session do is the OUTWARD half of row 40 — renaming the GitHub
repo itself (an external write the permission layer reserves for a human). So the rename is now split
honestly: content says live-spec everywhere (pushed), the repo/clone-dir rename waits on one command from
Alexander (`gh repo rename live-spec --repo happysasha18/livespec --yes`), after which the local dir move
and remote URL update are mechanical. Recorded here so the split is a fact with a reason, not a drift.

## 2026-07-05, ~14:00 — Row 50 lands: the flagship gets its own architecture and derived matrix

The bring-up the lost-layers session promised: live-spec now walks its own new pipeline. ARCHITECTURE.md
v0.1 names 12 nodes (five skills, templates, attach = ADOPT+installer, inbox, host-contract, the pack's
own docs, and the two honest [target] machines — guardrails and snapshot); all 69 spec anchors are owned
exactly once, every pin taken from a command run this session, none from memory. The architecture-lens
prover pass (docs/prover/2026-07-05-architecture.md) earned its keep on the first walk: the sharpest
find was S-0's broken promise — the spec swears every [target] machine has a queue row, and two didn't
(snapshot, model router → rows 55–56); it also caught the spec still claiming two decision pages were
"out" that Alexander had already answered (D-4/D-5 rewritten to their decided state, SPEC v0.7.1), and
a queue header with no date where M-3 requires one. Eight findings total: three must-fix folded in
session, two queued as row 57 (installer and decision page deserve spec sentences), three recorded.

TEST_MATRIX.md v0.1 derives 64 rows node × fact, every row with a DO and a NEVER side, and the honest
adaptation for a text product recorded in its header: the "rendered level" here is a string assertion
against the SHIPPED file — no browser surface exists, so the browser-level clause holds vacuously and
re-arms the day one ships. The coverage validation is not a checklist walked once: it is mechanized in
tests/test_traceability.py — 20 tests, zero deps, green with zero skips — and the walk went red on real
defects before it went green (unowned A-6/E-7, a range token double-counted), which is exactly the
red-first the method asks for. INV-15 binds from this landing. VERSION 0.2.1. Push held for Alexander's
look; the prover record doubles as the push-gate re-check for this state.

## 2026-07-05, ~14:10 — Iterativity enters the method (row 58), everything pushes

A piggyback wish with a perfect origin story: tlvphoto's agent asked Alexander "should I write the
architecture several milestones ahead?" — and the method had no sentence to answer with. Now it does,
in every home the question could be asked from: SPEC E-14 (v0.7.2) — the architecture doc is iterative,
maps the product as it stands plus the landing in flight; a node exists for what ships or what an owned
queue row already promises ([target], pin empty); a future feature earns its node when its landing
arrives, and a speculative node is unbacked structure, the structural twin of a silent micro-decision.
Same sentence in ARCHITECTURE.template.md and build-pipeline step 3 (skill 0.2.1, installed copy synced
so every host on this machine reads it at the next freshness check). Cross-link prover check green
(docs/prover/2026-07-05-iterativity.md) — the [target] node rule and INV-15's assign-on-landing already
compose with it cleanly. Row 58 landed the hour it was spoken. VERSION 0.2.2. Push follows on
Alexander's word given in the same message.

## 2026-07-05, ~15:45 — Rows 53 + 3 land, row 51 lands reduced, row 52 designed (session 4, afternoon)

**What:** Four movements in one afternoon stretch, on Alexander's "поехали" (~15:05) — he also set the
version plan: the next MINOR bump goes straight to **0.5.0** (his word, marking the volume since 0.2),
with the 3-pass preventive audit before it as always.

- **Row 53 (scope model):** SPEC v0.8.0 — the settings ladder generalized to four NESTED scopes with
  inheritance, resolution narrowest-out: session > host > personal > package default. The session scope
  is named for the first time: the human's live word, never a file; the agent never writes it; making it
  outlive the session is a PROMOTION into a profile, journaled. Base skill ladder rewritten (0.1.3, four
  inherit pins swept, installed copies synced). Prover pass docs/prover/2026-07-05-scopes.md: 3 findings
  (1 must-fix — the migration fork must never write a foreign repo), all folded same pass. New anchor
  E-16 owned by host-contract; matrix M-002 updated, M-065 added (70/70 anchors).
- **Row 52 (personal-layer migration) — designed, flip gated:** migration map + thin-loader draft +
  profile-v2 draft written to ~/.claude/playbook/row52/ (private repo — doubles as the git home row 38
  asked for, via a proposed symlink). Flip blocked on: folding row 12 gap 3 (fix-the-class — the one
  CLAUDE.md rule with no pack home yet) and Alexander's review of both drafts. Rollback = one copy back.
- **Row 3 (guardrails, pack slice) — landed by a Sonnet worker:** guardrails/ with pre-push gates
  (prover record · green suite · anchor ownership · matrix coverage) + opt-in commit fence + install.sh;
  hooks installed, each gate proven by deed incl. a failure case; 15 new tests. The worker caught its own
  test-recursion bug (pre-push invoked inside the suite re-discovering the suite) and fixed it with
  scratch-copy fixtures. Spec/architecture/matrix reconciled to the shipped slice (M-4 now mechanical
  for the pack; E-6 host-facing set stays [target]).
- **Row 51 (mirrors, reduced) — landed by a Sonnet worker:** scripts/sync-mirrors.sh + product-prover
  mirror synced to 0.2.2 (idempotency proven). Discovery: spec-author had NO standalone repo — the
  standing note was wrong. Creating four mirrors awaits Alexander's word (new public repos are his gate;
  the permission classifier enforced the same line when the first worker brief included repo creation).

**Why this order:** Alexander asked to distribute and economize — judgment (scope design, spec, prover)
stayed on Fable; both bounded rows ran on Sonnet in parallel with checkpoints. Old-name leftover
("livespec") found and fixed in the personal profile — a file outside the repo the row 40 sweep missed.

## 2026-07-05, 15:05 — Gap 3 folded (fix the class, sweep look-alikes) + three decisions from Alexander

**What:** The "never patch pointwise" rule got its pack home: base rule 14 (a found defect is a sample of
its class — sweep the repo and every user-facing surface before calling the fix done), the bug entry path
in build-pipeline now says the matrix row and red-on-bug test cover the CLASS not the instance, and
product-prover Phase 3e gained an eighth stress family, "Sibling instances" (sweep the document, write one
class finding listing every instance). The rule-list in all four working skills' headers + their base pin
(v0.1.4) swept in the same change — itself an application of the new rule. Versions: base 0.1.4,
build-pipeline 0.2.2, prover 0.1.3, spec-author 0.1.3, communicator 0.1.3.

**Also landed, same sitting:** (1) SPEC v0.8.1 — hooks are OFFERED, never imposed: on a host, git hooks
only where git exists and only after asking the human with a plain-words explanation (Alexander's word,
~15:00; rides E-6, row 57 keeps the installer/decision-page half). (2) README status line — the drifting
pinned "v0.1.0" replaced by the rule (release number lives in VERSION only) plus a plain explanation of the
two counters: VERSION counts package releases, the SPEC header counts spec revisions, and the spec's
counter runs ahead by design. Class-swept: no other drifting version pin in prose (the base-pin lines in
skill headers are deliberate written-against pins).

**Decisions by Alexander (this session, ~15:00):** NO new mirror repos — live-spec stays the one pack
repo, product-prover the sole standalone mirror, name unchanged (row 51 closed for good); one push after
today's tidy-up, not now; night audit run by Opus with a Fable spot-check of one pass (the model-comparison
sample), skill-creator eval (row 5) rides the same night.

**Why:** Gap 3 was the one CLAUDE.md rule with no pack home — the named blocker on row 52's flip
(CLAUDE.md → thin loader + profile). With it folded, the flip waits only on the drafts review.

## 2026-07-05, ~15:40 — The 0.5.0 preventive audit: run, compared across models, folded (session 5)

**What:** The full MINOR gate, run in daylight instead of overnight on Alexander's "поехали". Three audit
passes plus the skill-creator eval ran as parallel Opus workers; pass 1 (whole-spec prover) ran TWICE —
Opus and Fable independently, same brief, no cross-reads — as the model-comparison sample Alexander asked
for. Two workers hit the plan's session limit at the finish line but had already written their reports to
disk (checkpoint discipline paying for itself — zero loss, no resume needed). All records in
`docs/audit/2026-07-05/` (five reports + `model-comparison.md`).

**Results:** matrix pass — suite 35 green at audit time, 70/70 anchors each owned exactly once, zero
must-fix; composition pass — 20 surfaces, clean naming, zero must-fix; prover passes — Opus 4 must-fix /
8 should / 2 worth, Fable 1 / 5 / 3, agreeing on the headline defect: INV-2's serial-lane rule never said
how it scales to two sessions or delegated workers, while the flagship's own journal records blessed
parallel workers. Skill eval: all five skills sound, repo/installed copies byte-identical; one cross-skill
defect (top-level `version:` where the canonical validator wants `metadata.version`).

**Folded the same sitting (SPEC v0.8.1 → v0.9.0, anchor set unchanged):** the lane got its token (the
single in-work row; workers may overlap only on disjoint files under the fence, landings close serially);
a parked wish resumes ahead of any quick-win bubble; inbox harvest is one atomic commit per file,
idempotent on re-sweep; closed queue rows ARCHIVE at milestones, never delete (folds row 30 — the INV-1
vs compaction contradiction Opus caught); push-gate folds are enumerated in the record and stay local;
profile files got explicit tracked-ness (host profile tracked, created at attach; personal profile may
live in a PRIVATE human-owned git home — the wording fix that unblocked the row-52 flip); the inbox is
now host-general (every host gets the parallel-safe door); unrecognized profile lines leave a durable
journal note, not just a report line; [target] adoption phases are recorded-and-skipped; arrival ties
resolve by row order; M-1 gains the derived-header re-pin rule; version homes moved to `metadata.version`
across all ten SKILL.md copies (matrix M-001/M-002/M-012 reconciled, M-066 added, new
`test_settings_ladder_documented`). Architecture pins re-verified — one (`:83` ladder) was stale BEFORE
this session; all four corrected. Non-folded findings became queue rows 59–69.

**Model comparison verdict (the budget question):** Opus was fully sufficient for scaffolded document
review — denser findings, sound severity, best single fix proposal (the lane token). Fable's edge showed
in cross-document timeliness (catching that E-16's old wording would contradict the imminent row-52
landing) and severity restraint. Split confirmed: audits on Opus, fold triage and spec wording on Fable.

**Verified:** suite 36 green, zero skips — worker's run AND the senior's own re-run (the session's
delegate spot-check). VERSION 0.2.4 → 0.5.0 on Alexander's standing word (the straight-to-0.5.0 plan,
~15:00). Push still held for his review, per the same word.

**Also:** Alexander OK'd the row-52 five-line summary (~15:34) — the loader flip executes immediately
after this commit; its own journal entry follows.

## 2026-07-05, ~15:50 — Row 52 flip staged to one human command; row 38 closed (session 5)

**What:** Alexander OK'd the five-line summary (~15:34). Executed the reviewed checklist: pre-migration
`~/.claude/CLAUDE.md` AND the old personal profile attic'd (`playbook/row52/attic/*.2026-07-05`); profile
v2 written to its git home `playbook/personal/profile.md` (private repo, pushed — 5aa79a8) with
`~/.claude/live-spec/profile.md` now a symlink to it, which lands row 38's backup/history debt with the
same move; the final loader text staged at `row52/CLAUDE.final.md`.

**The one step that did NOT execute by agent hand — by design:** the permission classifier refused the
agent's rewrite of `~/.claude/CLAUDE.md` (self-modification of the global instruction file on a
narrated OK). That refusal is the method's own INV-9/ACT-1 line drawn by an outside machine: the swap of
the human's standing instruction file is the human's move. Alexander runs one command
(`cp ~/.claude/playbook/row52/CLAUDE.final.md ~/.claude/CLAUDE.md`); rollback is the same command from
attic. Row 52 marked "flip staged"; it closes on his copy.

**Why journal this:** the audit had just folded the worker-contract seam as a queue row (who may write
what a session's own machinery may not) — and an hour later a live permission gate enforced exactly that
seam against the senior itself. Primary evidence for row 59's design.

## 2026-07-05 (session 6, evening) — the 0.5.0 push lands; the Room incident files rows 70–71

Row 52 closed at Alexander's own hand (~16:12, the one `cp`; diff-verified identical) — the thin-loader
migration is live. The push gate then ran as designed: FULL prover pass on an Opus worker (per the
morning's model-split decision), senior triage. It found two real must-fix holes the morning's audit
folds had left — the lane token was a bare read, not a committed claim (two parallel sessions could
double-land, INV-2), and the milestone archive could swallow a deferred wish whose revisit trigger
hadn't fired (INV-1 violated by its own clause). Both folded as narrow wording fixes + three smaller
folds (inbox arrival = harvest moment; unreachable harvest-recovery parenthetical rewritten; the
architecture's stale loader pin flipped to landed). SPEC v0.9.0 → v0.9.1, anchor set unchanged, suite 36
green twice (before and after folds). Record: docs/prover/2026-07-05-v05-push.md.

**The Room incident (why rows 70–71 exist and cut the line).** Alexander, hot and right: tlvphoto's
similarity room was hand-built over the infrastructure past the pipeline — its own spec named Room a
"later surface, not yet specified", and no pack law made that line binding, no law defined "prototype",
no machine check compared the prod build against the spec. The agreement was "load casually, the system
lines it up" — the recognition half was never made a mandatory step. Rows 70 (feature-recognition
tripwire: classification said aloud before any code; hard triggers replace judgment) and 71 (prototype
quarantine + prod-traceability guardrail) land next, one pipeline landing; wish relayed to tlvphoto's
inbox (created with the file — the host had none). Fitting coda: while filing those very rows the
traceability suite went red on the senior's own class-cell vocabulary — the gate caught the gatekeeper,
live evidence that tripwires beat judgment.

## 2026-07-05 (session 6, ~17:40) — rows 70–71 land: the door law + the prototype law (the Room incident folded into the method)

Why this exists: Alexander, this afternoon, hot and right — tlvphoto's similarity room was hand-built
past the pipeline and shown as product while its own spec said "later surface, not yet specified". The
agreement was "load casually, the system lines it up"; the recognition half was guidance, not law. Two
laws land, one pipeline landing (door: feature, size: surface):

**The door (SPEC T-12, INV-16).** Classification is an explicit step said BEFORE any code: every wish
names size · priority · door (feature · bug · refactor · docs-only · skip) in one intake line. Hard
tripwires replace judgment — new visible surface / new state / new interaction / a [target]-marked
surface / unbacked behaviour ⇒ feature, however casual the ask. The verdict outranks a casual "bugfix"
label; queue-cutting stays with the bug door; the door re-fires mid-work the moment work is about to
create something its door doesn't grant.

**The prototype (SPEC E-17, INV-17, A-10).** Exploring is legal but fenced: prototype/ home, label per
artifact kind, senior-only creation, shown only as a sketch; promotion re-enters at the spec step.
Machine tooth shipped: guardrails gate (e) `check-prototype-fence.sh` — a prod file referencing into a
prototype home blocks the push (red-first proven). Adoption now gives every unbacked live surface a
human verdict: promote / quarantine / attic.

Pipeline walked in full: spec delta → CROSS-LINK prove (Opus worker; 4 must-fix + 6 clarify, ALL folded
— record docs/prover/2026-07-05-doors.md) → architecture assignments (T-12/INV-16 → build-pipeline,
E-17 → base-rulebook, INV-17 → guardrails, A-10 → attach; no node/seam change, no re-prove per the
doc's own rule) → matrix M-067..M-071 → tests (traceability class TestDoorLawAndPrototype + guardrails
TestGateE, red-first) → code (base rules 15–16 v0.1.5; build-pipeline step zero v0.2.3; prover ninth
lens v0.1.4; communicator PROTOTYPE-label line v0.1.4; spec-author [target]-tag rule v0.1.4; installed
copies synced) → sweep (README step 0, ROADMAP header + template, PLAYBOOK principle line — pushed).
Suite 36→43 green. Worker split held: Opus proved, Sonnet built the fence + its tests (checkpoint
`.live-spec/checkpoints/2026-07-05-prototype-fence.md`), Fable folded and worded. Alexander's second
wish of the evening (feature intake must sweep the standard facets a layman can't name — responsive,
touch, states) filed as row 72, enters next; row 44 (learn-from-others) will feed it.

## 2026-07-05 (evening, session 7) — row 72: the facet sweep — SPEC v0.11.0, pack 0.5.2

WHY: the Room incident's third lesson (after the door and the prototype laws). Alexander can't be
expected to ask "and what happens on a phone?" — the dimensions a layman can't name (narrow layout,
touch-vs-hover, empty/error/loading, accessibility, performance) simply never got a sentence, and the
Room shipped hover-only with no phone layout. The fix: when a wish's door says feature, drafting the
spec-delta walks the canonical facet list (its one home: spec-author). Every facet ends as a SPEC
SENTENCE — decided, or the recommended default taken with the literal `[default]` tag and reported back
as a plain-words tradeoff, batched. Silence stopped being a legal outcome.

Pipeline walked in full: spec delta → CROSS-LINK prove (Opus worker; 1 must-fix + 4 clarify + 2
worth-considering, ALL SEVEN folded — record docs/prover/2026-07-05-facets.md; the must-fix was real:
a defaulted facet had no durable home, hence the `[default]` tag) → architecture assignment
(T-13/INV-18 → spec-author, pin :144; no node/seam change, no re-prove) → matrix M-072..M-073 → tests
(TestFacetSweep, red-first proven) → code (spec-author facet-sweep section + completeness bullet
v0.1.5; communicator rule-10 tradeoff line v0.1.5; build-pipeline step-1 sweep sentence v0.2.4;
installed copies synced) → suite 45 green, 0 skips. Per the prover's process finding (F4) the MINOR
spec bump owes a FULL pass at the push gate — run before this push per M-6.

Same evening, before the landing: Alexander banned calques outright (Russian chat had been carrying
loan-translated pack terms — «растяжки», «та же семья»). Contract line `language.no-calques` live in
his profile (playbook 234bce6); pack-general rule filed as row 73 (communicator + base), lands next.

Push gate (M-6): FULL pass on an Opus worker (docs/prover/2026-07-05-v11-push.md) — ready-to-push, zero
must-fix, 77 anchors symmetric, all seven facet folds verified in prose. Its one should-clarify (a
headless feature — new persistent state, no visible surface — would owe layout sentences) folded same
sitting: the sweep scopes to VISIBLE surfaces, a headless feature writes one explicit "no visible
surface — facets N/A" line -> SPEC v0.11.1. Suite 45 green; pushed.

## 2026-07-05 (evening, session 7, second landing) — row 73: no calques — base 0.1.6, pack 0.5.3

WHY: twice in one day a Russian-chat report carried English pack terms as literal translations
(«растяжки» for tripwires, «та же семья»); Alexander: "НЕЛЬЗЯ использовать кальки… это позорит наш
продукт". The personal contract line (`language.no-calques`, his profile) had already landed; this
landing bakes the language-pair-general rule into the pack itself. One home per rule held: the ban
lives in base rule 2 (the plain-words rule — a calque is its cross-language case), communicator rule 6
elaborates with the field example. Spec step concluded NO spec delta: the rule elaborates an existing
base rule; SPEC's one-rulebook clause (INV-13) already owns the home. Test test_no_calques_rule; base
0.1.6 (pins swept across the four working skills by a Sonnet worker, checkpoint
2026-07-05-row73-mechanical.md — the delegation rule held this time), communicator 0.1.6, spec-author
0.1.6, build-pipeline 0.2.5, product-prover 0.1.5; installed copies synced; suite 46 green. Same
sitting: row 74 filed (a plain-language map of the whole structure — Alexander can't hold where things
live; he is right, and the two research agents on row 44 homework are running in the background).

## 2026-07-05 (night, session 7) — rows 77+85: non-goals, appetite, success measure — SPEC v0.13.0

WHY: Alexander's decision-page answers (harvested this evening). He took the intake trio NOW with the
KPI note ("зашивать сразу в фичу как мера успеха, все сразу дата дривен") and declined the waived-risk
verdict ("не понимаю о чем ты"). Landed: appetite as an optional rider on size (scope-only, trims
proceed on the recommended option and are surfaced — the prover's must-fix killed the lane-blocking
"come back to choose" wording); the two always-written closing sentences of every feature delta —
non-goals ("nothing left out" is valid prose, a narrowing one is surfaced) and one success measure
(`[default]` = provenance only, the KPI/A-B reading machinery honestly [target] under future rows).
Prover CROSS-LINK: 1 must-fix + 8 others, ALL folded (2026-07-05-intake-trio.md). Suite 50 green.
Same night: the promoter mis-founding (personal-vs-reusable never asked) → his profile line
product.default-reusable (playbook, pushed), inbox wish to the promoter, row 88 queued for tonight.

## 2026-07-05 (night, session 7) — rows 83+88: founding questions + design-sync [target] — SPEC v0.14.0

WHY: two lessons of the same evening. The promoter window founded a project as "a personal agent for
three artifacts" without asking the one question that shapes everything — personal or reusable; Alexander:
everything he builds is for reuse (profile line landed, playbook). And his 1.0 directive asked design-sync
to be thought through — the proposal (docs/research/2026-07-05-design-sync-proposal.md) made it an
OPTIONAL [target] machine: declared-scope footprint, supplements (never replaces) the real render,
human-gated because a sync publishes. Prover CROSS-LINK: 0 must-fix, 7 clarifications ALL folded
(founding answers = a deliberate strengthening that blocks the first wish; A-1 carries the pointer;
E-13/INV-14 seams stated). New [target] architecture node design-sync — the structure change re-proves at
tonight's milestone audit. Suite 51 green. Inbox harvested: promoter plugin-directory prep (89),
track-coach pin freshness (90), registry-as-gate (91), visual-hierarchy facet (92), design-sync wiring (93).

## 2026-07-05 (night, session 7) — MILESTONE 0.8.0: the research-integration night

WHY 0.8.0 and not 1.0: Alexander's own word ("может это 0.8 или 0.9, не надо спешить") — 1.0 waits for
the work-kind axis (row 86), design-sync wiring (93), skill-behavior evals (94), and the tlvphoto
lessons run through a real feature. What the night landed, every row through the full pipeline with an
independent prover pass and all findings folded same sitting: facet list 5→8 under a curation law
(rows 78+92) · regression fences (75) · non-goals + appetite + success measure (77+85, his KPI note) ·
founding questions + design-sync [target] machine (83+88) · self-contained worker briefs (79) ·
skill hygiene: when-NOT-to-use ×5 + loadability gate f (80) · excuses table (81) · prover anti-taste
line + base irreversibility rule 17 with HIS criterion — money/deletion yes, push no (82) ·
decision-file numbering (87) · plugin-directory prep + mirror fix (89) · symbol-first pins + drift
gate g — which immediately caught 3 stale labels in our own architecture (90) · executable registry
preferred (91). Alexander's page answers harvested: waived-risk DECLINED in his words; appetite+KPI
taken NOW. The promoter mis-founding became B-2 + his profile line product.default-reusable. tlvphoto
failure analysis (Sonnet, transcripts): the pack simply wasn't attached for the first 30 hours, then
fired unevenly — report in docs/research/, feeds the serious talk. Milestone: 64→65 terminal rows to
the dated queue archive; versions swept (base 0.1.7 · spec-author 0.1.7 · communicator 0.1.7 ·
build-pipeline 0.2.6 · product-prover 0.1.6 · pack 0.8.0); 3-pass audit (records in
docs/audit/2026-07-05-night/ + docs/prover/2026-07-05-v14-push.md): ONE must-fix across all three
passes (a matrix row under the wrong node — moved, and the class mechanized as a standing test), the
rest folded. Suite 46→61 green. Workers: two Opus provers ×5 passes, three Sonnet mechanical briefs
(the self-contained-brief rule dogfooded on its own landing night). Pushed on the clean verdict.

## 2026-07-05 evening (~20:50, session 8) — row 86: the pack now names WHAT it builds

Alexander opened the evening with "поехали по полной" — the queue's 1.0-shortlist head, row 86, went
through the full pipeline in one sitting. First, housekeeping: session 7 had mis-dated its late entries
"2026-07-06" while the git clock says everything landed 2026-07-05 19:23–20:14 — swept the class
(ROADMAP rows 95–97, NEXT_STEPS, the personal profile line, session memory), and row 74 closed on his
word: he read the rendered OVERVIEW and asked one follow-up (why the playbook loads per-session — 
answered in chat: always-on loader stays thin, rules arrive at the moment of use, durability lives in
files + guardrails, and row 94's evals are the honest answer to "what if a skill never fires").

The landing itself, SPEC v0.14.0 → v0.15.0, pack 0.8.0 → 0.8.1: the intake line's third axis, the
WORK-KIND — product · infra · skill · prose — his decision-page note made law ("скилл сет должен
понимать с чем работает… задействовать необходимые функционалы, не все всегда нужны"). T-16: kind named
at intake, one kind per wish, curated vocabulary, host-profile default only for a one-kind host (the
draft's own "live-spec = skill-and-prose default" broke that law and died in the CROSS-LINK pass — F1,
must-fix, folded). INV-22: the door picks WHICH steps run, the kind picks the FORM each running step
takes; at landing every door-granted step has APPLIED or STOOD DOWN by name in the report; an unresolved
kind scales nothing down; the safety net (door law, mandatory sentences, ask-at-intake) is kind-proof —
the same shape as appetite's law, deliberately. The per-kind step table's one normative home:
build-pipeline SKILL.md (new section, pinned in the architecture). Base rule 15 carries the axis
(0.1.8); communicator's landing report names stood-down steps (0.1.8); the base-pin test went dynamic —
it now reads the base version from the base's own frontmatter, so a base bump without the same-session
pin sweep is red by construction. Matrix rows M-084/M-085; suite 62 → 64 green, red-first shown on the
skills before the code step. Prover record: docs/prover/2026-07-05-row86.md (CROSS-LINK, 3 findings, all
folded same pass). This landing's own report dogfoods INV-22: kind = skill; prove-architecture stood
down (assignment only, E-14's rule); design-sync/snapshot stood down (text product, [target] anyway).

## 2026-07-05 late evening (~22:00, session 8) — row 94: the skills got their own failing tests

The evals machine (SPEC E-19, pack 0.8.1 → 0.8.2): each working skill now owns a recorded scenario
where a session without it errs and the skill corrects — superpowers' "no skill without a failing
test", made ours. Eight real runs tonight (four bare + four with-skill Sonnet workers), records in
docs/evals/2026-07-05-first-run/, eval files in evals/, self-closing suite check (a fifth working skill
goes red until its eval exists). The reds that survived scoring: spec-author's bare run decided ~10
product questions SILENTLY (zero tags, zero questions — the Room's hole, reproduced in vitro);
product-prover's bare run wrote an essay with no severities and missed the end-of-track dead-end the
skilled run caught; build-pipeline's bare run planned to PARK on the design question (INV-4 inverted)
and never named door/kind; communicator's bare run shipped no map and let version numbers do the
talking. The finding of the night (folded into evals/README): on this machine there is NO bare session
— the thin loader feeds the method to every agent (the "bare" bug plan cited "per this project's own
discipline"!), so a red here is bare-of-the-SKILL, honest boundary stated, per-criterion scoring with
MET BARE never claimed as the skill's win. Second lesson folded: a scenario that enumerates facet hints
does the skill's job (the first spec-author prompt did — recorded as contamination, de-contamination
scheduled for the next re-run). M-1 now carries the evals re-run; architecture gained the skill-evals
node (re-proven, record docs/prover/2026-07-05-row94.md); suite 64 → 66 green. This landing's own
INV-22 line: kind = infra; facets N/A (no visible surface, said aloud); design-sync/snapshot stand
down; prove-architecture APPLIED (node add).

## 2026-07-05 late evening (~22:20, session 8) — row 93, the pack-side half: design-sync is wired

The switch and the channels exist; the machine still owes its first real run. E-18 re-worded to the
honest split "[target: the machine; the wiring is live]": the `design-sync` setting sits off-by-default
in the base defaults table (0.1.9, pins swept — the dynamic pin test earned its keep the same evening it
was written), communicator rule 5 says where the cards go (the design project, only AFTER the human's
gate, the in-session render staying the authority), pipeline step 9 says when a sync fires. New matrix
row M-088 + `test_designsync_wiring`; suite 67 green; pack 0.8.3. The row stays OPEN — its named
remainder is the first real sync on a visual host through Alexander's gate; that needs a visual window
(track-coach or tlvphoto), not this one. Landing report line per INV-22: kind = skill; facet sweep — no
visible surface, N/A aloud; prove-architecture — pin/name updates only on an existing node, no
structure change, stands down by E-14's own rule; the sync machine itself — still [target], nothing
claims it ran.

## 2026-07-05 night (~22:50, session 8) — row 98: the publish skill, and the eval that cut both ways

Alexander, mid-evening: "короткий паблиш скилл — ридми грамотный; если скилл — команды показать;
сравнительный анализ, скриншоты или диаграммы — всё по типу того что заливается… плагин гитхаба должен
встраивать свои этапы". Landed as the pack's FIFTH working skill (E-20, pack 0.8.3 → 0.8.4): the
publication surface owes its reader what the artifact's KIND owes — the work-kind axis read at the
door instead of the intake — with a shared floor (what/who/how-to-start in the reader's language,
claims true today, license explicit, nothing secret or unshareable leaves), a per-kind table (its one
home: the skill), and the target-plugin seam: GitHub, plugin directory, design project each embed
their steps, never removing the kind's minimum; the checklist always finishes BEFORE the human's gate
and never sends anything itself. Count sweep ran everywhere ("four working skills" → five; base header
→ six skills; count-free wording where a count would rot). Base 0.1.10, pins swept third time tonight
— the dynamic pin test made each sweep a non-event. Two machines proved themselves on this landing:
the EVAL LAW caught the new skill mechanically (suite red until evals/publish.md existed — E-19's
self-closing promise, verified by deed), and the publish eval's first run cut BOTH ways — the bare arm
knew five public-repo hygiene steps the skill's draft lacked (secrets/history sweep, fixture copyright,
dependency licenses, fresh-clone check, name collision), all folded into the skill the same evening.
Records: docs/prover/2026-07-05-row98.md, docs/evals/2026-07-05-first-run/{bare,with-skill}-publish.md.
Suite 67 → 68 green. INV-22 line: kind = skill; facets N/A aloud; design-sync/snapshot stand down;
prove-architecture APPLIED (node add). First real use of the skill = this repo's own next public push.

## 2026-07-05 night (~23:25, session 8) — row 99: scope is the only negotiation; time budgets die

Alexander, on reading the evening's report: "сделай по-быстрому это неправильно… какой дебил спрашивает
программера 'сколько это займет?' надеясь на вменяемо квантизованный ответ? это всегда ложь. можно
играться со скоупом а не с таймлайнами." Stronger than the de-ceremonialization I'd recommended — not
the word, the MECHANISM: T-15 re-authored to scope-never-time (a too-big wish is CUT — fewer surfaces,
plainer defaults — or STAGED, each stage a full-pipeline landing; an hours-or-days answer is never an
input the walk accepts). What survived intact, deliberately: proceed-on-recommended + batched surfacing
(INV-4/5/18), only-priority-moves-the-lane (T-11), and the uncuttable safety net (fences, facets,
non-goals, success measure). The imported term swept from SPEC, build-pipeline (0.2.9), spec-author
(0.1.9), README, matrix M-076 — and the suite now asserts it ABSENT so muscle memory can't sneak it
back; history (journal, archives, prover records) keeps the old word, as history must. Pack 0.8.5,
suite 68 green. The research-adopt lesson closes its loop: we imported Shape Up's appetite with a named
incident behind half of it — the human kept the half with the incident (speed never cuts the safety
net, reborn as scope-cut law) and killed the half that was ceremony. Curation working as designed.

## 2026-07-05 night (~23:45, session 8) — row 61: the push gate stops trusting the calendar

Gate a checked "a prover record dated today, committed" — so a morning record blessed an evening SPEC
change it never reviewed. Now it checks the STATE: the newest docs/prover/ commit must not be older
than the last commit touching SPEC.md (record shipping in the same commit as its folds passes — M-6's
own fold clause). Door: bug (shipped gate weaker than M-6's promise); kind: infra; the mechanical half
ran as a Sonnet worker on a self-contained brief with a checkpoint (.live-spec/checkpoints/row61.md),
red→green shown raw, senior re-ran the gate and the suite by deed. Suite 68 → 70 green; M-015
re-authored; pack 0.8.6. The delegation debt (the standing "I keep not delegating" failure) got its
counter-example tonight: brief written in 5 minutes, worker landed it while the senior answered the
human's scope-never-time word.

## 2026-07-05 late (~22:20, session 9) — row 57: the spec stops pretending two mechanisms don't exist

The architecture audit (F2+F3) had named the hole: install.sh and the decision page both SHIP but had no
spec sentence — an unnamed mechanism is invisible to the prover, so its promises can silently rot. Door:
bug (prover-found spec hole); kind: prose. SPEC v0.15.1 adds two clauses in their scenarios' own homes:
"How the skills arrive on a machine" (adoption, E-21 — idempotent, timestamped backup, never deletes;
installing and A-7's version record are two halves of one seam) and "How batched questions reach you"
(the wish walk, E-22 — ONE decision page, answers archived + harvested same session; mechanics stay in
communicator rule 10, one home). Ownership: E-21 → attach (it already pinned install.sh), E-22 →
communicator — assignments only, no re-prove. Matrix M-091/M-092; and M-091's REAL-run test (a fresh
temp home, run twice) immediately caught a REAL bug: install.sh had no mkdir -p, so a genuinely fresh
machine — the exact machine the installer exists for — failed on first run. Red shown, one-line fix,
backup-and-never-delete sides asserted by the same run. Suite 70 → 73 green; pack 0.8.7.

## 2026-07-05 late (~22:40, session 9) — row 60: one collision law instead of two half-laws

The audit had it right (fable F3, opus F-7, comp N6): the attic said "source dir prefixes the name" with
no answer for a SECOND collision; the inbox said "-2, -3" with no semantic mark; nobody owned the rule.
Now base rule 18 states it once — semantic mark first (each home already has one), then numeric ordinal,
a session token where true concurrency can race one name (the inbox); never overwrite, never a third
scheme, never a lost file. The four surfaces that spoke halves (SPEC attic clause, SPEC inbox clause,
ADOPT, communicator rule 10's ordinal) now CITE the law — the prover's cross-link pass caught rule 10 as
the unswept fourth (F2, folded). Base 0.1.11, pin sweep across the five working skills (versions
untouched per the aff99f9 precedent), matrix M-093, suite 74 green; pack 0.8.8. Also from this session's
gate run: row 61's freshness lock proved itself live — the row-57 commit turned the repo red until this
record existed. The teeth bite in the right place.
