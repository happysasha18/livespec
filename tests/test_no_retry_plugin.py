"""INV-155 — the mechanical net. A flaky owned test is a defect fixed at its
root, never masked by a retry or rerun-until-green plugin. This guardrail greps
the repo's test configuration for such a mask and reds if one is ever added; the
repo uses none today, so it passes now. Landed 2026-07-15."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The config homes a mask would live in — only those that exist are read.
CONFIG_FILES = ["pytest.ini", "setup.cfg", "pyproject.toml", "tox.ini"]

# Retry / rerun-until-green masks a flaky test must never hide behind.
MASK_SUBSTRINGS = [
    "rerunfailures",
    "--reruns",
    "reruns=",
    "pytest-retry",
    "@flaky",
    "flaky(",
]


def _config_texts():
    homes = list(CONFIG_FILES)
    homes += [p.name for p in ROOT.glob("requirements*.txt")]
    for rel in homes:
        path = ROOT / rel
        if path.exists():
            yield rel, path.read_text(encoding="utf-8")


def test_no_retry_plugin():
    offences = []
    for rel, text in _config_texts():
        for needle in MASK_SUBSTRINGS:
            if needle in text:
                offences.append(f"{rel}: {needle}")
    assert not offences, (
        "a retry/rerun-until-green mask must never hide an owned flake "
        "(INV-155); found: " + "; ".join(offences)
    )
