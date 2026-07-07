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
        for name in ("SPEC", "ARCHITECTURE", "TEST_MATRIX", "ROADMAP", "JOURNAL", "NEXT_STEPS"):
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
        # the four working skills' base pin points at the CURRENT base version (read from its
        # frontmatter, so a base bump without the same-session pin sweep is red by construction)
        base_version = re.search(r"(?m)^\s*version:\s*([0-9.]+)",
                                 read("skills/live-spec-base/SKILL.md")).group(1)
        for rel in ("skills/build-pipeline/SKILL.md", "skills/communicator/SKILL.md",
                    "skills/product-prover/SKILL.md", "skills/spec-author/SKILL.md",
                    "skills/publish/SKILL.md"):
            self.assertIn("`live-spec-base` (v%s)" % base_version, read(rel),
                          "%s pins a stale base version" % rel)

    def test_spec_states_work_kind(self):
        body = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("The intake line also names WHAT is being built",
                       "A kind scales the steps — it never skips one silently",
                       "STOOD DOWN by name",
                       "An unresolved kind scales nothing down",
                       "never the safety net",
                       "one kind per wish",
                       "The vocabulary is CURATED like the facet list"):
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
        for phrase in ("A big wish negotiates scope, never time",  # row 99: his word, time budgets dead
                       "not an input the walk accepts",
                       "split into stages",
                       "bends scope only, never order",
                       "Scope dials richness; it never touches the safety net",
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
        self.assertIn("never a time budget or estimate", bp,
                      "build-pipeline intake line lost the scope-never-time law")
        self.assertNotIn("appetite", bp.lower(), "build-pipeline still speaks the retired term")
        self.assertIn("The delta CLOSES with its two sentences", bp)
        sa2 = re.sub(r"\s+", " ", read("skills/spec-author/SKILL.md"))
        self.assertNotIn("appetite", sa2.lower(), "spec-author still speaks the retired term")
        spec2 = re.sub(r"\s+", " ", read("SPEC.md"))
        self.assertNotIn("appetite", spec2.lower(), "SPEC still speaks the retired term")

    def test_spec_states_founding_and_designsync(self):
        body = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("The founding questions are asked, never inferred",
                       "personal tool, or reusable product?",
                       "deliberately STRONGER than the walk's proceed-on-default habit",  # F5 fold
                       "A-1 carries the pointer",                                          # F7 fold
                       "Design-sync [target: the machine; the wiring is live]",           # row 93 pack-side
                       "SUPPLEMENTS the in-session render",                                # F1 fold
                       "the components a landing DECLARED"):                               # F4 fold
            self.assertIn(phrase, body, "SPEC lost the founding/design-sync clause: %s" % phrase)
        for anchor in ("[B-2]", "[E-18]"):
            self.assertIn(anchor, body, "SPEC prose lost anchor %s" % anchor)
        adopt = re.sub(r"\s+", " ", read("adopt/ADOPT.md"))
        self.assertIn("Founding questions ride the orient", adopt, "ADOPT lost the founding-questions line")
        tpl = re.sub(r"\s+", " ", read("templates/SPEC.template.md"))
        self.assertIn("Founding answers (B-2)", tpl, "SPEC template lost the founding-answers slot")

    def test_night_batch_skill_rules(self):
        # rows 79/81/82/87: worker briefs, excuses table, two one-liners, decision-file numbering
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        self.assertIn("The brief is self-contained", bp, "build-pipeline lost the worker-brief rule")
        self.assertIn("The excuses table", bp, "build-pipeline lost the excuses table")
        self.assertIn("Size never picks the door", bp)
        pp = re.sub(r"\s+", " ", read("skills/product-prover/SKILL.md"))
        self.assertIn("Report gaps, not taste", pp, "product-prover lost the anti-taste line")
        base = read("skills/live-spec-base/SKILL.md")
        self.assertRegex(base, r"(?m)^17\. \*\*Irreversible means gone, not merely public",
                         "base rule 17 missing")
        self.assertIn("A push to your own repository is NOT irreversible", base)
        cm = re.sub(r"\s+", " ", read("skills/communicator/SKILL.md"))
        self.assertIn("append their ordinal", cm, "communicator lost the decision-file numbering")

    def test_spec_states_registry_and_pins(self):
        body = re.sub(r"\s+", " ", read("SPEC.md"))
        self.assertIn("the NORMATIVE pin is the named thing", body, "SPEC lost symbol-first pins (E-14)")
        self.assertIn("PREFERRED form is executable", body, "SPEC lost the executable-registry form (E-10)")
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
        self.assertIn("вердикт растяжки старше ярлыка", cm, "communicator lost the field example")


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
        self.assertIn("The list is curated, not collected", sa, "spec-author lost the curation law")
        self.assertIn("named real incident", sa)
        # every facet entry in the canonical list names its incident
        self.assertGreaterEqual(sa.count("(incident"), 3, "new facets must carry their incidents")

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
            for frag in ("<h1>Title</h1>", "<strong>bold</strong>", "<table>", "<td>2</td>"):
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("Publishing — the deposit owes what its kind owes",
                       "Each publish TARGET is a plugin",
                       "the checklist runs BEFORE the gate"):
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
        body = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("How the skills arrive on a machine",
                       "backed up with a timestamp before being overwritten, never deleted",
                       "two halves of one seam"):
            self.assertIn(phrase, body, "SPEC lost the installer clause: %s" % phrase)
        self.assertIn("[E-21]", body, "SPEC prose lost anchor E-21")

    def test_spec_names_decision_page(self):
        body = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("How batched questions reach you",
                       "never become a serialized chat questionnaire",
                       "an answer left un-harvested is a decision lost"):
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
        for rel in ("SPEC.md", "adopt/ADOPT.md", "inbox/README.md"):
            body = re.sub(r"\s+", " ", read(rel))
            self.assertIn("rule 18", body, "%s no longer cites the one collision law" % rel)
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        self.assertEqual(spec.count("rule 18"), 2,
                         "the law must be CITED at its two instances (attic, inbox), stated only in base")


class TestDeclineListsAbsorbed(unittest.TestCase):
    """Row 63 (M-094): declining an absorber lists the rows superseded into it — each declined by
    name or returned; a superseded wish never dies by pointer."""

    def test_spec_states_decline_absorbed(self):
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("declining is not a black hole",
                       "declined BY NAME",
                       "RETURNED to the queue as its own row again",
                       "a superseded wish never dies by pointer"):
            self.assertIn(phrase, spec, "SPEC lost the decline-lists-absorbed clause: %s" % phrase)
        tpl = re.sub(r"\s+", " ", read("templates/ROADMAP.template.md"))
        self.assertIn("never dies by pointer", tpl,
                      "ROADMAP template lost the decline-lists-absorbed rule")


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
        "ACT-3": 56,  # the model router
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
        spec = read("SPEC.md")
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("the thin loader stays thin",
                       "must this hold BEFORE any pack file loads?",
                       "states the line count",
                       "migrates to its real home"):
            self.assertIn(phrase, spec, "SPEC M-1 lost the loader-stays-thin item: %s" % phrase)

    def test_m1_names_skill_creator_rewalk(self):
        """Row 130 (M-128): the milestone gate re-walks the pack's skills through
        skill-creator; findings folded or rejected with reason in a dated record;
        a new skill walks it at birth."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("re-walked through the standard skill-making skill",
                       "folded or rejected with a written reason in a dated record",
                       "walks it at birth"):
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
        spec = read("SPEC.md")
        flat_spec = " ".join(spec.split())
        for needle in (
            "Each step is worked in its craft's mindset",
            "INV-33",
        ):
            self.assertIn(needle, flat_spec, "SPEC missing: %s" % needle)
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        flat_pipe = " ".join(pipeline.split())
        for needle in (
            "The craft ladder — whose head you wear at each step",
            "a strong product manager",
            "QA automation lead",
            "the visitor's own eyes, not the builder's",
            "a careful release hand",
        ):
            self.assertIn(needle, flat_pipe, "build-pipeline missing: %s" % needle)
        matrix = read("TEST_MATRIX.md")
        self.assertIn("test_craft_ladder", matrix, "M-120 must pin this test (row 124)")

    def test_brief_carries_ledger_and_clock(self):
        """Row 123 (M-119, ACT-3): every worker brief carries the problem-ledger
        walk and the clock read at briefing."""
        spec = read("SPEC.md")
        flat_spec = " ".join(spec.split())
        for needle in (
            "the brief ARMS the worker for the workshop",
            "carries the CLOCK",
        ):
            self.assertIn(needle, flat_spec, "SPEC ACT-3 missing: %s" % needle)
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        flat_pipe = " ".join(pipeline.split())
        for needle in (
            "the brief ARMS the worker for the workshop",
            "WATCHED-line duty",
            "carries the CLOCK",
            "never an invented hour",
        ):
            self.assertIn(needle, flat_pipe, "build-pipeline missing: %s" % needle)
        matrix = read("TEST_MATRIX.md")
        self.assertIn("test_brief_carries_ledger_and_clock", matrix,
                      "M-119 must pin this test (row 123)")

    def test_worker_contract_stated(self):
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("The worker contract",
                       "NARROWED to the files its brief names",
                       "fence-benign",
                       "ride INTO the brief verbatim",
                       "escalates ONE tier with a logged line",
                       "never a skipped rung"):
            self.assertIn(phrase, spec, "SPEC ACT-3 lost the worker-contract clause: %s" % phrase)
        bp = re.sub(r"\s+", " ", read("skills/build-pipeline/SKILL.md"))
        for phrase in ("The worker contract (SPEC ACT-3)",
                       "fence alarms on foreign sessions",
                       "never resolves the settings ladder itself",
                       "never a silent retry on the same tier"):
            self.assertIn(phrase, bp, "build-pipeline lost the worker-contract elaboration: %s" % phrase)


class TestBootstrapScaffold(unittest.TestCase):
    """Row 62 (M-034 extension): the bootstrap ships a runnable suite scaffold that defines green
    for landing #1. Verified BY DEED: a simulated bootstrap in a temp dir runs the shipped scaffold
    — green when the copy is filled, red when a placeholder survives."""

    def _bootstrap(self, tmp, fill=True):
        import shutil
        os.makedirs(os.path.join(tmp, "tests"))
        for name in ("SPEC", "ARCHITECTURE", "TEST_MATRIX", "ROADMAP", "JOURNAL", "NEXT_STEPS"):
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("The version-control gate runs FIRST",
                       "a gate cannot protect files older than itself",
                       "plus the suite scaffold",
                       "DEFINES what \"green\" means for landing #1",
                       "a leftover placeholder is red",
                       "Hooks are OFFERED at bootstrap exactly as at adoption"):
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for phrase in ("keeps its skills fresh by name, not by habit",
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
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
                       "never function names, internal ids, or row numbers",
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
        spec = read("SPEC.md")
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
        spec = read("SPEC.md")
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
        spec = read("SPEC.md")
        for needle in ("INV-27", "departures board", "hears itself land"):
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
        for home, text in (("SPEC.md", spec),
                           ("communicator SKILL.md", comm),
                           ("TEST_MATRIX.md", matrix)):
            flat = " ".join(text.split())
            self.assertIn(stations, flat,
                          "%s station list is missing a pipeline step (row 125)" % home)
            self.assertIn("plus the terminal landed", flat,
                          "%s must mark landed as the terminal state (row 125)" % home)

    def test_outcome_leads_law(self):
        """Row 116 (M-113, INV-28): the outcome does the talking — echo-names are plain
        descriptive phrases; handles and coined names only trail; one fact per sentence."""
        spec = read("SPEC.md")
        for needle in ("INV-28", "never chose to learn", "one fact = one standalone sentence"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = read(os.path.join("skills", "communicator", "SKILL.md"))
        for needle in ("coined feature name", "INV-28", "one fact = one standalone sentence"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)
        base = read(os.path.join("skills", "live-spec-base", "SKILL.md"))
        self.assertIn("coined feature name", base,
                      "base rule 2 must name coined feature names as handles")

    def test_fit_walk_law(self):
        """Row 108 (M-114, INV-29): a feature is interrogated for product fit at intake."""
        spec = read("SPEC.md")
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
        spec = read("SPEC.md")
        for needle in ("INV-30", "VISITOR WALK", "FEEL pass"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        for needle in ("VISITOR WALK", "FEEL pass"):
            self.assertIn(needle, pipeline, "pipeline step-8 missing: %s" % needle)

    def test_default_expiry_law(self):
        """Rows 118+120 (M-116, INV-31): a taste default is TOLD at landing, never confirmed."""
        spec = read("SPEC.md")
        for needle in ("INV-31", "TOLD, never confirmed"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = read(os.path.join("skills", "communicator", "SKILL.md"))
        self.assertIn("unclaimed decision files", comm,
                      "communicator rule 10 missing the resume-sweep of decision answers")
        pipeline = read(os.path.join("skills", "build-pipeline", "SKILL.md"))
        self.assertIn("open `[default]`s", pipeline, "pipeline step 9 missing the defaults list")

    def test_decision_card_consequences(self):
        """Row 119 (M-117, INV-32): a decision card asks in consequences, not mechanisms."""
        spec = read("SPEC.md")
        for needle in ("INV-32", "consequences, not mechanisms"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = read(os.path.join("skills", "communicator", "SKILL.md"))
        self.assertIn("what the choice CHANGES for the person", comm,
                      "communicator rule 10 missing the consequence-first card law")

    def test_bookkeeping_never_list(self):
        """Row 126 (M-121, INV-28): bookkeeping numbers are never message content —
        translated ("tested clean", "saved"), trailing, or in the records; a direct
        question or the done-claim walk (INV-25) keeps the number as the answer."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("Bookkeeping numbers are handles too", "NEVER-list",
                       "speaks as the answer, not as bookkeeping"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("test count", "version string", "tested clean",
                       "asked substance"):
            self.assertIn(needle, comm, "communicator rule 8 missing: %s" % needle)

    def test_pre_report_walk(self):
        """Row 128 (M-122, INV-34): before any movement-end/milestone report the
        communicator rules are re-read and the draft passes phrase by phrase through
        the outside-reader question; trailing anchors stay legal."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-34", "walked, not remembered",
                       "does this sentence stand for a reader who does not live inside the pack"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("pre-report walk", "phrase by phrase", "INV-34"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_chat_timestamp_at_write_time(self):
        """Row 127 (M-123, INV-24 chat face): a human-facing timestamp is read off the
        clock at write time, never extrapolated; quoting a past recorded time stays legal."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("CHAT face", "AT WRITE TIME"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("read off the clock at write time", "never continued or extrapolated"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_working_narration(self):
        """Row 131 (M-124, INV-35): work is narrated while it runs — beats in plain
        roadmap terms, the reports' voice, the grind quiet; a narration line is chat,
        not a report."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-35", "third voice between the echo and the report",
                       "narration marks beats, never a per-command commentary"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("Narrate the work while it runs", "narration line is chat, not a report",
                       "INV-35"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_narration_three_teeth(self):
        """Row 139 (M-124, INV-35 grown): identity — every beat names the wish and
        station in hand; digest — a station's completion is a beat digesting what the
        station produced (a worker-closed station is the senior's beat); heartbeat — a
        beatless stretch past ~10 minutes [default] names what grinds. Both homes carry
        the teeth; digests never speak in counters (INV-28 seam)."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("IDENTITY: every narration beat names the work it belongs to",
                       "a station's completion is itself a beat by law",
                       "a station a delegated worker closed becomes the senior's beat",
                       "beatless stretch past ~10 minutes owes its heartbeat [default]",
                       "token and test counts stay bookkeeping"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("Identity", "Digest", "Heartbeat",
                       "which wish is in hand and which station it stands at",
                       "digests what the station produced",
                       "a worker-closed station becomes the senior's beat",
                       "beatless stretch past ~10 minutes owes its heartbeat [default]",
                       "never a test count"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_offline_window(self):
        """Row 138 (M-138, INV-35): the heartbeat's offline-window face — before a
        stretch needing nothing from the human, narration says he may step away, an
        honest range, and what he is needed for at its end; the needed-again beat is
        a chat line awaiting his return, never a summons; the superseded fence
        sentence survives in neither home."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("OFFLINE WINDOW",
                       "he may step away, an honest range for how long",
                       "never a guess dressed as a promise",
                       "a chat line awaiting his return, never a summons",
                       "overrun, done sooner, or blocked on his word alone",
                       "no offline sentence fires when the very next beat needs the human"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("Offline window", "may step away", "honest range",
                       "never a guess dressed as a promise",
                       "a chat line awaiting his return, never a summons"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)
        for name, home in (("SPEC", spec), ("communicator", comm)):
            self.assertNotIn("its own promised law (queue row 138)", home,
                             "%s still carries the superseded row-138 fence sentence" % name)

    def test_his_word_read_right(self):
        """Row 145 (M-139, INV-42): a phrasing he killed stays killed — the kill-list
        written in the artifact's project records, never only session memory; his
        vivid phrase adopted only as meant — sarcasm is not instruction."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-42", "stays killed in every later draft",
                       "never only in session memory",
                       "mockery of a bad draft, not guidance"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("stays killed", "kill-list",
                       "Sarcasm is not instruction",
                       "never only in session memory"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_prototype_norm_pointer(self):
        """Row 109 (M-140, INV-43): an approved prototype is the norm — the clause
        cites `norm: <path>` (frozen into docs/norms/), the code step opens the
        artifact and records a plan-vs-prototype diff line, a mockup-first entry
        condition cancels only by the human naming it, and the prover carries the
        norm lens."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-43", "`norm: <path>`", "docs/norms/",
                       "a missing diff line is a defect at review",
                       "cancelled only by the human naming it"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        author = re.sub(r"\s+", " ", read(os.path.join("skills", "spec-author", "SKILL.md")))
        for needle in ("`norm: <path>`", "docs/norms/", "frozen copy",
                       "never into a live prototype home"):
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-44", "the shopfront rides every push",
                       "shopfront checked — current",
                       "a stale claim found is fixed BEFORE the push"):
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-45", "reach map",
                       "an unmapped or new file means the FULL suite",
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-46", "tasks completed, goal missed",
                       "never the worker's summary",
                       "MANDATORY when the code step was delegated"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("tasks completed, goal missed",
                       "TODO · FIXME · placeholder · lorem · hardcoded sample · empty function body",
                       "never the worker's summary"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)

    def test_lanes_by_graph(self):
        """Row 149 (M-147, INV-49): lanes picked by a dependency graph, integration
        order declared at claim, tiny rows serial."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-49", "DEPENDENCY GRAPH", "rows ride serial",
                       "first-declared lands first"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        pipe = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        for needle in ("Lanes are picked by a graph", "rows ride serial",
                       "DECLARED at claim"):
            self.assertIn(needle, pipe, "build-pipeline missing: %s" % needle)

    def test_entry_symmetry(self):
        """Row 150 (M-148, INV-50): a conditionally-entered face owes a re-entry
        path or a written one-way; the prover carries the lens."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-50", "deliberate RE-ENTRY path", "until dismissed"):
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-51", "never only the URL", "just an update"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("passport", "needs your word: what, by when", "never only the URL"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_windows_accumulate(self):
        """Row 152 (M-150, INV-52): during an away-stretch windows accumulate to one
        end-of-stretch opening."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-52", "accumulate on ONE page", "refreshed in place"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("windows accumulate", "refreshed in place",
                       "opens that one window once"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_brief_trio_laws(self):
        """Rows 111-113 (M-151..153, INV-53/54/55): a brief is born from read files,
        carries the closed HALT list, and is sized with paths, never bodies."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-56", "never dams the flow", "serviced in BATCH",
                       "never a per-instance ceremony"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        base = re.sub(r"\s+", " ", read(os.path.join("skills", "live-spec-base", "SKILL.md")))
        for needle in ("never dams the flow", "serviced in BATCH", "known limp"):
            self.assertIn(needle, base, "base missing: %s" % needle)

    def test_stretch_end_unmissable(self):
        """Row 154 (M-156, INV-57): the stretch's end is one short final line, last,
        after every tool call — delivery, not existence."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-57", "Delivery, not existence",
                       "the LAST rendered thing is one SHORT final line"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("final line comes LAST", "what closed", "when the agent wakes"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_promoter_harvest_trio(self):
        """Rows 158+160+162 (M-157..159, INV-58/59/60): frozen approved text; no
        question twice + converging dialogues; taste asks carry a mined proposal."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-58", "INV-59", "INV-60",
                       "never a fresh rewrite around it",
                       "a question a record already answers is a DEFECT",
                       "never arrives empty-handed"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("Approved text is frozen", "round N+1 carries only new material",
                       "mined the material first", "closes forever"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_process_cost_scales(self):
        """Row 155 (M-160, INV-61): the pre-push re-check scales its form to the
        delta; rigor and the safety net never scale."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-61", "SHORT-FORM record of three lines",
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-64", "inferences are flagged LOUDEST",
                       "COMMENTABLE, never a read-only wall"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("MY INFERENCE", "never a read-only wall",
                       "extended to review pages"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_kill_list_mechanical(self):
        """Row 159 (M-164, E-26): the kill-list template ships and the scanner
        guidance stands in guardrails."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("B-3", "learns WHO it is working with",
                       "a proposed line is accepted or dropped one at a time",
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-65", "it searches for an existing skill",
                       "adopted or rejected BY NAME",
                       "verbatim text travels only under its license"):
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("E-27", "six working skills", "test-author"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        skill = re.sub(r"\s+", " ", read(os.path.join("skills", "test-author", "SKILL.md")))
        for needle in ("The level ladder", "Red first, proven", "Pin the skip-set",
                       "Normally invoked by build-pipeline"):
            self.assertIn(needle, skill, "test-author skill missing: %s" % needle)
        bp = re.sub(r"\s+", " ", read(os.path.join("skills", "build-pipeline", "SKILL.md")))
        self.assertIn("invoke `test-author`", bp, "build-pipeline missing the invoke wiring")
        readme = re.sub(r"\s+", " ", read("README.md"))
        self.assertIn("test-author", readme, "README missing the new skill")

    def test_project_kind(self):
        """Row 129 (M-125, INV-36): the project knows its own kind — asked at
        founding/orient, one home in the host profile, alive as the project evolves."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-36", "The project knows what KIND of thing it is",
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-37", "PLACED on the product's map",
                       "A restructure verdict never re-carves in passing",
                       "Re-carving the whole map IS legal"):
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("INV-38", "Asking what the product does",
                       "transparency is a command, not archaeology",
                       "the whole map comes only when",
                       "a host with nothing to read", "shown as queued"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        comm = re.sub(r"\s+", " ", read(os.path.join("skills", "communicator", "SKILL.md")))
        for needle in ("feature map on demand", "no third document", "INV-38"):
            self.assertIn(needle, comm, "communicator missing: %s" % needle)

    def test_parallel_lanes_law(self):
        """Rows 135+142 (M-129, T-18): up to three trains may roll without asking, a fourth on the
        human's word, one pen writes — the law in SPEC, carried by build-pipeline + base; the
        waiting lane readable on the board (communicator)."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("Trains may roll", "T-18", "At most three build lanes roll at once",
                       "a FOURTH lane opens only on the human's asked word",
                       "waiting for the pen SAYS so and names the row it waits behind",
                       "a pen-stage is never cut mid-edit",
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("The architecture owes numbers, not only names", "INV-41",
                       "MEASURABLE quality",
                       "INSTRUMENTATION home",
                       "the project's KIND [INV-36] proposes the dimensions",
                       "no honest number, the architecture SAYS so by name",
                       "is a derivation defect the prover flags",
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
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
        for needle in ("economy ladder", "`budget.pressure`", "full [default]",
                       "moved only by the human's word",
                       "the economy rung is asked, or the standing default told",
                       "every taken shed named in the landing report",
                       "What NEVER bends, at any rung",
                       "a push still requires the full gate green at HEAD",
                       "red at batch end bisects by landing order",
                       "an explicit host line outlives any rung"):
            self.assertIn(needle, spec, "SPEC missing: %s" % needle)
        base = re.sub(r"\s+", " ", read(os.path.join("skills", "live-spec-base", "SKILL.md")))
        for needle in ("budget.pressure", "economy ladder", "SPEC T-19"):
            self.assertIn(needle, base, "base missing: %s" % needle)

    def test_landing_purity(self):
        """Row 135 (M-130, INV-39): a landing commit carries exactly one row's delta."""
        spec = re.sub(r"\s+", " ", read("SPEC.md"))
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
