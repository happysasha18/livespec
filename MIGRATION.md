# MIGRATION — the catch-up walk

This is the operating guide for the catch-up walk: the procedure an already-adopted host's own session runs to bring the host's documents and records onto the current package version. A package release that owes its hosts actions lands one dated chapter at the end of this file; the walk reads the chapter chain and applies it under the owner's gate, preserving every recorded fact. Nothing outside a host's own session ever writes that host's repo (INV-10).

The walk is the executable projection of PRODUCT_SPEC.md, "Bringing an adopted host up to the current pack" (F-catchup, A-11, INV-89…INV-92). The spec states the facts; this guide states the moves.

## When to run this

The ask arrives in any wording. It might read "re-layout the documentation" or "catch up to the current pack"; it names no procedure, so the package names one, and that procedure is this walk.

Route the ask before doing anything else. A host that never adopted the pack goes to adoption (`adopt/ADOPT.md`) — the first-adoption phases, not this walk. A host that already adopted goes to this catch-up walk. A single-document edit is not this walk; it belongs to the ordinary docs-only edit. A restructure of the host's own product is not this walk either; it is the host's own queue row through the build pipeline. This walk fires only to move an adopted host's own live-spec documents and records onto a newer package version. The catch-up walk fires only when the host's recorded package version is behind the current package VERSION. A docs restructure that carries no version delta is the host's own queue row through its pipeline, whatever wording the ask used. The trigger wordings are examples under this test. A wording never decides the routing; the version delta decides. (INV-110)

## The walk

The walk runs four phases in order (A-11). Its plan and its working artifacts live in the host's `.live-spec/adopt/` through the whole walk, tracked in git as the run's audit trail.

## Phase 1 — orient on the delta

1. Read the host's installed-set record and the tree as found.
2. Read the package's current `VERSION` and journal, and the migration chapters below.
3. Build the work list: the ordered chain of migration chapters from the host's recorded package version to the current one (see "Migration chapters"), plus any drift the tree shows against what those chapters expect. A record that carries no readable package version — commit pins, or no record at all — starts the chain at the earliest chapter; every step's already-done check makes over-application harmless (INV-89).
4. Treat every precondition written in this guide as a claim to check against the tree. Where a written precondition and the tree disagree, the tree is the truth.
5. Name the founding questions this host has never answered: read the host profile's `founding.set-version` against the current set in `scripts/founding-questions.json`, and list each question added after the host's recorded version — the agent card at `.live-spec/agent.md` (SPEC E-32) among them for a host that founded before it. A host with no `founding.set-version` line founded before the set was versioned and owes every question. Each gap rides the plan for the owner to answer, and the walk records the current set version once answered; a never-answered question is surfaced for the owner, answered on no one's behalf (SPEC INV-227, the duty binds forward INV-159).

## Phase 2 — plan, behind the owner's gate

Write one plan document into the host's `.live-spec/adopt/`, where it lives through the whole walk. It lists every file that moves, merges, or retires, every record that reformats, every rename offered, and every open conflict. It names the baseline commit of Phase 3 as the walk's restore point and states the one restore command that returns the host to the pre-walk state.

The owner's word on the plan comes before any file moves. A walk that finds nothing to do reports that and ends. No file is touched until the plan is approved.

## Phase 3 — execute, preserving facts

1. Open with a clean-tree baseline commit in the host (A-5). This commit is the restore point named in the plan; the whole walk stays reversible to it by the single restore command.
2. Run under the checkpoint discipline. The walk's checkpoint names the plan document and the per-step state. An interrupted walk resumes from the checkpoint under the already-given gate — the owner is not asked twice.
3. Apply each step under the half-done-state law and the preserve-and-re-home law (see "Step laws"). A step reads its precondition from the tree at the moment it runs, so a walk resumed after a partial application does the right thing on what it finds.

## Phase 4 — verify and re-record

1. Run the pack's CURRENT gate set backward over the host's existing tree — every gate scans the
   whole tree, retroactive by construction (SPEC INV-176), so a gate the pack gained since the host
   adopted finds the older debt now; an oversized backlog is absorbed by re-seeding the ratchet caps
   (SPEC INV-172).
2. Run the host's own gates, including the test suite where one exists. A red gate is the walk's own open defect: the walk stays open until the gates read green, and the checkpoint carries the red state across sessions.
3. Re-record the installed-set record in the current format.
4. Land one journal chapter in the host: what moved, why, the provenance, and any finding held for the owner.
5. Run the before-and-after self-test below and clear it before the walk is called done.

The plan document and the superseded files rest in the attic and the adopt records. The walk changes documents and records only; it creates no visible product surface, so the plan opens by the ordinary show rule.

### The before-and-after self-test (INV-92)

Before any file moves, in Phase 3, record a pre-walk inventory beside the plan in `.live-spec/adopt/`: every document with a content fingerprint, the host spec's anchor multiset, and the test suite's verdict and count as found.

After the execute phase, record the same inventory again and compare the two. Every difference must be accounted for by a plan item — a file is unchanged, re-homed to a named new path, merged from named sources, or resting in the attic under its manifest line; an anchor-multiset delta must match a change the plan names; and the suite reads at least as green as before. A difference outside the plan blocks the verify phase until the owner's gate accepts it as a plan amendment or the step is reverted.

The baseline commit is the walk's restore point: the plan names that commit and states the one restore command that returns the host to the pre-walk state. The attic keeps every superseded file readable without any restore.

## Step laws

### The half-done-state law (INV-89)

Every catch-up step reads its precondition from the tree before it acts. A step whose end state already holds is reported done and skipped. A step that finds both the old and the new form present merges file by file:

- A file with identical content on both sides drops the old copy to the attic.
- A profile file with differing content reconciles by the settings ladder: a line whose home sits at a machine-shared scope moves up, and a host-scoped line stays. A move up writes a machine-shared file, so it re-reads that file immediately before appending (the promotion law).
- Any other differing file, and any remaining conflict, rides the plan to the owner's gate.

Across all of this, never nest the old directory inside the new one, and never overwrite the new form with the old. The case this law was born from: `.livespec/` and `.live-spec/` both exist in a host that started the rename and stopped — the walk merges them rather than clobbering either.

An installed-set record kept in an outdated format, such as commit pins, retires to the attic. The new record is read from the version lines of the skills actually installed on the machine and from the package `VERSION`. The skills on disk are the authoritative set; a stale record is corrected from them.

### The preserve-and-re-home law (INV-90)

The host's recorded facts survive the walk. Content moves into the current shapes, and a fact leaves its home only by moving to a better one. Settled prose is rewritten only where the owner rejected it or where the new shape cannot hold it as written; the plan carries each proposed rewrite and the gate decides.

A host that adopted under its own names keeps them. A product spec named `SPEC.md` stays `SPEC.md`, recorded as one host-profile line, `spec.file: SPEC.md`; the package's guides read "PRODUCT_SPEC.md" as whatever file that line names. The plan may offer the rename together with its pointer sweep, and the gate decides. The canonical document set and names live in one list in `adopt/ADOPT.md`; this guide points there and holds no second copy.

Stray state files re-home. A checkpoint file at the repo root moves to `.live-spec/checkpoints/`, a closed one to the attic, and a look-alike state directory merges under the half-done-state law.

## Pair routing

The walk covers exactly one host. When the ask arrives at one window of an engine-and-instance pair and means both halves, the window executes its own repo's walk and files one inbox wish naming the other half's catch-up debt (INV-86) — it never writes the other repo.

A pair half that carries no `.live-spec` records of its own is an under-attached host. Its walk opens with the full adoption run for that repo (`adopt/ADOPT.md`) before the catch-up items — the walk runs the full adoption for that repo first, then catches it up.

A Phase-4 gate that reads red only because the other half's own catch-up has not landed keeps the walk open exactly as any red does: the checkpoint carries the state across sessions, and the block rides the host's status reports as a dated blocked-on-the-other-half line under the pair law (INV-56, INV-27) until the other half's session lands its walk.

## Machine-level steps

Some steps touch the machine's shared homes — the installed-skills folder and the personal profile — and run once per machine, not once per host. Each such step states its already-done check: the directory that already exists, or the record that already reads current. A step whose check passes is reported done and skipped, exactly as under the half-done-state law.

## Migration chapters

A package release that changes something hosts must act on lands one dated, versioned chapter here, stating the host-side steps. A release owing nothing adds no chapter and says so in its changelog. Orient reads the host's recorded package version, and the work list is the chain of chapters from that version to the current one, walked oldest first, one plan carrying the whole chain however far behind the host is.

### 1.0.0 — 2026-07-10

This chapter absorbs the 2026-07-05 package rename (livespec → live-spec, one name everywhere) and the same wave's matrix reshape, restated so each step is safe on a half-done tree.

1. Rename the host's pack folder `.livespec/` → `.live-spec/`. If only the old name exists, rename it preserving history. If both exist, merge file by file under the half-done-state law — never nest the old directory inside the new one, never overwrite the new form with the old. If only the new name exists, the step is done and skipped.
2. Sweep the host's own docs for `livespec` references (spec, roadmap, and journal pointers to the pack; skill names in running text) → `live-spec`. The host's journal history entries stay as written.
3. Re-record the installed set. The base skill is now named `live-spec-base`. A commit-pin record retires to the attic; the new record is read from the version lines of the skills actually installed and the package `VERSION`.
4. Update the git remote URL at leisure (`git remote set-url … live-spec.git`). The GitHub redirect keeps old clone and remote URLs working meanwhile, so this step blocks nothing.
5. Once-per-machine moves, each with its already-done check: `~/.claude/livespec/` → `~/.claude/live-spec/` (skip if the target already exists), and `~/.claude/skills/livespec-base` → `~/.claude/skills/live-spec-base` (skip if the target already exists). Sweep the machine-global loader file (`~/.claude/CLAUDE.md`, E-16) for old-name pointers the same once — already-done check: the file reads current.
6. Matrix reshape. A host holding an old-shape flat matrix regroups its rows under the architecture nodes at its first architecture landing — rows are preserved and re-homed, never re-derived from scratch.

### 2.0.0 — 2026-07-16

**Host action: none.** The 2.0.0 major is a readability and compaction pass over the pack's own living
documents (the spec, architecture, matrix, roadmap, and skill docs read plainly and stay compact), plus
the machinery that keeps them that way. It changes no runtime behaviour, no skill interface, no file the
host writes, and no adoption or catch-up step. A host adopts it the ordinary way — pull the pack, run
`scripts/sync-skills.sh` — and owes nothing further.

The major number marks two things a host inherits automatically by adopting, not a breaking change:

1. **The compaction ratchet on the host's own push gate.** A host that runs the pack's guardrails now
   carries the reached-clean floor: the register lint at zero, the redundancy gate at zero, the debt cap
   that only ratchets down (`scripts/spec-debt-cap.json`), and the compaction freeze
   (`guardrails/check-freeze.sh`, pre-push gate k, which skips itself where no local baseline exists). A
   host's documents can get cleaner from here, never worse — the recurrence-stop for document bloat.
2. **The method rule (base rule 30 / SPEC INV-164).** A quality a machine can verify is enforced by a
   gate, held by no pass's attention; compaction runs at every push, above the milestone whole-read.

No host file changes, so the catch-up walk records this chapter as done on read.
