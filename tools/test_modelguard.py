"""Tests for modelguard.py, the PreToolUse hook that blocks a Claude session
or subagent started with no model. Each case runs the hook as Claude Code
does: a JSON payload on stdin, a deny decision (or nothing) on stdout.

BYPASSES is the recurrence-prevention table (cold pass 160/1450, FL7): every
launch shape found to slip past the hook goes in it, and stays. LOOKUPS is the
other side (board 210/500): commands that only find, read or name the binary
must never be refused, or sessions learn to route round the guard."""
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
    (True, "Agent", {"prompt": "x", "description": "d", "subagent_type": "general-purpose"}),
    (True, "Task", {"prompt": "x", "description": "d"}),
    (False, "Task", {"prompt": "x", "description": "d", "model": "sonnet"}),
    (False, "Agent", {"prompt": "x", "description": "d", "model": "haiku"}),
    (False, "Agent", {"prompt": "x", "description": "d", "subagent_type": "fork"}),
    (False, "Read", {"file_path": "/x"}),
]

# Launches with no model that an earlier parse let through (FL7, probe P12).
# Each must be denied. Grow this table with every bypass found.
BYPASSES = [
    'for r in a b; do claude -p "x"; done',
    'if true; then claude -p x; fi',
    'while true; do claude -p x; break; done',
    'timeout 600 claude -p x',
    'timeout -s KILL 60 claude -p x',
    'stdbuf -oL claude -p x',
    'nice -n 10 claude -p x',
    'caffeinate -i claude -p x',
    'bash -lc "claude -p x"',
    "zsh -ic 'claude -p x'",
    'eval "claude -p x"',
    'find . -maxdepth 0 -exec claude -p x \\;',
    'sudo -u someone claude -p x',
    'out=`claude -p hi`',
    'out="$(claude -p hi)"',
    '{ claude -p x; }',
    '! claude -p x',
    'echo a#b; claude -p x',
    'echo ANTHROPIC_MODEL= ; claude -p x',
    'ANTHROPIC_MODEL= claude -p x',
    'bash <<EOF\nclaude -p x\nEOF',
    'cat <<EOF | sh\nclaude -p x\nEOF',
    'bash <<< "claude -p x"',
    "printf 'claude -p x' | bash",
    'echo $((1<<2))\nclaude -p x',
    'claude -p "update"',
    'claude -c "update"',
    'claude -p x --model',
    'claude -p x --model=',
    'C=claude; $C -p x',
    '"$CLAUDE_BIN" -p x',
    'npx @anthropic-ai/claude-code -p x',
    'npx -y claude -p x',
    'npm exec -- claude -p x',
    'xargs -I{} claude -p {}',
    'env -S "claude -p x"',
    '"$(command -v claude)" -p x',
    '$(which claude) -p x',
    'some-unknown-wrapper --flag claude -p x',
    '</dev/null claude -p x',
]

# Commands that only look up, read or name the binary (210/500), and launches
# that do name a model. Each must pass.
LOOKUPS = [
    'command -v claude',
    'ls ~/.local/bin/claude ; command -v claude',
    'command -V claude',
    'type claude',
    'type -a claude',
    'which -a claude',
    'whence claude',
    'hash claude',
    'ls -la "$(command -v claude)"',
    'readlink "$(which claude)"',
    'stat $(which claude)',
    'test -x ~/.local/bin/claude && echo ok',
    'pgrep -fl claude',
    'find . -name claude',
    'for f in claude other; do echo "$f"; done',
    'npm install -g @anthropic-ai/claude-code',
    'echo $((1<<2)); claude --version',
    'claude -p x \\\n--model claude-sonnet-5-5',
    'claude update',
    'export ANTHROPIC_MODEL=claude-opus-5-5; claude -p x',
    'env ANTHROPIC_MODEL=claude-opus-5-5 claude -p x',
    'bash -lc "claude -p --model claude-haiku-5-5 x"',
    'timeout 600 claude -p --model claude-opus-5-5 x',
    'sudo -u someone claude doctor',
    'git commit -m "$(cat <<\'EOF\'\nnote: claude -p x\nEOF\n)"',
    "echo '$(claude -p x)'",
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

    def check(self, cmd, expect):
        with self.subTest(cmd=cmd):
            r = run(json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}}))
            self.assertEqual((r.returncode, r.stderr), (0, ""))
            self.assertEqual('"deny"' in r.stdout, expect, r.stdout)

    def test_every_known_bypass_is_denied(self):
        for cmd in BYPASSES:
            self.check(cmd, True)

    def test_a_lookup_of_the_binary_passes(self):
        for cmd in LOOKUPS:
            self.check(cmd, False)

    def test_a_deny_is_well_formed(self):
        r = run(json.dumps({"tool_name": "Bash", "tool_input": {"command": 'claude -p "x"'}}))
        out = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertEqual((out["hookEventName"], out["permissionDecision"]), ("PreToolUse", "deny"))
        self.assertIn("--model", out["permissionDecisionReason"])

    def test_malformed_payload_never_blocks(self):
        for payload in ("not json", "[1, 2]", '"text"',
                        json.dumps({"tool_name": "Bash", "tool_input": "claude -p x"}),
                        json.dumps({"tool_name": "Bash", "tool_input": {"command": ["claude", "-p"]}}),
                        json.dumps({"tool_name": "Agent", "tool_input": None})):
            with self.subTest(payload=payload):
                r = run(payload)
                self.assertEqual((r.returncode, r.stdout, r.stderr), (0, "", ""))

    def test_the_reason_states_no_approval_rule(self):
        # FL18: whether a tier needs the principal's approval is the adopter's
        # own rule, not atelier doctrine, so the hook's reason does not state one.
        r = run(json.dumps({"tool_name": "Agent", "tool_input": {"prompt": "x"}}))
        reason = json.loads(r.stdout)["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertNotIn("approval", reason)


if __name__ == "__main__":
    unittest.main()
