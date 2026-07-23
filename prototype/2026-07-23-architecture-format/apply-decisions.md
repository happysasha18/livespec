# Row 456 apply — the 18 PARTIAL/ABSENT dispositions

The relocation audit left 12 PARTIAL and 6 ABSENT fragments for a placement decision. Each residual is
classified by what it IS, under the format design's own laws:

- **RULE → spec**: a genuine behavioral rule the spec under-describes moves into the named spec clause in
  this delivery, so the words live once at the spec (INV-279 AC3). It leaves the owns cell.
- **NOTE → arch**: architecture-level wiring — which gate a check rides, which file carries it, a roadmap
  pointer, a sibling relationship — stays in the node section (an owns parenthetical or the notes/pins
  field). It is not a spec rule; it is the map's own fact.
- **DROP → journal**: history, provenance, or a state-of-today status — a dated incident, "row now filled",
  "shipped complete", a past-reason — drops from the doc; the journal already holds when and why.

A RULE→spec and a DROP are named content deltas (word-preservation proof accounts for them). A NOTE→arch
stays in the node content region, so it is preserved verbatim, not a delta.

## PARTIAL (12)

| # | node | anchor | disposition | action |
|---|---|---|---|---|
| 1 | base-rulebook | INV-225 | NOTE→arch | "the sibling of the far-tier report-shape check" — a relationship note; keep as the anchor's parenthetical. |
| 2 | communicator | INV-223 | NOTE→pin | the fixture path `guardrails/check-far-tier.py --window` — a mechanism pointer; move to the pins field. |
| 3 | guardrails-a | INV-202 | DROP | "shipped complete and usable on demand" — a state-of-today status; drop. |
| 4 | guardrails-a | INV-203 | DROP | "it holds the register class the retracted growth-list never could" — a past-reason; drop. |
| 5 | guardrails-a | INV-205 | NOTE→arch | the roadmap pointer "rows 402/403/408/409" — keep as the anchor's parenthetical. |
| 6 | guardrails-a | INV-207 | DROP | "while the spec/base-rulebook/roadmap get the one-time first sweep" — a transitional/migration note; drop. |
| 7 | guardrails-a | INV-209 | NOTE→arch | "composes with the growth law rows 390+392 — the bound governs what is shown, the archive keeps all and stays grepable" — a composition/relationship note; keep as parenthetical. |
| 8 | guardrails-b | INV-213 | RULE→spec | "never a push gate, since a push gate runs long after the cores burn" — the fire-timing exclusion; append to R235.1. |
| 9 | guardrails-b | INV-216 | RULE→spec | "the host's project settings" scope + "strips a trailing glob to its literal ancestor, keeps a spaced path whole" — path-scope+parsing rules; append to R246.7. |
| 10 | guardrails-b | INV-238 | RULE→spec | "an optional personal-overlay JSON a host tunes" — the overlay parity with the scissors scan; append to R232.1. |
| 11 | inbox | INV-232 | RULE→spec | the literal field key `trust.read-grant` — name the field in R253.6 (siblings like `founding.set-version` are named literally in the spec). |
| 12 | product-prover | INV-248 | DROP | "the lens carries the prover's dual-discovery habit" — editorial rationale, no testable behavior; drop. |

## ABSENT (6)

| # | node | anchor | disposition | action |
|---|---|---|---|---|
| 13 | build-pipeline | INV-233 | RULE→spec | "rides the suite `tests/test_node_growth.py`, no push-gate letter, the far-tier check the precedent" — push-status rule; append to R244. The test path `tests/test_node_growth.py` → pins. Siblings (R95.3, R277.20, R285.5, R288.5) carry push-status in the spec, so this one matches them. |
| 14 | build-pipeline | INV-235 | RULE→spec | "no new push-gate letter since no gate reads a reversal cost — the far-tier and node-growth checks the precedent" — push-status rule; append to R214. |
| 15 | guardrails-b | INV-216 | DROP | "deploy permissions left dead a week after their folder was renamed" — dated incident; drop. |
| 16 | guardrails-b | INV-216 | RULE→spec | "stands down by name where the settings cannot be read and reds a present-but-unreadable one, never a false pass" — a stand-down rule; append to R246.7 (with #9). |
| 17 | guardrails-b | INV-218 | NOTE→pin | the gate mechanism `guardrails/check-index-prose.py` (gate x) → pins; drop the behavioral prose (an instance of the nonempty-input class INV-218; if the index-prose behavior wants its own invariant, that is a separate row the prover can surface). |
| 18 | guardrails-b | INV-243 | DROP | "a named future row now filled" — provenance; drop. |

## The spec rule-moves this produces (6 clauses, all words relocated from ARCHITECTURE owns cells)

- **R235.1 [INV-213]** — add the fire-timing exclusion: the notice fires at a stopping point, never the push
  gate, which runs long after the cores burn.
- **R246.7 [INV-216]** — add the project-settings scope, the glob/spaced-path parsing, and the
  unreadable-settings stand-down (reds a present-but-unreadable one, never a false pass).
- **R232.1 [INV-238]** — add the optional personal-overlay JSON a host tunes, as the scissors scan carries one.
- **R253.6 [INV-232]** — name the read grant's profile field `trust.read-grant`.
- **R244 [INV-233]** — add the node-growth check's push-status: rides the suite, no push-gate letter.
- **R214 [INV-235]** — add this check's push-status: no push-gate letter, no gate reading a reversal cost.

Each moved sentence already existed as words in an ARCHITECTURE owns cell, so the system's total content is
preserved: the content-preservation proof counts each as a named delta whose words survive at the spec.
