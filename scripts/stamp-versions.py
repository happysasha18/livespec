#!/usr/bin/env python3
"""stamp-versions.py — version is one fact (SPEC INV-178).

The root VERSION file is the pack version's one home. Every skill's frontmatter `version:` line
and every in-text base-version reference ("`live-spec-base` (vX.Y.Z)") is a stamped COPY of that
fact, written by this script and held by a guard test — a per-skill version hand-rolled at edit
time drifts the moment attention does (ten skills carried ten unrelated numbers before this law).
Run it at every version bump; idempotent. Prints old -> new per change, nothing when current.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    version = open(os.path.join(ROOT, "VERSION"), encoding="utf-8").read().strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        print("stamp-versions: unreadable VERSION file", file=sys.stderr)
        return 2
    changed = 0
    skills_dir = os.path.join(ROOT, "skills")
    for name in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(path):
            continue
        body = open(path, encoding="utf-8").read()
        new = body
        m = re.search(r"^(  version: )(\S+)$", new, flags=re.M)
        if m and m.group(2) != version:
            print("%s: version %s -> %s" % (name, m.group(2), version))
            new = new[:m.start(2)] + version + new[m.end(2):]
        new2 = re.sub(r"(`live-spec-base` \(v)\d+\.\d+\.\d+(\))",
                      r"\g<1>" + version + r"\g<2>", new)
        if new2 != new:
            print("%s: base reference stamped to v%s" % (name, version))
            new = new2
        if new != body:
            open(path, "w", encoding="utf-8").write(new)
            changed += 1
    print("stamp-versions: %d file(s) stamped to %s" % (changed, version))
    return 0


if __name__ == "__main__":
    sys.exit(main())
