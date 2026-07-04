# livespec — SPEC (v0.1, 2026-07-04)

> How to read: the prose is the meaning; the short codes (E-x, INV-x, ⟨DECIDE⟩) are quiet machine handles
> at line-ends for the prover and the test matrix. Edit history lives in JOURNAL.md; this spec states
> today's truth. First self-application run: this spec was written by the method it describes (wish →
> intake → queue → spec). Reviewed next by product-prover (ROADMAP row 7).

## What livespec is

A package a software project attaches to — at the start or in the middle — to work by one discipline:
wishes are thrown in passing, each one enters a proven process, machines hold the bounds, the human is
interrupted only for decisions that are genuinely theirs. The package is four skills (spec-author,
product-prover, build-pipeline, communicator), document templates, an adoption procedure, and a set of
mechanical guardrails a project instantiates.

## Entities

- **Host project** — the codebase livespec is attached to. Owns its own SPEC, matrix, queue, journal. [E-1]
- **Wish** — one request in plain words, any size, spoken at any moment. [E-2]
- **Queue (ROADMAP.md)** — the persistent, ordered home of every wish. One row per wish: words · size ·
  status · acceptance criterion. [E-3]
- **Spec (SPEC.md)** — the living statement of what the product is. One surface = one name. [E-4]
- **Matrix (TEST_MATRIX.md)** — one row per fact, each pinned to a test level; organized by architecture
  node × spec fact once the architecture doc exists. [E-5]
- **Guardrails** — the mechanical checks wired to the pre-push hook: completeness · tests-present ·
  behaviour-traces-to-spec · declared-scope diff vs the previous run's snapshot. [E-6]
- **Snapshot** — the saved artifact of the last accepted run (HTML, JSON, files, numbers — any product),
  the baseline the next run is diffed against. [E-7]
- **User profile** — the human's working contract: proactivity mode (ask-at-max | max-proactive), trust
  level, language, domain vocabulary. Read by communicator before every human-facing exchange. [E-8]
- **Attic (attic/)** — the archive folder inside the host for files superseded during adoption or rework.
  Append-only, with a one-line manifest entry per file (what it was, why moved, date). [E-9]

## The life of a wish (states and transitions)

arrived → classified (size: bug / small / surface / large; bugs may preempt the lane) → spec-delta drafted
→ validated (the delta is checked against the whole spec; ONLY genuinely-human questions go out, batched;
everything else proceeds on the recommended option, marked in the row) → queued → in-work (serial: one
landing at a time) → landed (green suite + guardrails + committed + queue row closed with its acceptance
met) → reported (one plain-language line: position on the map · what landed · what remains). [T-1..T-7]

Invariants:
- **No wish is ever lost** — spoken means a queue row exists before anything else happens. [INV-1]
- **One landing at a time** — intake is parallel, execution is serial; a new wish waits unless it is a
  bug preempting. [INV-2]
- **Every landing cites its wish row** — commit message or journal entry names the row. [INV-3]
- **A pending human question never blocks the lane** — work proceeds on the recommended option; the
  question stays open in the row, revisitable. [INV-4]
- **No silent micro-decisions** — every choice not in the wish is either asked, or recorded in the spec
  and surfaced in the same report. [INV-5]
- **Positive and negative coverage in kind** — every matrix row states what the fact DOES and what it
  must NOT do; the negative side is the regression fence. [INV-6]

## Entry mode 1: bootstrap (new project)

Copy templates (SPEC, TEST_MATRIX, ROADMAP, JOURNAL, NEXT_STEPS) → version-control gate (see INV-8) →
first wish enters the queue → pipeline runs from step 0. [B-1]

## Entry mode 2: adopting a live project

Adoption is a sequence; each phase completes before the next. [A-0]

1. **Orient — read everything first.** Every existing document is read BEFORE anything is touched:
   README, any roadmap, any spec, any test suite, journals, TODO files, wikis in the repo. Adoption
   never assumes a blank slate. [A-1]
2. **Inventory** — code, user-facing surfaces, and the document set from A-1, listed with owners
   (file:line for surfaces). [A-2]
3. **Re-engineer the existing documents into livespec shapes** — an existing spec becomes SPEC.md
   sections (original claims kept, marked unverified until reconciled); existing tests become matrix
   rows citing them at their real level; an existing roadmap/TODO becomes queue rows. Nothing existing
   is ignored, and nothing is trusted unreconciled. [A-3]
4. **Attic, not deletion** — any file superseded by A-3 moves to attic/ with a manifest line. An adopt
   run NEVER deletes a host file. [A-4] [INV-7]
5. **Version-control gate** — if the host has no git: init it, and recommend a remote (GitHub) plus a
   backup habit, before the first landing. No landing into an unversioned host. [A-5] [INV-8]
6. **Baseline snapshot** — render/produce the current artifacts as they are and save them; this is the
   diff baseline. From here every change declares its scope and is diffed against the baseline. [A-6]
7. **Incremental thereafter** — the host now works by the same wish lifecycle as a bootstrapped project. [A-7]

## Actors

- **The human** — owns taste, design, irreversible calls, publish/push gates, domain wording. [ACT-1]
- **The senior agent** — owns judgment: spec deltas, matrix levels, findings triage, this document. [ACT-2]
- **Workers (tiered)** — mechanical execution with persistent checkpoint files; cheapest sufficient tier
  (haiku one-shot / sonnet multi-step / senior judgment), budget-aware. [ACT-3]

## Milestones and hygiene

- **Milestone (MINOR gate):** full spec re-prove + matrix audit + surface-composition check + doc
  COMPACTION (pruning: redundancy removed from spec/matrix/queue/skills — nothing grows unboundedly). [M-1]
- **Safe breakpoint (end of every movement):** NEXT_STEPS live-state replaced (never stacked) + dated
  JOURNAL entry + committed ⇒ the session memory can be wiped with zero loss. [M-2]
- **Documents are versioned** like code: the queue and this spec carry dated versions, so "decided under
  which roadmap" is answerable. [M-3]
- **The package is itself a host project of livespec** — this spec, this queue, these rules govern
  livespec's own development (self-application; run #1 = this document). [M-4]

## Cross-section composition

Every stateful surface of a host is composed across the canonical axes (view · mode · tier · viewport ·
persistence/reopen · concurrency where real) — and adoption adds one axis of its own: **document
provenance** (native-livespec × re-engineered-from-existing), because a re-engineered claim behaves
differently (unverified until reconciled) from a native one. [C-1]

## Open decisions

- ⟨DECIDE⟩ attic/ layout: flat with a manifest (current pick) vs dated subfolders — revisit at the first
  real adopt run. [D-1]
- ⟨DECIDE⟩ whether the queue's size classification also fixes the model tier mechanically, or the senior
  may override per wish (current pick: router proposes, senior may override, override is logged). [D-2]
- ⟨DECIDE⟩ snapshot retention: last-only (current pick) vs last-N — revisit when snapshots get heavy. [D-3]
