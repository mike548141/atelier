"""Tests for tools/prefixhook.py (board 450/010 row 3)."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prefixhook.py")


class PrefixHook(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.ud = os.path.join(self.t.name, "claude")
        self.repo = os.path.join(self.t.name, "repo")
        os.makedirs(os.path.join(self.ud, "skills", "atelier"))
        os.makedirs(os.path.join(self.ud, "skills", "synced"))
        os.makedirs(self.repo)
        subprocess.run(["git", "init", "-q", self.repo], check=True)
        self.env = dict(os.environ, CLAUDE_CONFIG_DIR=self.ud)

    def tearDown(self):
        self.t.cleanup()

    def hook(self):
        r = subprocess.run([sys.executable, HOOK], input=json.dumps({"cwd": self.repo}),
                           capture_output=True, text=True, env=self.env, timeout=20)
        self.assertEqual(r.returncode, 0)
        return r.stdout.strip()

    def check(self):
        return subprocess.run([sys.executable, HOOK, "--check", self.repo],
                              capture_output=True, text=True, env=self.env, timeout=20)

    def test_clean_is_silent(self):
        self.assertEqual(self.hook(), "")
        self.assertEqual(self.check().returncode, 0)

    def test_user_skill_outside_prefix(self):
        os.makedirs(os.path.join(self.ud, "skills", "estate-health"))
        out = json.loads(self.hook())
        self.assertIn("/estate-health (~/.claude/skills)", out["systemMessage"])
        self.assertIn("MECHANISMS.md", out["hookSpecificOutput"]["additionalContext"])
        self.assertEqual(self.check().returncode, 1)

    def test_user_command_and_repo_skill(self):
        os.makedirs(os.path.join(self.ud, "commands"))
        open(os.path.join(self.ud, "commands", "tidy.md"), "w").close()
        os.makedirs(os.path.join(self.repo, ".claude", "skills", "local"))
        msg = json.loads(self.hook())["systemMessage"]
        self.assertIn("/tidy (~/.claude/commands)", msg)
        self.assertIn("/local (repo/.claude/skills)", msg)

    def test_bad_stdin_never_errors(self):
        r = subprocess.run([sys.executable, HOOK], input="not json", capture_output=True,
                           text=True, env=self.env, timeout=20)
        self.assertEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
