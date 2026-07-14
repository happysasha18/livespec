"""The senior verifies write-set disjointness at brief-time before spawning a second concurrent writer.

The concurrent-edit fence [INV-11] stays silent between same-session sibling workers (fence-benign),
so the reactive net cannot catch two of the orchestrator's OWN helper workers colliding on a shared
file. This law puts the check where the silence forces it: at brief-time, before the second concurrent
writer is spawned, the senior confirms the two briefs' write-sets are disjoint or gives the later worker
an isolated tree. It extends ACT-3 / INV-11 (a spawn-time obligation on the existing "the senior owns
the seams" duty), so it homes on the worker contract and adds no new invariant. Born of a real
two-sibling-worker collision that self-corrected (tlvphotos 2026-07-13).
"""

import unittest

from conftest import read_flat

# The shared imperative, punctuation-identical across every home so one needle matches all.
# N-ary (disjoint from EVERY already-running writer, since T-18 allows up to three lanes), R1 folded.
IMPERATIVE = (
    "before spawning another concurrent writer, the senior confirms its brief's write-set is "
    "disjoint from every already-running writer's brief"
)


class TestBriefTimeDisjointness(unittest.TestCase):
    def test_spec_worker_contract_carries_the_imperative(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn(IMPERATIVE, spec)
        # settled at brief-time, not discovered at the write.
        self.assertIn("settled when the briefs are written", spec)
        # homed on the fence-benign / worker-contract clause, no new invariant.
        self.assertIn("owns their seams", spec)

    def test_build_pipeline_carries_the_operational_imperative(self):
        sk = read_flat("skills/build-pipeline/SKILL.md")
        self.assertIn(IMPERATIVE, sk)
        self.assertIn("settled when the briefs are written", sk)

    def test_live_spec_base_carries_the_pointer(self):
        base = read_flat("skills/live-spec-base/SKILL.md")
        self.assertIn(IMPERATIVE, base)
        self.assertIn("brief-time", base)


if __name__ == "__main__":
    unittest.main()
