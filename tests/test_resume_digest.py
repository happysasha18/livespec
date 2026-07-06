"""Row 115 (M-146, INV-48): the resume file is a digest with a hard cap —
the whole NEXT_STEPS.md holds at most 100 lines; detail flows to the journal
and queue rows it points at; an open leg is never dropped, only stated tersely."""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAP = 100


def over_cap(text, cap=CAP):
    return len(text.splitlines()) > cap


class TestResumeDigestCap(unittest.TestCase):
    def test_resume_digest_cap(self):
        with open(os.path.join(ROOT, "NEXT_STEPS.md"), encoding="utf-8") as f:
            lines = f.read().splitlines()
        self.assertLessEqual(
            len(lines), CAP,
            "NEXT_STEPS.md is %d lines — over the %d-line digest cap (SPEC INV-48): "
            "move detail to the journal/queue rows; restate each open leg as one terse "
            "line; never drop a leg" % (len(lines), CAP))

    def test_resume_cap_catches_synthetic_bloat(self):
        bloated = "\n".join("line %d" % i for i in range(120))
        self.assertTrue(over_cap(bloated), "a 120-line synthetic file must be over the cap")
        self.assertFalse(over_cap("\n".join("l" for _ in range(50))),
                         "a 50-line file must be under the cap")

    def test_template_states_the_cap(self):
        with open(os.path.join(ROOT, "templates", "NEXT_STEPS.template.md"),
                  encoding="utf-8") as f:
            t = f.read()
        self.assertIn("100 lines", t,
                      "the template must state the digest cap (SPEC INV-48)")
