#!/usr/bin/env python3
"""check-doc-bound.py — gate z: every growable working doc stays within its declared bound (SPEC
INV-234, ROADMAP row 392, the growth-law family).

Everything that can grow declares the number that bounds it and the watcher that reads it. INV-41 states
the shape — a budget plus the watcher that reds past it — and this lifts it to the four large working
documents: PRODUCT_SPEC.md, ROADMAP.md, TEST_MATRIX.md, and JOURNAL.md, which grow with every landing
until a guard's scan and a grep run slow (the owner's word, 2026-07-17 ~18:25, at roughly half a
megabyte each). Each declares a byte ceiling with a recorded reason in `guardrails/doc-bounds.json`, and
this gate reds a doc past its ceiling.

It COMPOSES with the doc-rotation gate (gate t, `guardrails/check-doc-rotation.py`, SPEC INV-209):
crossing the bound is what earns a rotation, and the rotation is the remedy the red points to. A doc
rotated TODAY — carrying a `<!-- rotated-manifest -->` block naming an archive dated today — passes even
over its ceiling, since the grooming that shrinks the live file back under the bound has just been
applied. A rotation from another day does not clear today's overflow.

Three states, one gate:
  (a) size <= bound                                    -> pass.
  (b) size > bound AND freshly rotated today           -> pass (the remedy applied; compose with gate t).
  (c) size > bound, no fresh rotation, no raised bound -> RED, pointing at the two remedies:
      rotate the closed rows out (scripts/rotate-doc.py), or raise the ceiling in doc-bounds.json with a
      recorded reason.

A bound rises only with a recorded reason: every declared entry must carry a non-empty `reason`, and a
bound with none reds (the raise discipline, kin of the debt cap's deliberate-visible-edit rule). The
ceilings are seeded ABOVE the current file sizes with rotation headroom, so this very gate never reds
the already-large tree; the ratchet's direction is down, reset by rotation, never a silent creep up.

Usage:
  check-doc-bound.py                              push mode: read guardrails/doc-bounds.json at the repo.
  check-doc-bound.py --base DIR                   resolve the declared docs under DIR (default: repo root).
  check-doc-bound.py --bounds FILE               read the bounds from FILE (fixtures).
  check-doc-bound.py --today YYYY-MM-DD           override today's date (fixtures; default: the real day).
"""
import argparse
import datetime
import json
import os
import re
import sys

MANIFEST_OPEN = "<!-- rotated-manifest -->"
MANIFEST_CLOSE = "<!-- /rotated-manifest -->"
# an archive path names its rotation date: rotated-<doc>-YYYY-MM-DD.md
ARCHIVE_DATE_RE = re.compile(r"rotated-.*?-(\d{4}-\d{2}-\d{2})\.md")


def repo_root():
    import subprocess
    try:
        out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                      stderr=subprocess.DEVNULL, text=True).strip()
        if out:
            return out
    except Exception:
        pass
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rotated_today(doc_text, today):
    """True when the doc carries a rotation manifest naming an archive dated `today` — the fresh-rotation
    grace that composes with gate t (SPEC INV-209)."""
    for block in re.findall(re.escape(MANIFEST_OPEN) + r"(.*?)" + re.escape(MANIFEST_CLOSE),
                            doc_text, re.S):
        for m in ARCHIVE_DATE_RE.finditer(block):
            if m.group(1) == today:
                return True
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(description="the growable-doc bound watcher (SPEC INV-234)")
    ap.add_argument("--base", default=None)
    ap.add_argument("--bounds", default=None)
    ap.add_argument("--today", default=None)
    args = ap.parse_args(argv)

    root = args.base or repo_root()
    bounds_path = args.bounds or os.path.join(root, "guardrails", "doc-bounds.json")
    today = args.today or datetime.date.today().isoformat()

    with open(bounds_path, encoding="utf-8") as f:
        cfg = json.load(f)
    docs = cfg.get("docs", {})

    if not docs:
        print("doc-bound: the bounds file declares no growable doc — a check that looks at nothing is "
              "not a pass (SPEC INV-218 kin). Declare the four working docs in %s." % bounds_path)
        return 1

    violations = []
    for name, entry in sorted(docs.items()):
        bound = entry.get("max_bytes")
        reason = (entry.get("reason") or "").strip()
        path = os.path.join(root, name)
        if not reason:
            violations.append("%s declares a bound with no recorded reason — a bound rises only with a "
                              "recorded reason." % name)
            continue
        if bound is None:
            violations.append("%s declares no max_bytes." % name)
            continue
        if not os.path.isfile(path):
            violations.append("%s is declared a growable doc but is absent under %s." % (name, root))
            continue
        size = os.path.getsize(path)
        if size <= bound:
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        if rotated_today(text, today):
            continue  # the remedy was applied today — compose with gate t (INV-209).
        violations.append(
            "%s is %d bytes, past its declared bound of %d, with no rotation dated %s. Remedy: rotate "
            "the closed rows out (scripts/rotate-doc.py) so the live file shrinks back under the bound, "
            "or raise max_bytes in %s with a recorded reason."
            % (name, size, bound, today, os.path.basename(bounds_path)))

    if violations:
        print("doc-bound (gate z): %d growable doc(s) past bound (SPEC INV-234, ROADMAP 392):"
              % len(violations))
        for v in violations:
            print("  " + v)
        return 1

    print("doc-bound (gate z): OK — every growable doc sits within its declared bound (or was rotated "
          "today); %d docs read." % len(docs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
