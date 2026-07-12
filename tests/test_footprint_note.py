"""Every landed feature-or-refactor row carries its footprint note, and a suite check reads the queue — M-275 (SPEC INV-134, row 291).

INV-128 (row 259) states the three-source footprint read and defers the mechanical enforcement to the
follow-on rows. This is that enforcement — the mechanical floor under the footprint read, built to the
same shape the delegation-accounting check (INV-103) gives the routing rule. Beyond the string needles on
the law's homes, the ROADMAP scan is the check itself: a feature-or-refactor row landed once the
impact-analysis station was law (2026-07-12 ~17:01, when INV-128 landed) must carry a `footprint:` note.
Rows that landed before the read was law stay as they landed.
"""

import os
import re
import unittest

from conftest import ROOT, read_flat

# Capture the landed date and, when present, the ~HH:MM time-of-day of the stamp.
LANDED = re.compile(r"\*\*landed (20\d\d-\d\d-\d\d)(?:[^|]*?~(\d\d):(\d\d))?", re.IGNORECASE)
DOOR = re.compile(r"door:\s*([a-z-]+)", re.IGNORECASE)
# The note itself — `footprint: <value>` — not the bare word, which prose uses freely.
FOOTPRINT_NOTE = re.compile(r"footprint:\s*(presentation-only|single-module|cross-cutting)", re.IGNORECASE)
BINDS_FROM_DATE = "2026-07-12"      # the day the footprint read became law
BINDS_FROM_TIME = (17, 1)          # INV-128 (row 259) landed ~17:01 that day
ENFORCED_DOORS = ("feature", "refactor")


def _required(date, hm):
    """A feature-or-refactor row owes a footprint note once the impact-analysis
    station was law. Later dates always owe it; on the cutoff day only rows stamped
    at or after INV-128's landing time owe it (rows before it predate the read)."""
    if date > BINDS_FROM_DATE:
        return True
    if date == BINDS_FROM_DATE and hm is not None and hm >= BINDS_FROM_TIME:
        return True
    return False


class TestFootprintNoteLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md",)

    def test_law_in_the_spec(self):
        spec = read_flat("PRODUCT_SPEC.md")
        for needle in (
            "A landed feature-or-refactor row carries its footprint note, and a suite check holds it",
            "a landed feature-or-refactor row without a footprint note goes red",
            "the mechanical floor under the footprint read",
            "[INV-134]",
        ):
            self.assertIn(needle, spec, "SPEC INV-134 lost the enforcement clause: %s" % needle)

    def test_spec_index_row(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-134 |"):
                    self.assertIn("footprint", line.lower())
                    return
        self.fail("INV-134 Formal-index row missing")

    def test_roadmap_template_carries_the_footprint_field(self):
        tmpl = read_flat("templates/ROADMAP.template.md")
        self.assertIn("footprint", tmpl.lower(),
                      "the ROADMAP row template does not name the footprint field")
        for fp in ("presentation-only", "single-module", "cross-cutting"):
            self.assertIn(fp, tmpl, "template lost the footprint value: %s" % fp)

    def test_capture_echo_carries_the_footprint_field(self):
        cm = read_flat("skills/communicator/SKILL.md")
        self.assertIn("the footprint the three-source read named", cm,
                      "communicator's capture echo (rule 12) lost the footprint field")

    def test_every_forward_landed_feature_row_carries_the_note(self):
        checked = 0
        with open(os.path.join(ROOT, "ROADMAP.md"), encoding="utf-8") as f:
            for line in f:
                m = LANDED.search(line)
                if not m:
                    continue
                date = m.group(1)
                hm = (int(m.group(2)), int(m.group(3))) if m.group(2) else None
                cells = line.split("|")
                status = next((c for c in cells if re.search("landed", c, re.IGNORECASE)), "")
                d = DOOR.search(status)
                door = d.group(1).lower() if d else ""
                if door not in ENFORCED_DOORS:
                    continue
                if not _required(date, hm):
                    continue
                self.assertRegex(
                    status,
                    FOOTPRINT_NOTE,
                    "landed-forward feature/refactor row missing its footprint note: " + line[:70],
                )
                checked += 1
        self.assertGreater(checked, 0, "no forward-landed feature/refactor rows found to scan")


if __name__ == "__main__":
    unittest.main()
