"""Crossing the instance->engine boundary -- provenance and naming (SPEC INV-119, row 276).

A feature usually proves itself first on a live instance and then generalizes into the
engine. When that history goes into the engine's spec, it must read as the engine's own
record: a reconciliation log citing the engine's own public commits, never a private
instance's commit or the instance's own locale label standing as a mechanism name.
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestInstanceEngineBoundary(unittest.TestCase):
    def test_reconciliation_phrase_in_spec(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("how each behaviour landed in code", spec)

    def test_reconciliation_phrase_in_spec_author(self):
        body = read_flat("skills/spec-author/SKILL.md")
        self.assertIn("how each behaviour landed in code", body)

    def test_reconciliation_phrase_in_publish(self):
        body = read_flat("skills/publish/SKILL.md")
        self.assertIn("how each behaviour landed in code", body)

    def test_engine_commit_phrase_in_spec(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("landed in engine commit", spec)

    def test_engine_commit_phrase_in_spec_author(self):
        body = read_flat("skills/spec-author/SKILL.md")
        self.assertIn("landed in engine commit", body)

    def test_engine_commit_phrase_in_publish(self):
        body = read_flat("skills/publish/SKILL.md")
        self.assertIn("landed in engine commit", body)

    def test_proven_first_phrase_in_spec(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("proven first on a live instance", spec)

    def test_proven_first_phrase_in_spec_author(self):
        body = read_flat("skills/spec-author/SKILL.md")
        self.assertIn("proven first on a live instance", body)

    def test_proven_first_phrase_in_publish(self):
        body = read_flat("skills/publish/SKILL.md")
        self.assertIn("proven first on a live instance", body)

    def test_spec_anchor(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-119]", spec)

    def test_spec_anchor_and_index(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-119 |") and "INV-119" in line and "engine" in line.lower():
                    return
        self.fail("INV-119 index row missing or does not carry both INV-119 and 'engine'")


if __name__ == "__main__":
    unittest.main()
