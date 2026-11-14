"""Tests for ccfleet: the gate's decision, prompt rendering and its guards,
result harvesting, and end-to-end runs of `run`, `drive` and `drain` against a
throwaway git repo with a local bare remote and a stand-in `claude` binary.
No network, no real Claude session. Every repo name here is fictional."""
import importlib.machinery
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "ccfleet")
_loader = importlib.machinery.SourceFileLoader("ccfleet", TOOL)
_spec = importlib.util.spec_from_loader("ccfleet", _loader)
cf = importlib.util.module_from_spec(_spec)
_loader.exec_module(cf)

# A stand-in for `claude -p`: records its argv, cwd and stdin, then prints the
# JSON shape `--output-format json` prints.
FAKE_CLAUDE = textwrap.dedent("""\
    #!{py}
    import json, os, sys
    stdin = sys.stdin.read()
    rec = {{"argv": sys.argv[1:], "cwd": os.getcwd(), "stdin": stdin}}
    with open(os.environ["FAKE_CLAUDE_LOG"], "a") as f:
        f.write(json.dumps(rec) + "\\n")
    print(json.dumps({{"session_id": "sess-" + os.path.basename(os.getcwd()),
                      "result": "did the work\\nRESULT: " + os.environ.get("FAKE_RESULT", "DONE")}}))
    """)

# A stand-in review queue: serves the lines of a file, one per `next`, skipping
# what the launched list already holds.
FAKE_QUEUE = textwrap.dedent("""\
    #!{py}
    import sys
    cmd, rest = sys.argv[1], sys.argv[2:]
    root = {root!r}
    if cmd == "next":
        with open(rest[0]) as f:
            launched = set(f.read().splitlines())
        with open(root + "/queue.txt") as f:
            lines = f.read().splitlines()
        for line in lines:
            if line and line not in launched:
                print(line); break
    else:
        with open(root + "/" + cmd + ".log", "a") as f:
            f.write(" ".join(rest) + "\\n")
    """)


def wr(path, text, mode="w"):
    with open(path, mode) as f:
        f.write(text)


def rd(path):
    with open(path) as f:
        return f.read()


GIT_ID = ["-c", "user.name=t", "-c", "user.email=t@example.com"]  # leakscan:allow:email: a fictional identity for throwaway test commits


def sh(*args, cwd=None):
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout


class Gate(unittest.TestCase):
    g = {"max_load": 24, "min_mem_pct": 25, "min_disk_gb": 20}

    def r(self, l1=1, l5=1, mem=50, disk=100):
        return {"load": (l1, l5, 1), "mem_pct": mem, "disk_gb": disk}

    def test_headroom_goes(self):
        self.assertTrue(cf.gate_ok(self.g, self.r()))

    def test_each_reading_holds(self):
        for kw in ({"l1": 30}, {"l5": 24}, {"mem": 10}, {"disk": 5}):
            self.assertFalse(cf.gate_ok(self.g, self.r(**kw)), kw)

    def test_unreadable_memory_holds_unless_disabled(self):
        self.assertFalse(cf.gate_ok(self.g, self.r(mem=None)))
        self.assertTrue(cf.gate_ok({**self.g, "min_mem_pct": 0}, self.r(mem=None)))


class Render(unittest.TestCase):
    cfg = {"private_names": ["secret-root"], "repos": {"hidden": {"visibility": "private"}}}

    def test_fills_known_and_reports_unfilled(self):
        out, left = cf.render("a {REPO} b {MISSING} c {lower} d", {"REPO": "x"})
        self.assertEqual(out, "a x b {MISSING} c {lower} d")
        self.assertEqual(left, ["MISSING"])

    def test_private_names_blocked_for_public_and_unknown(self):
        text = "see secret-root and hidden here"
        for vis in ("PUBLIC", "UNKNOWN"):
            self.assertEqual(cf.private_hits(self.cfg, text, vis), ["hidden", "secret-root"])
        self.assertEqual(cf.private_hits(self.cfg, text, "PRIVATE"), [])

    def test_private_name_match_is_whole_word(self):
        self.assertEqual(cf.private_hits(self.cfg, "unhidden secret-rooted", "PUBLIC"), [])


class Harvest(unittest.TestCase):
    def test_reads_json_after_a_warning_line(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as f:
            f.write('warning: something\n{"session_id": "s1", "result": "x\\nRESULT: BUDGET EXHAUSTED at act 1"}')
        self.addCleanup(os.remove, f.name)
        _, sid, res = cf.harvest(f.name)
        self.assertEqual((sid, res), ("s1", "BUDGET EXHAUSTED"))

    def test_no_result_line_is_unknown(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as f:
            f.write("usage limit reached")
        self.addCleanup(os.remove, f.name)
        self.assertEqual(cf.harvest(f.name)[2], "UNKNOWN")


class EndToEnd(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ccfleet-")
        t = self.tmp
        for d in ("src", "remotes", "wt", "kit"):
            os.makedirs(os.path.join(t, d))
        self.repos = ["alpha", "beta"]
        for r in self.repos:
            bare = os.path.join(t, "remotes", r + ".git")
            sh("git", "init", "-q", "--bare", "-b", "main", bare)
            prim = os.path.join(t, "src", r)
            sh("git", "clone", "-q", bare, prim)
            sh("git", *GIT_ID, "commit", "-q",
               "--allow-empty", "-m", "init", cwd=prim)
            os.makedirs(os.path.join(prim, "docs"))
            wr(os.path.join(prim, "docs", "brief.md"), "brief\n")
            sh("git", "add", "docs/brief.md", cwd=prim)
            sh("git", *GIT_ID, "commit", "-q", "-m", "b", cwd=prim)
            sh("git", "push", "-q", "origin", "HEAD:main", cwd=prim)
            sh("git", "remote", "set-head", "origin", "main", cwd=prim)
        self.claude = os.path.join(t, "claude")
        wr(self.claude, FAKE_CLAUDE.format(py=sys.executable))
        self.queue = os.path.join(t, "queue")
        wr(self.queue, FAKE_QUEUE.format(py=sys.executable, root=t))
        for p in (self.claude, self.queue):
            os.chmod(p, 0o755)
        self.prompt = os.path.join(t, "prompt.md")
        wr(self.prompt, "Work on {REPO} ({VIS}) in {WT}. {ASK} {LANDING}\n")
        self.cfg = {
            "kit_dir": os.path.join(t, "kit"), "repos_root": os.path.join(t, "src"),
            "worktrees_root": os.path.join(t, "wt"), "default_model": "model-default",
            "claude_bin": self.claude, "claude_args": ["--dangerously-skip-permissions"], "nice": 0,
            "stagger_seconds": 0, "poll_seconds": 0.1,
            "gate": {"max_load": 10**6, "min_mem_pct": 0, "min_disk_gb": 0},
            "private_names": ["secret-root"], "vars": {"ASK": "Make it healthy."},
            "repos": {"alpha": {"visibility": "public", "model": "model-alpha"},
                      "beta": {"visibility": "private"}},
            "pass_prompt": self.prompt, "pass_model": "model-pass",
            "queue": {"next": [self.queue, "next", "{LAUNCHED}"],
                      "take": [self.queue, "take", "{REPO}:{ITEM}", "{BRIEF}"],
                      "release": [self.queue, "release", "{REPO}:{ITEM}"]},
        }
        self.cfgpath = os.path.join(t, "cfg.json")
        self.write_cfg()
        self.env = {**os.environ, "FAKE_CLAUDE_LOG": os.path.join(t, "claude.log")}

    def tearDown(self):
        for r in self.repos:
            subprocess.run(["git", "worktree", "prune"], cwd=os.path.join(self.tmp, "src", r))
        subprocess.run(["rm", "-rf", self.tmp])

    def write_cfg(self):
        wr(self.cfgpath, json.dumps(self.cfg))

    def cli(self, *args, env=None):
        return subprocess.run([sys.executable, TOOL, "--config", self.cfgpath, "--by", "orch-1", *args],
                              capture_output=True, text=True, env=env or self.env, timeout=120)

    def calls(self):
        p = os.path.join(self.tmp, "claude.log")
        return [json.loads(l) for l in rd(p).splitlines()] if os.path.exists(p) else []

    def test_run_bills_the_repo_and_cleans_up(self):
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("result=DONE", r.stdout)
        (call,) = self.calls()
        self.assertEqual(os.path.basename(call["cwd"]), "alpha")  # the billing key
        self.assertEqual(call["stdin"], "")  # stdin was /dev/null
        argv = call["argv"]
        self.assertEqual(argv[argv.index("--model") + 1], "model-alpha")
        self.assertIn("Make it healthy.", argv[-1])
        self.assertIn("(PUBLIC)", argv[-1])
        self.assertFalse(os.path.exists(call["cwd"]), "worktree left behind")
        day = os.listdir(os.path.join(self.tmp, "kit", "results"))[0]
        res = rd(os.path.join(self.tmp, "kit", "results", day, "alpha.md"))
        self.assertIn("<!-- session sess-alpha -->", res)

    def test_run_in_an_existing_worktree_keeps_it(self):
        wt = os.path.join(self.tmp, "wt", "pass-0101", "beta")
        os.makedirs(os.path.dirname(wt))
        sh("git", "worktree", "add", "-q", "--detach", wt, "origin/main", cwd=os.path.join(self.tmp, "src", "beta"))
        r = self.cli("run", "beta", "--prompt", self.prompt, "--in", wt)
        self.assertEqual(r.returncode, 0, r.stderr)
        (call,) = self.calls()
        self.assertEqual(os.path.realpath(call["cwd"]), os.path.realpath(wt))
        self.assertTrue(os.path.isdir(wt), "an adopted worktree is the caller's to remove")
        r = self.cli("run", "alpha", "--prompt", self.prompt, "--in", wt)
        self.assertEqual(r.returncode, cf.EXIT_SETUP, "basename must be the repo: it is the billing key")

    def test_public_prompt_naming_a_private_name_is_refused(self):
        self.cfg["vars"]["ASK"] = "as done in secret-root"
        self.write_cfg()
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, cf.EXIT_GUARD)
        self.assertIn("secret-root", r.stderr)
        self.assertEqual(self.calls(), [])
        self.assertEqual(os.listdir(os.path.join(self.tmp, "wt")), [])

    def test_unfilled_placeholder_is_refused(self):
        wr(self.prompt, mode="a", text="{NOPE}\n")
        r = self.cli("run", "beta", "--prompt", self.prompt)
        self.assertEqual(r.returncode, cf.EXIT_GUARD)
        self.assertIn("{NOPE}", r.stderr)

    def test_reset_reached_starts_nothing(self):
        self.cfg["reset_utc"] = "2000-01-01T00:00"
        self.write_cfg()
        r = self.cli("run", "beta", "--prompt", self.prompt)
        self.assertEqual(r.returncode, cf.EXIT_RESET)
        self.assertEqual(self.calls(), [])

    def test_dry_run_launches_nothing(self):
        r = self.cli("run", "beta", "--prompt", self.prompt, "--dry-run")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("< /dev/null", r.stdout)
        self.assertEqual(self.calls(), [])

    def test_drive_runs_every_job_then_resumes_by_skipping(self):
        jobs = os.path.join(self.tmp, "jobs.tsv")
        task = os.path.join(self.tmp, "task.md")
        wr(task, "Line one.\nLine two.\n")
        wr(jobs, f"# comment\nalpha\talpha\t{self.prompt}\n"
                              f"beta\tbeta-one\t{self.prompt}\tMODEL=model-x\n"
                              f"beta\tbeta-two\t{self.prompt}\tASK=Other ask.\n"
                              f"alpha\talpha-task\t{self.prompt}\tASK=@file:{task}\n")
        r = self.cli("drive", jobs, "--max", "3", "--serial-per-repo")
        self.assertIn("ASK=@file:", rd(jobs))
        self.assertEqual(r.returncode, 0, r.stderr)
        calls = self.calls()
        self.assertEqual(sorted(os.path.basename(c["cwd"]) for c in calls), ["alpha", "alpha", "beta", "beta"])
        models = {c["argv"][c["argv"].index("--model") + 1] for c in calls}
        self.assertEqual(models, {"model-alpha", "model-x", "model-default"})
        self.assertTrue(any("Other ask." in c["argv"][-1] for c in calls))
        self.assertTrue(any("Line one.\nLine two." in c["argv"][-1] for c in calls), "@file: not read")
        r = self.cli("drive", jobs)
        self.assertEqual(len(self.calls()), 4, "a re-run must skip jobs with a result today")
        log = rd(os.path.join(self.tmp, "kit", "driver.log"))
        self.assertIn("skip beta-two", log)
        # serial per repo: the second beta job starts only after the first ends
        self.assertLess(log.index("done beta-one"), log.index("start beta-two"))

    def test_drain_takes_runs_and_releases_until_empty(self):
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\nbeta 020 docs/brief.md\n")
        wr(self.prompt, "Pass {ITEM} brief {BRIEF} in {WT}\n")
        r = self.cli("drain", "--max", "2")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("DRAIN EXIT: queue empty", r.stdout)
        self.assertEqual(sorted(rd(os.path.join(self.tmp, "take.log")).split()),
                         sorted(["alpha:010", "beta:020", "docs/brief.md", "docs/brief.md"]))
        self.assertEqual(sorted(rd(os.path.join(self.tmp, "release.log")).split()),
                         ["alpha:010", "beta:020"])
        self.assertEqual({c["argv"][c["argv"].index("--model") + 1] for c in self.calls()}, {"model-pass"})

    def test_drain_stops_after_three_unclean_ends_and_keeps_claims(self):
        wr(os.path.join(self.tmp, "queue.txt"), 
            "".join(f"beta {n:03d} docs/brief.md\n" for n in range(1, 6)))
        wr(self.prompt, "Pass {ITEM}\n")
        r = self.cli("drain", "--max", "1", env={**self.env, "FAKE_RESULT": "FAILED"})
        self.assertIn("DRAIN EXIT: failures", r.stdout)
        self.assertEqual(len(self.calls()), 3)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "release.log")))
        # an unclean pass keeps its worktree for a resume
        self.assertEqual(len(os.listdir(os.path.join(self.tmp, "wt"))), 3)


if __name__ == "__main__":
    unittest.main()
