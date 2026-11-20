"""Tests for ccfleet: the gate's decision, prompt rendering and its guards,
result harvesting, and end-to-end runs of `run`, `drive` and `drain` against a
throwaway git repo with a local bare remote and a stand-in `claude` binary.
No network, no real Claude session. Every repo name here is fictional."""
import importlib.machinery
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "ccfleet")
_loader = importlib.machinery.SourceFileLoader("ccfleet", TOOL)
_spec = importlib.util.spec_from_loader("ccfleet", _loader)
cf = importlib.util.module_from_spec(_spec)
_loader.exec_module(cf)

# A stand-in for `claude -p`: records its argv, cwd, stdin, the environment
# values ccfleet sets and its session id, then prints the JSON shape
# `--output-format json` prints. With FAKE_TRANSCRIPT set, it writes its real
# report (with the RESULT line) to a transcript under $CLAUDE_CONFIG_DIR and
# prints a last turn with none, as a session woken by a background
# notification does.
FAKE_CLAUDE = textwrap.dedent("""\
    #!@PY@
    import datetime, json, os, sys
    stdin = sys.stdin.read()
    rec = {"argv": sys.argv[1:], "cwd": os.getcwd(), "stdin": stdin, "posix_sid": os.getsid(0),
           "ceiling": os.environ.get("CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS"),
           "extra": os.environ.get("FAKE_EXTRA_ENV")}
    with open(os.environ["FAKE_CLAUDE_LOG"], "a") as f:
        f.write(json.dumps(rec) + "\\n")
    sid = "sess-" + os.path.basename(os.getcwd()).replace(" ", "_")
    report = "did the work\\nRESULT: " + os.environ.get("FAKE_RESULT", "DONE")
    if os.environ.get("FAKE_TRANSCRIPT"):
        d = os.path.join(os.environ["CLAUDE_CONFIG_DIR"], "projects", "-enc-" + sid)
        os.makedirs(d, exist_ok=True)
        ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
        with open(os.path.join(d, sid + ".jsonl"), "a") as f:
            for text in (report, "Noted: the background task finished."):
                f.write(json.dumps({"type": "assistant", "timestamp": ts,
                                    "message": {"content": [{"type": "text", "text": text}]}}) + "\\n")
        report = "Noted: the background task finished."
    print(json.dumps({"session_id": sid, "result": report}))
    """)

# A stand-in review queue: serves the lines of a file, one per `next`, skipping
# what the launched list already holds.
FAKE_QUEUE = textwrap.dedent("""\
    #!{py}
    import os, sys
    cmd, rest = sys.argv[1], sys.argv[2:]
    root = {root!r}
    def fields(line):
        return tuple(line.split("\\t") if "\\t" in line else line.split())
    if cmd == "next":
        if os.environ.get("FAKE_QUEUE_RC_NEXT"):
            print("queue tool broke", file=sys.stderr)
            sys.exit(int(os.environ["FAKE_QUEUE_RC_NEXT"]))
        with open(rest[0]) as f:
            launched = {{fields(l) for l in f.read().splitlines()}}
        if os.environ.get("FAKE_QUEUE_IGNORE_LAUNCHED"):
            launched = set()
        with open(root + "/queue.txt") as f:
            lines = f.read().splitlines()
        for line in lines:
            if line and fields(line) not in launched:
                print(line); break
    else:
        with open(root + "/" + cmd + ".log", "a") as f:
            f.write(" ".join(rest) + "\\n")
        sys.exit(int(os.environ.get("FAKE_QUEUE_RC_" + cmd.upper(), "0")))
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


class TranscriptFallback(unittest.TestCase):
    """`claude -p` prints only the last turn; a RESULT written earlier is read
    from the session's transcript under $CLAUDE_CONFIG_DIR."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ccfleet-tr-")
        self.addCleanup(subprocess.run, ["rm", "-rf", self.tmp])
        d = os.path.join(self.tmp, "projects", "-some-worktree")
        os.makedirs(d)
        entries = [
            {"type": "assistant", "timestamp": "2026-01-01T10:00:00.000Z",
             "message": {"content": [{"type": "text", "text": "old run\nRESULT: BUDGET EXHAUSTED"}]}},
            {"type": "user", "timestamp": "2026-01-01T11:00:01.000Z",
             "message": {"content": "RESULT: FAILED (a prompt, not the session's own words)"}},
            {"type": "assistant", "timestamp": "2026-01-01T11:00:02.000Z",
             "message": {"content": [{"type": "text", "text": "report\nRESULT: DONE"}]}},
            {"type": "assistant", "timestamp": "2026-01-01T11:00:03.000Z",
             "message": {"content": [{"type": "text", "text": "Noted."}]}},
        ]
        wr(os.path.join(d, "s-42.jsonl"), "".join(json.dumps(e) + "\n" for e in entries) + "not json\n")
        self.log = os.path.join(self.tmp, "log.json")
        wr(self.log, json.dumps({"session_id": "s-42", "result": "Noted."}))
        patcher = mock.patch.dict(os.environ, {"CLAUDE_CONFIG_DIR": self.tmp})
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_newest_assistant_result_is_taken(self):
        text, sid, res = cf.harvest(self.log)
        self.assertEqual((sid, res), ("s-42", "DONE"))
        self.assertIn("read from the session transcript", text)

    def test_entries_before_the_launch_are_not_read(self):
        self.assertTrue(cf.transcript_result("s-42", since="2026-01-01T11:00:00").endswith("RESULT: DONE"))
        self.assertEqual(cf.transcript_result("s-42", since="2026-01-01T12:00:00"), "")

    def test_no_transcript_stays_unknown(self):
        wr(self.log, json.dumps({"session_id": "s-none", "result": "Noted."}))
        self.assertEqual(cf.harvest(self.log)[2], "UNKNOWN")
        self.assertEqual(cf.transcript_result("../s-42"), "", "a session id is never a path")


class PickParsing(unittest.TestCase):
    def test_tabs_keep_spaces_inside_fields(self):
        self.assertEqual(cf.parse_pick("noise\nbeta\t020\tdocs/the brief.md\n"),
                         ["beta", "020", "docs/the brief.md"])

    def test_no_tab_splits_on_whitespace(self):
        self.assertEqual(cf.parse_pick("alpha 010 docs/brief.md\n\n"), ["alpha", "010", "docs/brief.md"])
        self.assertEqual(cf.parse_pick("\n"), [])


class PacingFiles(unittest.TestCase):
    """The stop file counts only when written after the driver started, and
    <kit_dir>/max is the live ceiling."""

    def setUp(self):
        self.kit = tempfile.mkdtemp(prefix="ccfleet-kit-")
        self.addCleanup(subprocess.run, ["rm", "-rf", self.kit])
        self.cfg = {"kit_dir": self.kit}

    def test_stale_stop_file_is_ignored_and_said_once(self):
        stop = os.path.join(self.kit, "stop")
        wr(stop, "")
        old = time.time() - 3600
        os.utime(stop, (old, old))
        pace = cf.Pacing(self.cfg, 2)
        self.assertFalse(pace.stop())
        self.assertFalse(pace.stop())
        log = rd(os.path.join(self.kit, "driver.log"))
        self.assertEqual(log.count("stop file ignored"), 1)
        new = time.time() + 1
        os.utime(stop, (new, new))  # touched again during the run
        self.assertTrue(pace.stop())

    def test_max_file_is_written_read_live_and_removed(self):
        pace = cf.Pacing(self.cfg, 3)
        path = os.path.join(self.kit, "max")
        self.assertEqual(rd(path).strip(), "3")
        wr(path, "1\n")
        self.assertEqual(pace.max(), 1)
        wr(path, "lots")
        self.assertEqual(pace.max(), 1, "an unreadable value keeps the last good one")
        wr(path, "0")
        self.assertEqual(pace.max(), 0, "0 holds every new start")
        log = rd(os.path.join(self.kit, "driver.log"))
        self.assertIn("max 3 -> 1", log)
        self.assertIn("max file unreadable", log)
        pace.close()
        self.assertFalse(os.path.exists(path))


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
            wr(os.path.join(prim, "docs", "the brief.md"), "a brief whose name has a space\n")
            sh("git", "add", "docs/brief.md", "docs/the brief.md", cwd=prim)
            sh("git", *GIT_ID, "commit", "-q", "-m", "b", cwd=prim)
            sh("git", "push", "-q", "origin", "HEAD:main", cwd=prim)
            sh("git", "remote", "set-head", "origin", "main", cwd=prim)
        self.claude = os.path.join(t, "claude")
        wr(self.claude, FAKE_CLAUDE.replace("@PY@", sys.executable))
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
                      "ranked": [self.queue, "ranked", "{BY}"],
                      "take": [self.queue, "take", "{REPO}:{ITEM}", "{BRIEF}"],
                      "release": [self.queue, "release", "{REPO}:{ITEM}"]},
        }
        self.cfgpath = os.path.join(t, "cfg.json")
        self.write_cfg()
        self.env = {**os.environ, "FAKE_CLAUDE_LOG": os.path.join(t, "claude.log"),
                    "CLAUDE_CONFIG_DIR": os.path.join(t, "claude-config")}

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


    def test_every_launch_sets_the_wait_ceiling_and_the_config_env(self):
        self.cfg["env"] = {"FAKE_EXTRA_ENV": "from-config", "CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS": "600000"}
        self.write_cfg()
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, 0, r.stderr)
        (call,) = self.calls()
        self.assertEqual(call["ceiling"], "0", "the ceiling is always off, whatever the config says")
        self.assertEqual(call["extra"], "from-config")

    def test_a_result_only_in_the_transcript_is_harvested(self):
        r = self.cli("run", "alpha", "--prompt", self.prompt, env={**self.env, "FAKE_TRANSCRIPT": "1"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("result=DONE", r.stdout)
        day = os.listdir(os.path.join(self.tmp, "kit", "results"))[0]
        res = rd(os.path.join(self.tmp, "kit", "results", day, "alpha.md"))
        self.assertIn("read from the session transcript", res)
        self.assertIn("did the work", res)

    def commit_claude_md(self, repo, text):
        prim = os.path.join(self.tmp, "src", repo)
        wr(os.path.join(prim, "CLAUDE.md"), text)
        sh("git", "add", "CLAUDE.md", cwd=prim)
        sh("git", *GIT_ID, "commit", "-q", "-m", "pin", cwd=prim)
        sh("git", "push", "-q", "origin", "HEAD:main", cwd=prim)

    def test_pin_is_resolved_per_repo_or_said_unresolved(self):
        self.commit_claude_md("alpha", "Pinned to atelier@ABC1234 here.\n")
        wr(self.prompt, "Bump {REPO} from {PIN}.\n")
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("PIN abc1234 for alpha (from pins.py)", r.stdout)
        r = self.cli("run", "beta", "--prompt", self.prompt)
        self.assertIn("PIN UNRESOLVED for beta", r.stdout)
        prompts = [c["argv"][-1] for c in self.calls()]
        self.assertEqual(prompts, ["Bump alpha from abc1234.\n", "Bump beta from UNRESOLVED.\n"])
        # with no pins.py to ask, the CLAUDE.md on the mainline answers
        self.cfg["vars"]["ATELIER"] = os.path.join(self.tmp, "no-atelier-here")
        self.write_cfg()
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertIn("PIN abc1234 for alpha (from CLAUDE.md)", r.stdout)
        # a supplied pin is used as given, and nothing is resolved
        r = self.cli("run", "alpha", "--prompt", self.prompt, "--set", "PIN=feed123")
        self.assertNotIn("PIN abc1234", r.stdout)
        self.assertEqual(self.calls()[-1]["argv"][-1], "Bump alpha from feed123.\n")

    def test_drain_splits_on_tabs_and_detaches_its_passes(self):
        wr(os.path.join(self.tmp, "queue.txt"), "beta\t020\tdocs/the brief.md\n")
        wr(self.prompt, "Pass {ITEM} brief {BRIEF} in {WT}\n")
        r = self.cli("drain", "--max", "1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("DRAIN EXIT: queue empty", r.stdout)
        self.assertIn("beta:020 docs/the brief.md", rd(os.path.join(self.tmp, "take.log")))
        self.assertEqual(rd(os.path.join(self.tmp, "release.log")).split(), ["beta:020"])
        (call,) = self.calls()
        self.assertIn("brief docs/the brief.md in", call["argv"][-1])
        self.assertNotEqual(call["posix_sid"], os.getsid(0), "a pass must run in its own session")
        (launched,) = [f for f in os.listdir(os.path.join(self.tmp, "kit")) if f.startswith("launched-")]
        self.assertEqual(rd(os.path.join(self.tmp, "kit", launched)), "beta\t020\tdocs/the brief.md\n")
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "kit", "max")), "the live ceiling is tidied")

    def test_a_pass_and_its_resume_share_one_review_log_path(self):
        wr(os.path.join(self.tmp, "queue.txt"), "beta 160/030 docs/brief.md\n")
        wr(self.prompt, "Log {REVIEW_LOG}\n")
        r = self.cli("drain", env={**self.env, "FAKE_RESULT": "FAILED"})
        self.assertEqual(r.returncode, 0, r.stderr)
        want = os.path.join(self.tmp, "kit", "review-logs", "beta-160-030.md")
        self.assertEqual(self.calls()[0]["argv"][-1], f"Log {want}\n")
        self.assertTrue(os.path.isdir(os.path.dirname(want)))
        (wt,) = [os.path.join(self.tmp, "wt", d, "beta") for d in os.listdir(os.path.join(self.tmp, "wt"))]
        r = self.cli("resume", "beta", wt, "sess-beta", "--prompt", self.prompt, "--item", "160/030")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.calls()[1]["argv"][-1], f"Log {want}\n")

    def test_drain_with_an_empty_queue_exits_4(self):
        wr(os.path.join(self.tmp, "queue.txt"), "")
        r = self.cli("drain")
        self.assertEqual(r.returncode, cf.EXIT_EMPTY, r.stderr)
        self.assertIn("DRAIN EXIT: queue empty", r.stdout)

    def test_a_failing_queue_next_is_not_an_empty_queue(self):
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        r = self.cli("drain", env={**self.env, "FAKE_QUEUE_RC_NEXT": "3"})
        self.assertEqual(r.returncode, cf.EXIT_SETUP, r.stdout + r.stderr)
        self.assertIn("DRAIN EXIT: queue error", r.stdout)
        self.assertIn("queue next failed rc=3: queue tool broke", rd(os.path.join(self.tmp, "kit", "driver.log")))
        self.assertEqual(self.calls(), [])

    def test_an_unranked_queue_starts_nothing(self):
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        r = self.cli("drain", env={**self.env, "FAKE_QUEUE_RC_RANKED": "5"})
        self.assertEqual(r.returncode, cf.EXIT_SETUP, r.stdout + r.stderr)
        self.assertIn("DRAIN EXIT: not ranked", r.stdout)
        self.assertEqual(rd(os.path.join(self.tmp, "ranked.log")), "orch-1\n")
        self.assertEqual(self.calls(), [])
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "take.log")))

    def test_a_drain_config_without_ranked_is_refused(self):
        del self.cfg["queue"]["ranked"]
        self.write_cfg()
        r = self.cli("drain")
        self.assertEqual(r.returncode, cf.EXIT_USAGE, r.stdout + r.stderr)
        self.assertIn("queue.ranked", r.stdout + r.stderr)

    def test_a_fresh_kit_dir_is_made_by_the_driver(self):
        self.cfg["kit_dir"] = os.path.join(self.tmp, "fresh", "kit")
        self.write_cfg()
        wr(os.path.join(self.tmp, "queue.txt"), "")
        r = self.cli("drain")
        self.assertEqual(r.returncode, cf.EXIT_EMPTY, r.stdout + r.stderr)

    def test_a_dry_drain_reads_its_passes_as_ended(self):
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\nbeta 020 docs/brief.md\n")
        r = self.cli("drain", "--max", "1", "--dry-run")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        log = rd(os.path.join(self.tmp, "kit", "driver.log"))
        self.assertNotIn("ended early", log)
        self.assertEqual(log.count("result=DRY"), 2)
        self.assertEqual(self.calls(), [])

    def test_a_queue_offering_a_launched_pass_again_is_not_rerun(self):
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        r = self.cli("drain", "--max", "1", env={**self.env, "FAKE_QUEUE_IGNORE_LAUNCHED": "1"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(len(self.calls()), 1)
        self.assertIn("again, already launched", rd(os.path.join(self.tmp, "kit", "driver.log")))

    def test_a_stale_stop_file_does_not_end_a_new_drain(self):
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        stop = os.path.join(self.tmp, "kit", "stop")
        wr(stop, "")
        old = time.time() - 7 * 86400
        os.utime(stop, (old, old))
        r = self.cli("drain")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(len(self.calls()), 1)
        self.assertIn("stop file ignored", rd(os.path.join(self.tmp, "kit", "driver.log")))

    def test_launched_list_is_keyed_by_the_reset(self):
        self.cfg["reset_utc"] = "2099-01-05T23:00"
        self.write_cfg()
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        self.cli("drain")
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, "kit", "launched-reset-2099-01-05T2300.txt")))

    def test_ended_hook_release_on_and_stop_on(self):
        q = self.cfg["queue"]
        q["take"] = [self.queue, "take", "{REPO}:{ITEM}", "{WT}", "{LOG}"]
        q["ended"] = [self.queue, "ended", "{REPO}:{ITEM}", "{RESULT}", "{SESSION}", "{WT}", "{LOG}"]
        q["release_on"] = ["DONE", "SKIPPED", "REFUSED"]
        q["stop_on"] = ["BUDGET EXHAUSTED", "STOPPED"]
        self.write_cfg()
        wr(os.path.join(self.tmp, "queue.txt"), "beta 001 docs/brief.md\nbeta 002 docs/brief.md\n")
        wr(self.prompt, "Pass {ITEM}\n")
        r = self.cli("drain", "--max", "1", env={**self.env, "FAKE_RESULT": "REFUSED"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(rd(os.path.join(self.tmp, "release.log")).split(), ["beta:001", "beta:002"])
        take = rd(os.path.join(self.tmp, "take.log")).splitlines()[0].split()
        self.assertTrue(take[1].endswith("/beta") and take[2].endswith(".json"), take)
        ended = rd(os.path.join(self.tmp, "ended.log")).splitlines()
        self.assertEqual([l.split()[:3] for l in ended],
                         [["beta:001", "REFUSED", "sess-beta"], ["beta:002", "REFUSED", "sess-beta"]])
        self.assertEqual(os.listdir(os.path.join(self.tmp, "wt")), [], "a released pass loses its worktree")
        for f in ("release.log", "ended.log", "take.log"):
            os.remove(os.path.join(self.tmp, f))
        wr(os.path.join(self.tmp, "queue.txt"), "beta 003 docs/brief.md\nbeta 004 docs/brief.md\n")
        r = self.cli("drain", "--max", "1", env={**self.env, "FAKE_RESULT": "STOPPED"})
        self.assertIn("DRAIN EXIT: result STOPPED", r.stdout)
        self.assertEqual(rd(os.path.join(self.tmp, "ended.log")).split()[:2], ["beta:003", "STOPPED"])
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "release.log")))
        self.assertEqual(len(self.calls()), 3)

    def test_resume_fills_every_value_and_checks_the_release(self):
        wr(self.prompt, "Resume {SESSION} {ITEM} {PRIMARY} {NOTES} {SCRATCH} {PIN}\n")
        self.cfg["repos"]["beta"]["notes"] = "Beta notes."
        self.write_cfg()

        def worktree(n):
            wt = os.path.join(self.tmp, "wt", f"pass-{n}", "beta")
            os.makedirs(os.path.dirname(wt))
            sh("git", "worktree", "add", "-q", "--detach", wt, "origin/main",
               cwd=os.path.join(self.tmp, "src", "beta"))
            return wt

        wt = worktree(1)
        r = self.cli("resume", "beta", wt, "sess-old", "--prompt", self.prompt, "--item", "020",
                     env={**self.env, "FAKE_QUEUE_RC_RELEASE": "1"})
        self.assertEqual(r.returncode, cf.EXIT_CLAIM, r.stdout + r.stderr)
        self.assertIn("release refused", r.stdout)
        self.assertTrue(os.path.isdir(wt), "a refused release keeps the worktree")
        argv = self.calls()[0]["argv"]
        self.assertEqual(argv[argv.index("--resume") + 1], "sess-old")
        self.assertIn(f"Resume sess-old 020 {os.path.join(self.tmp, 'src', 'beta')} Beta notes. "
                      f"{os.path.join(self.tmp, 'kit', 'scratch', 'beta')}/ UNRESOLVED", argv[-1])
        self.assertEqual(self.calls()[0]["ceiling"], "0")
        wt = worktree(2)
        r = self.cli("resume", "beta", wt, "sess-old", "--prompt", self.prompt, "--item", "020")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(os.path.isdir(wt), "a released resume removes the worktree")


class HelpAndManual(unittest.TestCase):
    """The two-register convention: --help is a digest that points at the man
    page, and the page covers every flag --help prints."""
    SUBCOMMANDS = ["check", "gate", "run", "drive", "drain", "pass", "resume"]

    def help_text(self, *argv):
        r = subprocess.run([sys.executable, TOOL, *argv, "--help"], capture_output=True, text=True,
                           stdin=subprocess.DEVNULL)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout

    def test_top_level_help_is_a_digest_pointing_at_the_manual(self):
        text = self.help_text()
        self.assertIn("man ccfleet", text)
        self.assertLessEqual(len(text.splitlines()), 40)
        for sub in self.SUBCOMMANDS:
            self.assertIn(sub, text)

    def test_the_man_page_covers_every_flag_and_command_help_prints(self):
        with open(os.path.join(HERE, "man", "ccfleet.1"), encoding="utf-8") as fh:
            page = fh.read().replace("\\-", "-")  # roff writes a literal hyphen as \-
        flags = set(re.findall(r"--[a-z][a-z-]*", self.help_text()))
        for sub in self.SUBCOMMANDS:
            flags.update(re.findall(r"--[a-z][a-z-]*", self.help_text(sub)))
        self.assertIn("--serial-per-repo", flags)  # the harvest reached the subcommands
        missing = sorted(f for f in flags if f not in page)
        self.assertEqual(missing, [], "flags in --help but absent from man/ccfleet.1")
        for sub in self.SUBCOMMANDS:
            self.assertRegex(page, r"\.B(R)? " + sub + r"\b", f"no entry for {sub}")


if __name__ == "__main__":
    unittest.main()
