"""The Formal-index non-empty description-field gate (SPEC INV-239, M-421; E-35/INV-239, M-423).

The named-reference pair gives every registered code a plain one-sentence description, and that
description's one home is a dedicated field the Formal index gains [E-35, base rule 4]. This suite
covers the mechanical presence net over that field — `guardrails/check-description-field.py` — and
the field's own existence in the shipped index.

Two facts sit under one owning test file, as the matrix rows say (M-421 the gate, M-423 the field):
the gate reds a registered code whose description field is empty and passes one that carries a
description, judging PRESENCE alone and never whether the description reads well or matches the item
(that semantic read is the human sampling net, INV-41); and it ships DORMANT — the existing code set
carries no rich descriptions yet (the back-describe migration is a future his-gated landing, INV-217,
folded finding N5), so an armed gate would red the whole tree, and the gate stays down until the
migration arms it through `guardrails/description-field.json`.

Every armed/dormant case drives the real shipped script over a FIXTURE Formal-index snippet and a
FIXTURE config, so the real `guardrails/description-field.json` is never flipped and the real tree
stays green under the dormant ship.
"""
import json
import os
import re
import subprocess
import tempfile
import unittest

from conftest import ROOT, read, read_flat

GATE = os.path.join(ROOT, "guardrails", "check-description-field.py")


def run_gate(spec_path=None, config_path=None):
    """Drive the shipped gate, pointing it at a fixture spec and/or a fixture config.

    Returns the CompletedProcess; the gate prints its finding to stdout and carries its verdict in
    the exit code (0 clean or dormant, non-zero on a red), the file-read-and-exit-code level the
    sibling index gates take [M-399, M-400].
    """
    env = dict(os.environ)
    if spec_path is not None:
        env["DESCRIPTION_FIELD_SPEC"] = spec_path
    if config_path is not None:
        env["DESCRIPTION_FIELD_CONFIG"] = config_path
    return subprocess.run(["python3", GATE], env=env, capture_output=True, text=True)


def write(tmp, name, text):
    path = os.path.join(tmp, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


# A Formal-index snippet carrying the description field the migration adds — a dedicated Description
# column. INV-1 carries its description; INV-2's field is empty (the seeded red).
INDEX_WITH_EMPTY = """\
## Formal index

| Anchor | One line | Description | Section |
|---|---|---|---|
| INV-1 | no wish lost | Every wish a person throws reaches a recorded terminal state. | Throwing a wish |
| INV-2 | queue rows |  | Machines |
"""

# The same shape with every description present — the seeded green.
INDEX_ALL_DESCRIBED = """\
## Formal index

| Anchor | One line | Description | Section |
|---|---|---|---|
| INV-1 | no wish lost | Every wish a person throws reaches a recorded terminal state. | Throwing a wish |
| INV-2 | queue rows | Every wish is a row in the queue, so no request is tracked by memory. | Machines |
"""

# A row that OMITS its Description cell — three cells where the header names four. A header→cell zip
# would slide the multi-word Section text into the description slot and false-pass; the short-row
# guard must red it instead.
INDEX_OMITTED_CELL = """\
## Formal index

| Anchor | One line | Description | Section |
|---|---|---|---|
| INV-1 | no wish lost | Every wish a person throws reaches a recorded terminal state. | Throwing a wish |
| INV-2 | queue rows | When agents work together |
"""

# A row whose Description is a single character — present in the cell but no real description. The
# presence floor (at least two plain words, the floor the deposit lint shares) must red it.
INDEX_ONE_CHAR = """\
## Formal index

| Anchor | One line | Description | Section |
|---|---|---|---|
| INV-1 | no wish lost | Every wish a person throws reaches a recorded terminal state. | Throwing a wish |
| INV-2 | queue rows | x | Machines |
"""

ARMED = json.dumps({"armed": True, "reason": "test fixture — armed"})
DORMANT = json.dumps({"armed": False, "reason": "test fixture — dormant"})


class TestDescriptionFieldGate(unittest.TestCase):
    """M-421: the presence gate reds an empty description field and passes a carried one, and stays
    dormant until the back-describe migration arms it."""

    def test_gate_ships(self):
        self.assertTrue(os.path.isfile(GATE), "the gate script does not ship: %s" % GATE)
        self.assertTrue(os.access(GATE, os.X_OK) or GATE.endswith(".py"),
                        "the gate is not runnable")

    def test_gate_reds_a_code_with_an_empty_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            spec = write(tmp, "spec.md", INDEX_WITH_EMPTY)
            cfg = write(tmp, "cfg.json", ARMED)
            r = run_gate(spec, cfg)
            self.assertNotEqual(r.returncode, 0,
                                "the armed gate passed a code with an empty description field:\n%s" % r.stdout)
            self.assertIn("INV-2", r.stdout, "the red does not name the offending code")

    def test_gate_passes_a_code_that_carries_a_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            spec = write(tmp, "spec.md", INDEX_ALL_DESCRIBED)
            cfg = write(tmp, "cfg.json", ARMED)
            r = run_gate(spec, cfg)
            self.assertEqual(r.returncode, 0,
                             "the armed gate red a fully described index:\n%s" % r.stdout)

    def test_gate_reds_a_code_that_omits_its_description_cell(self):
        # A row shorter than the header omits a cell — a missing description, red exactly like an empty
        # one. Parsing by column index alone would slide the Section text into the description slot and
        # false-pass; the short-row guard reds it and names the code.
        with tempfile.TemporaryDirectory() as tmp:
            spec = write(tmp, "spec.md", INDEX_OMITTED_CELL)
            cfg = write(tmp, "cfg.json", ARMED)
            r = run_gate(spec, cfg)
            self.assertNotEqual(r.returncode, 0,
                                "the armed gate passed a row that omits its description cell:\n%s" % r.stdout)
            self.assertIn("INV-2", r.stdout, "the red does not name the code with the omitted cell")

    def test_gate_reds_a_one_character_description(self):
        # The presence floor is at least two plain words — the floor the deposit lint shares — so a
        # single-character cell is not a description. Presence only, never a correctness read.
        with tempfile.TemporaryDirectory() as tmp:
            spec = write(tmp, "spec.md", INDEX_ONE_CHAR)
            cfg = write(tmp, "cfg.json", ARMED)
            r = run_gate(spec, cfg)
            self.assertNotEqual(r.returncode, 0,
                                "the armed gate passed a one-character description:\n%s" % r.stdout)
            self.assertIn("INV-2", r.stdout, "the red does not name the thinly-described code")

    def test_gate_stays_dormant_until_the_migration_arms_it(self):
        # A tree whose description fields are empty (every code) — armed this reds the whole tree, so
        # the dormant ship must exit 0 on exactly this tree, proving the arming guard, not luck.
        with tempfile.TemporaryDirectory() as tmp:
            spec = write(tmp, "spec.md", INDEX_WITH_EMPTY)
            cfg = write(tmp, "cfg.json", DORMANT)
            r = run_gate(spec, cfg)
            self.assertEqual(r.returncode, 0,
                             "the dormant gate did not stand down on a tree with empty fields:\n%s" % r.stdout)
            self.assertIn("dormant", r.stdout.lower(), "the dormant gate does not say it stood down")

    def test_gate_judges_presence_not_semantic_match(self):
        # A description that is present but plainly wrong for the code (a mismatch) still PASSES: the
        # gate judges presence alone, the semantic read belonging to the human net [INV-41].
        mismatched = INDEX_ALL_DESCRIBED.replace(
            "Every wish is a row in the queue, so no request is tracked by memory.",
            "This sentence has nothing to do with the queue and is simply wrong for the code.")
        with tempfile.TemporaryDirectory() as tmp:
            spec = write(tmp, "spec.md", mismatched)
            cfg = write(tmp, "cfg.json", ARMED)
            r = run_gate(spec, cfg)
            self.assertEqual(r.returncode, 0,
                             "the gate reached past presence into a semantic match:\n%s" % r.stdout)

    def test_real_config_ships_dormant(self):
        # The real shipped config must ship dormant, so the real tree and the push chain stay green
        # until the his-gated migration flips it (INV-217, folded finding N5).
        cfg = json.loads(read("guardrails/description-field.json"))
        self.assertFalse(cfg["armed"],
                         "the real description-field.json ships ARMED — it must stay dormant until the "
                         "back-describe migration lands")
        self.assertTrue(cfg.get("reason", "").strip(), "the config states no reason for its arming state")

    def test_dormant_on_the_real_tree(self):
        # No env override: the gate reads the real config (dormant) and the real spec, and exits 0.
        # This is the gate's ENFORCEMENT ride: the suite runs it against the real tree, so a real
        # violation would red the suite (gate b) and block the push — the gate takes no push letter.
        r = run_gate()
        self.assertEqual(r.returncode, 0,
                         "the gate does not stand down on the real dormant tree:\n%s\n%s"
                         % (r.stdout, r.stderr))

    def test_gate_not_wired_into_pre_push(self):
        # It rides the suite (gate b) and takes NO push-gate letter, so it is never invoked from the
        # pre-push chain or the CI mirror directly (the far-tier placement).
        self.assertNotIn("check-description-field", read("guardrails/pre-push"),
                         "the gate is invoked in pre-push — it must ride the suite, not take a letter")
        self.assertNotIn("check-description-field", read(".github/workflows/gates.yml"),
                         "the gate has its own CI step — it must ride the suite pytest step")


class TestDescriptionFieldTraceability(unittest.TestCase):
    """M-421/M-423 doc-structural checks: the law stands in the spec, the Formal index, and the
    architecture (the traceability quartet), and the field's own existence in the shipped index."""

    def test_spec_states_the_law(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("dedicated description field the Formal index gains", spec,
                      "SPEC lost the description-field law (INV-239/E-35)")
        self.assertIn("reds a code whose description field is empty", spec,
                      "SPEC lost the presence-net statement of the gate")
        self.assertIn("this gate arms in the same landing that back-describes", spec.lower().replace("this", "this"),
                      "SPEC lost the dormant-until-migration arming clause")

    def test_formal_index_row(self):
        spec = read("PRODUCT_SPEC.md")
        index = spec.split("## Formal index", 1)[1]
        self.assertRegex(index, r"\|\s*INV-239\s*\|", "the Formal index carries no INV-239 row")

    def test_architecture_owns_the_invariant(self):
        arch = read_flat("ARCHITECTURE.md")
        self.assertIn("check-description-field.py", arch,
                      "ARCHITECTURE does not own the description-field gate under its guardrails node")
        self.assertIn("INV-239", arch, "ARCHITECTURE lost the INV-239 anchor")

    def test_matrix_row_covers_the_law(self):
        matrix = read("TEST_MATRIX.md")
        self.assertRegex(matrix, r"\|\s*M-421\s*\|", "TEST_MATRIX lost the M-421 row")
        self.assertIn("check-description-field.py", matrix, "M-421 row does not name the gate script")

    def test_index_shape_carries_a_description_field(self):
        # M-423: every registered code has one home for its human-clear line in the Formal index — a
        # bare code never stands alone before a reader. Today that home is the index's per-code "One
        # line" column, and it carries a non-empty cell for every registered code. The back-describe
        # migration ADDS a NEW, separate `Description` column (the fuller E-35 one-sentence bar) while
        # the terse "One line" stays the machine handle's home; the gate arms on that new column then.
        # This test asserts the home that exists now — the "One line" column — is present and full.
        spec = read("PRODUCT_SPEC.md")
        index = spec.split("## Formal index", 1)[1]
        header = next((ln for ln in index.splitlines() if ln.strip().startswith("| Anchor")), None)
        self.assertIsNotNone(header, "the Formal index has no header row")
        cols = [c.strip().lower() for c in header.strip().strip("|").split("|")]
        self.assertIn("one line", cols,
                      "the Formal index lost its per-code description home (the 'One line' column)")
        desc_col = cols.index("one line")
        rows = re.findall(r"^\|.*\|$", index, re.M)
        bare = []
        for row in rows:
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) <= desc_col:
                continue
            anchor = cells[0]
            if not re.fullmatch(r"[A-Z]+-[0-9]+(?:\.\.[A-Z]*-?[0-9]+)?", anchor):
                continue
            if not cells[desc_col]:
                bare.append(anchor)
        self.assertEqual(bare, [], "registered codes standing in the index with no one-line home: %s" % bare)

    def test_e35_formal_index_row(self):
        spec = read("PRODUCT_SPEC.md")
        index = spec.split("## Formal index", 1)[1]
        self.assertRegex(index, r"\|\s*E-35\s*\|", "the Formal index carries no E-35 row")

    def test_architecture_owns_e35_under_base_rulebook(self):
        arch = read_flat("ARCHITECTURE.md")
        self.assertIn("E-35", arch, "ARCHITECTURE lost the E-35 anchor")
        # E-35 is owned by the base-rulebook node (the named-reference machinery's family home).
        self.assertRegex(arch, r"base-rulebook[^|]*E-35",
                         "E-35 is not owned under the base-rulebook node in ARCHITECTURE")


if __name__ == "__main__":
    unittest.main()
