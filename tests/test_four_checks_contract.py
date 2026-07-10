"""The four host checks' shipping contract — matrix row M-226 (SPEC INV-97, row 241).

The web session's curator read, 2026-07-10: the pipeline's four teeth (completeness,
tests-present, behaviour-traces-to-spec, conflicts) ship as generic runnable code a host
attaches by ONE config file — honest failure modes, adopt-walk attachment, the pack repo
as the first host. This test pins the CONTRACT's presence; the checks' own function-level
rows land with their code (the row 241 build).
"""

import os
import subprocess
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


class TestFourChecksContract(unittest.TestCase):
    def test_contract_in_the_spec(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn("code a host attaches, never prose it re-implements", spec)
        self.assertIn("parametrized by one host config file", spec)
        self.assertIn("a missing config is red with an attach-me line, never a silent pass", spec)

    def test_waivers_are_declared(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn("an undeclared gap never passes quietly", spec)

    def test_acceptance_is_measured(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn("each check proves itself red-first on one planted defect", spec)

    def test_spec_anchor_and_index(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn("[INV-97]", spec)
        self.assertIn("| INV-97 |", spec)


if __name__ == "__main__":
    unittest.main()
