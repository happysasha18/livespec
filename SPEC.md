# live-spec — SPEC (v0.8.1, 2026-07-05)

> How to read: each section is a scenario — what you do and what you see. The short codes in brackets are
> quiet machine anchors (for the prover, the test matrix, and transcript greps); the Formal index at the end
> maps every anchor to its home section. Edit history lives in JOURNAL.md; this spec states today's truth.
> Restructured use-case-first 2026-07-04 (queue row 22) under an anchor-set guard: v0.4 carries exactly the
> anchor set of v0.3 — the shape changed, no rule was lost.

**Current vs target.** Shipped today: the five skills (the base rulebook and the four working ones), the
templates, the adoption procedure text, the inbox, this spec and queue, and the first guardrails slice —
the pack repo's own pre-push gates and the opt-in commit fence, installed and tested. Target (each owned
by a ROADMAP row, not yet code): the guardrails' host-facing checks and surface registry [E-6, E-10], the
snapshot machinery [E-7], the CI mirror [M-5], the model router [ACT-3].
This spec never claims shipped what isn't — sections below marked [target] await their row. [S-0]

## What live-spec is

A package a software project attaches to — at the start or in the middle — to work by one discipline:
wishes are thrown in passing, each one enters a proven process, machines hold the bounds, the human is
interrupted only for decisions that are genuinely theirs. The package is a **base skill** — the pack's
shared rulebook and default settings [E-12] — plus four working skills (spec-author, product-prover,
build-pipeline, communicator), document templates, an adoption procedure, and a set of mechanical
guardrails a project instantiates.

The project it attaches to is the **host**. The host owns its own spec, matrix, queue, journal, surface
registry, and a `.live-spec/` folder (profile, checkpoints, installed-skill versions). [E-1]

## Throwing a wish

You say, mid-anything: "and let the card also show…" — and go back to your thought. A **wish** is exactly
that: one request in plain words, any size, spoken at any moment. [E-2]

That same minute the wish becomes a row in the **queue (ROADMAP.md)** — the persistent, ordered home of
every wish: your words · class (size, plus priority when it isn't normal) · status · acceptance criterion,
one row each. [E-3] Spoken means the row
exists before anything else happens; it survives even if the session dies a second later, and rows are
never deleted — only closed with a named exit. No wish is ever lost. [INV-1]

From the row the wish walks one path: classified by size and priority (the two paragraphs below) → a
spec-delta is drafted → validated against the WHOLE spec — here only genuinely-human questions go out to you, batched;
everything else proceeds on the recommended option, marked in the row → queued → in-work → landed (green
suite + guardrails + committed + the row closed with its acceptance met) → reported to you in one
plain-language line: position on the map · what landed · what remains. [T-1..T-7]

**How a wish is classified.** Size is one four-word vocabulary everywhere — **bug / small / surface /
large** — and the queue's class column speaks the same four words, never a second scale. Priority is
**normal** unless the row says otherwise; two marks exist: **critical** — the shipped product is broken for
its user (an unusable surface, data being lost, a safety gate violated) — and **quick win** — low effort,
immediate value, no design decision inside. When the classifier can't call a size or a priority, it asks
you at intake and never guesses; until you answer, the wish carries normal and the open question rides in
the row — the lane keeps moving [INV-4]. [INV-12]

**Priority bends the lane order, visibly.** A critical bug lands before everything — it heads even the
waiting-bug line (next section). A quick win may bubble up: when the lane frees, it may be taken ahead of
larger queued wishes, the jump marked in its row, never silent; after one bubbled landing the queue head
goes next, so a stream of quick wins cannot starve a big wish forever. [T-11]

While it walks, four things are always true:
- Intake is parallel, execution is serial — **one landing at a time**; a new wish waits its turn unless it
  is a bug preempting (next section). [INV-2]
- **A pending question for you never stops the work** — the lane proceeds on the recommended option; the
  question stays open in the row, revisitable any time. [INV-4]
- **No silent micro-decisions** — every choice not in your wish is either asked, or recorded in the spec
  AND surfaced in the same report. Nothing decided-and-buried. [INV-5]
- **Every landing cites its wish row** — the commit message or journal entry names it, so "why does this
  exist" is always answerable. [INV-3]

A wish can also end without landing; its row stays in the table: **declined** (you said no) · **deferred**
(parked with a named revisit trigger) · **superseded** (absorbed by another wish; the row points to the
absorbing one). [T-8]

What the wishes grow is the **spec (SPEC.md)** — the living statement of what the product is, one surface
= one name, everywhere. [E-4]

## When a bug cuts the line

A bug may interrupt the wish in-work. The interrupted wish moves to **parked**: a checkpoint is written
(failing test names if red, hypothesis, touched files — nothing red is ever committed), the bug takes the
lane, and the parked wish resumes as the immediate next landing. Should more bugs arrive while one holds
the lane, **critical** bugs head the waiting line (among themselves by arrival), the rest follow by
arrival; the parked wish resumes only once no bug waits. A bug already in the lane is never itself
interrupted — an arriving bug, critical included, joins the line, so at most one wish is ever parked. [T-9]

## Starting a new project (bootstrap)

Copy the templates (SPEC, ARCHITECTURE, TEST_MATRIX, ROADMAP, JOURNAL, NEXT_STEPS) → version-control gate
→ the first wish enters the queue → the pipeline runs from intake. [B-1] The gate itself is an always-rule: **no
landing into an unversioned host** — version control exists, and a remote either exists or is explicitly
declined (recorded, not merely recommended), before the first landing. [INV-8]

## Attaching to a live project (adoption)

Adoption is a sequence; each phase completes before the next. In practice the version-control gate [A-5]
is performed FIRST — before anything is touched or moved — so the whole run is reversible; the codes below
name meanings, not a frozen order (proven on the first real run, tlvphoto 2026-07-04). [A-0]

1. **Orient — read everything first.** Every existing document is read BEFORE anything is touched: README,
   any roadmap, any spec, any test suite, journals, TODO files, wikis in the repo. Adoption never assumes
   a blank slate. [A-1]
2. **Inventory** — code, user-facing surfaces (seeding the host's surface registry [E-10]), and the
   document set from the orient pass, listed with owners (file:line for surfaces). [A-2] Adoption's
   working artifacts — the orient digest, this inventory, reconcile notes — live in the host's
   `.live-spec/adopt/`, tracked in git as the run's audit trail, never scattered into the host's own
   folders (the pilot polluted the host's `data/`). [A-8]
3. **Re-engineer the existing documents into live-spec shapes** — an existing spec becomes SPEC.md sections
   (original claims kept, marked unverified); the inventory's `file:line` pins seed ARCHITECTURE.md [E-14]
   (the nodes come from the real code structure, so the layer arrives at adoption, not as an afterthought);
   existing tests become matrix rows citing them at their real level, organized under those nodes [E-15];
   an existing roadmap/TODO becomes queue rows. Nothing existing is ignored, and nothing is trusted
   unreconciled. An unverified claim is reconciled (pinned to file:line, or removed) at the FIRST landing
   that touches its surface — and all remaining ones at the first milestone, whichever comes first. [A-3]
4. **Attic, not deletion.** Any file superseded during adoption or rework moves to the **attic (attic/)**
   — the host's archive folder: append-only, one manifest line per file (what it was, why moved, date); on
   a basename collision the source dir prefixes the name [E-9]. Flat-with-manifest vs dated subfolders is
   an open decision [D-1]. [A-4] The rule behind it never bends for anything authored: **no adopt or
   rework run deletes a host file** — superseded files move to attic/ with a manifest line. [INV-7]
   One exception, and only through a gate: adoption may OFFER a cruft sweep — clearly-regenerable junk
   (caches, build leftovers, already gitignored) listed with file counts and sizes, deleted only on the
   human's explicit OK, never silently; authored content never qualifies and always goes through the
   attic. [A-9]
5. **Version-control gate (done FIRST — see the note above).** If the host has no git: init it, write a
   `.gitignore` that excludes heavy generated/media artifacts, make a pristine baseline commit (this
   doubles as the diff baseline), and settle the remote as a NAMED deliverable: by the first landing a
   remote (GitHub) either exists or the human has explicitly declined one, and the outcome is recorded in
   the run's journal entry — a recommendation alone doesn't close the gate (the pilot ended local-only on
   a mere recommendation) [INV-8]. [A-5]
6. **Baseline snapshot [target]** — render/produce the current artifacts as they are and save them; this
   is the diff baseline the snapshot machinery [E-7] will guard. [A-6]
7. **Incremental thereafter** — the host now works by the same wish lifecycle as a bootstrapped project;
   installed skill versions are recorded in `.live-spec/` at attach time. **On any version change (live-spec
   or any installed skill), the agent RE-READS the changed SKILL.md before continuing** — never coasts on
   the stale in-memory version — and writes a one-line journal note naming old → new. The check is not
   event-only: at every safe breakpoint [M-2] the agent re-stats the installed skills and the package on
   disk (version / file mtime) and re-reads what changed — a parallel session may have shipped an update
   mid-flight. [A-7]

## One rulebook behind the skills

Open any skill of the pack and the same working rules greet you: ask, never guess; plain words with the
code trailing quietly; one surface = one name; one canonical home per fact; work a junior can resume from
a checkpoint after a cut-off. Until now each skill carried its own near-copy of those rules — and copies
drift (the pack's own sweep caught the anchor convention told two ways, and the concurrent-edit fence
stated only in the adoption text while every skill that writes shared files needs it).

**So the shared rules live ONCE, in the base skill** — the pack's fifth skill and shared rulebook (folder:
`live-spec-base`; the pack-structure half of the question is still open [D-4]). Every rule that belongs to every skill is stated there normatively, next to the
package's default settings [E-13]; each working skill opens with one line naming the base skill and the
base version it was written against — a pin the landing that bumps the base sweeps in the same session,
never leaves stale — and REFERENCES the shared rules instead of restating them. A working
skill elaborates only its own domain — communicator may teach HOW to speak plainly; THAT we speak plainly
is the base's sentence. A skill used standalone, outside the pack, still stands: the pointer reads as
plain advice and nothing in the skill's own domain depends on the base being installed. [E-12]

While the pack evolves, one thing is always true: **a shared rule has exactly one normative home — the
base skill; a second full statement inside a working skill is drift, a defect to fold, not a
convenience.** Restatements older than the base skill are pruned at milestones through the compaction pass
[M-1], skill by skill, never in one risky rewrite. [INV-13]

## Who decides what

**You (the human)** own taste, design, irreversible calls, publish/push gates, domain wording — and your
own working contract [INV-9]. [ACT-1] That contract is what the settings ladder RESOLVES to (next
paragraph): the lines about you — proactivity mode (ask-at-max | max-proactive), trust level, language,
domain vocabulary — live in your personal profile and follow you everywhere; the **host profile** at
`.live-spec/profile.md` narrows them for one project when you say so [E-8]. Communicator reads the resolved
contract, not any single file, before every human-facing exchange [E-13]. **Mode and trust are written
ONLY on your word — the agent may propose, never set; it never raises its own trust or proactivity
level.** [INV-9]

**Settings climb a ladder of four NESTED scopes — the narrowest word wins.** Every way the pack behaves
for you is a named setting with a home in exactly one scope, and the scope is chosen by what the setting
DESCRIBES: about the pack itself → the **package defaults**, each value stated in the base skill beside
the rule it tunes [E-12]; about YOU, following you across every project (language: docs and commits vs
conversation · proactivity mode · trust · your domain vocabulary) → your **personal profile**, one file
per human at `~/.claude/live-spec/profile.md`; about THIS project → the **host profile** [E-8]; about
RIGHT NOW → the **session scope**: your live word in one conversation. The scopes nest — the package
holds every human, a personal profile holds every project that human touches, a host holds every session
run inside it — and a setting set at a broad scope is INHERITED down through the narrower ones until a
narrower one overrides it on your word (an all-English project overriding your Russian-chat line; a
"today answer me in English" overriding both for one sitting). Resolution therefore reads from the
narrowest scope out: session beats host beats personal beats package default. Profiles are re-read at
the same freshness points as skills [A-7]; a profile line the current pack does not recognize (written
under an older vocabulary) is ignored ALOUD — named once in the session's next report, never a silent
drop and never an error. [E-13]

**No override is ever silent.** An override exists only as a written line in its profile file, and
setting one leaves a dated journal note in the home it governs — the host's journal for a host line, the
package's for a default change. This is the no-silent-micro-decisions rule [INV-5] applied to settings;
live-spec's own push gate [M-6] is the worked example: the package default says a full prover pass before
a MINOR bump, and live-spec's own host contract tightens it to "before every push" — recorded, visible,
never assumed. The session scope is the one that is never a file: a session override lives only in your
spoken word and dies with the conversation — the agent never writes it anywhere on its own; if it should
outlive the session, that is a PROMOTION into the profile it describes (personal or host), made on your
word and journaled like any other override. An announced self-compaction [M-2] carries the live session
lines forward in its summary; a full wipe ends the sitting — session lines die with it by design, and
that loss is your own move, never the agent's. [INV-14]

**Your profile is the ONE home of the personal layer; the global instruction file is a thin loader.**
Everything personal — who you are, how you like to be spoken to, your standing working rules — lives in
the personal profile, never scattered across always-on instruction files. The machine-global instruction
file (on this stack, `~/.claude/CLAUDE.md`) shrinks to a thin loader: the pointer that loads the profile,
plus ONLY the bootstrap lines that must hold before any pack file is read — the which-project
disambiguation rule is the type specimen: the rule that stops a session writing into a foreign repo
cannot itself wait for that repo's files to load. The loader is those bootstrap lines' ONE home; the
profile never restates them [INV-13]. Migrating an existing rule file into this shape is a
fork by scope — each rule moves to the scope it describes: a method rule the pack already states stays
the pack's (a second copy is drift [INV-13]); a personal line → the profile; a project line → that
project's host profile — proven lossless by a rule-by-rule mapping, with the old file kept in the attic
[INV-7] so one move rolls the whole change back. And the fork only WRITES what the running session owns:
pack rules land in the pack, the personal profile lives on the human's machine outside any project repo;
a project line becomes a written migration note that the project's OWN session lands at its next update —
nothing in this migration writes a foreign repo [INV-10]. [E-16]

**The senior agent** owns judgment: spec deltas, matrix levels, findings triage, this document. [ACT-2]

**Workers (tiered) [router: target]** own mechanical execution, with persistent checkpoint files in the
host's `.live-spec/checkpoints/` (gitignored; never /tmp — a reboot must not erase a resume point); the
cheapest sufficient tier does the job (haiku one-shot / sonnet multi-step / senior judgment), budget-aware.
Whether the queue's size class fixes the tier mechanically or the senior may override is an open decision
[D-2]. [ACT-3]

## From the spec to the tests: two layers that must not be skipped

The spec says WHAT the product is; tests prove facts about the shipped artifact. Between them live two
documents that were once implicit — and an implicit layer is a lost layer (Alexander caught the gap
2026-07-05: the pack taught a matrix template but not the layers that produce it).

**The architecture doc (ARCHITECTURE.md)** — how the product is BUILT: a short list of named nodes
(pipeline stages, modules, the owners of surfaces), one responsibility each, one name each — the
one-surface-one-name rule applied to structure. Every spec fact is OWNED by exactly one node; in a live
codebase every node pins to its owning `file:line` — so drafting the architecture IS where spec claims
get reconciled against shipped reality (each pin comes from a command actually run, never from the doc's
own prose). It is written from the proven spec (template: `ARCHITECTURE.template.md`) and — like the spec
— it is PROVEN before anything derives from it: a product-prover pass with the architecture lens (every
spec fact has an owning node · no node stands without spec backing · the seams between nodes are named).
A large or surface-class wish updates the doc before the matrix is touched; a bug or small wish cites the
existing node it lands in — or, when its fact has no owner yet, ASSIGNS it to the fitting existing node
(recorded in the doc; an assignment alone triggers no re-prove) — so no fix is ever the thing the rules
forbid to land. The doc is re-proven when its structure CHANGES, not on every landing. And it is
ITERATIVE, like the spec it serves: it maps the product as it stands plus the landing in flight — a node
exists for what ships today, or for what the spec already promises under an owned queue row (marked
[target] with an empty pin); it is never designed several milestones ahead. A future feature earns its
node when its landing arrives — speculative nodes are unbacked structure, the architecture's version of
a silent micro-decision. [E-14]

**The test spec — the matrix is DERIVED, never just filled.** The matrix [E-5] is not a bucket of rows.
Derivation is a method with a checkable output: rows are organized **architecture node × spec fact**,
every fact gets at least one row, every row pins a test level — and the derivation closes with the
**coverage validation** — the checklist whose normative home is the matrix template, actually walked:
every spec anchor appears in ≥1 row · every artifact-inventory entry owns ≥1 rendered-level row · every
visibility/layout/colour/interaction fact sits at level ≥ browser-computed · every node carries its
negative-side rows [INV-6] · no row cites an anchor or node that no longer exists (stale rows retire,
never vanish). A fact with no row, or a row at a too-weak level, is a derivation defect — caught at
derivation time, not by the user. [E-15]

While both layers live, one thing holds: **no wish lands whose facts lack an owning architecture node and
a matrix row at the right level** — the bridge from spec to tests is walked layer by layer, never jumped.
A project that predates these layers — this pack itself included — brings them up as an OWNED landing:
the invariant binds from the landing that creates its ARCHITECTURE.md and matrix, never retroactively
(the pack's own bring-up is queue row 50). [INV-15]

## The machines that hold the bounds [target]

What keeps "it works" honest, each one a named machine:

- **The matrix (TEST_MATRIX.md)** — at least one row per fact, each row pinned to a test level; organized
  architecture node × spec fact, produced by the derivation method above [E-14, E-15]. [E-5] Every row states the
  positive AND the negative side — what the fact does and what it must never do; the negative side is the
  regression fence. [INV-6]
- **The guardrails** — the mechanical checks wired to the pre-push hook. Live for the pack repo itself:
  a today-dated prover record exists · the suite is green · every anchor owned by exactly one node · no
  unchecked matrix-coverage box, plus the opt-in concurrent-edit fence on commit. Still [target]: the
  host-facing set — completeness (against the surface registry) · tests-present · behaviour-traces-to-spec
  · declared-scope diff vs snapshot. On a host, hooks are OFFERED, never imposed: only where the host uses
  git at all, and installed only after asking the human — with a plain-words explanation of what the hook
  will check and block, because the human may not know what a git hook is (Alexander 2026-07-05). [E-6]
- **The snapshot [target]** — the saved artifact of the last accepted run (HTML, JSON, files, numbers —
  any product), the baseline the next run is diffed against. The baseline advances only at *landed*, and
  only for the surfaces the change DECLARED; undeclared surfaces keep the old baseline — that asymmetry is
  what catches the unasked change. Retention (last-only vs last-N) is an open decision [D-3]. [E-7]
- **The surface registry** — one named list per host of every user-facing surface. The completeness check
  scans the real rendered artifact against it; a surface that renders but isn't registered is RED, so the
  registry is self-closing, never a trusted hand-list. [E-10]

## The package repo: who may write, and two sessions at once

live-spec eats its own cooking — this spec, this queue, these rules govern live-spec's own development,
and the pack repo's own push gates run mechanically on the installed hooks (a fresh prover record, a
green suite, anchor ownership, matrix coverage — `guardrails/`); the host-facing checks stay [target]
with E-6. [M-4] That makes its repo a shared surface, and one evening
of two parallel sessions taught us the rules:

**Only a session you assigned to live-spec itself writes this repo** (spec, queue, journal, skills,
templates, adopt procedure). Every other session — a host adopt run, a skill install, anything that merely
reads the package — is read-only here, with exactly one exception: creating a new wish file in the inbox.
The test is crisp: if the session cannot say "the human asked ME, in this conversation — or via a standing
routine the human created FOR live-spec — to change live-spec", it does not write. A host run's story lives
in the HOST's journal, never here. [INV-10]

**The inbox (inbox/)** is the parallel-safe intake door for wishes born outside a live-spec session: one
NEW file per wish (`YYYY-MM-DD-<source>-<slug>.md`; name taken → append `-2`, `-3`, …), a few plain lines,
never an edit to an existing file — creating a fresh file cannot collide, shared files can. The outsider
COMMITS its one new file (a commit touching inbox/ only, message naming the source) — that commit is
inside the read-only exception. [E-11] A live-spec session sweeps the inbox as its FIRST act and harvests
each file into a queue row — a wish must not wait durably-recorded but operationally invisible; the
harvest commit removes the file (git history keeps it — this internal removal is not an attic case, which
protects HOST files). So "spoken means it exists" holds without the outside session touching the queue. [T-10]

**Before writing to a repo — and again before every commit** — the agent re-checks `git status` + HEAD
against what it last read. If HEAD moved or the tree holds changes it did not make: STOP, re-read the
changed files, and only then proceed surgically — or back off to the inbox. New files under inbox/ are the
expected benign case, not a fence trip. Never push while another session is known to be live in the repo —
push coordination belongs to the human. Applies to live-spec AND to any host repo two sessions might share
(the concurrency axis of the composition rule, made mechanical). [INV-11]

## The rhythm: breakpoints, milestones, pushes

- **Safe breakpoint (end of every movement):** NEXT_STEPS live-state replaced (never stacked) + dated
  JOURNAL entry + committed ⇒ the session memory can be wiped with zero loss. A long session SHOULD take
  that offer: at a breakpoint the agent compacts its own context to keep working — and SAYS so, never
  silently; a full wipe/clear of the conversation is the human's move, not the agent's. On the way back
  in, re-check skill freshness [A-7]. [M-2]
- **Milestone (MINOR gate):** full spec re-prove + matrix audit (the coverage validation [E-15] re-walked
  against the CURRENT spec + architecture) + surface-composition check + doc
  COMPACTION (pruning: redundancy removed from spec/matrix/queue/skills — nothing grows unboundedly) + a
  re-listing of every open human gate AND every unharvested inbox/ file, one line each, so a waiting wish
  is never forgotten + the formal index re-checked against the prose (the index is a derived map and must
  never drift into a second truth). [M-1]
- **Documents are versioned** like code: the queue and this spec carry dated versions, so "decided under
  which roadmap" is answerable. [M-3]
- **Versions have named homes.** The package: a `VERSION` file at the repo root. Each skill: a `version:`
  line in its SKILL.md frontmatter. A host: the installed set recorded in `.live-spec/` at attach and on
  every update. So the freshness check [A-7] compares version against version, not just file times, and
  its "old → new" journal note is finally writable. [M-7]
- **CI mirror [target]** — the guardrails' native home is the local pre-push hook; a host may additionally
  mirror the same checks in its CI (Jenkins, GitHub Actions) as a second net. Same checks, one source of
  truth — CI runs them, never redefines them. (ROADMAP row 14.) [M-5]
- **Push gate for live-spec itself** — this repo is public and is the method's own flagship, so EVERY push
  is preceded, in the same session, by (a) the concurrent-edit fence [INV-11] and (b) a fresh whole-spec
  re-check: a product-prover pass over SPEC.md as it stands, its record landing in docs/prover/ before the
  push (record name `YYYY-MM-DD[-suffix].md`; suffix mandatory when the date's file exists). Findings that
  are must-fix fold before pushing; folds produced by the gate's own pass do NOT re-trigger the gate — they
  ship with the same record; the rest become queue rows. No re-check record for the pushed state ⇒ the
  push should not have happened. [M-6]

## Composing across axes

Every stateful surface of a host is composed across the canonical axes (view · mode · tier · viewport ·
persistence/reopen · concurrency where real) — and adoption adds one axis of its own: **document
provenance** (native-live-spec × re-engineered-from-existing), because a re-engineered claim behaves
differently (unverified until reconciled per the adoption rules [A-3]) from a native one. [C-1]

## Open decisions

- ⟨DECIDE⟩ attic/ layout: flat with a manifest and source-dir prefix on collision (current pick) vs dated
  subfolders — revisit at the next real adopt run. [D-1]
- ⟨DECIDE⟩ whether the queue's size classification also fixes the model tier mechanically, or the senior
  may override per wish (current pick: router proposes, senior may override, override is logged). [D-2]
- ⟨DECIDE⟩ snapshot retention: last-only (current pick) vs last-N — revisit when a diff dispute needs
  history. [D-3]
- Decided 2026-07-05 (page 2): pack ↔ standalone-skill-repos structure is **package-is-source** — the
  pack repo is the single truth, standalone repos become read-only mirrors (Alexander's note: reusable
  parts must stay findable alone — exactly what mirrors give). The folder-NAME half had closed earlier
  the same day (`live-spec-base`). Execution: queue row 51 (mirrors + one sync command). [D-4]
- Decided 2026-07-05 (page 2): the personal-settings split is **all-into-profile** — everything personal
  moves into live-spec settings with servlet-style scopes (nested, inherited), CLAUDE.md shrinks to a
  thin loader, and setup gains an "understand who you're working with" onboarding step. The scope model
  and the thin-loader shape are spec'd (the ladder and profile paragraphs above, 2026-07-05, rows 52–53);
  the onboarding step remains row 54's landing. [D-5]

## Formal index

Machine handles → home section. For the prover, the matrix, and transcript greps; the prose above is the
meaning, this table is only the map.

| Anchor | One line | Section |
|---|---|---|
| S-0 | shipped vs target marked honestly | header |
| E-1 | host project + its `.live-spec/` | What live-spec is |
| E-2 | wish: plain words, any moment | Throwing a wish |
| E-3 | queue ROADMAP.md, one row per wish | Throwing a wish |
| E-4 | spec: living truth, one surface = one name | Throwing a wish |
| E-5 | matrix: fact × test level | Machines |
| E-6 | guardrails on the pre-push hook [target] | Machines |
| E-7 | snapshot baseline, declared-scope diff [target] | Machines |
| E-8 | host profile at `.live-spec/profile.md` | Who decides what |
| E-9 | attic: archive, never delete | Adoption step 4 |
| E-10 | surface registry, self-closing | Machines |
| E-11 | inbox: one new committed file per outside wish | Package repo |
| E-12 | base skill: shared rules + defaults, stated once | One rulebook |
| E-13 | settings ladder: four nested scopes, session > host > personal > package default | Who decides what |
| E-14 | architecture doc: named nodes own spec facts, pinned to file:line, proven | From spec to tests |
| E-15 | test spec: matrix derived node × fact, coverage validated per level | From spec to tests |
| E-16 | personal layer lives in the profile; global instruction file = thin loader | Who decides what |
| T-1..T-7 | arrived → … → landed → reported | Throwing a wish |
| T-8 | exits: declined / deferred / superseded | Throwing a wish |
| T-9 | bug preempts, wish parks with checkpoint | Bug cuts the line |
| T-10 | outside wish arrives via inbox, swept first | Package repo |
| T-11 | priority bends the lane order, visibly; one bubble then the queue head | Throwing a wish |
| INV-1 | no wish is ever lost | Throwing a wish |
| INV-2 | one landing at a time | Throwing a wish |
| INV-3 | every landing cites its row | Throwing a wish |
| INV-4 | a pending question never blocks the lane | Throwing a wish |
| INV-5 | no silent micro-decisions | Throwing a wish |
| INV-6 | matrix rows state DO and NEVER sides | Machines |
| INV-7 | authored host files: attic, never deletion | Adoption step 4 |
| INV-8 | no landing into an unversioned host | Bootstrap |
| INV-9 | trust set only by the human | Who decides what |
| INV-10 | write-ownership of the package repo | Package repo |
| INV-11 | concurrent-edit fence before write/commit | Package repo |
| INV-12 | ambiguous size/priority is asked at intake, never guessed | Throwing a wish |
| INV-13 | one normative home per shared rule: the base skill | One rulebook |
| INV-14 | no silent override; every profile line recorded + journaled | Who decides what |
| INV-15 | no landing without an owning node + a right-level matrix row | From spec to tests |
| B-1 | bootstrap: templates → gate → first wish | Bootstrap |
| A-0 | codes name meanings, VCS-gate runs first | Adoption |
| A-1 | orient: read everything first | Adoption step 1 |
| A-2 | inventory code + surfaces + docs | Adoption step 2 |
| A-3 | re-engineer docs, unverified until reconciled | Adoption step 3 |
| A-4 | superseded files move to attic | Adoption step 4 |
| A-5 | version-control gate | Adoption step 5 |
| A-6 | baseline snapshot [target] | Adoption step 6 |
| A-7 | re-read changed skills; re-stat at breakpoints | Adoption step 7 |
| A-8 | adopt artifacts live in `.live-spec/adopt/`, tracked | Adoption step 2 |
| A-9 | cruft sweep: gated, listed, regenerable-only | Adoption step 4 |
| ACT-1 | the human: taste, gates, wording | Who decides what |
| ACT-2 | senior agent: judgment | Who decides what |
| ACT-3 | tiered workers, checkpoints [router target] | Who decides what |
| M-1 | milestone: re-prove + audit + compaction + gate list | Rhythm |
| M-2 | safe breakpoint; announced self-compaction | Rhythm |
| M-3 | documents versioned like code | Rhythm |
| M-4 | live-spec is its own host | Package repo |
| M-5 | CI mirror of the same checks [target] | Rhythm |
| M-6 | push gate: prover re-check before every push | Rhythm |
| M-7 | version homes: VERSION file · SKILL.md frontmatter · host record | Rhythm |
| C-1 | canonical axes + provenance axis | Composing across axes |
| D-1 | attic layout | Open decisions |
| D-2 | tier routing override | Open decisions |
| D-3 | snapshot retention | Open decisions |
| D-4 | pack structure: package-is-source decided; mirrors = row 51 | Open decisions |
| D-5 | all-into-profile decided; rows 52–54 execute | Open decisions |
