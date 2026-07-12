#!/usr/bin/env python3
"""preshow-register-lint.py — the mechanical register gate for anything SHOWN to a human (SPEC INV-83).

Why this exists, and how it differs from its neighbour preshow-lint.py:
  preshow-lint.py catches a human-facing line that OPENS with an internal handle (a spec code, a
  row/session number) — a placement tell. THIS lint catches a different disease on the same surface:
  the pack's machine dialect leaking into the words themselves — a coined internal metaphor shown raw
  ("the wish door", "work lean"), an English pack term loan-translated into Russian chat (a calque,
  «швы с соседями» for "seams with neighbours"), or a transliterated pack term («пайплайн»). The law
  it mechanizes is the profile's `language.no-calques` + `language.register`: Russian human-facing text
  NEVER loan-translates the pack's English doc terms, industry-standard words only, and internal
  coinages live in the DOCS only — never in a mockup, a report, a decision page, or a rendered artifact
  a new reader sees first. A caught leak is what «это бред» sounds like from the next user (2026-07-10).

  The two lints stay separate scripts on purpose; the senior decides any merge. Run BOTH at the
  pre-show gate.

What it can and cannot do (stated honestly, so no one over-trusts it):
  A PATTERN lint catches KNOWN coinages, KNOWN calques, and named term classes — the leaks already
  seen. It CANNOT judge a novel machine-flavoured abstraction it has never been shown ("everything
  comes up naturally when it first matters" is only caught because tonight's exact leak was folded in
  as a pattern). That residual — a fresh abstraction in the same machine register — belongs to the
  CLEAN-READER CHECK (a fresh agent, pack NOT loaded, reads the surface as an outside reader; docs/
  spec-style.md "clean agent" split). This lint is the floor; the clean-reader check is the ceiling.

The growth duty (SPEC INV-83): the pattern set GROWS BY ONE per caught leak. Each new leak that gets
past the lint becomes a pattern the SAME day, with a comment naming its source and date. That is how a
pattern lint stays ahead of a living dialect.

Design rule that keeps the accepted reader docs green: a pattern is the SPECIFIC coined collocation,
never its ordinary constituent words. "station", "door", "lean", "full" are legitimate industry words
the reader docs use freely; only the coinages "pipeline station", "wish door", "work lean", "full
rigor" are flagged. Verified 2026-07-10: the nine accepted reader docs contain the constituent words
but none of the coinages.

Usage: preshow-register-lint.py FILE [FILE ...]      (or: cat text | preshow-register-lint.py -)
Exit 0 = clean · exit 1 = at least one pattern hit (printed with file, line, pattern id, source).
"""
import re
import sys

# Each pattern: (id, language, compiled-regex, source-of-the-leak, date-folded-in).
# ALL patterns are case-insensitive; \w and \b are Unicode-aware in Python 3, so Cyrillic word
# boundaries work. A pattern is a SPECIFIC coinage/calque collocation, never a bare industry word.
_F = re.IGNORECASE | re.UNICODE
PATTERNS = [
    # ---- English: internal SETTING / MECHANISM names shown raw ---------------------------------
    # source: onboarding mockup jargon strip, «это бред» (2026-07-10 ~00:14)
    ("en-full-rigor", "en", re.compile(r"\bfull\s+rigou?r\b", _F),
     "onboarding mockup — internal setting name 'full rigor' shown raw", "2026-07-10"),
    ("en-work-lean", "en", re.compile(r"\bwork\s+lean\b", _F),
     "onboarding mockup — internal setting name 'work lean' shown raw", "2026-07-10"),
    # source: pack coinages that must live in docs only, never in a shown mockup/report
    ("en-pipeline-station", "en", re.compile(r"\bpipeline\s+stations?\b", _F),
     "pack coinage 'the pipeline station' shown raw to a reader", "2026-07-10"),
    ("en-wish-door", "en", re.compile(r"\bwish\s+doors?\b", _F),
     "pack coinage 'the wish door' shown raw to a reader", "2026-07-10"),
    # source: onboarding mockup — a machine-flavoured abstraction; folded in as the exact caught
    # phrases (the grows-by-one duty). NOTE: these two are ordinary English, not coinages; a stricter
    # reading leaves them to the clean-reader check. Kept here as tonight's caught leak; senior's call.
    ("en-comes-up-naturally", "en", re.compile(r"\bcomes?\s+up\s+naturally\b", _F),
     "onboarding mockup — 'comes up naturally' machine abstraction", "2026-07-10"),
    ("en-when-it-first-matters", "en", re.compile(r"\bwhen\s+it\s+first\s+matters\b", _F),
     "onboarding mockup — 'when it first matters' machine abstraction", "2026-07-10"),

    # ---- Russian: CALQUES of the pack's English coinages (loan-translations) --------------------
    # source: another window's chat, same disease class (2026-07-10)
    ("ru-shvy-s-sosedyami", "ru", re.compile(r"шв\w+\s+с\s+сосед\w+", _F),
     "chat calque «швы с соседями» ← 'seams with neighbours'", "2026-07-10"),
    ("ru-rabotniki-v-pole", "ru", re.compile(r"работник\w*\s+в\s+поле", _F),
     "chat calque «работники в поле» ← 'workers in the field'", "2026-07-10"),
    ("ru-smert-scheta", "ru", re.compile(r"смерт\w*\s+сч[её]т\w*", _F),
     "chat calque «смерть счёта» ← 'budget death'", "2026-07-10"),
    ("ru-styki-poverkhnostei", "ru", re.compile(r"стык\w*\s+поверхност\w+", _F),
     "chat calque «стыки поверхностей» ← 'surface seams'", "2026-07-10"),

    # ---- Russian: the known-bad calque list from the profile (language.no-calques) -------------
    # source: profile.md language.no-calques (2026-07-05 / 2026-07-07)
    ("ru-rastyazhki", "ru", re.compile(r"растяжк\w*", _F),
     "profile known-bad calque «растяжки» ← 'tripwires'", "2026-07-05"),
    ("ru-ta-zhe-semya", "ru", re.compile(r"(?<!\w)т[аяойеу]\w*\s+же\s+семь\w+", _F),
     "profile known-bad calque «та же семья» ← 'the same incident family'", "2026-07-05"),
    ("ru-posadka", "ru", re.compile(r"(?<!\w)посадк\w*", _F),
     "profile known-bad calque «посадка» ← 'landing'", "2026-07-05"),
    ("ru-uzel-vladelets", "ru", re.compile(r"уз(?:ел|л\w+)[-\s]владел\w+", _F),
     "profile known-bad coinage «узел-владелец» ← 'owner node'", "2026-07-07"),

    # ---- Russian: TRANSLITERATED pack terms (say the industry word or the mechanism instead) ---
    # source: profile.md language.no-calques — internal coinages transliterated read as machine-speak
    ("ru-payplayn", "ru", re.compile(r"(?<!\w)пайплайн\w*", _F),
     "transliterated pack term «пайплайн» ← 'pipeline'", "2026-07-07"),
    ("ru-vorker", "ru", re.compile(r"(?<!\w)воркер\w*", _F),
     "transliterated pack term «воркер» ← 'worker'", "2026-07-07"),
    ("ru-steyshn", "ru", re.compile(r"(?<!\w)стейшн\w*", _F),
     "transliterated pack term «стейшн» ← 'station'", "2026-07-07"),

    # ---- Self-certification of sincerity (SPEC INV-94) ------------------------------------------
    # source: the pack's own README certified itself twice in one day; his word 2026-07-10 ~13:53
    ("en-say-so-plainly", "en", re.compile(r"\bsay\s+so\s+plainly\b", _F),
     "self-certification 'we say so plainly' — the content carries the honesty", "2026-07-10"),
    ("en-honest-treatment", "en", re.compile(r"\bhonest\s+treatment\b", _F),
     "self-certification 'deserves the same honest treatment'", "2026-07-10"),
    ("en-unsoftened", "en", re.compile(r"\bunsoftened\b", _F),
     "self-certification 'published unsoftened' — say what it IS (in full)", "2026-07-10"),
    ("ru-iz-chestnogo", "ru", re.compile(r"(?<!\w)из\s+честного", _F),
     "self-certification «из честного» — as if the rest were otherwise", "2026-07-10"),
    ("ru-chestno-govorya", "ru", re.compile(r"(?<!\w)честно\s+говоря", _F),
     "self-certification «честно говоря»", "2026-07-10"),
    ("ru-ne-po-pamyati", "ru", re.compile(r"(?<!\w)не\s+по\s+памяти", _F),
     "self-certification of diligence «проверил не по памяти» — state the source, drop the label", "2026-07-10"),
]

# Comment example, deliberately NOT a pattern: a bare unevidenced claim like
#   "How setup feels — almost no questions"
# is a register/evidence problem a phrase-pattern cannot judge (nothing lexical to match). It belongs
# to the clean-reader check and the evidence/no-bare-claim gate, not here.


def scan(text):
    """Return a list of (line_no, pattern_id, snippet, source) for every pattern hit."""
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        for pid, _lang, rx, source, _date in PATTERNS:
            if rx.search(line):
                hits.append((i, pid, line.strip()[:110], source))
    return hits


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("usage: preshow-register-lint.py FILE [FILE ...]|-\n")
        return 2
    any_hit = False
    for src in argv[1:]:
        text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
        hits = scan(text)
        if not hits:
            continue
        any_hit = True
        print("PRE-SHOW REGISTER LINT (SPEC INV-83): the pack's machine dialect leaked into text a")
        print("human is about to see. Say it in the reader's own plain words before showing. File: %s" % src)
        for line_no, pid, snippet, source in hits:
            print("  line %d  [%s]  %s" % (line_no, pid, snippet))
            print("          ↳ source: %s" % source)
    if any_hit:
        print('{"severity":"error","code":"register-leak","message":"a shown surface carries a coined '
              'metaphor, a calque, or a transliterated pack term","fix":"say it in the reader\'s own '
              'plain words; internal coinages live in docs only"}')
        return 1
    print("OK (preshow-register): no coined metaphor, calque, or transliterated pack term found.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
