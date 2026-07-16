"""INV-178 — version is one fact: every skill inherits the pack VERSION, the stamp writes it.

Ten skills carried ten unrelated hand-rolled versions (1.0.0 through 1.1.4) while the pack was
2.0.0 — a per-skill number drifts the moment attention does, and a prover record naming the
skill version that ran the pass named a number nobody maintained. The root VERSION file is the
one home; frontmatter versions and in-text base references are stamped copies, held here.
"""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = open(os.path.join(REPO, "VERSION"), encoding="utf-8").read().strip()


def _skills():
    d = os.path.join(REPO, "skills")
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name, "SKILL.md")
        if os.path.isfile(p):
            yield name, open(p, encoding="utf-8").read()


def test_every_skill_frontmatter_version_equals_pack_version():
    for name, body in _skills():
        m = re.search(r"^  version: (\S+)$", body, flags=re.M)
        assert m, "%s: no frontmatter version line" % name
        assert m.group(1) == VERSION, "%s: version %s, pack %s" % (name, m.group(1), VERSION)


def test_every_base_reference_equals_pack_version():
    rx = re.compile(r"`live-spec-base` \(v(\d+\.\d+\.\d+)\)")
    for name, body in _skills():
        for got in rx.findall(body):
            assert got == VERSION, "%s: base reference v%s, pack %s" % (name, got, VERSION)


def test_spec_states_the_law():
    spec = open(os.path.join(REPO, "PRODUCT_SPEC.md"), encoding="utf-8").read()
    assert "version is one fact" in spec
    assert "| INV-178 |" in spec
