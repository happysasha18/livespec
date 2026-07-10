"""Tiny host test — named smoke.py (not test_*.py) so the pack's own pytest
run never collects fixture-host tests. The tests-present check only looks at
paths under tests_dir, not filenames."""


def check_revenue():
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
    import app
    assert app.revenue() == 42
