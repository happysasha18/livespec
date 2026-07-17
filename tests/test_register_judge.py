# -*- coding: utf-8 -*-
"""The register judge holds the class a literal list cannot (ROADMAP rows 416+418, SPEC INV-203).

A register law that names a CLASS is held by a model that reads meaning; a list of literal patterns holds
only the instances someone thought of. This module red-proves both surfaces of that law:

  - CHAT (416): four empty intensifiers pass the literal scissors list untouched, and the judge reds them.
    A flat informative sentence passes both. A turn holding many messages is gathered whole, so an offence
    in an early inter-tool message reds — the PLACE fix as well as the KIND fix.
  - DOCUMENT (418): a Russian fixture carrying pack coinages as calques passes the literal preshow list,
    and the judge reds it.

The judge makes a live model call, so nothing here depends on a live `claude` binary. The mechanism's
PARSE / VALIDATE / DECISION logic is driven against canned model responses; the stand-down is driven by
faking a missing binary; the literal-list passes are real and deterministic.

Red-first: before hooks/register_judge_core.py exists, this module fails to import — that is the red.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOKS = os.path.join(REPO, "hooks")
SCRIPTS = os.path.join(REPO, "scripts")


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sys.path.insert(0, HOOKS)
core = _load(os.path.join(HOOKS, "register_judge_core.py"), "register_judge_core")
judge_hook = _load(os.path.join(HOOKS, "register-judge.py"), "register_judge_hook")
lint = _load(os.path.join(SCRIPTS, "preshow-register-lint.py"), "preshow_register_lint")
scissors = _load(os.path.join(HOOKS, "scissors-scan.py"), "scissors_scan")


# The full literal list the row names: the universal scissors frame (shipped, in scissors-scan) plus the
# 22-pattern personal overlay the row counted. Embedded here so the "passes the list" proof is exact and
# self-contained, never dependent on a machine's ~/.claude overlay.
SCISSORS_PERSONAL = [
    r",\s+а\s+не\s+\S", r",\s+но\s+не\s+\S", r"\s+—\s+не\s+\S",
    r"сам(ое|ая|ый)\s+(главн|важн|интересн|сильн)",
    r"(красив|лучш|хуж|интересн|проще|сложнее)\w*,?\s+чем\s+(я\s+)?(рассчитыва|ожида|дума|надея)",
    r"\bв\s+корне\b", r"меняет\s+(всё|все|дело)", r"\bв\s+чистом\s+виде\b", r"\bпереворачивает\b",
    r"бьёт\s+мимо", r"\bсильно\s+(лучше|хуже|важнее|проще)", r"хорошая\s+новость",
    r"\b(катастрофа|провал|ужас)\b", r"\bполностью\s+(сломан|разрушен|провал)",
    r"\b(точно|верно|метко|хорошо)\s+(подметил|поймал|заметил|сказал)",
    r"\b(поймал|уловил)\s+(верно|точно|главное|суть)", r"^\s*(ты\s+)?прав[,.]",
    r"\bсправедлив(о|ы)\b", r"\bхороший\s+вопрос",
    r"\b(отличн|прекрасн|замечательн)\w*\s+(вопрос|мысль|замечание|наблюдение)",
    r"\bты\s+(поймал|назвал)\s+(настоящ|главн|сам)", r"\bи\s+это\s+справедлив",
]


def _full_literal_list():
    return [re.compile(p) for p in scissors.PATTERNS] + [re.compile(p) for p in SCISSORS_PERSONAL]


def _literal_hits(text):
    return scissors.find_hits(text, _full_literal_list())


# The four phrases the row probed — empty intensifiers that carry no fact.
FOUR_INTENSIFIERS = ["по-настоящему", "реально", "на самом деле", "действительно"]


# ---- KIND (416): the four intensifiers pass the list, red under the judge --------------------------

@pytest.mark.parametrize("phrase", FOUR_INTENSIFIERS)
def test_intensifier_passes_the_literal_list(phrase):
    """Each probed intensifier walks the full 22+-pattern literal list untouched — the list's own gap."""
    sentence = "Это %s важный шаг для проекта, и мы его сделали." % phrase
    assert _literal_hits(sentence) == [], "the literal list should NOT catch %r" % phrase


@pytest.mark.parametrize("phrase", FOUR_INTENSIFIERS)
def test_intensifier_reds_under_the_judge(phrase):
    """The judge, handed the model's verdict, reds each intensifier the list let through."""
    sentence = "Это %s важный шаг для проекта, и мы его сделали." % phrase
    canned = json.dumps({"offences": [{"quote": sentence, "law": 2, "why": "intensifier, no fact"}]})
    offences, error = core.parse_offences(canned, sentence)
    assert error is None
    assert len(offences) == 1 and offences[0]["quote"] == sentence


def test_flat_informative_sentence_passes_both():
    """A plain sentence carrying a fact passes the literal list and draws an empty verdict from the judge."""
    sentence = "Suite is 921 tests green and the three judge arms are wired in settings.json."
    assert _literal_hits(sentence) == []
    offences, error = core.parse_offences('{"offences": []}', sentence)
    assert error is None and offences == []


# ---- PLACE (416): a turn holding many messages reds on the one that offends -------------------------

def _transcript(tmp_path, messages):
    """messages: list of (role, text). Writes a JSONL transcript and returns its path."""
    p = tmp_path / "transcript.jsonl"
    with open(p, "w", encoding="utf-8") as f:
        for role, text in messages:
            if role == "user":
                rec = {"type": "user", "message": {"role": "user", "content": text}}
            else:
                rec = {"type": "assistant",
                       "message": {"role": "assistant", "id": "m%d" % id(text),
                                   "content": [{"type": "text", "text": text}]}}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return str(p)


def test_turn_gathers_every_message_not_only_the_last(tmp_path):
    """The offence sits in an EARLY inter-tool message; the last message is clean. turn_text must still
    hold the offending line, so the judge sees it — proving PLACE, not only KIND."""
    offending = "Это по-настоящему меняет ход работы над задачей."
    path = _transcript(tmp_path, [
        ("user", "поехали"),
        ("assistant", offending),                    # early, between tool calls
        ("assistant", "Промежуточный шаг выполнен."),
        ("assistant", "Готово, тесты зелёные."),      # the LAST message is clean
    ])
    gathered = judge_hook.turn_text(path)
    assert offending in gathered, "the whole turn must be gathered, not the last message alone"
    # the old last-message-only read would have missed it:
    assert "Готово, тесты зелёные." in gathered


def test_turn_scopes_to_the_current_turn(tmp_path):
    """Only assistant text AFTER the last human message is this turn's output."""
    path = _transcript(tmp_path, [
        ("user", "first"),
        ("assistant", "prior turn reply that should be out of scope"),
        ("user", "second"),
        ("assistant", "this turn's reply"),
    ])
    gathered = judge_hook.turn_text(path)
    assert "this turn's reply" in gathered
    assert "prior turn" not in gathered


# ---- The mechanism: parse / validate / stand-down ---------------------------------------------------

def test_hallucinated_quote_is_dropped():
    """A quote the model invents that is not verbatim in the text is no evidence."""
    offences, error = core.parse_offences(
        '{"offences":[{"quote":"a line never written","law":1,"why":"x"}]}', "the real text")
    assert error is None and offences == []


def test_unreadable_shape_stands_down():
    offences, error = core.parse_offences("I could not comply", "the real text")
    assert offences == [] and error is not None


def test_code_fence_is_stripped():
    offences, error = core.parse_offences('```json\n{"offences": []}\n```', "the real text")
    assert error is None and offences == []


def test_judge_stands_down_when_no_binary(monkeypatch):
    """No claude on PATH stands the judge down with an error, never a block on its own breakage."""
    def _boom(*a, **k):
        raise FileNotFoundError("no claude")
    monkeypatch.setattr(core.subprocess, "run", _boom)
    offences, error = core.judge("some text here", core.UNIVERSAL_CHAT_LAW)
    assert offences == [] and "no claude binary" in error


def test_judge_stands_down_on_nonzero_exit(monkeypatch):
    def _fail(*a, **k):
        return subprocess.CompletedProcess(a, 1, stdout="", stderr="boom")
    monkeypatch.setattr(core.subprocess, "run", _fail)
    offences, error = core.judge("some text here", core.UNIVERSAL_CHAT_LAW)
    assert offences == [] and error is not None


# ---- The universal/personal law split (SPEC INV-173) -----------------------------------------------

def test_universal_chat_law_ships_and_names_the_scissors_frame():
    assert "not Y" in core.UNIVERSAL_CHAT_LAW or "а не" in core.UNIVERSAL_CHAT_LAW


def test_personal_law_overlay_rides_the_personal_layer(tmp_path):
    """The personal laws (empty intensifier, grading the person) load from an overlay the personal layer
    owns; a missing overlay falls back to universal-only, silently."""
    assert core.load_personal_law(path=str(tmp_path / "absent.md")) == ""
    overlay = tmp_path / "register-judge-personal.md"
    overlay.write_text("LAW 2 — no empty intensifier.\nLAW 3 — no grading the person.", encoding="utf-8")
    body = core.load_personal_law(path=str(overlay))
    assert "empty intensifier" in body and "grading the person" in body


def test_chat_law_composes_universal_plus_personal(monkeypatch, tmp_path):
    overlay = tmp_path / "register-judge-personal.md"
    overlay.write_text("LAW 2 — no empty intensifier.", encoding="utf-8")
    monkeypatch.setattr(core.os.path, "expanduser", lambda p: str(overlay)
                        if "register-judge-personal" in p else os.path.expanduser(p))
    law = judge_hook.chat_law()
    assert "not Y" in law or "а не" in law          # universal present
    assert "empty intensifier" in law               # personal appended


# ---- DOCUMENT (418): the Russian calque fixture passes the list, reds under the judge ---------------

# A calque of pack coinages ("wish door", "pipeline stations") — a machine-dialect leak the literal list
# never listed in Russian. The audit's worked instance.
RU_CALQUE_FIXTURE = "Брось пожелание в дверь желаний, и оно само пройдёт конвейер по станциям."


def test_document_calque_passes_the_literal_list():
    """The fixture carries the pack's coinages as Russian calques; the literal preshow list misses it."""
    assert lint.scan(RU_CALQUE_FIXTURE) == [], "the literal list should NOT catch the calque fixture"


def test_document_calque_reds_under_the_judge():
    canned = json.dumps({"offences": [
        {"quote": RU_CALQUE_FIXTURE, "law": 1, "why": "calque of an internal coinage"}]})
    offences, error = core.parse_offences(canned, RU_CALQUE_FIXTURE)
    assert error is None and len(offences) == 1


def test_document_judge_is_opt_in_and_stands_down(monkeypatch):
    """Off by default so the suite and push gate stay deterministic; on, it stands down on breakage."""
    monkeypatch.delenv("PRESHOW_REGISTER_JUDGE", raising=False)
    assert lint.judge_document(RU_CALQUE_FIXTURE) == []      # disabled -> empty
    monkeypatch.setenv("PRESHOW_REGISTER_JUDGE", "1")
    monkeypatch.setattr(core.subprocess, "run",
                        lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError()))
    # even enabled, a missing binary stands it down without raising
    assert lint.judge_document(RU_CALQUE_FIXTURE) == []


def test_document_law_ships():
    assert "calque" in core.DOCUMENT_REGISTER_LAW and "reader" in core.DOCUMENT_REGISTER_LAW


# ---- The growth duty is RETRACTED (418) ------------------------------------------------------------

def test_growth_duty_retracted_in_the_lint_docstring():
    src = open(os.path.join(SCRIPTS, "preshow-register-lint.py"), encoding="utf-8").read()
    assert "GROWS BY ONE per caught leak" not in src
    assert "grows by NOBODY's duty" in src or "grows by nobody's duty" in src.lower()


def test_growth_duty_retracted_in_the_spec():
    spec = open(os.path.join(REPO, "PRODUCT_SPEC.md"), encoding="utf-8").read()
    # INV-83's paragraph no longer commands the list to grow per leak.
    assert "The set grows by one per caught leak" not in spec
    assert "grows by nobody" in spec.lower()


# ---- Wiring: the pack installer ships the judge (SPEC INV-173) --------------------------------------

def test_pack_installer_wires_the_judge_arms():
    src = open(os.path.join(SCRIPTS, "install-pack-hooks.sh"), encoding="utf-8").read()
    assert "register-judge-collect.sh" in src
    assert "register-judge-report.sh" in src
    assert "register_judge_core.py" in src
