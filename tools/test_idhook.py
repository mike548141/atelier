"""Tests for tools/idhook.py (board 210/490)."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "idhook.py")
SID = "00000000-1111-2222-3333-444444444444"


class IdHook(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.ud = os.path.join(self.t.name, "claude")
        os.makedirs(os.path.join(self.ud, "sessions"))
        self.env = dict(os.environ, CLAUDE_CONFIG_DIR=self.ud)
        self.env.pop("CLAUDE_CODE_SESSION_ID", None)

    def tearDown(self):
        self.t.cleanup()

    def record(self, pid, sid, name):
        with open(os.path.join(self.ud, "sessions", "%d.json" % pid), "w") as f:
            json.dump({"pid": pid, "sessionId": sid, "name": name}, f)

    def hook(self, payload):
        r = subprocess.run([sys.executable, HOOK], input=payload, capture_output=True,
                           text=True, env=self.env, timeout=20)
        self.assertEqual(r.returncode, 0)
        return r.stdout.strip()

    def test_both_ids_shown(self):
        self.record(7, "someone-else", "other-1a")
        self.record(9, SID, "atelier-df")
        out = json.loads(self.hook(json.dumps(
            {"session_id": SID, "transcript_path": "/x/%s.jsonl" % SID})))
        msg = out["systemMessage"]
        self.assertIn("Messaging name: atelier-df", msg)
        self.assertIn("Transcript id: %s" % SID, msg)
        self.assertIn("/x/%s.jsonl" % SID, msg)
        self.assertIn("first line of your first reply, before any other text",
                      out["hookSpecificOutput"]["additionalContext"])

    def test_missing_name_is_said_not_guessed(self):
        out = json.loads(self.hook(json.dumps({"session_id": SID})))
        self.assertIn("not yet assigned", out["systemMessage"])
        self.assertIn(SID, out["systemMessage"])

    def test_bad_stdin_never_errors(self):
        self.assertEqual(self.hook("not json"), "")


if __name__ == "__main__":
    unittest.main()
