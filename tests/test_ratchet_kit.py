"""tests/test_ratchet_kit.py — the turnkey ratchet-adoption kit (SPEC INV-172) and the canonical
hook home (SPEC INV-173).

Two things under test: hooks/scissors-scan.py (the pack's own copy of the scissors Stop-hook,
universal tier only, with a personal-overlay hook and a quoted-demo skip) and adopt/install-ratchet.sh
(vendors the style/redundancy/freeze gates into a host repo and seeds a debt cap the host's own
CURRENT size, generating a lock test that only ever tightens).
"""
import hashlib
import json
import os
import subprocess
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOK = os.path.join(ROOT, "hooks", "scissors-scan.py")
INSTALL_PACK_HOOKS = os.path.join(ROOT, "scripts", "install-pack-hooks.sh")
INSTALL_RATCHET = os.path.join(ROOT, "adopt", "install-ratchet.sh")


def run(args, cwd=None, extra_env=None, input_text=None):
    env = dict(os.environ)
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        args, cwd=cwd or ROOT, capture_output=True, text=True, env=env, input=input_text,
    )


def _write_transcript(tmp, lines):
    """Write a Stop-hook transcript .jsonl with one assistant text turn."""
    path = os.path.join(tmp, "transcript.jsonl")
    text = "\n".join(lines)
    ev = {"type": "assistant", "message": {"content": [{"type": "text", "text": text}]}}
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(ev) + "\n")
    return path


def _stop_payload(transcript_path):
    return json.dumps({"transcript_path": transcript_path, "stop_hook_active": False})


class TestCanonicalHook(unittest.TestCase):
    def test_canonical_hook_exists_with_universal_patterns_only(self):
        self.assertTrue(os.path.isfile(HOOK), "hooks/scissors-scan.py must ship")
        body = open(HOOK, encoding="utf-8").read()
        self.assertIn(r",\s+not\s+\S", body)
        self.assertIn(r"\s+—\s+not\s+\S", body)
        self.assertNotIn("а не", body)
        self.assertNotIn("но не", body)

    def test_hook_skips_quoted_demos(self):
        with tempfile.TemporaryDirectory() as tmp:
            transcript = _write_transcript(tmp, ["the «X — not Y» frame is banned"])
            result = run(["python3", HOOK], input_text=_stop_payload(transcript))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(result.stdout.strip(), "", "quoted demo must not fire the block")

            transcript2 = _write_transcript(tmp, ["this is good — not bad"])
            result2 = run(["python3", HOOK], input_text=_stop_payload(transcript2))
            self.assertIn('"decision": "block"', result2.stdout)

    def test_hook_reads_personal_overlay(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = os.path.join(tmp, "home")
            hooks_dir = os.path.join(home, ".claude", "hooks")
            os.makedirs(hooks_dir)
            overlay = os.path.join(hooks_dir, "scissors-personal.json")
            with open(overlay, "w", encoding="utf-8") as f:
                json.dump([r",\s+а\s+не\s+\S"], f)

            transcript = _write_transcript(tmp, ["свежий, а не недельный"])

            result = run(
                ["python3", HOOK],
                extra_env={"HOME": home},
                input_text=_stop_payload(transcript),
            )
            self.assertIn('"decision": "block"', result.stdout)

            # without the overlay (a HOME with no scissors-personal.json), no block.
            home2 = os.path.join(tmp, "home2")
            os.makedirs(os.path.join(home2, ".claude", "hooks"))
            result2 = run(
                ["python3", HOOK],
                extra_env={"HOME": home2},
                input_text=_stop_payload(transcript),
            )
            self.assertEqual(result2.returncode, 0)
            self.assertEqual(result2.stdout.strip(), "")


class TestInstaller(unittest.TestCase):
    def test_installer_dry_run_touches_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = os.path.join(tmp, "home")
            os.makedirs(home)
            result = run(
                ["bash", INSTALL_PACK_HOOKS, "--dry-run"],
                extra_env={"HOME": home},
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertFalse(
                os.path.exists(os.path.join(home, ".claude", "hooks", "scissors-scan.py"))
            )


class TestRatchetInstall(unittest.TestCase):
    VENDOR_FILES = (
        "scripts/spec-style-lint.py",
        "scripts/spec-redundancy-precheck.py",
        "scripts/spec-freeze.py",
        "scripts/gate_common.py",
        "guardrails/check-freeze.sh",
    )

    def _init_host(self, tmp):
        run(["git", "init", "-q"], cwd=tmp)
        run(["git", "config", "user.email", "a@example.com"], cwd=tmp)
        run(["git", "config", "user.name", "a"], cwd=tmp)

    def _measured_style_errors(self, doc_path):
        result = run(["python3", os.path.join(ROOT, "scripts", "spec-style-lint.py"),
                       "--tier", "universal", doc_path])
        last_line = result.stdout.strip().splitlines()[-1]
        return json.loads(last_line)["errors"]

    def _write_doc(self, tmp):
        doc = os.path.join(tmp, "DOC.md")
        with open(doc, "w", encoding="utf-8") as f:
            f.write(
                "# Test doc\n\n"
                "The output is good — not bad quality.\n\n"
                "The result is good — not bad quality.\n"
            )
        return doc

    def test_ratchet_install_seeds_at_current_size(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_host(tmp)
            doc = self._write_doc(tmp)
            expected = self._measured_style_errors(doc)
            self.assertGreater(expected, 0, "fixture doc must trip at least one style error")

            result = run(["bash", INSTALL_RATCHET, "DOC.md"], cwd=tmp)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

            for rel in self.VENDOR_FILES:
                self.assertTrue(os.path.isfile(os.path.join(tmp, rel)), "missing vendored: %s" % rel)

            manifest_path = os.path.join(tmp, "scripts", "ratchet-manifest.json")
            self.assertTrue(os.path.isfile(manifest_path))
            manifest = json.load(open(manifest_path, encoding="utf-8"))
            pack_version = open(os.path.join(ROOT, "VERSION"), encoding="utf-8").read().strip()
            self.assertEqual(manifest["pack_version"], pack_version)
            for rel in self.VENDOR_FILES:
                actual_sha = hashlib.sha256(open(os.path.join(tmp, rel), "rb").read()).hexdigest()
                self.assertEqual(manifest["vendored"][rel], actual_sha)

            cap_path = os.path.join(tmp, "scripts", "spec-debt-cap.json")
            self.assertTrue(os.path.isfile(cap_path))
            cap = json.load(open(cap_path, encoding="utf-8"))
            self.assertEqual(cap["max_style_errors"], expected)

            lock_test = os.path.join(tmp, "tests", "test_ratchet_lock.py")
            self.assertTrue(os.path.isfile(lock_test))

            result2 = run(["python3", "-m", "pytest", "-q", "tests/test_ratchet_lock.py"], cwd=tmp)
            self.assertEqual(result2.returncode, 0, result2.stdout + result2.stderr)

    def test_ratchet_lock_reds_on_growth(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_host(tmp)
            doc = self._write_doc(tmp)
            run(["bash", INSTALL_RATCHET, "DOC.md"], cwd=tmp)

            with open(doc, "a", encoding="utf-8") as f:
                f.write("\nOne more line, good — not bad quality.\n")

            result = run(["python3", "-m", "pytest", "-q", "tests/test_ratchet_lock.py"], cwd=tmp)
            self.assertNotEqual(result.returncode, 0, "lock test must red on doc growth")

    def test_ratchet_lock_reds_on_cap_raise(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_host(tmp)
            self._write_doc(tmp)
            run(["bash", INSTALL_RATCHET, "DOC.md"], cwd=tmp)

            cap_path = os.path.join(tmp, "scripts", "spec-debt-cap.json")
            cap = json.load(open(cap_path, encoding="utf-8"))
            cap["max_style_errors"] = cap["max_style_errors"] + 5
            with open(cap_path, "w", encoding="utf-8") as f:
                json.dump(cap, f)

            result = run(["python3", "-m", "pytest", "-q", "tests/test_ratchet_lock.py"], cwd=tmp)
            self.assertNotEqual(result.returncode, 0, "lock test must red on a bare cap raise")


if __name__ == "__main__":
    unittest.main()
