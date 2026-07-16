"""INV-174 — the inbox's local co-located arm: the deposit is the file alone, never a git act.

Co-located sessions share one working tree and one git index, so a depositor's git add or
commit races whatever the assigned session holds staged mid-landing. The local deposit stops
at writing the one new file; the assigned session's sweep commits the harvest itself. The
remote arm's commit-and-push road stays (INV-112).
"""
from conftest import read


def test_spec_states_the_local_arm():
    spec = read("PRODUCT_SPEC.md")
    assert "local co-located arm" in spec
    assert "| INV-174 |" in spec


def test_local_deposit_never_stages():
    spec = read("PRODUCT_SPEC.md")
    assert "no staging, no commit, no push" in spec


def test_inbox_readme_carries_the_split():
    readme = read("inbox/README.md")
    assert "same filesystem" in readme
    assert "INV-174" in readme
