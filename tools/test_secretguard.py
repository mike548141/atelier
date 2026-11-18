"""Tests for secretguard.py, the PreToolUse hook that refuses a Bash command
which would print a secret file (board 450/010 row 6). Each case runs the hook
as Claude Code does: a JSON payload on stdin, a deny decision (or nothing) on
stdout. Every path, host, container and tool name here is fictional.

The ESTATE cases are the original guard's own selftest, carried over with its
estate paths moved into a repo-level config: the generalisation must block and
allow exactly what the original did once the same paths are configured."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "secretguard.py")

ESTATE_CONFIG = """\
# a fictional service estate's secret paths
/run/secrets/
/srv/vault/docker/secrets/
forwarding.secret
*/periphery/stacks/*.env   # inline comment
pointer: Use tools/config-read.py, which masks credentials.
reader: config-read.py
reader: gamectl.py config show
reveal: --reveal
"""

# (expect_block, command)
ESTATE = [
    (True, "cat /run/secrets/db_password"),
    (True, "ssh h 'sudo docker exec mc cat /server/forwarding.secret'"),
    (True, "sudo cat /srv/vault/docker/secrets/abc-def"),
    (True, "grep pass /srv/ops/periphery/stacks/gaming/.env"),
    (True, "head -c 40 /run/secrets/x | od -c"),
    (False, "grep -c pass /run/secrets/x"),
    (False, "cat /run/secrets/x | sha256sum"),
    (False, "PGPASSWORD=$(cat /run/secrets/db) psql -c 'select 1'"),
    (False, "python3 tools/config-read.py --container mc /server/forwarding.secret"),
    (False, "ls -l /run/secrets/"),
    (False, "cat docs/ROADMAP.md"),
    (False, "git log --oneline"),
    # the bypasses a cold pass measured on the original, each blocked ...
    (True, "cat /run/secrets/x # config-read.py"),
    (True, "echo config-read.py; cat /run/secrets/x"),
    (True, "config-read.py --key k --reveal f | cat"),
    (True, "python3 tools/config-read.py --key k --reveal /run/secrets/x | tee /tmp/x"),
    # ... and their near relatives
    (True, "python3 tools/config-read.py --key k --reveal f.yaml | cat"),
    (True, "python3 tools/config-read.py --key k --reveal f.yaml |& less"),
    (True, "nice -n 19 /usr/bin/python3 tools/config-read.py --key k --reveal f.yaml | xargs echo"),
    (True, "python3 tools/config-read.py --key k --reveal f.yaml >&2"),
    (True, "python3 tools/config-read.py --key k --reveal f.yaml > >(cat)"),
    (True, "tools/gamectl.py config show mc-home /data/x.yml --key k --reveal | cat"),
    (True, "cat /run/secrets/x; python3 tools/config-read.py f"),
    (True, "python3 -c 'import os' tools/config-read.py; cat /run/secrets/x"),
    (True, "tools/gamectl.py rcon mc-home cat /server/forwarding.secret"),
    # ... while the legitimate forms still pass
    (False, "python3 tools/config-read.py stacks/proxy-config/proxy.toml"),
    (False, "tools/config-read.py --key proxies.proxy.secret /data/x.yml"),
    (False, "nice -n 19 python3 tools/config-read.py --selftest"),
    (False, "/usr/bin/python3 -I tools/config-read.py /run/secrets/x"),
    (False, "cd /x && python3 tools/config-read.py --container mc /run/secrets/db"),
    (False, "python3 tools/config-read.py --container mc-proxy /server/forwarding.secret --reveal"
            " | sha256sum | cut -c1-8"),
    (False, "python3 tools/config-read.py --key k --reveal f.yaml 2>/dev/null | sha256sum"),
    (False, "tools/gamectl.py config show mc-home /data/x.yml --key proxy.secret --reveal | sha256sum"),
    (False, "docker logs proxy 2>&1 | tools/config-read.py -"),
    (False, "python3 tools/config-read.py --key tail /data/x.yml"),
]

# The built-in set alone: no config file anywhere.
DEFAULTS = [
    (True, "cat .env"),
    (True, "grep API_KEY config/.env.production"),
    (True, "tail -n 5 deploy/stack.env"),
    (True, "cat ~/.ssh/id_ed25519"),
    (True, "head certs/server.key"),
    (True, "cat /etc/ssl/private/privkey1.pem"),
    (True, "cat ~/.aws/credentials"),
    (True, "cat /run/secrets/db"),
    (True, "bash -c 'cat .env'"),
    (True, "cat ./*.env"),
    (False, "cat .env.example"),
    (False, "cat config/.env.sample"),
    (False, "cat ~/.ssh/id_ed25519.pub"),
    (False, "cat certs/fullchain.pem"),
    (False, "cat credentials.json"),
    (False, "cat package.json"),
    (False, "cat .envrc"),
    (False, "grep -q API_KEY .env"),
    (False, "grep -l API_KEY -r ."),
    (False, "rg -c API_KEY .env"),
    (False, "rg -n API_KEY --glob '!*.env' ."),
    (False, "sed -i 's/old/new/' .env"),
    (False, "sed --in-place 's/old/new/' .env"),
    (False, "sha256sum .env"),
    (False, "cat .env | wc -l"),
    (False, "ls -la .env"),
    (False, "git commit -F - <<EOF\ndocs: never cat .env\n\ncat .env printed it once\nEOF"),
    (False, "cat > notes.md <<'EOF'\nrun: grep KEY .env\nEOF"),
]


class Base(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.root = os.path.realpath(self.t.name)
        self.ud = os.path.join(self.root, "claude")   # an empty user config dir
        self.repo = os.path.join(self.root, "repo")
        os.makedirs(self.ud)
        os.makedirs(self.repo)
        self.env = {k: v for k, v in os.environ.items() if k != "SECRETGUARD_PATHS"}
        self.env["CLAUDE_CONFIG_DIR"] = self.ud

    def tearDown(self):
        self.t.cleanup()

    def write(self, rel, text):
        p = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)
        return p

    def run_hook(self, payload, cwd=None):
        return subprocess.run([sys.executable, HOOK], input=payload, capture_output=True,
                              text=True, env=self.env, cwd=cwd or self.root, timeout=20)

    def bash(self, cmd, cwd=None, payload_cwd=None):
        payload = {"tool_name": "Bash", "tool_input": {"command": cmd},
                   "cwd": payload_cwd or cwd or self.repo}
        r = self.run_hook(json.dumps(payload), cwd=cwd)
        self.assertEqual((r.returncode, r.stderr), (0, ""))
        return r.stdout

    def assert_cases(self, cases, **kw):
        for expect, cmd in cases:
            with self.subTest(cmd=cmd):
                self.assertEqual('"deny"' in self.bash(cmd, **kw), expect)


class EstateConfig(Base):
    def setUp(self):
        super().setUp()
        self.write("repo/.atelier/secret-paths", ESTATE_CONFIG)

    def test_original_cases(self):
        self.assert_cases(ESTATE)

    def test_found_from_a_subdirectory(self):
        sub = os.path.join(self.repo, "a", "b")
        os.makedirs(sub)
        self.assertIn('"deny"', self.bash("sudo cat /srv/vault/docker/secrets/x", cwd=sub))

    def test_payload_cwd_wins_over_process_cwd(self):
        # The process runs outside the repo; the payload says where the session is.
        self.assertIn('"deny"', self.bash("cat /server/forwarding.secret",
                                          cwd=self.root, payload_cwd=self.repo))
        self.assertEqual(self.bash("cat /server/forwarding.secret", cwd=self.root,
                                   payload_cwd=self.ud), "")

    def test_deny_is_well_formed_and_carries_the_pointer(self):
        out = json.loads(self.bash("cat /run/secrets/db"))["hookSpecificOutput"]
        self.assertEqual((out["hookEventName"], out["permissionDecision"]), ("PreToolUse", "deny"))
        reason = out["permissionDecisionReason"]
        self.assertIn("Use tools/config-read.py, which masks credentials.", reason)
        self.assertIn("/run/secrets/", reason)          # the pattern that matched
        self.assertIn(".atelier/secret-paths", reason)  # where it came from

    def test_reveal_without_a_configured_flag_is_not_judged(self):
        self.write("repo/.atelier/secret-paths", ESTATE_CONFIG.replace("reveal: --reveal\n", ""))
        self.assertEqual(self.bash("config-read.py --key k --reveal f | cat"), "")


class BuiltInDefaults(Base):
    def test_defaults_alone(self):
        self.assert_cases(DEFAULTS)

    def test_defaults_off(self):
        self.write("repo/.atelier/secret-paths", "defaults: off\n/run/secrets/\n")
        self.assertEqual(self.bash("cat .env"), "")
        self.assertIn('"deny"', self.bash("cat /run/secrets/db"))

    def test_repo_exemption(self):
        self.write("repo/.atelier/secret-paths", "!fixtures/*.env\n")
        self.assertEqual(self.bash("cat tests/fixtures/demo.env"), "")
        self.assertIn('"deny"', self.bash("cat deploy/demo.env"))

    def test_default_pointer(self):
        reason = json.loads(self.bash("cat .env"))["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("masks credentials", reason)
        self.assertIn("built-in default", reason)


class UserLevel(Base):
    def test_claude_config_dir_file(self):
        self.write("claude/secretguard-paths", "*.vault\npointer: Use the vault reader.\n")
        reason = json.loads(self.bash("cat x/app.vault"))["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("Use the vault reader.", reason)

    def test_explicit_env_file(self):
        p = self.write("elsewhere/paths", "*.vault\n")
        self.env["SECRETGUARD_PATHS"] = p
        self.assertIn('"deny"', self.bash("cat x/app.vault"))

    def test_repo_pointer_beats_user_pointer(self):
        self.write("claude/secretguard-paths", "pointer: USER POINTER\n")
        self.write("repo/.atelier/secret-paths", "pointer: REPO POINTER\n")
        reason = json.loads(self.bash("cat .env"))["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("REPO POINTER", reason)
        self.assertNotIn("USER POINTER", reason)


class NeverBlocksOnBadInput(Base):
    def test_malformed_payloads(self):
        for payload in ("not json", "[]", "null", json.dumps({"tool_input": {"command": 7}}),
                        json.dumps({"tool_name": "Bash"})):
            with self.subTest(payload=payload):
                r = self.run_hook(payload)
                self.assertEqual((r.returncode, r.stdout, r.stderr), (0, "", ""))

    def test_other_tools_pass(self):
        r = self.run_hook(json.dumps({"tool_name": "Read", "tool_input": {"command": "cat .env"},
                                      "cwd": self.repo}))
        self.assertEqual((r.returncode, r.stdout), (0, ""))

    def test_unreadable_config_falls_back(self):
        os.makedirs(os.path.join(self.repo, ".atelier", "secret-paths"))   # a dir, not a file
        os.makedirs(os.path.join(self.ud, "secretguard-paths"))
        self.assertIn('"deny"', self.bash("cat .env"))                     # defaults still hold

    def test_payload_cwd_missing_on_disk(self):
        self.assertEqual(self.bash("ls", payload_cwd=os.path.join(self.root, "gone")), "")


class Cli(Base):
    def cli(self, *args):
        return subprocess.run([sys.executable, HOOK, *args], capture_output=True, text=True,
                              env=self.env, cwd=self.repo, timeout=20)

    def test_try(self):
        self.write("repo/.atelier/secret-paths", ESTATE_CONFIG)
        r = self.cli("--try", "cat /run/secrets/x")
        self.assertEqual(r.returncode, 1)
        self.assertIn("Refused", r.stdout)
        r = self.cli("--try", "cat README.md")
        self.assertEqual((r.returncode, r.stdout.strip()), (0, "allowed"))

    def test_show(self):
        self.write("repo/.atelier/secret-paths", ESTATE_CONFIG)
        out = self.cli("--show").stdout
        for want in ("built-in defaults", "secret  forwarding.secret", "exempt  .env.example",
                     "reader  gamectl.py config show", "reveal  --reveal",
                     "pointer: Use tools/config-read.py"):
            self.assertIn(want, out)


if __name__ == "__main__":
    unittest.main()
