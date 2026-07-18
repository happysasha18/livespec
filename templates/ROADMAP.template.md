# [Project Name] — Roadmap

The wish queue. Intake is continuous — a wish lands here the moment it is spoken. Execution is serial:
the current landing finishes before the next starts. Every row names its size, its priority when not
normal, and its DOOR — feature · bug · refactor · docs-only · skip — said at intake, before any code
(SPEC T-12, INV-16). It also names its WORK-KIND — product · infra · skill · prose — what the wish
builds; the kind scales the form each pipeline step takes, and a stood-down step is named in the
landing report, never silently skipped (SPEC T-16, INV-22). It also names its FOOTPRINT —
presentation-only · single-module · cross-cutting — the three-source impact read taken at intake
(the spec says what behaviour changes, the architecture which module owns it, the code what is
touched); the footprint is written in the row's `footprint:` note beside `door:`, `kind:`, and
`map:`, and every landed feature-or-refactor row carries it — a suite check reddens one that omits
it (SPEC INV-128, INV-134).

| # | Wish (plain words) | Class | Status | Decision / acceptance |
|---|---|---|---|---|
| 1 | [Wish in plain producer/user language] | bug / small / surface / large | queued / in-work / landed / waiting | [Who decides, what they need to see, or what was decided] |
| 2 | | | | |

**Class = size, plus a priority mark when it isn't normal.** Size speaks the spec's four words — **bug**
(something shipped is wrong) · **small** (one landing, no new surface) · **surface** (a new stateful
user-facing surface — enters the pipeline in full) · **large** (decomposes into several landings). Priority
is normal unless marked: **· critical** (the shipped product is broken for its user — lands before
everything) or **· quick win** (low effort, immediate value — may bubble up between landings, the jump
marked in the row). Ambiguous size or priority is asked at intake, never guessed.

**Status values:** `queued` (ready to enter the pipeline) · `in-work` (active) · `waiting` (blocked on a
person or event) · `far` (kept in the queue with no revisit trigger and no plan to run — a thought kept
because discarding it would lose it; stood down by name in the what's-left report and shown on request,
distinct from `deferred` whose trigger the queue-take re-scans every time, SPEC INV-222) · `landed`
(acceptance met, committed) · `declined` / `deferred` / `superseded` (closed
without landing; the row stays). Declining a wish that other rows were superseded INTO lists those rows:
each is declined by name or returned to the queue — a superseded wish never dies by pointer (SPEC T-8). A row carrying several user stories enumerates per-story acceptance in its Decision/acceptance cell and cannot close with an unmet leg (SPEC INV-26) — though the norm is one wish = one story, split at intake (SPEC T-17).
