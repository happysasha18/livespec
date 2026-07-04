# livespec — SPEC (v0.3, 2026-07-04)

> How to read: the prose is the meaning; the short codes (E-x, INV-x, ⟨DECIDE⟩) are quiet machine handles
> at line-ends for the prover and the test matrix. Edit history lives in JOURNAL.md; this spec states
> today's truth. Written by the method it describes (self-application run #1); proven by product-prover
> the same day (docs/prover/2026-07-04.md — 11 findings, all folded → this v0.2).

**Current vs target.** Shipped today: the four skills, the templates, the adoption procedure text, this
spec and queue. Target (each owned by a ROADMAP row, not yet code): the guardrails scaffold [E-6], the
snapshot machinery [E-7], the model router [ACT-3], and therefore full self-enforcement [M-4]. This spec
never claims shipped what isn't — sections below marked [target] await their row. [S-0]

## What livespec is

A package a software project attaches to — at the start or in the middle — to work by one discipline:
wishes are thrown in passing, each one enters a proven process, machines hold the bounds, the human is
interrupted only for decisions that are genuinely theirs. The package is four skills (spec-author,
product-prover, build-pipeline, communicator), document templates, an adoption procedure, and a set of
mechanical guardrails a project instantiates.

## Entities

- **Host project** — the codebase livespec is attached to. Owns its own SPEC, matrix, queue, journal,
  surface registry, and a `.livespec/` folder (profile, checkpoints, installed-skill versions). [E-1]
- **Wish** — one request in plain words, any size, spoken at any moment. [E-2]
- **Queue (ROADMAP.md)** — the persistent, ordered home of every wish. One row per wish: words · size ·
  status · acceptance criterion. A row, once created, is never deleted — only closed with a named exit. [E-3]
- **Spec (SPEC.md)** — the living statement of what the product is. One surface = one name. [E-4]
- **Matrix (TEST_MATRIX.md)** — one row per fact, each pinned to a test level; organized by architecture
  node × spec fact once the architecture doc exists. Every row states the positive AND the negative side
  (what the fact does / what it must never do). [E-5]
- **Guardrails [target]** — the mechanical checks wired to the pre-push hook: completeness (against the
  surface registry) · tests-present · behaviour-traces-to-spec · declared-scope diff vs snapshot. [E-6]
- **Snapshot [target]** — the saved artifact of the last accepted run (HTML, JSON, files, numbers — any
  product), the baseline the next run is diffed against. The baseline advances only at *landed*, and only
  for the surfaces the change DECLARED; undeclared surfaces keep the old baseline — that asymmetry is what
  catches the unasked change. [E-7]
- **User profile** — the human's working contract: proactivity mode (ask-at-max | max-proactive), trust
  level, language, domain vocabulary. Lives at `.livespec/profile.md` in the host (global default as
  fallback). Mode and trust are written ONLY on the human's word — the agent may propose, never set. Read
  by communicator before every human-facing exchange. [E-8]
- **Attic (attic/)** — the archive folder inside the host for files superseded during adoption or rework.
  Append-only, one manifest line per file (what it was, why moved, date); on basename collision the source
  dir prefixes the name. [E-9]
- **Surface registry** — one named list per host of every user-facing surface. The completeness check
  scans the real rendered artifact against it; a surface that renders but isn't registered is RED, so the
  registry is self-closing, never a trusted hand-list. [E-10]
- **Inbox (inbox/)** — the parallel-safe intake door for wishes born OUTSIDE a livespec session (a host's
  adopt run, any passing conversation). One NEW file per wish (`YYYY-MM-DD-<source>-<slug>.md`; if the name
  exists, append `-2`, `-3`, …), a few plain lines; never an edit to an existing file — creating a fresh
  file cannot collide, shared files can. The outsider COMMITS its one new file (a commit touching inbox/
  only, message naming the source) — that commit is inside the read-only exception. The next livespec
  session harvests inbox files into queue rows; the harvest commit removes the file (git history keeps it —
  this internal removal is not an INV-7 case, which protects HOST files). [E-11]

## The life of a wish (states and transitions)

arrived → classified (size: bug / small / surface / large; bugs may preempt — see below) → spec-delta
drafted → validated (the delta is checked against the whole spec; ONLY genuinely-human questions go out,
batched; everything else proceeds on the recommended option, marked in the row) → queued → in-work
(serial: one landing at a time) → landed (green suite + guardrails + committed + queue row closed with its
acceptance met) → reported (one plain-language line: position on the map · what landed · what remains). [T-1..T-7]

Exit states (a wish can end without landing; the row stays in the table): **declined** (the human said
no) · **deferred** (parked with a named revisit trigger) · **superseded** (absorbed by another wish; the
row points to the absorbing one). [T-8]

Preemption: a bug may interrupt the wish in-work. The interrupted wish moves to **parked**: a checkpoint
is written (failing test names if red, hypothesis, touched files — nothing red is ever committed), the bug
takes the lane, and the parked wish resumes as the immediate next landing. [T-9]

Arrival from outside: a wish born in a NON-livespec session (a host adopt run that hits a package defect,
any other conversation) arrives as one new `inbox/` file [E-11] — that file IS the durable record, so
"spoken means it exists" [INV-1] holds without the outside session touching the queue. A livespec session
sweeps inbox/ as its FIRST act and harvests each file into a row — a wish must not wait durably-recorded
but operationally invisible. [T-10]

Invariants:
- **No wish is ever lost** — spoken means a queue row exists before anything else happens; rows are never
  deleted, only closed with a named exit state. [INV-1]
- **One landing at a time** — intake is parallel, execution is serial; a new wish waits unless it is a
  bug preempting per T-9. [INV-2]
- **Every landing cites its wish row** — commit message or journal entry names the row. [INV-3]
- **A pending human question never blocks the lane** — work proceeds on the recommended option; the
  question stays open in the row, revisitable. [INV-4]
- **No silent micro-decisions** — every choice not in the wish is either asked, or recorded in the spec
  and surfaced in the same report. [INV-5]
- **Positive and negative coverage in kind** — every matrix row states what the fact DOES and what it
  must NOT do; the negative side is the regression fence. [INV-6]
- **Attic, never deletion** — no adopt or rework run deletes a host file; superseded files move to
  attic/ with a manifest line. [INV-7]
- **No landing into an unversioned host** — version control exists (and a remote is recommended) before
  the first landing. [INV-8]
- **Trust is set only by the human** — the agent never raises its own trust or proactivity level. [INV-9]
- **Session write-ownership** — only a session the human has assigned to livespec ITSELF writes this
  repo's files (spec, queue, journal, skills, templates, adopt procedure). Every other session — a host
  adopt run, a skill install, anything that merely reads the package — is READ-ONLY here, with exactly one
  exception: creating a new wish file in inbox/ [E-11]. The test is crisp: if the session cannot say "the
  human asked ME, in this conversation — or via a standing routine the human created FOR livespec — to
  change livespec", it does not write. A host run's story lives in
  the HOST's journal, never here. [INV-10]
- **Concurrent-edit fence** — before writing to a repo and again before every commit, the agent re-checks
  `git status` + HEAD against what it last read; if HEAD moved or the tree holds changes it did not make,
  it STOPS, re-reads the changed files, and only then proceeds surgically — or backs off to inbox/. New
  files under inbox/ are the expected benign case, not a fence trip. It
  never pushes while another session is known to be live in the repo — push coordination belongs to the
  human. Applies to livespec AND to any host repo two sessions might share (the concurrency axis of C-1
  made mechanical). [INV-11]

## Entry mode 1: bootstrap (new project)

Copy templates (SPEC, TEST_MATRIX, ROADMAP, JOURNAL, NEXT_STEPS) → version-control gate [INV-8] → first
wish enters the queue → pipeline runs from step 0. [B-1]

## Entry mode 2: adopting a live project

Adoption is a sequence; each phase completes before the next. In practice the version-control gate [A-5]
is performed FIRST — before A-1 touches or moves anything — so the whole run is reversible; the codes below
name meanings, not a frozen order (proven on the first real run, tlvphoto 2026-07-04). [A-0]

1. **Orient — read everything first.** Every existing document is read BEFORE anything is touched:
   README, any roadmap, any spec, any test suite, journals, TODO files, wikis in the repo. Adoption
   never assumes a blank slate. [A-1]
2. **Inventory** — code, user-facing surfaces (seeding the surface registry [E-10]), and the document set
   from A-1, listed with owners (file:line for surfaces). [A-2]
3. **Re-engineer the existing documents into livespec shapes** — an existing spec becomes SPEC.md
   sections (original claims kept, marked unverified); existing tests become matrix rows citing them at
   their real level; an existing roadmap/TODO becomes queue rows. Nothing existing is ignored, and nothing
   is trusted unreconciled. An unverified claim is reconciled (pinned to file:line, or removed) at the
   FIRST landing that touches its surface — and all remaining ones at the first milestone, whichever
   comes first. [A-3]
4. **Attic, not deletion** — any file superseded by A-3 moves to attic/ per INV-7. [A-4]
5. **Version-control gate (done FIRST — see A-0)** — if the host has no git: init it, write a `.gitignore`
   that excludes heavy generated/media artifacts, make a pristine baseline commit (this doubles as the A-6
   baseline), and recommend a remote (GitHub) plus a backup habit before the first landing [INV-8]. [A-5]
6. **Baseline snapshot [target]** — render/produce the current artifacts as they are and save them; this
   is the diff baseline per E-7. [A-6]
7. **Incremental thereafter** — the host now works by the same wish lifecycle as a bootstrapped project;
   installed skill versions are recorded in `.livespec/` at attach time. **On any version change (livespec
   or any installed skill), the agent RE-READS the changed SKILL.md before continuing** — never coasts on
   the stale in-memory version — and writes a one-line journal note naming old → new. The check is not
   event-only: at every safe breakpoint [M-2] the agent re-stats the installed skills and the package on
   disk (version / file mtime) and re-reads what changed — a parallel session may have shipped an update
   mid-flight. [A-7]

## Actors

- **The human** — owns taste, design, irreversible calls, publish/push gates, domain wording, and the
  profile's mode/trust fields [INV-9]. [ACT-1]
- **The senior agent** — owns judgment: spec deltas, matrix levels, findings triage, this document. [ACT-2]
- **Workers (tiered) [router: target]** — mechanical execution with persistent checkpoint files in the
  host's `.livespec/checkpoints/` (gitignored; never /tmp — a reboot must not erase a resume point);
  cheapest sufficient tier (haiku one-shot / sonnet multi-step / senior judgment), budget-aware. [ACT-3]

## Milestones and hygiene

- **Milestone (MINOR gate):** full spec re-prove + matrix audit + surface-composition check + doc
  COMPACTION (pruning: redundancy removed from spec/matrix/queue/skills — nothing grows unboundedly) +
  a re-listing of every open human gate AND every unharvested inbox/ file, one line each, so a waiting
  wish is never forgotten. [M-1]
- **Safe breakpoint (end of every movement):** NEXT_STEPS live-state replaced (never stacked) + dated
  JOURNAL entry + committed ⇒ the session memory can be wiped with zero loss. A long session SHOULD take
  that offer: compact or clear the conversation context at a breakpoint (the disk state is the resume) and
  re-check skill freshness [A-7] on the way back in. [M-2]
- **Documents are versioned** like code: the queue and this spec carry dated versions, so "decided under
  which roadmap" is answerable. [M-3]
- **The package is itself a host project of livespec [target until E-6 lands]** — this spec, this queue,
  these rules govern livespec's own development. Enforcement becomes mechanical when the guardrails
  scaffold (ROADMAP row 3) ships; until then the discipline is followed by hand and says so. [M-4]
- **CI mirror [target]** — the guardrails' native home is the local pre-push hook; a host may additionally
  mirror the same checks in its CI (Jenkins, GitHub Actions) as a second net. Same checks, one source of
  truth — CI runs them, never redefines them. (ROADMAP row 14.) [M-5]
- **Push gate for livespec itself** — this repo is public and is the method's own flagship, so EVERY push
  is preceded, in the same session, by (a) the concurrent-edit fence [INV-11] and (b) a fresh whole-spec
  re-check: a product-prover pass over SPEC.md as it stands, its record landing in docs/prover/ before the
  push (record name `YYYY-MM-DD[-suffix].md`; suffix mandatory when the date's file exists). Findings that
  are must-fix fold before pushing; folds produced by the gate's own pass do NOT re-trigger the gate — they
  ship with the same record; the rest become queue rows. No re-check record for the pushed state ⇒ the push
  should not have happened. [M-6]

## Cross-section composition

Every stateful surface of a host is composed across the canonical axes (view · mode · tier · viewport ·
persistence/reopen · concurrency where real) — and adoption adds one axis of its own: **document
provenance** (native-livespec × re-engineered-from-existing), because a re-engineered claim behaves
differently (unverified until reconciled per A-3) from a native one. [C-1]

## Open decisions

- ⟨DECIDE⟩ attic/ layout: flat with a manifest and source-dir prefix on collision (current pick) vs dated
  subfolders — revisit at the first real adopt run. [D-1]
- ⟨DECIDE⟩ whether the queue's size classification also fixes the model tier mechanically, or the senior
  may override per wish (current pick: router proposes, senior may override, override is logged). [D-2]
- ⟨DECIDE⟩ snapshot retention: last-only (current pick) vs last-N — revisit when a diff dispute needs
  history. [D-3]
