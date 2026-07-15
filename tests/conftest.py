"""Suite hygiene: the run leaves the machine as it found it (SPEC INV-100, M-236, row 222).

A session-scoped before/after diff of the system temp home, filtered to the suite's own
artifact prefixes — a new file surviving to session end is a leak and fails the run.
"""

import glob
import os
import re
import tempfile

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    return " ".join(read(rel).split())


def _skill_surface(rel):
    """The files that make up a skill's whole normative surface.

    A skill may offload set-piece material (large tables, worked examples) from its
    SKILL.md into a sibling references/ directory to stay within the length budget —
    build-pipeline does. A content-presence check reads the skill as ONE home, so its
    surface is SKILL.md plus its references/*.md: the anchor is found wherever inside
    the skill it lives. A size check keeps reading SKILL.md alone via read(), because
    the body-thinness ideal is about the SKILL.md body itself.
    """
    m = re.match(r"(skills/[^/]+)/SKILL\.md$", rel)
    if not m:
        return [rel]
    refs = sorted(glob.glob(os.path.join(ROOT, m.group(1), "references", "*.md")))
    return [rel] + [os.path.relpath(p, ROOT) for p in refs]


def read_all(rel):
    """A skill's whole normative surface (SKILL.md + references/*.md) as one text."""
    texts = []
    for r in _skill_surface(rel):
        with open(os.path.join(ROOT, r), encoding="utf-8") as f:
            texts.append(f.read())
    return "\n".join(texts)


def read_all_flat(rel):
    """The whole-surface text with whitespace collapsed, so wrapped lines match needles."""
    return " ".join(read_all(rel).split())


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
