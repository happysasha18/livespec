# ADOPT — Mid-flight adoption procedure

How to attach live-spec to an existing codebase — at the start or in the middle. This is the executable
projection of PRODUCT_SPEC.md "Entry mode 2: adopting a live project" (A-0…A-9). Follow the phases in order; each
has a clear done-state. Adoption never assumes a blank slate, and it **never deletes a host file** (INV-7).

First proven on a real project (tlvphoto, 2026-07-04); the practical notes below are from that run.

**The package repo is read-only from a host session (SPEC INV-10).** An adopt run that discovers a live-spec
defect (a stale phase here, a template gap) does NOT edit the live-spec repo — it drops ONE new file into
live-spec's `inbox/` (see `inbox/README.md`) and records the finding in the HOST's own journal. Learned the
hard way: the pilot run edited live-spec directly while another session was mid-flight in the same repo.

---

## Phase 0 — Version-control gate FIRST (SPEC A-5, done early for reversibility)

The spec requires version control before the first *landing* (INV-8). In practice, do it **before you touch
anything** — then the whole adopt run is reversible.

1. If the host has no git: `git init`.
2. Write a `.gitignore` that keeps source + structured data and excludes the virtualenv, caches, and heavy
   generated/media artifacts. (On the pilot this was ~7.6 GB of media out of a 7.7 GB tree — commit the
   ~source and exclude the exports.)
3. Make ONE **baseline commit** of the pristine original — this is the restore point and the diff baseline
   (SPEC A-6 / E-7).
4. **Settle the remote — a named deliverable (SPEC A-5).** By the first landing a
   remote (GitHub) either EXISTS or the human has EXPLICITLY DECLINED one; record the outcome in the run's
   journal entry. Creating/pushing the remote is the human's gate — offer and follow through, don't do it
   silently and don't let "recommended" quietly become "never happened" (the pilot ended local-only that way).

Done when: the host is a git repo with a clean baseline commit, heavy artifacts are gitignored, and the
remote outcome (exists / declined) is recorded.

---

## Phase 0.5 — Optional cruft sweep (human-gated; SPEC A-9)

Writing the `.gitignore` usually surfaces pre-existing regenerable junk (caches, build leftovers, stale
exports). Offer ONE sweep: list what qualifies as "N files, M MB" per group, get the human's explicit OK,
delete ONLY the approved regenerable junk. Never silent, never authored content — anything a human wrote
goes through the attic (INV-7) instead of this sweep. Skipping the offer is fine; deleting without the OK is not.

Done when: the sweep was offered and either declined or executed exactly as approved.

---

## Phase 1 — Orient: read everything first (SPEC A-1)

**Who am I working with (SPEC B-3) — the first breath of orient:** before any founding question
resolves, look for the human's personal profile (`~/.claude/live-spec/profile.md`). Found ⇒ load it
and say so — the file, plus any line ignored aloud (SPEC E-13). Absent ⇒ offer to create it from
`templates/profile.template.md`: the human tells about themselves and may name sources to read; every
line lands on their word, and a declined proposal is dropped. Declining the whole step runs the
session on package defaults, said aloud. A worker session never runs this step (SPEC ACT-3).

**Founding questions ride the orient (SPEC B-2 via A-1):** before the digest closes, the run asks —
or reads from the human's profile — the answers that shape everything downstream, personal-vs-reusable
first, and **what kind of project this is** — book · backend service · static site · fullstack app ·
CLI · skill pack · a custom kind — recorded as the host profile's `project.kind` line; that one is
always ASKED, never profile-read: no personal line can say what a host is (SPEC INV-36); an answer
inferred from examples is a defect. The same breath asks — or tells the standing
default of — the ECONOMY rung (`budget.pressure`: full · lean · tight, SPEC T-19): the human hears the
choice at setup, before any crisis; the rung moves only on their word.

**Skill search rides the setup (SPEC INV-65):** with the founding questions answered, scan the
installed skills and the catalogs you can reach for ones matching the project's kind and its crafts;
propose the fit list with a recommendation — the human's word picks. Later, any struggle (a ledger
entry seen twice, a taste artifact rejected twice) buys one search before the next attempt.

**The settings card closes the setup (SPEC INV-87):** when setup finishes, once the project's kind
and the working pace have been settled, the session renders the settings card with
`scripts/onboarding-card.py` and opens it for the human. It is one page showing what is set up and
what is theirs to change, and it asks nothing.

Read every existing document BEFORE writing or moving anything: README, any roadmap, any spec, any test
suite, journals, TODO/notes files, changelogs, in-repo wikis. **A well-run host may already keep most of
these in live-spec shape** — then adoption is light and you rewrite nothing.

Produce a **document digest** (`.live-spec/adopt/orient_digest.md` — ALL adopt working artifacts live in
`.live-spec/adopt/`, tracked in git as the run's audit trail, never in the host's own folders; SPEC A-8):
per doc — kind (spec/roadmap/journal/notes/report/…) · one-paragraph what-it-says · CURRENT or STALE (and
why) · what it overlaps/duplicates.

> Delegate this read to a worker — it is fan-out fact-gathering. Judgment stays with the senior, who reads the digest.

Done when: every existing document has a digest entry.

---

## Phase 2 — Inventory the code & surfaces (SPEC A-2)

**Registry form (E-10):** when the host has a test harness, lift the surface inventory into an
executable completeness gate (or recognise an existing one — a declared surface map inside a gate test
satisfies E-10 outright); the `SURFACE_REGISTRY.md` document is the fallback for doc-only hosts.

1. List every **user-facing output** (HTML, CLI output, API responses, rendered widgets, emails, consumed
   JSON).
2. List every **surface** (a page, panel, form, chart) and pin it to its owning `file:line` — this seeds the
   **surface registry** (`SURFACE_REGISTRY.md`, SPEC E-10), which is self-closing: a surface that renders but
   isn't registered is RED.
3. List every significant **data entity** (from filenames, JSON keys, class names, tables, config).

Record in `.live-spec/adopt/inventory.md` (one line per item; A-8 home), then lift the surfaces into
`SURFACE_REGISTRY.md`.

Done when: the inventory exists and every surface in the registry has a real `file:line` (or is marked
`⟨DECIDE⟩`).

---

## Phase 3 — Re-engineer existing documents into live-spec shapes (SPEC A-3)

Turn what exists into the canonical set — **keeping original claims, marking them unverified**:
- an existing spec → `PRODUCT_SPEC.md` sections (entities / states & transitions / actors / invariants /
  cross-section composition / glossary); if the host's spec is already in this shape, **do not rewrite it** —
  just confirm structure and fill the two things hosts usually lack: the **surface registry** (Phase 2) and
  the **test matrix** (Phase 5).
- existing tests → matrix rows citing them at their real level.
- an existing roadmap/TODO → queue rows in `ROADMAP.md`.

**Provenance (SPEC C-1).** Mark each document `native-live-spec` (authored in the method) or
`re-engineered-from-existing`. A re-engineered claim is **unverified until reconciled** — pinned to
`file:line` or removed at the FIRST landing that touches its surface, and all remaining ones at the first
milestone. A host authored entirely in the method (like the pilot) has no reconcile backlog beyond its own
`⟨DECIDE⟩` / `[planned]` markings.

**Unbacked live surfaces get a verdict (SPEC A-10).** Anything the inventory found that reaches the user
but has no spec backing — a de-facto prototype, the adopted host's most common residue — is flagged here,
and the human decides per surface: **promote** (it enters at the spec step as a feature, SPEC INV-16) ·
**quarantine** (moved into a prototype home and labelled, SPEC E-17) · **attic** (A-4). No unbacked
surface is silently registered as product.

Done when: the canonical doc set exists (SPEC/ROADMAP/JOURNAL/NEXT_STEPS + registry + matrix), every claim
is marked native or unverified, and every unbacked live surface carries its verdict.

---

## Phase 4 — Attic over deletion (SPEC A-4, INV-7)

Any document Phase 3 supersedes (an old spec, a stale resume, a folded notes file, a completed process
checkpoint) **moves to `attic/`** with a one-line manifest entry (original path · why · absorbing doc ·
date). Flat layout; on a basename collision the source dir prefixes the name; still taken → a numeric ordinal `-2`, `-3` (the pack's one collision law, base rule 18).

**The selection is a human gate.** These are the human's authored files in a live project — propose the attic
set with reasons and get an OK before moving. Moving is done with `git mv` (history preserved).

**Sweep the coupling.** After moving, fix any **live current-state pointer** in the KEPT docs that named a
moved file as canonical (e.g. a JOURNAL header "canonical state lives in X") — repoint it, or it becomes a
dead backpointer. Leave pure historical citations in dated entries (they resolve via the manifest).

Done when: superseded files are under `attic/` with a manifest, and no live pointer is dead.

---

## Phase 5 — Architecture, then the test matrix (SPEC A-3 tail, E-14/E-15)

**Pins are names first (E-14):** pin nodes to a named thing (function, marker, selector); the `:line`
is a cache. Wire the drift check (`guardrails/check-pin-drift.sh`) so a stale pin is reported, never
trusted.

**First the architecture.** Seed `ARCHITECTURE.md` from Phase 2's inventory: the surfaces' `file:line`
pins become named nodes (one responsibility, one name each — template: `ARCHITECTURE.template.md`), every
spec fact is assigned an owning node, seams are named. The pins ARE the reconciliation of re-engineered
claims (A-3) — they come from commands run in Phase 2, independent of the old docs' prose. Run a
product-prover pass with the architecture lens before deriving anything from it.

**Then DERIVE `TEST_MATRIX.md` through it**: rows organized node × fact, at least one row per invariant /
transition / cross-section / surface, each pinned to a test **level** (string / DOM / browser / pixel —
extend with `data` for a data pipeline). Every row states BOTH sides — what the fact DOES and what it must
NEVER do (the negative is the regression fence). Visibility/layout facts get level ≥ browser. The
derivation closes with the template's coverage-validation checklist, actually walked. If the host has no
suite yet, all rows are `TODO` — the data/invariant rows become the acceptance criteria for the next
build sprint.

Done when: `ARCHITECTURE.md` exists with every spec fact owned (prover-lensed), and `TEST_MATRIX.md` has
≥ 1 row per spec invariant under its owning node, each with a level, all `TODO` (or better).

---

## Phase 6 — Attach record & incremental from here (SPEC A-7)

1. Record installed skill versions in `.live-spec/` (every pack SKILL.md carries a version line under
   `metadata:` in its frontmatter and the package a root `VERSION` file — SPEC M-7) and seed
   `.live-spec/profile.md` — the HOST's overrides
   only; settings about the human (language, proactivity) belong in their personal profile
   (`~/.claude/live-spec/profile.md`), which this host file overrides per the settings ladder (SPEC E-13).
   Mode/trust set only on the human's word (INV-9).
2. Write the run's JOURNAL entry (what landed · why · provenance · the remote outcome (exists/declined) ·
   any findings held for the human).
3. The host is now on the standard pipeline: every new wish enters at intake and flows
   `spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show`.

**First recommended action after adoption:** run `product-prover` on the whole spec to catch what the
reverse-spec pass missed — UNLESS the spec was prover-proven recently, with no drift since, AND by the
same prover version as the one installed now (the record names the version that ran). A prover that grew
a lens since that record re-arms the full pass: a spec proven under the old lens set has not met the new
lens — that is exactly how a whole class of composition holes once kept a stale green (2026-07-09).
