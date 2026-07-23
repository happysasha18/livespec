# GAPS — source holes found during the rewrite

These are places where the source essay states a behaviour but leaves the measure, the default, or the interim answer unstated. Each became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. Neither hole blocks the rewrite; each is a question the source owes.

## New holes

### G1 — the input-capability co-occurrence value has no interim answer
**Where:** Requirement 8, criterion 12. Source: the composition-axes clause, `PRODUCT_SPEC.md` line 2065, `[INV-244]`.
**Hole:** The input-capability axis is modelled as combinable capabilities that co-occur on one device — touch, a fine pointer, hover, and a keyboard together. The source owes and answers the two elementary poles (touch and a fine pointer) up front, then defers the co-occurrence value — one device holding hover alongside touch, the tablet-with-trackpad-and-touchscreen case — to "the deferred forcing step that makes the author answer for the in-between." The value space is said to represent the co-occurrence now, but no interim answer and no default behaviour is stated for it today.
**What it blocks:** A surface's behaviour when touch and hover are both present on one device is unspecified until the forcing step ships, so a test author cannot pin the co-occurrence case. The forward mechanism is named (the forcing step); the interim behaviour is not.

### G2 — the delivery-separability "too small to split" payload has no measure
**Where:** Requirement 9, criterion 3. Source: the delivery-separability clause, `PRODUCT_SPEC.md` line 2067, `[INV-248]`.
**Hole:** A monolith may stand as a settled answer when its payload is "small enough that a split costs more than it saves." The source names the design as the judge (the lens stays a senior read the prover carries, not a gate) but states no measure — no payload size, and no comparison of split cost against split saving — for when a payload is small enough to make a whole-ship monolith settled.
**What it blocks:** The boundary between a settled small-payload monolith and an unexamined one cannot be pinned. The judge is named, so the format's judge-naming law is met; the measure that judge weighs is left to the design with no reference size, so a test author cannot plant the boundary case.

## Note on scope

These two are the genuinely open holes. Several other items in the essay read like holes but are stated deferrals with a named mechanism, or judgments with a named judge — each a complete answer for the format rather than a gap:

- **The sibling axes** (browser engine, locale and text direction, connection reach, first-versus-returning visit, accessibility, measurement reach) enter as their own per-kind increments; the source names them and defers each to its own increment, a stated roadmap rather than a blank.
- **The other kinds' axis sets** (a backend's load, version, and tenant among them) are each kind's own increment; the source names the backend set by example and leaves the rest to the per-kind founding declaration.
- **The refinement values** past the elementary input-capability poles (a stylus, a keyboard-only reach, an advanced-user device) are named as the human's taste, entering later — the judge is named (the human).
- **The recursive axis-registry similarity sweep** that would ask a kind which sibling axes it still lacks is named as a later increment with its own future row.
- **The minor-versus-major release-tier call** (R17) reads meaning no machine can and is a stated judgment the releasing session applies and names — the judge is named, so it is not a hole.
- **Motion-feel judgments** (R4, R6) are surfaced to the human wherever the author cannot judge; the judge is named.
