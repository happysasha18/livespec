"""INV-159 (the forward-binding law has one stated home) and INV-160 (the
suite-honesty / test-infrastructure invariants are one declared class with a
stated net-parity).

ROADMAP 322: forward-binding was cited to two silent roots (INV-15 / T-16 kin /
A-3 / INV-21 kin), neither of which STATED the law in its own text. INV-159 mints
the law once and every forward-binding cite is repointed at it, so a reader
tracing "binds forward" lands on the sentence that states it.

ROADMAP 328: the test-infrastructure family sat co-located in one section but was
never declared a same-kind class with an enumerated parity, unlike INV-101 / 125 /
153 / 156. INV-160 declares it, enumerates its nine members, and states the parity
(each member names the net that reddens a run on its own violation), so an
under-netted member becomes the prover's declared-class defect [INV-125].

String-level assertions on the shipped PRODUCT_SPEC.md. Landed 2026-07-15."""
from conftest import ROOT, read

INFRA_MEMBERS = ("INV-77", "INV-78", "INV-79", "INV-80", "INV-100",
                 "INV-102", "INV-155", "INV-157", "INV-158")


def _spec():
    return read("PRODUCT_SPEC.md")


def _index_row(anchor):
    """The Formal-index row text for an anchor, or None."""
    for line in _spec().splitlines():
        if line.startswith("| %s |" % anchor):
            return line
    return None


# ---- INV-159: the forward-binding law has one stated home

def test_forward_binding_law_stated_once():
    spec = _spec()
    # the law is stated in its own sentence, in words, tagged INV-159 (the requirement title
    # carries the sentence; the new format never puts a period at the end of a title)
    assert "A duty binds forward from the first landing after its clause exists" in spec
    assert "[INV-159]" in spec
    # and it carries a Formal-index row; the new-format index carries locations only (SPEC
    # INV-271), so the "binds forward" prose check moves to the title assertion above.
    row = _index_row("INV-159")
    assert row is not None, "INV-159 has no Formal-index row"


def test_forward_binding_cites_are_repointed_off_the_silent_roots():
    spec = _spec()
    # the mislabels the prover named (F1/F5) are gone: no forward-binding cite still
    # points at INV-15 (the node/matrix law), T-16-kin, or INV-21-kin
    assert "binds forward [INV-15]" not in spec
    assert "binds forward like INV-74 [INV-15]" not in spec
    assert "forward-binding intake law [T-16 kin]" not in spec
    assert "never retroactively en masse [INV-21 kin]" not in spec
    # and the repointed cites resolve to INV-159 instead — the footprint-note duty (one of the
    # silent-root sites the docstring names) now co-cites its own code with the forward-binding
    # law in the same criterion, rather than a bare or misrouted citation
    assert (
        "require the footprint note only on a feature-or-refactor row landed once the "
        "impact-analysis station was law" in spec
    )
    assert "[INV-134, INV-159]" in spec
    # the kind-axis backfill duty (the other silent-root site, once bare T-16) now co-cites
    # T-16 alongside INV-159 in its own criterion
    assert "[T-16, INV-159]" in spec


def test_every_binds_forward_clause_cites_the_law():
    # INV-159's standing net (the enforced membership the design review recommended, and the reverse of
    # the prover's F1 where the body once claimed cites that were absent): every clause saying a duty
    # "binds forward" carries [INV-159], so a stray one is caught here rather than drifting to a silent
    # or missing root. Each self-enforcing instance (INV-103/134/156/160) states its own arm AND cites
    # the law, which this net proves.
    #
    # In the new requirements format, only a numbered acceptance-criterion line ever trails a
    # bracket code — a requirement title, its Context, its User Story, and a Case heading never
    # do, by construction (SPEC: "Bracket codes ... trail a criterion"). So the net scopes to
    # criterion lines only; a heading merely naming "binds forward" is not an offender.
    import re
    offenders = []
    for i, line in enumerate(_spec().splitlines(), 1):
        if not re.match(r"^\d+\.\s", line.strip()):
            continue
        if re.search(r"binds? forward", line) and "INV-159" not in line:
            offenders.append((i, line.strip()[:90]))
    assert not offenders, "'binds forward' clause(s) not citing INV-159: %r" % offenders


# ---- INV-160: the test-infrastructure family is one declared class with net-parity

def test_infra_family_declared_a_class():
    spec = _spec()
    assert "The suite-honesty invariants are one class" in spec
    assert "[INV-160]" in spec
    row = _index_row("INV-160")
    assert row is not None, "INV-160 has no Formal-index row"


def test_infra_class_enumerates_every_member():
    # CANDIDATE REAL DEFECT (see repin log): the class clause must name each of the nine
    # members, so an author adding a tenth has an enumerated parity to write against (the gap
    # the design review flagged). The rewritten Requirement 116 states the class and its
    # parity rule but no longer enumerates the member codes anywhere in its body — confirmed
    # by reading the full requirement section (title through the next "---"). Left red.
    body = _spec().split("The suite-honesty invariants are one class", 1)[1].split("[INV-160]", 1)[0]
    for member in INFRA_MEMBERS:
        assert member in body, "class clause omits %s" % member


def test_infra_class_states_net_parity_and_binds_forward():
    # the old split-at-first-"[INV-160]" extraction truncated at the end of criterion 1 in the
    # new format, where "[INV-160]" now appears once per criterion rather than once at a
    # paragraph's end; widen it to the whole Requirement 116 section (title to the next "---")
    # so criterion 2's [INV-125] cite is actually in view.
    body = _spec().split(
        "## Requirement 116: The suite-honesty invariants are one class", 1
    )[1].split("\n---\n", 1)[0]
    # the parity: each member names the net that reddens a run on its violation
    assert "name the net" in body
    # a member with no net is the prover's declared-class defect (co-bracketed with a sibling
    # code in the new format, never a bare "[INV-125]")
    assert "INV-160, INV-125, INV-156]" in body
    # CANDIDATE REAL DEFECT (see repin log): the class's own "Case: the class binds forward"
    # criterion (3) cites only [INV-160, INV-157, INV-158] — it never co-cites INV-159, unlike
    # its sibling self-enforcing classes (e.g. INV-180's own "class binds forward" criterion
    # cites [INV-180, INV-159]). Left red.
    assert "binds forward [INV-159]" in body
