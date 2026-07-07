#!/usr/bin/env python3
"""needle-extract — the mechanical safety gate for the SPEC-humanize migration.

Direction matters (Fable MUST-FIX 2): we match the traceability suite's verbatim prose literals
AGAINST a section, never grep the section's prose for fragments. And the check is SECTION-SCOPED
(Fable MUST-FIX 1): a needle the OLD section carried must still live in the NEW section — a copy
surviving elsewhere in the doc does NOT excuse dropping it here.

The registry is `tests/test_traceability.py` (+ any skill doc that echoes a clause; pass extra files
with --also). No copy of the needles is kept anywhere — this script derives them live, so the tests
stay the one home.

Flow per batch:
  1. BEFORE editing:  needle-extract.py --section "What live-spec is" --capture /tmp/nx.json
  2. edit SPEC.md
  3. AFTER editing:   needle-extract.py --section "What live-spec is" --verify /tmp/nx.json
     -> exit 0 and "OK: N needles preserved"  |  exit 1 and the list of DROPPED needles.

Also: --list dumps every needle the current section carries; --between A B uses a line range instead
of a heading name (for sections whose heading text you don't want to type).
"""
import ast, re, sys, os, json, argparse

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS = os.path.join(REPO, "tests", "test_traceability.py")
SPEC = os.path.join(REPO, "SPEC.md")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def registry_literals(extra_files):
    """Every plain, prose-like string constant in the traceability suite (+ any --also file).

    Conservative on purpose: over-collecting is safe (we only ever ASSERT a phrase we kept stays),
    under-collecting drops a needle. So we take every string constant that reads like prose and skip
    only format strings / anchors / paths.
    """
    lits = set()
    for path in [TESTS] + list(extra_files):
        try:
            tree = ast.parse(open(path).read())
        except (SyntaxError, FileNotFoundError):
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                v = norm(node.value)
                if len(v) >= 8 and " " in v and "%" not in v and "\\" not in v:
                    lits.add(v)
    return lits


def section_text(name=None, between=None):
    lines = open(SPEC).read().split("\n")
    if between:
        return "\n".join(lines[between[0] - 1:between[1]])
    out, grab = [], False
    for ln in lines:
        if ln.startswith("## "):
            if grab:
                break
            grab = norm(ln[3:]) == norm(name)
            continue
        if grab:
            out.append(ln)
    return "\n".join(out)


def needles_in(text, extra_files):
    body = norm(text)
    return sorted(n for n in registry_literals(extra_files) if n in body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--section")
    ap.add_argument("--between", nargs=2, type=int)
    ap.add_argument("--also", nargs="*", default=[], help="extra registry files (skill docs echoing a clause)")
    ap.add_argument("--capture", metavar="PATH")
    ap.add_argument("--verify", metavar="PATH")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    text = section_text(name=args.section, between=tuple(args.between) if args.between else None)
    if not text.strip():
        print("ERROR: empty section — check the heading text / line range", file=sys.stderr)
        return 2
    current = needles_in(text, args.also)

    if args.capture:
        json.dump(current, open(args.capture, "w"), ensure_ascii=False, indent=0)
        print("captured %d needles -> %s" % (len(current), args.capture))
        return 0

    if args.verify:
        want = json.load(open(args.verify))
        body = norm(text)
        dropped = [n for n in want if n not in body]
        if dropped:
            print("DROPPED %d needle(s) — the rewrite lost verbatim prose the suite asserts:" % len(dropped))
            for n in dropped:
                print("  - " + (n[:110] + ("…" if len(n) > 110 else "")))
            return 1
        print("OK: %d needles preserved (section-scoped)." % len(want))
        return 0

    for n in current:
        print(n)
    print("\n(%d needles in section)" % len(current), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
