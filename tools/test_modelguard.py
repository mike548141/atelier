"""Tests for modelguard.py, the PreToolUse hook that blocks a Claude session
or subagent started with no model. Each case runs the hook as Claude Code
does: a JSON payload on stdin, a deny decision (or nothing) on stdout."""
import json
import os
import subprocess
import sys
import unittest

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modelguard.py")

# (expect_block, tool, input); every path and repo name is fictional.
CASES = [
    (True, "Bash", 'claude -p "do x"'),
    (True, "Bash", 'cd ~/src/example-app && claude -p --dangerously-skip-permissions "x" < /dev/null'),
    (True, "Bash", 'nohup claude -p "x" > log 2>&1 &'),
    (True, "Bash", 'FOO=1 /opt/example/bin/claude -r abc -p "go on"'),
    (True, "Bash", 'bash -c "cd x && claude -p hi"'),
    (True, "Bash", 'out=$(claude -p "hi")'),
    (True, "Bash", 'claude --bg "task"'),
    (True, "Bash", 'claude --fallback-model sonnet -p x'),
    (True, "Bash", 'echo hi; claude "summarise"'),
    (True, "Bash", 'claude -p "unbalanced'),
    (False, "Bash", 'claude -p --model claude-sonnet-5-5 "x"'),
    (False, "Bash", 'claude --model=claude-haiku-5-5 -p x'),
    (False, "Bash", 'ANTHROPIC_MODEL=claude-opus-5-5 claude -p x'),
    (False, "Bash", 'cd ~/src/example-app && claude -p --model claude-opus-5-5 --dangerously-skip-permissions < /dev/null'),
    (False, "Bash", 'claude --version'),
    (False, "Bash", 'claude mcp list'),
    (False, "Bash", 'claude plugin update atelier'),
    (False, "Bash", 'claude --help | grep model'),
    (False, "Bash", 'git commit -m "tools: claude -p now needs a model"'),
    (False, "Bash", 'git commit -F - <<EOF\ndocs: note\n\nclaude -p "x" was used\nEOF'),
    (False, "Bash", 'grep -rn "claude -p" docs/'),
    (False, "Bash", 'ls ~/.claude # claude -p'),
    (False, "Bash", 'which claude'),
    (False, "Bash", 'cat <<< "claude -p x"'),
    (True, "Agent", {"prompt": "x", "description": "d"}),
    (False, "Agent", {"prompt": "x", "description": "d", "model": "haiku"}),
    (False, "Agent", {"prompt": "x", "description": "d", "subagent_type": "fork"}),
    (False, "Read", {"file_path": "/x"}),
]


def run(payload):
    return subprocess.run([sys.executable, HOOK], input=payload, capture_output=True, text=True)


class ModelGuard(unittest.TestCase):
    def test_cases(self):
        for expect, tool, inp in CASES:
            ti = {"command": inp} if tool == "Bash" else inp
            with self.subTest(tool=tool, inp=inp):
                r = run(json.dumps({"tool_name": tool, "tool_input": ti}))
                self.assertEqual(r.returncode, 0)
                self.assertEqual(r.stderr, "")
                self.assertEqual('"deny"' in r.stdout, expect)

    def test_a_deny_is_well_formed(self):
        r = run(json.dumps({"tool_name": "Bash", "tool_input": {"command": 'claude -p "x"'}}))
        out = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertEqual((out["hookEventName"], out["permissionDecision"]), ("PreToolUse", "deny"))
        self.assertIn("--model", out["permissionDecisionReason"])

    def test_malformed_payload_never_blocks(self):
        r = run("not json")
        self.assertEqual((r.returncode, r.stdout), (0, ""))


if __name__ == "__main__":
    unittest.main()
