# GAPS — source holes found during the rewrite

These are places where the source states a behaviour but leaves a measure, a default, a judge, or a definition unanswered. Each became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. Neither of these blocks the rewrite; each is a question the source owes a test author who has to pin the boundary.

## New holes

### G1 — the geometry assertion names no tolerance and no step count
**Where:** Requirement 12, criterion 1. Source: "A geometry fact is asserted relative, wide, and long", `PRODUCT_SPEC.md` line 696, `[INV-78]`.
**Hole:** The law asserts that the distance between an element's center and the viewport's center stays within a bound over a run of consecutive interaction steps — the source writes it as `|center(element) − center(viewport)| ≤ ε ... after N consecutive steps`. The "two or more viewport sizes" half is concrete, but the tolerance (the ε bound) and the step count (N) are named as symbols with no value, no default, and no statement of who sets them. Unlike the quality budgets, which the spec explicitly hands to the human's word at the first budget landing, this assertion names no owner for its two numbers.
**What it blocks:** A test author writing the assertion needs a concrete tolerance to compare against and a concrete step count to iterate; the pass-or-fail boundary of a geometry row cannot be pinned while both stay unstated. The shape of the assertion (relative, multi-size, cumulative) is complete; its two thresholds are not.

### G2 — the launch sweep's young-versus-old age boundary is unstated
**Where:** Requirement 17, criterion 2. Source: the browser test harness's launch sweep, `PRODUCT_SPEC.md` line 706, `[INV-157]`, and the `[INV-162]` index row.
**Hole:** On launch the harness sweeps a stale ownerless profile directory a killed prior run left "before it ever recorded an owner", while "a young ownerless dir is left alone, since it may be a live sibling mid-launch". The `[INV-162]` row states the test as "an age well past any live-use window". The behaviour turns on an age boundary between young and old, but the source names neither the boundary value, its owner (the pack, the host, a config line), nor a default, and the "live-use window" it is measured past is itself unquantified.
**What it blocks:** The sweep either reaps an ownerless directory or leaves it, and which it does depends entirely on this age boundary. A test author cannot pin the boundary case — a directory just old enough to reap versus just young enough to spare — while the age and its owner stay unstated, so the sweep's reaping behaviour on an ownerless directory has no pinnable firing point.

### G3 — the judge of carries-the-argument versus decoration is unstated
**Where:** Requirement 46, criterion 3. Source: "A comparison or a diagram joins only when it carries the argument; it never rides along as decoration.", `PRODUCT_SPEC.md` line 881, `[T-16]`.
**Hole:** The law states the criterion — a comparison or a diagram earns its place only when it carries the argument — but names no one who applies it. The surrounding publish walk names the publish skill as the owner of the per-kind checklist and names the register judge elsewhere in the spec for a different call (the enumerable-facts meaning call), but neither this sentence nor its neighbors assign a judge to this criterion.
**What it blocks:** A reviewer or a test author cannot pin who rules on a given comparison or diagram — the author drafting the publication, the publish walk, or the register judge — while the source leaves the call unmeasured.

## Note on scope

These three are the genuinely new holes this stretch opens. Several other numbers in the four subsections are host-settable or defaulted *by design* and are not holes, because the source states their default or names the human as their owner: the resume file's line cap (100 lines), the full-audit cadence (every ten landings, a host-settable default), the worker-liveness windows (a short file-time window, a heartbeat interval, a probe wait), the process-bookkeeping short-form record (three lines), and the quality-budget numbers (explicitly the host's taste, set on the human's word at the first budget landing). Each of those names both a value or an owner and, where relevant, the human's power to change it, which is a complete answer rather than a hole. The harness's per-command deadline is left "a real per-command deadline" against a blanket timeout deliberately — the point is that the bound is per-command rather than one fixed number — so it is a design stance rather than an unanswered measure.
