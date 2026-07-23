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
# Row 128 -> ARCHIVE (final round, cold read): its cell reads "landed 2026-07-06 — whole: the open
# leg ... CLOSED 2026-07-06 ~13:57" — the leg closed minutes later in the same cell; terminally
# landed; the open-leg tail scan over-matched. Moved verbatim.
FORCE_ARCHIVE = {99, 128, 445}

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
    # final round (cold read): closed-family leaders that fell to *queued* — each is a landed build
    # with one leg still riding, so *deferred* on the named leg, the old cell as the status note.
    55: "*deferred* 2026-07-07 — revisit trigger: the machine leg rides row 3's landing",
    129: "*deferred* 2026-07-06 — revisit trigger: the first real adopted host carries a "
         "project.kind line by deed",
    131: "*deferred* 2026-07-06 — revisit trigger: the next working session narrates unprompted, "
         "with no third ask",
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
    if any(_has(lead, s) for s in CLOSED_SIGNALS):
        return "deferred"                  # a live-kept closed-family leader is a parked leg, never
                                           # a fresh queue entry (final-round rule; zero extra rows
                                           # beyond the override table on the pinned source, probed)
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


# Trigger extraction (round 6): a *deferred* row's status cell names its REAL trigger inline — the
# shortest clause of the old cell that names the concrete revisit event, <= 20 words. Patterns tried
# in order; the captured clause is cut at the first structural boundary (`**`, `;`, ` — `, newline)
# and capped at 20 words. A row where every pattern fails takes the last-resort fallback and is
# flagged NEEDS-TRIGGER on the mapping table.
TRIGGER_PATTERNS = [
    re.compile(r"revisit trigger:\s*", re.I),   # colon required: prose says "revisit trigger" without
                                                # one when merely describing the mechanism (row 405)
    re.compile(r"Remainder:\s*"),
    re.compile(r"REMAINS\s*(?:\([^)]*\))?:\s*"),
    re.compile(r"open legs?\s*(?:\([^)]*\))?\s*[:]\s*", re.I),   # optional (INV-nn) before the colon
    re.compile(r"OPEN\s*—\s*"),
    re.compile(r"waiting on\s+", re.I),
    re.compile(r"waits(?:\s*\[[^\]]*\])?:\s*", re.I),            # "Field beat that waits [INV-94]: …"
    re.compile(r"field-gated\s+on\s+", re.I),
    re.compile(r"still deferred[^:]{0,60}:\s*", re.I),           # "still deferred and owned …: …"
    re.compile(r"deferred\s*—\s*", re.I),
]
# the trailing form: "<the open leg's event> — OPEN[,;…]" — tried only after every leading pattern
# fails; the LAST such clause is taken (a row lists its legs done-first, open-last).
TRAILING_OPEN_RE = re.compile(r"—\s*OPEN(?![A-Za-z0-9])")
FALLBACK_TRIGGER = "re-read the wish's record in the status notes"


def _clip(clause):
    clause = clause.strip().rstrip(",.").strip()
    words = clause.split()
    if len(words) > 20:
        clause = " ".join(words[:20])
    return clause


def extract_trigger(status):
    """Return (trigger_text, how) — how is 'inline' or 'fallback'."""
    for pat in TRIGGER_PATTERNS:
        m = pat.search(status)
        if not m:
            continue
        rest = status[m.end():]
        cut = len(rest)
        for d in ("**", ";", " — ", "\n"):
            j = rest.find(d)
            if j != -1:
                cut = min(cut, j)
        clause = _clip(rest[:cut])
        if clause:
            return clause, "inline"
    last = None
    for m in TRAILING_OPEN_RE.finditer(status):
        last = m
    if last is not None:
        head = status[:last.start()]
        start = max(head.rfind(";"), head.rfind("**"), head.rfind("\n"))
        clause = _clip(head[start + 1:].lstrip("*"))
        if clause:
            return clause, "inline"
    return FALLBACK_TRIGGER, "fallback"


def new_status_cell(status, wish, rid):
    """The normalized status cell: `*word* DATE`, a *deferred* row carrying its REAL revisit trigger
    inline (round 6: the status cell is the sole authority on current state; no cell may point at the
    status note for its trigger). STATUS_CELL_OVERRIDE wins where the orchestrator ruled a cell's
    exact text."""
    if rid in STATUS_CELL_OVERRIDE:
        return STATUS_CELL_OVERRIDE[rid]
    word = status_word(status)
    date, _src = pick_date(status, wish)
    date = date or "0000-00-00"          # a no-date row is reported; this keeps the cell lint-shaped
    cell = "*%s* %s" % (word, date)
    if word == "deferred":
        trigger, _how = extract_trigger(status)
        cell += " — revisit trigger: %s" % trigger
    return cell


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


# --- round 7: the three-cell sweep --------------------------------------------------------------
# Some rows recorded their landings in the WISH or ACCEPTANCE cells while the status cell stayed
# queued (rows 130/133/190/279's class), so the classifier reads all three text cells per LIVE row:
# a whole-landing record (dated landed tokens / MET on the Done-when clauses) with NO open marker
# archives the row; landed-leg markers PLUS an open marker re-status the row *deferred* with the
# extracted trigger; no landed markers leaves the row as mapped; an unsettleable disagreement joins
# the AMBIGUOUS list and stays live.
SWEEP_LANDED_RE = re.compile(r"(?<![A-Za-z0-9])landed(?![A-Za-z0-9])[^|]{0,40}?(20\d\d-\d\d-\d\d)",
                             re.I | re.S)
SWEEP_MET_RE = re.compile(r"(?<![A-Za-z0-9])MET(?![A-Za-z0-9])")
SWEEP_OPEN_RES = [
    re.compile(r"(?<![A-Za-z0-9])OPEN(?![A-Za-z0-9])"),           # the uppercase state marker
    re.compile(r"open leg", re.I),
    re.compile(r"(?<![A-Za-z0-9])remains(?![A-Za-z0-9])", re.I),
    re.compile(r"(?<![A-Za-z0-9])waits(?![A-Za-z0-9])", re.I),
    re.compile(r"(?<![A-Za-z0-9])rides(?![A-Za-z0-9])", re.I),
    re.compile(r"field leg", re.I),
    re.compile(r"\[target\]"),
    re.compile(r"leg:\s*open", re.I),
    re.compile(r"(?<![A-Za-z0-9])PENDING(?![A-Za-z0-9])"),
    re.compile(r"(?<![A-Za-z0-9])still deferred(?![A-Za-z0-9])", re.I),  # row 436's own open marker
]

# per-row sweep overrides (recorded, deterministic — the generic markers over-match on one row):
# Row 420 -> ARCHIVE 2026-07-18: its acceptance closes "With candidate 4 landed the row-420
# audit-and-build is COMPLETE" — all four candidates carry dated LANDED records; the lone open-marker
# hit is prose ("rides no CI step"), not an open leg.
SWEEP_OVERRIDES = {420: ("archive", "2026-07-18")}


def acceptance_cell(cells):
    return cells[5] if len(cells) >= 6 else (cells[4] if len(cells) >= 5 else "")


def sweep_evidence(cells):
    """Return (landed_dates, met_count, open_marker_names) read across wish+status+acceptance."""
    acc = acceptance_cell(cells)
    combined = " | ".join((cells[1], cells[3], acc))
    landed_dates = SWEEP_LANDED_RE.findall(combined)
    met = len(SWEEP_MET_RE.findall(acc))
    opens = [p.pattern for p in SWEEP_OPEN_RES if p.search(combined)]
    return landed_dates, met, opens


def sweep_verdict(rid, cells, mapped_word, trigger_how):
    """The round-7 verdict for a live row: ('archive', date) | ('deferred', trigger, how) |
    ('keep',) | ('ambiguous', note). mapped_word/trigger_how are the round-6 mapping's outputs."""
    if rid in SWEEP_OVERRIDES:
        return SWEEP_OVERRIDES[rid]
    landed, met, opens = sweep_evidence(cells)
    if not landed and not met:
        return ("keep",)
    if mapped_word == "in-work":
        # an active claim beside a landed record is the stale-claim sweep's case (round-3 triage
        # kept 386/412/480 in-work); the sweep does not re-judge a claim, it lists the tension.
        return ("ambiguous", "in-work claim beside landed evidence — held for the stale-claim sweep")
    if mapped_word == "deferred" and trigger_how in ("inline", "override"):
        return ("keep",)   # already deferred with a named trigger
    if not opens:
        dates = sorted(landed)
        if not dates:
            dates = sorted(DATE_RE.findall(cells[3] + " " + acceptance_cell(cells)))
        return ("archive", dates[-1] if dates else None)
    trigger, how = extract_trigger(cells[3] + " ; " + acceptance_cell(cells))
    return ("deferred", trigger, how)


def final_row(rid, cells):
    """The whole classification for one source body row. Returns one of:
       ('archive-r6',)                       — rounds 1-6: terminally closed, moves per archive rules;
       ('archive-sweep', date)               — round-7 rule 1: whole landing recorded off-status;
       ('live', status_cell, acceptance, meta) — meta: {'word','how','sweep','ambiguous'}."""
    status = cells[3]
    live, ambiguous = is_live(status, rid)
    if not live:
        return ("archive-r6",)
    scell = new_status_cell(status, cells[1], rid)
    word = scell.split("*")[1]
    how = None
    if rid in STATUS_CELL_OVERRIDE:
        how = "override"
    elif word == "deferred":
        how = extract_trigger(status)[1]
    verdict = sweep_verdict(rid, cells, word, how)
    sweep = verdict[0] if verdict[0] != "keep" else None
    if verdict[0] == "archive":
        return ("archive-sweep", verdict[1])
    if verdict[0] == "deferred":
        date, _src = pick_date(status, cells[1])
        scell = "*deferred* %s — revisit trigger: %s" % (date or "0000-00-00", verdict[1])
        word, how = "deferred", verdict[2]
    acc, removed = rewrite_acceptance(word, acceptance_cell(cells))
    meta = {"word": word, "how": how, "sweep": sweep,
            "ambiguous": ambiguous or verdict[0] == "ambiguous",
            "inwork_rewrites": removed}
    return ("live", scell, acc, meta)


def rewrite_acceptance(word, acc):
    """Round-7 named delta: in a *deferred* row's acceptance cell the literal phrase 'stays in-work'
    (any casing) reads 'stays open'. Returns (new_acc, removed_tokens) where removed_tokens are the
    exact 'in-work' spellings replaced (each adds one 'open')."""
    if word != "deferred":
        return acc, []
    removed = []

    def _sub(m):
        removed.append(m.group(2))
        return m.group(1) + "open"

    new = re.sub(r"(stays\s+)(in-work)", _sub, acc, flags=re.I)
    return new, removed


def normalize_live_row(rid, cells):
    """Build the normalized five-cell live row string (no trailing newline). cells is the stripped
    field list (5 or 6 wide). The sixth drift cell (a lone dash at index 4) is dropped. Round 6: the
    wish cell rides verbatim — the pre-conversion status text moves to the status-notes file, not
    into the row (a bold LANDED inside an in-body quote out-shouts the italic status)."""
    verdict = final_row(rid, cells)
    assert verdict[0] == "live", "normalize_live_row called on an archived row %d" % rid
    _, scell, acc, _meta = verdict
    return "| %d | %s | %s | %s | %s |" % (rid, cells[1], new_class(cells[2], rid), scell, acc)
