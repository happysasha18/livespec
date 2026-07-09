"""Traceability suite — the coverage validation of TEST_MATRIX.md, mechanized (SPEC E-14/E-15/INV-15).

Zero dependencies; run from the repo root:  python3 -m unittest discover tests -v
Every check here asserts the SHIPPED files on disk, never a source fragment or a memory of one.
This is the first slice of the guardrails' conflicts check (ROADMAP rows 3 and 12's gap 3 territory);
the pre-push hook generalizes it when row 3 lands.
"""

import json
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
    """Anchors from PRODUCT_SPEC.md's Formal index table, ranges expanded."""
    spec = read("PRODUCT_SPEC.md")
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
        spec = read("PRODUCT_SPEC.md")
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

    def test_matrix_rows_sit_under_their_owning_node(self):
        # the 0.8.0 matrix audit's F1: a row whose anchors are all owned elsewhere is misplaced
        nodes = architecture_nodes()
        for block, rows in matrix_blocks().items():
            owned = nodes.get(block, set())
            for row in rows:
                self.assertTrue(row["refs"] & owned,
                                "%s sits under %r but cites only %s (owned elsewhere)"
                                % (row["id"], block, sorted(row["refs"])))

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
        for name in ("PRODUCT_SPEC", "ARCHITECTURE", "TEST_MATRIX", "ROADMAP", "JOURNAL", "NEXT_STEPS"):
            rel = "templates/%s.template.md" % name
            full = os.path.join(ROOT, rel)
            self.assertTrue(os.path.isfile(full), "missing template: %s" % rel)
            self.assertGreater(os.path.getsize(full), 100, "template suspiciously small: %s" % rel)
        scaffold = os.path.join(ROOT, "templates", "test_scaffold.template.py")
        self.assertTrue(os.path.isfile(scaffold), "missing the bootstrap suite scaffold (B-1, row 62)")


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
        self.assertGreater(len(rows), 3, "queue parse failure")
        # terminal rows move to dated archives at milestones (INV-1/M-1); the archive dir must exist once one happened
        self.assertTrue(os.path.isdir(os.path.join(ROOT, "docs", "queue-archive")),
                        "closed rows gone but no queue archive present")
        pat = re.compile(r"^(bug|small|surface|large)( · (critical|quick win))?$")
        bad = [(r[0], r[2]) for r in rows if not pat.match(r[2])]
        self.assertEqual(bad, [], "class cells outside the four-word vocabulary (+ priority)")

    def test_roadmap_in_work_cap(self):
        in_work = [r[0] for r in self._rows() if r[3].lower().startswith("in-work")]
        self.assertLessEqual(len(in_work), 3,
                             "more than three rows in-work — the lane cap (SPEC T-18): rows %s" % in_work)

    def test_roadmap_header_dated(self):
        first = read("ROADMAP.md").splitlines()[0]
        self.assertRegex(first, r"\d{4}-\d{2}-\d{2}", "queue header carries no date (SPEC M-3)")
        spec_first = read("PRODUCT_SPEC.md").splitlines()[0]
        self.assertRegex(spec_first, r"\(v[\d.]+, \d{4}-\d{2}-\d{2}\)", "spec header not versioned+dated")


class TestVersionsAndPins(unittest.TestCase):
    SKILLS = ("live-spec-base", "spec-author", "product-prover", "build-pipeline", "communicator",
              "publish", "test-author", "feedback-intake")

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
        base_version = re.search(r"(?m)^\s*version:\s*([0-9.]+)",
                                  read("skills/live-spec-base/SKILL.md")).group(1)
        for s in self.SKILLS:
            if s == "live-spec-base":
                continue
            body = read("skills/%s/SKILL.md" % s)
            self.assertIn("live-spec-base", body, "%s carries no base-skill inherit pin" % s)
            self.assertIn("`live-spec-base` (v%s)" % base_version, body,
                          "%s pins a stale (or missing) base version" % s)

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
        body = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))  # prose wraps mid-phrase; compare normalized
        self.assertIn("feature · bug · refactor · docs-only · skip", body,
                      "SPEC lost the five-door vocabulary")
        for phrase in ("The door is named before any code",
                       "A prototype stays a sketch",
                       "one-way",
                       "re-checked mid-work"):
            self.assertIn(phrase, body, "SPEC lost the door/prototype clause: %s" % phrase)
        for anchor in ("[T-12]", "[INV-16]", "[E-17]", "[INV-17]", "[A-10]"):
            self.assertIn(anchor, body, "SPEC prose lost anchor %s" % anchor)
        # the tripwire verdict must outrank a casual label, and preemption stays with the bug door
        self.assertIn("outranks a casual label", body)
        self.assertIn("no preemption", body)

    def test_base_rules_door_and_prototype(self):
        body = read("skills/live-spec-base/SKILL.md")
        self.assertRegex(body, r"(?m)^15\. \*\*The door is named before any code", "base rule 15 missing")
        self.assertRegex(body, r"(?m)^16\. \*\*A prototype stays a sketch", "base rule 16 missing")
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
        # the four working skills' base pin points at the CURRENT base version (read from its
        # frontmatter, so a base bump without the same-session pin sweep is red by construction)
        base_version = re.search(r"(?m)^\s*version:\s*([0-9.]+)",
                                 read("skills/live-spec-base/SKILL.md")).group(1)
        for rel in ("skills/build-pipeline/SKILL.md", "skills/communicator/SKILL.md",
                    "skills/product-prover/SKILL.md", "skills/spec-author/SKILL.md",
                    "skills/publish/SKILL.md", "skills/test-author/SKILL.md",
                    "skills/feedback-intake/SKILL.md"):
            self.assertIn("`live-spec-base` (v%s)" % base_version, read(rel),
                          "%s pins a stale base version" % rel)

    def test_spec_states_work_kind(self):
        body = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("intake line also names what is being built",
                       "scales the steps",
                       "stood down by name",
                       "An unresolved kind scales nothing down",
                       "never the mandatory checks",
                       "one kind per wish",
                       "curated like the facet list"):
            self.assertIn(phrase, body, "SPEC lost the work-kind clause: %s" % phrase)
        for kind in ("**product**", "**infra**", "**skill**", "**prose**"):
            self.assertIn(kind, body, "SPEC lost the kind %s" % kind)
        for anchor in ("[T-16]", "[INV-22]"):
            self.assertIn(anchor, body, "SPEC prose lost anchor %s" % anchor)

    def test_skills_carry_work_kind(self):
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("product · infra · skill · prose", bp,
                      "build-pipeline lost the work-kind vocabulary")
        self.assertIn("The work-kind table", bp,
                      "build-pipeline lost the per-kind step table (its ONE normative home)")
        for phrase in ("APPLIED in its kind's form or STOOD DOWN by name",
                       "An unresolved kind scales nothing down"):
            self.assertIn(phrase, bp, "build-pipeline lost the work-kind clause: %s" % phrase)
        base = re.sub(r"\s+", " ", read("skills/live-spec-base/SKILL.md"))
        self.assertIn("work-kind", base, "base rule 15 lost the work-kind axis")
        self.assertIn("product · infra · skill · prose", base,
                      "base rule 15 lost the four-kind vocabulary")
        cm = re.sub(r"\s+", " ", read("skills/communicator/SKILL.md"))
        self.assertIn("stood down", cm, "communicator lost the stood-down-steps report line")

    def test_spec_states_regression_fences(self):
        body = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("What already works is promised before the agent touches it",
                       "regression fences",
                       "earns no new matrix row",              # F1 fold: no second home
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
        body = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("negotiates scope, never time",  # row 99: his word, time budgets dead (anchor+term, register-A safe)
                       "in hours or days",              # time estimate refused as input
                       "split into stages",
                       "scope only, never order",
                       "No cut touches the delta's mandatory sentences",  # scope dials richness, safety net = the mandatory sentences
                       "A feature also says what it is not doing",
                       "[INV-20]",  # F4 fold: "nothing deliberately left out this time" is a valid non-goals sentence
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
        self.assertIn("never a time budget or estimate", bp,
                      "build-pipeline intake line lost the scope-never-time law")
        self.assertNotIn("appetite", bp.lower(), "build-pipeline still speaks the retired term")
        self.assertIn("The delta CLOSES with its two sentences", bp)
        sa2 = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertNotIn("appetite", sa2.lower(), "spec-author still speaks the retired term")
        spec2 = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertNotIn("appetite", spec2.lower(), "SPEC still speaks the retired term")

    def test_spec_states_founding_and_designsync(self):
        body = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("founding questions asked, never inferred",
                       "personal tool, or reusable product?",
                       "[INV-4, INV-12]",  # F5 fold: the founding answer's stronger-than-usual habit clause
                       "A-1 carries the pointer",                                          # F7 fold
                       "Design-sync [target: the machine; the wiring is live]",           # row 93 pack-side
                       "[E-18]",                                # F1 fold: design-sync supplements the in-session render
                       "[E-7]"):                                # F4 fold: the components a landing declared
            self.assertIn(phrase, body, "SPEC lost the founding/design-sync clause: %s" % phrase)
        for anchor in ("[B-2]", "[E-18]"):
            self.assertIn(anchor, body, "SPEC prose lost anchor %s" % anchor)
        adopt = re.sub(r"\s+", " ", read("adopt/ADOPT.md"))
        self.assertIn("Founding questions ride the orient", adopt, "ADOPT lost the founding-questions line")
        tpl = re.sub(r"\s+", " ", read("templates/PRODUCT_SPEC.template.md"))
        self.assertIn("Founding answers (B-2)", tpl, "SPEC template lost the founding-answers slot")

    def test_night_batch_skill_rules(self):
        # rows 79/81/82/87: worker briefs, excuses table, two one-liners, decision-file numbering
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("The brief is self-contained", bp, "build-pipeline lost the worker-brief rule")
        self.assertIn("The excuses table", bp, "build-pipeline lost the excuses table")
        self.assertIn("Size never picks the door", bp)
        pp = re.sub(r"\s+", " ", read("skills/product-prover/SKILL.md"))
        self.assertIn("Report gaps. Taste is out of scope.", pp, "product-prover lost the anti-taste line")
        base = read("skills/live-spec-base/SKILL.md")
        self.assertRegex(base, r"(?m)^17\. \*\*Irreversible means gone, not merely public",
                         "base rule 17 missing")
        self.assertIn("A push to your own repository is NOT irreversible", base)
        cm = re.sub(r"\s+", " ", read("skills/communicator/SKILL.md"))
        self.assertIn("append their ordinal", cm, "communicator lost the decision-file numbering")

    def test_spec_states_registry_and_pins(self):
        body = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("pinned to file:line", body, "SPEC lost symbol-first pins (E-14)")
        self.assertIn("preferred form is executable", body, "SPEC lost the executable-registry form (E-10)")
        adopt = re.sub(r"\s+", " ", read("adopt/ADOPT.md"))
        self.assertIn("lift the surface inventory into an executable completeness gate", adopt)
        self.assertIn("Pins are names first", adopt)

    def test_no_calques_rule(self):
        # row 73: the calque ban lives once in base rule 2; communicator elaborates with the example
        base = re.sub(r"\s+", " ", read("skills/live-spec-base/SKILL.md"))
        self.assertIn("no calques", base, "base rule 2 lost the calque ban")
        self.assertIn("never loan-translated", base)
        cm = re.sub(r"\s+", " ", read("skills/communicator/SKILL.md"))
        self.assertIn("Calques are the same bug across a language split", cm,
                      "communicator rule 6 lost the calque elaboration")
        self.assertIn("the stretch's verdict outranks the label", cm, "communicator lost the calque example")


class TestUnwrittenSeamHunt(unittest.TestCase):
    """The prover hunts the unwritten seam (SPEC INV-72 + C-1 axis, row prover-wish 2026-07-09).
    Normative homes: SPEC prose + index (INV-72 owned by product-prover, C-1 axis owned by spec-author),
    the stress-lens in product-prover, the axis in spec-author's compose list. String-level, matrix M-179."""

    SEAM = "every other surface that can be present at the same time"

    def test_prover_hunts_unwritten_seam(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        # SPEC: the invariant and its C-1 axis exist, both sides stated.
        self.assertIn("[INV-72]", spec, "SPEC lost the unwritten-seam invariant anchor")
        self.assertIn(self.SEAM, spec, "SPEC lost the every-other-live-surface axis")
        self.assertIn("whether or not that other surface holds state", spec,
                      "SPEC lost F4: a non-stateful co-present surface (a static end screen) is in scope")
        self.assertIn("a reachable situation with a blank answer is a finding", spec.lower(),
                      "SPEC lost the finding side of INV-72")
        for anchor in ("[C-1]", "[E-14]", "[INV-18]", "[INV-31]"):
            self.assertIn(anchor, spec, "SPEC INV-72 prose lost anchor %s" % anchor)

        # product-prover skill: the active-hunt stress lens ships in the SKILL.md.
        pp = re.sub(r"\s+", " ", read("skills/product-prover/SKILL.md"))
        self.assertIn("unwritten seam", pp.lower(), "product-prover lost the unwritten-seam lens headline")
        self.assertIn(self.SEAM, pp, "product-prover lens lost the co-present-surface enumeration")
        self.assertIn("[INV-72]", pp, "product-prover lens lost its anchor")
        # never-side: the prover reports, it does not invent or ask the human.
        self.assertIn("invents no answer", pp, "product-prover lost the never-invent side of the hunt")

        # spec-author skill: the matching axis lives in the compose list (its operational home).
        sa = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn(self.SEAM, sa, "spec-author compose list lost the every-other-live-surface axis")


class TestFacetSweep(unittest.TestCase):
    """The facet-sweep landing (SPEC v0.11.0, row 72): a feature-doored spec-delta walks the standard
    facets a layman can't name; every facet ends as a spec sentence — decided or [default]-tagged +
    reported. Normative homes: SPEC prose + index (T-13/INV-18), the canonical facet list in
    spec-author, the tradeoff-report line in communicator, the step-1 sweep sentence in build-pipeline.
    String-level per matrix rows M-072..M-073."""

    FACETS = ("phone or narrow window", "hover-only needs a touch answer",
              "empty, error, and", "accessibility", "performance envelope",
              "visual hierarchy", "two windows at once", "missing source")

    def test_facet_list_is_curated(self):
        sa = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn("The list is curated, each facet earning its place by named incident", sa, "spec-author lost the curation law")
        self.assertIn("named real incident", sa)
        # every facet entry in the canonical list names its incident
        self.assertGreaterEqual(sa.count("(incident"), 3, "new facets must carry their incidents")

    def test_spec_states_facet_sweep(self):
        body = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("A feature is specified past what the human knows to ask", body,
                      "SPEC lost the facet-sweep headline")
        for phrase in self.FACETS:
            self.assertIn(phrase, body, "SPEC lost the facet: %s" % phrase)
        for phrase in ("Every facet ends as a spec sentence",
                       "`[default]`",                       # the default tag (F1 fold)
                       "walks the sweep before work resumes",  # mid-work re-door (F3 fold)
                       "A fenced prototype is not swept",       # prototype boundary (F7 fold)
                       "reconciled like any re-engineered claim",  # adopted surface (F6 fold)
                       "authors the facet sentences"):          # sweep vs axes split (F5 fold)
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
        self.assertIn("veto becomes a new wish", cm)
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("standard-facet sweep", bp, "build-pipeline step 1 lost the sweep sentence")
        self.assertIn("canonical list lives in spec-author", bp)


if __name__ == "__main__":
    unittest.main(verbosity=2)


class TestDocRenderer(unittest.TestCase):
    """Row 97: documents a human reads render to a real page (no VT220)."""

    def test_render_doc_smoke(self):
        import subprocess, tempfile
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "t.md")
            with open(src, "w") as f:
                f.write("# Title\n\nA **bold** point.\n\n| a | b |\n|---|---|\n| 1 | 2 |\n")
            out = os.path.join(tmp, "t.html")
            r = subprocess.run(["python3", os.path.join(ROOT, "scripts", "render-doc.py"), src, out],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            body = open(out).read()
            for frag in ('<h1 id="title">Title</h1>', "<strong>bold</strong>", "<table>", "<td>2</td>"):
                self.assertIn(frag, body)


class TestSkillEvals(unittest.TestCase):
    """SPEC E-19: every working skill owns an eval — self-closing over skills/ (row 94)."""

    def working_skills(self):
        return sorted(d for d in os.listdir(os.path.join(ROOT, "skills"))
                      if os.path.isdir(os.path.join(ROOT, "skills", d))
                      and d != "live-spec-base")

    def test_skill_evals_present(self):
        skills = self.working_skills()
        self.assertGreaterEqual(len(skills), 4)
        for s in skills:
            path = "evals/%s.md" % s
            self.assertTrue(os.path.exists(os.path.join(ROOT, path)),
                            "working skill %s has no eval (%s) — E-19 binds" % (s, path))
            body = read(path)
            for section in ("## Scenario", "## Criteria", "## The red", "## Re-run"):
                self.assertIn(section, body, "%s lost its %s section" % (path, section))
            self.assertRegex(body, r"bare run: \d{4}-\d{2}-\d{2}",
                             "%s carries no dated bare-run record — red must be PROVEN" % path)

    def test_eval_readme_states_honest_boundary(self):
        body = read("evals/README.md")
        self.assertIn("bare-of-the-SKILL", body,
                      "evals/README lost the loader-contamination boundary")
        self.assertIn("the scenario speaks like the human", body,
                      "evals/README lost the no-enumerated-hints authoring rule")


class TestDesignSyncWiring(unittest.TestCase):
    """SPEC E-18, row 93 pack-side half: the switch + channel lines are wired; the machine stays [target]."""

    def test_designsync_wiring(self):
        base = re.sub(r"\s+", " ", read("skills/live-spec-base/SKILL.md"))
        self.assertIn("`design-sync`", base, "base defaults table lost the design-sync switch")
        self.assertIn("off — a host with visual components may switch it on", base,
                      "design-sync switch lost its off-by-default value")
        cm = re.sub(r"\s+", " ", read("skills/communicator/SKILL.md"))
        self.assertIn("design project", cm, "communicator lost the design-sync channel line")
        self.assertIn("after the human's gate", cm,
                      "communicator's design-sync line lost the gate")
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("design-sync is ON", bp,
                      "build-pipeline step 9 lost the design-sync line")
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("[target: the machine; the wiring is live]", spec,
                      "SPEC E-18 lost the honest wired-vs-target split")


class TestPublishSkill(unittest.TestCase):
    """SPEC E-20, row 98: the publish-quality gate ships as the fifth working skill."""

    def test_publish_skill_carries_checklist(self):
        body = re.sub(r"\s+", " ", read("skills/publish/SKILL.md"))
        for phrase in ("The kind checklist",
                       "Targets are plugins",
                       "FRESH screenshots",
                       "when to USE it and when NOT",
                       "at least one REAL run",
                       "never sends anything itself",
                       "the human releases it"):
            self.assertIn(phrase, body, "publish skill lost: %s" % phrase)
        for target in ("GitHub repo", "Plugin directory", "Design project"):
            self.assertIn(target, body, "publish skill lost target plugin: %s" % target)
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("Publishing — the deposit owes what its kind owes",
                       "Each publish target is a plugin",
                       "checklist runs before the gate"):
            self.assertIn(phrase, spec, "SPEC lost the publishing clause: %s" % phrase)
        self.assertIn("[E-20]", spec, "SPEC prose lost anchor E-20")


class TestInstallerAndDecisionPage(unittest.TestCase):
    """Row 57 (SPEC v0.15.1): the two shipped mechanisms the spec now names — the installer (E-21,
    M-091) and the decision page (E-22, M-092). The installer row is a REAL run against a temp home,
    twice, because its promises (fresh machine works · backup before overwrite · never deletes) are
    behaviours of the script, not strings in it."""

    def test_install_sh_installs_and_backs_up(self):
        import subprocess
        import tempfile
        script = os.path.join(ROOT, "install.sh")
        skills = sorted(d for d in os.listdir(os.path.join(ROOT, "skills"))
                        if os.path.isdir(os.path.join(ROOT, "skills", d)))
        self.assertGreaterEqual(len(skills), 5, "skills/ parse failure")
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, HOME=tmp)
            r = subprocess.run(["bash", script], env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0,
                             "install.sh failed on a FRESH home (no ~/.claude/skills yet):\n%s\n%s"
                             % (r.stdout, r.stderr))
            dest = os.path.join(tmp, ".claude", "skills")
            for s in skills:
                self.assertTrue(os.path.isfile(os.path.join(dest, s, "SKILL.md")),
                                "%s not installed" % s)
            r2 = subprocess.run(["bash", script], env=env, capture_output=True, text=True)
            self.assertEqual(r2.returncode, 0, "second (idempotent) run failed:\n%s" % r2.stderr)
            for s in skills:
                self.assertTrue(os.path.isfile(os.path.join(dest, s, "SKILL.md")),
                                "%s gone after re-run — the never-deletes side broke" % s)
            attic = dest + "-attic"
            self.assertTrue(os.path.isdir(attic),
                            "second run left no attic dir beside the live skills dest (row 122)")
            attic_backups = [d for d in os.listdir(attic) if ".bak_" in d]
            self.assertGreaterEqual(len(attic_backups), len(skills),
                                    "second run left no timestamped backups in the attic")
            dest_backups = [d for d in os.listdir(dest) if ".bak_" in d]
            self.assertEqual(dest_backups, [],
                             "a backup landed inside the live skills dir — row 122 regression")

    def test_spec_names_installer(self):
        body = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("How the skills arrive on a machine",
                       "backs up an existing copy with a timestamp before overwriting, and never",
                       "two halves of one seam"):
            self.assertIn(phrase, body, "SPEC lost the installer clause: %s" % phrase)
        self.assertIn("[E-21]", body, "SPEC prose lost anchor E-21")

    def test_spec_names_decision_page(self):
        body = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("decision page",              # register-invariant domain terms, not phrasing
                       "docs/decisions/",
                       "answered-then-withdrawn"):
            self.assertIn(phrase, body, "SPEC lost the decision-page clause: %s" % phrase)
        self.assertIn("[E-22]", body, "SPEC prose lost anchor E-22")
        cm = re.sub(r"\s+", " ", read("skills/communicator/SKILL.md"))
        self.assertIn("ONE interactive decision page", cm, "communicator rule 10 lost the page law")
        self.assertIn("docs/decisions/", cm, "communicator rule 10 lost the archive step")


class TestCollisionLaw(unittest.TestCase):
    """Row 60 (M-093): one name-collision law, one home — base rule 18; the attic, the inbox and
    ADOPT cite it instead of each speaking half of it."""

    def test_collision_law_one_home(self):
        base = read("skills/live-spec-base/SKILL.md")
        self.assertRegex(base, r"(?m)^18\. \*\*One name-collision law",
                         "base rule 18 missing")
        flat = re.sub(r"\s+", " ", base)
        for phrase in ("first the semantic mark its home already defines",
                       "numeric ordinal",
                       "Never overwrite, never a third scheme",
                       "a short session token",
                       "never a lost file"):
            self.assertIn(phrase, flat, "base rule 18 lost: %s" % phrase)
        for rel in ("PRODUCT_SPEC.md", "adopt/ADOPT.md", "inbox/README.md"):
            body = re.sub(r"\s+", " ", read(rel))
            self.assertIn("rule 18", body, "%s no longer cites the one collision law" % rel)
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertEqual(spec.count("rule 18"), 2,
                         "the law must be CITED at its two instances (attic, inbox), stated only in base")


class TestDeclineListsAbsorbed(unittest.TestCase):
    """Row 63 (M-094): declining an absorber lists the rows superseded into it — each declined by
    name or returned; a superseded wish never dies by pointer."""

    def test_spec_states_decline_absorbed(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("[T-8]",  # "declining is not a black hole" for what a decline absorbed
                       "declined by name",
                       "returned to the queue as its own row again",
                       "superseded wish never dies by pointer"):
            self.assertIn(phrase, spec, "SPEC lost the decline-lists-absorbed clause: %s" % phrase)
        tpl = re.sub(r"\s+", " ", read("templates/ROADMAP.template.md"))
        self.assertIn("never dies by pointer", tpl,
                      "ROADMAP template lost the decline-lists-absorbed rule")


def _pack_list_gaps(skill_names, spec_body, footer_bodies, readme_body, overview_body=None):
    """Row 167 (M-168, INV-66): pure checker — which skill names are missing from
    which pack list. Returns a list of "list-label: missing-name" strings.
    overview_body is the OVERVIEW.md reader prose (the 2026-07-08 stale-quote grep
    found it silently drifted to five working skills while the parity check never read
    it — the INV-66 class on an uncovered surface); None skips it."""
    gaps = []
    working = [s for s in skill_names if s != "live-spec-base"]
    for name in working:
        if name not in spec_body:
            gaps.append("SPEC working-skills text: %s" % name)
        if name not in readme_body:
            gaps.append("README: %s" % name)
        if overview_body is not None and name not in overview_body:
            gaps.append("OVERVIEW: %s" % name)
    for label, body in footer_bodies.items():
        for name in skill_names:
            if name not in body:
                gaps.append("%s closing list: %s" % (label, name))
    return gaps


class TestPackListParity(unittest.TestCase):
    """Row 167 (M-168, INV-66): every place the pack lists its skills names the same
    complete set — born of the communicator footer that predated publish."""

    def all_skills(self):
        return sorted(d for d in os.listdir(os.path.join(ROOT, "skills"))
                      if os.path.isdir(os.path.join(ROOT, "skills", d)))

    def footer_bodies(self):
        out = {}
        for s in self.all_skills():
            body = read(os.path.join("skills", s, "SKILL.md"))
            if "The pack, whole:" in body:
                out[s] = re.sub(r"\s+", " ", body.split("The pack, whole:", 1)[1])
        return out

    def test_real_repo_lists_complete(self):
        skills = self.all_skills()
        self.assertGreaterEqual(len(skills), 7)
        footers = self.footer_bodies()
        self.assertGreaterEqual(len(footers), 2,
                                "the closing pack lists disappeared — the parity check lost its subject")
        gaps = _pack_list_gaps(skills, re.sub(r"\s+", " ", read("PRODUCT_SPEC.md")),
                               footers, re.sub(r"\s+", " ", read("README.md")),
                               re.sub(r"\s+", " ", read("OVERVIEW.md")))
        self.assertEqual(gaps, [], "pack lists drifted: %s" % gaps)

    def test_stripped_copy_goes_red(self):
        # The never side, permanent: the pre-fix communicator footer (four skills,
        # publish missing since its birth) must FAIL this checker.
        old_footer = ("**spec-author** writes the spec · **product-prover** reviews it · "
                      "**build-pipeline** ships it · **communicator** makes the human-facing exchange land.")
        gaps = _pack_list_gaps(self.all_skills(), re.sub(r"\s+", " ", read("PRODUCT_SPEC.md")),
                               {"communicator": old_footer},
                               re.sub(r"\s+", " ", read("README.md")))
        self.assertTrue(any("communicator closing list" in g for g in gaps),
                        "the checker passed the historic four-skill footer — it has no teeth")

    def test_stripped_overview_goes_red(self):
        # The never side, permanent: OVERVIEW.md drifted to five working skills for two
        # skills' whole lifetime because the parity check never read it (2026-07-08). A
        # reader body missing a working skill must FAIL the checker.
        stripped_overview = ("live-spec-base spec-author product-prover build-pipeline "
                             "communicator publish")  # test-author + feedback-intake absent
        gaps = _pack_list_gaps(self.all_skills(), re.sub(r"\s+", " ", read("PRODUCT_SPEC.md")),
                               {}, re.sub(r"\s+", " ", read("README.md")),
                               stripped_overview)
        self.assertTrue(any(g.startswith("OVERVIEW:") for g in gaps),
                        "the checker passed an OVERVIEW missing two working skills — no teeth")


class TestPluginMetadata(unittest.TestCase):
    """Row 169 (M-171, INV-44/INV-66): the shipped plugin metadata matches the pack's truth —
    both .claude-plugin JSONs carry a description, plugin.json's version equals the VERSION
    file, and a description naming ANY pack skill names them all (the row-167 drift class)."""

    def _load(self, rel):
        return json.loads(read(rel))

    def test_metadata_described_and_current(self):
        plugin = self._load(".claude-plugin/plugin.json")
        market = self._load(".claude-plugin/marketplace.json")
        self.assertTrue(market.get("description", "").strip(),
                        "marketplace.json ships no description — the validator's warning (row 169)")
        self.assertTrue(plugin.get("description", "").strip(),
                        "plugin.json ships no description")
        self.assertEqual(plugin.get("version"), read("VERSION").strip(),
                         "plugin.json pins a version that drifted from the VERSION file")

    def test_descriptions_never_carry_a_partial_skill_list(self):
        skills = sorted(d for d in os.listdir(os.path.join(ROOT, "skills"))
                        if os.path.isdir(os.path.join(ROOT, "skills", d)))
        self.assertGreaterEqual(len(skills), 7)
        for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
            desc = self._load(rel).get("description", "")
            named = set(s for s in skills if s in desc)
            self.assertTrue(named == set() or named == set(skills),
                            "%s description names SOME pack skills, missing: %s"
                            % (rel, sorted(set(skills) - named)))


class TestFeedbackIntake(unittest.TestCase):
    """Row 47 (M-172..174, E-28/T-20/INV-68): the intake skill ships, every route has a
    home, and the never-lost law agrees across its three surfaces."""

    def skill(self):
        return read(os.path.join("skills", "feedback-intake", "SKILL.md"))

    def test_feedback_intake_ships(self):
        body = self.skill()
        head = "\n".join(body.splitlines()[:8])
        self.assertIn("name: feedback-intake", head, "frontmatter lost its name")
        self.assertIn("version:", head, "frontmatter lost its version")
        flat = re.sub(r"\s+", " ", body)
        for channel in ("Spoken or typed", "A comment on something shown", "A dropped file"):
            self.assertIn(channel, flat, "skill lost a channel: %s" % channel)
        self.assertIn("FEEDBACK.md", flat, "skill lost the ledger's name")
        for part in ("when it arrived", "who handed it in", "which channel",
                     "what it concerns", "where it went"):
            self.assertIn(part, flat, "ledger line shape lost: %s" % part)

    def test_feedback_routes_have_homes(self):
        flat = re.sub(r"\s+", " ", self.skill())
        for route, home in (("WISH", "queue row"), ("FIXED", "journal"),
                            ("CLOSES", "archive"), ("FIELD EVIDENCE", "ledger"),
                            ("workshop noise", "problem ledger")):
            self.assertIn(route, flat, "routing table lost the %s route" % route)
            self.assertIn(home, flat, "route %s lost its home %s" % (route, home))
        self.assertIn("inbox sweep", flat, "the sweep fire-moment is gone")
        self.assertIn("never on the agent's own output", flat.lower(),
                      "the never-fires side is gone")
        self.assertIn("never opens a queue row on its own judgment", flat.lower(),
                      "the wish-door boundary is gone")

    def test_feedback_never_lost_in_both_homes(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("| INV-68 |", spec, "SPEC index lost INV-68")
        self.assertIn("route's own home", spec, "SPEC lost the route-homes law")
        skill = re.sub(r"\s+", " ", self.skill())
        for phrase in ("one echo per item", "appends its date", "only the assigned session"):
            self.assertIn(phrase, skill.lower(), "skill lost the never-lost clause: %s" % phrase)
        inbox = re.sub(r"\s+", " ", read(os.path.join("inbox", "README.md")))
        self.assertIn("wishes and feedback", inbox, "inbox README still speaks wishes only")
        self.assertIn("the home its route owns", inbox,
                      "inbox README still harvests everything into rows")


class TestTargetOwnership(unittest.TestCase):
    """Row 64 (M-095): SPEC S-0 mechanized. Every [target]-marked index fact maps to a still-open
    queue row (the map below is declared HERE, self-closing: a new [target] without a map entry is
    red, a map entry whose index mark disappeared is red too); and the architecture stays honest —
    a node carrying [target] names its missing pin with an em-dash, a node whose pins are all real
    carries no tag."""

    TARGET_ROW_OWNERS = {
        "E-6": 55,    # host-facing gates ride the registry+snapshot family (archived row 3's remainder)
        "E-7": 55,    # snapshot machinery
        "E-10": 55,   # surface registry executable form rides the same family
        "E-18": 93,   # design-sync machine: first real sync on a visual host
        "INV-17": 55, # build⊆spec honesty legs = the host-facing gate legs
        "INV-21": 96, # success-measure reading machinery = the feedback family
        "A-6": 55,    # adoption baseline rides the snapshot
    }

    def roadmap_rows(self):
        rows = {}
        for line in read("ROADMAP.md").splitlines():
            if line.startswith("|") and not line.startswith("|---"):
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) == 5 and cells[0].isdigit():
                    rows[int(cells[0])] = cells[3]
        return rows

    def test_targets_owned_by_open_rows(self):
        spec = read("PRODUCT_SPEC.md")
        index_lines = re.findall(r"^\| (%s) \| ([^|]*) \|" % ANCHOR_TOKEN, spec, re.M)
        marked = {a for a, fact in index_lines if re.search(r"\[[^\]]*target", fact)}
        self.assertEqual(marked, set(self.TARGET_ROW_OWNERS),
                         "the [target] map and the Formal index disagree — a new target needs its "
                         "map entry WITH an owning row; a landed one leaves both (SPEC S-0)")
        rows = self.roadmap_rows()
        for anchor, row_no in sorted(self.TARGET_ROW_OWNERS.items()):
            self.assertIn(row_no, rows,
                          "%s's owning row %d is not in the ACTIVE queue (landed/archived?) — "
                          "re-own the target or drop its tag" % (anchor, row_no))
            status = rows[row_no].lstrip("*").strip().lower()
            self.assertFalse(status.startswith(("landed", "declined", "superseded")),
                             "%s's owning row %d is terminal (%r) — a target owned by a closed row "
                             "is an orphan" % (anchor, row_no, rows[row_no][:60]))

    def test_target_nodes_pin_honesty(self):
        arch = read("ARCHITECTURE.md")
        section = arch.split("## Nodes", 1)[1].split("## Seams", 1)[0]
        for line in section.splitlines():
            if not line.startswith("|") or line.startswith("|---"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) != 4 or cells[0] == "Node":
                continue
            name, resp, owned, pins = cells
            has_tag = "[target" in name or "[target" in resp
            if has_tag:
                self.assertIn("—", pins,
                              "node %r carries [target] but every pin reads real — drop the tag or "
                              "mark the missing pin with an em-dash" % name)
            if pins.strip().startswith("—"):
                self.assertTrue(has_tag, "node %r has no real pin but no [target] mark" % name)


class TestLoaderStaysThin(unittest.TestCase):
    """Row 65 (M-029 extension): the milestone gate list carries the loader-stays-thin item."""

    def test_m1_names_loader_thin_item(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("the thin loader stays thin",
                       "must this hold before any pack file loads?",
                       "states the line count",
                       "migrates to its real home"):
            self.assertIn(phrase, spec, "SPEC M-1 lost the loader-stays-thin item: %s" % phrase)

    def test_m1_names_skill_creator_rewalk(self):
        """Row 130 (M-128): the milestone gate re-walks the pack's skills through
        skill-creator; findings folded or rejected with reason in a dated record;
        a new skill walks it at birth."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("the skill-making skill",
                       "with a written reason, in a dated record",
                       "walks this at birth"):
            self.assertIn(phrase, spec, "SPEC M-1 lost the skill-creator re-walk item: %s" % phrase)
        import glob
        recs = glob.glob(os.path.join(ROOT, "docs", "audit", "*skill-creator*"))
        self.assertTrue(recs, "no dated skill-creator walk record in docs/audit/ (M-128)")


class TestWorkerContract(unittest.TestCase):
    """Row 59 (M-095): the worker contract — ownership narrowed to the brief, sibling files
    fence-benign, session lines ride the brief, failed acceptance escalates one logged tier."""

    def test_craft_ladder(self):
        """Row 124 (M-120, INV-33): every pipeline step is worked in its craft's
        mindset; the step->craft ladder's one home is build-pipeline."""
        spec = read("PRODUCT_SPEC.md")
        flat_spec = " ".join(spec.split())
        for needle in (
            "craft's standards",
            "INV-33",
        ):
            self.assertIn(needle, flat_spec, "SPEC missing: %s" % needle)
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        flat_pipe = " ".join(pipeline.split())
        for needle in (
            "The craft ladder — whose head you wear at each step",
            "a strong product manager",
            "QA automation lead",
            "the visitor's own fresh eyes, the builder's own view set aside",
            "a careful release hand",
        ):
            self.assertIn(needle, flat_pipe, "build-pipeline missing: %s" % needle)
        matrix = read("TEST_MATRIX.md")
        self.assertIn("test_craft_ladder", matrix, "M-120 must pin this test (row 124)")

    def test_brief_carries_ledger_and_clock(self):
        """Row 123 (M-119, ACT-3): every worker brief carries the problem-ledger
        walk and the clock read at briefing."""
        spec = read("PRODUCT_SPEC.md")
        flat_spec = " ".join(spec.split())
        for needle in (
            "brief arms the worker for the workshop",
            "carries the clock",
        ):
            self.assertIn(needle, flat_spec, "SPEC ACT-3 missing: %s" % needle)
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        flat_pipe = " ".join(pipeline.split())
        for needle in (
            "the worker never hunts context",
            "WATCHED-line duty",
            "carries the CLOCK",
            "never an invented hour",
        ):
            self.assertIn(needle, flat_pipe, "build-pipeline missing: %s" % needle)
        matrix = read("TEST_MATRIX.md")
        self.assertIn("test_brief_carries_ledger_and_clock", matrix,
                      "M-119 must pin this test (row 123)")

    def test_worker_contract_stated(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("The worker contract",
                       "narrowed to the files its brief names",
                       "fence-benign",
                       "ride into the brief verbatim",
                       "escalates one tier with a logged line",
                       "[ACT-3]"):  # "It never retries silently on the same tier, and never skips a rung"
            self.assertIn(phrase, spec, "SPEC ACT-3 lost the worker-contract clause: %s" % phrase)
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        for phrase in ("The worker contract (SPEC ACT-3)",
                       "fence alarms on foreign sessions",
                       "never resolves the settings ladder itself",
                       "escalates exactly ONE tier every time, with a logged line covering the move"):
            self.assertIn(phrase, bp, "build-pipeline lost the worker-contract elaboration: %s" % phrase)

    def test_routing_rule(self):
        """Row 56 (M-175, INV-69): the model router — a unit of work's tier is PROPOSED
        (judgment→senior, mechanical→worker), the economy rung moves the threshold, and
        the senior may override per wish with the override logged (D-2 decided advisory)."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("The routing rule",
                       "proposes the cheapest tier that can pass the brief",
                       "proposes the senior",
                       "economy rung moves the threshold",
                       "The proposal is advisory",
                       "proposed tier → chosen tier → why"):
            self.assertIn(phrase, spec, "SPEC INV-69 lost the routing rule: %s" % phrase)
        # D-2 is decided, no longer open
        self.assertNotIn("tier routing override | Open decisions", spec,
                         "D-2 still reads as an open override choice — row 56 decides it")
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        for phrase in ("The routing rule (SPEC INV-69)",
                       "propose the cheapest tier that can pass the brief",
                       "economy rung moves the threshold",
                       "proposed tier → chosen tier → why"):
            self.assertIn(phrase, bp, "build-pipeline lost the routing-rule elaboration: %s" % phrase)
        matrix = read("TEST_MATRIX.md")
        self.assertIn("test_routing_rule", matrix, "M-175 must pin this test (row 56)")

    def test_parameter_default(self):
        """Row 172 (M-176, INV-70): a tunable parameter is set by the agent to a
        sensible default and TOLD (never asked), carrying the taste-told law (INV-31)
        to numeric/config knobs; the agent moves every task it can (INV-4); and where
        the human GRANTS it, the agent pushes to prod on its own certification (M-6)."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("A tunable parameter is set to a sensible default and told, never asked",
                       "never stalls a task on a knob it can reasonably set",
                       "[INV-70]",  # "at most the parameter gets updated together later, and re-asking is never owed"
                       "the agent ships to prod on its own certification once the work is sound"):
            self.assertIn(phrase, spec, "SPEC INV-70 lost: %s" % phrase)
        index = spec.split("Formal index", 1)[1]
        self.assertIn("INV-70", index, "INV-70 missing from the Formal index")
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("tunable parameter", bp,
                      "build-pipeline lost the parameter-default elaboration (INV-70)")
        matrix = read("TEST_MATRIX.md")
        self.assertIn("test_parameter_default", matrix, "M-176 must pin this test (row 172)")


class TestBootstrapScaffold(unittest.TestCase):
    """Row 62 (M-034 extension): the bootstrap ships a runnable suite scaffold that defines green
    for landing #1. Verified BY DEED: a simulated bootstrap in a temp dir runs the shipped scaffold
    — green when the copy is filled, red when a placeholder survives."""

    def _bootstrap(self, tmp, fill=True):
        import shutil
        os.makedirs(os.path.join(tmp, "tests"))
        for name in ("PRODUCT_SPEC", "ARCHITECTURE", "TEST_MATRIX", "ROADMAP", "JOURNAL", "NEXT_STEPS"):
            src = os.path.join(ROOT, "templates", "%s.template.md" % name)
            with open(src, encoding="utf-8") as f:
                body = f.read()
            if fill:
                body = body.replace("[Project Name]", "demo").replace(
                    "(v0.1, [date])", "(v0.1, 2026-07-05)")
            with open(os.path.join(tmp, "%s.md" % name), "w", encoding="utf-8") as f:
                f.write(body)
        shutil.copy(os.path.join(ROOT, "templates", "test_scaffold.template.py"),
                    os.path.join(tmp, "tests", "test_scaffold.py"))

    def test_scaffold_bootstrap_runs(self):
        import subprocess
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            self._bootstrap(tmp, fill=True)
            r = subprocess.run(["python3", "-m", "unittest", "discover", "tests"],
                               cwd=tmp, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0,
                             "scaffold not green on a filled bootstrap:\n%s" % r.stderr)
        with tempfile.TemporaryDirectory() as tmp:
            self._bootstrap(tmp, fill=False)
            r = subprocess.run(["python3", "-m", "unittest", "discover", "tests"],
                               cwd=tmp, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0,
                                "scaffold stayed green on an UNFILLED bootstrap — placeholders "
                                "must be red")

    def test_spec_states_bootstrap_order(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("The version-control gate runs first",
                       "[INV-8]",  # "a gate can't protect files older than itself" / no landing into an unversioned host
                       "plus the suite scaffold",
                       "defines what \"green\" means for landing #1",
                       "a leftover placeholder counts as red",
                       "never impose them, plain words first"):  # hooks offered at bootstrap exactly as at adoption
            self.assertIn(phrase, spec, "SPEC lost the bootstrap-order clause: %s" % phrase)


class TestSkillSync(unittest.TestCase):
    """Row 66 (M-096): the dev-machine sync is a named tool with a spoken report, not a habit."""

    def test_sync_skills_script(self):
        import subprocess
        import tempfile
        script = os.path.join(ROOT, "scripts", "sync-skills.sh")
        self.assertTrue(os.access(script, os.X_OK), "sync-skills.sh not executable")
        with tempfile.TemporaryDirectory() as tmp:
            r = subprocess.run(["bash", script, tmp], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("absent ->", r.stdout, "first sync must report absent -> version")
            self.assertIn("RE-READ", r.stdout, "the A-7 trigger line is the tool's whole point")
            self.assertTrue(os.path.isfile(os.path.join(tmp, "live-spec-base", "SKILL.md")),
                            "base skill not synced")
            r2 = subprocess.run(["bash", script, tmp], capture_output=True, text=True)
            self.assertEqual(r2.returncode, 0, r2.stderr)
            self.assertIn("everything fresh", r2.stdout, "second run must be a no-op that says so")

    def test_spec_states_skill_sync(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("keeps its skills fresh by a named step, run deliberately",
                       "sync-skills.sh",
                       "reports every version change old → new",
                       "A hand-copy is the anti-pattern the tool retires"):
            self.assertIn(phrase, spec, "SPEC lost the skill-sync clause: %s" % phrase)


class TestPackUpdateCheck(unittest.TestCase):
    """Row 136 (M-131, E-25): once a day the machine asks the public repo whether the pack
    moved; propose-never-install, forward only, honest offline skip naming the address."""

    def _run(self, tmp, remote=None, installed="0.8.40", stamp_content=None, force=True):
        import subprocess
        script = os.path.join(ROOT, "scripts", "check-pack-update.sh")
        inst = os.path.join(tmp, "VERSION")
        with open(inst, "w") as f:
            f.write(installed)
        stamp = os.path.join(tmp, "stamp")
        if stamp_content is not None:
            with open(stamp, "w") as f:
                f.write(stamp_content)
        cmd = ["bash", script, "--installed-file", inst, "--stamp-file", stamp]
        rf = os.path.join(tmp, "REMOTE" if remote is not None else "no-such-file")
        if remote is not None:
            with open(rf, "w") as f:
                f.write(remote)
        cmd += ["--remote-file", rf]
        if force:
            cmd.append("--force")
        r = subprocess.run(cmd, capture_output=True, text=True)
        return r, stamp

    def test_pack_update_check(self):
        import datetime
        import tempfile
        script = os.path.join(ROOT, "scripts", "check-pack-update.sh")
        self.assertTrue(os.access(script, os.X_OK), "check-pack-update.sh not executable (E-25)")
        with tempfile.TemporaryDirectory() as tmp:
            # newer remote -> the spoken proposal: versions, pointer, road, proposal-only
            r, stamp = self._run(tmp, remote="9.9.9")
            self.assertEqual(r.returncode, 0, r.stderr)
            for needle in ("PACK UPDATE AVAILABLE: 9.9.9", "0.8.40", "JOURNAL.md",
                           "install.sh", "PROPOSAL ONLY"):
                self.assertIn(needle, r.stdout, "proposal missing: %s" % needle)
            self.assertTrue(os.path.isfile(stamp), "a successful check must write the stamp")
        with tempfile.TemporaryDirectory() as tmp:
            r, _ = self._run(tmp, remote="0.8.40")
            self.assertIn("up to date", r.stdout)
        with tempfile.TemporaryDirectory() as tmp:
            # OLDER remote (the dev machine ahead mid-work) -> forward only
            r, _ = self._run(tmp, remote="0.1.0")
            self.assertIn("up to date", r.stdout, "ahead-of-public must never propose a downgrade")
            self.assertNotIn("UPDATE AVAILABLE", r.stdout)
        with tempfile.TemporaryDirectory() as tmp:
            # unreadable remote -> honest skip NAMING the address, stamp left unwritten
            r, stamp = self._run(tmp, remote=None)
            self.assertEqual(r.returncode, 0, "offline must never block")
            self.assertIn("skipped", r.stdout)
            self.assertIn("no-such-file", r.stdout, "the skip line must name the address it tried")
            self.assertFalse(os.path.isfile(stamp), "an offline day must leave the stamp unwritten")
        with tempfile.TemporaryDirectory() as tmp:
            # same-day stamp -> quiet daily throttle
            today = datetime.date.today().isoformat()
            r, _ = self._run(tmp, remote="9.9.9", stamp_content=today, force=False)
            self.assertIn("already ran today", r.stdout)
            self.assertNotIn("UPDATE AVAILABLE", r.stdout)

    def test_spec_states_update_check(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for phrase in ("check-pack-update.sh", "once a day", "never installs anything",
                       "naming the address it tried", "never a downgrade", "E-25"):
            self.assertIn(phrase, spec, "SPEC lost the update-check clause: %s" % phrase)


class TestStandaloneTemplatePointers(unittest.TestCase):
    """Row 67 (M-097/M-098): a skill installed standalone must still resolve its template
    references — the pointers name the pack repo, no in-skill copies (D-4: a copy forks the truth)."""

    def test_standalone_template_pointers(self):
        for rel in ("skills/spec-author/SKILL.md", "skills/build-pipeline/SKILL.md"):
            body = re.sub(r"\s+", " ", read(rel))
            if ".template." not in body:
                continue
            self.assertIn("github.com/happysasha18/live-spec", body,
                          "%s names templates but not their resolvable home (row 67)" % rel)
            self.assertIn("a copy would fork the truth", body,
                          "%s lost the no-in-skill-copies rationale" % rel)
        for skill_dir in ("spec-author", "build-pipeline"):
            path = os.path.join(ROOT, "skills", skill_dir, "templates")
            self.assertFalse(os.path.isdir(path),
                             "in-skill template copies appeared in %s — D-4 forbids the fork" % skill_dir)


class TestMinedGapFolds(unittest.TestCase):
    """Row 12's remaining gaps, folded one landing each (session 9). Each test pins one fold to the
    shipped skill text; the mining map in the private playbook records the same fold by number."""

    def test_gap4_recurring_bug_escalates(self):
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        for phrase in ("A RECURRING bug re-doors to feature",
                       "missing an INVARIANT",
                       "grep JOURNAL.md for the area's name"):
            self.assertIn(phrase, bp, "build-pipeline lost the recurring-bug escalation: %s" % phrase)

    def test_gap10_step5_both_sides(self):
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("every row states BOTH sides — what the fact DOES and what it must NEVER do", bp,
                      "build-pipeline step 5 lost the DO+NEVER instruction (INV-6)")
        self.assertIn("a row without it is a derivation defect", bp)

    def test_gap9_prover_domain_language_lens(self):
        pp = re.sub(r"\s+", " ", read("skills/product-prover/SKILL.md"))
        for phrase in ("Domain language on every user-facing surface",
                       "read them as the USER would",
                       "a leaked internal word is a finding"):
            self.assertIn(phrase, pp, "product-prover Phase 4 lost the domain-language lens: %s" % phrase)

    def test_gap6_delegation_savings_line(self):
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        for phrase in ("Every delegation reports its saving",
                       "roughly how much senior work it saved",
                       "quietly stopped delegating"):
            self.assertIn(phrase, bp, "build-pipeline lost the delegation-savings line: %s" % phrase)

    def test_gaps5_8_docs_discipline(self):
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        for phrase in ("The CHANGELOG speaks to the USER, the journal to the builder",
                       "one concrete example from real output",
                       "Function names, internal ids, and row numbers live in the journal instead",
                       "no doc pins a drifting version number in prose"):
            self.assertIn(phrase, bp, "build-pipeline step 9 lost the docs discipline: %s" % phrase)
        sa = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn("Pinning a drifting version number in prose", sa,
                      "spec-author anti-patterns lost the version-pin entry")


class TestCommunicatorTrigger(unittest.TestCase):
    """Row 68 (M-099): the communicator description fires on decisions and landing reports,
    and says what it is NOT for — the eval caught it loading on every passing status line."""

    def test_communicator_trigger_narrowed(self):
        head = "".join(read("skills/communicator/SKILL.md").splitlines(True)[:8])
        self.assertIn("NOT a reason to LOAD it: a passing mid-work narration line", head,
                      "communicator description lost its NOT-side (row 68; reworded at row 131 — "
                      "narration is rule 13's standing habit, never a load-trigger)")
        self.assertIn("landing or milestone is REPORTED", head,
                      "communicator description lost the narrowed report trigger")
        self.assertNotIn("before writing a status update", head,
                         "the over-trigger phrase is back — every status line would load the skill")


class TestProblemLedger(unittest.TestCase):
    """Row 100: the workshop's problem ledger (SPEC E-24, INV-23; matrix M-103/M-104/M-105)."""

    STATUSES = ["WATCHED", "OWNED", "AGREED NON-PROBLEM", "SOLVED"]

    def test_problems_template_shape(self):
        t = read("templates/PROBLEMS.template.md")
        for s in self.STATUSES:
            self.assertIn(s, t, "ledger template lost status %s" % s)
        low = t.lower()
        self.assertIn("signature", low, "ledger template lost the signature concept")
        self.assertIn("second occurrence", low, "ledger template lost the second-occurrence law")
        self.assertIn("ARCHIVED", t, "ledger template lost the dated ARCHIVED tail (prover row100 F3)")
        self.assertIn("silent retry", low, "ledger template lost the never-a-silent-retry side")

    def test_base_rule_problem_ledger(self):
        base = read("skills/live-spec-base/SKILL.md")
        # normalize whitespace: the rule's sentences wrap across hard line breaks
        low = " ".join(base.lower().split())
        self.assertIn("problem ledger", low, "base skill lost the workshop-noise rule (INV-23)")
        for phrase in ["watched", "second occurrence", "agreed non-problem",
                       "defect of the method", "silent retry", "bug lane"]:
            self.assertIn(phrase, low, "base rule lost its '%s' leg" % phrase)

    def test_done_claim_evidence_walk(self):
        """Row 101 (M-107, INV-25): a done-claim is answered as an evidence walk,
        wearing its method version; an absent installed set is said, never invented."""
        spec = read("PRODUCT_SPEC.md")
        self.assertIn("INV-25", spec)
        self.assertIn("walking the evidence", spec)
        skill = read(os.path.join("skills", "communicator", "SKILL.md"))
        for needle in (
            "claim → artifact → version",
            "walking the evidence",
            "method version",
            "an absent version is itself an honest answer, never an invented one",
            "INV-25",
        ):
            self.assertIn(needle, skill,
                          "communicator rule 11 missing: %s" % needle)

    def test_one_story_close_whole(self):
        """Row 102 (M-108/M-109, T-17/INV-26): one wish = one story at intake;
        a multi-leg row closes only whole; LIVE-STATE never compresses an open leg."""
        spec = read("PRODUCT_SPEC.md")
        for needle in ("T-17", "INV-26", "closes only whole"):
            self.assertIn(needle, spec)
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        for needle in (
            "One wish = one user story",
            "SPEC T-17",
            "A row closes only whole",
            "SPEC INV-26",
            "half-done is a status, never a landing",
        ):
            self.assertIn(needle, pipeline,
                          "build-pipeline missing: %s" % needle)
        self.assertIn("INV-26", read(os.path.join("templates", "NEXT_STEPS.template.md")))
        self.assertIn("INV-26", read(os.path.join("templates", "ROADMAP.template.md")))

    def test_capture_echo_and_board(self):
        """Row 105 (M-111/M-112, INV-27): every intake is echoed back in one sentence;
        every status report names each in-flight feature's pipeline station."""
        spec = read("PRODUCT_SPEC.md")
        for needle in ("INV-27", "echo", "status report"):  # register-invariant terms + anchor
            self.assertIn(needle, spec)
        comm = read(os.path.join("skills", "communicator", "SKILL.md"))
        for needle in (
            "The capture echo",
            "row number",
            "departures board",
            "pipeline STATION",
            "INV-27",
        ):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        self.assertIn("capture echo", pipeline,
                      "build-pipeline step zero must cite the capture echo")
        # Row 125 (M-112): the board names ALL NINE pipeline steps — prove
        # architecture and commit & show included; landed is the terminal
        # state, not a step. Lists wrap across lines, so compare flattened.
        stations = ("spec → prove → architecture → prove architecture → "
                    "matrix → test → code → verify → commit & show")
        matrix = read("TEST_MATRIX.md")
        for home, text in (("PRODUCT_SPEC.md", spec),
                           ("communicator SKILL.md", comm),
                           ("TEST_MATRIX.md", matrix)):
            flat = " ".join(text.split())
            self.assertIn(stations, flat,
                          "%s station list is missing a pipeline step (row 125)" % home)
            self.assertRegex(flat, r"terminal\b.{0,20}landed|landed\b.{0,40}terminal",
                             "%s must mark landed as the terminal state (row 125)" % home)

    def test_outcome_leads_law(self):
        """Row 116 (M-113, INV-28): the outcome does the talking — echo-names are plain
        descriptive phrases; handles and coined names only trail; one fact per sentence."""
        spec = read("PRODUCT_SPEC.md")
        for needle in ("INV-28", "never chose to learn", "one fact = one standalone sentence"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = read(os.path.join("skills", "communicator", "SKILL.md"))
        for needle in ("coined feature name", "INV-28", "One fact = one standalone sentence"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)
        base = read(os.path.join("skills", "live-spec-base", "SKILL.md"))
        self.assertIn("coined feature name", base,
                      "base rule 2 must name coined feature names as handles")

    def test_fit_walk_law(self):
        """Row 108 (M-114, INV-29): a feature is interrogated for product fit at intake."""
        spec = read("PRODUCT_SPEC.md")
        for needle in ("INV-29", "small prover on the wish itself", "FEATURE-FIT"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        author = read(os.path.join("skills", "spec-author", "SKILL.md"))
        for needle in ("The fit walk", "journey", "INV-29"):
            self.assertIn(needle, author, "spec-author missing: %s" % needle)
        prover = read(os.path.join("skills", "product-prover", "SKILL.md"))
        self.assertIn("FEATURE-FIT", prover, "prover missing its FEATURE-FIT mode")
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        self.assertIn("fit walk", pipeline, "pipeline step 1 must cite the fit walk")

    def test_visitor_walk_feel_pass(self):
        """Row 117 (M-115, INV-30): product-kind verify walks the visit and watches the feel."""
        spec = read("PRODUCT_SPEC.md")
        for needle in ("INV-30", "visitor walk", "feel pass"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        for needle in ("VISITOR WALK", "FEEL pass"):
            self.assertIn(needle, pipeline, "pipeline step-8 missing: %s" % needle)

    def test_default_expiry_law(self):
        """Rows 118+120 (M-116, INV-31): a taste default is TOLD at landing, never confirmed."""
        spec = read("PRODUCT_SPEC.md")
        for needle in ("INV-31", "told, never confirmed"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = read(os.path.join("skills", "communicator", "SKILL.md"))
        self.assertIn("unclaimed decision files", comm,
                      "communicator rule 10 missing the resume-sweep of decision answers")
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        self.assertIn("open `[default]`s", pipeline, "pipeline step 9 missing the defaults list")

    def test_decision_card_consequences(self):
        """Row 119 (M-117, INV-32): a decision card asks in consequences, not mechanisms."""
        spec = read("PRODUCT_SPEC.md")
        for needle in ("INV-32", "consequences; the mechanism trails"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = read(os.path.join("skills", "communicator", "SKILL.md"))
        self.assertIn("what the choice CHANGES for the person", comm,
                      "communicator rule 10 missing the consequence-first card law")

    def test_bookkeeping_never_list(self):
        """Row 126 (M-121, INV-28): bookkeeping numbers are never message content —
        translated ("tested clean", "saved"), trailing, or in the records; a direct
        question or the done-claim walk (INV-25) keeps the number as the answer."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("Bookkeeping numbers are handles too", "NEVER-list",
                       "speaks as the answer: the number itself is the content, this once"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("test count", "version string", "tested clean",
                       "asked substance"):
            self.assertIn(needle, comm, "communicator rule 8 missing: %s" % needle)

    def test_pre_report_walk(self):
        """Row 128 (M-122, INV-34): before any movement-end/milestone report the
        communicator rules are re-read and the draft passes phrase by phrase through
        the outside-reader question; trailing anchors stay legal."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-34", "The report law is walked — a live step each time.",
                       "gets explained in the reader's own words, or dropped"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("pre-report walk", "phrase by phrase", "INV-34"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_chat_timestamp_at_write_time(self):
        """Row 127 (M-123, INV-24 chat face): a human-facing timestamp is read off the
        clock at write time, never extrapolated; quoting a past recorded time stays legal."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("Chat timestamps", "at write time"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("read off the clock at write time", "never continued or extrapolated"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_working_narration(self):
        """Row 131 (M-124, INV-35): work is narrated while it runs — beats in plain
        roadmap terms, the reports' voice, the grind quiet; a narration line is chat,
        not a report."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-35", "third voice between the echo and the report",
                       "narration marks beats, never per-command commentary"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("Narrate the work while it runs", "A narration line is chat, lighter than a report",
                       "INV-35"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_live_status(self):
        """Row 166 (M-178, INV-71): where we are now is answerable in any seat — a NOW/NEXT
        status kept current in the chat (present in every seat), never relying on the harness's
        local-only task list; binds for every project live-spec runs."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("answerable at any moment, in any setting",
                       "the one surface present in every setting",
                       "[INV-71]",  # "It refreshes at every station change"
                       "every project the pack runs"):
            self.assertIn(needle, spec, "SPEC INV-71 lost: %s" % needle)
        self.assertIn("INV-71", spec.split("Formal index", 1)[1], "INV-71 missing from the index")
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("Live status, any seat", "never the status's home"):
            self.assertIn(needle, comm, "communicator lost the live-status rule: %s" % needle)
        self.assertIn("test_live_status", read("TEST_MATRIX.md"), "M-178 must pin this test")

    def test_narration_three_teeth(self):
        """Row 139 (M-124, INV-35 grown): identity — every beat names the wish and
        station in hand; digest — a station's completion is a beat digesting what the
        station produced (a worker-closed station is the senior's beat); heartbeat — a
        beatless stretch past ~10 minutes [default] names what grinds. Both homes carry
        the teeth; digests never speak in counters (INV-28 seam)."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("**IDENTITY:**",
                       "a station's completion is itself a beat by law",
                       "station a delegated worker closed becomes the senior's beat",
                       "beatless stretch past ~10 minutes owes its heartbeat [default]",
                       "token and test counts stay bookkeeping"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("Identity", "Digest", "Heartbeat",
                       "which wish is in hand and which station it stands at",
                       "digests what the station produced",
                       "worker-closed station becomes the senior's beat",
                       "beatless stretch past ~10 minutes owes its heartbeat [default]",
                       "never a test count"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_offline_window(self):
        """Row 138 (M-138, INV-35): the heartbeat's offline-window face — before a
        stretch needing nothing from the human, narration says he may step away, an
        honest range, and what he is needed for at its end; the needed-again beat is
        a chat line awaiting his return, never a summons; the superseded fence
        sentence survives in neither home."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("offline window",
                       "he may step away, an honest range for how long",
                       "never a guess dressed as a promise",
                       "a chat line awaiting his return, never a summons",
                       "overrun, done sooner, or blocked on his word alone",
                       "no offline sentence fires when the very next beat needs the human"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("Offline window", "may step away", "honest range",
                       "guess is never dressed as a promise",
                       "a chat line awaiting his return, never a summons"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)
        for name, home in (("SPEC", spec), ("communicator", comm)):
            self.assertNotIn("its own promised law (queue row 138)", home,
                             "%s still carries the superseded row-138 fence sentence" % name)

    def test_his_word_read_right(self):
        """Row 145 (M-139, INV-42): a phrasing he killed stays killed — the kill-list
        written in the artifact's project records, never only session memory; his
        vivid phrase adopted only as meant — sarcasm is not instruction."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-42", "in every later draft",
                       "not only in session memory",
                       "mockery of a bad draft"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("stays killed", "kill-list",
                       "Sarcasm is not instruction",
                       "Never keep it only in session memory"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_prototype_norm_pointer(self):
        """Row 109 (M-140, INV-43): an approved prototype is the norm — the clause
        cites `norm: <path>` (frozen into docs/norms/), the code step opens the
        artifact and records a plan-vs-prototype diff line, a mockup-first entry
        condition cancels only by the human naming it, and the prover carries the
        norm lens."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-43", "`norm: <path>`", "docs/norms/",
                       "a missing line = review defect",
                       "only by the human naming it"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        author = re.sub(r"\s+", " ", read(os.path.join("skills", "spec-author", "SKILL.md")))
        for needle in ("`norm: <path>`", "docs/norms/", "frozen copy",
                       "a pointer into a live prototype home would break it"):
            self.assertIn(needle, author, "spec-author missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("plan-vs-prototype diff", "entry: mockup-first",
                       "only by the human naming it", "OPEN the artifact before building"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)
        prover = re.sub(r"\s+", " ", read(os.path.join("skills", "product-prover", "SKILL.md")))
        for needle in ("`norm: <path>`", "contradicting its own artifact"):
            self.assertIn(needle, prover, "product-prover missing: %s" % needle)

    def test_shopfront_fresh_at_push(self):
        """Row 146 (M-141, INV-44): a version push re-opens the shopfront — README
        claims match the pushed truth, kind-owed visuals ride along, the landing
        report carries the outcome line."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-44", "the shopfront rides every push",
                       "shopfront checked — current",
                       "Find a stale claim and fix it before the push"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pub = re.sub(r"\s+", " ", read(os.path.join("skills", "publish", "SKILL.md")))
        for needle in ("any push that ships a new version",
                       "shopfront checked — current",
                       "even when the diff never touched a doc"):
            self.assertIn(needle, pub, "publish missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        self.assertIn("shopfront", pipe, "build-pipeline step 9 missing the shopfront pointer")

    def test_push_gate_reach_law(self):
        """Row 147 (M-142, INV-45): the push gate derives its check-set from a
        declared, conservative, self-tested reach map."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-45", "reach map",
                       "CONSERVATIVE",  # "an unmapped or new file ⇒ the full suite"
                       "every check the diff can reach, green"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        self.assertIn("every check the diff can reach", pipe,
                      "build-pipeline missing the reach sentence")
        self.assertTrue(
            os.path.isfile(os.path.join(ROOT, "guardrails", "check-push-reach.sh")),
            "guardrails/check-push-reach.sh missing")

    def test_adversarial_verify_option(self):
        """Row 110 (M-144, INV-46): verify's adversarial option — a fresh-context
        checker re-derives from the spec sentences, never the worker's summary."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-46", "tasks completed, goal missed",
                       "never the worker's summary",
                       "MANDATORY when the code step was delegated"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("tasks completed, goal missed",
                       "TODO · FIXME · placeholder · lorem · hardcoded sample · empty function body",
                       "primary sources only, apart from the worker's summary or your own plan"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)

    def test_lanes_by_graph(self):
        """Row 149 (M-147, INV-49): lanes picked by a dependency graph, integration
        order declared at claim, tiny rows serial."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-49", "dependency graph", "rows ride serial",
                       "first-declared lands first"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("Lanes are picked by a graph", "rows ride serial",
                       "DECLARED at claim"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)

    def test_entry_symmetry(self):
        """Row 150 (M-148, INV-50): a conditionally-entered face owes a re-entry
        path or a written one-way; the prover carries the lens."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-50", "deliberate re-entry path", "until dismissed"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        prover = re.sub(r"\s+", " ", read(os.path.join("skills", "product-prover", "SKILL.md")))
        for needle in ("Entry symmetry", "A get with no set is a finding", "SPEC INV-50"):
            self.assertIn(needle, prover, "product-prover missing: %s" % needle)
        author = re.sub(r"\s+", " ", read(os.path.join("skills", "spec-author", "SKILL.md")))
        self.assertIn("re-entry path", author,
                      "spec-author journey lens missing the re-entry clause")

    def test_artifact_passport(self):
        """Row 151 (M-149, INV-51): anything handed to the human leads with its
        passport — project name + the read contract."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-51", "never only the URL", "just an update"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("passport", "needs your word: what, by when", "never only the URL"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_windows_accumulate(self):
        """Row 152 (M-150, INV-52): during an away-stretch windows accumulate to one
        end-of-stretch opening."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-52", "accumulate on ONE page", "refreshed in place"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("windows accumulate", "refreshed in place",
                       "opens that one window once"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_brief_trio_laws(self):
        """Rows 111-113 (M-151..153, INV-53/54/55): a brief is born from read files,
        carries the closed HALT list, and is sized with paths, never bodies."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-53", "INV-54", "INV-55",
                       "current state · what changes · what must survive",
                       "two consecutive unexplained failures",
                       "never inlined file bodies"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("READING them in full", "closed HALT list",
                       "~300 lines", "never inlined file bodies"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)

    def test_limp_never_dams_flow(self):
        """Row 153 (M-155, INV-56): a known owned problem parks; unrelated lanes
        roll; batch servicing for mechanically-owned defects, never ceremony."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-56", "never dams the flow", "serviced in batch",
                       "never a per-instance ceremony"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        base = re.sub(r"\s+", " ", read(os.path.join("skills", "live-spec-base", "SKILL.md")))
        for needle in ("never dams the flow", "serviced in BATCH", "known limp"):
            self.assertIn(needle, base, "base missing: %s" % needle)

    def test_stretch_end_unmissable(self):
        """Row 154 (M-156, INV-57): the stretch's end is one short final line, last,
        after every tool call — delivery, not existence."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-57", "Delivery is the rule; existence alone does not satisfy it",
                       "the last rendered thing is one short final line"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("final line comes LAST", "what closed", "when the agent wakes"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_promoter_harvest_trio(self):
        """Rows 158+160+162 (M-157..159, INV-58/59/60): frozen approved text; no
        question twice + converging dialogues; taste asks carry a mined proposal."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-58", "INV-59", "INV-60",
                       "does not rewrite the surrounding text",
                       "a record already answers is a defect",
                       "arrives with work already done"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("Approved text is frozen", "round N+1 carries only new material",
                       "mined the material first", "closes forever"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_process_cost_scales(self):
        """Row 155 (M-160, INV-61): the pre-push re-check scales its form to the
        delta; rigor and the safety net never scale."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-61", "short-form record of three lines",
                       "never per tiny row", "quality itself, never"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("scales to the delta", "three-line SHORT-FORM record",
                       "once per landing batch"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)
        prof = re.sub(r"\s+", " ", read(os.path.join(".live-spec", "profile.md")))
        self.assertIn("FORM scaled by the delta", prof,
                      "host profile line not reconciled with INV-61")

    def test_sample_first_and_source_reopen(self):
        """Rows 156+157 (M-161/162, INV-62/63): smallest sample judged first;
        a rejected artifact reopens its source, never line-patches."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-62", "INV-63", "cheapest judgeable sample",
                       "the five-round trap"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("build smallest-first", "reopens its SOURCE",
                       "cheapest judgeable sample"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)

    def test_review_provenance_commentable(self):
        """Row 161 (M-163, INV-64): review surfaces carry per-claim provenance and
        take his pen — never a read-only wall."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("[INV-64]",  # "Inferences get flagged LOUDEST"
                       "commentable rather than a read-only wall"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("MY INFERENCE", "never a read-only wall",
                       "extended to review pages"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_kill_list_mechanical(self):
        """Row 159 (M-164, E-26): the kill-list template ships and the scanner
        guidance stands in guardrails."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("E-26", "this is its teeth"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        t = read(os.path.join("templates", "KILL_LIST.template.md"))
        for needle in ("NEVER removed", "Killed literal (exact)", "turns the suite RED"):
            self.assertIn(needle, t, "template missing: %s" % needle)
        g = read(os.path.join("guardrails", "README.md"))
        for needle in ("kill-list scanner", "KILL_LIST.template.md"):
            self.assertIn(needle, g, "guardrails README missing: %s" % needle)

    def test_onboarding_step(self):
        """Row 54 (M-165, B-3): the pack learns WHO it works with at setup —
        the profile found or founded, every line on the human's word."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("B-3", "[B-3]",  # "Learn who you're working with before any founding question resolves"
                       "a dropped proposal stays dropped",
                       "templates/profile.template.md"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        base = re.sub(r"\s+", " ", read(os.path.join("skills", "live-spec-base", "SKILL.md")))
        for needle in ("found or founded at setup", "profile.template.md",
                       "never onboards anyone"):
            self.assertIn(needle, base, "base missing: %s" % needle)
        adopt = re.sub(r"\s+", " ", read(os.path.join("adopt", "ADOPT.md")))
        for needle in ("Who am I working with", "profile.template.md"):
            self.assertIn(needle, adopt, "ADOPT.md missing: %s" % needle)
        t = read(os.path.join("templates", "profile.template.md"))
        for needle in ("on the human's word", "placeholder", "SPEC INV-9", "settings ladder"):
            self.assertIn(needle, t, "template missing: %s" % needle)

    def test_skill_discovery(self):
        """Row 165 (M-166, INV-65): search for an existing skill at setup and at
        every struggle; borrow by invoking, or by paraphrase with named credit."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-65", "Before reinventing a fix, search for an existing skill",
                       "Adopt or reject a found skill by name",
                       "Unlicensed text is never republished"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        base = re.sub(r"\s+", " ", read(os.path.join("skills", "live-spec-base", "SKILL.md")))
        for needle in ("Search for a skill before reinventing",
                       "credit the source by name"):
            self.assertIn(needle, base, "base missing: %s" % needle)
        adopt = re.sub(r"\s+", " ", read(os.path.join("adopt", "ADOPT.md")))
        self.assertIn("Skill search rides the setup", adopt, "ADOPT.md missing the setup arm")

    def test_test_author_skill(self):
        """Row 163 (M-167, E-27): the test method's one home — the test-author
        skill, wired from the pipeline's matrix and test steps."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("E-27", "the working skills (spec-author", "test-author"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        skill = re.sub(r"\s+", " ", read(os.path.join("skills", "test-author", "SKILL.md")))
        for needle in ("The level ladder", "Red first, proven", "Pin the skip-set",
                       "Normally invoked by build-pipeline"):
            self.assertIn(needle, skill, "test-author skill missing: %s" % needle)
        bp = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        self.assertIn("invoke `test-author`", bp, "build-pipeline missing the invoke wiring")
        readme = re.sub(r"\s+", " ", read("README.md"))
        self.assertIn("test-author", readme, "README missing the new skill")

    def test_showing_seat(self):
        """Row 168 (M-170, INV-67): the showing channel matches the session's seat —
        local window vs remote artifact page, detected and said."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-67", "matches where the session runs",
                       "a defect of the exchange"):
            self.assertIn(needle, spec, "SPEC missing seat-law fact: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("picked by the SEAT", "Detect the seat before the first show"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_snapshot_design(self):
        """Row 55 (M-169, E-7): the snapshot design decided — home, manifest,
        advance-at-landed for declared surfaces only, git history as the archive."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in (".live-spec/snapshot/", "advances at *landed*",
                       "undeclared surfaces keep their old baseline",
                       "git history is the archive",
                       "only the hash gets diffed"):
            self.assertIn(needle, spec, "SPEC missing snapshot-design fact: %s" % needle)
        decisions = spec.split("## Open decisions", 1)[1].split("## Formal index", 1)[0]
        self.assertIn("Decided 2026-07-07 (row 55)", decisions,
                      "D-3 not closed in the Open-decisions section")
        self.assertNotIn("snapshot retention: last-only (current pick) vs last-N", decisions,
                         "the old open D-3 wording survived the close")

    def test_project_kind(self):
        """Row 129 (M-125, INV-36): the project knows its own kind — asked at
        founding/orient, one home in the host profile, alive as the project evolves."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-36", "The project knows what kind of thing it is",
                       "never silently overrides an explicit profile line"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        base = re.sub(r"\s+", " ", read(os.path.join("skills", "live-spec-base", "SKILL.md")))
        for needle in ("`project.kind`", "asked at founding and at adoption"):
            self.assertIn(needle, base, "base missing: %s" % needle)
        adopt = re.sub(r"\s+", " ", read(os.path.join("adopt", "ADOPT.md")))
        self.assertIn("project.kind", adopt, "ADOPT.md missing the project-kind founding ask")
        prof = re.sub(r"\s+", " ", read(os.path.join(".live-spec", "profile.md")))
        self.assertIn("project.kind", prof,
                      "the pack's own host profile carries no project.kind line (dogfood)")

    def test_feature_map_placement(self):
        """Row 132 (M-126, INV-37): every wish is placed on the feature map at intake —
        spoken with the echo, written in the row, restructure only through a landing."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-37", "feature map", "restructure",   # register-invariant terms + anchor
                       "Re-carving the whole map is legal"):      # (unchanged, architecture section)
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("place on the product's map", "INV-37"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("place on the map", "changes feature X", "INV-37"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)

    def test_feature_map_on_demand(self):
        """Row 133 (M-127, INV-38): the whole feature map is readable on demand —
        read at ask-time off spec scenarios + header + queue, no third document,
        statuses at the [target] tag's own granularity, queued NEW wishes included."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-38", "Asking what the product does",
                       "[INV-38]",  # "one answer gives you the whole product map"
                       "the whole map only on request",
                       "a host with nothing to read", "queued NEW-verdict wishes included"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("feature map on demand", "no third document", "INV-38"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_parallel_lanes_law(self):
        """Rows 135+142 (M-129, T-18): up to three trains may roll without asking, a fourth on the
        human's word, one pen writes — the law in SPEC, carried by build-pipeline + base; the
        waiting lane readable on the board (communicator)."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("Trains may roll", "T-18", "At most three build lanes roll at once",
                       "a fourth lane opens only on the human's asked word",
                       "waiting for the pen says so and names the row it waits behind",
                       "pen-stage is never cut mid-edit",
                       "never against another lane's half-written draft"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("Trains, one pen", "SPEC T-18", "isolated tree",
                       "a fourth opens only on the human's asked word"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)
        base = re.sub(r"\s+", " ", read(os.path.join("skills", "live-spec-base", "SKILL.md")))
        for needle in ("SPEC T-18", "PEN"):
            self.assertIn(needle, base, "base missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        self.assertIn("waiting behind row", comm, "communicator missing the waiting-lane board face")

    def test_architecture_owes_budgets(self):
        """Row 143 (M-136, INV-41): a user-facing surface's architecture states measurable
        quality budgets + an instrumentation home; carried by build-pipeline + spec-author."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("ask \"what does quality mean here, in numbers?\"", "INV-41",
                       "measurable quality budgets",
                       "instrumentation home",
                       "the project's KIND proposes the dimensions",
                       "a quality with no honest number is said by name",
                       "no budgets + no instrumentation home = derivation defect",
                       "set on the human's word at the surface's first budget landing"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("SPEC INV-41", "measurable quality budgets", "instrumentation home",
                       "WHAT is measurable comes from the project's KIND"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)
        author = re.sub(r"\s+", " ", read(os.path.join("skills", "spec-author", "SKILL.md")))
        for needle in ("SPEC INV-41", "budget sentence"):
            self.assertIn(needle, author, "spec-author missing: %s" % needle)

    def test_task_list_plain_words(self):
        """Row 144 (M-137, INV-28): the session's task list speaks plain product English,
        codes only trail — the rule lives in communicator's language family."""
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("TASK LIST", "docs language", "codes, row numbers, and internal step names only trail"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_economy_ladder(self):
        """Row 140 (M-134/M-135, T-19/INV-40): the economy ladder — legal sheds per rung, the
        never-bend list, the rung moved only by the human's word; base carries the setting row."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("economy ladder", "`budget.pressure`", "full [default]",
                       "moved only by the human's word",
                       "the pack asks the economy rung, or tells the standing default",
                       "every taken shed named in the landing report",
                       "What never bends at any rung",
                       "a push still requires the batch's reach-scoped gate [INV-45] green at HEAD",
                       "red at batch end bisects by landing order",
                       "an explicit host line outlives any rung"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        base = re.sub(r"\s+", " ", read(os.path.join("skills", "live-spec-base", "SKILL.md")))
        for needle in ("budget.pressure", "economy ladder", "SPEC T-19"):
            self.assertIn(needle, base, "base missing: %s" % needle)

    def test_landing_purity(self):
        """Row 135 (M-130, INV-39): a landing commit carries exactly one row's delta."""
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for needle in ("INV-39", "a landing commit carries exactly one row's delta",
                       "landed-first wins, the later lanes re-verify",
                       "half of another train never rides a landing"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        self.assertIn("exactly one row's delta", pipe, "build-pipeline missing INV-39's clause")

    def test_install_backup_home(self):
        """Row 122 (M-118): installer backups live outside the live skills dir."""
        script = read("install.sh")
        self.assertIn("-attic", script, "install.sh must back up into an attic, not the live dir")
        self.assertNotIn('backup="$dest.bak_', script,
                         "install.sh still backs up inside ~/.claude/skills")

    def test_pack_own_ledger(self):
        led = read(".live-spec/PROBLEMS.md")
        rows = [l for l in led.splitlines()
                if l.startswith("| ") and not l.startswith("| Signature")]
        self.assertTrue(rows, "the pack's own ledger has no entries (dogfood, M-105)")
        for r in rows:
            self.assertRegex(r, r"\d{4}-\d{2}-\d{2}", "ledger entry without a date: %s" % r)
            self.assertTrue(any(s in r for s in self.STATUSES),
                            "ledger entry without a legal status: %s" % r)


class TestClockDiscipline(unittest.TestCase):
    """Row 103: time is read off the clock, never invented (SPEC INV-24, matrix M-106).
    Scope: file NAMES repo-wide, JOURNAL entry headings, ledger dates — prose quoting a
    past incident's wrong date stays legal (the journal describes defects, it doesn't repeat them)."""

    DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")

    def test_no_future_dated_stamps(self):
        import datetime
        today = datetime.date.today().isoformat()
        offenders = []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames
                           if d not in (".git", "__pycache__", "node_modules")]
            for name in filenames:
                for d in self.DATE.findall(name):
                    if d > today:
                        offenders.append(os.path.relpath(os.path.join(dirpath, name), ROOT))
        for line in read("JOURNAL.md").splitlines():
            if line.startswith("## "):
                for d in self.DATE.findall(line):
                    if d > today:
                        offenders.append("JOURNAL.md heading: %s" % line[:70])
        for line in read(".live-spec/PROBLEMS.md").splitlines():
            if line.startswith("| "):
                for d in self.DATE.findall(line):
                    if d > today:
                        offenders.append("ledger: %s" % line[:70])
        self.assertFalse(
            offenders,
            "future-dated stamps — the invented-time family (INV-24): %s" % offenders)


def _feature_coverage_gaps(tags, rows, real_nodes, real_test_defs):
    """Pure two-way checker for the feature-coverage trace (SPEC INV-73). tags = {F-id: heading} tagged
    in the spec; rows = coverage table rows [{feature, nodes, tests}]; real_nodes = node-name stems;
    real_test_defs = existing test fn names. Returns a list of gap strings — empty means clean."""
    gaps = []
    tag_ids = set(tags)
    row_ids = [r["feature"] for r in rows]
    for fid in sorted(tag_ids - set(row_ids)):
        gaps.append("tagged feature with no coverage row: %s" % fid)
    for fid in sorted(set(row_ids) - tag_ids):
        gaps.append("coverage row for an untagged feature: %s" % fid)
    for fid in sorted(f for f in set(row_ids) if row_ids.count(f) > 1):
        gaps.append("duplicate coverage row: %s" % fid)
    for r in rows:
        if not r["nodes"]:
            gaps.append("%s names no implementer node" % r["feature"])
        for n in r["nodes"]:
            if n not in real_nodes:
                gaps.append("%s names a non-node implementer: %s" % (r["feature"], n))
        if not r["tests"]:
            gaps.append("%s names no test" % r["feature"])
        for t in r["tests"]:
            if t not in real_test_defs:
                gaps.append("%s names a missing test: %s" % (r["feature"], t))
    return gaps


class TestFeatureCoverage(unittest.TestCase):
    """The feature layer above the anchor matrix — the spec-format-by-project-type landing
    (docs/spec-format-by-project-type.md; SPEC E-29, INV-73). A spec's PRIMARY UNIT is a parameter of the
    project type; live-spec's unit is its person-facing scenario, so each such heading carries an inline
    [feature: F-x] tag, and ARCHITECTURE.md's 'Feature coverage' table maps every unit to its implementer
    node(s) and a real test. Two-way, string/structure level (matrix M-180/M-181)."""

    # the person-facing scenarios the pack promises; each MUST carry its tag — a scenario stripped of its
    # [feature:] tag goes red (the reverse guard)
    SCENARIOS = {
        "F-wish": "Throwing a wish",
        "F-prototype": "A prototype stays a sketch",
        "F-publish": "Publishing",
        "F-feedback": "Sending feedback in",
        "F-feature-map": "Asking what the product does",
        "F-bug": "When a bug cuts the line",
        "F-problem-ledger": "When the workshop itself misbehaves",
        "F-bootstrap": "Starting a new project",
        "F-adoption": "Attaching to a live project",
    }

    def feature_tags(self):
        """{F-id: heading text} from PRODUCT_SPEC.md headings carrying an inline [feature: F-x] tag."""
        spec = read("PRODUCT_SPEC.md")
        tags = {}
        for m in re.finditer(r"^#{2,4}\s+(.*?)\s*\[feature:\s*(F-[a-z-]+)\]\s*$", spec, re.M):
            tags[m.group(2)] = m.group(1).strip()
        return tags

    def coverage_rows(self):
        """[{feature, nodes, tests}] from ARCHITECTURE.md's Feature coverage table."""
        arch = read("ARCHITECTURE.md")
        if "## Feature coverage" not in arch:
            return []
        section = arch.split("## Feature coverage", 1)[1].split("\n## ", 1)[0]
        rows = []
        for line in section.splitlines():
            if line.startswith("|") and not line.startswith("|---") and "implemented by" not in line:
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) == 3 and re.match(r"F-[a-z-]+$", cells[0]):
                    nodes = [n.strip(" `") for n in re.split(r"[,·]", cells[1]) if n.strip(" `")]
                    tests = re.findall(r"test_\w+", cells[2])
                    rows.append({"feature": cells[0], "nodes": nodes, "tests": tests})
        return rows

    def real_test_defs(self):
        tests_dir = os.path.join(ROOT, "tests")
        blob = "\n".join(read(os.path.join("tests", f)) for f in sorted(os.listdir(tests_dir))
                         if f.startswith("test_") and f.endswith(".py"))
        return set(re.findall(r"def (test_\w+)", blob))

    def real_nodes(self):
        return {n.split(" [")[0] for n in architecture_nodes()}

    def test_every_scenario_carries_its_feature_tag(self):
        tags = self.feature_tags()
        for fid, heading in self.SCENARIOS.items():
            self.assertIn(fid, tags, "scenario %r lost its [feature: %s] tag" % (heading, fid))
            self.assertIn(heading, tags[fid],
                          "tag %s sits on %r, expected the %r heading" % (fid, tags[fid], heading))

    def test_feature_coverage_two_way(self):
        gaps = _feature_coverage_gaps(self.feature_tags(), self.coverage_rows(),
                                      self.real_nodes(), self.real_test_defs())
        self.assertEqual(gaps, [], "feature-coverage trace broke: %s" % gaps)

    def test_spec_and_spec_author_carry_the_format(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("[E-29]", spec, "SPEC lost the feature-coverage-trace anchor")
        self.assertIn("[INV-73]", spec, "SPEC lost the two-way coverage invariant anchor")
        self.assertIn("feature-coverage trace", spec.lower(),
                      "SPEC lost the feature-coverage-trace machine name")
        self.assertIn("primary unit", spec.lower(), "SPEC lost the primary-unit notion")
        sa = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn("primary unit", sa.lower(), "spec-author lost the primary-unit-by-type format")
        self.assertIn("[feature:", sa, "spec-author lost the inline feature-tag mechanic")
        for unit in ("feature", "command", "guarantee", "argument"):
            self.assertIn(unit, sa.lower(), "spec-author unit table lost the %s row" % unit)

    def test_stripped_coverage_goes_red(self):
        # the never side, permanent: a tagged-but-unmapped unit, an orphan row, a fake node and a fake
        # test must all be caught by the pure checker
        tags = {"F-wish": "Throwing a wish", "F-x": "Ghost"}
        rows = [{"feature": "F-wish", "nodes": ["build-pipeline"],
                 "tests": ["test_every_scenario_carries_its_feature_tag"]},
                {"feature": "F-orphan", "nodes": ["nope-node"], "tests": ["test_ghost_fn"]}]
        gaps = _feature_coverage_gaps(tags, rows, self.real_nodes(), self.real_test_defs())
        self.assertTrue(any("no coverage row: F-x" in g for g in gaps),
                        "the checker missed a tagged-but-unmapped unit — no teeth")
        self.assertTrue(any("untagged feature: F-orphan" in g for g in gaps),
                        "the checker missed an orphan coverage row")
        self.assertTrue(any("non-node implementer" in g for g in gaps),
                        "the checker missed a fake implementer node")
        self.assertTrue(any("missing test" in g for g in gaps),
                        "the checker missed a fake test name")


class TestSmallDesignHoles(unittest.TestCase):
    """The seven small design holes from the 2026-07-09 full re-prove (ROADMAP rows 173-179 = findings
    F5,F6,F7,F8,F9,F10,F4). Each is a SPEC/ARCHITECTURE prose clarification of an EXISTING invariant, so
    no new anchor — the test asserts the clause now stands. Record:
    docs/prover/2026-07-09-full-reprove-session29-body.md."""

    def spec(self):
        return re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))

    def test_173_deferred_trigger_evaluation_point(self):
        s = self.spec()
        self.assertIn("re-scan every deferred queue row's revisit trigger", s,
                      "milestone gate lost the deferred-trigger re-scan (F5)")
        self.assertIn("a fired trigger returns the row to the runnable queue", s)

    def test_174_bug_parked_resume_refences(self):
        s = self.spec()
        self.assertIn("re-fences and re-proves its delta against the now-committed truth", s,
                      "T-9 resume lost the re-fence/re-prove step (F6)")
        self.assertIn("never integrated blind", s)

    def test_175_bug_during_running_milestone(self):
        s = self.spec()
        self.assertIn("A milestone gate is one indivisible pen-stage", s,
                      "SPEC lost the milestone-as-indivisible-pen-stage rule (F7)")
        self.assertIn("waits for the gate to finish rather than preempting a half-run audit", s)

    def test_176_milestone_hold_state_named(self):
        s = self.spec()
        self.assertIn("held-for-milestone", s, "SPEC lost the distinct milestone-hold state name (F8)")
        self.assertIn("named apart from bug-", s, "milestone-hold not distinguished from bug-parked")

    def test_177_lane_claim_tiebreaker(self):
        s = self.spec()
        self.assertIn("the lower inbox session token breaks the tie", s,
                      "SPEC lost the lane-claim tie-breaker ordering key (F9)")
        self.assertIn("mutual back-off cannot happen", s)

    def test_178_tight_rung_rollback(self):
        s = self.spec()
        self.assertIn("reverts the batch to its last green base and re-applies the clean landings", s,
                      "economy ladder lost the tight-rung rollback path (F10)")
        self.assertIn("HEAD never sits red across a breakpoint", s)

    def test_179_architecture_inv67_ownership_prose(self):
        arch = re.sub(r"\s+", " ", read("ARCHITECTURE.md"))
        self.assertNotIn("the invariant's owner is the guardrails node, INV-67", arch,
                         "ARCHITECTURE still reads as if guardrails owns INV-67 (F4)")
        self.assertIn("INV-67 (the showing channel matches the session's seat)", arch,
                      "INV-67 no longer reads as communicator's own")


class TestAuthoringTerminology(unittest.TestCase):
    """The 1.0 RUN item 4: plain-language rename (the coined 'needle' → 'traceability check-phrase') and
    the standard-vocabulary crosswalk grounding the pack's terms in the requirements-engineering corpus
    (ISO 29148, arc42, C4). String level."""

    def test_extract_tool_speaks_check_phrase(self):
        tool = read("scripts/needle-extract.py")
        self.assertIn("def trace_phrases_in", tool, "the extract tool kept the coined 'needles_in'")
        self.assertNotIn("def needles_in", tool)
        self.assertIn("check-phrase", tool, "the tool no longer speaks 'check-phrase'")

    def test_no_needle_metaphor_in_authoring_docs(self):
        # the live authoring surfaces speak the plain term, never the old metaphor
        for rel in ("skills/spec-author/SKILL.md", "docs/prose-quality-gate-design.md"):
            body = read(rel).lower()
            self.assertNotIn("needle", body, "%s still carries the coined 'needle' metaphor" % rel)
            self.assertIn("check-phrase", body, "%s lost the plain 'check-phrase' term" % rel)

    def test_standard_vocabulary_crosswalk(self):
        sa = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn("Standard vocabulary", sa, "spec-author lost the vocabulary crosswalk")
        for std in ("ISO 29148", "arc42", "C4"):
            self.assertIn(std, sa, "crosswalk lost the standard: %s" % std)
        self.assertIn("measurable or verifiable here", sa,
                      "crosswalk lost the borrowed-authority boundary")
        arch = re.sub(r"\s+", " ", read("ARCHITECTURE.md"))
        for std in ("C4", "arc42"):
            self.assertIn(std, arch, "ARCHITECTURE lost the %s lineage pointer" % std)


class TestArchitectureTiers(unittest.TestCase):
    """The 1.0 RUN item 5 (b): the ARCHITECTURE structure is proposed by project.kind (INV-36). The
    template carries a per-kind node-structure scaffold and build-pipeline step 3 points at it. String
    level."""

    def test_template_carries_per_kind_node_structure(self):
        tpl = re.sub(r"\s+", " ", read("templates/ARCHITECTURE.template.md"))
        self.assertIn("Node structure by project.kind", tpl,
                      "architecture template lost the per-kind node-structure scaffold")
        self.assertIn("INV-36", tpl, "the scaffold no longer keys off project.kind (INV-36)")
        for kind in ("fullstack app", "backend service", "CLI", "skill pack", "book"):
            self.assertIn(kind, tpl, "per-kind scaffold lost the %s row" % kind)
        # the scaffold-not-a-frame boundary: a node still earns its place by owning a fact
        self.assertIn("a speculative node is unbacked structure", tpl)
        # the two shapes the plain rows miss (learned from the 2026-07-09 tlvphoto read-only derivation)
        self.assertIn("derive-pipeline tier", tpl, "scaffold lost the data/ML derive-tier learning")
        self.assertIn("static-first", tpl, "scaffold lost the static-first + edge-backend blend learning")

    def test_build_pipeline_points_at_the_scaffold(self):
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("Node structure by project.kind", bp,
                      "build-pipeline step 3 lost the pointer to the per-kind scaffold")
        self.assertIn("PROPOSES the starting node structure", bp)


class TestArchitectureViews(unittest.TestCase):
    """Row 180 (reopened RUN item 5): the architecture doc owes a runtime view (INV-74) and a
    placement view (INV-75), the lens grows to six items, the template carries the sections, and
    the pack's own ARCHITECTURE.md models all of it. String level."""

    def test_spec_mandates_runtime_and_placement_views(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        for anchor in ("INV-74", "INV-75"):
            self.assertIn("| %s |" % anchor, spec, "Formal index lost %s" % anchor)
        self.assertIn("The architecture traces each flow at runtime.", spec)
        self.assertIn("The architecture says where everything runs.", spec)
        self.assertIn("where does this run", spec, "the placement view's at-a-glance question is gone")
        # both views scale by kind, and the duty binds forward
        self.assertIn("Both views scale by the project's kind", spec)

    def test_architecture_lens_is_six_items(self):
        # the lens's three homes all speak six items — the tlvphoto validation skipped budgets and
        # views exactly because the three-item lens never asked
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("That lens checks six things", spec)
        for home, needle in (
            ("skills/product-prover/SKILL.md", "runtime view"),
            ("skills/product-prover/SKILL.md", "placement"),
            ("skills/product-prover/SKILL.md", "instrumentation home"),
            ("skills/build-pipeline/SKILL.md", "runtime view"),
            ("skills/build-pipeline/SKILL.md", "placement view"),
        ):
            text = re.sub(r"\s+", " ", read(home)).lower()
            self.assertIn(needle.lower(), text,
                          "%s does not carry the lens item '%s'" % (home, needle))

    def test_template_carries_the_views(self):
        tpl = re.sub(r"\s+", " ", read("templates/ARCHITECTURE.template.md"))
        for section in ("## Runtime view", "## Placement view", "## Quality budgets",
                        "## Feature coverage"):
            self.assertIn(section, tpl, "architecture template misses the '%s' section" % section)
        # the per-kind flow unit, so "every flow the spec promises" is answerable for any kind
        for unit in ("visitor scenario", "one invocation per command",
                     "a wish through the skills", "one sentence"):
            self.assertIn(unit, tpl, "template's runtime view lost the per-kind flow unit: %s" % unit)
        # the runtime view cites seams, the payload/format stay the seam table's fact (one home)
        self.assertIn("cites the seam", tpl)
        # placement is first-class and readable at a glance
        self.assertIn("where does this run", tpl)

    def test_own_architecture_carries_views_and_budgets(self):
        arch = read("ARCHITECTURE.md")
        flat = re.sub(r"\s+", " ", arch)
        for section in ("## Runtime view", "## Placement view", "## Quality budgets"):
            self.assertIn(section, arch, "live-spec's own ARCHITECTURE.md misses '%s'" % section)
        # every feature in the coverage table walks in the runtime view
        coverage = arch.split("## Feature coverage", 1)[1].split("## ", 1)[0]
        runtime = arch.split("## Runtime view", 1)[1].split("## ", 1)[0]
        features = re.findall(r"^\| (F-[a-z-]+) \|", coverage, re.M)
        self.assertTrue(features, "feature coverage table parsed empty")
        for f in features:
            self.assertIn(f, runtime, "feature %s has no walk in the runtime view" % f)
        # budgets carry numbers and instrumentation homes
        self.assertIn("Instrumentation home", flat)
        self.assertIn("suite wall-time", flat)


class TestWorkerLiveness(unittest.TestCase):
    """Row 181 (INV-76): a background worker outlives a memory wipe — the resume protocol proves it
    dead or alive before any file is touched or a sibling spawned. String level."""

    def test_worker_liveness_protocol(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("| INV-76 |", spec, "Formal index lost INV-76")
        self.assertIn("proves it dead or alive", spec)
        # the two checks, with their told defaults
        self.assertIn("file times", spec.lower())
        self.assertIn("~30 s [default]", spec)
        self.assertIn("~2 min [default]", spec)
        # neither list is proof of death
        self.assertIn("harness task list", spec)
        # the boundary: fence-benign never crosses a wipe
        self.assertIn("foreign writer until verified", spec)
        # the base rules carry the working elaboration (checkpoint duty + fence extension)
        base = re.sub(r"\s+", " ", read("skills/live-spec-base/SKILL.md"))
        for needle in ("prior context", "proof of death", "halting", "write-set",
                       "INV-76"):
            self.assertIn(needle.lower(), base.lower(),
                          "base rules miss the liveness protocol piece: %s" % needle)
        # never framed finished before the verdict
        self.assertIn("never framed", spec.lower())


class TestFieldLessons(unittest.TestCase):
    """Rows 182-186: the tlvphoto week's escaped-bug classes folded back into the test method.
    String level, each red-proven against the pre-delta text."""

    def test_real_device_boundary(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("| INV-77 |", spec, "Formal index lost INV-77")
        self.assertIn("real-device walk row", spec)
        ta = re.sub(r"\s+", " ", read("skills/test-author/SKILL.md"))
        self.assertIn("real-device walk row", ta)
        for boundary in ("scroll snapping", "background throttling"):
            self.assertIn(boundary, ta, "test-author lost the named boundary: %s" % boundary)
        # the honest claim: the suite says what it cannot see
        self.assertIn("what it cannot see", ta)

    def test_relative_geometry_assertions(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("| INV-78 |", spec, "Formal index lost INV-78")
        self.assertIn("relative, wide, and long", spec)
        ta = re.sub(r"\s+", " ", read("skills/test-author/SKILL.md"))
        self.assertIn("relative, wide, and long", ta)
        # the three axes: relative geometry, multiple viewports, consecutive steps
        self.assertIn("two or more viewport sizes", ta)
        self.assertIn("consecutive steps", ta)
        self.assertIn("cumulative drift", ta)

    def test_engine_generic_fixtures(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("| INV-79 |", spec, "Formal index lost INV-79")
        self.assertIn("its own generic fixtures", spec)
        # both halves of the one law
        ta = re.sub(r"\s+", " ", read("skills/test-author/SKILL.md"))
        self.assertIn("engine-shaped fixtures", ta)
        self.assertIn("works-without-it test", ta)
        sa = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn("content contract", sa)
        self.assertIn("donor", sa)
        # the boundary: donor data legal as an extra, illegal as the only suite
        self.assertIn("never as the only one", ta)

    def test_prove_exemption_is_lens_aware(self):
        # row 185 (bug door): the miss mechanism pinned — a spec proven under an OLD lens set kept
        # its green; the exemption must read the prover version off the record
        adopt = re.sub(r"\s+", " ", read("adopt/ADOPT.md"))
        self.assertIn("same prover version", adopt)
        self.assertIn("re-arms the full pass", adopt)
        prover = re.sub(r"\s+", " ", read("skills/product-prover/SKILL.md"))
        self.assertIn("naming the prover skill version", prover)

    def test_suite_plumbing_must_not_lie(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("| INV-80 |", spec, "Formal index lost INV-80")
        self.assertIn("plumbing must not lie", spec)
        ta = re.sub(r"\s+", " ", read("skills/test-author/SKILL.md"))
        # the three legs
        self.assertIn("import the skip helper at module load", ta)
        self.assertIn("re-export completeness test", ta)
        self.assertIn("suite log", ta)
        # the boundary that keeps CI legal
        self.assertIn("background or delegated run", ta)


class TestPreAskScan(unittest.TestCase):
    """Row 187 (INV-81): a question to the human walks the pre-ask scan — the outside-reader read
    plus the can-I-decide-this-myself gate, asked first. String level."""

    def test_pre_ask_scan_covers_questions(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("| INV-81 |", spec, "Formal index lost INV-81")
        self.assertIn("can I decide or verify this myself?", spec)
        comm = re.sub(r"\s+", " ", read("skills/communicator/SKILL.md"))
        self.assertIn("guards every QUESTION", comm)
        self.assertIn("can I decide or verify this myself?", comm)
        # the three places a question rides
        for place in ("batched tail", "decision page", "lone ask"):
            self.assertIn(place, comm, "communicator's scan misses the question's place: %s" % place)
        # a surviving question carries its recommendation
        self.assertIn("recommendation attached", comm)


class TestLLDReadingOrder(unittest.TestCase):
    """Row 188: the architecture doc reads as an LLD reader expects — tiers first, fallbacks per
    failure point, the placement table framed as the tiers-and-technology table. String level."""

    def test_lld_reading_order_and_fallbacks(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("what happens then", spec)
        self.assertIn("reads tiers-first", spec)
        tpl = read("templates/ARCHITECTURE.template.md")
        self.assertIn("## The shape at a glance", tpl)
        self.assertIn("| If it fails |", tpl)
        self.assertIn("tiers-and-technology", tpl)
        # the shape section comes BEFORE the nodes table
        self.assertLess(tpl.index("## The shape at a glance"), tpl.index("## Nodes"))
        arch = read("ARCHITECTURE.md")
        self.assertIn("## The shape at a glance", arch)
        self.assertLess(arch.index("## The shape at a glance"), arch.index("## Nodes"))
        # every runtime-view row carries a fallback cell (4 pipes-cells per row)
        runtime = arch.split("## Runtime view", 1)[1].split("## ", 1)[0]
        rows = [l for l in runtime.split("\n") if l.startswith("| F-")]
        self.assertTrue(rows, "runtime view parsed empty")
        for r in rows:
            self.assertEqual(r.count(" | "), 3, "runtime row misses its if-it-fails cell: %s" % r[:60])
        crosswalk = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertIn("BMAD", crosswalk)
        self.assertIn("Kiro design.md", crosswalk)

    def test_field_norm_pieces(self):
        # row 189: the three adopted field-norm pieces (decisions pointer · schema homes · secrets place)
        tpl = read("templates/ARCHITECTURE.template.md")
        self.assertIn("## Decisions — where they live", tpl)
        self.assertIn("never a second home", tpl)
        self.assertIn("where that schema lives", tpl)
        self.assertIn("where SECRETS live", tpl)
        arch = read("ARCHITECTURE.md")
        self.assertIn("## Decisions — where they live", arch)
        self.assertIn("No secret lives in this pack", arch)
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("where secrets live", spec)


class TestPushToRemote(unittest.TestCase):
    """Row 194 (INV-82): accepted work reaches the host's remote by rule. String level."""

    def test_push_to_remote_law(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("| INV-82 |", spec, "Formal index lost INV-82")
        self.assertIn("Accepted work reaches the project's remote.", spec)
        self.assertIn("never parked locally", spec)
        # discover-first, one contextual question only when no remote
        self.assertIn("git remote -v", spec)
        self.assertIn("first push moment", spec)
        self.assertIn("one question per gap", spec)
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("PUSH accepted work there by rule", bp)
        self.assertIn("GitLab", bp)
        # his named gates survive the law
        self.assertIn("personally named gates still wait", bp)
        # every push re-walks the README (his 2026-07-10 word)
        self.assertIn("re-walks the README", bp)
        spec2 = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("re-walks the README", spec2)


class TestCleanWriterLaw(unittest.TestCase):
    """Row 208 (INV-84): human-facing prose is drafted by a clean writer. String level (M-198)."""

    def test_clean_writer_law(self):
        spec = re.sub(r"\s+", " ", read("PRODUCT_SPEC.md"))
        self.assertIn("| INV-84 |", spec, "Formal index lost INV-84")
        self.assertIn("Human-facing prose is drafted by a clean writer.", spec)
        self.assertIn("does not have the package rules loaded", spec)
        self.assertIn("refuses a blanket rewrite of settled text", spec)
        base = re.sub(r"\s+", " ", read(os.path.join("skills", "live-spec-base", "SKILL.md")))
        self.assertIn("Human-facing prose is drafted by a clean writer (SPEC INV-84).", base)
        self.assertIn("do not write the prose yourself", base)
