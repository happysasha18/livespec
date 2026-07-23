#!/usr/bin/env python3
"""proof.py — content-preservation proof for the row-477 matrix conversion (PROTOTYPE).

Restructure-safety: word-token identity alone is insufficient, so this checks BOTH the word-token
multiset AND the punctuation multiset of TEST_MATRIX.md, old (git show HEAD:TEST_MATRIX.md) vs new,
EXCLUDING the generated `## Reference` section, MODULO the declared deltas — each named with its count:

  - the preamble is rewritten (excluded from both sides; old/new token counts reported);
  - the `## Coverage validation` section retires (excluded from the old side; token count reported);
  - the generated `## Reference` section is excluded from the new side;
  - node-block table headers and separators are reshaped (excluded from both sides by structure);
  - status tokens are lowercased: BUILT -> built, TODO -> todo, RETIRED -> retired (word delta);
  - status tokens are italicised: +2 `*` per row (punctuation delta);
  - each spec-ref moves into its fact sentence wrapped in one bracket: +`[` +`]` per row, and the
    anchor WORD tokens are UNCHANGED by the move (a position move, asserted — the residual proves it);
  - each row narrows from six cells to five: -1 `|` per row (punctuation delta);
  - a cold-reader finding, folded the same delivery: every all-caps emphasis word left over from the
    six-cell format's house style (a code anchor, an acronym, a file name, or an id-prefix excepted) is
    lowercased in the Fact cells, one proper noun (ENGLISH -> English) aside — the exact 192-token
    removed/added map is declared below (word delta, no punctuation change; a hyphenated pair counts as
    one token, matching WORD_RE's own tokenizing of a hyphen-joined run).

Any OTHER token difference — word or punctuation — is a failure, printed as the offending residual.
Writes the verdict to PROOF.md beside this script. Run from the repo root:
  python3 prototype/2026-07-23-matrix-format/proof.py
"""
import collections
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MATRIX = os.path.join(ROOT, "TEST_MATRIX.md")
REPORT = os.path.join(os.path.dirname(__file__), "PROOF.md")

INVENTORY_HEAD = "## Artifact inventory"
COVERAGE_HEAD = "## Coverage validation"
REFERENCE_RE = re.compile(r"(?m)^## Reference *$")

WORD_RE = re.compile(r"[^\W_]+(?:[-'][^\W_]+)*", re.UNICODE)
PUNCT_RE = re.compile(r"[^0-9A-Za-z\s]", re.UNICODE)

# The row-477 cold-reader caps-emphasis sweep: every leftover all-caps emphasis word in the Fact cells,
# lowercased (one proper noun, ENGLISH -> English, aside). A fixed, one-time, hand-reconciled map — not
# derived from the current file, since the pre-sweep text it is a delta against no longer exists on
# disk once the sweep lands. Counted from the Fact-cell text before/after the sweep, backtick/quote spans
# excluded first so nothing verbatim was ever a candidate.
CAPS_SWEEP_REMOVED = {
    'ABOVE': 1, 'ACCEPTS': 1, 'ADDED': 1, 'ADJACENT': 1, 'ADOPTING': 1, 'ADVISORY': 2,
    'AGREED': 1, 'ALL': 1, 'ALOUD': 1, 'ALPHABET': 1, 'ALWAYS': 3, 'AND': 9,
    'ANY': 2, 'APPLIED': 1, 'ARCHIVED': 1, 'AT': 1, 'BEFORE': 4, 'BLOCK': 1,
    'BLOCKING': 1, 'BOTH': 7, 'BY': 8, 'CHANGES': 1, 'CHANNEL': 1, 'CHAT': 2,
    'CHECK': 2, 'CITE': 1, 'CITES': 1, 'CLASS': 1, 'CLOSED': 1, 'CODE': 1,
    'COMMITS': 1, 'CONFLICT': 1, 'CONVERSATION': 1, 'CROSS-LINK': 2, 'CURRENT': 1, 'DECIDE': 2,
    'DECIDED': 1, 'DECLARED': 4, 'DEED': 6, 'DEFAULT': 1, 'DEFINES': 1, 'DENIES': 1,
    'DERIVED': 1, 'DESIGN': 2, 'DIFFS': 1, 'DIGEST': 1, 'DIRECT': 1, 'DISCIPLINE': 1,
    'DISTINCT': 1, 'DO': 1, 'DOCUMENT': 1, 'DOES': 11, 'DONE': 1, 'DOWN': 1,
    'DRAFT': 1, 'DUTY': 1, 'ENGLISH': 1, 'ENTERED': 1, 'EXITS': 1, 'FEATURE': 1,
    'FEATURE-FIT': 2, 'FEEL': 1, 'FILE': 1, 'FIND': 1, 'FINDING': 1, 'FIRED': 1,
    'FIRST': 4, 'FLAG': 1, 'FOOTPRINT': 1, 'FOREIGN': 1, 'FORM': 2, 'FULL': 3,
    'GAP': 2, 'GRANTS': 1, 'HALT': 1, 'HARD-blocks': 1, 'HEARTBEAT': 1, 'HIGH-STAKES': 1,
    'HOLDING': 1, 'HOST': 1, 'HOW': 1, 'IDENTITY': 1, 'IN': 1, 'INCLUDING': 1,
    'INDEPENDENT': 1, 'INTAKE': 1, 'IS': 1, 'KIND': 5, 'KNOWN': 2, 'LAST': 1,
    'LATER': 1, 'LAW': 1, 'LIVE': 1, 'LIVE-STATE': 1, 'MAIN': 2, 'MANDATORY': 1,
    'MEANING': 1, 'MET': 1, 'METHOD': 1, 'MINOR': 1, 'NAME': 6, 'NAMING': 1,
    'NEITHER': 1, 'NEVER': 40, 'NEVER-list': 1, 'NEW': 4, 'NEW-verdict': 1, 'NO': 2,
    'NON-PROBLEM': 1, 'NOT': 1, 'NOT-side': 1, 'NOW': 3, 'OFF': 1, 'OFFER': 1,
    'OLD': 1, 'OLDER': 1, 'ONCE': 1, 'ONE': 17, 'ONLY': 1, 'OPENS': 4,
    'OR': 2, 'ORDER': 1, 'OUTSIDE': 1, 'OWED': 1, 'OWN': 1, 'OWNED': 1,
    'PASSES': 1, 'PERFORMS': 1, 'PLACE': 1, 'PLUGINS': 1, 'PREFERRED': 1, 'PREFIX-NUMBER': 1,
    'PRINCIPLES': 1, 'PRODUCES': 1, 'PROPOSAL-ONLY': 1, 'PROPOSED': 1, 'PROTOTYPE': 1, 'PROVEN': 1,
    'PUSHED': 1, 'REACHES': 1, 'READ': 1, 'REAL': 2, 'RED': 5, 'REPORTED': 1,
    'RETRACTS': 1, 'RUNNER': 1, 'SAME': 2, 'SCENARIO': 1, 'SCOPED': 2, 'SEARCH': 1,
    'SECOND': 2, "SENDER's": 1, 'SHAPE': 2, 'SILENT': 1, 'SIX': 1, 'SOFT': 1,
    'SOLVED': 1, 'SOURCE': 1, 'SPLITS': 1, 'START': 1, 'STATE': 2, 'STATED': 2,
    'STILL-OPEN': 1, 'STOOD': 1, 'STOP': 1, 'STOPS': 1, 'STORE': 1, 'STRICTLY': 1,
    'SURFACED': 1, 'THE': 1, 'TODAY': 1, 'TOLD': 3, 'TRAIL': 1, 'TRIGGER-FIRED': 1,
    'UNANCHORED': 1, 'UNKNOWN': 1, 'UNTRACKED': 1, 'VISITOR': 1, 'VISUAL': 1, 'WALK': 1,
    'WATCHED': 2, 'WATCHED-line': 1, 'WHAT': 1, 'WHEN': 1, 'WHOLE': 3, 'WIRING': 1,
    'WITH': 4, 'WITHOUT': 1, 'before-a-MINOR': 1, 'say-what-it-IS': 1, 'surface-CLASS': 1, 'when-NOT': 1,
}
CAPS_SWEEP_ADDED = {k.lower() if k != 'ENGLISH' else 'English': v for k, v in CAPS_SWEEP_REMOVED.items()}


def old_text():
    return subprocess.run(["git", "show", "HEAD:TEST_MATRIX.md"], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout


def is_scaffold(line):
    """A table separator or a table HEADER row (first cell 'ID' or 'Artifact') — the reshaped chrome,
    excluded from the content comparison on both sides."""
    s = line.strip()
    if s.startswith("|---"):
        return True
    if s.startswith("|"):
        first = s.strip("|").split("|")[0].strip()
        return first in ("ID", "Artifact")
    return False


def content_region(text, side):
    """The inventory + matrix-rows region, scaffold rows dropped."""
    start = text.index(INVENTORY_HEAD)
    if side == "old":
        end = text.index(COVERAGE_HEAD)
        region = text[start:end]
    else:
        region = REFERENCE_RE.split(text[start:], 1)[0]
    return "\n".join(l for l in region.splitlines() if not is_scaffold(l))


def counts(region):
    return collections.Counter(WORD_RE.findall(region)), collections.Counter(PUNCT_RE.findall(region))


def data_rows(text):
    """The converted five-cell data rows of the new matrix: (n_rows, {status: count})."""
    region = REFERENCE_RE.split(text, 1)[0]
    n = 0
    st = collections.Counter()
    current = False
    for line in region.splitlines():
        if line.startswith("### [node:"):
            current = True
            continue
        if current and re.match(r"^\| [A-Z]+-\d", line):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) == 5:
                n += 1
                st[cells[4].strip().strip("*").strip()] += 1
    return n, st


def main():
    old = old_text()
    new = open(MATRIX, encoding="utf-8").read()

    old_words, old_punct = counts(content_region(old, "old"))
    new_words, new_punct = counts(content_region(new, "new"))

    n_rows, statuses = data_rows(new)
    nB, nT, nR = statuses.get("built", 0), statuses.get("todo", 0), statuses.get("retired", 0)

    # Expected deltas (removed from old / added in new), derived from the converted structure.
    exp_word_removed = collections.Counter({"BUILT": nB, "TODO": nT, "RETIRED": nR})
    exp_word_added = collections.Counter({"built": nB, "todo": nT, "retired": nR})
    exp_word_removed += collections.Counter(CAPS_SWEEP_REMOVED)
    exp_word_added += collections.Counter(CAPS_SWEEP_ADDED)
    exp_word_removed += collections.Counter()  # drop zero entries below
    exp_word_removed = collections.Counter({k: v for k, v in exp_word_removed.items() if v})
    exp_word_added = collections.Counter({k: v for k, v in exp_word_added.items() if v})

    exp_punct_removed = collections.Counter({"|": n_rows})
    exp_punct_added = collections.Counter({"[": n_rows, "]": n_rows, "*": 2 * n_rows})

    word_removed = old_words - new_words
    word_added = new_words - old_words
    punct_removed = old_punct - new_punct
    punct_added = new_punct - old_punct

    word_removed_residual = word_removed - exp_word_removed
    word_added_residual = word_added - exp_word_added
    punct_removed_residual = punct_removed - exp_punct_removed
    punct_added_residual = punct_added - exp_punct_added
    # An expected delta the data did NOT produce is also a failure (under-application).
    word_removed_short = exp_word_removed - word_removed
    word_added_short = exp_word_added - word_added
    punct_removed_short = exp_punct_removed - punct_removed
    punct_added_short = exp_punct_added - punct_added

    residuals = {
        "word tokens removed beyond the named deltas": word_removed_residual,
        "word tokens added beyond the named deltas": word_added_residual,
        "punctuation removed beyond the named deltas": punct_removed_residual,
        "punctuation added beyond the named deltas": punct_added_residual,
        "named word-removal not found in the diff": word_removed_short,
        "named word-addition not found in the diff": word_added_short,
        "named punctuation-removal not found in the diff": punct_removed_short,
        "named punctuation-addition not found in the diff": punct_added_short,
    }
    ok = all(not c for c in residuals.values())

    # Preamble + retired-section token counts, for the named-delta report.
    old_pre_w = len(WORD_RE.findall(old[:old.index(INVENTORY_HEAD)]))
    new_pre_w = len(WORD_RE.findall(new[:new.index(INVENTORY_HEAD)]))
    cov_w = len(WORD_RE.findall(old[old.index(COVERAGE_HEAD):]))
    ref_w = len(WORD_RE.findall(REFERENCE_RE.split(new, 1)[1]))

    lines = []
    lines.append("# Content-preservation proof — row 477 matrix conversion")
    lines.append("")
    lines.append("_This proof covers the mechanical conversion. Run it at conversion time, BEFORE the "
                 "row-477 close flips M-448/M-449/M-450 from todo to built (an intended, separate delta "
                 "that repoints their owning-test cells to the now-existing tests); re-running after that "
                 "flip is expected to show those three rows as a residual and is not a conversion "
                 "defect._")
    lines.append("")
    lines.append("**Verdict: %s**" % ("PASS — every token difference is a declared delta"
                                       if ok else "FAIL — an unexplained token difference remains"))
    lines.append("")
    lines.append("Compared `git show HEAD:TEST_MATRIX.md` (old) against the converted `TEST_MATRIX.md` "
                 "(new), over the inventory + matrix-rows region, word-token multiset and punctuation "
                 "multiset, modulo the named deltas below. Data rows counted: %d (built %d · todo %d · "
                 "retired %d)." % (n_rows, nB, nT, nR))
    lines.append("")
    lines.append("## Named deltas (excluded regions)")
    lines.append("")
    lines.append("- **Preamble rewritten** — excluded from both sides. Old preamble %d word tokens; "
                 "new preamble %d word tokens." % (old_pre_w, new_pre_w))
    lines.append("- **`## Coverage validation` section retired** — excluded from the old side; %d word "
                 "tokens removed with it." % cov_w)
    lines.append("- **Generated `## Reference` section** — excluded from the new side; %d word tokens "
                 "(built by scripts/build-matrix-reference.py, not compared)." % ref_w)
    lines.append("- **Node-block table headers and separators reshaped** — excluded from both sides by "
                 "structure (a separator, or a header row whose first cell is `ID` or `Artifact`).")
    lines.append("")
    lines.append("## Named deltas (reconciled in the compared region)")
    lines.append("")
    lines.append("- **Status lowercased** (word): removed %s; added %s."
                 % ({"BUILT": nB, "TODO": nT, "RETIRED": nR}, {"built": nB, "todo": nT, "retired": nR}))
    lines.append("- **Caps-emphasis sweep** (word): every leftover all-caps emphasis word in the Fact "
                 "cells lowercased (one proper noun, ENGLISH -> English, aside; code anchors, acronyms, "
                 "file names, and id-prefixes excepted) — %d unique tokens, %d occurrences each side; "
                 "full removed/added map is `CAPS_SWEEP_REMOVED`/`CAPS_SWEEP_ADDED` in this script."
                 % (len(CAPS_SWEEP_REMOVED), sum(CAPS_SWEEP_REMOVED.values())))
    lines.append("- **Status italicised** (punctuation): added `*` × %d (two per row)." % (2 * n_rows))
    lines.append("- **Spec-ref moved into the fact sentence, wrapped in one bracket** (punctuation): "
                 "added `[` × %d and `]` × %d; the anchor word tokens are unchanged by the "
                 "move (position move) — proven by the empty word residual below." % (n_rows, n_rows))
    lines.append("- **Row narrowed six cells to five** (punctuation): removed `|` × %d (one per "
                 "row)." % n_rows)
    lines.append("")
    lines.append("## Residuals (must all be empty)")
    lines.append("")
    for name, c in residuals.items():
        lines.append("- %s: %s" % (name, dict(c) if c else "empty"))
    lines.append("")
    report = "\n".join(lines) + "\n"
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(report)

    sys.stdout.write(report)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
