# GAPS — source holes found during the rewrite

These are places where the source section states a behaviour but leaves a judge, a measure, a default, or a definition unanswered. Each became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. None of these blocks the rewrite; each is a question the source owes.

## New holes

### G1 — the net-liveness meter's "declared window" has no owner or default
**Where:** Requirement 9, criterion 3. Source: the net-liveness meter, `PRODUCT_SPEC.md` ~line 1876, `[INV-202]`.
**Hole:** A net "with runs at or over a declared window and zero fires is surfaced as a retirement candidate." The source names a per-net declared window as the threshold for the retirement reading but never states who declares that window (the pack, the host, the roster entry) or what its default value is. The sibling number — how often the net ran and fired — is concrete; this window is not.
**What it blocks:** The meter cannot decide when a quiet net becomes a retirement candidate without knowing the window, so the retirement reading either never fires or fires on an undeclared value. A test author cannot pin the boundary case.

### G2 — the conduct judge's built-in strictness default is unstated
**Where:** Requirement 13, criterion 8. Source: the conduct judge, `PRODUCT_SPEC.md` ~line 1884, `[INV-241]`.
**Hole:** The per-person strictness — how hard a host's judge reds a borderline act — has its home named as the future parameters registry, and "until that registry ships the judge reads a built-in default a host overrides by environment." The source names that a built-in default exists but never states its value or how hard it reds a borderline act out of the box.
**What it blocks:** A host adopting the conduct judge before the parameters registry ships cannot know how the judge will treat a borderline act, and a test author cannot pin the default strictness behaviour. The registry dependency is handled (a default stands in), but the default itself is undefined.

### G3 — the runaway-child "burning" threshold has no default
**Where:** Requirement 15, criterion 1. Source: the runaway-child report, `PRODUCT_SPEC.md` ~line 1913, `[INV-213]`.
**Hole:** A descendant counts as burning when "its processor share at or above the host-settable threshold." The source makes the threshold host-settable but names no default value. The mechanism ships usable on demand, yet the reporter's firing point depends on a number no default supplies.
**What it blocks:** On a host that has set no threshold, the reporter's out-of-box firing point is unstated — it may never fire, or fire on an undeclared value. A test author cannot pin the burning boundary without the default.

### G4 — the "conflicts" check names no conflict
**Where:** Requirement 8, criterion 1. Source: the four project-side checks, `PRODUCT_SPEC.md` ~line 1965, `[INV-97]`, and the E-6 index row.
**Hole:** The four project-side checks are named completeness, tests-present, behaviour-traces-to-spec, and conflicts. The first three carry their subject in their own names; "conflicts" does not, and neither the section body, the INV-97 index row, nor the E-6 index row states what conflict the check detects (two documents disagreeing, two owners claiming one fact, or something else).
**What it blocks:** A host attaching the four checks cannot know what the conflicts check will red on, and a test author cannot plant the one defect the check must prove itself red on.

## Note on scope

These three are the genuinely new holes this machinery section opens. Several other numbers in the section are host-settable *by design* and are not holes, because the source states their default: the waiting board's shown cap (12 items), the far-tier surface cadence (one offer per 14 days), the lean-orchestrator threshold (50 KiB), the monitor's stale-lock bound (~1 hour), and the legibility floor's own numbers (owned by the founding section). Each of those names both a default and the human's power to change it, which is a complete answer rather than a hole.
