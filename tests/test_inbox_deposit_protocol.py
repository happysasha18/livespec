"""The inbox deposit protocol for concurrent windows — M-434 (SPEC INV-249, ROADMAP 439).

Two windows sharing one repo raced an inbox deposit once: the live-spec receiving sweep deleted a
deposit while the tlvphotos window was still writing it (the truncation is recorded in the deposit's
own body). Writing a file's content is not atomic, so a sweep that reads the inbox mid-write can
harvest or delete a half-written file. The protocol: the sender writes its deposit under a `.draft`
suffix on the lawful name and renames it to the final `from-...md` name in one step once complete — a
rename within one filesystem is atomic, so the final name appears whole or never — and the receiving
sweep acts only on a complete deposit, passing over any `.draft` name and never deleting a mid-write
file. A routed deposit is left earned in place rather than removed under a live writer (INV-247).

This file proves the law's homes: the SPEC clause and Formal-index row, the inbox/README.md protocol
paragraph, the feedback-intake sweep fence, and the owning inbox node in ARCHITECTURE. Against HEAD
118ad87 (pre-delta) none of these exist — recorded in the station's red run.
"""

import unittest

from conftest import read, read_flat


class TestInboxDepositProtocol(unittest.TestCase):
    def test_inv249_spec_clause_stands(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn(
            "A deposit into another window's inbox is written whole under a draft name and made final "
            "by an atomic rename",
            spec,
        )
        self.assertIn("[INV-249]", spec)

    def test_inv249_formal_index_row(self):
        spec = read("PRODUCT_SPEC.md")
        row = next((l for l in spec.splitlines() if l.startswith("| INV-249 |")), "")
        self.assertTrue(row, "INV-249 Formal-index row missing")
        low = row.lower()
        self.assertIn(".draft", low)
        self.assertIn("atomic rename", low)
        self.assertIn("mid-write", low)

    def test_inv249_readme_carries_the_protocol(self):
        """inbox/README.md — the node's own home — states the atomic-write protocol: a deposit is
        written under a .draft name and renamed to its final name only when complete."""
        readme = read_flat("inbox/README.md")
        self.assertIn("INV-249", readme, "inbox/README.md does not carry the deposit protocol")
        self.assertIn(".draft", readme, "inbox/README.md does not name the .draft suffix")
        self.assertIn("written whole before it is named", readme)

    def test_inv249_sweep_fences_the_draft(self):
        """The receiving sweep (feedback-intake) removes only a complete deposit and passes over a
        .draft file a neighbour may still be writing (SPEC INV-249)."""
        fi = read_flat("skills/feedback-intake/SKILL.md")
        self.assertIn("INV-249", fi, "feedback-intake sweep does not fence the mid-write deposit")
        self.assertIn(".draft", fi, "feedback-intake sweep does not name the .draft skip")

    def test_inv249_architecture_owns_the_invariant(self):
        """INV-249 is owned by the inbox node."""
        arch = read("ARCHITECTURE.md")
        owner_line = next((l for l in arch.splitlines()
                           if l.startswith("|") and "INV-249" in l and "| inbox |" in l), "")
        self.assertTrue(owner_line, "the inbox node does not own INV-249 in the Nodes owns-list")

    def test_inv249_matrix_row_covers_the_law(self):
        mat = read("TEST_MATRIX.md")
        row = next((l for l in mat.splitlines() if l.startswith("| M-434 |")), "")
        self.assertTrue(row, "TEST_MATRIX has no M-434 row")
        self.assertIn("INV-249", row)

    def test_inv249_gate_passes_over_a_draft(self):
        """The mechanical earned-message gate (gate m) skips a `.draft` name, so a mid-write deposit
        reds no push and the gate agrees with the sweep (SPEC INV-249). Runs the REAL shipped gate
        against a real mid-write draft fixture and reads its exit code — the same shape the earned-
        message gate tests use."""
        import os
        import subprocess
        import tempfile
        from conftest import ROOT
        gate = os.path.join(ROOT, "guardrails", "check-earned-message.py")
        with tempfile.TemporaryDirectory() as d:
            draft = os.path.join(d, "2026-07-21-from-tlvphotos-payload.md.draft")
            with open(draft, "w", encoding="utf-8") as f:
                f.write("half-written deposit, no Blocked / Lived / Re line yet\n")
            r = subprocess.run(["python3", gate, d], capture_output=True, text=True)
            self.assertEqual(
                r.returncode, 0,
                "the gate red on a .draft mid-write deposit: %s" % (r.stdout + r.stderr))
            self.assertNotIn(".draft", r.stdout, "the gate named a .draft file in its output")


if __name__ == "__main__":
    unittest.main()
