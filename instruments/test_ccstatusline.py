"""Tests for instruments/ccstatusline (board 450/010 row 5)."""
import json
import os
import subprocess
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "ccstatusline")


class StatusLine(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.stub = os.path.join(self.tmp.name, "ccusage")
        with open(self.stub, "w") as f:
            f.write("#!/bin/sh\n[ \"$1\" = statusline ] || exit 9\ncat >/dev/null\nprintf STUB\n")
        os.chmod(self.stub, 0o755)

    def tearDown(self):
        self.tmp.cleanup()

    def run_tool(self, model, **env):
        e = dict(os.environ, CCUSAGE=self.stub, **env)
        payload = json.dumps({"model": {"id": model}}) if model is not None else "{}"
        r = subprocess.run([TOOL], input=payload, capture_output=True, text=True, env=e, timeout=20)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout

    def test_build_model_is_silent(self):
        self.assertEqual(self.run_tool("claude-opus-5-5"), "STUB")

    def test_review_model_shouts(self):
        out = self.run_tool("claude-fable-5-2")
        self.assertIn("FABLE — REVIEW MODEL, NOT OPUS", out)
        self.assertTrue(out.endswith("STUB"))

    def test_other_model_named(self):
        self.assertIn("claude-sonnet-5-5 (not opus)", self.run_tool("claude-sonnet-5-5"))

    def test_no_model_no_guess(self):
        self.assertEqual(self.run_tool(None), "STUB")

    def test_build_model_is_configurable(self):
        self.assertEqual(self.run_tool("claude-sonnet-5-5", ATELIER_BUILD_MODEL="sonnet"), "STUB")
        self.assertIn("(not sonnet)", self.run_tool("claude-opus-5-5", ATELIER_BUILD_MODEL="sonnet"))

    def test_help(self):
        r = subprocess.run([TOOL, "--help"], capture_output=True, text=True, timeout=20)
        self.assertIn("ATELIER_BUILD_MODEL", r.stdout)


if __name__ == "__main__":
    unittest.main()
