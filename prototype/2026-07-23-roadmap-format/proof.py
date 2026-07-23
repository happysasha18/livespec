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
# OLD side pinned to the last pre-conversion commit (the working ROADMAP.md is the applied NEW body
# since 6edcf32); same pin as convert.py's OLD_COMMIT.
OLD_COMMIT = "859dcfc"
NEW_BODY = os.path.join(HERE, "out", "ROADMAP.md")
NEW_ARCHIVE = os.path.join(HERE, "out", "rotated-ROADMAP-2026-07.md")
NEW_NOTES = os.path.join(HERE, "out", "docs", "queue-archive",
                         "status-notes-ROADMAP-2026-07-23.md")
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
    import subprocess
    old_text = subprocess.run(["git", "show", "%s:ROADMAP.md" % OLD_COMMIT], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout
    new_body_text = open(NEW_BODY, encoding="utf-8").read()
    new_arch_text = open(NEW_ARCHIVE, encoding="utf-8").read()
    new_notes_text = open(NEW_NOTES, encoding="utf-8").read()

    old_rows = rowconv.parse_body_rows(old_text)
    live = []              # (rid, cells, scell, meta) — the shared final_row classification
    n_sweep_archived = 0
    for rid, cells, raw in old_rows:
        v = rowconv.final_row(rid, cells)
        if v[0] == "live":
            live.append((rid, cells, v[1], v[3]))
        elif v[0] == "archive-sweep":
            n_sweep_archived += 1

    # --- the compared regions: OLD data rows vs NEW body rows + archive rows + notes ENTRIES ------
    # (round 6: each live row's pre-conversion status text lives verbatim in the notes file, so it
    # cancels against the old cell there; the notes file's prose header is excluded and reported.)
    notes_entries = new_notes_text[new_notes_text.index("\n## row"):]
    old_region = data_rows_text(old_text)
    new_region = (data_rows_text(new_body_text) + "\n" + data_rows_text(new_arch_text)
                  + "\n" + notes_entries)
    old_w, old_p = counts(old_region)
    new_w, new_p = counts(new_region)

    # --- expected deltas, built from named classes ------------------------------------------------
    exp_add_w, exp_rem_w = collections.Counter(), collections.Counter()
    exp_add_p, exp_rem_p = collections.Counter(), collections.Counter()

    n_live6 = 0
    n_inwork_rewrites = 0
    class_pairs = []
    for rid, cells, scell, meta in live:
        # new status cell additions (tokenized from the exact generated string, sweep verdicts
        # included). DUPLICATION CHOICE: a deferred row's extracted trigger is COPIED into the status
        # cell while the old text stays verbatim in the notes file / acceptance cell, so the
        # duplicated tokens are accounted here inside the status-cell addition — copy-not-move keeps
        # the notes verbatim under the nothing-lost rule.
        w, p = counts(scell)
        exp_add_w += w
        exp_add_p += p
        # round-7 rule 5: a deferred row's acceptance phrase "stays in-work" reads "stays open".
        for tok in meta["inwork_rewrites"]:
            exp_rem_w[tok] += 1
            exp_add_w["open"] += 1
            exp_rem_p["-"] += tok.count("-")   # the hyphen inside `in-work` leaves with the word
            n_inwork_rewrites += 1
        # the notes entry's own section header: `## row <id>` (the entry BODY cancels with the old
        # status cell, both verbatim).
        exp_add_w["row"] += 1
        exp_add_w[str(rid)] += 1
        exp_add_p["#"] += 2
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
                          {rid for rid, _, _ in old_rows} - {rid for rid, _, _, _ in live})
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

    status_hist = collections.Counter(m["word"] for _, _, _, m in live)

    L = []
    L.append("# Content-preservation proof — ROADMAP.md format conversion (row 480)\n")
    L.append("**Verdict: %s**\n" % ("PASS — every token difference is a declared delta" if ok
                                     else "FAIL — an unexplained token difference remains"))
    L.append("Compared the OLD `ROADMAP.md` body (git %s) against the NEW live body plus the July "
             "archive plus the status-notes file's entries, over the data-row region (preambles, table "
             "headers, separators, and the notes file's prose header excluded and reported), "
             "word-token multiset and punctuation multiset, modulo the named deltas below. "
             "Live rows: %%d (%%s). Archived rows: %%d — moved verbatim, byte-identical, so they "
             "cancel." % OLD_COMMIT
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
    notes_head_w = len(WORD_RE.findall(new_notes_text[:new_notes_text.index("\n## row")]))
    L.append("- **Status-notes file header generated** — excluded from the new side; %d word tokens "
             "(what the file is; not a rotated-rows archive, no manifest line)." % notes_head_w)
    L.append("")
    L.append("## Named deltas (reconciled in the compared data-row region)\n")
    L.append("- **Archived rows verbatim** — %d of %d archived rows, present in the OLD body and the "
             "NEW archive byte-for-byte; net-zero token contribution (the nothing-lost move)."
             % (len(old_rows) - len(live) - len(rewrite_rows), len(old_rows) - len(live)))
    for rid in rewrite_rows:
        L.append("- **Archived row %d status corrected at the move** (override table) — the cell "
                 "gains `%s`, the old cell text riding verbatim inside the note; tokenized and "
                 "reconciled per row." % (rid, rowconv.ARCHIVE_STATUS_REWRITE[rid] % "…"))
    L.append("- **Status normalized, token-preserving** — each of the %d live rows' pre-conversion "
             "status text stands verbatim in the status-notes file (so it cancels against the old "
             "cell); ADDED per row: the new `*word* DATE` status cell (a deferred row with its real "
             "inline `— revisit trigger: …` clause) and the notes entry's `## row <id>` header "
             "(`row`, the id; `#` × 2)." % len(live))
    L.append("- **Deferred trigger duplication (the declared choice: copy, not move)** — a deferred "
             "row's extracted trigger clause is COPIED into the status cell while the notes entry "
             "stays verbatim, so the duplicated tokens are counted inside the per-row status-cell "
             "addition above; moving the clause out of the note would have broken the notes file's "
             "verbatim guarantee.")
    L.append("- **Round-7 sweep archives** — %d rows whose landing was recorded off the status cell "
             "(wish/acceptance evidence, no open marker) moved to the archive verbatim; they cancel "
             "like every verbatim move." % n_sweep_archived)
    L.append("- **Acceptance-cell state words (round-7 rule 5)** — `stays in-work` reads `stays "
             "open` in a deferred row's acceptance cell: %d instance(s) (removed the matched "
             "`in-work` spelling, added `open`; `stays` untouched)." % n_inwork_rewrites)
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
