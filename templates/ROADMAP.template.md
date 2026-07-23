# [Project Name] — Roadmap

The wish queue: the live record of what is asked of the product and where each ask stands. A wish
is a request for a change the product does not yet carry, and a wish lands when the delivery that
completes it ships. Intake is continuous, a wish entering the queue the moment it is spoken;
execution is serial, the current landing finishing before the next starts.

The roadmap is a member of the format family. Its shared rules — the closed-vocabulary glossary,
the keyword form, the no-capitals rule, the trailing code anchor, the no-history law, the
comprehension gate — live once in `docs/spec-format.md` and hold here unchanged. Its own rules —
the row shape, the status and class vocabularies, the live-body law, the row lint — are defined in
full in `docs/roadmap-format.md`; read that page before editing this file, since this template only
teaches the shape and does not restate the definition. The keywords *when*, *if*, *then*, and
*shall*, where a row's acceptance cell uses them, are set in lowercase italics. A bracket code
trailing a line, such as `[INV-277]`, points to the rule's home in `PRODUCT_SPEC.md`; a reader may
ignore it, and a maintainer follows it.

## Glossary

[Domain nouns the queue's own rows use, each with a one-sentence definition. A word of ordinary
English needs no entry.]

## The body

The table below is the body: the live queue, one row per open wish, the rows standing in ascending
id order. A rotated-manifest block sits above the body, one line per monthly archive file naming
the rows that moved and the file that received them; a script maintains this block and a gate
cross-checks it against the archive.

<!-- rotated-manifest -->
Rotated closed rows (the archive keeps every moved row, grepable by number; the body below holds
only the live queue):
- rows [ids] → docs/queue-archive/rotated-ROADMAP-[YYYY-MM].md
<!-- /rotated-manifest -->

| # | Wish (plain words) | Class | Status | Decision / acceptance |
|---|---|---|---|---|
| 1 | [Wish in plain producer/user language]. Asked by [name], [date]. door: [feature / bug / refactor / docs-only / skip] · kind: [product / infra / skill / prose] · footprint: [presentation-only / single-module / cross-cutting] · map: [architecture node] · entry: [entry condition, where one applies] | small | *queued* [date] | [Done-when criteria and non-goals, code anchors trailing at the line ends] |
| 2 | [Second example wish, its delivery split into two legs]. Asked by [name], [date]. door: feature · kind: product · footprint: single-module · map: [architecture node] · priority: quick win | surface | *in-work* [date] | [Leg one: done — ...; leg two: open — ...] |

Both rows above are invented placeholders, shown to teach the shape; a new roadmap starts with row
1 held open for the first real wish.

## The wish cell

The wish cell carries three things: the ask, in plain producer or user language; its provenance —
whose word asked for the wish, and the date; and the intake notes — the wish's door (feature · bug
· refactor · docs-only · skip), its kind (product · infra · skill · prose), its footprint
(presentation-only · single-module · cross-cutting), its placement on the architecture map, and an
entry condition where the wish declared one. A priority mark rides the intake notes when the
wish's priority is other than normal: **critical** (the shipped product is broken for its user, and
the row lands before everything) or **quick win** (low effort, immediate value, free to bubble up
between landings with the jump named in the row). Ambiguous size or priority is asked at intake,
never guessed.

## The class cell

The class cell carries one word of the closed size vocabulary, one vocabulary shared with the
spec: **bug** (something shipped is wrong), **small** (one landing, no new surface), **surface** (a
new stateful user-facing surface, entering the pipeline in full), or **large** (a wish that
decomposes into several landings).

## The status cell

The status cell carries one word of the closed status vocabulary, each set in lowercase italics and
carrying its date:

- *queued* — the wish is accepted and waiting its turn.
- *in-work* — the wish is claimed by a session.
- *deferred* — the wish is parked on a named revisit trigger, the trigger written in the status
  cell.
- *far* — the wish is parked with no near trigger.

A row whose wish carries more than one leg stays *in-work* while any leg remains open, the open leg
named in the acceptance cell; the row reaches a terminal exit only when every leg is closed — a row
closes only whole. [INV-26]

## The live-body law

The body holds live rows only. A row reaching a terminal exit — *landed*, *declined*, or
*superseded* — moves verbatim, its delivery report riding with it, from the body to the month's
file in the archive in the same commit that closes it. The word *landed* names that transition a
row makes; a body row never carries it as a status. An archive file gathers one calendar month's
moved rows, and the rotated-manifest block above the body grows one line per archive file. A
*deferred* or a *far* row stays live in the body, its revisit trigger re-read at the next milestone
review and whenever a session takes its next wish from the queue.

Declining a row that absorbed other wishes lists the absorbed rows: decline each listed row by name
or return it to the queue as its own row — a superseded wish never dies by pointer. [T-8]

## The acceptance cell

The acceptance cell carries the done-when criteria and the non-goals, with code anchors trailing at
the line ends. The spec's Context blocks and User Stories stand down from the row: the spec owns
them, and the row points at the spec by anchor, the spec staying their one home.
