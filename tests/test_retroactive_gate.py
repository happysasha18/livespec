"""INV-176 — a law that earns a gate gets a retroactive gate: it scans the whole tree.

A gate that reads only the changed lines finds old debt the day each old file happens to be
touched; a gate that scans the whole tracked tree finds it the day the gate lands. The
browser-mute gate (INV-157's tree scanner) is the worked example; the cap-seeding law (INV-172)
absorbs a backlog too large to fold at once.
"""
from conftest import read


def test_spec_states_the_retroactive_gate_law():
    spec = read("PRODUCT_SPEC.md")
    assert "retroactive by construction" in spec
    assert "| INV-176 |" in spec


def test_gate_contract_carries_the_clause():
    readme = read("guardrails/README.md")
    assert "INV-176" in readme


def test_adoption_runs_gates_backward():
    adopt = read("adopt/ADOPT.md")
    assert "backward over" in adopt
