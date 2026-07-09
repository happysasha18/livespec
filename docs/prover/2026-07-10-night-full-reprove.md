# Prover record — FULL night re-prove of the whole product spec (2026-07-10)

**Prover skill version:** product-prover **v0.1.15** (the version-aware re-prove law: this pass ran under
the six-check architecture lens and the full Phase-3e stress family, including the unwritten-seams,
entry-symmetry, persistence-and-versions, and surface-authority lenses). base skill referenced at v0.1.26.

**Mode:** FULL (whole-spec re-check). **Trigger:** a standing full re-prove over PRODUCT_SPEC.md as it
stands tonight, with the recent additions under the hardest look — the runtime/placement view mandates
(INV-74/75), worker liveness (INV-76), the test lessons (INV-77..80), the pre-ask scan (INV-81), and the
push law (INV-82) — asking whether they compose cleanly with the older sections or whether any two clauses
now collide.

**Documents proven:** PRODUCT_SPEC.md (v0.16.13) with ARCHITECTURE.md (v0.3.0) in view for fact-ownership.

**How this pass was run:** the prover read the whole spec end to end (1697 lines) and the whole
architecture doc, extracted the model, then walked every recent invariant against the sections it composes
with — push against the gates and the human's authority, worker liveness against the concurrent-edit fence,
the test lessons against the coverage machinery, and the two architecture views against the flow inventory.

## Opening assessment

The spec is in strong shape and the recent additions are, in the main, well-composed: the runtime and
placement views (INV-74/75) land cleanly against the flow inventory and the architecture doc already
carries both in full; the test lessons (INV-77..80) sit correctly under the test-author node; the pre-ask
scan (INV-81) layers over INV-4/INV-34/INV-59/INV-60 without conflict. Notably, the six queued design
findings from the 2026-07-09 pass (F5–F10 — deferred-trigger evaluation, park-resume re-fence, bug-vs-milestone
preemption, milestone-quiesce state, lane-claim tie-breaker, tight-batch recovery) have all since been
folded into the live text (M-1's deferred re-scan, T-9 criterion 6, lines 471/473, INV-2's total order,
T-19's bisect-and-reapply). That is real hardening.

The one section that does not compose cleanly is the new push law (INV-82). Read literally, it collides
with two older, load-bearing rules: the human's ownership of push gates (ACT-1 / INV-9 / the INV-70 grant)
and the never-push-while-a-peer-is-live fence (INV-11). Both are worth fixing before the docs wave rides on
the spec, because a push to a remote is exactly the irreversible/outward act those older rules reserve.
Worker liveness (INV-76) has two narrower design seams. Overall confidence: **needs one more iteration on
the push law**, sound elsewhere.

## Findings

Each finding gives its headline, the source quote with line, the operational consequence, and a concrete
action. The Disposition column is left for the senior to fill (folded / rejected + why).

| # | Finding | Lines | Severity | Disposition |
|---|---|---|---|---|
| F1 | Push-by-rule collides with the human's push grant | 402, 698, 1617, 1657 | must-fix · internal-conflict (consistency) | FOLDED 2026-07-10 night (spec v0.16.14): INV-82 now runs inside the standing push grant [INV-70, INV-9]; an ungranted remoted host keeps work local and asks the grant question once at its first push moment; body + index row updated |
| F2 | Push-by-rule vs never-push-while-a-peer-is-live | 698, 1485, 1617 | should-clarify · direct-contradiction (contradiction) | FOLDED 2026-07-10 night (spec v0.16.14): INV-82 stands down while a peer session is known live; push coordination returns to the human [INV-11]; body + index row updated |
| F3 | The two liveness checks can declare a live-but-busy worker dead | 662, 1687 | should-clarify · stuck-state (liveness) | QUEUE ROW (night batch): conservative-on-ambiguity verdict — in-progress long operation in the checkpoint means ALIVE; windows read from the brief |
| F4 | "Dead" is not "done" — a crashed worker looks like a finished one | 662, 1687 | should-clarify · partial-success-risk (atomicity) | QUEUE ROW (night batch): dead = liveness only; completeness read from the worker's checkpoint finished-marker, else the verify ladder [INV-46] |
| F5 | A real-device row's representation is unstated between INV-77 and INV-80/E-15 | 576, 582, 644, 1688, 1691 | should-clarify · boundary-issue (composition) | QUEUE ROW (night batch): human-walk marker in matrix template + INV-77; the suite lists such rows as owed-to-human, the coverage gate counts them covered at the real-device level |
| F6 | "Full gate green at HEAD" vs the reach-scoped push gate | 1365, 1447, 1622, 1627 | worth-considering · internal-conflict (consistency) | FOLDED 2026-07-10 night (spec v0.16.14): line 1365 rewords to "the batch's reach-scoped gate [INV-45] green at HEAD" |

---

**F1 — Push-by-rule makes the push grant automatic, which contradicts the rule that the grant is the human's to give.**

> "work that is same or better and has passed every gate the diff reaches is PUSHED, by rule, never parked locally… Only a host with NO remote gets one question" — Section: Rhythm / Push and CI gates [INV-82]

> "where the human has granted it, the agent ships to prod on its own certification… the grant stays the human's to give or withdraw [INV-9]" — Throwing a wish [INV-70]

INV-82 grants itself license to auto-push from the mere presence of a remote: a host with a configured
remote is pushed to "by rule," and the stay-local choice is offered only to a host that has NO remote.
INV-70 and ACT-1 hold the opposite — autonomous push runs only "where the human has granted it," and push
is one of the gates the human owns. On any adopted host that already has a GitHub/GitLab remote but never
granted autonomous push, an accepted landing would be pushed to that public remote unbidden — an
irreversible outward act the human never authorized, discoverable only after the fact in the remote's
history.

Add the grant as an explicit precondition to INV-82: "by rule" fires only where the host profile records
the INV-70/INV-9 autonomous-push grant; absent the grant, an accepted landing stays local and the push
waits for the human's word, exactly as a named milestone gate does. State that the first-push question a
remoted-but-ungranted host gets is the grant question, not only the create-or-stay-local question.

`must-fix · internal-conflict (consistency)`

---

**F2 — Push-by-rule does not carve out the concurrent-session fence, so the two rules openly conflict when a peer session is live.**

> "the agent never pushes while another session is known to be live in the repo; push coordination belongs to the human" — Package repo [INV-11]

INV-82 mandates that accepted work is "pushed to the host's remote by rule, never parked locally." INV-11
forbids any push while another session is known live in the repo and hands push coordination to the human.
On the exact scenario the pack is built to survive — two sessions sharing one repo (the live-spec
parallel-access case) — an agent implementing INV-82 literally would push during a peer's live session,
violating INV-11 and racing the peer's unpushed work. The two rules can both hold only if INV-82 is
understood to yield to INV-11, but INV-82's text states no such deferral.

Add one clause to INV-82: the by-rule push is suppressed while a peer session is known live in the repo;
in that state push coordination returns to the human per INV-11, and the accepted work waits local until
the repo is single-session. Cross-link INV-11 from INV-82's line.

`should-clarify · direct-contradiction (contradiction)`

---

**F3 — The two liveness checks can both fail for a worker that is alive but busy, re-opening the two-writer race INV-76 exists to close.**

> "watch the write-set's file times over a short window (~30 s [default]…anything changing means a live writer), and send one message to the recorded id (a live worker answers; allow ~2 min [default]). Alive ⇒ reconnect…; quiet on both ⇒ declare it dead" — Rhythm [INV-76]

Both checks are false-negative-prone for a live worker mid-long-operation. A worker running a five-minute
render or a large suite writes no files in the write-set for that stretch and, if it is blocked inside a
tool call, does not answer the message within two minutes. Both checks report "quiet," the resume declares
it dead, spawns a second worker onto the same files — the precise two-writer race whose real incident
(2026-07-09) motivated the invariant. The timeouts trade a false-dead risk for a wait bound, and the
default bounds are short enough that a normal long operation trips them.

Make the verdict conservative on ambiguity: state that a worker whose checkpoint shows an in-progress
long operation (a render, a suite run) is treated as ALIVE until its own reply or a checkpoint line marks
it finished, regardless of the file-time and message windows; or lengthen the windows to bound the longest
briefed operation and say the bound is read from the brief. The safe default when both checks are
inconclusive must be alive-not-dead, since the cost of a false-dead is the race and the cost of a
false-alive is only a wait.

`should-clarify · stuck-state (liveness)`

---

**F4 — A dead verdict establishes that the worker's files are safe to touch, not that its output is complete; a crashed-mid-work worker is indistinguishable from a finished one.**

> "quiet on both ⇒ declare it dead in one written line, then proceed. Until that verdict, the worker's output is never framed as finished." — Rhythm [INV-76]

The two checks answer "is a writer still active," not "did the work finish." A worker that crashed
mid-write and a worker that finished cleanly present identically to the resume: static file times, no
reply. INV-76 says the output is not framed finished "until that verdict," which reads as implying the
dead verdict clears it to be treated as finished — but a crashed worker's output is partial. The resume
could then integrate half-written output as complete.

State that the dead verdict is a liveness verdict only, and that completeness is a separate check the
resume runs on the dead worker's output before treating it as done: read the worker's own checkpoint file
(the id already points at it, per INV-76) for a finished-marker, and route the output through the
adversarial verify ladder [INV-46] when the checkpoint does not confirm completion. "Dead" ⇒ safe to
touch the files; "done" ⇒ the checkpoint or verify says so.

`should-clarify · partial-success-risk (atomicity)`

---

**F5 — A real-device walk row is a permanently non-green matrix row; how the coverage gate distinguishes it from a blocking red or an INV-80-forbidden silent skip is unstated.**

> "a real-device walk row: a matrix row the suite can never turn green, owed to the human's own hands before ship" — From the spec to the tests [INV-77]

> "a skip path executes even when never taken…an unrunnable skip is red instead of a silent pass" — From the spec to the tests [INV-80]

INV-77 mandates matrix rows the suite can never green. INV-80 mandates that a skip that cannot run turns
red, and the push gate blocks on red. E-15's coverage validation requires every fact to sit at its right
level with no unchecked box. A real-device row therefore needs a defined representation that is neither a
blocking red (which would wedge every push behind an unrunnable row) nor a silent skip (which INV-80
forbids). Nothing states how the coverage gate and the suite recognize a real-device row and account it as
covered-by-human-walk rather than failing.

State the representation once, in the matrix template's coverage validation and in INV-77: a real-device
walk row carries an explicit human-walk marker, the coverage gate counts it as covered at the real-device
level, and the suite neither greens nor reds it but lists it as an owed-to-human walk in its output — the
honest boundary INV-77 already asks the suite to name.

`should-clarify · boundary-issue (composition)`

---

**F6 — The tight rung says a push needs "the full gate green at HEAD," while the push gate elsewhere is reach-scoped; a reader could take line 1365 to override the reach map.**

> "Even so, a push still requires the full gate green at HEAD [M-6]." — When money or time run short / tight [T-19]

> "'full rigor' (INV-40) = every check the diff can reach, green" — The machines that hold the bounds [INV-45]

INV-40/INV-45 define the push gate as reach-scoped: full rigor is every check the diff can reach, and a
prose-only push legitimately stands the behavioural suite down. The tight-rung recovery line says a push
"requires the full gate green at HEAD," which — read on its own — says the entire suite regardless of
reach. The intent is almost certainly "the batch's accumulated reach, green at the batched HEAD," but the
wording invites a reader to run the full suite on a prose-only tight-rung push, contradicting the reach map.

Reword line 1365 to "the reach-scoped gate green at HEAD per INV-45" (or "every check the batched diff can
reach, green at HEAD"), so the tight rung inherits the reach map rather than appearing to override it.

`worth-considering · internal-conflict (consistency)`

## What was probed hardest and found sound

- **Runtime and placement views (INV-74/75)** against the flow inventory: the architecture doc's runtime
  table walks all nine promised flows with a where-it-fails and an if-it-fails cell each (INV-74's fallback
  duty discharged), and the placement table names every node's tier, its load-bearing technology, and the
  secrets home (INV-75). Both bind forward with INV-15; no retroactive-sweep trap.
- **Test lessons (INV-77..80)** under the test-author node: the geometry rule (relative, two viewports, N
  steps), the engine-fixtures rule, and the plumbing-must-not-lie legs compose with the pinned skip-set and
  the log-tail-not-exit-code gate; only INV-77's matrix representation (F5) is underspecified.
- **The pre-ask scan (INV-81)** against INV-4/INV-34/INV-59/INV-60: the self-decide-first gate and the
  phrase-by-phrase read layer cleanly over the older ask rules; the ordering against INV-59's records
  search is benign (search then self-decide-gate both precede the ask).
- **The 2026-07-09 queued design findings (F5–F10)** re-checked as folded: M-1 now re-scans deferred
  triggers; T-9 criterion 6 and INV-39 make park-resume re-fence and re-prove; lines 471/473 define the
  held-for-milestone state and the bug-vs-running-milestone order; INV-2 defines the lane-claim total
  order; T-19 defines the tight-batch bisect-and-reapply. All resolved in the live text.
- **Anchor ownership and the formal index**: every recent anchor (INV-74..82, E-27..29, T-20) resolves to
  a home section and to an owning node in ARCHITECTURE.md; no orphan, no double-owner spotted by read.

## Coverage note

CRUD and authorization tables are N/A for this product: live-spec is a single-human skill pack with no
multi-user persistent entity and no role model — its "entities" are documents the assigned session alone
writes, governed by INV-10/INV-11 rather than a permission matrix. The invariant coverage that matters
here is the anchor→node ownership map, which the architecture doc and `tests/test_traceability.py` already
carry.

## Gate

Six findings, no regression in the prose itself. F1 is the one that should block the docs wave riding on
the spec: the push law as written authorizes an outward, effectively-irreversible act (a push to a public
remote) without the grant ACT-1/INV-9/INV-70 reserve to the human, and it contradicts INV-11 on the
concurrent-session case (F2). F3–F5 are worker-liveness and test-representation seams worth closing but
bounded in blast radius. F6 is a wording nit. Recommend folding F1 and F2 (both are a sentence-level
clause added to INV-82 with cross-links) before the wave; F3–F6 can ride as queue rows if the senior
prefers, since none is a prose regression.
