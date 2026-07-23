"""The installed-copy drift-net class is declared once (SPEC INV-180, ROADMAP row 356).

The pack authors artifacts that live twice — a source copy in the pack and a running copy on
the host — and four such pairs already each named their own staleness net in their own words
(the vendored-kit ratchet pin INV-172/177, the installed-hooks config-health check INV-175, the
stamped-version guard INV-178) with no sentence declaring them one class or stating the shared
parity. INV-180 declares the class, enumerates its four members (vendored kit scripts, installed
hooks and gates, stamped version copies, installed skills), states the parity every member holds
(each names the mechanical net that tells its running copy stale), and binds forward off INV-159 —
mirroring the sibling class-declaration shape (INV-156, INV-160).

String-level assertions on the shipped PRODUCT_SPEC.md.
"""
from conftest import read, read_flat

# Requirement 275: The pack's authored artifacts and their installed copies are one class [INV-180].
# The requirements-format rewrite spreads the class's parity and its per-member nets across the
# Context paragraph and six numbered acceptance criteria rather than one prose paragraph, so the
# needles below re-pin to the same content across that wider span.
CLASS_LEAD = "The pack's authored artifacts and their installed copies are one class"
PARITY_SENTENCE = ("The class carries one parity: each member names the mechanical net that "
                    "tells its running copy stale.")


def _spec():
    return read("PRODUCT_SPEC.md")


def _spec_flat():
    return read_flat("PRODUCT_SPEC.md")


def _index_row(anchor):
    """The Formal-index row text for an anchor, or None."""
    for line in _spec().splitlines():
        if line.startswith("| %s |" % anchor):
            return line
    return None


def _class_body():
    flat = _spec_flat()
    start = flat.index("## Requirement 275:")
    end = flat.index("## Requirement 276:", start)
    return flat[start:end]


def test_installed_copy_class_declared():
    spec = _spec_flat()
    assert CLASS_LEAD in spec, "the installed-copy class clause is missing from the spec body"
    assert "[INV-180]" in spec, "INV-180 has no body owner"
    # index now carries locations only (SPEC INV-271) — the row's presence is the anchor proof.
    row = _index_row("INV-180")
    assert row is not None, "INV-180 has no Formal-index row"


def test_installed_copy_class_enumerates_every_member():
    body = _class_body()
    for phrase, anchors in (
        ("the vendored kit scripts", ("INV-172", "INV-177")),
        ("the installed hooks and gates", ("INV-173", "INV-175")),
        ("the stamped version copies", ("INV-178",)),
        ("the installed skills", ("A-7", "M-7", "E-23", "E-25")),
    ):
        assert phrase in body, "class clause omits member: %s" % phrase
        for anchor in anchors:
            assert anchor in body, "member %r missing its anchor %s" % (phrase, anchor)


def test_installed_copy_class_states_parity_and_binds_forward():
    body = _class_body()
    # the parity: each member names the mechanical net that tells its running copy stale
    assert PARITY_SENTENCE in body
    # the installed-skills member is named the class's acknowledged weakest, held by discipline
    # rather than a machine, distinguishing it from its three machine-held siblings
    assert "weakest member" in body
    assert "held by discipline" in body
    # and the class binds forward, its own named Case, off the one stated law [INV-159]
    assert "the class binds forward" in body
    assert "INV-159" in body
