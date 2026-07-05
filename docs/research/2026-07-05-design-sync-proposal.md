# Design-sync as an optional machine — proposal (row 83, 2026-07-05 night)

Alexander's ask: "включать ли дизайн синк — по мере надобности, как плагин или как решим" (2026-07-05,
the 1.0 directive). This is the thought-through answer; landing anything from it is its own row.

## What design-sync IS (verified against the tool itself, not from memory)

A capability of the Claude Code environment (`DesignSync` tool + `/design-sync` skill): it keeps a LOCAL
component library in sync with a **design-system project on claude.ai/design** — the human's team can
then browse rendered component cards (buttons, cards, layouts) in a gallery pane. The tool's own
discipline is remarkably live-spec-shaped: read first (`list_projects`/`list_files`), then a **finalized
plan** naming exactly which paths will be written/deleted (the human sees and approves the list), only
then writes — incremental, never a wholesale replace.

## Where it fits the pack — and where it does not

- **The pack itself: nowhere.** live-spec ships text (skills, templates, docs). It has no visual
  components; the flagship repo never syncs anything. Design-sync must not become a core pipeline step.
- **A HOST with visual surfaces: two natural seams.**
  1. **The show step (communicator).** Where today the rule says "open the real render in a new browser
     window", a host with a component library gains an alternative channel: sync the touched components
     to the team's design project, and the human reviews cards there. Same rule (show the REAL artifact),
     different window.
  2. **The verify step (build-pipeline step 8).** A synced design project is a rendered, inspectable
     artifact of the landing — for visual work it can serve as the "seen with your own eyes" evidence,
     with the snapshot machine ([E-7], still [target]) later diffing what changed.

## The shape: an OPTIONAL MACHINE, switched in the host profile

The pack already has exactly the right slot: "The machines that hold the bounds" — guardrails, snapshot,
surface registry — machines a host INSTANTIATES. Design-sync joins as the first *optional* one:

- A host profile line switches it: `design-sync: off` (package default) / `on + project id`.
- When on, the communicator show-rule and the verify step name the design project as a legal channel.
- **The human gate is non-negotiable:** a sync PUBLISHES outside the machine (to claude.ai, visible to
  the org). Per the irreversibility criterion Alexander set tonight (publishing to an audience = stop
  and ask), the first sync of a session — and any sync touching components the plan didn't name — asks
  first. The tool's own finalize_plan flow makes this natural.
- Kinship with row 86 (the pack understands WHAT it builds): a "product with visual components" kind is
  exactly what switches this machine on. The two should land as one family when row 86 opens.

## Recommendation

Do NOT fold design-sync into 1.0's core. Spec it at 1.0 as a NAMED optional machine with the [target]
tag and one owning queue row (the same honest pattern as snapshot/registry): the spec says "an optional
design-sync machine exists for hosts with visual components, switched in the host profile, human-gated
because it publishes" — and the wiring (skill lines, host-profile vocabulary, first real run on
tlvphoto or track-coach widgets) lands post-1.0 under its row, ideally together with row 86.

Cost of this shape: one spec paragraph + one index row now; zero risk to the 1.0 push; the first real
host that needs it gets the full landing.
