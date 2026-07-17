"""Document rotation — the pack's append-only working docs are split and rotated, and nothing
rotated is lost (SPEC INV-209, ROADMAP rows 390 + 392, the growth/grooming family).

ROADMAP.md, JOURNAL.md, PRODUCT_SPEC.md, and TEST_MATRIX.md grow with every landing until a guard's
scan and a grep run slow (the owner's word, 2026-07-17 ~18:25). So a fully-closed portion of a growable
document rotates out of the live file into a dated archive with a manifest line (base rule 10), the live
file keeping only live material and the archive keeping everything, grepable, so a rotated row stays
findable by its number.

Two machines hold the invariant:
  - scripts/rotate-doc.py         — the mechanism: moves closed rows to a dated archive, leaves the
                                    manifest line in the live file.
  - guardrails/check-doc-rotation.py (gate t) — the net: reds a rotation that DROPS content (a
                                    manifested row found in neither the live file nor its archive) and a
                                    rotation with NO manifest (a rotated-* archive no manifest points to).

This file is red-first: run it against the pre-delta tree and the gate/mechanism are absent, the
spec/index/architecture/matrix carry no INV-209, and the push chain is unwired.
"""
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GATE = os.path.join(ROOT, "guardrails", "check-doc-rotation.py")
ROTATE = os.path.join(ROOT, "scripts", "rotate-doc.py")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def run_gate(base, docs, extra=None):
    """Run the gate over a fixture base dir; return (exit_code, combined_output)."""
    cmd = [sys.executable, GATE, "--base", base]
    for d in docs:
        cmd += ["--doc", d]
    cmd += ["--archive-glob", "rotated-*.md"]
    if extra:
        cmd += extra
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


# ---- fixtures ---------------------------------------------------------------

MANIFEST = (
    "<!-- rotated-manifest -->\n"
    "Rotated closed rows (base rule 10 — nothing lost; the archive keeps everything):\n"
    "- rows 14, 27 → rotated-ROADMAP-2026-07-18.md\n"
    "<!-- /rotated-manifest -->\n"
)


def _live_doc(manifest):
    return (
        "# live-spec Roadmap (dated version: 2026-07-18)\n\n"
        "The wish queue.\n\n"
        + manifest +
        "\n| # | Wish (plain words) | Class | Status | Decision / acceptance |\n"
        "|---|---|---|---|---|\n"
        "| 42 | a live open wish | surface | queued 2026-07-18 | Done when: x |\n"
    )


def _archive(rows):
    head = "> ARCHIVED 2026-07-18 by scripts/rotate-doc.py from ROADMAP.md — nothing lost (base rule 10).\n\n"
    body = "".join(
        "| %d | closed wish %d | small | **landed 2026-07-05** | Done when: met |\n" % (n, n)
        for n in rows
    )
    return head + "| # | Wish | Class | Status | Decision |\n|---|---|---|---|---|\n" + body


def _write(base, name, text):
    with open(os.path.join(base, name), "w", encoding="utf-8") as f:
        f.write(text)


class TestRotationGate(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = tempfile.mkdtemp(prefix="rotation-fixture-")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_gate_ships(self):
        self.assertTrue(os.path.isfile(GATE), "the rotation gate guardrails/check-doc-rotation.py is missing")

    def test_mechanism_ships(self):
        self.assertTrue(os.path.isfile(ROTATE), "the rotation mechanism scripts/rotate-doc.py is missing")

    def test_gate_reds_a_rotation_that_loses_a_row(self):
        # the manifest claims rows 14 and 27 rotated, but the archive holds only 14 — row 27 is
        # present in neither the live file nor the archive: the nothing-lost violation.
        _write(self.tmp, "ROADMAP.md", _live_doc(MANIFEST))
        _write(self.tmp, "rotated-ROADMAP-2026-07-18.md", _archive([14]))
        code, out = run_gate(self.tmp, ["ROADMAP.md"])
        self.assertNotEqual(code, 0, "a rotation that drops row 27 must red")
        self.assertIn("27", out)

    def test_gate_reds_a_rotation_with_no_manifest(self):
        # a rotated-* archive exists but no manifest line in any live doc points to it: the
        # base-rule-10 violation (a superseded portion moved with no manifest line).
        _write(self.tmp, "ROADMAP.md", _live_doc(""))  # no manifest block at all
        _write(self.tmp, "rotated-ROADMAP-2026-07-18.md", _archive([14, 27]))
        code, out = run_gate(self.tmp, ["ROADMAP.md"])
        self.assertNotEqual(code, 0, "an orphan archive with no manifest line must red")
        self.assertIn("rotated-ROADMAP-2026-07-18.md", out)

    def test_gate_reds_a_row_that_is_both_live_and_rotated(self):
        # row 14 is declared rotated yet still present as a live table row — ambiguous, findable
        # twice, the canonical copy unclear.
        live = _live_doc(MANIFEST) + "| 14 | still here | small | **landed 2026-07-05** | Done: met |\n"
        _write(self.tmp, "ROADMAP.md", live)
        _write(self.tmp, "rotated-ROADMAP-2026-07-18.md", _archive([14, 27]))
        code, out = run_gate(self.tmp, ["ROADMAP.md"])
        self.assertNotEqual(code, 0, "a row both live and rotated must red")
        self.assertIn("14", out)

    def test_gate_passes_a_clean_rotation(self):
        # the live file shrank, the archive holds every rotated row, the manifest names them, and no
        # rotated row is still live: a clean rotation passes.
        _write(self.tmp, "ROADMAP.md", _live_doc(MANIFEST))
        _write(self.tmp, "rotated-ROADMAP-2026-07-18.md", _archive([14, 27]))
        code, out = run_gate(self.tmp, ["ROADMAP.md"])
        self.assertEqual(code, 0, "a clean rotation must pass:\n" + out)

    def test_rotated_row_is_findable_by_number_in_the_archive(self):
        # findability: a reader who greps the archive for the row's own `| n |` line finds it.
        _write(self.tmp, "rotated-ROADMAP-2026-07-18.md", _archive([14, 27]))
        arch = open(os.path.join(self.tmp, "rotated-ROADMAP-2026-07-18.md"), encoding="utf-8").read()
        self.assertRegex(arch, r"(?m)^\| 27 \|", "a rotated row must keep its `| n |` line so a grep finds it")

    def test_gate_passes_the_real_tree(self):
        # the repo's own ROADMAP.md after the first rotation must be clean under the gate.
        p = subprocess.run([sys.executable, GATE], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(p.returncode, 0, "the real tree fails the rotation gate:\n" + p.stdout + p.stderr)


class TestMechanism(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = tempfile.mkdtemp(prefix="rotation-mech-")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_rotate_moves_closed_rows_and_leaves_a_manifest(self):
        live = (
            "# live-spec Roadmap (dated version: 2026-07-18)\n\n"
            "The wish queue.\n\n"
            "| # | Wish (plain words) | Class | Status | Decision / acceptance |\n"
            "|---|---|---|---|---|\n"
            "| 14 | closed wish | small | **landed 2026-07-05** | Done when: met |\n"
            "| 42 | open wish | surface | queued 2026-07-18 | Done when: x |\n"
        )
        _write(self.tmp, "ROADMAP.md", live)
        p = subprocess.run(
            [sys.executable, ROTATE, "--doc", "ROADMAP.md", "--rows", "14",
             "--base", self.tmp, "--date", "2026-07-18"],
            capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, "rotate-doc.py failed:\n" + p.stdout + p.stderr)
        new_live = open(os.path.join(self.tmp, "ROADMAP.md"), encoding="utf-8").read()
        self.assertNotRegex(new_live, r"(?m)^\| 14 \|", "the rotated row is still a live table row")
        self.assertRegex(new_live, r"(?m)^\| 42 \|", "the live open row was dropped")
        self.assertIn("rotated-manifest", new_live, "no manifest block left in the live file")
        self.assertIn("14", new_live, "the manifest does not name the rotated row number")
        arch = os.path.join(self.tmp, "docs", "queue-archive", "rotated-ROADMAP-2026-07-18.md")
        self.assertTrue(os.path.isfile(arch), "no archive file written")
        self.assertRegex(open(arch, encoding="utf-8").read(), r"(?m)^\| 14 \|", "rotated row not in the archive")

    def test_rotate_halts_on_a_row_that_is_not_closed(self):
        # safety: a row still open (queued / in-work / deferred / open field leg) is never rotated.
        live = (
            "# live-spec Roadmap (dated version: 2026-07-18)\n\n"
            "| # | Wish (plain words) | Class | Status | Decision / acceptance |\n"
            "|---|---|---|---|---|\n"
            "| 42 | open wish | surface | queued 2026-07-18 | Done when: x |\n"
        )
        _write(self.tmp, "ROADMAP.md", live)
        p = subprocess.run(
            [sys.executable, ROTATE, "--doc", "ROADMAP.md", "--rows", "42",
             "--base", self.tmp, "--date", "2026-07-18"],
            capture_output=True, text=True)
        self.assertNotEqual(p.returncode, 0, "rotating a still-open row must halt, not proceed")

    def test_rotate_output_survives_the_gate(self):
        # the mechanism and the net agree: what rotate-doc.py produces passes check-doc-rotation.py.
        live = (
            "# live-spec Roadmap (dated version: 2026-07-18)\n\n"
            "| # | Wish (plain words) | Class | Status | Decision / acceptance |\n"
            "|---|---|---|---|---|\n"
            "| 14 | closed wish | small | **landed 2026-07-05** | Done when: met |\n"
            "| 27 | closed wish two | small | **decided 2026-07-05** | picked X |\n"
            "| 42 | open wish | surface | queued 2026-07-18 | Done when: x |\n"
        )
        _write(self.tmp, "ROADMAP.md", live)
        subprocess.run(
            [sys.executable, ROTATE, "--doc", "ROADMAP.md", "--rows", "14,27",
             "--base", self.tmp, "--date", "2026-07-18"],
            capture_output=True, text=True, check=True)
        code, out = run_gate(self.tmp, ["ROADMAP.md"],
                             extra=["--archive-glob", "docs/queue-archive/rotated-*.md"])
        self.assertEqual(code, 0, "rotate-doc.py output failed the gate:\n" + out)


# --- wired into the push chain, both nets ---

def test_gate_wired_into_pre_push():
    assert "check-doc-rotation.py" in read("guardrails/pre-push"), \
        "pre-push does not wire the rotation gate (gate t)"


def test_gate_mirrored_in_ci():
    assert "check-doc-rotation.py" in read(".github/workflows/gates.yml"), \
        "the CI mirror does not run the rotation gate"


# --- traceability across the four documents ---

def test_spec_states_the_law():
    spec = read("PRODUCT_SPEC.md")
    assert "[INV-209]" in spec
    assert "check-doc-rotation.py" in spec
    assert "rotate-doc.py" in spec


def test_formal_index_row():
    assert "| INV-209 |" in read("PRODUCT_SPEC.md")


def test_architecture_owns_the_invariant():
    arch = read("ARCHITECTURE.md")
    assert "INV-209" in arch
    assert "check-doc-rotation.py" in arch


def test_matrix_row_covers_the_law():
    matrix = read("TEST_MATRIX.md")
    assert "M-390" in matrix
    assert "INV-209" in matrix


if __name__ == "__main__":
    unittest.main()
