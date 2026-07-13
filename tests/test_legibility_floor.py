"""INV-139 — the legibility floor: min contrast ratio + min text size, checked at the pre-show gate.
Landed 2026-07-13."""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "preshow-legibility-lint.py"
FIX = ROOT / "tests" / "fixtures"


def _run(path):
    return subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)


def test_red_fixture_flagged():
    r = _run(FIX / "legibility_red.html")
    assert r.returncode == 1, r.stdout + r.stderr
    assert "low-contrast" in r.stdout
    assert "small-text" in r.stdout


def test_green_fixture_passes():
    r = _run(FIX / "legibility_green.html")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "OK (preshow-legibility)" in r.stdout


def test_contrast_math():
    import importlib.util
    spec = importlib.util.spec_from_file_location("leg", SCRIPT)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    # black vs white is 21:1
    assert round(mod.contrast((0, 0, 0), (255, 255, 255)), 1) == 21.0


def test_spec_clause_and_index():
    spec = (ROOT / "PRODUCT_SPEC.md").read_text(encoding="utf-8")
    assert "legibility floor" in spec
    assert "[INV-139]" in spec
    assert any(line.startswith("| INV-139 |") for line in spec.splitlines())


def test_design_principle_and_preshow_wired():
    arch = (ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
    assert "legibility floor" in arch
    comm = (ROOT / "skills" / "communicator" / "SKILL.md").read_text(encoding="utf-8")
    assert "preshow-legibility-lint.py" in comm


def test_matrix_row():
    matrix = (ROOT / "TEST_MATRIX.md").read_text(encoding="utf-8")
    assert any(l.startswith("| M-") and "INV-139" in l for l in matrix.splitlines())
