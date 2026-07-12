"""The chat laws' mechanical voice (row 141, SPEC INV-28 delivery).

The language law (plain words talk, codes only trail) and the narration law
(beats name wish+station, station ends digest, long silence owes a heartbeat)
live in skills a window may never load — so a prompt hook injects a one-line
reminder into every prompt on the working machine. The skills stay the laws'
homes; the hook only reminds. This test proves the script on disk, the line it
speaks, and that the one installer covers both session hooks (clock + laws).

Zero dependencies beyond the stdlib; run from the repo root:
  python3 -m unittest discover tests -v
"""

import os
import subprocess
import unittest

from conftest import ROOT
SCRIPT = os.path.join(ROOT, "scripts", "chat-law-hook.sh")
INSTALLER = os.path.join(ROOT, "scripts", "install-session-hooks.sh")


class TestChatLawHookScript(unittest.TestCase):
    def test_script_exists_and_executable(self):
        self.assertTrue(os.path.isfile(SCRIPT), "missing script: %s" % SCRIPT)
        self.assertTrue(os.access(SCRIPT, os.X_OK), "%s is not executable" % SCRIPT)

    def test_output_carries_both_laws(self):
        result = subprocess.run([SCRIPT], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        out = result.stdout
        for needle in (
            "plain product words",          # the language law's positive side
            "trail in parentheses",         # codes never lead
            "wish",                          # narration identity: which wish
            "station",                       # narration identity: which station
            "digest",                        # station-end digest
            "10 minutes",                    # the heartbeat threshold
        ):
            self.assertIn(needle, out, "law line missing: %r" % needle)

    def test_output_carries_the_no_scissors_law(self):
        result = subprocess.run([SCRIPT], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        out = result.stdout
        for needle in (
            "its own positive sentence",     # say what a thing IS
            "contrast frame",                # the banned shape, named
            "banned in every text",          # the scope
            "language.no-scissors",          # the law's home stays the profile
        ):
            self.assertIn(needle, out, "no-scissors line missing: %r" % needle)

    def test_output_carries_the_routing_law(self):
        result = subprocess.run([SCRIPT], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        out = result.stdout
        for needle in (
            "orchestrator seat",
            "cheapest sufficient tier",
            "locate their own anchors",
            "SPEC INV-69",
        ):
            self.assertIn(needle, out, "routing line missing: %r" % needle)

    def test_installer_covers_both_hooks(self):
        self.assertTrue(os.path.isfile(INSTALLER), "missing installer: %s" % INSTALLER)
        self.assertTrue(os.access(INSTALLER, os.X_OK), "%s is not executable" % INSTALLER)
        body = open(INSTALLER).read()
        for needle in ("clock-hook.sh", "chat-law-hook.sh", "UserPromptSubmit"):
            self.assertIn(needle, body, "installer missing: %r" % needle)


if __name__ == "__main__":
    unittest.main()
