# -*- coding: utf-8 -*-
"""The answer-first arm reds a lead-less wall and passes a genuine lead (ROADMAP row 397, SPEC INV-220).

The answer-first law (the personal profile's `language.answer-first`, PERMANENT) is stated and the chat-law
hook reminds, but a stated law with no machine is a wish (live-spec base rule 30). This arm is the machine:
a Stop-hook NOTICE that reds a MEASURABLE PROXY of the fault — a chat reply over a length floor whose
opening block is a wall carrying no short lead.

This module holds the arm to the scissors overlay's own rigor (SPEC INV-173): every method-first WALL
fires, and not one genuine lead-first reply is falsely flagged. The fixtures beside it carry eight walls
(the fault's shape: a reply that opens with its method and buries the finding) and thirteen lead-first
replies plus three short replies (a reply that opens with its answer, two of them long enough to prove the
discriminator is the opening SHAPE, never the total length).

Red-first: before hooks/answer-first-scan.py exists, this module fails to import — that is the red.
"""
import importlib.util
import glob
import json
import os
import subprocess

from conftest import ROOT

HOOKS = os.path.join(ROOT, "hooks")
FIXTURES = os.path.join(ROOT, "tests", "answer_first_fixtures")
SCRIPT = os.path.join(HOOKS, "answer-first-scan.py")


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


afs = _load(SCRIPT, "answer_first_scan")


def _fixtures(prefix):
    return sorted(glob.glob(os.path.join(FIXTURES, prefix + "*.txt")))


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


# ---- The measurable proxy: walls fire, leads and shorts pass -----------------------------------------

def test_every_wall_fires():
    """Every method-first wall — a reply opening with its method, the finding buried — reds (has_lead False)."""
    walls = _fixtures("wall_")
    assert len(walls) >= 8, "the red-proof needs the scissors overlay's rigor: at least eight walls"
    caught = [p for p in walls if not afs.has_lead(_read(p))]
    missed = [os.path.basename(p) for p in walls if afs.has_lead(_read(p))]
    assert not missed, "these walls opened with a wall yet were not flagged: %s" % missed
    assert len(caught) == len(walls)


def test_no_lead_first_reply_is_falsely_flagged():
    """Not one genuine lead-first reply reds — the false-positive bar the scissors overlay met (0 of N)."""
    leads = _fixtures("lead_")
    assert len(leads) >= 10, "need a real run of lead-first replies to check false positives against"
    falsely = [os.path.basename(p) for p in leads if not afs.has_lead(_read(p))]
    assert not falsely, "these lead-first replies were falsely flagged: %s" % falsely


def test_short_replies_owe_no_lead():
    """A reply under the length floor owes no engineered lead and never fires."""
    shorts = _fixtures("short_")
    assert shorts
    falsely = [os.path.basename(p) for p in shorts if not afs.has_lead(_read(p))]
    assert not falsely, "short replies must never fire: %s" % falsely


def test_discriminator_is_shape_not_length():
    """A LONG lead-first reply (well over the length floor) still passes — proving the arm reads the opening
    shape, not the total length; a short-lead 900-char reply must not fire."""
    long_leads = [p for p in _fixtures("lead_") if len(afs._strip_timestamp(_read(p)).strip()) > 700]
    assert long_leads, "the proof needs at least one long lead-first reply over the length floor"
    for p in long_leads:
        assert afs.has_lead(_read(p)), "a long reply that leads with its answer must not fire: %s" % p


# ---- The three lead signals, each exercised directly -------------------------------------------------

def test_short_opening_sentence_is_a_lead():
    body = "The vendor is cheaper by 18%. " + "Detail sentence that runs on. " * 30
    assert afs.has_lead(body)


def test_structural_opening_is_a_lead():
    body = ("- the setting writes through the store\n"
            "- the empty state is specified on all three surfaces\n"
            "- the hero image is compressed\n\n") + "Prose detail underneath. " * 30
    assert afs.has_lead(body)


def test_long_first_sentence_with_no_break_fires():
    """A single long opening sentence of method, no early stop and no structure, over the floor, fires."""
    body = ("I began by scoping the question against the sources you named and then ran a wide fan-out of "
            "searches across every one of them and cross-checked each candidate claim against at least two "
            "independent references and discarded the ones that traced back to a single blog restating a "
            "press release and read the primary filings in full and pulled all of the numbers into a large "
            "table and normalized the currencies to a common base and re-ran the entire comparison twice "
            "under both a nominal and an inflation-adjusted view before I would trust the ordering enough "
            "to say anything at all about which of the two options actually comes out cheaper for you")
    assert len(body) >= afs.LENGTH_THRESHOLD
    assert not afs.has_lead(body)


# ---- End to end on the Stop event -------------------------------------------------------------------

def _transcript(tmp_path, msgs):
    p = tmp_path / "t.jsonl"
    with open(p, "w", encoding="utf-8") as f:
        for role, txt in msgs:
            if role == "user":
                rec = {"type": "user", "message": {"role": "user", "content": txt}}
            else:
                rec = {"type": "assistant",
                       "message": {"role": "assistant", "id": "m%d" % id(txt),
                                   "content": [{"type": "text", "text": txt}]}}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return str(p)


def _run(payload):
    return subprocess.run(["python3", SCRIPT], input=json.dumps(payload),
                          capture_output=True, text=True)


def test_stop_hook_blocks_on_a_wall(tmp_path):
    wall = _read(os.path.join(FIXTURES, "wall_research_digest.txt"))
    tp = _transcript(tmp_path, [("user", "go"), ("assistant", "One moment."), ("assistant", wall)])
    r = _run({"transcript_path": tp, "hook_event_name": "Stop", "stop_hook_active": False})
    assert r.returncode == 0
    decision = json.loads(r.stdout)
    assert decision["decision"] == "block"
    assert decision["suppressOutput"] is True
    assert "ANSWER-FIRST" in decision["reason"]


def test_stop_hook_is_silent_on_a_lead(tmp_path):
    lead = _read(os.path.join(FIXTURES, "lead_short_answer.txt"))
    tp = _transcript(tmp_path, [("user", "go"), ("assistant", lead)])
    r = _run({"transcript_path": tp, "hook_event_name": "Stop", "stop_hook_active": False})
    assert r.returncode == 0 and r.stdout.strip() == ""


def test_stop_hook_active_stands_down(tmp_path):
    """Never loop: a prior stop-hook already fired this turn stands the arm down."""
    wall = _read(os.path.join(FIXTURES, "wall_research_digest.txt"))
    tp = _transcript(tmp_path, [("user", "go"), ("assistant", wall)])
    r = _run({"transcript_path": tp, "hook_event_name": "Stop", "stop_hook_active": True})
    assert r.stdout.strip() == ""


def test_reads_the_last_message_not_the_narration(tmp_path):
    """The arm judges the FINAL reply the human reads, not the short inter-tool narration lines."""
    wall = _read(os.path.join(FIXTURES, "wall_research_digest.txt"))
    # a wall appears as an EARLY narration line, but the final reply is a clean short lead -> no fire.
    tp = _transcript(tmp_path, [("user", "go"), ("assistant", wall),
                                ("assistant", "Done — the answer is 18% cheaper, details above.")])
    r = _run({"transcript_path": tp, "hook_event_name": "Stop", "stop_hook_active": False})
    assert r.stdout.strip() == "", "only the final reply owes a lead; a short final reply passes"


# ---- Honesty: the arm names what it cannot see, and it is a notice, never a pre-push gate ------------

def test_honest_boundary_is_stated_in_the_source():
    src = _read(SCRIPT)
    low = src.lower()
    assert "never whether the lead is the right answer" in low or "not whether the lead is the right" in low
    assert "notice" in low and "pre-push gate" in low


def test_pack_installer_ships_and_wires_the_arm():
    """SPEC INV-173: a universal pack hook lives as source in hooks/ and installs via the setup walk."""
    src = _read(os.path.join(ROOT, "scripts", "install-pack-hooks.sh"))
    assert "answer-first-scan.py" in src
    assert 'wire("Stop", "answer-first-scan.py"' in src


def test_reason_admits_a_possible_misread():
    """The block message tells the model the net may misread the shape, so a real lead-first reply is not
    argued with — it says so in one line and continues."""
    src = _read(SCRIPT)
    assert "misread" in src.lower() or "if the reply already led" in src.lower()


# ---- Traceability: the law stands in every document it is owed in (SPEC INV-220) --------------------

def test_spec_states_the_law():
    spec = _read(os.path.join(ROOT, "PRODUCT_SPEC.md"))
    assert "The answer-first arm reds a lead-less wall" in spec
    assert "[INV-220]" in spec


def test_formal_index_row():
    spec = _read(os.path.join(ROOT, "PRODUCT_SPEC.md"))
    assert "| INV-220 |" in spec
    assert "The answer-first arm reds a lead-less wall" in spec


def test_architecture_owns_the_invariant():
    arch = _read(os.path.join(ROOT, "ARCHITECTURE.md"))
    assert "INV-220 (the answer-first arm:" in arch
    assert "hooks/answer-first-scan.py:1" in arch


def test_matrix_row_covers_the_law():
    mat = _read(os.path.join(ROOT, "TEST_MATRIX.md"))
    assert "| M-401 |" in mat and "INV-220" in mat
