#!/usr/bin/env bash
# adopt/install-ratchet.sh — the turnkey ratchet-adoption kit (SPEC INV-172).
#
# Run from a HOST repo root. Vendors the pack's style/redundancy/freeze gates into the host, seeds a
# debt cap at the host's CURRENT size (an adoption run never blocks on pre-existing debt — only on
# growth beyond it), and generates a lock test that only ever tightens: doc growth beyond the seeded
# cap reds the suite, and raising the cap itself means editing the generated test (deliberate,
# visible, reviewed — never a silent raise).
#
# Usage: adopt/install-ratchet.sh [--force] [--tier universal|full] [DOC ...]
#   DOC...     gated doc paths (relative to the host root). If omitted: read
#              guardrails.config.json's spec_path (+ extra_gated_docs) if present in the host root,
#              else default to PRODUCT_SPEC.md if that file exists, else fail.
#   --force    overwrite an already-vendored file (default: skip an existing file and note it).
#   --tier     tier passed to the vendored style lint when seeding + locking (default: universal).
set -euo pipefail

PACK_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOST_ROOT="$(pwd)"

FORCE=0
TIER="universal"
DOCS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --force) FORCE=1; shift ;;
    --tier) TIER="$2"; shift 2 ;;
    --tier=*) TIER="${1#--tier=}"; shift ;;
    *) DOCS+=("$1"); shift ;;
  esac
done

# --- step a: resolve the host's gated doc set --------------------------------------------------
if [ ${#DOCS[@]} -eq 0 ]; then
  if [ -f "$HOST_ROOT/guardrails.config.json" ]; then
    while IFS= read -r d; do
      [ -n "$d" ] && DOCS+=("$d")
    done < <(python3 - "$HOST_ROOT/guardrails.config.json" << 'PYEOF'
import json, sys
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
docs = []
if cfg.get("spec_path"):
    docs.append(cfg["spec_path"])
docs.extend(cfg.get("extra_gated_docs") or [])
for d in docs:
    print(d)
PYEOF
)
  elif [ -f "$HOST_ROOT/PRODUCT_SPEC.md" ]; then
    DOCS=("PRODUCT_SPEC.md")
  fi
fi

if [ ${#DOCS[@]} -eq 0 ]; then
  echo '{"severity":"error","code":"ratchet-install","message":"no gated docs found","fix":"pass doc paths as arguments"}'
  exit 1
fi

# --- step b: vendor the pack's gate files into the host ------------------------------------------
VENDOR_FILES=(
  "scripts/spec-style-lint.py"
  "scripts/spec-redundancy-precheck.py"
  "scripts/spec-freeze.py"
  "scripts/gate_common.py"
  "guardrails/check-freeze.sh"
)

for rel in "${VENDOR_FILES[@]}"; do
  src="$PACK_ROOT/$rel"
  dest="$HOST_ROOT/$rel"
  mkdir -p "$(dirname "$dest")"
  if [ -f "$dest" ] && [ "$FORCE" -ne 1 ]; then
    echo "skip (exists, use --force to overwrite): $rel"
  else
    cp "$src" "$dest"
    echo "vendored: $rel"
  fi
done

# --- step d: seed caps at the host's CURRENT size -----------------------------------------------
STYLE_ERRORS=0
REDUNDANCY_OPEN=0
for doc in "${DOCS[@]}"; do
  style_out="$(python3 "$HOST_ROOT/scripts/spec-style-lint.py" --tier "$TIER" "$HOST_ROOT/$doc" 2>&1 || true)"
  style_json="$(printf '%s\n' "$style_out" | tail -n1)"
  n="$(python3 -c "import json,sys; print(json.loads(sys.argv[1])['errors'])" "$style_json")"
  STYLE_ERRORS=$((STYLE_ERRORS + n))

  redundancy_out="$(python3 "$HOST_ROOT/scripts/spec-redundancy-precheck.py" "$HOST_ROOT/$doc" 2>&1 || true)"
  redundancy_json="$(printf '%s\n' "$redundancy_out" | tail -n1)"
  m="$(python3 -c "import json,sys; print(json.loads(sys.argv[1])['open'])" "$redundancy_json")"
  REDUNDANCY_OPEN=$((REDUNDANCY_OPEN + m))
done

# --- step c + d: write the manifest, the debt cap, and the generated lock test -------------------
python3 - "$HOST_ROOT" "$PACK_ROOT" "$TIER" "$STYLE_ERRORS" "$REDUNDANCY_OPEN" "${DOCS[@]}" << 'PYEOF'
import hashlib
import json
import os
import sys

host_root, pack_root, tier = sys.argv[1], sys.argv[2], sys.argv[3]
style_errors, redundancy_open = int(sys.argv[4]), int(sys.argv[5])
docs = sys.argv[6:]

VENDOR_FILES = [
    "scripts/spec-style-lint.py",
    "scripts/spec-redundancy-precheck.py",
    "scripts/spec-freeze.py",
    "scripts/gate_common.py",
    "guardrails/check-freeze.sh",
]


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


vendored_sha = {rel: sha256_of(os.path.join(host_root, rel)) for rel in VENDOR_FILES}

# The scaffold kit's files, where the host carries them, join the manifest (the design-review
# recommendation of 2026-07-16: one source-pin mechanism covers both installable kits, so the
# update watcher reads one file). Informational pins; this installer never vendors them.
SCAFFOLD_NAMES = ("check_completeness.py", "check_tests_present.py",
                  "check_traces_to_spec.py", "check_conflicts.py", "gate_lib.py")
for d in ("scaffold/guardrails", "guardrails"):
    for name in SCAFFOLD_NAMES:
        rel = os.path.join(d, name)
        p = os.path.join(host_root, rel)
        if os.path.isfile(p) and rel not in vendored_sha:
            vendored_sha[rel] = sha256_of(p)
pack_version = open(os.path.join(pack_root, "VERSION"), encoding="utf-8").read().strip()

scripts_dir = os.path.join(host_root, "scripts")
tests_dir = os.path.join(host_root, "tests")
os.makedirs(scripts_dir, exist_ok=True)
os.makedirs(tests_dir, exist_ok=True)

manifest = {
    "pack_version": pack_version,
    "vendored": vendored_sha,
    "seeded": {"style_errors": style_errors, "redundancy_open": redundancy_open},
    "tier": tier,
}
with open(os.path.join(scripts_dir, "ratchet-manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)
    f.write("\n")
print("wrote scripts/ratchet-manifest.json")

cap = {"max_waivers": 0, "max_redundancy_open": redundancy_open, "max_style_errors": style_errors}
with open(os.path.join(scripts_dir, "spec-debt-cap.json"), "w", encoding="utf-8") as f:
    json.dump(cap, f, indent=2)
    f.write("\n")
print("wrote scripts/spec-debt-cap.json (max_style_errors=%d max_redundancy_open=%d)"
      % (style_errors, redundancy_open))

LOCK_TEST_TEMPLATE = '''"""tests/test_ratchet_lock.py — generated by adopt/install-ratchet.sh (SPEC INV-172). Do not hand-edit
the SEEDED_* constants; they are the size measured at adoption time. The ratchet only ever tightens:
the suite reds when a gated doc grows past the seeded size, and reds when scripts/spec-debt-cap.json
is raised past what was seeded here — raising a cap for real means editing this file, on purpose,
reviewed.
"""
import json
import os
import subprocess

SEEDED_STYLE_ERRORS = {seeded_style_errors}
SEEDED_REDUNDANCY_OPEN = {seeded_redundancy_open}
GATED_DOCS = {gated_docs!r}
TIER = {tier!r}


def _host_root():
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True
    )
    return out.stdout.strip()


def _cap():
    root = _host_root()
    with open(os.path.join(root, "scripts", "spec-debt-cap.json"), encoding="utf-8") as f:
        return json.load(f)


def test_caps_never_raised_past_seed():
    cap = _cap()
    assert cap["max_style_errors"] <= SEEDED_STYLE_ERRORS, (
        "max_style_errors raised above the seeded %d — raising the cap for real means editing "
        "this generated test" % SEEDED_STYLE_ERRORS)
    assert cap["max_redundancy_open"] <= SEEDED_REDUNDANCY_OPEN, (
        "max_redundancy_open raised above the seeded %d — raising the cap for real means editing "
        "this generated test" % SEEDED_REDUNDANCY_OPEN)
    assert cap["max_waivers"] <= 0


def test_style_errors_within_cap():
    root = _host_root()
    cap = _cap()
    total = 0
    for doc in GATED_DOCS:
        out = subprocess.run(
            ["python3", os.path.join(root, "scripts", "spec-style-lint.py"), "--tier", TIER,
             os.path.join(root, doc)],
            capture_output=True, text=True,
        )
        last_line = out.stdout.strip().splitlines()[-1]
        total += json.loads(last_line)["errors"]
    assert total <= cap["max_style_errors"], (
        "style errors grew to %d, above the cap %d" % (total, cap["max_style_errors"]))


def test_redundancy_open_within_cap():
    root = _host_root()
    cap = _cap()
    total = 0
    for doc in GATED_DOCS:
        out = subprocess.run(
            ["python3", os.path.join(root, "scripts", "spec-redundancy-precheck.py"),
             os.path.join(root, doc)],
            capture_output=True, text=True,
        )
        last_line = out.stdout.strip().splitlines()[-1]
        total += json.loads(last_line)["open"]
    assert total <= cap["max_redundancy_open"], (
        "redundancy-open grew to %d, above the cap %d" % (total, cap["max_redundancy_open"]))
'''

lock_test = LOCK_TEST_TEMPLATE.format(
    seeded_style_errors=style_errors,
    seeded_redundancy_open=redundancy_open,
    gated_docs=list(docs),
    tier=tier,
)
with open(os.path.join(tests_dir, "test_ratchet_lock.py"), "w", encoding="utf-8") as f:
    f.write(lock_test)
print("wrote tests/test_ratchet_lock.py")
PYEOF

# --- step f: wire (or recommend) the pre-push gate ------------------------------------------------
PRE_PUSH="$HOST_ROOT/guardrails/pre-push"
if [ -f "$PRE_PUSH" ]; then
  if grep -q "gate r — ratchet caps" "$PRE_PUSH"; then
    echo "already wired: guardrails/pre-push gate r — ratchet caps"
  else
    {
      echo ""
      echo "echo \"\""
      echo "echo \"-- gate r — ratchet caps --\""
      echo "if ! python3 -m pytest -q tests/test_ratchet_lock.py; then"
      echo "  fail=1"
      echo "fi"
    } >> "$PRE_PUSH"
    echo "wired: guardrails/pre-push gate r — ratchet caps"
  fi
else
  echo "no guardrails/pre-push found — add this recipe to your own push gate:"
  echo "  echo \"-- gate r — ratchet caps --\""
  echo "  python3 -m pytest -q tests/test_ratchet_lock.py || fail=1"
fi

# --- step g: final summary -------------------------------------------------------------------------
python3 - "$STYLE_ERRORS" "$REDUNDANCY_OPEN" "${#VENDOR_FILES[@]}" "${DOCS[@]}" << 'PYEOF'
import json, sys

style_errors, redundancy_open, vendored = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
docs = sys.argv[4:]
print(json.dumps({
    "severity": "ok",
    "code": "ratchet-install",
    "docs": docs,
    "style_errors": style_errors,
    "redundancy_open": redundancy_open,
    "vendored": vendored,
}))
PYEOF
