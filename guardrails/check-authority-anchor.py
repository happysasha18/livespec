#!/usr/bin/env python3
"""check-authority-anchor.py — the machine that holds the writing rule on HUMAN AUTHORITY
(SPEC INV-207, ROADMAP row 415).

THE LAW it enforces. Every claim in this pack stands on an artifact a reader can go and check. A
human's word is the one input with no artifact behind it, and therefore the one claim no agent,
prover, or gate questions. So a sentence that records a decision, word, or ruling AS the person's must
name the EXCHANGE it came from — at minimum a date a reader can go to and check. A sentence the pack
reasoned out for itself is written in the pack's own voice; it claims no human authority, is
challengeable by every reader, and is not this gate's business. An autonomy grant authorizes an agent
to DECIDE; it never authorizes recording that decision AS the human's.

WHAT IT READS — the DECISION set, not the prose's meaning. The gate is structural. It has one home it
ENFORCES and one act it serves:

  * The DECISION-SET RECORD (the enforced, push-wired scan). A file that declares itself a decision
    record with a `DECISION-RECORD` marker line (the touchpoint-kind gate's self-declaration shape)
    holds, by construction, nothing but decisions recorded as the person's. Every live on-record entry
    there must carry its exchange anchor (a date); a struck entry is skipped, since the person has
    already reached in and struck it. This surface is free of the rule-language noise below, so the
    anchor rule is unambiguous and false-positive-free — which is why it, not free prose, is the
    standing scan.
  * The FIRST-SWEEP act (arg mode, this row's first act). Given files as arguments, the gate reports
    every authority-claim SENTENCE that names no date, so a human can sweep the spec, the base
    rulebook, and the active roadmap once and resolve each. Free prose mixes two things the gate cannot
    fully tell apart — a genuine dated attribution (passes) and the pack's own RULE language, which
    references "the human's word" as a policy category and rightly needs no anchor (it is the law's
    own challengeable side). The gate exempts the abstract-role forms ("the human", "the person", "the
    reader", "one") that are always rule language, and reports the rest for the sweeper to triage: give
    a genuine unanchored attribution its exchange, or rewrite it in the pack's voice. This is a
    one-time diagnostic, not a standing gate over churny prose (the archive is spared, as the other
    guards spare it).

An authority-claim is (patterns in authority-anchor.json, so this code names no person):
  * a possessive authority-noun with a DEFINITE possessor — "his word", "the owner's ruling", "her
    call", a named person's ranking (prepositional forms like "on his OK" / "per his word" are this case);
  * a verb of authority with a DEFINITE personal subject — "he decided", "the owner ordered", a named
    person chose.
The abstract-role possessors ("the human's", "the person's", "the reader's", "a human", "one") are
NOT authority-claims: they are the pack stating a rule in its own voice. The person names are a
per-host roster (data); the definite role forms ("his", "the owner's", "he decided") are
person-agnostic, so the law is stated for ANY person and ANY host.

THE ANCHOR. A claim passes when its sentence carries a date token (YYYY-MM-DD). A bare time (~15:37)
alone is not enough — the exchange's WHEN is a day. The profile's own style is the target shape:
"<person> 2026-07-03, standing" / "<person> 2026-07-14, on the passivity finding: ...". The person
names live in the config data, never in this code, so the detector names no person.

Usage:
  check-authority-anchor.py                 push mode: scan every tracked DECISION-RECORD surface.
  check-authority-anchor.py [--config F] FILE ...
                                            sweep/fixture mode: report each file's unanchored
                                            authority claims (a DECISION-RECORD file uses the strict
                                            per-entry rule; free prose uses the sentence rule).
Exit 0 = no unanchored authority-claim. Exit 1 = at least one.
"""
import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys

DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
STRUCK = re.compile(r"(?i)(~~.*~~|\bSTRUCK\b)")
# The marker declares a file a decision record only as a STANDALONE line (the TOUCHPOINT-KIND shape),
# so a doc that merely MENTIONS `DECISION-RECORD` inline (the spec, the matrix, this gate) is not one.
RECORD_MARKER = re.compile(r"(?m)^\s*DECISION-RECORD\s*$")
ON_REGION = re.compile(r"<!--\s*record:on\s*-->")
OTHER_REGION = re.compile(r"<!--\s*record:(struck|note)\s*-->")
BULLET = re.compile(r"^\s*[-*]\s+\S")

# The standing push scan reaches only DECLARED DECISION-RECORD surfaces, and spares the fixture homes
# (which carry DECISION-RECORD markers to be exercised, one of them deliberately unanchored) and the
# archive/diaries, exactly as check-shipped-language and check-freeze spare them.
TEXT_EXT = (".md", ".txt")
SENT_SPLIT = re.compile(r"(?<=[.;:])\s+")
SPARED_DIRS = ("guardrails/authority-anchor-fixtures/", "docs/", "attic/", "inbox/",
               ".live-spec/", "tests/", "evals/", "prototype/")
SPARED_FILES = ("JOURNAL.md", "NEXT_STEPS.md", "MIGRATION.md", "ROADMAP.md")


def is_spared(rel):
    if any(rel == f or rel.endswith("/" + f) for f in SPARED_FILES):
        return True
    return any(rel.startswith(d) for d in SPARED_DIRS)


def load_config(path):
    if path and os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def compile_claim(cfg):
    """The authority-claim matcher from the declared roster and role forms, kept as data so the gate
    names no person. DEFINITE possessors/subjects only — the abstract-role forms are rule language."""
    names = cfg.get("person_names") or []
    nouns = cfg.get("authority_nouns") or []
    verbs = cfg.get("authority_verbs") or []
    if not (nouns or verbs):
        return None
    name_alt = "|".join(re.escape(n) for n in names)
    # \b anchors the possessor so "her" does not match inside "whether"/"other"/"gather".
    poss = r"\b(?:his|her|their|the owner's"
    if name_alt:
        poss += r"|(?:%s)'s" % name_alt
    poss += r")"
    subj = r"\b(?:he|she|they|the owner"
    if name_alt:
        subj += r"|%s" % name_alt
    subj += r")"
    noun_alt = "|".join(re.escape(n) for n in nouns)
    verb_alt = "|".join(re.escape(v) for v in verbs)
    pats = []
    if noun_alt:
        # one or two tokens may sit between the possessor and the noun: "his 2026-07-06 word",
        # "his own considered ranking".
        pats.append(r"%s\s+(?:\S+\s+){0,2}(?:%s)\b" % (poss, noun_alt))
    if verb_alt:
        pats.append(r"\b%s\s+(?:%s)\b" % (subj, verb_alt))
    return re.compile("(?:%s)" % "|".join(pats), re.IGNORECASE)


def waived(rel, snippet, waivers):
    for w in waivers or []:
        if fnmatch.fnmatch(rel, w.get("file", "")) and w.get("snippet", "") in snippet:
            return True
    return False


def is_record(text):
    return bool(RECORD_MARKER.search(text))


def scan_record(path, rel, claim_re, waivers):
    """A declared DECISION-RECORD surface: every live on-record bullet must carry a date anchor. An
    entry is on-record inside a `<!-- record:on -->` region (or, absent regions, any bullet); a struck
    or ~~struck~~ entry is skipped; a bullet outside the on-record region (a struck/note region) is
    skipped. This is the strict, false-positive-free rule the standing gate rests on."""
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except (UnicodeDecodeError, OSError):
        return
    region_seen = any(ON_REGION.search(l) or OTHER_REGION.search(l) for l in lines)
    in_on = not region_seen  # no regions declared → every bullet is on-record
    for i, raw in enumerate(lines, 1):
        if ON_REGION.search(raw):
            in_on = True
            continue
        if OTHER_REGION.search(raw):
            in_on = False
            continue
        if not in_on or not BULLET.match(raw):
            continue
        if STRUCK.search(raw):
            continue
        if DATE.search(raw):
            continue
        snip = raw.strip()[:120]
        if waived(rel, snip, waivers):
            continue
        yield (i, snip, "on-record decision entry names no date")


def scan_prose(path, rel, claim_re, waivers):
    """Free prose (the first-sweep act): report each authority-claim sentence naming no date."""
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except (UnicodeDecodeError, OSError):
        return
    for i, raw in enumerate(lines, 1):
        for sent in SENT_SPLIT.split(raw):
            if STRUCK.search(sent) or not claim_re.search(sent) or DATE.search(sent):
                continue
            snip = sent.strip()[:120]
            if waived(rel, snip, waivers):
                continue
            yield (i, snip, "authority claim names no date")


def record_surfaces(root):
    try:
        out = subprocess.run(["git", "-C", root, "ls-files"],
                             capture_output=True, text=True, check=True).stdout
        rels = out.splitlines()
    except Exception:
        rels = []
        for dp, _, fns in os.walk(root):
            for fn in fns:
                rels.append(os.path.relpath(os.path.join(dp, fn), root))
    hits = []
    for r in rels:
        if not r.endswith(TEXT_EXT) or is_spared(r):
            continue
        p = os.path.join(root, r)
        try:
            if is_record(open(p, encoding="utf-8").read()):
                hits.append((p, r))
        except (UnicodeDecodeError, OSError):
            continue
    return hits


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--config", default=None)
    ap.add_argument("files", nargs="*")
    a = ap.parse_args(argv[1:])
    default_cfg = os.path.join(os.path.dirname(os.path.abspath(__file__)), "authority-anchor.json")
    cfg = load_config(a.config or default_cfg)
    claim_re = compile_claim(cfg)
    waivers = cfg.get("waivers")

    if claim_re is None:
        print("OK (authority-anchor): no authority patterns declared — the gate stands inert.")
        return 0

    if a.files:
        pairs = [(f, os.path.relpath(f, a.root)) for f in a.files]
    else:
        pairs = record_surfaces(a.root)

    offences = []
    for path, rel in pairs:
        try:
            record = is_record(open(path, encoding="utf-8").read())
        except (UnicodeDecodeError, OSError):
            record = False
        scan = scan_record if record else scan_prose
        for ln, snip, why in scan(path, rel, claim_re, waivers):
            offences.append((rel, ln, snip, why))

    if not offences:
        if not pairs:
            print("OK (authority-anchor): no DECISION-RECORD surface in the tree yet — the standing "
                  "gate stands down by name (SPEC INV-207).")
        else:
            print("OK (authority-anchor): every recorded decision names its exchange (a date a reader "
                  "can check) — SPEC INV-207.")
        return 0

    print("FAIL (authority-anchor): a decision, word, or ruling stands recorded AS the person's but")
    print("names no exchange to check it against (SPEC INV-207, ROADMAP row 415). A human's word is")
    print("the one claim no gate questions, so an unanchored one is unfalsifiable:")
    for rel, ln, snip, why in offences:
        print("  %s:%d  [%s]  %s" % (rel, ln, why, snip))
    print("  Fix: name the exchange it came from — at minimum a date, in the profile's own style")
    print("  (\"<person> 2026-07-03, standing\" / \"...2026-07-14, on X: ...\"). If no exchange backs")
    print("  it, it is the pack's OWN judgment: rewrite it in the pack's voice, challengeable by every")
    print("  reader. A grant to DECIDE never authorizes recording the decision as the human's; strike")
    print("  what the person never said on the read-back surface (DECISIONS.md).")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
