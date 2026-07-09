"""Bootstrap suite scaffold (live-spec B-1) — the host's FIRST runnable suite.

Copy this file to `tests/test_scaffold.py` at bootstrap, together with the six document templates.
Run from the project root:  python3 -m unittest discover tests

This is what "green suite" MEANS for landing #1: the document set is present and filled (headers
dated, the coverage checklist in place, one live-state block) — i.e., the bootstrap itself is
complete. It is a floor, not a ceiling: landing #1 ships its own first real test beside this file,
and the traceability checks grow from here (the pack's own tests/test_traceability.py is the worked
example of where this scaffold is headed).
"""

import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOCS = ("PRODUCT_SPEC.md", "ARCHITECTURE.md", "TEST_MATRIX.md", "ROADMAP.md", "JOURNAL.md", "NEXT_STEPS.md")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


class TestBootstrapComplete(unittest.TestCase):
    def test_document_set_present(self):
        for doc in DOCS:
            path = os.path.join(ROOT, doc)
            self.assertTrue(os.path.isfile(path), "bootstrap doc missing: %s" % doc)
            self.assertGreater(os.path.getsize(path), 100, "%s is an empty shell" % doc)

    def test_headers_filled_not_placeholders(self):
        spec_head = read("PRODUCT_SPEC.md").splitlines()[0]
        self.assertRegex(spec_head, r"\(v[\d.]+, \d{4}-\d{2}-\d{2}\)",
                         "SPEC header must carry a real version + date, not the template placeholder")
        for doc in DOCS:
            head = read(doc).splitlines()[0]
            self.assertNotIn("[Project Name]", head,
                             "%s still carries the template placeholder name" % doc)

    def test_matrix_carries_coverage_validation(self):
        self.assertIn("Coverage validation", read("TEST_MATRIX.md"),
                      "TEST_MATRIX lost the coverage-validation checklist (E-15)")

    def test_queue_is_a_table(self):
        body = read("ROADMAP.md")
        self.assertIn("| # |", body, "ROADMAP lost its queue table header")

    def test_next_steps_single_live_state(self):
        blocks = re.findall(r"(?im)^#+ .*live state", read("NEXT_STEPS.md"))
        self.assertLessEqual(len(blocks), 1, "LIVE STATE blocks must be replaced, never stacked")


if __name__ == "__main__":
    unittest.main(verbosity=2)
