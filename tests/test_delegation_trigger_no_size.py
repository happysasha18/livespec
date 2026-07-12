"""No pack skill states a size/time numeric delegation trigger — the trigger is judgment vs mechanical,
size a weak hint only (base rule 5, SPEC INV-69) — M-277 (row 295).

Base rule 5 settled the delegation trigger — "the trigger is judgment against mechanical ... Size is a
weak hint only, never the decider" — and INV-69's routing rule reads the STEP and kind of the work "beyond
the row's size alone". Row 262 consolidated the delegation accounting, but a divergent numeric trigger
SURVIVED in build-pipeline's junior-delegation passage — an operative "delegate when ≥1 holds — >3 files
touched/read ... a script/suite runs >~30s ..." that contradicted base rule 5 and INV-69. This guard
scans every pack SKILL.md for that superseded shape: a comparison threshold on a file count or a running
time used as a delegation trigger ('>3 files', '>~30s'), or the 'N files touched/read' file-count trigger.
It keys on the threshold SHAPE (the `>` operator, or the touched/read trigger vocabulary), so prose that
merely mentions the demoted proxy while pointing at INV-69 — "size is a weak hint only, never the decider"
— never trips it, and a benign "scan in 30 seconds" or "~8 files to edit" is not a threshold trigger.

Red-proven against the pre-fix build-pipeline text (the surviving numeric trigger); green once the passage
states delegation only as the judgment-vs-mechanical test pointing at base rule 5 / INV-69 as its home.
"""

import glob
import os
import re
import unittest

from conftest import ROOT

# The superseded delegation-trigger shapes. Each keys on structure a benign mention cannot wear:
#  - a `>` comparison threshold on a file count or a running time (">3 files", ">~30s") — an operative bar;
#  - the "N files touched/read" file-count phrasing — the trigger's own vocabulary.
# A sentence that only demotes the proxy ("size is a weak hint only, never the decider") carries no
# threshold and no touched/read count, so it passes; "scan in 30 seconds" / "~8 files to edit" carry no
# `>` operator, so they pass too.
TRIGGER_PATTERNS = [
    (re.compile(r">\s*~?\s*\d+\s*(?:files?\b|s\b|sec\b|seconds?\b|min\b|minutes?\b)", re.IGNORECASE),
     "a `>` threshold on files/time used as a delegation trigger (e.g. '>3 files', '>~30s')"),
    (re.compile(r"\b\d+\s+files\s+(?:touched|read)\b", re.IGNORECASE),
     "a file-count delegation trigger ('N files touched/read')"),
]


def _pack_skill_files():
    return sorted(glob.glob(os.path.join(ROOT, "skills", "**", "SKILL.md"), recursive=True))


class TestDelegationTriggerNoSize(unittest.TestCase):
    def test_no_pack_skill_states_a_size_or_time_delegation_trigger(self):
        files = _pack_skill_files()
        self.assertTrue(files, "no pack SKILL.md files found to scan")
        hits = []
        for path in files:
            with open(path, encoding="utf-8") as f:
                for lineno, line in enumerate(f, 1):
                    for rx, why in TRIGGER_PATTERNS:
                        if rx.search(line):
                            rel = os.path.relpath(path, ROOT)
                            hits.append("%s:%d — %s :: %s" % (rel, lineno, why, line.strip()[:90]))
        self.assertEqual(
            hits, [],
            "a pack skill states a superseded size/time delegation trigger — base rule 5 / INV-69 make "
            "the trigger judgment-vs-mechanical, size a weak hint only:\n" + "\n".join(hits),
        )

    def test_scan_has_teeth(self):
        """The never side, permanent: the scan catches the trigger shapes and spares the demoted-proxy
        sentence and the benign numeric prose."""
        def flagged(text):
            return any(rx.search(text) for rx, _ in TRIGGER_PATTERNS)

        # the superseded trigger shapes are caught
        self.assertTrue(flagged("delegate when >3 files touched/read for facts"),
                        "the scan missed the '>3 files' size trigger")
        self.assertTrue(flagged("a known script/suite runs >~30s"),
                        "the scan missed the '>~30s' time trigger")
        self.assertTrue(flagged("3 files touched or read decides it"),
                        "the scan missed the 'N files touched/read' trigger")
        # the demoted-proxy sentence and benign numeric prose are spared
        self.assertFalse(flagged("Size is a weak hint only, never the decider (base rule 5, INV-69)."),
                         "the scan false-flagged the demoted-proxy sentence")
        self.assertFalse(flagged("notes easy to scan in 30 seconds, read carefully in 5 minutes"),
                         "the scan false-flagged benign '30 seconds' prose")
        self.assertFalse(flagged("the brief is SIZED — at most ~8 files to edit [default]"),
                         "the scan false-flagged the benign '~8 files to edit' SIZED prose")


if __name__ == "__main__":
    unittest.main(verbosity=2)
