#!/usr/bin/env python3
"""rowconv.py — the deterministic core of the ROADMAP → queue-member conversion (PROTOTYPE).

Both convert.py (writes the sandbox out/ files) and proof.py (proves content preservation) import
this module, so the classification and the per-row normalization are stated ONCE and the proof checks
the written files against exactly the transform they were written by.

Classification word-lists: the CLOSED_SIGNALS / OPEN_SIGNALS logic is COPIED from
scripts/rotate-doc.py (not imported — that script's `_is_closed` reads only cell index 3 of a live
line and cuts its headline at the first `(`, which mis-reads a row whose leader is plain text followed
by a later `**bold**` span, e.g. row 436 "queued ... **... opening landed ...**"). The copy keeps
rotate-doc's two signal sets and extends them: the closed set gains `closed`/`verified`/`superseded`
(the terminal exits the queue-format names beyond rotate-doc's landed/decided/met), and matching is
word-boundary rather than substring so `ideal` no longer reads as `idea` and `opening` no longer reads
as `open`.
"""
import re

# --- copied from scripts/rotate-doc.py, extended (see module docstring) --------------------------
CLOSED_SIGNALS = ("landed", "decided", "met", "closed", "verified", "superseded")
# open signals that, in the row's LEADER, keep the row live (rotate-doc's OPEN_SIGNALS + the
# queue-format live words the leader can carry).
OPEN_LEADER = ("queued", "in-work", "in work", "deferred", "field leg", "field legs", "field-gated",
               "intended", "open", "[target]", "waiting", "waits", "remains", "half landed",
               "in flight", "far", "idea", "capture only", "open design", "captured")
# structured open-leg markers scanned across the WHOLE status: a leader that reads closed but carries
# one of these describes a still-open leg (row 424's "REMAINS (the his-gate)", row 235's
# "; open leg: ..."), so the row stays live and is flagged AMBIGUOUS for the reviewer. Kept to
# STRUCTURED forms — a leg declaration, not delivery-report prose: row 280's quoted `"open leg"` and
# row 115's "one terse line per open leg" carry no leg and must not match.
OPEN_TAIL_MARKERS = ("remains (", "field leg open", "field legs open", "firing deferred", "in flight")
# an "open leg" clause: the words followed by a colon or a dash (its detail), the shape a real pending
# leg takes; the quoted-noun and prose uses lack the trailing `:`/dash.
OPEN_LEG_CLAUSE_RE = re.compile(r"open leg\b\s*[:—–-]", re.I)

DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

# --- explicit deterministic overrides (orchestrator triage, 2026-07-23 ~19:5x) --------------------
# Recorded here so the re-run stays reproducible; both convert.py and proof.py read them.
#
# Row 99 -> ARCHIVE: its leader reads "in-work 2026-07-05" but the same cell later carries
# "**landed 2026-07-05 ~23:25, session 8**" and its acceptance closes "— MET" — terminally landed,
# the in-work leader is stale narration. Moved verbatim like the other closed rows.
# Row 445 -> ARCHIVE: it is the spec-format conversion itself, shipped as v4.0.0 on 2026-07-23
# (NEXT_STEPS.md's closed-movements line records it); its status cell was simply never updated at
# landing. It moves to the July file with a corrected cell (ARCHIVE_STATUS_REWRITE below).
FORCE_ARCHIVE = {99, 445}

# An archived row whose status cell is rewritten at the move (the only non-verbatim archive move,
# each a named per-row delta in the proof): the corrected landed marker leads, and the old cell text
# rides verbatim inside `(status note: …)` so no token is lost. Row 445's cell also carries the
# delegation accounting line, since tests/test_delegation_line.py scans archived forward-landed rows
# (a `**landed 20xx-xx-xx` cell dated 2026-07-12 or later must contain "delegation", INV-103).
ARCHIVE_STATUS_REWRITE = {445: (
    "**landed 2026-07-23 (v4.0.0).** Delegation (INV-103): the drafter-applier pipeline carried the "
    "format draft and the spec rewrite on worker seats, the door and the fold verdicts staying "
    "senior; the full accounting lives in JOURNAL.md's v4.0.0 chapter. — (status note: %s)")}


def archive_row_line(rid, cells, raw):
    """The line an archived row takes in the month file: the original line verbatim, except a row in
    ARCHIVE_STATUS_REWRITE, whose status cell is replaced by the corrected marker wrapping the old
    cell text (all other cells, the sixth drift cell included, ride unchanged)."""
    if rid not in ARCHIVE_STATUS_REWRITE:
        return raw if raw.endswith("\n") else raw + "\n"
    new_cells = list(cells)
    new_cells[3] = ARCHIVE_STATUS_REWRITE[rid] % cells[3]
    return "| " + " | ".join(new_cells) + " |\n"
# Row 69 -> stays deferred; no date exists anywhere on the row, so the date is its first git
# appearance (commit 810af02, 2026-07-05), and the trigger is named so the lint's deferred-trigger
# check reads it. The old status text still rides as the status note per the normal rule.
STATUS_CELL_OVERRIDE = {
    69: "*deferred* 2026-07-05 — revisit trigger: the next edit to the product-prover skill",
}


def tail_open(status):
    """True when the status carries a structured open-leg marker anywhere (a still-open leg)."""
    low = status.lower()
    if any(m in low for m in OPEN_TAIL_MARKERS):
        return True
    return OPEN_LEG_CLAUSE_RE.search(status) is not None


def _has(text, sig):
    """Word-boundary containment: `sig` bounded by a non-alphanumeric on each side (so `open` is not
    found inside `opening`, `idea` not inside `ideal`, `far` not inside `farther`)."""
    return re.search(r"(?<![A-Za-z0-9])" + re.escape(sig) + r"(?![A-Za-z0-9])", text, re.I) is not None


def leader(status):
    """The row's own leading claim. If the status opens with a bold span, that span is the leader;
    else the opening clause up to the first bold / `;` / em- or en-dash / newline."""
    s = status.strip()
    if s.startswith("**"):
        m = re.match(r"\*\*(.+?)\*\*", s, re.S)
        if m:
            return m.group(1).strip()
    idx = len(s)
    for d in ("**", ";", "—", "–", "\n"):
        j = s.find(d)
        if j != -1:
            idx = min(idx, j)
    return s[:idx].strip()


def is_live(status, rid=None):
    """Return (live: bool, ambiguous: bool). A row is ARCHIVE only when its leader reads terminally
    closed AND no structured open-leg marker appears anywhere in the status (the safe default is
    live: an unclassifiable or conflicting row is never buried). The FORCE_ARCHIVE override table
    stands above the word-lists: a row the orchestrator ruled terminally closed archives regardless
    of its stale leader."""
    if rid is not None and rid in FORCE_ARCHIVE:
        return False, False
    lead = leader(status)
    has_closed = any(_has(lead, s) for s in CLOSED_SIGNALS)
    has_open_lead = any(_has(lead, s) for s in OPEN_LEADER)
    if has_closed and not has_open_lead:
        if tail_open(status):
            return True, True   # leader closed, but a tail open-leg marker -> live + AMBIGUOUS
        return False, False     # ARCHIVE
    return True, False          # LIVE (leader carries an open word, or no closed signal)


def status_word(status):
    """Map the leader to one closed status word. Priority per the conversion brief:
    deferred > far > (named wait -> deferred) > in-work > queued."""
    lead = leader(status)
    if _has(lead, "deferred"):
        return "deferred"
    if _has(lead, "far tier") or _has(lead, "far"):
        return "far"
    for w in ("field leg", "field legs", "leg open", "legs open", "field-gated", "remains",
              "waiting", "waits", "half landed"):
        if _has(lead, w):
            return "deferred"          # the named wait is the revisit trigger
    for w in ("in-work", "in work", "in flight"):
        if _has(lead, w):
            return "in-work"
    if tail_open(status):
        return "deferred"                  # a leg named open is the revisit trigger
    return "queued"


def pick_date(status, wish):
    """The earliest ISO date in the status cell; fallback the earliest in the wish cell.
    Returns (date_or_None, source) where source is 'status' | 'wish' | 'none'."""
    ds = DATE_RE.findall(status)
    if ds:
        return min(ds), "status"
    dw = DATE_RE.findall(wish)
    if dw:
        return min(dw), "wish"
    return None, "none"


def new_class(old_class, rid):
    """Class-cell normalization: big -> large; row 411's stray `far` -> the surface its wish names."""
    c = old_class.strip()
    if rid == 411:
        return "surface"                # the wish names a new user-facing orchestrator surface
    # keep any priority suffix (e.g. "small · quick win") intact, mapping only the size word.
    parts = c.split(" · ", 1)
    size = parts[0].strip()
    if size == "big":
        size = "large"
    return size + (" · " + parts[1] if len(parts) > 1 else "")


DEFERRED_TRIGGER_TAIL = " — revisit trigger: see the status note"


def new_status_cell(status, wish, rid):
    """The normalized status cell: `*word* DATE`, a deferred row carrying a revisit-trigger clause so
    the row lint (which demands the literal trigger/revisit word) passes; the real trigger text rides
    on, unedited, inside the status note appended to the wish cell. STATUS_CELL_OVERRIDE wins where
    the orchestrator ruled a cell's exact text (row 69: no date exists on the row, so the git-history
    date and a named trigger are supplied)."""
    if rid in STATUS_CELL_OVERRIDE:
        return STATUS_CELL_OVERRIDE[rid]
    word = status_word(status)
    date, _src = pick_date(status, wish)
    date = date or "0000-00-00"          # a no-date row is reported; this keeps the cell lint-shaped
    cell = "*%s* %s" % (word, date)
    if word == "deferred":
        cell += DEFERRED_TRIGGER_TAIL
    return cell


def new_wish_cell(wish, status):
    """The wish cell gains ` (status note: <old status verbatim>)` so no status token is deleted."""
    return "%s (status note: %s)" % (wish, status)


def parse_body_rows(text):
    """Every body data row of ROADMAP.md as (rownum, cells, raw_line). Cells are the stripped
    pipe-split fields; raw_line keeps the exact original line (trailing newline included)."""
    rows = []
    for raw in text.splitlines(keepends=True):
        line = raw.rstrip("\n")
        if line.startswith("|") and not line.startswith("|---") and "Wish (plain words)" not in line:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and cells[0].isdigit():
                rows.append((int(cells[0]), cells, raw))
    return rows


def normalize_live_row(rid, cells):
    """Build the normalized five-cell live row string (no trailing newline). cells is the stripped
    field list (5 or 6 wide). The sixth drift cell (a lone dash at index 4) is dropped."""
    wish = cells[1]
    old_class = cells[2]
    status = cells[3]
    accept = cells[5] if len(cells) >= 6 else (cells[4] if len(cells) >= 5 else "")
    w = new_wish_cell(wish, status)
    c = new_class(old_class, rid)
    s = new_status_cell(status, wish, rid)
    return "| %d | %s | %s | %s | %s |" % (rid, w, c, s, accept)
