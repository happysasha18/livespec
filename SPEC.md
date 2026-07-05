# livespec — SPEC (v0.4, 2026-07-04)

> How to read: each section is a scenario — what you do and what you see. The short codes in brackets are
> quiet machine anchors (for the prover, the test matrix, and transcript greps); the Formal index at the end
> maps every anchor to its home section. Edit history lives in JOURNAL.md; this spec states today's truth.
> Restructured use-case-first 2026-07-04 (queue row 22) under an anchor-set guard: v0.4 carries exactly the
> anchor set of v0.3 — the shape changed, no rule was lost.

**Current vs target.** Shipped today: the four skills, the templates, the adoption procedure text, the
inbox, this spec and queue. Target (each owned by a ROADMAP row, not yet code): the guardrails scaffold
[E-6], the snapshot machinery [E-7], the model router [ACT-3], and therefore full self-enforcement [M-4].
This spec never claims shipped what isn't — sections below marked [target] await their row. [S-0]

## What livespec is

A package a software project attaches to — at the start or in the middle — to work by one discipline:
wishes are thrown in passing, each one enters a proven process, machines hold the bounds, the human is
interrupted only for decisions that are genuinely theirs. The package is four skills (spec-author,
product-prover, build-pipeline, communicator), document templates, an adoption procedure, and a set of
mechanical guardrails a project instantiates.

The project it attaches to is the **host**. The host owns its own spec, matrix, queue, journal, surface
registry, and a `.livespec/` folder (profile, checkpoints, installed-skill versions). [E-1]

## Throwing a wish

You say, mid-anything: "and let the card also show…" — and go back to your thought. A **wish** is exactly
that: one request in plain words, any size, spoken at any moment. [E-2]

That same minute the wish becomes a row in the **queue (ROADMAP.md)** — the persistent, ordered home of
every wish: your words · size · status · acceptance criterion, one row each. [E-3] Spoken means the row
exists before anything else happens; it survives even if the session dies a second later, and rows are
never deleted — only closed with a named exit. No wish is ever lost. [INV-1]

From the row the wish walks one path: classified by size (bug / small / surface / large) → a spec-delta is
drafted → validated against the WHOLE spec — here only genuinely-human questions go out to you, batched;
everything else proceeds on the recommended option, marked in the row → queued → in-work → landed (green
suite + guardrails + committed + the row closed with its acceptance met) → reported to you in one
plain-language line: position on the map · what landed · what remains. [T-1..T-7]

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
the lane, bugs take it in arrival order; the parked wish resumes only once no bug waits. [T-9]

## Starting a new project (bootstrap)

Copy the templates (SPEC, TEST_MATRIX, ROADMAP, JOURNAL, NEXT_STEPS) → version-control gate → the first
wish enters the queue → the pipeline runs from step 0. [B-1] The gate itself is an always-rule: **no
landing into an unversioned host** — version control exists (and a remote is recommended) before the
first landing. [INV-8]

## Attaching to a live project (adoption)

Adoption is a sequence; each phase completes before the next. In practice the version-control gate [A-5]
is performed FIRST — before anything is touched or moved — so the whole run is reversible; the codes below
name meanings, not a frozen order (proven on the first real run, tlvphoto 2026-07-04). [A-0]

1. **Orient — read everything first.** Every existing document is read BEFORE anything is touched: README,
   any roadmap, any spec, any test suite, journals, TODO files, wikis in the repo. Adoption never assumes
   a blank slate. [A-1]
2. **Inventory** — code, user-facing surfaces (seeding the host's surface registry [E-10]), and the
   document set from the orient pass, listed with owners (file:line for surfaces). [A-2]
3. **Re-engineer the existing documents into livespec shapes** — an existing spec becomes SPEC.md sections
   (original claims kept, marked unverified); existing tests become matrix rows citing them at their real
   level; an existing roadmap/TODO becomes queue rows. Nothing existing is ignored, and nothing is trusted
   unreconciled. An unverified claim is reconciled (pinned to file:line, or removed) at the FIRST landing
   that touches its surface — and all remaining ones at the first milestone, whichever comes first. [A-3]
4. **Attic, not deletion.** Any file superseded during adoption or rework moves to the **attic (attic/)**
   — the host's archive folder: append-only, one manifest line per file (what it was, why moved, date); on
   a basename collision the source dir prefixes the name [E-9]. Flat-with-manifest vs dated subfolders is
   an open decision [D-1]. [A-4] The rule behind it never bends: **no adopt or rework run deletes a host
   file** — superseded files move to attic/ with a manifest line. [INV-7]
5. **Version-control gate (done FIRST — see the note above).** If the host has no git: init it, write a
   `.gitignore` that excludes heavy generated/media artifacts, make a pristine baseline commit (this
   doubles as the diff baseline), and recommend a remote (GitHub) plus a backup habit before the first
   landing [INV-8]. [A-5]
6. **Baseline snapshot [target]** — render/produce the current artifacts as they are and save them; this
   is the diff baseline the snapshot machinery [E-7] will guard. [A-6]
7. **Incremental thereafter** — the host now works by the same wish lifecycle as a bootstrapped project;
   installed skill versions are recorded in `.livespec/` at attach time. **On any version change (livespec
   or any installed skill), the agent RE-READS the changed SKILL.md before continuing** — never coasts on
   the stale in-memory version — and writes a one-line journal note naming old → new. The check is not
   event-only: at every safe breakpoint [M-2] the agent re-stats the installed skills and the package on
   disk (version / file mtime) and re-reads what changed — a parallel session may have shipped an update
   mid-flight. [A-7]

## Who decides what

**You (the human)** own taste, design, irreversible calls, publish/push gates, domain wording — and your
own working contract [INV-9]. [ACT-1] That contract is the **user profile**: proactivity mode (ask-at-max
| max-proactive), trust level, language, domain vocabulary, at `.livespec/profile.md` in the host (global
default as fallback), read by communicator before every human-facing exchange. [E-8] **Mode and trust are
written ONLY on your word — the agent may propose, never set; it never raises its own trust or proactivity
level.** [INV-9]

**The senior agent** owns judgment: spec deltas, matrix levels, findings triage, this document. [ACT-2]

**Workers (tiered) [router: target]** own mechanical execution, with persistent checkpoint files in the
host's `.livespec/checkpoints/` (gitignored; never /tmp — a reboot must not erase a resume point); the
cheapest sufficient tier does the job (haiku one-shot / sonnet multi-step / senior judgment), budget-aware.
Whether the queue's size class fixes the tier mechanically or the senior may override is an open decision
[D-2]. [ACT-3]

## The machines that hold the bounds [target]

What keeps "it works" honest, each one a named machine:

- **The matrix (TEST_MATRIX.md)** — one row per fact, each pinned to a test level; organized by
  architecture node × spec fact once the architecture doc exists. [E-5] Every row states the positive AND
  the negative side — what the fact does and what it must never do; the negative side is the regression
  fence. [INV-6]
- **The guardrails [target]** — the mechanical checks wired to the pre-push hook: completeness (against
  the surface registry) · tests-present · behaviour-traces-to-spec · declared-scope diff vs snapshot. [E-6]
- **The snapshot [target]** — the saved artifact of the last accepted run (HTML, JSON, files, numbers —
  any product), the baseline the next run is diffed against. The baseline advances only at *landed*, and
  only for the surfaces the change DECLARED; undeclared surfaces keep the old baseline — that asymmetry is
  what catches the unasked change. Retention (last-only vs last-N) is an open decision [D-3]. [E-7]
- **The surface registry** — one named list per host of every user-facing surface. The completeness check
  scans the real rendered artifact against it; a surface that renders but isn't registered is RED, so the
  registry is self-closing, never a trusted hand-list. [E-10]

## The package repo: who may write, and two sessions at once

livespec eats its own cooking — this spec, this queue, these rules govern livespec's own development
[target until the guardrails land: enforcement becomes mechanical with ROADMAP row 3; until then the
discipline is followed by hand and says so]. [M-4] That makes its repo a shared surface, and one evening
of two parallel sessions taught us the rules:

**Only a session you assigned to livespec itself writes this repo** (spec, queue, journal, skills,
templates, adopt procedure). Every other session — a host adopt run, a skill install, anything that merely
reads the package — is read-only here, with exactly one exception: creating a new wish file in the inbox.
The test is crisp: if the session cannot say "the human asked ME, in this conversation — or via a standing
routine the human created FOR livespec — to change livespec", it does not write. A host run's story lives
in the HOST's journal, never here. [INV-10]

**The inbox (inbox/)** is the parallel-safe intake door for wishes born outside a livespec session: one
NEW file per wish (`YYYY-MM-DD-<source>-<slug>.md`; name taken → append `-2`, `-3`, …), a few plain lines,
never an edit to an existing file — creating a fresh file cannot collide, shared files can. The outsider
COMMITS its one new file (a commit touching inbox/ only, message naming the source) — that commit is
inside the read-only exception. [E-11] A livespec session sweeps the inbox as its FIRST act and harvests
each file into a queue row — a wish must not wait durably-recorded but operationally invisible; the
harvest commit removes the file (git history keeps it — this internal removal is not an attic case, which
protects HOST files). So "spoken means it exists" holds without the outside session touching the queue. [T-10]

**Before writing to a repo — and again before every commit** — the agent re-checks `git status` + HEAD
against what it last read. If HEAD moved or the tree holds changes it did not make: STOP, re-read the
changed files, and only then proceed surgically — or back off to the inbox. New files under inbox/ are the
expected benign case, not a fence trip. Never push while another session is known to be live in the repo —
push coordination belongs to the human. Applies to livespec AND to any host repo two sessions might share
(the concurrency axis of the composition rule, made mechanical). [INV-11]

## The rhythm: breakpoints, milestones, pushes

- **Safe breakpoint (end of every movement):** NEXT_STEPS live-state replaced (never stacked) + dated
  JOURNAL entry + committed ⇒ the session memory can be wiped with zero loss. A long session SHOULD take
  that offer: at a breakpoint the agent compacts its own context to keep working — and SAYS so, never
  silently; a full wipe/clear of the conversation is the human's move, not the agent's. On the way back
  in, re-check skill freshness [A-7]. [M-2]
- **Milestone (MINOR gate):** full spec re-prove + matrix audit + surface-composition check + doc
  COMPACTION (pruning: redundancy removed from spec/matrix/queue/skills — nothing grows unboundedly) + a
  re-listing of every open human gate AND every unharvested inbox/ file, one line each, so a waiting wish
  is never forgotten + the formal index re-checked against the prose (the index is a derived map and must
  never drift into a second truth). [M-1]
- **Documents are versioned** like code: the queue and this spec carry dated versions, so "decided under
  which roadmap" is answerable. [M-3]
- **CI mirror [target]** — the guardrails' native home is the local pre-push hook; a host may additionally
  mirror the same checks in its CI (Jenkins, GitHub Actions) as a second net. Same checks, one source of
  truth — CI runs them, never redefines them. (ROADMAP row 14.) [M-5]
- **Push gate for livespec itself** — this repo is public and is the method's own flagship, so EVERY push
  is preceded, in the same session, by (a) the concurrent-edit fence [INV-11] and (b) a fresh whole-spec
  re-check: a product-prover pass over SPEC.md as it stands, its record landing in docs/prover/ before the
  push (record name `YYYY-MM-DD[-suffix].md`; suffix mandatory when the date's file exists). Findings that
  are must-fix fold before pushing; folds produced by the gate's own pass do NOT re-trigger the gate — they
  ship with the same record; the rest become queue rows. No re-check record for the pushed state ⇒ the
  push should not have happened. [M-6]

## Composing across axes

Every stateful surface of a host is composed across the canonical axes (view · mode · tier · viewport ·
persistence/reopen · concurrency where real) — and adoption adds one axis of its own: **document
provenance** (native-livespec × re-engineered-from-existing), because a re-engineered claim behaves
differently (unverified until reconciled per the adoption rules [A-3]) from a native one. [C-1]

## Open decisions

- ⟨DECIDE⟩ attic/ layout: flat with a manifest and source-dir prefix on collision (current pick) vs dated
  subfolders — revisit at the next real adopt run. [D-1]
- ⟨DECIDE⟩ whether the queue's size classification also fixes the model tier mechanically, or the senior
  may override per wish (current pick: router proposes, senior may override, override is logged). [D-2]
- ⟨DECIDE⟩ snapshot retention: last-only (current pick) vs last-N — revisit when a diff dispute needs
  history. [D-3]

## Formal index

Machine handles → home section. For the prover, the matrix, and transcript greps; the prose above is the
meaning, this table is only the map.

| Anchor | One line | Section |
|---|---|---|
| S-0 | shipped vs target marked honestly | header |
| E-1 | host project + its `.livespec/` | What livespec is |
| E-2 | wish: plain words, any moment | Throwing a wish |
| E-3 | queue ROADMAP.md, one row per wish | Throwing a wish |
| E-4 | spec: living truth, one surface = one name | Throwing a wish |
| E-5 | matrix: fact × test level | Machines |
| E-6 | guardrails on the pre-push hook [target] | Machines |
| E-7 | snapshot baseline, declared-scope diff [target] | Machines |
| E-8 | user profile: mode/trust/language | Who decides what |
| E-9 | attic: archive, never delete | Adoption step 4 |
| E-10 | surface registry, self-closing | Machines |
| E-11 | inbox: one new committed file per outside wish | Package repo |
| T-1..T-7 | arrived → … → landed → reported | Throwing a wish |
| T-8 | exits: declined / deferred / superseded | Throwing a wish |
| T-9 | bug preempts, wish parks with checkpoint | Bug cuts the line |
| T-10 | outside wish arrives via inbox, swept first | Package repo |
| INV-1 | no wish is ever lost | Throwing a wish |
| INV-2 | one landing at a time | Throwing a wish |
| INV-3 | every landing cites its row | Throwing a wish |
| INV-4 | a pending question never blocks the lane | Throwing a wish |
| INV-5 | no silent micro-decisions | Throwing a wish |
| INV-6 | matrix rows state DO and NEVER sides | Machines |
| INV-7 | attic, never deletion of host files | Adoption step 4 |
| INV-8 | no landing into an unversioned host | Bootstrap |
| INV-9 | trust set only by the human | Who decides what |
| INV-10 | write-ownership of the package repo | Package repo |
| INV-11 | concurrent-edit fence before write/commit | Package repo |
| B-1 | bootstrap: templates → gate → first wish | Bootstrap |
| A-0 | codes name meanings, VCS-gate runs first | Adoption |
| A-1 | orient: read everything first | Adoption step 1 |
| A-2 | inventory code + surfaces + docs | Adoption step 2 |
| A-3 | re-engineer docs, unverified until reconciled | Adoption step 3 |
| A-4 | superseded files move to attic | Adoption step 4 |
| A-5 | version-control gate | Adoption step 5 |
| A-6 | baseline snapshot [target] | Adoption step 6 |
| A-7 | re-read changed skills; re-stat at breakpoints | Adoption step 7 |
| ACT-1 | the human: taste, gates, wording | Who decides what |
| ACT-2 | senior agent: judgment | Who decides what |
| ACT-3 | tiered workers, checkpoints [router target] | Who decides what |
| M-1 | milestone: re-prove + audit + compaction + gate list | Rhythm |
| M-2 | safe breakpoint; announced self-compaction | Rhythm |
| M-3 | documents versioned like code | Rhythm |
| M-4 | livespec is its own host | Package repo |
| M-5 | CI mirror of the same checks [target] | Rhythm |
| M-6 | push gate: prover re-check before every push | Rhythm |
| C-1 | canonical axes + provenance axis | Composing across axes |
| D-1 | attic layout | Open decisions |
| D-2 | tier routing override | Open decisions |
| D-3 | snapshot retention | Open decisions |
