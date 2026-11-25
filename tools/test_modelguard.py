"""Tests for modelguard.py, the PreToolUse hook that blocks a Claude session
or subagent started with no model. Each case runs the hook as Claude Code
does: a JSON payload on stdin, a deny decision (or nothing) on stdout.

BYPASSES is the recurrence-prevention table (cold pass 160/1450, FL7): every
launch shape found to slip past the hook goes in it, and stays. LOOKUPS is the
other side (board 210/500): commands that only find, read or name the binary
must never be refused, or sessions learn to route round the guard. NAMED is the
same side for a `claude` that names a user, a unit, a container or a search
term after a head the hook does not know (cold pass 160/1790, RK9)."""
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
    # 210/570: ssh's remote command is still read as code.
    'ssh host claude -p x',
    "ssh -i k host 'claude -p x'",
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
    # 160/1790, RK15: nine shapes that passed, and their near variants.
    'function f { claude -p hi; }; f',
    'command claude -p update',
    'command -p claude -p update',
    "echo 'claude -p hi' | sudo sh",
    "echo 'claude -p hi' | env bash",
    "printf 'claude -p hi' | sudo -u someone bash -s",
    'python3 -c \'import subprocess; subprocess.run(["claude", "-p", "hi"])\'',
    'python3 -c "import os; os.system(\'claude -p hi\')"',
    'node -e \'require("child_process").execSync("claude -p hi")\'',
    'at now <<EOF\nclaude -p hi\nEOF',
    "echo 'claude -p hi' | at now",
    "git -c alias.x='!claude -p hi' x",
    "git -c core.editor='claude -p' commit",
    'set -- claude -p hi; "$@"',
    'set -- claude -p hi; $1 "$2" "$3"',
    'c=cl; ${c}aude -p hi',
    '${c}aude -p hi',
    # Denied before RK9 too: they pin that its narrowing of the unknown-head
    # rule still reads a launch (each passes if the narrowing over-reaches).
    'function f() { claude -p hi; }; f',
    'at now <<< "claude -p hi"',
    "su - claude -c 'claude -p hi'",
    'somewrapper -u claude --dangerously-skip-permissions "do x"',
    'somewrapper claude "summarise the log"',
    "somewrapper 'claude -p hi'",
]

# Commands that only look up, read or name the binary (210/500), and launches
# that do name a model. Each must pass.
LOOKUPS = [
    # 210/570: a login named claude is data, not the binary.
    "ssh -i k claude@host 'sh -s' < script",
    "ssh -i k -l claude host 'sh -s' < script",
    'ssh claude@host uptime',
    'ssh -o BatchMode=yes claude@host -- ls /srv',
    'scp f claude@host:/tmp/',
    'rsync -a d/ claude@host:/x/',
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
    # RK15's readers stop at a launch that names a model or starts none.
    'python3 -c \'import subprocess; subprocess.run(["claude", "--model", "claude-haiku-5-5", "-p", "hi"])\'',
    "git -c alias.x='!claude --version' x",
    'set -- claude --version; "$@"',
]

# 160/1790, RK9: a `claude` naming a user, a unit, a container or a search term
# after a head the hook does not know. Each must pass; before RK9 each was
# refused, the parse failing closed on any `claude` with a word after it.
NAMED = [
    "su - claude -c 'ls'",
    'docker exec -u claude box ls',
    'runuser -u claude -- ls',
    "psql -U claude -d db -c 'select 1'",
    'mysql -u claude -p',
    'journalctl -u claude -n 50',
    'systemctl status claude --no-pager',
    'tmux new -s claude -d',
    'docker logs claude --tail 5',
    'fd claude src',
    'zgrep claude log.gz',
    'python3 -m pytest -k claude tests',
    'python3 -m pytest -k "claude and not slow" tests',
    'ccrepo claude --json',
    'useradd -m claude -s /bin/zsh',
    "ssh host 'su - claude -c ls'",
    'smbclient -U claude //host/share -c ls',
    'docker run --name claude img',
    'podman logs claude --since 1h',
    'kubectl logs claude -n tools',
    'crontab -u claude -l',
    'pytest tests -k claude -x',
    'cargo test claude -- --nocapture',
    'sudo journalctl -u claude -f',
    "docker exec -it claude sh -c 'ls /data'",
    'ansible claude -m ping',
    "osascript -e 'tell application \"claude\" to quit'",
    'python3 -c \'import shutil; print(shutil.which("claude"))\'',
    # the refusal's own advice, applied to the case still refused below
    'kubectl -n tools logs -c main claude',
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

    def test_a_claude_named_as_data_passes(self):
        for cmd in NAMED:
            self.check(cmd, False)

    def test_a_refusal_says_how_to_rephrase(self):
        # RK9: a positional `claude` followed by `-c` still reads as a launch;
        # the refusal says how to say it when no session was meant, and the
        # rephrased command is in NAMED.
        r = run(json.dumps({"tool_name": "Bash", "tool_input": {
            "command": "kubectl -n tools logs claude -c main"}}))
        reason = json.loads(r.stdout)["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("--model", reason)
        self.assertIn("If no session was meant", reason)
        self.assertIn("option's value", reason)

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
