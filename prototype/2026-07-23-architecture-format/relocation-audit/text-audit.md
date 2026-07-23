# text-audit — owns-field relocation audit

owns codes: INV-266, INV-267, INV-268. The prose is one parenthetical on INV-268 (split into its distinct clauses below) plus one trailing roster wiring clause.

| fragment (quoted; … past 40 words) | anchor | class | evidence |
|---|---|---|---|
| "the comprehension gate: the mechanical-lint layer runs first and free" | INV-268 (content of INV-266) | DUPLICATE | R281.1: "*when* a section changes, the system *shall* run the mechanical lints … before any reader, on every push. [INV-266]"; glossary line 135: "**mechanical lint** — a free script check the comprehension gate runs before any reader …". |
| "then a cold-reader panel reads each changed section until two consecutive reads return zero blocking findings" | INV-268 (content of INV-267) | DUPLICATE | R281.5: "The system *shall* pass a changed section only *when* two consecutive reads return zero blocking findings. [INV-267]" (and R281.3, the cold-reader panel with zero project context). |
| "and a reader-named source hole opens a queue row" | INV-268 | DUPLICATE | R281.7: "*when* a cold reader's finding names a source hole, the system *shall* open a queue row for the hole and *shall* record the criterion it sits under. [INV-268]" |
| "text-audit is the skill that runs this loop" | INV-268 | KEEP | Ownership note — states why the anchor sits at this node (which skill runs the comprehension-gate loop); an architecture fact, not a spec rule. |
| "the working-skill roster's text-audit member (the roster entity's home stays base-rulebook; this node bodies the skill without owning that anchor)" | roster (owned by base-rulebook) | KEEP | Wiring/ownership note — it explicitly disclaims owning the roster anchor and points at its true home (base-rulebook); an architecture-only fact about node/anchor placement. |

## Pins carrying provenance
None. (Pins are skill file paths only; no date, session number, or landed-row note. The "added row 458" note sits in the responsibility line, not the pins field.)
