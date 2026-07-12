"""Suite hygiene: the run leaves the machine as it found it (SPEC INV-100, M-236, row 222).

A session-scoped before/after diff of the system temp home, filtered to the suite's own
artifact prefixes — a new file surviving to session end is a leak and fails the run.
"""

import os
import tempfile

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


_PREFIXES = ("livespec-test-", "row241-host-")


def _ours(names):
    return {n for n in names if n.startswith(_PREFIXES)}


@pytest.fixture(autouse=True, scope="session")
def suite_leaves_no_trace():
    tmp = tempfile.gettempdir()
    before = _ours(set(os.listdir(tmp)))
    yield
    after = _ours(set(os.listdir(tmp)))
    leaked = sorted(after - before)
    assert not leaked, "the suite leaked temp artifacts (SPEC INV-100): %s" % leaked
