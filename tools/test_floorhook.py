"""Tests for floorhook.py, the SessionStart hook that says at session open
whether a child's atelier pin and floor copy are current. Each case runs the hook
as Claude Code does (a JSON payload with `cwd` on stdin, one JSON object or
nothing on stdout) against synthetic fixtures only: a throwaway "atelier" (a git
repo with a local bare origin, the real pins.py and its helpers copied in) and a
throwaway child stamped with that floor. No real sibling repo, no network."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

TOOLS = os.path.dirname(os.path.abspath(__file__))
HOOK = os.path.join(TOOLS, "floorhook.py")
PINS_FILES = ["pins.py", "estate.py", "stampscan.py", "filewalk.py", "allowmarker.py", "report.py"]
FLOOR = [
    "## Doctrine — inherited from atelier (pinned `atelier@<SHA>`)",
    "",
    "- **Rule one:** keep the safety rule verbatim.",
    "- **Source & drift:** canonical doctrine is `<atelier-path>/docs/method/`.",
    "- **This repo's visibility:** <visibility fact>.",
]


def propagation(region):
    return "# PROPAGATION\n\nprose\n\n<!-- floor:begin -->\n```markdown\n%s\n```\n<!-- floor:end -->\n\ntail\n" % "\n".join(region)


def filled(region, sha):
    return ("\n".join(region).replace("<SHA>", sha[:7]).replace("<atelier-path>", "../atelier")
            .replace("<visibility fact>", "PRIVATE by design"))


def stamped(body):
    return ("# child\n\n<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor -->\n%s\n"
            "<!-- stamp:end -->\n" % body)


class Fixture(unittest.TestCase):
    def setUp(self):
        self.base = tempfile.mkdtemp(prefix="floorhook-test-")
        self.addCleanup(shutil.rmtree, self.base, True)
        self.env = {k: v for k, v in os.environ.items()
                    if not k.startswith(("ATELIER_", "GIT_", "FLOORHOOK_"))}
        self.env.update(HOME=self.base, GIT_CONFIG_NOSYSTEM="1")

    def git(self, cwd, *args):
        r = subprocess.run(["git", "-c", "user.name=Test", "-c", "user.email=" + "t" + chr(64) + "example.invalid",
                            "-c", "commit.gpgsign=false", "-C", cwd, *args],
                           capture_output=True, text=True, env=self.env)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout.strip()

    def write(self, root, rel, text):
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as f:
            f.write(text)

    def commit(self, root, msg):
        self.git(root, "add", "-A")
        self.git(root, "commit", "-q", "-m", msg)

    def atelier(self, name="atelier"):
        d = os.path.join(self.base, name)
        bare = os.path.join(self.base, name + ".git")
        os.makedirs(os.path.join(d, "tools"))
        for f in PINS_FILES:
            shutil.copy(os.path.join(TOOLS, f), os.path.join(d, "tools", f))
        self.write(d, "docs/method/PROPAGATION.md", propagation(FLOOR))
        self.git(self.base, "init", "-q", "--bare", "-b", "main", bare)
        self.git(d, "init", "-q", "-b", "main")
        self.git(d, "remote", "add", "origin", bare)
        self.commit(d, "floor v1")
        self.git(d, "push", "-q", "-u", "origin", "main")
        self.sha = self.git(d, "rev-parse", "HEAD")
        return d

    def child(self, body, name="child", claude=None):
        d = os.path.join(self.base, name)
        os.makedirs(d)
        self.git(d, "init", "-q", "-b", "main")
        self.write(d, "CLAUDE.md", claude if claude is not None else stamped(body))
        self.commit(d, "claude")
        return d

    def advance(self, a, region=None):
        self.write(a, "docs/method/other.md", "x\n")
        self.commit(a, "unrelated change")
        if region:
            self.write(a, "docs/method/PROPAGATION.md", propagation(region))
            self.commit(a, "floor v2")
        self.git(a, "push", "-q", "origin", "main")

    def run_hook(self, cwd, a=None, hook=HOOK, extra=None, stdin=None):
        env = dict(self.env)
        if a:
            env["ATELIER_TOOLS"] = os.path.join(a, "tools")
        env.update(extra or {})
        payload = stdin if stdin is not None else json.dumps(
            {"hook_event_name": "SessionStart", "source": "startup", "cwd": cwd})
        t0 = time.time()
        r = subprocess.run([sys.executable, hook], input=payload, capture_output=True,
                           text=True, env=env, cwd=self.base, timeout=60)
        self.assertEqual(r.returncode, 0, "the hook must always exit 0: " + r.stderr)
        self.assertEqual(r.stderr, "")
        out = json.loads(r.stdout) if r.stdout.strip() else None
        ctx = ((out or {}).get("hookSpecificOutput") or {}).get("additionalContext", "")
        return out, ctx, (out or {}).get("systemMessage", ""), time.time() - t0

    def standin_hook(self):
        """A copy of the hook in a place no atelier checkout is found from."""
        d = os.path.join(self.base, "lone", "tools")
        os.makedirs(d)
        shutil.copy(HOOK, d)
        return os.path.join(d, "floorhook.py")


class Verdicts(Fixture):
    def test_current_says_one_line_to_the_user_and_nothing_to_the_model(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, self.sha))
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assertEqual(ctx, "")
        self.assertIn("is current with origin/main; floor copy identical", msg)
        self.assertNotIn("hookSpecificOutput", out)

    def test_behind_with_the_floor_unchanged_is_one_quiet_line(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, self.sha))
        self.advance(a)
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assertIn("1 commit(s) behind origin/main; floor unchanged since the pin", ctx)
        self.assertNotIn("FLOOR OUT OF DATE", ctx)
        self.assertEqual(msg, "")

    def test_behind_and_the_floor_moved_is_loud(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, self.sha))
        self.advance(a, [l.replace("verbatim", "verbatim, always") for l in FLOOR])
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assertIn("FLOOR OUT OF DATE", ctx)
        self.assertIn("and the safety floor has changed since the pin", ctx)
        self.assertIn("floor v2", ctx)                      # the commits the child would inspect
        self.assertTrue(msg.startswith("⚠️ FLOOR OUT OF DATE"))

    def test_a_floor_copy_that_differs_is_loud_even_with_a_current_pin(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, self.sha).replace("keep the safety rule verbatim", "keep it, roughly"))
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assertIn("FLOOR OUT OF DATE", ctx)
        self.assertIn("floor copy differs from atelier's floor at the pin", ctx)
        self.assertNotIn("is current", ctx + msg)

    def test_a_pin_atelier_does_not_know_is_loud(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, "abcdef0123456789"))
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assertIn("FLOOR OUT OF DATE", ctx)
        self.assertIn("pin abcdef0 is not a commit in the atelier checkout", ctx)

    def test_the_hook_runs_from_a_subdirectory_of_the_child(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, self.sha).replace("verbatim", "loosely"))
        os.makedirs(os.path.join(c, "src", "deep"))
        out, ctx, msg, _ = self.run_hook(os.path.join(c, "src", "deep"), a)
        self.assertIn("FLOOR OUT OF DATE", ctx)


class Silent(Fixture):
    def test_atelier_itself_is_silent(self):
        a = self.atelier()
        out, ctx, msg, _ = self.run_hook(a, a)
        self.assertIsNone(out)

    def test_a_repo_that_pins_nothing_is_silent(self):
        a = self.atelier()
        c = self.child("", name="plain", claude="# plain\n\nno pin here\n")
        self.assertIsNone(self.run_hook(c, a)[0])

    def test_a_repo_with_no_claude_md_is_silent(self):
        a = self.atelier()
        c = os.path.join(self.base, "bare")
        os.makedirs(c)
        self.git(c, "init", "-q", "-b", "main")
        self.assertIsNone(self.run_hook(c, a)[0])

    def test_a_directory_that_is_no_git_repo_is_silent(self):
        a = self.atelier()
        d = os.path.join(self.base, "notrepo")
        os.makedirs(d)
        self.assertIsNone(self.run_hook(d, a)[0])


class NoResult(Fixture):
    def assert_no_result(self, out, ctx, msg, reason):
        self.assertIn("no result: ", ctx)
        self.assertIn(reason, ctx)
        self.assertIn("NOT checked", ctx)
        self.assertNotIn("is current", ctx + msg)
        self.assertTrue(msg.startswith("floorhook: no result"))

    def test_no_atelier_checkout_is_no_result(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, self.sha))
        out, ctx, msg, _ = self.run_hook(c, None, hook=self.standin_hook(),
                                         extra={"ATELIER_TOOLS": os.path.join(self.base, "nowhere", "tools")})
        self.assert_no_result(out, ctx, msg, "no atelier checkout found")

    def test_a_failed_fetch_is_no_result_with_pins_own_reason(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, self.sha))
        self.git(a, "remote", "set-url", "origin", os.path.join(self.base, "gone.git"))
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assert_no_result(out, ctx, msg, "pins.py exited 2")

    def stand_in(self, body):
        a = self.atelier("standin")
        with open(os.path.join(a, "tools", "pins.py"), "w") as f:
            f.write(body)
        return a

    def test_a_hang_is_no_result_inside_the_time_limit(self):
        a = self.stand_in("import time\ntime.sleep(60)\n")
        c = self.child(filled(FLOOR, self.sha))
        out, ctx, msg, secs = self.run_hook(c, a, extra={"FLOORHOOK_TIMEOUT": "1"})
        self.assertLess(secs, 15)
        self.assert_no_result(out, ctx, msg, "did not finish within 1.0 s")

    def test_unparseable_output_is_no_result(self):
        a = self.stand_in('print("all is well")\n')
        c = self.child(filled(FLOOR, self.sha))
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assert_no_result(out, ctx, msg, "printed nothing readable")

    def test_an_unknown_status_is_no_result(self):
        a = self.stand_in('import json\nprint(json.dumps({"children":[{"status":"fine"}]}))\n')
        c = self.child(filled(FLOOR, self.sha))
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assert_no_result(out, ctx, msg, "a status floorhook does not know")

    def test_a_crashing_pins_is_no_result(self):
        a = self.stand_in("raise SystemExit(7)\n")
        c = self.child(filled(FLOOR, self.sha))
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assert_no_result(out, ctx, msg, "pins.py exited 7")


class Contract(Fixture):
    def test_the_atelier_checkout_can_come_from_git_config(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, self.sha).replace("verbatim", "loosely"))
        self.git(c, "config", "hooks.atelierTools", os.path.join(a, "tools"))
        out, ctx, msg, _ = self.run_hook(c, None, hook=self.standin_hook())
        self.assertIn("FLOOR OUT OF DATE", ctx)

    def test_it_exits_zero_on_garbage_and_empty_stdin(self):
        for stdin in ("", "not json", "[1,2]", "null", '{"cwd": 5}', '{"cwd": "/no/such/dir"}'):
            with self.subTest(stdin=stdin):
                self.run_hook(self.base, None, stdin=stdin)

    def test_stdout_is_one_json_object_or_nothing(self):
        a = self.atelier()
        c = self.child(filled(FLOOR, self.sha).replace("verbatim", "loosely"))
        r = subprocess.run([sys.executable, HOOK], input=json.dumps({"cwd": c}), capture_output=True,
                           text=True, env={**self.env, "ATELIER_TOOLS": os.path.join(a, "tools")})
        obj = json.loads(r.stdout)
        self.assertEqual(obj["hookSpecificOutput"]["hookEventName"], "SessionStart")
        self.assertEqual(r.stdout.count("\n"), 1)

    def test_a_hook_with_hostile_detail_text_stays_on_one_line(self):
        a = self.atelier("evil")
        with open(os.path.join(a, "tools", "pins.py"), "w") as f:
            f.write('import json\nprint(json.dumps({"children":[{"status":"current","pin":"abc1234",'
                    '"copy":"drift","copy_detail":"line one\\nline two\\x1b[31m"}]}))\n')
        c = self.child(filled(FLOOR, self.sha))
        out, ctx, msg, _ = self.run_hook(c, a)
        self.assertIn("FLOOR OUT OF DATE", ctx)
        self.assertNotIn("\x1b", ctx)
        self.assertNotIn("\n", ctx)


if __name__ == "__main__":
    unittest.main()
