# -*- coding: utf-8 -*-
"""An expensive decision earns an adversarial read before it lands (ROADMAP row 395, SPEC INV-235).

Agent birth [T-22] says the owner ratifies a new agent, and says nothing about what he ratifies ON:
the proposal names the capability, the zone, and the contracts, and it carries no adversarial read.
The class of EXPENSIVE decisions — the ones whose reversal costs more than the decision itself — has no
stated way to be decided at all. Row 395 names that class, sweeps its members, states the road from
pieces the pack already owns, and has agent birth carry it (the owner's word, 2026-07-17, continuing the
multi-agent thread).

An expensive decision cannot be told from an ordinary one by a machine — no gate reads a decision's
reversal cost — so this is a STATED DUTY at the named decision points, and this module is the
traceability proof that those points name the read. No new pre-push gate letter: the duty rides the
suite here, the way the far-tier and node-growth checks ride the suite and mint no push-gate letter.

Red-first: against HEAD 35069ba the spec carries no INV-235, the road pieces are cited nowhere as a
class, and T-22 names no adversarial read, so every assertion below fails — the red recorded in
docs/prover/2026-07-18-row395-expensive-decision.md.
"""
import json
import os
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as f:
        return f.read()


def line_with(text, phrase):
    """The single line carrying a distinctive phrase (an invariant is one line per paragraph)."""
    for line in text.splitlines():
        if phrase in line:
            return line
    return None


CLASS_OPENER = "An expensive decision earns an adversarial read before it lands"


class TestExpensiveDecisionLawStands(unittest.TestCase):
    def test_spec_states_the_law(self):
        spec = read("PRODUCT_SPEC.md")
        line = line_with(spec, CLASS_OPENER)
        self.assertIsNotNone(line, "the INV-235 clause is absent from the spec")
        self.assertIn("[INV-235]", line, "the clause carries no [INV-235] tag")
        low = line.lower()
        # the class is named by its defining property: reversal costs more than the decision
        self.assertIn("unwinding it costs more than making it", low)

    def test_members_swept_enumerated(self):
        """The class is closed and enumerable, so every member is named in the clause [INV-226]."""
        spec = read("PRODUCT_SPEC.md")
        line = line_with(spec, CLASS_OPENER)
        self.assertIsNotNone(line, "the INV-235 clause is absent")
        low = line.lower()
        self.assertIn("closed", low)
        self.assertIn("enumerable", low)
        self.assertIn("[INV-226]", line, "the clause does not key on the enumerate-versus-ride family")
        # the swept members, each by its anchor (agent birth, node carve/merge, pinned contract,
        # project kind, the engine/instance split, a repo going public)
        for anchor in ("[T-22]", "[INV-113, INV-122]", "[INV-187]", "[INV-36]", "[INV-85]", "[INV-44]"):
            self.assertIn(anchor, line, "member %s is not enumerated in the class clause" % anchor)

    def test_road_states_owned_pieces(self):
        """The road is assembled from pack-owned pieces, cited by anchor rather than invented."""
        spec = read("PRODUCT_SPEC.md")
        line = line_with(spec, CLASS_OPENER)
        self.assertIsNotNone(line, "the INV-235 clause is absent")
        low = line.lower()
        self.assertIn("adversarial", low)
        self.assertIn("recommendation", low)
        # the audit, the periodic-audit stance, the design-review grouping read, and the human's taste
        # call (surfaced by the orchestrator [INV-143] because it needs a fact only he holds [INV-152])
        for anchor in ("[INV-46]", "[INV-145]", "[INV-141, INV-142]", "[INV-143]", "[INV-152]"):
            self.assertIn(anchor, line, "road piece %s is not cited in the class clause" % anchor)

    def test_stated_duty_no_detector(self):
        """The clause is honest that no machine tells an expensive decision from an ordinary one."""
        spec = read("PRODUCT_SPEC.md")
        line = line_with(spec, CLASS_OPENER)
        self.assertIsNotNone(line, "the INV-235 clause is absent")
        low = line.lower()
        self.assertIn("no machine tells an expensive decision from an ordinary one", low)
        self.assertIn("traceability test", low)


class TestAgentBirthCarriesTheRead(unittest.TestCase):
    """T-22's ratification now names the adversarial read the owner ratifies on (SPEC INV-235)."""

    def test_proposal_carries_the_read(self):
        spec = read("PRODUCT_SPEC.md")
        line = line_with(spec, "The proposal names the capability, the zone the new agent would own")
        self.assertIsNotNone(line, "the T-22 proposal clause is absent")
        self.assertIn("carries the adversarial read", line,
                      "the birth proposal does not carry the adversarial read")
        self.assertIn("[INV-235]", line, "the birth proposal does not cite INV-235")

    def test_owner_ratifies_on_the_read(self):
        spec = read("PRODUCT_SPEC.md")
        line = line_with(spec, "first member of the expensive-decision class")
        self.assertIsNotNone(line, "T-22 does not name agent birth as a member of the expensive-decision class")
        self.assertIn("ratifies on", line, "T-22 does not say the owner ratifies ON the read")
        self.assertIn("[INV-235]", line, "the T-22 ratifies-on sentence does not cite INV-235")


class TestTraceability(unittest.TestCase):
    def test_formal_index_row(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn(
            "| INV-235 | an expensive decision earns an adversarial read before it lands",
            spec, "no Formal-index row for INV-235")

    def test_architecture_owns_the_invariant(self):
        arch = read("ARCHITECTURE.md")
        owners = [line for line in arch.splitlines() if "INV-235" in line]
        self.assertTrue(any("| build-pipeline |" in line for line in owners),
                        "build-pipeline does not own INV-235 in the architecture owns-list")

    def test_matrix_row_covers_the_law(self):
        mat = read("TEST_MATRIX.md")
        self.assertIn("| M-416 |", mat)
        row = line_with(mat, "| M-416 |")
        self.assertIn("INV-235", row, "M-416 does not cite INV-235")

    def test_duty_rides_the_suite_not_the_push_chain(self):
        """Stated duty rather than a mechanical gate: no INV-235 push-gate letter is wired.

        An expensive decision cannot be detected mechanically, so the duty is held by this traceability
        test riding the suite, and the gate chain is untouched. This test is the honesty check on that.
        """
        proofs = json.loads(read("guardrails/gate-red-proofs.json"))
        blob = json.dumps(proofs)
        self.assertNotIn("INV-235", blob,
                         "INV-235 appears in the gate red-proofs — a push gate was wired where a stated "
                         "duty was intended")


if __name__ == "__main__":
    unittest.main(verbosity=2)
