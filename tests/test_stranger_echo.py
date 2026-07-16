"""The stranger arm's echo-and-close law (INV-147/INV-27) — M-337.

M-337 asserts a captured stranger wish is answered on its source too, not just harvested:
the capture echo posted as a comment on the source Issue at harvest, the Issue closed once
its row reaches a terminal exit — extending M-289's no-wish close (a no-wish item is closed
with a recorded note) to the yes-wish case.
"""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def test_stranger_yes_wish_echoes_and_closes_source():
    spec = (REPO / "PRODUCT_SPEC.md").read_text()
    # INV-147's body clause: the captured wish's echo lands as a comment on the source Issue
    # at harvest, and the Issue closes once its row reaches a terminal exit.
    assert "comment on the source Issue" in spec
    assert "at harvest" in spec
    assert "closed once its row reaches a terminal exit" in spec
    # INV-27's body clause carries the bridged-stranger pointer to that same echo.
    assert "bridged in from a stranger's Issue" in spec
