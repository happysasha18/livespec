"""Traceability suite — the coverage validation of TEST_MATRIX.md, mechanized (SPEC E-14/E-15/INV-15).

Zero dependencies; run from the repo root:  python3 -m unittest discover tests -v
Every check here asserts the SHIPPED files on disk, never a source fragment or a memory of one.
This is the first slice of the guardrails' conflicts check (ROADMAP rows 3 and 12's gap 3 territory);
the pre-push hook generalizes it when row 3 lands.
"""

import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def expand(anchor):
    """T-1..T-7 -> [T-1 ... T-7]; plain anchors pass through."""
    m = re.match(r"([A-Z]+)-(\d+)\.\.(?:[A-Z]+-)?(\d+)$", anchor)
    if m:
        prefix, lo, hi = m.group(1), int(m.group(2)), int(m.group(3))
        return ["%s-%d" % (prefix, i) for i in range(lo, hi + 1)]
    return [anchor]


ANCHOR_TOKEN = r"[A-Z]+-[0-9]+(?:\.\.[A-Z]*-?[0-9]+)?"


def spec_index_anchors():
    """Anchors from SPEC.md's Formal index table, ranges expanded."""
    spec = read("SPEC.md")
    raw = re.findall(r"^\| (%s) \|" % ANCHOR_TOKEN, spec, re.M)
    out = set()
    for a in raw:
        out.update(expand(a))
    return raw, out


def architecture_nodes():
    """{node name: set of owned anchors} from ARCHITECTURE.md's Nodes table."""
    arch = read("ARCHITECTURE.md")
    nodes = {}
    in_nodes = False
    for line in arch.splitlines():
        if line.startswith("## Nodes"):
            in_nodes = True
            continue
        if in_nodes and line.startswith("## "):
            break
        if in_nodes and line.startswith("|") and not line.startswith("|---") and "Responsibility" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) == 4:
                owned = set()
                for tok in re.findall(ANCHOR_TOKEN, cells[1]):
                    pass  # responsibility column may mention rows; anchors come from column 3 only
                for tok in re.findall(ANCHOR_TOKEN, cells[2]):
                    owned.update(expand(tok))
                nodes[cells[0]] = owned
    return nodes


def matrix_blocks():
    """{block node name: [row dicts]} from TEST_MATRIX.md."""
    mat = read("TEST_MATRIX.md")
    blocks = {}
    current = None
    for line in mat.splitlines():
        m = re.match(r"^### \[node: (.*)\]\s*$", line)
        if m:
            current = m.group(1)
            blocks[current] = []
            continue
        if current and line.startswith("|") and not line.startswith("|---") and "Owning test" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) == 6:
                refs = set()
                for tok in re.findall(ANCHOR_TOKEN, cells[2]):
                    refs.update(expand(tok))
                blocks[current].append(
                    {"id": cells[0], "fact": cells[1], "refs": refs,
                     "level": cells[3], "owning": cells[4], "status": cells[5]}
                )
    return blocks


def inventory_entries():
    """[(path, is_dir)] from the Artifact inventory table."""
    mat = read("TEST_MATRIX.md")
    section = mat.split("## Artifact inventory", 1)[1].split("## Matrix rows", 1)[0]
    entries = []
    for m in re.finditer(r"^\|[^|]+\| `([^`]+)` \|", section, re.M):
        path = m.group(1)
        entries.append((path, path.endswith("/")))
    return entries


class TestSpecIndex(unittest.TestCase):
    def test_spec_index_unique_anchors(self):
        raw, _ = spec_index_anchors()
        dupes = [a for a in set(raw) if raw.count(a) > 1]
        self.assertEqual(dupes, [], "duplicate anchor ids in the Formal index")
        self.assertGreater(len(raw), 40, "index suspiciously small — parser broke or index truncated")

    def test_spec_decide_markers_match_open(self):
        spec = read("SPEC.md")
        _, index = spec_index_anchors()
        d_anchors = {a for a in index if a.startswith("D-")}
        open_section = spec.split("## Open decisions", 1)[1].split("## Formal index", 1)[0]
        for line_group in re.split(r"\n- ", open_section):
            if "⟨DECIDE⟩" in line_group:
                cited = set(re.findall(r"\[?(D-\d+)\]?", line_group))
                self.assertTrue(cited & d_anchors,
                                "a ⟨DECIDE⟩ entry cites no D-anchor from the index: %r" % line_group[:80])
                self.assertNotIn("Decided", line_group.split("⟨DECIDE⟩")[0],
                                 "an entry is both Decided and ⟨DECIDE⟩-open")
        for d in sorted(d_anchors):
            self.assertIn(d, open_section, "index D-anchor %s missing from Open decisions" % d)


class TestArchitecture(unittest.TestCase):
    def test_architecture_owns_every_anchor_once(self):
        _, index = spec_index_anchors()
        nodes = architecture_nodes()
        owners = {}
        for node, owned in nodes.items():
            for a in owned:
                owners.setdefault(a, []).append(node)
        missing = sorted(a for a in index if a not in owners)
        dupes = {a: ns for a, ns in owners.items() if len(ns) > 1}
        stale = sorted(a for a in owners if a not in index)
        self.assertEqual(missing, [], "index anchors with no owning node")
        self.assertEqual(dupes, {}, "anchors owned by more than one node")
        self.assertEqual(stale, [], "owned anchors absent from the index")

    def test_architecture_no_orphan_nodes(self):
        nodes = architecture_nodes()
        self.assertGreaterEqual(len(nodes), 10, "nodes table parse failure")
        orphans = [n for n, owned in nodes.items() if not owned]
        self.assertEqual(orphans, [], "nodes owning no spec fact (no spec backing)")

    def test_architecture_pins_exist(self):
        arch = read("ARCHITECTURE.md")
        section = arch.split("## Nodes", 1)[1].split("## Seams", 1)[0]
        pins = re.findall(r"`([\w./-]+):(\d+)`", section)
        self.assertGreater(len(pins), 10, "pin parse failure")
        for path, line_no in pins:
            full = os.path.join(ROOT, path)
            self.assertTrue(os.path.isfile(full), "pinned file missing: %s" % path)
            with open(full, encoding="utf-8") as f:
                n_lines = len(f.readlines())
            self.assertGreaterEqual(n_lines, int(line_no),
                                    "pin %s:%s beyond end of file (%d lines)" % (path, line_no, n_lines))


class TestMatrix(unittest.TestCase):
    def test_matrix_blocks_match_architecture_nodes(self):
        nodes = set(architecture_nodes())
        blocks = set(matrix_blocks())
        self.assertEqual(blocks - nodes, set(), "matrix blocks citing no architecture node (stale)")
        self.assertEqual(nodes - blocks, set(), "architecture nodes with no matrix block")

    def test_matrix_covers_every_anchor(self):
        _, index = spec_index_anchors()
        covered = set()
        for rows in matrix_blocks().values():
            for row in rows:
                covered.update(row["refs"])
        self.assertEqual(sorted(index - covered), [], "index anchors with no matrix row")
        self.assertEqual(sorted(covered - index), [], "matrix rows citing anchors absent from the index")

    def test_matrix_rows_have_level_and_negative_side(self):
        levels = {"string", "DOM-text", "browser-computed", "pixel"}
        statuses = ("BUILT", "TODO", "RETIRED")
        ids = []
        for node, rows in matrix_blocks().items():
            self.assertTrue(rows, "empty matrix block: %s" % node)
            for row in rows:
                ids.append(row["id"])
                self.assertIn(row["level"], levels, "%s: unknown level %r" % (row["id"], row["level"]))
                self.assertIn("never", row["fact"].lower(),
                              "%s: no NEVER side (regression fence missing)" % row["id"])
                self.assertTrue(row["status"].startswith(statuses),
                                "%s: status outside vocabulary: %r" % (row["id"], row["status"]))
        dupes = [i for i in set(ids) if ids.count(i) > 1]
        self.assertEqual(dupes, [], "duplicate matrix row ids")

    def test_matrix_built_rows_name_real_tests(self):
        module = globals()
        tests_dir = os.path.join(ROOT, "tests")
        this_file = "\n".join(
            read(os.path.join("tests", f)) for f in sorted(os.listdir(tests_dir))
            if f.startswith("test_") and f.endswith(".py")
        )
        for rows in matrix_blocks().values():
            for row in rows:
                if row["status"].startswith("BUILT"):
                    names = re.findall(r"test_\w+", row["owning"])
                    self.assertTrue(names, "%s: BUILT but owning test cell names none" % row["id"])
                    for name in names:
                        self.assertIn("def %s" % name, this_file,
                                      "%s: BUILT row cites missing test %s" % (row["id"], name))


class TestArtifacts(unittest.TestCase):
    def test_artifact_inventory(self):
        entries = inventory_entries()
        self.assertGreater(len(entries), 20, "inventory parse failure")
        for path, is_dir in entries:
            full = os.path.join(ROOT, path)
            if is_dir:
                self.assertTrue(os.path.isdir(full), "inventory dir missing: %s" % path)
                self.assertTrue(os.listdir(full), "inventory dir empty: %s" % path)
            else:
                self.assertTrue(os.path.isfile(full), "inventory file missing: %s" % path)
                self.assertGreater(os.path.getsize(full), 0, "inventory file empty: %s" % path)

    def test_templates_ship(self):
        for name in ("SPEC", "ARCHITECTURE", "TEST_MATRIX", "ROADMAP", "JOURNAL", "NEXT_STEPS"):
            rel = "templates/%s.template.md" % name
            full = os.path.join(ROOT, rel)
            self.assertTrue(os.path.isfile(full), "missing template: %s" % rel)
            self.assertGreater(os.path.getsize(full), 100, "template suspiciously small: %s" % rel)


class TestQueue(unittest.TestCase):
    def _rows(self):
        rows = []
        for line in read("ROADMAP.md").splitlines():
            if line.startswith("|") and not line.startswith("|---") and "Wish (plain words)" not in line:
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) == 5 and cells[0].isdigit():
                    rows.append(cells)
        return rows

    def test_roadmap_class_vocabulary(self):
        head = read("ROADMAP.md").splitlines()
        header = next(l for l in head if "Wish (plain words)" in l)
        for col in ("Class", "Status", "Decision / acceptance"):
            self.assertIn(col, header, "queue missing column: %s" % col)
        rows = self._rows()
        self.assertGreater(len(rows), 40, "queue parse failure")
        pat = re.compile(r"^(bug|small|surface|large)( · (critical|quick win))?$")
        bad = [(r[0], r[2]) for r in rows if not pat.match(r[2])]
        self.assertEqual(bad, [], "class cells outside the four-word vocabulary (+ priority)")

    def test_roadmap_single_in_work(self):
        in_work = [r[0] for r in self._rows() if r[3].lower().startswith("in-work")]
        self.assertLessEqual(len(in_work), 1, "more than one wish in-work: rows %s" % in_work)

    def test_roadmap_header_dated(self):
        first = read("ROADMAP.md").splitlines()[0]
        self.assertRegex(first, r"\d{4}-\d{2}-\d{2}", "queue header carries no date (SPEC M-3)")
        spec_first = read("SPEC.md").splitlines()[0]
        self.assertRegex(spec_first, r"\(v[\d.]+, \d{4}-\d{2}-\d{2}\)", "spec header not versioned+dated")


class TestVersionsAndPins(unittest.TestCase):
    SKILLS = ("live-spec-base", "spec-author", "product-prover", "build-pipeline", "communicator")

    def test_version_homes(self):
        v = read("VERSION").strip()
        self.assertRegex(v, r"^\d+\.\d+\.\d+$", "VERSION is not semver")
        for s in self.SKILLS:
            head = read("skills/%s/SKILL.md" % s).splitlines()[:20]
            metadata_idx = next((i for i, l in enumerate(head) if l.strip() == "metadata:"), None)
            self.assertIsNotNone(metadata_idx, "no metadata: block in %s frontmatter" % s)
            self.assertTrue(
                re.match(r"^\s+version: \d+\.\d+\.\d+", head[metadata_idx + 1]),
                "metadata: block in %s does not carry version: on the next line" % s)
            self.assertFalse(any(re.match(r"^version: \d+\.\d+\.\d+", l) for l in head),
                              "%s still carries a top-level version: line (must live under metadata:)" % s)

    def test_skills_inherit_base_pin(self):
        for s in self.SKILLS:
            if s == "live-spec-base":
                continue
            body = read("skills/%s/SKILL.md" % s)
            self.assertIn("live-spec-base", body, "%s carries no base-skill inherit pin" % s)

    def test_settings_ladder_documented(self):
        body = read("skills/live-spec-base/SKILL.md")
        self.assertRegex(body, r"session beats host beats personal beats\s+package default",
                          "base skill no longer states the settings-ladder resolution order (SPEC E-13)")


class TestDoors(unittest.TestCase):
    def test_next_steps_live_state(self):
        body = read("NEXT_STEPS.md")
        blocks = re.findall(r"^## LIVE STATE", body, re.M)
        self.assertEqual(len(blocks), 1, "LIVE STATE blocks must be replaced, never stacked")
        self.assertRegex(body, r"## LIVE STATE \(\d{4}-\d{2}-\d{2}", "LIVE STATE carries no date")

    def test_adopt_phases_cite_spec(self):
        body = read("adopt/ADOPT.md")
        for code in ("A-0", "A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9",
                     "A-10", "INV-7", "INV-8", "E-14", "E-15"):
            self.assertIn(code, body, "ADOPT.md no longer cites %s" % code)
        for verdict in ("promote", "quarantine", "attic"):
            self.assertIn(verdict, body, "ADOPT.md unbacked-surface verdict lost: %s" % verdict)

    def test_inbox_states_write_rule(self):
        body = read("inbox/README.md")
        self.assertIn("INV-10", body)
        self.assertIn("NEW file", body)
        self.assertIn("YYYY-MM-DD-<source>-<slug>.md", body)

    def test_host_profile_recorded_override(self):
        body = read(".live-spec/profile.md")
        for code in ("INV-14", "E-13", "M-6"):
            self.assertIn(code, body, "host profile no longer cites %s" % code)


class TestDoorLawAndPrototype(unittest.TestCase):
    """The doors landing (SPEC v0.10.0, rows 70-71): the door law and the prototype law must live in
    their normative homes — SPEC prose + index, base rules 15-16, and each working skill's own domain
    slice. String-level per the matrix rows M-067..M-069; the fence machine (M-070) is asserted in
    test_guardrails.py."""

    def test_spec_states_door_procedure(self):
        body = re.sub(r"\s+", " ", read("SPEC.md"))  # prose wraps mid-phrase; compare normalized
        self.assertIn("feature · bug · refactor · docs-only · skip", body,
                      "SPEC lost the five-door vocabulary")
        for phrase in ("The door is named before any code",
                       "A prototype is not the product",
                       "one-way",
                       "re-checked mid-work"):
            self.assertIn(phrase, body, "SPEC lost the door/prototype clause: %s" % phrase)
        for anchor in ("[T-12]", "[INV-16]", "[E-17]", "[INV-17]", "[A-10]"):
            self.assertIn(anchor, body, "SPEC prose lost anchor %s" % anchor)
        # the tripwire verdict must outrank a casual label, and preemption stays with the bug door
        self.assertIn("outranks a casual label", body)
        self.assertIn("takes no preemption", body)

    def test_base_rules_door_and_prototype(self):
        body = read("skills/live-spec-base/SKILL.md")
        self.assertRegex(body, r"(?m)^15\. \*\*The door is named before any code", "base rule 15 missing")
        self.assertRegex(body, r"(?m)^16\. \*\*A prototype is not the product", "base rule 16 missing")
        body = re.sub(r"\s+", " ", body)
        for phrase in ("FEATURE, however casually asked", "re-fires mid-work",
                       "PROTOTYPE label", "its code holds no rights"):
            self.assertIn(phrase, body, "base rules 15-16 lost: %s" % phrase)

    def test_working_skills_carry_the_door(self):
        bp = read("skills/build-pipeline/SKILL.md")
        self.assertIn("Step zero, before ANY tool call: name the door aloud", bp,
                      "build-pipeline lost the door step")
        self.assertIn("feature · bug · refactor · docs-only · skip", bp)
        pp = read("skills/product-prover/SKILL.md")
        self.assertIn("Unbacked surfaces and unlabelled sketches", pp,
                      "product-prover lost the ninth lens")
        self.assertIn("nine families", pp, "prover lens count not updated")
        cm = read("skills/communicator/SKILL.md")
        self.assertIn("shown ONLY under its `PROTOTYPE` label", cm,
                      "communicator lost the prototype-showing rule")
        sa = read("skills/spec-author/SKILL.md")
        self.assertIn("Name the future with the [target] tag", sa,
                      "spec-author lost the [target] tripwire rule")
        # the four working skills' base pin points at the current base version
        for rel in ("skills/build-pipeline/SKILL.md", "skills/communicator/SKILL.md",
                    "skills/product-prover/SKILL.md", "skills/spec-author/SKILL.md"):
            self.assertIn("`live-spec-base` (v0.1.6)", read(rel),
                          "%s pins a stale base version" % rel)

    def test_spec_states_regression_fences(self):
        body = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("What already works is promised before you touch it",
                       "regression fences",
                       "earns NO new matrix row",              # F1 fold: no second home
                       "fenced, cited, untouched",             # the stays/changed split
                       "reconciled from the shipped truth",    # F4/F5 fold
                       'fences by the anchors they cite',      # F8 fold: greppable marker
                       "a prototype fences nothing"):          # F7 fold
            self.assertIn(phrase, body, "SPEC lost the fences clause: %s" % phrase)
        for anchor in ("[T-14, INV-19]",):
            self.assertIn(anchor, body, "SPEC prose lost anchor %s" % anchor)

    def test_skills_carry_regression_fences(self):
        sa = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn("The regression fences — run FIRST", sa, "spec-author lost the fences section")
        self.assertIn("you cannot fence a hope", sa)
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("regression fences", bp, "build-pipeline step 1 lost the fences sentence")
        self.assertIn("never a new row (SPEC T-14, INV-19)", bp)

    def test_spec_states_intake_trio(self):
        body = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("Your time budget is part of the wish",
                       "optional rider on the size word",     # F2 fold
                       "bends scope only, never order",       # F3 fold (index line wording differs)
                       "proceeds on the recommended trim",    # F1 fold
                       "A feature also says what it is NOT doing",
                       "nothing deliberately left out this time",  # F4 fold
                       "the tag marking provenance only",     # F6 fold
                       "bind forward",                        # F7 fold
                       "A prototype writes neither"):         # F8 fold
            self.assertIn(phrase, body, "SPEC lost the intake-trio clause: %s" % phrase)
        for anchor in ("[T-15]", "[INV-20]", "[INV-21]"):
            self.assertIn(anchor, body, "SPEC prose lost anchor %s" % anchor)

    def test_skills_carry_intake_trio(self):
        sa = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn("The delta's two closing sentences", sa,
                      "spec-author lost the closing-sentences section")
        self.assertIn("only a missing sentence is a hole", sa)
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("optional appetite rider", bp, "build-pipeline intake line lost the appetite rider")
        self.assertIn("The delta CLOSES with its two sentences", bp)

    def test_no_calques_rule(self):
        # row 73: the calque ban lives once in base rule 2; communicator elaborates with the example
        base = re.sub(r"\s+", " ", read("skills/live-spec-base/SKILL.md"))
        self.assertIn("no calques", base, "base rule 2 lost the calque ban")
        self.assertIn("never loan-translated", base)
        cm = re.sub(r"\s+", " ", read("skills/communicator/SKILL.md"))
        self.assertIn("Calques are the same bug across a language split", cm,
                      "communicator rule 6 lost the calque elaboration")
        self.assertIn("вердикт растяжки старше ярлыка", cm, "communicator lost the field example")


class TestFacetSweep(unittest.TestCase):
    """The facet-sweep landing (SPEC v0.11.0, row 72): a feature-doored spec-delta walks the standard
    facets a layman can't name; every facet ends as a spec sentence — decided or [default]-tagged +
    reported. Normative homes: SPEC prose + index (T-13/INV-18), the canonical facet list in
    spec-author, the tradeoff-report line in communicator, the step-1 sweep sentence in build-pipeline.
    String-level per matrix rows M-072..M-073."""

    FACETS = ("phone or narrow window", "hover-only needs a touch answer",
              "empty, error, and", "accessibility", "performance envelope")

    def test_spec_states_facet_sweep(self):
        body = re.sub(r"\s+", " ", read("SPEC.md"))
        self.assertIn("A feature is specified past what you know to ask", body,
                      "SPEC lost the facet-sweep headline")
        for phrase in self.FACETS:
            self.assertIn(phrase, body, "SPEC lost the facet: %s" % phrase)
        for phrase in ("Every facet ends as a spec sentence",
                       "`[default]`",                       # the default tag (F1 fold)
                       "walks the sweep before work resumes",  # mid-work re-door (F3 fold)
                       "A fenced prototype is NOT swept",       # prototype boundary (F7 fold)
                       "reconciled like any re-engineered claim",  # adopted surface (F6 fold)
                       "AUTHORS the facet sentences"):          # sweep vs axes split (F5 fold)
            self.assertIn(phrase, body, "SPEC lost the facet-sweep clause: %s" % phrase)
        for anchor in ("[T-13]", "[INV-18]"):
            self.assertIn(anchor, body, "SPEC prose lost anchor %s" % anchor)

    def test_skills_carry_facet_sweep(self):
        sa = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn("canonical facet list", sa, "spec-author lost the facet list home")
        for phrase in self.FACETS:
            self.assertIn(phrase, sa, "spec-author facet list lost: %s" % phrase)
        self.assertIn("`[default]`", sa, "spec-author lost the [default] tag rule")
        cm = re.sub(r"\s+", " ", read("skills/communicator/SKILL.md"))
        self.assertIn("standard-facet sweep", cm, "communicator lost the facet tradeoff-report line")
        self.assertIn("a veto becomes a new wish", cm)
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("standard-facet sweep", bp, "build-pipeline step 1 lost the sweep sentence")
        self.assertIn("canonical list lives in spec-author", bp)


if __name__ == "__main__":
    unittest.main(verbosity=2)
