#!/usr/bin/env python3
"""nonempty_input.py — the shared shape behind "a check that looked at nothing is not a pass"
(SPEC INV-218, ROADMAP 384).

THE LAW behind it: a check whose INPUT SET is empty reports clean while testing nothing. A
uniqueness check over zero items finds zero collisions; a "does every X satisfy Y" over zero X
is vacuously true. The check turns green not because the fact holds but because nothing was
looked at — and an empty input set is nearly always the defect, not a happy void. The drafter's
own self-catch minted this class: it scanned its freshly minted codes for collisions, the codes
were absent from the prose entirely, and the scan compared zero against zero and reported clean.

So the shape is one line of discipline, the sibling of the unexpected-skip law [INV-155] (green
means the skip-set is exactly the pinned list; an unexpected skip is a failure outright): a check
DECLARES the input set it expects to be non-empty, and an empty set REDS BY NAME rather than
passing silently. Where a check genuinely may look at an empty set, it says so at that call site
with its own reason, exactly as a skip is pinned with its reason — the default is that empty is a
finding.

A guardrail script uses `require_nonempty` at the top of its own run: it hands its check name and
a human name for the input set, and gets the items back when they are non-empty or a
`VacuousInputError` naming both when they are empty. A script catches it and exits non-zero with
the named message, so the gate reds by name in place of reporting clean over nothing.
"""


class VacuousInputError(Exception):
    """A check's expected-non-empty input set came up empty — the check would report clean while
    testing nothing (SPEC INV-218). Raised by `require_nonempty`, carrying a message that names
    both the check and the empty input set."""


def require_nonempty(check_name, input_name, items):
    """Return `items` as a list when it holds at least one member; raise `VacuousInputError`
    naming both the check and the input set when it is empty.

    check_name  — the check declaring the expectation (usually the script's basename), so the red
                  says WHICH check looked at nothing.
    input_name  — a human name for the input set ("the Formal-index anchors", "the tracked
                  scripts"), so the red says WHICH set was empty.
    items       — any iterable; consumed into a list once.
    """
    items = list(items)
    if not items:
        raise VacuousInputError(
            "%s: the input set %r is EMPTY — the check would report clean while testing nothing "
            "(a vacuous pass, SPEC INV-218). An empty input set is nearly always the defect: the "
            "parse broke, the source moved, or the set was never populated. Fix the input, or "
            "declare at this call site why an empty set is legitimate here." % (check_name, input_name))
    return items
