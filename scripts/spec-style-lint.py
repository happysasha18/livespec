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

Usage: spec-style-lint.py FILE            (or: cat text | spec-style-lint.py -)
Exit 0 = no ERROR (WARN may still print) · exit 1 = at least one ERROR.
"""
import re
import sys

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
              "LIVE", "STATE", "NEXT", "NOW", "MUST", "SHALL", "NOTE", "QA", "TODO"}
FILENAME_RE = re.compile(r"\b[\w./-]+\.(?:md|py|sh|json|txt|html|js|css|yml|yaml|toml)\b")
CAPS_RE = re.compile(r"(?<![\w`\[])([A-Z]{2,})(?![\w`\]-])")

# --- second person ---------------------------------------------------------------------------
SECOND_PERSON = re.compile(r"(?<!\w)(you|your|you're|yours|yourself)(?!\w)", re.IGNORECASE)


def lint(text):
    """Return (errors, warnings); each a list of (line_no, code, snippet)."""
    errors, warnings = [], []
    prev_blank = True
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip("\n")
        stripped = line.strip()
        if not stripped:
            prev_blank = True
            continue
        # strip a leading bullet/quote marker (so "- Never …" is not read as a dash-cut), then
        # inline code spans and bracketed anchors, so `docs/decisions/` and [INV-4] never trip
        # caps / jargon / scissors. A **bold title** is kept — jargon/caps inside it still count.
        scrub = LEAD_MARKERS.sub("", stripped)
        scrub = re.sub(r"`[^`]*`", " ", scrub)
        scrub = re.sub(r"\[[^\]]*\]", " ", scrub)
        scrub = FILENAME_RE.sub(" ", scrub)          # ROADMAP.md / SPEC.md are filenames, not shout

        is_block_lead = prev_blank or bool(LEAD_MARKERS.match(line))
        if is_block_lead and _is_negation_opener(_strip_lead(line)):
            errors.append((i, "negation-opener", stripped[:110]))
        if SCISSORS.search(scrub):
            errors.append((i, "scissors", stripped[:110]))
        for m in JARGON_RE.finditer(scrub):
            errors.append((i, "machine-jargon:%s" % m.group(1).lower(), stripped[:110]))
        for m in CAPS_RE.finditer(scrub):
            if m.group(1) not in CAPS_ALLOW:
                warnings.append((i, "caps-shout:%s" % m.group(1), stripped[:110]))
        if SECOND_PERSON.search(scrub):
            warnings.append((i, "second-person", stripped[:110]))
        prev_blank = False
    return errors, warnings


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: spec-style-lint.py FILE|-\n")
        return 2
    src = argv[1]
    text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    errors, warnings = lint(text)
    if not errors and not warnings:
        print("OK (spec-style): no register tells found.")
        return 0
    if errors:
        print("SPEC-STYLE LINT — ERROR (docs/spec-style.md): a rule opens with what it is NOT,")
        print("shouts, uses machine jargon, or cuts with «X — not Y». Rewrite these:")
        for line_no, code, snip in errors:
            print("  line %d  [%s]  %s" % (line_no, code, snip))
    if warnings:
        print("SPEC-STYLE LINT — warn (soft signals; a fully-converted section clears these too):")
        for line_no, code, snip in warnings:
            print("  line %d  [%s]  %s" % (line_no, code, snip))
    print('{"severity":"%s","code":"spec-style","errors":%d,"warnings":%d}'
          % ("error" if errors else "advisory", len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
