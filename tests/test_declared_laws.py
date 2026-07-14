"""Declared cross-cutting laws: one home, a prover station, an author habit — M-237 (SPEC INV-101, row 223).

His 2026-07-10 ~10:38 word from the worked miss: analytics covered some beats while whole
surfaces emitted nothing, and only his eye found it. The spec names its cross-cutting laws in
one declared-laws home; every new surface's section states its line against each declared law
(the clause or a dated exemption) before the prover reads it; the prover's station enumerates
every surface and transition per declared law. String rows on the three homes.
"""

import os
import re
import unittest

from conftest import ROOT, read_flat


class TestDeclaredLaws(unittest.TestCase):

    def test_the_home_and_the_packs_own_list(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("declared-laws home", spec)
        self.assertIn("the declared laws are three", spec)
        self.assertIn("dated exemption", spec)

    def test_the_prover_station(self):
        prover = read_flat("skills/product-prover/SKILL.md")
        self.assertIn("Declared cross-cutting laws", prover)
        self.assertIn("dated exemption", prover)
        self.assertIn("ranks as a broken invariant", prover)

    def test_the_author_habit(self):
        author = read_flat("skills/spec-author/SKILL.md")
        self.assertIn("declared-laws home", author)
        self.assertIn("before the prover", author)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-101]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-101 |"):
                    self.assertIn("dated exemption", line)
                    return
        self.fail("INV-101 index row missing")


class TestLawNamesItsNet(unittest.TestCase):
    """INV-150 — every declared cross-cutting law names its enforcing net; a netless law is a
    broken invariant; declaration promotes a property from the design review to the prover.
    Homes: the routing clause + INV-101 declared-laws field + the INV-101 prover station +
    spec-author's habit + the architecture ownership backstop. (Born of the tlvphotos openable-
    face miss: a law-shaped property lived only as prose on one member, never promoted into the
    declared space where the prover enumerates, 2026-07-14.)"""

    def test_each_law_names_its_net(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("names its net", spec)
        self.assertIn("declared-laws home", spec)

    def test_net_routing_law_stands(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("Every declared cross-cutting law names the net that enforces it", spec)
        self.assertIn("[INV-150]", spec)
        self.assertIn("Declaration is the lever", spec)
        # a watch-level net (the design review) carries a dated reason, the shape of a dated exemption
        self.assertIn("watch-level", spec)
        self.assertIn("dated reason", spec)

    def test_prover_station_demands_net(self):
        prover = read_flat("skills/product-prover/SKILL.md")
        self.assertIn("names its net", prover)
        self.assertIn("no named net", prover)

    def test_spec_author_writes_the_net(self):
        author = read_flat("skills/spec-author/SKILL.md")
        self.assertIn("carries its net", author)
        self.assertIn("INV-150", author)

    def test_spec_index_and_ownership(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            spec_lines = list(f)
        self.assertTrue(any(l.startswith("| INV-150 |") for l in spec_lines),
                        "INV-150 index row missing")
        for line in spec_lines:
            if line.startswith("| INV-150 |"):
                self.assertIn("enforcing net", line)
        arch = read_flat("ARCHITECTURE.md")
        self.assertIn("INV-150", arch)


# --- the net-floor: a declared law with no net reds without the agent (INV-150) ---

NET_TOKEN = re.compile(r"`[^`]+\.(?:sh|py)`|prover|design review")


def laws_without_net(laws):
    """laws: list of (law_text, net_text_or_None). Returns the law_texts naming no net.
    The per-item floor mirroring declared_law_surface_gaps in test_interface_coverage: it
    reds if any enumerated declared law lacks a net (SPEC INV-150)."""
    return [text for text, net in laws if not net]


def parse_declared_laws_and_nets(spec_flat):
    """Parse the declared-laws home. Returns (declared_law_count, laws), where the count is
    the laws enumerated (each carries its invariant anchors) and laws is [(segment, net_or_None)]
    from the per-law net-assignment sentence. A net is a named guardrail/test path, or the
    prover, or the design review."""
    m = re.search(r"the declared laws are \w+ —(.+?)— with .*? dated exemptions", spec_flat)
    region = m.group(1) if m else ""
    declared_law_count = len(re.findall(r"\[INV-[^\]]*\]", region))
    n = re.search(r"each name a mechanical gate[^:]*:(.+?)\. The prover", spec_flat)
    net_region = n.group(1) if n else ""
    laws = []
    for seg in net_region.split(", "):
        if not seg.strip():
            continue
        tok = NET_TOKEN.search(seg)
        laws.append((seg.strip(), tok.group(0) if tok else None))
    return declared_law_count, laws


class TestEachDeclaredLawNamesANet(unittest.TestCase):
    """INV-150 net-floor: the declared-laws home is parsed, each listed law enumerated, and each
    asserted to name a net — a mechanical gate, the prover's station, or the design review. A
    future declared law added with no net reds here without the agent, the same shape as the
    per-item interface/coverage floors. (Born of the tlvphotos openable-face miss, 2026-07-14.)"""

    def test_missing_net_is_flagged(self):
        laws = [("register", "`guardrails/check-shipped-language.sh`"), ("clock-honesty", None)]
        self.assertEqual(laws_without_net(laws), ["clock-honesty"],
                         "a declared law naming no net must be flagged")

    def test_fully_netted_flags_nothing(self):
        laws = [("register", "`x.sh`"), ("clock-honesty", "prover")]
        self.assertEqual(laws_without_net(laws), [])

    def test_pack_declared_laws_each_name_a_net(self):
        count, laws = parse_declared_laws_and_nets(read_flat("PRODUCT_SPEC.md"))
        self.assertGreaterEqual(count, 3, "declared-laws enumeration parse failure")
        self.assertEqual(laws_without_net(laws), [],
                         "an enumerated declared law names no net (SPEC INV-150)")
        self.assertEqual(len(laws), count,
                         "declared-law count (%d) and net assignments (%d) disagree — a law has no net"
                         % (count, len(laws)))


if __name__ == "__main__":
    unittest.main()
