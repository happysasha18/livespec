"""The named-reference living-description law (INV-240, M-424) and the earned auto-deposit with its
two user-tells (T-24, M-425).

Both facts are stated as law and homed in their normative surfaces; the BEHAVIOUR each names — that
an agent actually defers and rewrites a description on its next penned run, routes a cross-window
re-question as a fault-birth earned message, auto-deposits on an earned birth, and emits the two
tells — lives on the model and the live status surface no script observes [INV-150, INV-83]. So the
honest test level here is doc-structural: the law stands in the spec, the Formal index, ARCHITECTURE,
and this matrix (the traceability quartet, re-walked by tests/test_traceability.py), and the clauses'
own wording is present. No behavioural test is invented for what a script cannot see.
"""
import unittest

from conftest import read, read_flat


def index_of(spec):
    return spec.split("## Formal index", 1)[1]


class TestLivingDescriptionLaw(unittest.TestCase):
    """M-424 (INV-240): the self-heal law is stated with its deferred / next-penned-run / fault-birth
    / restructure-delta wording."""

    def test_spec_states_the_living_description_law(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn(
            "A description that leaves a reader asking what a term means is rewritten on the owning "
            "agent's next penned run", spec,
            "SPEC lost the living-description law headline (INV-240)")
        self.assertIn("[INV-240]", spec, "SPEC prose lost the INV-240 anchor")

    def test_spec_carries_the_deferred_penned_run_and_fault_birth_wording(self):
        spec = read_flat("PRODUCT_SPEC.md")
        for phrase in (
            "next penned run",                                   # the overwrite waits for the penned run
            "fault-birth earned message",                        # the cross-window route [INV-189]
            "firing reactively",                                 # deferred, never mid-turn
            "rides as a named intended delta to the restructure-identity merge gate",  # the matched token [INV-111]
        ):
            self.assertIn(phrase, spec, "SPEC INV-240 clause lost the wording: %s" % phrase)

    def test_formal_index_row_inv240(self):
        self.assertRegex(index_of(read("PRODUCT_SPEC.md")), r"\|\s*INV-240\s*\|",
                         "the Formal index carries no INV-240 row")

    def test_architecture_owns_the_invariant(self):
        from test_traceability import architecture_nodes
        self.assertIn("INV-240", architecture_nodes().get("base-rulebook", set()),
                      "INV-240 is not owned under the base-rulebook node in ARCHITECTURE")

    def test_matrix_row_covers_the_law_inv240(self):
        self.assertRegex(read("TEST_MATRIX.md"), r"\|\s*M-424\s*\|", "TEST_MATRIX lost the M-424 row")


class TestEarnedAutoDeposit(unittest.TestCase):
    """M-425 (T-24): the earned auto-deposit and both user-tells are stated as law, homed in the
    status report, the decline-tell scoped to a drafted-then-refused message."""

    def test_spec_states_the_earned_auto_deposit_law(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn(
            "An agent deposits an earned message in the course of its own work", spec,
            "SPEC lost the earned auto-deposit law headline (T-24)")
        self.assertIn("The trigger is any earned birth, the whole class", spec,
                      "SPEC lost the whole-class trigger (T-24, INV-153)")
        self.assertIn("[T-24]", spec, "SPEC prose lost the T-24 anchor")

    def test_both_tells_home_in_the_status_report(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("their home is the status report", spec,
                      "SPEC lost the status-report home for the two tells")
        for tell in ("escalation", "wrong-referral"):
            self.assertIn(tell, spec, "SPEC lost the beside-%s placement of the tells" % tell)

    def test_decline_tell_scoped_to_a_drafted_message(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn(
            "The decline-tell fires only on a drafted message and never on a suppressed impulse", spec,
            "SPEC lost the decline-tell scoping to a drafted-then-refused message")

    def test_deposit_names_references_by_the_pair(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("The deposited message names its references by the pair", spec,
                      "SPEC lost the deposit-names-references-by-the-pair clause (E-35)")

    def test_formal_index_row_t24(self):
        self.assertRegex(index_of(read("PRODUCT_SPEC.md")), r"\|\s*T-24\s*\|",
                         "the Formal index carries no T-24 row")

    def test_architecture_owns_the_transition(self):
        from test_traceability import architecture_nodes
        self.assertIn("T-24", architecture_nodes().get("base-rulebook", set()),
                      "T-24 is not owned under the base-rulebook node in ARCHITECTURE")

    def test_matrix_row_covers_the_law_t24(self):
        self.assertRegex(read("TEST_MATRIX.md"), r"\|\s*M-425\s*\|", "TEST_MATRIX lost the M-425 row")


if __name__ == "__main__":
    unittest.main()
