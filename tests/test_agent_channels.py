"""When agents work together — the agent/skill boundary, the two channels, the roster and the
card, the published contract, the earned message, and the birth walk.

Matrix rows M-352..M-368, derived from the spec's `## When agents work together` section through
ARCHITECTURE.md's node table: base-rulebook (E-31, INV-182, INV-183, INV-188, INV-189, INV-190,
INV-191, INV-193, INV-194), spec-author (E-33, INV-185, INV-186, INV-187), host-contract (E-32,
INV-184), inbox (INV-192), build-pipeline (T-22).

Levels, in this repo's declared four-rung vocabulary (the matrix header's recorded interpretation;
the closed set is enforced at tests/test_traceability.py): the pack ships documents, so a law's
rendered level is a `string` assertion against the SHIPPED file on disk. Two rows here go past a
document read and exercise a real artifact, the way the guardrail rows M-229..M-231 already do —
`test_gate_passes_a_message_naming_its_blocked_work` / `test_gate_reds_a_message_naming_no_blocked_work`
run `guardrails/check-earned-message.py` against a real fixture deposit and read its exit code both
ways, and `test_pack_card_exists_and_names_its_five_fields` reads this pack's own real card from disk.

The contract's mechanical arms (a producer's permission gate, a consumer's freshness check, a
compatibility test) are NOT asserted here: this pack contains no data producer, so there is nothing
to exercise, and they ship when a host declares its first contract (ROADMAP row 385, [target]). The
rows for E-33, INV-185, INV-186 and INV-187 assert that those laws stand in the documents today.
"""

import os
import re
import shutil
import subprocess
import tempfile
import unittest

from conftest import ROOT, read, read_flat


SPEC = "PRODUCT_SPEC.md"
BASE = "skills/live-spec-base/SKILL.md"


def _index_row(anchor):
    """True when the spec's Formal index carries a row for this anchor."""
    return any(l.startswith("| %s |" % anchor) for l in read(SPEC).splitlines())


def _declaration(anchor):
    """The one prose paragraph in the spec that DECLARES this anchor.

    The home is the paragraph whose trailing anchor is the code; an index row is a lookup into
    that home, so table lines are passed over. Scoping a needle to the declaration keeps a check
    from passing off the index row or a neighbouring clause that merely cites the code
    (ROADMAP row 384, the vacuous-pass class).
    """
    tail = "[%s]" % anchor
    found = [l for l in read(SPEC).splitlines()
             if l.rstrip().endswith(tail) and not l.lstrip().startswith("|")]
    return " ".join(" ".join(found).split()) if found else ""


def _architecture_owners(anchor):
    """Every node whose owns-anchors cell lists this anchor.

    ARCHITECTURE.md's node table reads `| node | responsibility | owns | pins |`, so an owned
    anchor is a token in the third cell. An anchor sitting only in loose prose is owned by
    nobody and reads as zero owners here — the reading a whole-file search cannot make.
    """
    owners = []
    for line in read("ARCHITECTURE.md").splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 3:
            continue
        tokens = [re.sub(r"\s*\(.*", "", tok).strip() for tok in re.split(r"[,;]", cells[2])]
        if anchor in tokens:
            owners.append(cells[0])
    return owners


class _AnchorHomeMixin:
    def assert_index_and_ownership(self, anchor):
        self.assertTrue(_index_row(anchor), "%s index row missing" % anchor)
        owners = _architecture_owners(anchor)
        self.assertEqual(len(owners), 1,
                         "%s is owned by %d architecture nodes %s; every spec fact is owned by "
                         "exactly one node" % (anchor, len(owners), owners))

    def assert_declared(self, anchor):
        """The anchor's own declaration paragraph, asserted present before it is read."""
        clause = _declaration(anchor)
        self.assertTrue(clause, "%s has no declaring paragraph in %s; the home is absent"
                                % (anchor, SPEC))
        return clause


# --------------------------------------------------------------------------- #
# [node: base-rulebook]
# --------------------------------------------------------------------------- #

class TestAgentSkillBoundary(unittest.TestCase, _AnchorHomeMixin):
    """E-31 / INV-182 (M-352, M-353) — an agent is a project window whose things outlive any one
    conversation; a skill loads into a window and dies with the session."""

    def test_agent_is_a_project_window(self):
        spec = read_flat(SPEC)
        self.assertIn("An agent is a project window, and everything an agent works with is its own",
                      spec)
        self.assertIn("its own tree, its own queue, its own gates, its own contracts, "
                      "a standing mission, and a seat in the roster", spec)
        self.assertIn("Each of those outlives any one conversation", spec)
        self.assertIn("[E-31]", spec)

    def test_skill_dies_with_the_session(self):
        spec = read_flat(SPEC)
        self.assertIn("A skill is a capability any window loads, and it dies with the session", spec)
        self.assertIn("A skill holds no tree, no mission, and no queue of its own", spec)
        self.assertIn("leaves nothing standing when the conversation ends", spec)

    def test_e31_index_and_ownership(self):
        self.assert_index_and_ownership("E-31")

    def test_grain_boundary_names_its_three_marks(self):
        """The grain test is durable state + a standing mission + a zone of its own — never size."""
        spec = read_flat(SPEC)
        self.assertIn("durable state, a standing mission, and a zone of its own make a capability "
                      "an agent, and a capability living wholly inside a session is a skill", spec)
        self.assertIn("[INV-182]", spec)

    def test_grain_on_the_line_is_the_owners_word(self):
        spec = read_flat(SPEC)
        self.assertIn("Where a real case sits on the line, the owner's word places it", spec)

    def test_inv182_index_and_ownership(self):
        self.assert_index_and_ownership("INV-182")


class TestTwoChannels(unittest.TestCase, _AnchorHomeMixin):
    """INV-183 (M-354) — exactly two channels, and the reply rides one of them backwards so the
    count of two holds."""

    def test_exactly_two_channels_in_the_spec(self):
        spec = read_flat(SPEC)
        self.assertIn("Exactly two channels carry everything that passes between two agents", spec)
        self.assertIn("[INV-183]", spec)

    def test_no_third_channel_exists(self):
        spec = read_flat(SPEC)
        self.assertIn("No third channel exists between two agents", spec)
        self.assertIn("A reply rides the inbox channel in the other direction, so the count of "
                      "two holds", spec)
        self.assertIn("a remote agent reaches the other through git alone", spec)

    def test_base_rulebook_carries_the_two_channel_law(self):
        self.assertIn("exactly two channels", read_flat(BASE),
                      "the base rulebook does not carry the two-channel law")

    def test_inv183_index_and_ownership(self):
        self.assert_index_and_ownership("INV-183")


class TestDataNeverTravelsAsAMessage(unittest.TestCase, _AnchorHomeMixin):
    """INV-188 (M-355) — a consumer wanting data reads the contract; a consumer wanting a field
    the contract lacks holds a request about the contract's shape."""

    def test_data_never_travels_as_a_message(self):
        spec = read_flat(SPEC)
        self.assertIn("Data never travels as a message", spec)
        self.assertIn("A consumer wanting data reads the contract", spec)
        self.assertIn("[INV-188]", spec)

    def test_missing_field_routes_to_the_earned_message(self):
        spec = read_flat(SPEC)
        self.assertIn("A consumer wanting a field the contract lacks holds a request about the "
                      "contract's shape", spec)

    def test_inv188_index_and_ownership(self):
        self.assert_index_and_ownership("INV-188")


class TestEarnedMessage(unittest.TestCase, _AnchorHomeMixin):
    """INV-189 (M-356) — a message names the sender's OWN blocked work, in the message; the births
    are a closed set of two; the zone's owner is presumed competent and informed."""

    def test_earned_message_names_its_block(self):
        """F-agent-ask's named test (ARCHITECTURE.md feature coverage)."""
        spec = read_flat(SPEC)
        self.assertIn("A message names its birth, in the message", spec)
        self.assertIn("names the blocked work", spec)
        self.assertIn("names the fault and the evidence the sender lived", spec)
        self.assertIn("A message that can name neither is never sent", spec)
        self.assertIn("[INV-189]", spec)

    def test_two_births_are_a_closed_set(self):
        spec = read_flat(SPEC)
        self.assertIn("A message has exactly three births, and the set is closed", spec)
        self.assertIn("A candidate message matching no birth has no birth, and it stays "
                      "unsent", spec)

    def test_owner_presumed_competent_and_informed(self):
        spec = read_flat(SPEC)
        self.assertIn("The zone's owner is presumed competent and informed", spec)
        self.assertIn("That presumption is what keeps the second birth narrow", spec)

    def test_base_rulebook_carries_the_earned_message_law(self):
        self.assertIn("names the sender's own blocked work", read_flat(BASE),
                      "the base rulebook does not carry the earned-message law")

    def test_inv189_index_and_ownership(self):
        self.assert_index_and_ownership("INV-189")


class TestEarnedMessageGate(unittest.TestCase):
    """INV-189's mechanical arm (M-356), exercised: `guardrails/check-earned-message.py` runs
    against a real fixture inbox deposit and its exit code is read both ways. The gate's own
    contract: exit 0 when every agent message names its blocked work, exit 1 when one does not.

    The deposit's source has one home, the filename (`inbox/README.md`): an agent's deposit is
    `YYYY-MM-DD-from-<agent>-<slug>.md`, which is the form the folder's real corpus has carried
    since 2026-07-10. `from-owner` and the monitor's `stranger-*` are the reserved non-agent
    doors, and they owe nothing (INV-193, INV-146). The fixtures below take that real form, so
    the suite exercises the format the pack ships. The 2026-07-17 audit found the gate inert on
    it — every hostile fixture the audit proved passing owns a test here.
    """

    SCRIPT = os.path.join(ROOT, "guardrails", "check-earned-message.py")

    # The real deposit that proved the gate inert (the audit's live evidence). Frozen here in
    # the shape it landed in, so this regression outlives the sweep that removes the file.
    REAL_DEPOSIT = "2026-07-17-from-track-coach-worker-completion-orphans-runaway-child.md"
    REAL_DEPOSIT_FROZEN = (
        "# feedback: a worker's completion should also reap its spawned OS subprocesses\n\n"
        "**The item (a worker-hygiene rule for the pack's orchestration).** When a subagent\n"
        "finishes, that signals the AGENT is done; the OS processes it spawned can still be alive.\n\n"
        "**Why (what happened, 2026-07-17, track-coach s77).** A background worker's orphaned child\n"
        "burned a full CPU core at 100% for 46 minutes doing work nobody would read.\n\n"
        "**Who threw it.** track-coach window (this Mac), session s77, 2026-07-17.\n"
    )

    def setUp(self):
        # The suite's own prefix, so conftest's session-scoped leak diff can see a leak (INV-100).
        self.tmp = tempfile.mkdtemp(prefix="livespec-test-agent-inbox-")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _deposit(self, name, text):
        path = os.path.join(self.tmp, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path

    def _run(self):
        return subprocess.run(["python3", self.SCRIPT, self.tmp],
                              capture_output=True, text=True)

    def _assert_gate_present(self):
        self.assertTrue(os.path.isfile(self.SCRIPT),
                        "the earned-message gate is absent: guardrails/check-earned-message.py "
                        "(SPEC INV-189)")

    # -- the corpus format, both ways ---------------------------------------- #

    def test_gate_passes_a_message_naming_its_blocked_work(self):
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-render-offset-unpinned.md",
                      "# the render offset stays unpinned\n\n"
                      "Blocked: ROADMAP row 12 cannot land while the render offset stays unpinned\n"
                      "Need-by: 2099-07-24\n"
                      "Id: track-coach-s77-a1\n\n"
                      "The body of the request.\n")
        r = self._run()
        self.assertEqual(r.returncode, 0,
                         "the gate red an earned message that names its blocked work:\n%s"
                         % (r.stdout + r.stderr))

    def test_gate_reds_a_message_naming_no_blocked_work(self):
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-thought-you-should-know.md",
                      "# a thought\n\n"
                      "Need-by: 2099-07-24\n"
                      "Id: track-coach-s77-a2\n\n"
                      "I thought you might want to know about this.\n")
        r = self._run()
        self.assertEqual(r.returncode, 1,
                         "the gate passed an agent message naming no blocked work (SPEC INV-189)")
        self.assertIn("INV-189", r.stdout + r.stderr,
                      "the gate's finding does not cite the law it enforces")

    def test_gate_reds_the_real_corpus_format_carrying_no_body_source_field(self):
        """The audit's finding 1: the source's home is the filename, and the corpus writes no
        body `From:` field at all. A gate keyed on that body field is inert on everything the
        pack actually ships."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-tlvphotos-face-reentry-state.md",
                      "# the face re-entry state\n\n"
                      "The item, in plain words, with no field naming any work of my own.\n\n"
                      "**Who threw it.** tlvphotos window, session s41.\n")
        r = self._run()
        self.assertEqual(r.returncode, 1,
                         "the gate is inert on the pack's own inbox format: a deposit whose "
                         "filename names an agent source passed while naming no blocked work "
                         "(SPEC INV-189, inbox/README.md's format)")

    def test_gate_passes_a_fault_message_naming_what_it_lived(self):
        """INV-189's second birth. A fault message owes the evidence the sender lived, and
        nothing of that sender's need stand still — a gate demanding blocked work of both
        births would refuse the fault message, which is the message a neighbour most wants."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-worker-orphans-a-child.md",
                      "# a worker's completion leaves its child alive\n\n"
                      "Lived: s77 ran a background re-render; the worker returned while its child "
                      "burned a core at 100% for 46 minutes, shown by ps against an idle output "
                      "file (2026-07-17)\n"
                      "Need-by: 2099-08-01\n"
                      "Id: track-coach-s77-a6\n")
        r = self._run()
        self.assertEqual(r.returncode, 0,
                         "the gate red a fault message that names the evidence it lived; the "
                         "fault birth owes the evidence (SPEC INV-189):\n%s"
                         % (r.stdout + r.stderr))

    def test_gate_reds_a_message_naming_neither_birth(self):
        """The births are a closed set of two, and a candidate matching neither stays unsent."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-a-thought-about-your-zone.md",
                      "# a thought\n\n"
                      "Need-by: 2099-07-24\n"
                      "Id: track-coach-s77-a7\n\n"
                      "Your dashboard already shows this, and I thought you might want to know.\n")
        r = self._run()
        self.assertEqual(r.returncode, 1,
                         "a message naming neither birth passed (SPEC INV-189)")

    def test_gate_declines_the_real_track_coach_deposit(self):
        """The audit's live proof, run as a regression, and the reason INV-189 was corrected on
        2026-07-17. The deposit is earned under the SECOND birth: track-coach lived a fault in
        the pack's zone and carries the evidence it lived (s77, an orphaned child burning a core
        for 46 minutes) — the outside view the pack's own instruments cannot take. It names no
        blocked work, correctly: nothing of track-coach's own stood still. What it carries no
        field for is the evidence, which sits in its prose under a `**Why (what happened...)**`
        heading, so the gate declines it at the door on the format alone. One `Lived:` line
        clears the red, and the sweep clears it by harvesting the file. The real bytes are read
        while the file is on disk; the frozen shape carries the regression once it is swept."""
        self._assert_gate_present()
        rel = os.path.join("inbox", self.REAL_DEPOSIT)
        on_disk = os.path.isfile(os.path.join(ROOT, rel))
        self._deposit(self.REAL_DEPOSIT, read(rel) if on_disk else self.REAL_DEPOSIT_FROZEN)
        r = self._run()
        self.assertEqual(r.returncode, 1,
                         "the gate passed the 2026-07-17 track-coach deposit, which names its "
                         "lived fault in prose and carries no field for it (SPEC INV-189)")
        self.assertIn("INV-189", r.stdout + r.stderr)

    def test_the_real_deposit_names_no_blocked_work_and_the_spec_says_so(self):
        """The deposit the spec holds up as its first real message. Nothing of track-coach's own
        stood still, so a gate demanding blocked work of it would refuse a message the law calls
        correct. This pins the fixture's shape against the law it drove."""
        rel = os.path.join("inbox", self.REAL_DEPOSIT)
        if not os.path.isfile(os.path.join(ROOT, rel)):
            return  # swept into its routed home; the frozen shape above carries the regression
        deposit = read(rel)
        self.assertNotIn("Blocked:", deposit,
                         "the deposit names blocked work, so it is no longer the fault-birth "
                         "fixture this suite reads it as (SPEC INV-189)")
        self.assertIn("s77", deposit,
                      "the deposit carries no session evidence, which is what earns a fault "
                      "message its file (SPEC INV-189)")

    # -- the doors that owe nothing ------------------------------------------ #

    def test_gate_reads_the_owners_own_deposit_as_owing_nothing(self):
        """A wish from the owner carries the owner's own authority (INV-193). The reserved word
        is the role, since a shipped file names no person (INV-120's gate)."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-owner-please-fix-the-thing.md",
                      "# please fix the thing\n\n"
                      "The thing is broken. Fix it.\n")
        r = self._run()
        self.assertEqual(r.returncode, 0,
                         "the gate asked the owner's own wish for blocked work (SPEC INV-193):\n%s"
                         % (r.stdout + r.stderr))

    def test_gate_reads_a_relayed_owner_wish_as_owing_nothing(self):
        """An agent relaying the owner's word carries the owner's authority: relaying changes a
        message's carrier and leaves its authority exactly where it started (INV-193). So the
        filename names whose the item is — `from-owner` — and the body names the window that
        threw it. The live promoter deposit of 2026-07-17 is this case, and a gate reading the
        depositing window as the source would ask the owner's own instruction for a birth."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-owner-agent-ownership-and-routing.md",
                      "# Wish: who owns a cross-cutting concern (owner's word, 2026-07-17)\n\n"
                      "The owner asks live-spec to own the meta-question.\n\n"
                      "## Who threw it\n\n"
                      "The promoter product-dev window, relaying the owner's word.\n")
        r = self._run()
        self.assertEqual(r.returncode, 0,
                         "the gate asked the owner's own relayed wish for a birth; his word "
                         "carries his own authority (SPEC INV-193):\n%s" % (r.stdout + r.stderr))

    def test_gate_leaves_a_bridged_stranger_issue_alone(self):
        """A stranger's Issue comes through the wish template and owes nothing (INV-146). The
        filename is the one the monitor writes (scripts/stranger-wish-monitor.py)."""
        self._assert_gate_present()
        self._deposit("stranger-issue-42-the-install-ratchet-appends-past-exit.md",
                      "surface-key: issue-42-gen0\n"
                      "source: GitHub Issue #42\n\n"
                      "# the install ratchet appends past exit\n\n"
                      "A stranger's report, owing no blocked work of anyone's.\n")
        r = self._run()
        self.assertEqual(r.returncode, 0,
                         "the gate asked a bridged stranger Issue for blocked work "
                         "(SPEC INV-146):\n%s" % (r.stdout + r.stderr))

    # -- the reply road (INV-192) -------------------------------------------- #

    def test_gate_passes_a_reply_naming_the_message_it_discharges(self):
        """INV-192: a reply owes no blocked work of its own, since the message it discharges
        already named the blocked work that earned the exchange; it names that message's
        identifier instead. The spec's own reply road red against the pre-fix gate."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-tlvphotos-reply-to-live-spec-s68-a41.md",
                      "From: tlvphotos (agent)\n"
                      "Re: live-spec-s68-a41\n"
                      "Terminal state: declined. The commerce policy lives in this agent's zone.\n")
        r = self._run()
        self.assertEqual(r.returncode, 0,
                         "the gate red a spec-legal reply, which owes no blocked work of its own "
                         "(SPEC INV-192):\n%s" % (r.stdout + r.stderr))

    def test_gate_reds_a_reply_naming_no_message(self):
        """The reply exemption stands on naming the message it discharges. A `Re:` line carrying
        a placeholder ties to nothing, so the deposit owes blocked work like any message."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-tlvphotos-reply-to-nothing.md",
                      "From: tlvphotos (agent)\n"
                      "Re: TBD\n"
                      "Terminal state: declined.\n")
        r = self._run()
        self.assertEqual(r.returncode, 1,
                         "a placeholder identifier bought the reply exemption (SPEC INV-192)")

    # -- the hostile fixtures the audit proved passing ----------------------- #

    def test_gate_reads_an_agent_marker_split_across_lines(self):
        """The audit's fixture: `From: live-spec` with `(agent)` on the NEXT line. The marker
        search read the captured value alone, so the deposit passed unread."""
        self._assert_gate_present()
        self._deposit("2026-07-17-a-deposit-with-a-wrapped-source-mark.md",
                      "# a request\n\n"
                      "From: live-spec\n"
                      "(agent)\n\n"
                      "No field of mine names any work.\n")
        r = self._run()
        self.assertEqual(r.returncode, 1,
                         "an agent marker wrapped onto the next line escaped the gate "
                         "(SPEC INV-189)")

    def test_gate_reads_a_deposit_that_is_not_markdown(self):
        """The audit's fixture: a `.txt` deposit. The scan globbed `*.md`, so renaming the file
        cleared the gate. Every deposit in the folder is read."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-a-plain-text-deposit.txt",
                      "# a request\n\nNo field of mine names any work.\n")
        r = self._run()
        self.assertEqual(r.returncode, 1,
                         "a deposit escaped the gate by its file extension (SPEC INV-189)")

    def test_gate_reads_the_source_marks_variants(self):
        """The audit's fixtures: a fullwidth colon, the field named `Sender`, and the marker in
        square brackets. Each read as no agent at all, so each passed unread."""
        self._assert_gate_present()
        variants = {
            "fullwidth colon": "From： live-spec (agent)\n",
            "the field named Sender": "Sender: live-spec (agent)\n",
            "the marker in square brackets": "From: live-spec [agent]\n",
        }
        for label, mark in variants.items():
            with self.subTest(variant=label):
                for f in os.listdir(self.tmp):
                    os.remove(os.path.join(self.tmp, f))
                self._deposit("2026-07-17-a-deposit-with-a-variant-mark.md",
                              "# a request\n\n" + mark + "\nNo field names any work of mine.\n")
                r = self._run()
                self.assertEqual(r.returncode, 1,
                                 "a source mark written with %s escaped the gate (SPEC INV-189)"
                                 % label)

    def test_gate_passes_over_a_field_inside_a_fenced_block(self):
        """The audit's fixture: `Blocked:` inside a fenced code block. The scan was line-based
        with no fence awareness, so quoting the template's block cleared the gate. A fenced block
        is an example, and the gate reads past it — for the source mark on the same terms, so a
        deposit quoting the card's block is not made agent traffic by the quote."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-a-fenced-field.md",
                      "# a request\n\n"
                      "Here is the shape the card prescribes:\n\n"
                      "```\n"
                      "Blocked: <the work of mine that stands until this is answered>\n"
                      "```\n\n"
                      "No field of my own names any work.\n")
        r = self._run()
        self.assertEqual(r.returncode, 1,
                         "a `Blocked:` field inside a fenced code block cleared the gate "
                         "(SPEC INV-189)")

    def test_gate_reds_a_blocked_field_that_only_points_elsewhere(self):
        """The audit's fixture: `Blocked: see above`. The field is a pointer carrying no work,
        which is the placeholder family the gate already nets (TBD, none, N/A). The match is the
        whole field, so a field that says `see above` AND names work stays legal."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-blocked-see-above.md",
                      "# a request\n\n"
                      "Blocked: see above\n"
                      "Id: track-coach-s77-a3\n")
        r = self._run()
        self.assertEqual(r.returncode, 1,
                         "a blocked-work field pointing elsewhere and naming nothing cleared the "
                         "gate (SPEC INV-189)")
        self._deposit("2026-07-17-from-track-coach-blocked-see-above.md",
                      "# a request\n\n"
                      "Blocked: see above — ROADMAP row 12 stands until this is answered\n"
                      "Id: track-coach-s77-a3\n")
        r = self._run()
        self.assertEqual(r.returncode, 0,
                         "a field naming real work red because it also pointed at the prose:\n%s"
                         % (r.stdout + r.stderr))

    # -- the fields the gate reports (INV-192) ------------------------------- #

    def test_gate_reports_a_need_by_it_can_see_without_redding(self):
        """The audit's finding 5: `Need-by:` was named in the usage and never read. It is read
        here and reported. It never reds: INV-192 gives an expired need-by one road — the
        SENDER's own status report, which the human reads — so a receiver's push is the wrong
        red for a sender's clock. An absent `Id:` reports on the same terms."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-an-expired-need-by.md",
                      "# a request\n\n"
                      "Blocked: ROADMAP row 12 cannot land while the render offset stays unpinned\n"
                      "Need-by: 2001-01-01\n"
                      "Id: track-coach-s77-a4\n")
        r = self._run()
        self.assertEqual(r.returncode, 0,
                         "an expired need-by red the receiver's gate; INV-192 sends the "
                         "escalation to the sender's own status report:\n%s"
                         % (r.stdout + r.stderr))
        self.assertIn("2001-01-01", r.stdout,
                      "the gate reads the need-by and reports nothing about it (SPEC INV-192)")
        self.assertIn("INV-192", r.stdout,
                      "the need-by report cites no law")

    def test_gate_reports_an_agent_message_that_states_no_need_by(self):
        """INV-192: every message states its need-by. The gate reports the absence and leaves the
        exit code to INV-189, the law this gate is the arm of."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-no-need-by.md",
                      "# a request\n\n"
                      "Blocked: ROADMAP row 12 cannot land while the render offset stays unpinned\n"
                      "Id: track-coach-s77-a5\n")
        r = self._run()
        self.assertEqual(r.returncode, 0)
        self.assertIn("need-by", r.stdout.lower(),
                      "a message stating no need-by drew no report (SPEC INV-192)")

    # -- the gate and the README name one format ----------------------------- #

    def test_gate_help_prescribes_the_format_the_readme_prescribes(self):
        """The audit's finding 4: the help printed a three-field template omitting `Id:`, so a
        sender following the error message wrote a message INV-192 refuses. The help names the
        filename form the README prescribes, and every field it names is one the spec requires."""
        self._assert_gate_present()
        self._deposit("2026-07-17-from-track-coach-thought-you-should-know.md",
                      "# a thought\n\nNo work of mine is named here.\n")
        r = self._run()
        self.assertEqual(r.returncode, 1)
        help_text = r.stdout
        self.assertIn("from-<agent>", help_text,
                      "the help does not name the filename form the README prescribes")
        self.assertIn("Blocked:", help_text)
        self.assertIn("Lived:", help_text,
                      "the help names one birth of the two, so a sender carrying a lived fault "
                      "reads that its message is unearned (SPEC INV-189)")
        self.assertIn("Id:", help_text,
                      "the help prescribes a message with no identifier, which INV-192 refuses")
        self.assertIn("Re:", help_text,
                      "the help does not name the reply road (SPEC INV-192)")
        self.assertNotIn("From: <name> (agent)", help_text,
                         "the help still prescribes a body source field; the source's one home "
                         "is the filename (inbox/README.md)")

    def test_readme_and_the_gate_agree_on_the_sources_one_home(self):
        """The audit's root finding: the source had two homes that disagreed, and the gate read
        the one nobody used. The README is the format's home, so it prescribes the filename form
        and names the reserved non-agent doors the gate honours."""
        readme = read_flat(os.path.join("inbox", "README.md"))
        self.assertIn("from-<agent>", readme,
                      "inbox/README.md prescribes no source form for an agent's deposit, so the "
                      "gate reads a format its own home never states (SPEC INV-189)")
        self.assertIn("from-owner", readme,
                      "inbox/README.md names no reserved door for the owner's own wish "
                      "(SPEC INV-193)")
        self.assertIn("relaying", readme.lower(),
                      "inbox/README.md does not say which name a relayed owner wish takes, and "
                      "an agent relaying his word is the live case (SPEC INV-193)")
        self.assertIn("stranger-", readme,
                      "inbox/README.md names no reserved door for a bridged Issue (SPEC INV-146)")
        self.assertIn("Re:", readme,
                      "inbox/README.md prescribes no reply form, which the gate exempts "
                      "(SPEC INV-192)")
        for birth in ("Blocked:", "Lived:"):
            self.assertIn(birth, readme,
                          "inbox/README.md prescribes no %s field, and the gate reads one; the "
                          "format's home and its gate name one format (SPEC INV-189)" % birth)
        gate = read(os.path.join("guardrails", "check-earned-message.py"))
        self.assertIn("from-", gate,
                      "the gate reads no filename source, which is the source's one home")


class TestReferralDirection(unittest.TestCase, _AnchorHomeMixin):
    """INV-190 (M-357) — a referral travels BACK to whoever asked; the zone's owner receives
    nothing from it."""

    def test_referral_travels_back_to_the_asker(self):
        spec = read_flat(SPEC)
        self.assertIn("A question from another agent's zone is referred, and a referral travels "
                      "back to whoever asked", spec)
        self.assertIn("The direction is the whole law", spec)
        self.assertIn("[INV-190]", spec)

    def test_zone_owner_receives_nothing_from_a_referral(self):
        spec = read_flat(SPEC)
        self.assertIn("The zone's owner receives nothing from a referral", spec)
        self.assertIn("Forwarding a neighbour's question to the owner of its zone is the defect "
                      "this law names", spec)
        self.assertIn("it carries the question to the human as its own question on no occasion",
                      spec)

    def test_base_rulebook_carries_the_referral_direction(self):
        self.assertIn("travels back to whoever asked", read_flat(BASE),
                      "the base rulebook does not carry the referral's direction")

    def test_inv190_index_and_ownership(self):
        self.assert_index_and_ownership("INV-190")


class TestHomelessQuestionDropped(unittest.TestCase, _AnchorHomeMixin):
    """INV-191 (M-358) — a question pinning to no artifact, on which no work of the sender's
    stands, is dropped, and the holding was itself the defect."""

    def test_homeless_question_is_dropped(self):
        spec = read_flat(SPEC)
        self.assertIn("A question that pins to no artifact, and on which no work of the sender's "
                      "stands, is dropped, and holding it was itself the defect", spec)
        self.assertIn("[INV-191]", spec)

    def test_the_holding_is_itself_the_finding(self):
        spec = read_flat(SPEC)
        self.assertIn("the finding is the question itself: the agent drops it, and the holding is "
                      "what the finding names", spec)
        self.assertIn("[INV-153]", spec)

    def test_inv191_index_and_ownership(self):
        self.assert_index_and_ownership("INV-191")


class TestProposalUntilRatified(unittest.TestCase, _AnchorHomeMixin):
    """INV-193 (M-359) — an agent-initiated message stands as a proposal until the owner ratifies
    it; relaying changes only the carrier."""

    def test_agent_message_is_a_proposal_until_ratified(self):
        spec = read_flat(SPEC)
        self.assertIn("An agent's message is a proposal until the owner ratifies it", spec)
        self.assertIn("An owner-initiated message is the one kind that carries the owner's "
                      "authority", spec)
        self.assertIn("[INV-193]", spec)

    def test_relaying_leaves_authority_where_it_started(self):
        spec = read_flat(SPEC)
        self.assertIn("relaying changes a message's carrier and leaves its authority exactly where "
                      "it started", spec)

    def test_base_rulebook_carries_the_ratification_law(self):
        self.assertIn("stays a proposal until the owner ratifies", read_flat(BASE),
                      "the base rulebook does not carry the ratification law")

    def test_inv193_index_and_ownership(self):
        self.assert_index_and_ownership("INV-193")


class TestNonDuplication(unittest.TestCase, _AnchorHomeMixin):
    """INV-194 (M-360) — a neighbour's capability is reached through one of the two channels; a
    local copy is the violation the roster exists to prevent."""

    def test_capability_taken_through_one_of_the_two_channels(self):
        spec = read_flat(SPEC)
        self.assertIn("A capability another agent's zone owns is taken through one of the two "
                      "channels", spec)
        self.assertIn("An agent needing such a capability sends a message or reads a contract",
                      spec)
        self.assertIn("[INV-194]", spec)

    def test_local_copy_is_the_violation_the_roster_prevents(self):
        spec = read_flat(SPEC)
        self.assertIn("A local copy of a neighbour's capability is the violation the roster exists "
                      "to prevent", spec)
        self.assertIn("the two owners then answer one question two ways", spec)

    def test_base_rulebook_carries_the_non_duplication_law(self):
        self.assertIn("a local copy of a neighbour's capability", read_flat(BASE),
                      "the base rulebook does not carry the non-duplication law")

    def test_inv194_index_and_ownership(self):
        self.assert_index_and_ownership("INV-194")


# --------------------------------------------------------------------------- #
# [node: spec-author]
# --------------------------------------------------------------------------- #

class TestContractIsASpecSurface(unittest.TestCase, _AnchorHomeMixin):
    """E-33 (M-361) — the contract is a spec surface in the producer's own spec, and its artifact
    carries its own version and generation stamp."""

    def test_contract_is_a_spec_surface(self):
        spec = read_flat(SPEC)
        self.assertIn("A contract is a spec surface in the producer's own spec", spec)
        self.assertIn("It is written, proven, and tested where the producer's other surfaces are",
                      spec)
        self.assertIn("[E-33]", spec)

    def test_artifact_carries_its_version_and_stamp(self):
        spec = read_flat(SPEC)
        self.assertIn("The published artifact is machine-readable, and it carries its own contract "
                      "version and its generation stamp", spec)
        self.assertIn("A reader tells the artifact's shape and its age from the artifact itself, "
                      "with no second document to consult", spec)

    def test_e33_index_and_ownership(self):
        self.assert_index_and_ownership("E-33")


class TestContractDefaultDeny(unittest.TestCase, _AnchorHomeMixin):
    """INV-185 (M-362) — a contract publishes nothing by default; a permission is an act with an
    author and a date; credentials never cross at all."""

    def test_contract_default_deny(self):
        """F-contract's named test (ARCHITECTURE.md feature coverage)."""
        spec = read_flat(SPEC)
        self.assertIn("A contract publishes nothing by default", spec)
        self.assertIn("Every field leaves the producer's tree on the owner's explicit permission",
                      spec)
        self.assertIn("A permission is an act with an author and a date", spec)
        self.assertIn("[INV-185]", spec)

    def test_construction_grants_no_permission(self):
        spec = read_flat(SPEC)
        self.assertIn("the way a system is built grants no permission, and a field with no "
                      "recorded permission stays home", spec)

    def test_credentials_never_cross_a_channel(self):
        spec = read_flat(SPEC)
        self.assertIn("Credentials never cross a channel at all, under any permission", spec)
        self.assertIn("the only road a producer's product data takes between two "
                      "agents", spec)

    def test_base_rulebook_carries_the_default_deny_law(self):
        self.assertIn("publishes nothing by default", read_flat(BASE),
                      "the base rulebook does not carry the contract's default-deny law")

    def test_inv185_index_and_ownership(self):
        self.assert_index_and_ownership("INV-185")


class TestProducerFormAndClock(unittest.TestCase, _AnchorHomeMixin):
    """INV-186 (M-363) — every field names its four things; the producer declares ONE number, its
    cadence, and a deploy never triggers the contract."""

    def test_every_contract_field_names_its_four_things(self):
        spec = read_flat(SPEC)
        for naming in ("what the field means", "the window it is measured over",
                       "how it is aggregated", "the source it derives from"):
            self.assertIn(naming, spec, "a contract field's naming is unstated: %r" % naming)
        self.assertIn("A field missing any of the four is an incomplete surface", spec)
        self.assertIn("[INV-186]", spec)

    def test_producer_declares_its_cadence_and_its_watcher(self):
        spec = read_flat(SPEC)
        self.assertIn("The producer declares the contract's cadence and regenerates on its own "
                      "clock", spec)
        self.assertIn("reds at its session-start sweep when its scheduled regeneration did not run",
                      spec)

    def test_a_deploy_never_triggers_the_contract(self):
        spec = read_flat(SPEC)
        self.assertIn("a deploy never triggers the contract", spec)
        self.assertIn("a contract triggered by it goes stale the day the building stops", spec)

    def test_inv186_index_and_ownership(self):
        self.assert_index_and_ownership("INV-186")


class TestConsumerRead(unittest.TestCase, _AnchorHomeMixin):
    """INV-187 (M-364) — the consumer declares ONE number, its staleness bound; it pins a version
    and reads read-only; the two numbers are set independently."""

    def test_consumer_declares_its_staleness_bound(self):
        spec = read_flat(SPEC)
        self.assertIn("The consumer declares its staleness bound, pins a version, and reads "
                      "read-only", spec)
        self.assertIn("the consumer's freshness check reds past that bound, before any analysis "
                      "runs", spec)
        self.assertIn("[INV-187]", spec)

    def test_consumer_pins_a_version_and_reads_read_only(self):
        spec = read_flat(SPEC)
        self.assertIn("It pins the contract version it was written against", spec)
        self.assertIn("It reads the artifact read-only", spec)
        self.assertIn("It carries a compatibility test that reds when its pinned version and the "
                      "artifact's version diverge", spec)
        self.assertIn("stale data is named aloud and the analysis stops there", spec)

    def test_cadence_and_bound_are_two_independent_numbers(self):
        spec = read_flat(SPEC)
        self.assertIn("The cadence and the staleness bound are two numbers, set independently, and "
                      "neither side reads the other's", spec)

    def test_inv187_index_and_ownership(self):
        self.assert_index_and_ownership("INV-187")


# --------------------------------------------------------------------------- #
# [node: host-contract]
# --------------------------------------------------------------------------- #

class TestRosterAndCard(unittest.TestCase, _AnchorHomeMixin):
    """E-32 (M-365) — the roster in the personal profile, the card in each agent's own tree, and
    the read that runs before the acting."""

    def test_roster_and_card_law(self):
        """F-roster's named test (ARCHITECTURE.md feature coverage)."""
        spec = read_flat(SPEC)
        self.assertIn("Each agent publishes a card describing itself, in its own tree, at "
                      "`.live-spec/agent.md`", spec)
        self.assertIn("The roster lives in the human's personal profile, one line per agent — a "
                      "name and a tree path", spec)
        self.assertIn("Who does what is a lookup", spec)
        self.assertIn("[E-32]", spec)

    def test_card_names_its_five_fields(self):
        spec = read_flat(SPEC)
        for field in ("the agent's name;", "its standing mission;", "the zones it owns;",
                      "the contracts it publishes, each with the path its artifact lives at;",
                      "its inbox address."):
            self.assertIn(field, spec, "the card's field is unstated: %r" % field)

    def test_the_read_runs_before_the_acting(self):
        spec = read_flat(SPEC)
        self.assertIn("An agent reads the roster and the relevant card before it acts on anything "
                      "that might not be its own", spec)
        self.assertIn("The read runs first, ahead of the acting", spec)

    def test_e32_index_and_ownership(self):
        self.assert_index_and_ownership("E-32")


class TestRosterLaw(unittest.TestCase, _AnchorHomeMixin):
    """INV-184 (M-366) — write-ownership is the roster/card split's reason; the roster row is the
    ratifying session's to write; the pack's own card is read from disk."""

    def test_pack_card_exists_and_names_its_five_fields(self):
        """The card arm, exercised against this pack's own real `.live-spec/agent.md` on disk."""
        path = os.path.join(ROOT, ".live-spec", "agent.md")
        self.assertTrue(os.path.isfile(path),
                        "this pack's own card is absent: .live-spec/agent.md (SPEC E-32, INV-184)")
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        low = " ".join(raw.split()).lower()
        for field in ("name", "mission", "zone", "contract", "inbox"):
            self.assertIn(field, low, "the card names no %s (SPEC E-32)" % field)

        # The contracts field names each contract WITH the path its artifact lives at, so the
        # claim is read against the CONTRACTS section alone — a path elsewhere on the card (the
        # inbox address, a pointer to a rulebook) says nothing about a published contract.
        sections = re.split(r"^##\s+", raw, flags=re.M)
        contracts = [s for s in sections if s.lower().startswith("contracts")]
        self.assertEqual(len(contracts), 1,
                         "the card carries no single contracts section (SPEC E-32)")
        body = contracts[0]
        declares_none = re.search(r"\bnone\b", body, re.I) is not None
        paths = re.findall(r"`[^`]*/[^`]*`", body)
        self.assertTrue(
            declares_none or paths,
            "the card's contracts section names neither a published contract with the path its "
            "artifact lives at, nor its emptiness (SPEC E-32)")
        if not declares_none:
            # Each named contract carries its path; a bare list of names is an incomplete card.
            self.assertTrue(paths, "a card naming a published contract owes its artifact's path "
                                   "(SPEC E-32)")

    def test_roster_row_written_by_the_ratifying_session(self):
        spec = read_flat(SPEC)
        self.assertIn("A roster row is written by the session holding the ratification "
                      "conversation", spec)
        self.assertIn("An agent writes its own roster row on no other occasion, and never "
                      "unbidden", spec)
        self.assertIn("each agent owns its own description the way it owns its own tree", spec)
        self.assertIn("[INV-184]", spec)

    def test_card_permission_is_the_birth_ratification(self):
        spec = read_flat(SPEC)
        self.assertIn("The card's permission is the birth ratification itself", spec)
        self.assertIn("Product data placed in a card is a contract field, and it takes the "
                      "contract's permission road whatever file it sits in", spec)

    def test_cardless_tree_is_flagged_beside_its_siblings(self):
        spec = read_flat(SPEC)
        self.assertIn("A tree with no card is flagged where its siblings are flagged", spec)
        self.assertIn("a host tree carrying no `.live-spec/agent.md` is named there as an "
                      "incomplete record", spec)

    def test_inv184_index_and_ownership(self):
        self.assert_index_and_ownership("INV-184")


# --------------------------------------------------------------------------- #
# [node: inbox]
# --------------------------------------------------------------------------- #

class TestMessageLifecycle(unittest.TestCase, _AnchorHomeMixin):
    """INV-192 (M-367) — the stable identifier, the reply riding the sender's own inbox, and the
    terminal state every message reaches."""

    def test_message_carries_a_stable_identifier(self):
        spec = read_flat(SPEC)
        self.assertIn("A message carries a stable identifier its reply can name", spec)
        self.assertIn("The identifier is minted per message", spec)
        self.assertIn("[INV-192]", spec)

    def test_reply_travels_the_senders_own_inbox(self):
        spec = read_flat(SPEC)
        self.assertIn("A reply travels the sender's own inbox, and it inherits its passage from "
                      "the message it answers", spec)
        self.assertIn("it keeps the channel count at two", spec)

    def test_reply_owes_no_blocked_work_of_its_own(self):
        spec = read_flat(SPEC)
        self.assertIn("A reply owes no blocked work of its own", spec)
        self.assertIn("the message it discharges already named the blocked work that earned the "
                      "exchange", spec)

    def test_every_message_reaches_a_terminal_state(self):
        spec = read_flat(SPEC)
        self.assertIn("Every message states its need-by and reaches a terminal state", spec)
        self.assertIn("A message ends delivered, declined, or escalated past its stated need-by",
                      spec)
        self.assertIn("An escalated message surfaces in the sender's own status report as blocked "
                      "work aged past its stated need-by", spec)

    def test_no_agent_wakes_a_dormant_window(self):
        spec = read_flat(SPEC)
        self.assertIn("An agent wakes a dormant window on no occasion", spec)

    def test_inv192_index_and_ownership(self):
        self.assert_index_and_ownership("INV-192")


# --------------------------------------------------------------------------- #
# [node: build-pipeline]
# --------------------------------------------------------------------------- #

class TestAgentBirth(unittest.TestCase, _AnchorHomeMixin):
    """T-22 (M-368) — the proposal, the owner's ratification, the contract that outlives the
    migration, and the grain the owner's word settles."""

    def test_agent_birth_walk(self):
        """F-agent-birth's named test (ARCHITECTURE.md feature coverage)."""
        spec = read_flat(SPEC)
        self.assertIn("A capability no agent's zone owns, or one that has outgrown its host, lets "
                      "any agent propose a new agent", spec)
        self.assertIn("The proposal names the capability, the zone the new agent would own, and "
                      "the contracts it would publish", spec)
        self.assertIn("[T-22]", spec)

    def test_ratification_creates_the_agent_and_the_row_records_it(self):
        spec = read_flat(SPEC)
        self.assertIn("It stands as a proposal until the owner ratifies the birth", spec)
        self.assertIn("The owner's ratification is the act that seats the agent, and the roster "
                      "row is that seat's record", spec)
        # The properties constitute agent-hood; the ratification seats it (prover F2). An unseated
        # agent is real and unlisted, which is every tree that predates the roster.
        self.assertIn("a tree carrying all three is an agent whether or not a row names it yet", spec)

    def test_contract_outlives_the_migration(self):
        spec = read_flat(SPEC)
        self.assertIn("The contract outlives the migration", spec)
        self.assertIn("the consumer keeps reading its pinned version until it chooses to move",
                      spec)
        self.assertIn("A migration that breaks a consumer's pin has broken the contract rather "
                      "than moved it", spec)

    def test_grain_is_the_owners_call_recorded_with_its_date(self):
        spec = read_flat(SPEC)
        self.assertIn("The grain of a capability — a skill or an agent — is the owner's call, "
                      "recorded in the roster with its date", spec)
        self.assertIn("That weighing is taste, which is the human-only fact this deferral names",
                      spec)

    def test_t22_index_and_ownership(self):
        self.assert_index_and_ownership("T-22")


# --------------------------------------------------------------------------- #
# [node: base-rulebook] — recognition, the exchange bound, the default owner
# --------------------------------------------------------------------------- #

class TestRecogniseAndRoute(unittest.TestCase, _AnchorHomeMixin):
    """INV-195 — an agent recognises a neighbour's zone on its own; the owner's word afterwards
    is an acknowledgement of a thing already done."""

    def test_agent_recognises_a_neighbours_zone_itself(self):
        clause = self.assert_declared("INV-195")
        self.assertIn("reads the roster", clause)
        self.assertIn("carries no fact the agent lacked", clause)
        self.assertIn("made the owner its router", clause)

    def test_the_base_rulebook_carries_the_recognition_duty(self):
        base = read_flat(BASE)
        self.assertIn("recognises a neighbour's zone on its own", base)
        self.assertIn("has made the owner its router", base)

    def test_inv195_index_and_ownership(self):
        self.assert_index_and_ownership("INV-195")


class TestExchangeBound(unittest.TestCase, _AnchorHomeMixin):
    """INV-196 — one question crosses between two agents twice; the third crossing goes to the
    owner. Every hop of a refer-and-re-send loop passes its own law, so the exchange needs its
    own bound."""

    def test_one_question_crosses_twice_then_goes_to_the_owner(self):
        clause = self.assert_declared("INV-196")
        self.assertIn("The bound is two", clause)
        self.assertIn("third crossing goes to the owner", clause)
        self.assertIn("reopen it by rewording", clause)

    def test_the_bound_cites_the_kin_it_copies(self):
        """The human-decision withdrawal loop already carries this shape [INV-130]; the bound is
        that pattern applied to a channel rather than a fresh invention."""
        self.assertIn("INV-130", self.assert_declared("INV-196"))

    def test_inv196_index_and_ownership(self):
        self.assert_index_and_ownership("INV-196")


class TestDefaultOwner(unittest.TestCase, _AnchorHomeMixin):
    """INV-197 — a concern no agent's zone owns goes to the pack, and the work never stalls on
    ownership (the owner's word through the promoter's inbox deposit, 2026-07-17)."""

    def test_an_unowned_concern_goes_to_the_pack(self):
        clause = self.assert_declared("INV-197")
        self.assertIn("the pack stands as the default owner", clause)
        self.assertIn("owning zone does not exist yet", clause)
        self.assertIn("INV-191", clause)

    def test_work_never_stalls_on_ownership(self):
        clause = self.assert_declared("INV-197")
        self.assertIn("does the reasonable thing now", clause)
        self.assertIn("marks that work provisional", clause)
        self.assertIn("a stall while ownership is settled", clause)

    def test_zones_may_overlap(self):
        """His word, recorded against the queued uniqueness row it refuted the same day."""
        self.assertIn("Zones may overlap", self.assert_declared("INV-197"))

    def test_inv197_index_and_ownership(self):
        self.assert_index_and_ownership("INV-197")


if __name__ == "__main__":
    unittest.main()
