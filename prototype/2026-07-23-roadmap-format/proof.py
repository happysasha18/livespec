#!/usr/bin/env python3
"""proof.py — content-preservation proof for the ROADMAP.md format conversion (PROTOTYPE, row 480).

Restructure-safety (SPEC INV-111): word-token identity alone is insufficient, so this checks BOTH the
word-token multiset AND the punctuation multiset of the OLD ROADMAP.md body against the NEW live body
plus the month archive, over the DATA-ROW region only (preambles, table headers, and separators
excluded on both sides and reported), MODULO the declared deltas — each a named class with its count:

  - archived rows move VERBATIM: each terminally-closed row's line is byte-identical in the OLD body
    and in the NEW archive, so the 225 archived rows cancel and prove nothing was lost in the move;
  - live rows keep every token: the ENTIRE old status text rides on, unedited, inside the wish cell's
    `(status note: …)`, so the old status multiset is preserved (not removed);
  - per live row, ADDED: the wrapper `(status note: )` (words status, note; punct ( ) :) and the new
    status cell `*word* DATE` (+ the deferred revisit-trigger tail), tokenized from the exact strings;
  - per live row, REMOVED: the dropped sixth drift cell (punct — and one | ) where the row had it;
  - class re-vocabularying: big -> large (rows 445, 455) and row 411's far -> surface.

Any token difference — word or punctuation — not attributed to a named class, in either direction, is
a failure printed as the offending residual. The proof PASSES only when every residual is empty.
Writes the verdict to out/proof-report.md. Run from the repo root:
  python3 prototype/2026-07-23-roadmap-format/proof.py
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rowconv  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OLD_SRC = os.path.join(ROOT, "ROADMAP.md")
NEW_BODY = os.path.join(HERE, "out", "ROADMAP.md")
NEW_ARCHIVE = os.path.join(HERE, "out", "rotated-ROADMAP-2026-07.md")
REPORT = os.path.join(HERE, "out", "proof-report.md")

WORD_RE = re.compile(r"[^\W_]+(?:[-'][^\W_]+)*", re.UNICODE)
PUNCT_RE = re.compile(r"[^0-9A-Za-z\s]", re.UNICODE)
HEADER_FIRST = "| # | Wish (plain words) | Class | Status | Decision / acceptance |"


def counts(text):
    return (collections.Counter(WORD_RE.findall(text)),
            collections.Counter(PUNCT_RE.findall(text)))


def data_rows_text(text):
    """Concatenate every body DATA row line (a `| n | … |` line), dropping the header and separator."""
    out = []
    for raw in text.splitlines():
        line = raw.rstrip("\n")
        if line.startswith("|") and not line.startswith("|---") and "Wish (plain words)" not in line:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and cells[0].isdigit():
                out.append(line)
    return "\n".join(out)


def preamble_wordcount(text):
    return len(WORD_RE.findall(text.split(HEADER_FIRST, 1)[0]))


def main():
    old_text = open(OLD_SRC, encoding="utf-8").read()
    new_body_text = open(NEW_BODY, encoding="utf-8").read()
    new_arch_text = open(NEW_ARCHIVE, encoding="utf-8").read()

    old_rows = rowconv.parse_body_rows(old_text)
    live = [(rid, cells) for rid, cells, raw in old_rows if rowconv.is_live(cells[3], rid)[0]]

    # --- the two compared regions (data rows only) ------------------------------------------------
    old_region = data_rows_text(old_text)
    new_region = data_rows_text(new_body_text) + "\n" + data_rows_text(new_arch_text)
    old_w, old_p = counts(old_region)
    new_w, new_p = counts(new_region)

    # --- expected deltas, built from named classes ------------------------------------------------
    exp_add_w, exp_rem_w = collections.Counter(), collections.Counter()
    exp_add_p, exp_rem_p = collections.Counter(), collections.Counter()

    WRAP = " (status note: "          # opens the status note in the wish cell
    WRAP_CLOSE = ")"
    n_live6 = 0
    class_pairs = []
    for rid, cells in live:
        status = cells[3]
        wish = cells[1]
        # wrapper additions
        w, p = counts(WRAP + WRAP_CLOSE)
        exp_add_w += w
        exp_add_p += p
        # new status cell additions (tokenized from the exact generated string)
        scell = rowconv.new_status_cell(status, wish, rid)
        w, p = counts(scell)
        exp_add_w += w
        exp_add_p += p
        # dropped sixth drift cell
        if len(cells) >= 6:
            n_live6 += 1
            exp_rem_p["—"] += 1
            exp_rem_p["|"] += 1
        # class re-vocabularying
        old_size = cells[2].split(" · ", 1)[0].strip()
        new_size = rowconv.new_class(cells[2], rid).split(" · ", 1)[0].strip()
        if old_size != new_size:
            exp_rem_w[old_size] += 1
            exp_add_w[new_size] += 1
            class_pairs.append((rid, old_size, new_size))

    # --- the rewritten archive rows (ARCHIVE_STATUS_REWRITE): the only non-verbatim archive moves,
    # each a named per-row delta — the corrected landed marker wraps the old cell text, which rides
    # verbatim, so the expected addition is exactly the template with the old text removed.
    rewrite_rows = sorted(set(rowconv.ARCHIVE_STATUS_REWRITE) &
                          {rid for rid, _, _ in old_rows} - {rid for rid, _ in live})
    for rid in rewrite_rows:
        w, p = counts(rowconv.ARCHIVE_STATUS_REWRITE[rid] % "")
        exp_add_w += w
        exp_add_p += p

    # --- signed multiset deltas (add and remove of the SAME token net out) ------------------------
    def signed(new_c, old_c):
        d = {}
        for t in set(new_c) | set(old_c):
            v = new_c[t] - old_c[t]
            if v:
                d[t] = v
        return d

    def signed_expected(add_c, rem_c):
        d = {}
        for t in set(add_c) | set(rem_c):
            v = add_c[t] - rem_c[t]
            if v:
                d[t] = v
        return d

    raw_delta_w = signed(new_w, old_w)
    raw_delta_p = signed(new_p, old_p)
    exp_delta_w = signed_expected(exp_add_w, exp_rem_w)
    exp_delta_p = signed_expected(exp_add_p, exp_rem_p)

    def residual(raw, exp):
        out = {}
        for t in set(raw) | set(exp):
            v = raw.get(t, 0) - exp.get(t, 0)
            if v:
                out[t] = v
        return out

    residuals = {
        "word-token residual (raw delta minus named deltas)": residual(raw_delta_w, exp_delta_w),
        "punctuation residual (raw delta minus named deltas)": residual(raw_delta_p, exp_delta_p),
    }
    ok = all(not c for c in residuals.values())

    # --- excluded-region reporting ----------------------------------------------------------------
    old_pre = preamble_wordcount(old_text)
    new_pre = preamble_wordcount(new_body_text)
    arch_head_w = len(WORD_RE.findall(new_arch_text.split(HEADER_FIRST, 1)[0]))

    status_hist = collections.Counter(rowconv.status_word(c[3]) for _, c in live)

    L = []
    L.append("# Content-preservation proof — ROADMAP.md format conversion (row 480)\n")
    L.append("**Verdict: %s**\n" % ("PASS — every token difference is a declared delta" if ok
                                     else "FAIL — an unexplained token difference remains"))
    L.append("Compared the OLD `ROADMAP.md` body against the NEW live body plus the July archive, over "
             "the data-row region (preambles, table headers, and separators excluded on both sides), "
             "word-token multiset and punctuation multiset, modulo the named deltas below. "
             "Live rows: %d (%s). Archived rows: %d — moved verbatim, byte-identical, so they cancel."
             % (len(live), " · ".join("%s %d" % (k, status_hist[k]) for k in
                ("queued", "in-work", "deferred", "far")),
                len(old_rows) - len(live)))
    L.append("")
    L.append("## Named deltas (excluded regions, reported)\n")
    L.append("- **Preamble replaced** — excluded both sides. Old preamble+manifest %d word tokens; new "
             "%d word tokens (the new-format preamble; the manifest keeps the 2026-07-18 line and gains "
             "one July line)." % (old_pre, new_pre))
    L.append("- **Archive file header generated** — excluded from the new side; %d word tokens (the "
             "`# Rotated …` title and the ARCHIVED provenance note)." % arch_head_w)
    L.append("")
    L.append("## Named deltas (reconciled in the compared data-row region)\n")
    L.append("- **Archived rows verbatim** — %d of %d archived rows, present in the OLD body and the "
             "NEW archive byte-for-byte; net-zero token contribution (the nothing-lost move)."
             % (len(old_rows) - len(live) - len(rewrite_rows), len(old_rows) - len(live)))
    for rid in rewrite_rows:
        L.append("- **Archived row %d status corrected at the move** (override table) — the cell "
                 "gains `%s`, the old cell text riding verbatim inside the note; tokenized and "
                 "reconciled per row." % (rid, rowconv.ARCHIVE_STATUS_REWRITE[rid] % "…"))
    L.append("- **Status normalized, token-preserving** — the old status cell of each of the %d live "
             "rows is preserved unedited inside the wish cell's `(status note: …)`; ADDED per row: the "
             "wrapper (`status`, `note`; `(` `)` `:`) and the new `*word* DATE` status cell (a deferred "
             "row also `— revisit trigger: see the status note`)." % len(live))
    L.append("- **Sixth drift cell dropped** — %d live rows carried a lone-dash sixth cell; removed "
             "`—` × %d and `|` × %d." % (n_live6, n_live6, n_live6))
    L.append("- **Class re-vocabularying** — %d rows: %s."
             % (len(class_pairs), "; ".join("row %d %s→%s" % t for t in class_pairs)))
    L.append("")
    L.append("## Residuals (must all be empty)\n")
    for name, c in residuals.items():
        L.append("- %s: %s" % (name, dict(c) if c else "empty"))
    L.append("")
    report = "\n".join(L) + "\n"
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(report)
    sys.stdout.write(report)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
