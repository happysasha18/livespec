#!/usr/bin/env python3
"""spec-style-lint.py — the mechanical arm of the SPEC prose register (docs/spec-style.md).

Why this exists: re-styling the spec by hand drifted five times — a picked voice read fine on a
short sample, then degraded across long, constraint-heavy prose, and the tells only surfaced when a
human read it late. The tells are mechanical: a rule that OPENS with a negation instead of what
happens, machine jargon in user-facing prose, ALL-CAPS shouting where the plain statement carries
the force, and the banned «X — not Y» scissors. This scans the register and flags each tell with its
line, so the author (or a fresh session rewriting from scratch) drives a section to clean against a
machine — not against a reader's patience. The register lives in docs/spec-style.md; this only holds
the floor it can check. Positive elegance (flow, sharpness) the linter cannot judge — that is what
the gold exemplars in docs/spec-style.md are for. Floor + exemplars = the whole quality system.

Checks (each maps to a rule in docs/spec-style.md):
  ERROR   negation-opener  a block leads with what it is NOT before what it IS (R4/plainness).
  ERROR   scissors         the «X — not Y» / «X — never Y» construction — a GLOBAL, PERMANENT ban.
  ERROR   machine-jargon   a dev/corporate word that has no place in this user-facing spec (R7).
  WARN    caps-shout       an ALL-CAPS ordinary word; force comes from the statement, not caps (R12).
  WARN    second-person    "you"/"your" — the register speaks of named actors, not the reader (R3).

In --gate mode (the DONE-GATE, docs/prose-quality-gate-design.md) the two soft signals are PROMOTED to
blocking errors, two more mechanical rules join them (reassurance, future-narration), the normative-only
rules skip marked informative regions (a user-story line, a blockquote, a NOTE), and a machine-readable
waiver file (scripts/spec-waivers.json) moves a still-unfixed finding into a dated, counted debt bucket
instead of a silent pass. Default mode is unchanged (caps-shout and second-person stay advisory), so the
section-by-section workflow and its tests keep their contract.

Usage: spec-style-lint.py [--gate] FILE       (or: cat text | spec-style-lint.py [--gate] -)
Exit 0 = no ERROR (WARN may still print) · exit 1 = at least one ERROR.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_common  # noqa: E402  (sibling module in scripts/)

# --- negation-opener -------------------------------------------------------------------------
# A block (a paragraph line, a bullet, or a bold-titled rule) should open with what happens, not
# with what the thing is NOT. The ugly pattern is DEFINE-BY-EXCLUSION: the opening states what the
# subject is not, via a copula or a becoming verb ("X is not Y", "X does not become Y", "Not a Z"),
# instead of what it is. An ACTION prohibition ("does not ask", "never re-carves", "no design
# decision inside") is correct register (R4 blesses "does not"/"never" for prohibitions) and is NOT
# flagged. We examine only the block's opening clause, after stripping markdown markers and a
# leading **bold title** (the title names the rule; the body that follows carries the statement).
LEAD_MARKERS = re.compile(r"^\s*(?:(?:[-*+>]\s+)|(?:#{1,6}\s+))+")   # real bullet/quote/heading (marker + space), never a **bold** run
BOLD_TITLE = re.compile(r"^\s*\*\*[^*]+\*\*\.?\s*")          # a leading **bold title** (+ its period)
NEG_OPENER_WORDS = 12                                        # opening clause window
COPULA = {"is", "are", "was", "were", "be", "been", "being"}
COPULA_NT = {"isn't", "aren't", "wasn't", "weren't"}         # contracted copula-negation
BECOMING = {"become", "becomes", "make", "makes", "mean", "means", "form", "forms",
            "constitute", "constitutes", "turn", "turns", "represent", "represents"}
# a subordinator fronts a CONDITION; a negation inside a condition ("priority when it is not
# normal") is legal, not define-by-exclusion. Only a negation NOT under a preceding subordinator
# counts as an opener tell.
SUBORD = {"when", "if", "where", "until", "once", "while", "unless", "whenever", "wherever",
          "as", "after", "before", "because", "since", "though", "although", "whether"}


def _strip_lead(line):
    """Remove markdown markers and a leading bold title; return the body that states the rule."""
    body = LEAD_MARKERS.sub("", line)
    body = BOLD_TITLE.sub("", body)
    return body.strip()


def _is_negation_opener(body):
    """A block opener defines by exclusion: it states what the subject is NOT (via a copula or a
    becoming verb) before what it is. Prohibitions on an action and negations inside a fronted
    condition are NOT tells."""
    words = [w.lower() for w in re.findall(r"[A-Za-z']+", body)][:NEG_OPENER_WORDS]
    if not words:
        return False
    if words[0] in ("not", "neither"):
        return True
    if words[0] == "no" and len(words) > 1 and words[1] == "longer":
        return True
    seen_subord = False
    for i, w in enumerate(words):
        if w in SUBORD:
            seen_subord = True
        if seen_subord:
            continue
        if w in COPULA_NT:
            return True
        if w in COPULA and i + 1 < len(words) and words[i + 1] == "not":
            return True
        if w in ("do", "does", "did") and i + 2 < len(words) \
                and words[i + 1] == "not" and words[i + 2] in BECOMING:
            return True
    return False


# --- scissors --------------------------------------------------------------------------------
SCISSORS = re.compile(r"[—–]\s*(?:not|never)\b|(?<!\w)-{1,2}\s+(?:not|never)\b", re.IGNORECASE)

# --- machine jargon (curated, extensible — add a word only when it is unambiguously wrong here) --
JARGON = {"serialized", "questionnaire", "instantiate", "instantiated", "functionality",
          "leverage", "leveraging", "utilize", "utilizes", "utilization", "performant"}
JARGON_RE = re.compile(r"(?<!\w)(%s)(?!\w)" % "|".join(sorted(JARGON)), re.IGNORECASE)

# --- caps-shout ------------------------------------------------------------------------------
# an ALL-CAPS alphabetic word of length >= 2 that is not a known acronym or defined term.
CAPS_ALLOW = {"JSON", "CI", "HTML", "CSS", "RFC", "API", "URL", "UI", "MVP", "TTL", "MECE",
              "LLD", "HLD", "PRD", "README", "OK", "MD", "CLI", "ID", "IDE", "NLP", "SPEC",
              "LIVE", "STATE", "NEXT", "NOW", "MUST", "SHALL", "NOTE", "QA", "TODO", "HEAD",
              "KPI", "UX", "FIXME",
              # defined prover/verify mode names — literal terms, not shout
              "CROSS-LINK", "FEATURE-FIT", "RE-ENTRY",
              # defined bold law-part labels of the narration law (INV-35)
              "IDENTITY", "DIGEST", "HEARTBEAT"}
FILENAME_RE = re.compile(r"\b[\w./-]+\.(?:md|py|sh|json|txt|html|js|css|yml|yaml|toml)\b")
# capture an ALL-CAPS token, including a hyphenated compound (CROSS-LINK) as one token, so a
# defined mode name is judged whole against the allowlist rather than split into "LINK".
CAPS_RE = re.compile(r"(?<![\w`\[])([A-Z]{2,}(?:-[A-Z]{2,})*)(?![\w`\]-])")

# --- second person ---------------------------------------------------------------------------
SECOND_PERSON = re.compile(r"(?<!\w)(you|your|you're|yours|yourself)(?!\w)", re.IGNORECASE)

# --- reassurance / invitation (gate mode only, R4/R7) ----------------------------------------
# Reassuring or inviting the reader has no place in a normative sentence. Curated phrases, kept
# conservative so a legitimate word ("just one row" as a quantity) is not caught; "simply" and the
# listed phrases are the unambiguous tells (the recurring intro-block leak said "you can ignore").
REASSURANCE = ("don't worry", "no need to", "feel free", "of course", "rest assured",
               "you can ignore", "you don't have to", "as we saw", "as noted above",
               "needless to say", "simply put")
REASSURANCE_RE = re.compile(r"(?<!\w)simply(?!\w)", re.IGNORECASE)  # bare 'simply' is a tell on its own

# --- future narration (gate mode only, R4) ---------------------------------------------------
# A reference spec states what is true in the present. "the card will show", "the row that shall
# carry" is future narration; rephrase to present. Scoped to will/shall + a spec verb to avoid
# catching every "will".
FUTURE_NARRATION = re.compile(
    r"(?<!\w)(?:will|shall)\s+(?:be|show|shows|display|appear|open|contain|"
    r"return|carry|report|hold|become|run|fire|land|ship)\b", re.IGNORECASE)


def lint(text, gate=False):
    """Return (errors, warnings); each a list of (line_no, code, snippet).

    Default: negation-opener/scissors/machine-jargon are errors; caps-shout/second-person are
    warnings. --gate: caps-shout and second-person are promoted to errors, reassurance and
    future-narration join them, and the normative-only rules (negation-opener, second-person,
    reassurance, future-narration) skip marked informative regions (user-story line, blockquote,
    NOTE) — global rules (scissors, machine-jargon, caps-shout) always run."""
    errors, warnings = [], []
    lines = text.splitlines()
    exempt = gate_common.exempt_flags(lines) if gate else [False] * len(lines)
    prev_blank = True
    for idx, raw in enumerate(lines):
        i = idx + 1
        line = raw.rstrip("\n")
        stripped = line.strip()
        if not stripped:
            prev_blank = True
            continue
        # strip a leading bullet/quote marker (so "- Never …" is not read as a dash-cut), then
        # inline code spans and bracketed anchors, so `docs/decisions/` and [INV-4] never trip
        # caps / jargon / scissors. A **bold title** is kept — jargon/caps inside it still count.
        scrub = gate_common.scrub(stripped)
        exempt_here = exempt[idx]
        # bucket a rule by mode: in gate mode the promoted rules are errors, else warnings.
        norm_bucket = errors if gate else warnings

        is_block_lead = prev_blank or bool(LEAD_MARKERS.match(line))
        if is_block_lead and _is_negation_opener(_strip_lead(line)) and not exempt_here:
            errors.append((i, "negation-opener", stripped[:110]))
        if SCISSORS.search(scrub):                                   # global
            errors.append((i, "scissors", stripped[:110]))
        for m in JARGON_RE.finditer(scrub):                          # global
            errors.append((i, "machine-jargon:%s" % m.group(1).lower(), stripped[:110]))
        for m in CAPS_RE.finditer(scrub):                            # global
            if m.group(1) not in CAPS_ALLOW:
                (errors if gate else warnings).append(
                    (i, "caps-shout:%s" % m.group(1), stripped[:110]))
        if SECOND_PERSON.search(scrub) and not exempt_here:          # normative-only
            norm_bucket.append((i, "second-person", stripped[:110]))
        if gate and not exempt_here:
            low = scrub.lower()
            hit = next((p for p in REASSURANCE if p in low), None) or \
                (REASSURANCE_RE.search(scrub) and "simply")
            if hit:
                errors.append((i, "reassurance:%s" % hit, stripped[:110]))
            if FUTURE_NARRATION.search(scrub):
                errors.append((i, "future-narration", stripped[:110]))
        prev_blank = False
    return errors, warnings


def apply_waivers(findings, filename, waivers, today=None):
    """Split findings into (active_errors, waived). A finding is (line, code, snippet); its rule is
    the code's head before ':'. Records which waiver ids matched, for stale-waiver reporting."""
    active, waived, matched = [], [], set()
    for line, code, snip in findings:
        rule = code.split(":", 1)[0]
        w = gate_common.match_waiver(rule, filename, snip, waivers, today)
        if w:
            waived.append((line, code, snip, w["id"]))
            matched.add(w["id"])
        else:
            active.append((line, code, snip))
    return active, waived, matched


WAIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spec-waivers.json")


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    gate = "--gate" in argv[1:]
    if len(args) != 1:
        sys.stderr.write("usage: spec-style-lint.py [--gate] FILE|-\n")
        return 2
    src = args[0]
    text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    errors, warnings = lint(text, gate=gate)

    waived, stale = [], []
    if gate:
        waivers = gate_common.load_waivers(WAIVER_PATH)
        errors, waived, matched = apply_waivers(errors, src, waivers)
        stale = gate_common.stale_waivers(waivers, matched)

    if not errors and not warnings and not waived:
        print("OK (spec-style%s): no register tells found." % ("/gate" if gate else ""))
    if errors:
        print("SPEC-STYLE LINT — ERROR (docs/spec-style.md): a rule opens with what it is NOT,")
        print("shouts, uses machine jargon, cuts with «X — not Y», reassures, or narrates the future.")
        for line_no, code, snip in errors:
            print("  line %d  [%s]  %s" % (line_no, code, snip))
    if warnings:
        print("SPEC-STYLE LINT — warn (soft signals; a fully-converted section clears these too):")
        for line_no, code, snip in warnings:
            print("  line %d  [%s]  %s" % (line_no, code, snip))
    if waived:
        print("SPEC-STYLE LINT — WAIVED (dated debt, scripts/spec-waivers.json; still counted):")
        for line_no, code, snip, wid in waived:
            print("  line %d  [%s]  (%s)  %s" % (line_no, code, wid, snip))
    if stale:
        print("SPEC-STYLE LINT — stale waivers (defect gone; remove these from spec-waivers.json):")
        for w in stale:
            print("  [%s]  %s" % (w.get("id"), w.get("snippet")))
    print('{"severity":"%s","code":"spec-style","errors":%d,"warnings":%d,"waived":%d,"stale":%d}'
          % ("error" if errors else "advisory", len(errors), len(warnings), len(waived), len(stale)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
