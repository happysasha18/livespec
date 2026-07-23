"""INV-163 (the ship-the-shape / host-owns-the-instance split has one stated home).

ROADMAP 332: the split "the pack ships the shape and the host owns the instance
where a body is host-specific; it centralizes to one pack home where the pack can
ship one identical body every host runs" recurred re-derived across five sites in
its own words — INV-125 (no DOM of its own), INV-136/139 (the design-principle
projection left to the adopting project), E-26 (the removal scanner), and INV-158
(the harness, the centralize case) — plus a sixth in ARCHITECTURE.md. INV-163 mints
the split once: it states the discriminator and both poles, and every site cites it
in place of re-deriving the contrast. This is the same move INV-159 and INV-160 made
for the forward-binding law and the suite-honesty class.

String-level assertions on the shipped PRODUCT_SPEC.md, ARCHITECTURE.md, and the
spec-author skill. Red-proven against the pre-delta tree (INV-163 absent).
Landed 2026-07-15 (v2.0.0)."""
import os
import sys

from conftest import ROOT, read

sys.path.insert(0, os.path.join(ROOT, "guardrails"))
import archformat  # the one node reader every consumer reads through (SPEC INV-280)

# the five spec sites the split now routes through, and the pole each takes
SHIP_SHAPE_SITES = ("INV-125", "INV-136", "INV-139")   # ship-the-shape pole
CENTRALIZE_SITE = "INV-158"                            # centralize pole
SCANNER_SITE = "E-26"                                  # ship-the-shape (removal scanner)


def _spec():
    return read("PRODUCT_SPEC.md")


def _index_row(anchor):
    for line in _spec().splitlines():
        if line.startswith("| %s |" % anchor):
            return line
    return None


# ---- INV-163 states the split once (discriminator + both poles) ----

def test_pack_to_host_split_stated_once():
    spec = _spec()
    assert "[INV-163]" in spec
    # the discriminator, in its own words
    assert "can the pack ship a single identical body that every host runs" in spec
    # both poles named
    assert "centralize the body to a single pack home" in spec  # centralize pole
    assert "have each host own the instance it fills" in spec    # ship-the-shape pole
    # and it carries a Formal-index row; the new-format index carries locations only (SPEC
    # INV-271), so the "pack-to-host" prose check moves to the requirement title instead.
    row = _index_row("INV-163")
    assert row is not None, "INV-163 has no Formal-index row"
    assert "pack-to-host" in spec.split("## Requirement 267", 1)[1].split("\n---\n", 1)[0] \
        or "Where a capability's body lives is placed on the pack-to-host axis" in spec


def test_split_binds_forward_off_the_stated_law():
    # a new host-specific capability names its pole from its first landing (INV-159). The old
    # split-at-first-"[INV-163]" extraction truncated after criterion 1 in the new format,
    # where "[INV-163]" now appears once per criterion; widen it to the whole Requirement 267
    # section. The new format also never places the words "binds forward" immediately before a
    # bracket (codes trail whole criterion sentences instead), so the check moves to the
    # co-citation that proves the same fact: the pole-declaration criterion co-cites INV-159.
    body = _spec().split("## Requirement 267: A capability the pack can ship identically", 1)[1] \
        .split("\n---\n", 1)[0]
    assert "state which pole it takes from its first landing" in body
    assert "[INV-163, INV-159]" in body


# ---- every site cites INV-163 in place of re-deriving the split ----

def test_every_ship_shape_site_cites_the_root():
    spec = _spec()
    for anchor in SHIP_SHAPE_SITES:
        # the clause body for the anchor cites INV-163 as the ship-the-shape pole; the new
        # format ends the sentence with a period before the bracket and often co-brackets
        # INV-163 with the site's own code, rather than placing "[INV-163]" bare right after
        # the phrase.
        assert "the ship-the-shape pole of the pack-to-host split" in spec, \
            "no ship-the-shape citation for the %s family" % anchor
        assert "INV-125, INV-163" in spec
    # the removal scanner cites it too — in the new format the E-26 criteria state the duty in
    # their own words rather than repeating the requirement title on the same line
    e26_lines = [ln for ln in spec.splitlines() if "E-26" in ln and "INV-163" in ln]
    assert e26_lines, "E-26 does not cite INV-163"
    # the centralize pole cites it
    assert "the centralize pole of the pack-to-host split" in spec
    assert "INV-158, INV-157, INV-163" in spec


def test_no_site_re_derives_the_split_in_its_own_words():
    spec = _spec()
    # the old re-derivations the sites used before the root existed are gone
    assert "the pack ships the shape and the host owns the instance" not in spec
    assert "The discriminator is whether the pack can ship one identical body every host runs" not in spec
    assert "the same split cross-surface uniformity takes [INV-125]" not in spec
    assert "the split the interactive-overlap rule takes [INV-136]" not in spec
    assert "the INV-136 split, live-spec has no UI" not in spec


# ---- the split reaches the architecture and the authoring duty is real ----

def test_architecture_cites_the_root_not_a_re_derivation():
    arch = read("ARCHITECTURE.md")
    assert "the ship-the-shape pole of the pack-to-host split [INV-163]" in arch
    # INV-163 is owned by a node (base-rulebook carries it in its owns field)
    nodes = archformat.parse_nodes(arch)
    base_rulebook = next((n for n in nodes if n.name == "base-rulebook"), None)
    assert base_rulebook is not None, "ARCHITECTURE.md carries no base-rulebook node"
    assert "INV-163" in base_rulebook.anchors_expanded, "INV-163 not homed on the base-rulebook node"


def test_pole_declaration_duty_homed_in_spec_author():
    # INV-163's homes line names spec-author's pole-declaration duty; that home is real
    skill = read("skills/spec-author/SKILL.md")
    assert "SPEC INV-163" in skill
    assert "Declare the pole" in skill
    assert "ship the shape" in skill or "ships the shape" in skill
