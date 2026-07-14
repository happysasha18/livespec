# Prover record — the stranger door (INV-146 / INV-147), 2026-07-14

**Wish:** ROADMAP row 261 — a stranger with no push rights and no per-repo grant submits a wish to a
live-spec repo through a GitHub Issue or Discussion, swept the way inbox/ is swept, kept parallel-safe;
plus a monitor that watches for new stranger-wishes. Reopened on the owner's word 2026-07-14 (his flip to
accept-Issues, named in the row's own "his flip reopens the build" note).

**Pass:** FULL adversarial prove in a fresh independent context (INV-46 — this is a method edit, two new
invariants), opening hypothesis "goal missed, there is a hole". product-prover method (composition,
atomicity, liveness, edge-completeness).

**Verdict of the first draft:** GOAL MISSED — nine findings. The load-bearing safety claim (two sessions
never route one Issue twice) did not hold, and the door was scoped on the wrong axis. Every finding folded
before the matrix step by a redesign; the folded spec is what stands.

| # | severity | kind | finding | fold |
|---|---|---|---|---|
| F1 | must-fix | defect | the claim race was not closed — GitHub label-add is not compare-and-swap and carries no git ancestry, so the borrowed pen tie-break [INV-117] was unsound; two sessions could both route one Issue | **redesign:** the monitor is the single bridge — it converts each Issue into one new inbox/ file, and routing then rides the inbox's git-atomic harvest, already proven race-safe [T-10, INV-11]. No distributed claim on GitHub at all |
| F2 | must-fix | defect | door scoped "for a public repo" — a read-only collaborator on a PRIVATE repo is a stranger (no push, no grant) with no door, wish lost against INV-1 | re-scoped INV-146 to the property "a contributor with no push and no grant who can open an Issue/Discussion", any repo |
| F3 | should-clarify | defect | reopen/edit/comment-after-swept content was durably-recorded but operationally invisible | new stranger activity on a swept Issue drops the surfaced label and re-surfaces it [INV-138] |
| F4 | should-clarify | defect | "wish Issues" set undefined; bare Issues / spam had no handling | the monitor surfaces ALL open un-surfaced items as inbox files; the inbox sweep applies the wish-vs-not verdict; a no-wish item is closed with a recorded note (a dismiss) |
| F5 | should-clarify | defect | INV-147 "surfaces the wishes it finds" smuggled the is-it-a-wish verdict the monitor is forbidden to make [T-20] | monitor surfaces ITEMS and holds no verdict; the verdict stays the inbox sweep's call |
| F6 | should-clarify | defect | crash between claim and route left a stale mark of undefined meaning | dissolved by the redesign — the monitor surfaces at most once by checking label + existing inbox file, so a crash still surfaces exactly once; no claim marks exist |
| F7 | should-clarify | defect | first-act session sweep needs GitHub reach but had no honest-failure path when unreachable | dissolved — sessions sweep the LOCAL inbox as always; only the monitor needs GitHub reach, and it fails honestly [INV-67] |
| F8 | should-clarify | recommendation | liveness rested on an optional monitor | the schedule is REQUIRED where the door is open; the liveness bound is stated (seen as often as the monitor runs) |
| F9 | nit | recommendation | "a template that requires a source" overclaims for Discussions (cannot enforce) | template REQUESTS the source; the wordless-item ask is the real guarantee [E-11] |

**Where the design held (first draft, confirmed):** the grant/no-grant partition with INV-112 is clean and
total; INV-10 write-ownership is preserved (the stranger has no write path); the wordless-item backstop
[E-11] is sound and load-bearing.

**Design review:** STANDS DOWN by INV-141 — live-spec is a skill pack with no acted-on UI elements to
group. Same stand-down as the 2026-07-14 cleanup-movement record.

**Post-fold state:** the redesign reuses the proven inbox machinery (the monitor is a bridge Issue → inbox
file); the two must-fix holes are closed at the root, not patched.

## Confirm pass on the folded design (independent fresh context, INV-46)

Verdict of the fold: **GOAL MISSED — narrowly.** F1 (session race) and F2 (private-repo scope) confirmed
CLOSED at the root. But the fold of F3 was incomplete and the code diverged from the spec. Second-round
folds, all landed:

| finding | fold |
|---|---|
| F3 re-surface had **no actor** — spec said the label "is dropped" passively; the code never dropped it, never populated new-activity, so a reopened/edited swept Issue was never re-surfaced (the invisible-content failure persisted) | the monitor is now the named actor: it records the Issue's update generation at surfacing time and re-surfaces an Issue whose current generation is newer. No third-party label-drop; the comparison is the mechanism (spec + code + a new unit test) |
| the monitor deposited an **UNCOMMITTED** file, breaking the committed-file law [E-11] the git-atomic harvest leans on | `_deposit` now commits the file touching inbox/ only with the source in the message, and returns done only when the commit AND the generation record both held |
| **silent deposit failure** — `check=False` on the label/comment swallowed failures, contradicting INV-67 | a deposit that does not complete is logged and left for the next run, never counted surfaced (spec + code + a new unit test) |
| **Discussions claimed, unimplemented** — the door invited a channel the monitor did not watch | scoped to Issues this stage; the Discussion template is withdrawn so no stranger is invited to an unwatched door; Discussions ride the same mechanism as the stated next stage (GraphQL path, verified against a live discussion) |
| **stale lock** wedged the monitor forever after a hard kill, defeating required liveness | `single_instance` steals a lock older than an age bound |
| **cross-machine double-surface** was unacknowledged | stated as a bound in INV-147: the single-instance guard holds within one host; two hosts' monitors on one repo can duplicate a wish, a duplicate the maintainers drop rather than a wish lost [INV-1]; the cross-host coordinator is a later stage |

**Verified after the second fold:** suite 692 green; the monitor runs clean against the live public repo
(0 items, exit 0, no stray commit, lock released); the pure core (surfacing decision, honest failure,
half-done deposit) is unit-tested. The one residual is the acknowledged cross-host duplicate — a bound, not
a hole (INV-1 holds).

## Third fold — Discussions added on the owner's word (2026-07-14, "все сразу")

The owner asked for both channels at once, so the Issues-only scope was widened back to Issues + Discussions
in the same movement. The monitor now bridges Discussions over the GraphQL path (`gh api graphql`:
`discussions(states:OPEN)` for the fetch, `addDiscussionComment` for the generation record), keyed by the
same marker comment so no label is needed. The Discussion template is restored. Spec, index, matrix, README,
and the architecture pin all name both channels.

**Verified:** suite 692 green; the Discussion READ path verified by deed on the live repo (the GraphQL query
is valid, returns cleanly with zero open discussions, the item shape carries the node id the comment mutation
needs). The live Discussion WRITE round-trip — a real discussion created, bridged to a committed inbox file,
its marker comment posted, a second run proven idempotent — is a **field beat that waits on a real run and is
not self-certified [INV-94]**, the same posture INV-112's one-real-remote-deposit beat holds. The auto-mode
classifier declined the agent's own attempt to create a test discussion under the owner's identity, which is
the right boundary; the beat waits for the owner's hand or a real stranger's Discussion.
