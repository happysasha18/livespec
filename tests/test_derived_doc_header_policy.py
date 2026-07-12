"""Derived-doc header version policy — row 265 (SPEC M-7; the no-drifting-version-in-prose rule).

A derived doc (ARCHITECTURE.md, TEST_MATRIX.md) is derived from PRODUCT_SPEC.md. Its header used to
pin a frozen spec-version number — ARCHITECTURE.md read "v0.3.0", TEST_MATRIX.md read "v0.1" — which
went stale against a spec well past v1.0 and read wrong to a reader. Policy: a derived-doc header
carries no frozen spec-version number; it names what it derives from, points at the version's one
home (VERSION), and carries a dated "Last reconciled" provenance line instead. This lint keeps the
two headers in step with that policy.
"""

import os
import re
import unittest

from conftest import ROOT

DERIVED = ("ARCHITECTURE.md", "TEST_MATRIX.md")
# a frozen spec-version pin in the header: "(v0.3.0, 2026-07-09)" or "(v0.1, 2026-07-05)"
FROZEN_PIN = re.compile(r"\(v\d+\.\d+[^)]*\d{4}-\d\d-\d\d\)")


def header(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return "".join(f.readline() for _ in range(6))


class TestDerivedDocHeaderPolicy(unittest.TestCase):
    def test_no_frozen_version_pin_in_header(self):
        for rel in DERIVED:
            self.assertIsNone(
                FROZEN_PIN.search(header(rel)),
                f"{rel} header still pins a frozen (version, date) that reads stale — "
                f"point at VERSION and carry a Last-reconciled date instead (row 265)",
            )

    def test_header_points_at_version_and_reconcile_date(self):
        for rel in DERIVED:
            h = header(rel)
            self.assertIn("VERSION", h, f"{rel} header must point at the version's one home")
            self.assertIn("Last reconciled", h, f"{rel} header must carry a Last-reconciled date")


if __name__ == "__main__":
    unittest.main()
