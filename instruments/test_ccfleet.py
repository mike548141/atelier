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
# notification does. FAKE_RC, FAKE_IS_ERROR, FAKE_SILENT (exit 1, print
# nothing), FAKE_SLEEP, FAKE_DIRTY (an untracked file), FAKE_COMMIT (an
# unpushed commit) and FAKE_RESULT_<REPO> shape the cut-off cases.
FAKE_CLAUDE = textwrap.dedent("""\
    #!@PY@
    import datetime, json, os, subprocess, sys, time
    stdin = sys.stdin.read()
    rec = {"argv": sys.argv[1:], "cwd": os.getcwd(), "stdin": stdin, "posix_sid": os.getsid(0),
           "ceiling": os.environ.get("CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS"),
           "extra": os.environ.get("FAKE_EXTRA_ENV")}
    with open(os.environ["FAKE_CLAUDE_LOG"], "a") as f:
        f.write(json.dumps(rec) + "\\n")
    base = os.path.basename(os.getcwd())
    sid = "sess-" + base.replace(" ", "_")
    if os.environ.get("FAKE_SLEEP"):
        time.sleep(float(os.environ["FAKE_SLEEP"]))
    if os.environ.get("FAKE_DIRTY"):
        open("left-behind.txt", "w").close()
    if os.environ.get("FAKE_COMMIT"):
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "-q",  # leakscan:allow:email: a fictional identity for a throwaway test commit
                        "--allow-empty", "-m", "unpushed"], check=True)
    if os.environ.get("FAKE_SILENT"):
        sys.exit(1)
    result = os.environ.get("FAKE_RESULT_" + base.upper(), os.environ.get("FAKE_RESULT", "DONE"))
    report = "did the work\\nREPO: " + base + "\\nRESULT: " + result
    if os.environ.get("FAKE_TRANSCRIPT"):
        d = os.path.join(os.environ["CLAUDE_CONFIG_DIR"], "projects", "-enc-" + sid)
        os.makedirs(d, exist_ok=True)
        ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
        with open(os.path.join(d, sid + ".jsonl"), "a") as f:
            for text in (report, "Noted: the background task finished."):
                f.write(json.dumps({"type": "assistant", "timestamp": ts,
                                    "message": {"content": [{"type": "text", "text": text}]}}) + "\\n")
        report = "Noted: the background task finished."
    out = {"session_id": sid, "result": report}
    if os.environ.get("FAKE_IS_ERROR"):
        out.update(is_error=True, subtype="error_during_execution")
    print(json.dumps(out))
    sys.exit(int(os.environ.get("FAKE_RC", "0")))
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
    if cmd in ("evidence", "owed"):
        with open(root + "/" + cmd + ".log", "a") as f:
            f.write(" ".join(rest) + "\\n")
        if os.environ.get("FAKE_QUEUE_RC_" + cmd.upper()):
            print("queue tool broke", file=sys.stderr)
            sys.exit(int(os.environ["FAKE_QUEUE_RC_" + cmd.upper()]))
        with open(root + "/" + cmd + ".json") as f:
            sys.stdout.write(f.read())
        sys.exit(0)
    if cmd == "next":
        open(root + "/next.called", "a").close()
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
             "message": {"content": [{"type": "text", "text": "report\nITEM: x:010\nRESULT: DONE"}]}},
            {"type": "assistant", "timestamp": "2026-01-01T11:00:02.500Z",
             "message": {"content": [{"type": "text", "text": "Next I will write RESULT: FAILED if it breaks."}]}},
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
        self.assertIn("<!-- session sess-alpha rc=0 result=DONE -->", res)

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
        want = cf.review_log({"kit_dir": os.path.join(self.tmp, "kit")}, "beta", "160/030")
        self.assertTrue(os.path.basename(want).startswith("beta-160-030-"))
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


    # ----- the 160/1450 findings, end to end -----

    def worktrees(self):
        root = os.path.join(self.tmp, "wt")
        return [os.path.join(root, d, r) for d in os.listdir(root) for r in os.listdir(os.path.join(root, d))]

    def test_a_nonzero_exit_keeps_the_worktree_and_is_not_done(self):
        """FL1: rc=1 with a RESULT: DONE printed is an error end."""
        r = self.cli("run", "alpha", "--prompt", self.prompt, env={**self.env, "FAKE_RC": "1"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("rc=1 result=ERROR", r.stdout)
        self.assertEqual(len(self.worktrees()), 1, "an error end keeps its worktree")

    def test_a_cut_off_pass_keeps_its_claim_and_its_worktree(self):
        """FL1: the drain path: an error end releases nothing."""
        wr(os.path.join(self.tmp, "queue.txt"), "beta 010 docs/brief.md\n")
        wr(self.prompt, "Pass {ITEM}\n")
        r = self.cli("drain", "--max", "1", env={**self.env, "FAKE_IS_ERROR": "1"})
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "release.log")))
        self.assertEqual(len(self.worktrees()), 1)
        self.assertIn("result=ERROR", rd(os.path.join(self.tmp, "kit", "driver.log")))

    def test_a_worktree_holding_work_is_never_removed(self):
        """FL1, FL6, 210/560: a clean RESULT that leaves uncommitted files or
        unpushed commits reads as UNLANDED, keeps the tree, and says why."""
        for flag, said in (("FAKE_DIRTY", "uncommitted"), ("FAKE_COMMIT", "on no remote branch")):
            r = self.cli("run", "alpha", "--prompt", self.prompt, "--label", flag.lower(),
                         env={**self.env, flag: "1"})
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("result=UNLANDED", r.stdout)
            self.assertIn("the session said RESULT DONE but left", r.stdout)
            self.assertIn("KEPT worktree", r.stdout)
            self.assertIn(said, r.stdout)
            day = os.listdir(os.path.join(self.tmp, "kit", "results"))[0]
            res = rd(os.path.join(self.tmp, "kit", "results", day, flag.lower() + ".md"))
            self.assertIn("result=UNLANDED -->", res.splitlines()[0])
            self.assertIn("RESULT DONE read as UNLANDED", res)
        self.assertEqual(len(self.worktrees()), 2)
        self.assertTrue(any(os.path.exists(os.path.join(w, "left-behind.txt")) for w in self.worktrees()))

    def test_a_clean_pass_that_leaves_unlanded_work_keeps_its_claim_and_resumes(self):
        """210/560 part 2 (the principal, 2026-11-23: "Treat as not clean"): a
        DONE pass whose worktree holds uncommitted work releases nothing, keeps
        its worktree, counts as unclean, and its resume releases once it lands."""
        q = self.cfg["queue"]
        q["ended"] = [self.queue, "ended", "{REPO}:{ITEM}", "{RESULT}"]
        self.write_cfg()
        wr(os.path.join(self.tmp, "queue.txt"), "beta 030 docs/brief.md\n")
        wr(self.prompt, "Pass {ITEM}\n")
        r = self.cli("drain", "--max", "1", env={**self.env, "FAKE_DIRTY": "1"})
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "release.log")), "the claim was released")
        self.assertEqual(rd(os.path.join(self.tmp, "ended.log")).split(), ["beta:030", "UNLANDED"])
        (wt,) = self.worktrees()
        self.assertTrue(os.path.exists(os.path.join(wt, "left-behind.txt")))
        self.assertIn("result=UNLANDED", rd(os.path.join(self.tmp, "kit", "driver.log")))
        # Resumed while the work is still unlanded: still not clean.
        r = self.cli("resume", "beta", wt, "sess-beta", "--prompt", self.prompt, "--item", "030")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("result=UNLANDED", r.stdout)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "release.log")))
        self.assertTrue(os.path.isdir(wt))
        # Landed (here: the stray file removed), the resume releases and removes.
        os.remove(os.path.join(wt, "left-behind.txt"))
        r = self.cli("resume", "beta", wt, "sess-beta", "--prompt", self.prompt, "--item", "030")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("result=DONE", r.stdout)
        self.assertEqual(rd(os.path.join(self.tmp, "release.log")).split(), ["beta:030"])
        self.assertFalse(os.path.isdir(wt))

    def test_unlanded_may_not_be_a_release_word(self):
        self.cfg["queue"]["release_on"] = ["DONE", "UNLANDED"]
        self.write_cfg()
        r = self.cli("check")
        self.assertEqual(r.returncode, cf.EXIT_USAGE)
        self.assertIn("may not hold UNLANDED", r.stderr)

    # ----- 210/560 part 1: the config is the whole grant -----

    def user_settings(self, settings, claude_md=None):
        d = self.env["CLAUDE_CONFIG_DIR"]
        os.makedirs(d, exist_ok=True)
        wr(os.path.join(d, "settings.json"), json.dumps(settings))
        if claude_md is not None:
            wr(os.path.join(d, "CLAUDE.md"), claude_md)

    USER = {
        "permissions": {"allow": ["Bash", "Edit"], "deny": ["Bash(rm -rf /)"], "ask": ["Bash(git push:*)"],
                        "defaultMode": "auto", "additionalDirectories": ["/elsewhere"]},
        "hooks": {"PreToolUse": [
            {"matcher": "mcp__.*", "hooks": [{"type": "command", "command":
                "echo '{\"hookSpecificOutput\":{\"permissionDecision\":\"allow\"}}'"}]},
            {"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 /guards/secretguard.py"},
                                          {"type": "command", "command": "python3 /guards/noisy.py"}]}]},
        "enabledPlugins": {"house@house": True}, "env": {"HOUSE": "1"}, "effortLevel": "high",
    }

    def test_a_launch_loads_no_user_grant_but_keeps_its_guards(self):
        """The principal, 2026-11-23: "Config is the whole grant". No user-level
        settings source loads; the settings file ccfleet writes carries the
        user's guards (deny, ask, hooks) and equipment (plugins, env), never its
        allow rules, default mode, extra directories or an approving hook."""
        self.user_settings(self.USER, claude_md="# House rules\nNever push to main on a Friday.\n")
        self.cfg["claude_args"] = ["--allowedTools", "Bash(git *)"]
        self.cfg["drop_hooks"] = ["noisy.py"]
        self.cfg["settings"] = {"permissions": {"allow": ["Read"]}, "env": {"FLEET": "1"}}
        self.write_cfg()
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        argv = self.calls()[0]["argv"]
        self.assertEqual(argv[argv.index("--setting-sources") + 1], "project,local")
        got = json.loads(rd(argv[argv.index("--settings") + 1]))
        perms = got["permissions"]
        self.assertEqual(perms["allow"], ["Read"], "only the config's allow rules")
        for k in ("defaultMode", "additionalDirectories"):
            self.assertNotIn(k, perms)
        self.assertEqual((perms["deny"], perms["ask"]), (["Bash(rm -rf /)"], ["Bash(git push:*)"]))
        cmds = [h["command"] for g in got["hooks"]["PreToolUse"] for h in g["hooks"]]
        self.assertEqual(cmds, ["python3 /guards/secretguard.py"], "guard kept; approving and dropped hooks out")
        self.assertEqual(got["enabledPlugins"], {"house@house": True})
        self.assertEqual(got["env"], {"HOUSE": "1", "FLEET": "1"})
        self.assertEqual(got["effortLevel"], "high")
        instructions = rd(argv[argv.index("--append-system-prompt-file") + 1])
        self.assertIn("Never push to main on a Friday.", instructions)
        self.assertEqual(argv[argv.index("--allowedTools") + 1], "Bash(git *)")
        # The resume path launches the same way.
        wt = os.path.join(self.tmp, "wt", "pass-9", "beta")
        os.makedirs(os.path.dirname(wt))
        sh("git", "worktree", "add", "-q", "--detach", wt, "origin/main", cwd=os.path.join(self.tmp, "src", "beta"))
        self.cli("resume", "beta", wt, "sess-old", "--prompt", self.prompt)
        argv = self.calls()[1]["argv"]
        self.assertEqual(argv[argv.index("--setting-sources") + 1], "project,local")
        self.assertEqual(json.loads(rd(argv[argv.index("--settings") + 1]))["permissions"]["allow"], ["Read"])
        self.assertIn("--append-system-prompt-file", argv)

    def test_no_user_settings_still_loads_no_user_source(self):
        r = self.cli("run", "alpha", "--prompt", self.prompt, "--dry-run")
        self.assertIn("--setting-sources project,local --settings", r.stdout)
        self.assertNotIn("--append-system-prompt-file", r.stdout, "no user CLAUDE.md, nothing appended")
        self.cli("run", "alpha", "--prompt", self.prompt)
        argv = self.calls()[0]["argv"]
        self.assertEqual(json.loads(rd(argv[argv.index("--settings") + 1])), {})

    def test_an_unreadable_user_settings_file_refuses_before_any_start(self):
        d = self.env["CLAUDE_CONFIG_DIR"]
        os.makedirs(d, exist_ok=True)
        wr(os.path.join(d, "settings.json"), "{not json")
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, cf.EXIT_SETUP, r.stdout + r.stderr)
        self.assertIn("would drop their hooks and deny rules", r.stderr)
        self.assertEqual(self.calls(), [])
        self.assertEqual(os.listdir(os.path.join(self.tmp, "wt")), [])

    def test_a_repos_own_grants_are_said_at_launch(self):
        prim = os.path.join(self.tmp, "src", "alpha")
        os.makedirs(os.path.join(prim, ".claude"))
        wr(os.path.join(prim, ".claude", "settings.json"),
           json.dumps({"permissions": {"allow": ["Bash"], "defaultMode": "acceptEdits"}}))
        sh("git", "add", ".claude/settings.json", cwd=prim)
        sh("git", *GIT_ID, "commit", "-q", "-m", "repo settings", cwd=prim)
        sh("git", "push", "-q", "origin", "HEAD:main", cwd=prim)
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertRegex(r.stdout, r'WIDENED by the repo\'s own \.claude/settings\.json: allow \["Bash"\]; '
                                   r'defaultMode "acceptEdits"')
        self.assertLess(r.stdout.index("WIDENED"), r.stdout.index("START"))

    def test_claude_args_may_not_take_the_settings_flags_back(self):
        for args in (["--settings", "/x.json"], ["--setting-sources=user,project"],
                     ["--append-system-prompt-file", "/x.md"]):
            self.cfg["claude_args"] = args
            self.write_cfg()
            r = self.cli("check")
            self.assertEqual(r.returncode, cf.EXIT_USAGE, args)
            self.assertIn("so the config is the whole grant", r.stderr)
        self.cfg["claude_args"] = []
        for k, v in (("settings", ["x"]), ("drop_hooks", "noisy"), ("drop_hooks", [""])):
            self.cfg[k] = v
            self.write_cfg()
            self.assertEqual(self.cli("check").returncode, cf.EXIT_USAGE, (k, v))
            self.cfg.pop(k)

    def test_an_unclean_run_keeps_its_worktree_and_drive_runs_it_again(self):
        """FL6: run keeps the worktree unless the RESULT is clean; drive skips
        a job only on a clean result."""
        jobs = os.path.join(self.tmp, "jobs.tsv")
        wr(jobs, f"alpha\ta-job\t{self.prompt}\nbeta\tb-job\t{self.prompt}\n")
        env = {**self.env, "FAKE_RESULT_BETA": "PARTIAL"}
        r = self.cli("drive", jobs, "--max", "2", env=env)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual([os.path.basename(w) for w in self.worktrees()], ["beta"])
        self.cli("drive", jobs, env=env)
        self.assertEqual(sorted(os.path.basename(c["cwd"]) for c in self.calls()), ["alpha", "beta", "beta"])
        log = rd(os.path.join(self.tmp, "kit", "driver.log"))
        self.assertIn("skip a-job (a clean result exists", log)
        self.assertNotIn("skip b-job", log)

    def test_drive_keeps_one_results_day(self):
        """FL6: a drive's children write to the drive's day, and --day resumes it."""
        jobs = os.path.join(self.tmp, "jobs.tsv")
        wr(jobs, f"alpha\ta-job\t{self.prompt}\n")
        r = self.cli("drive", jobs, "--day", "2001-02-03")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, "kit", "results", "2001-02-03", "a-job.md")))
        self.cli("drive", jobs, "--day", "2001-02-03")
        self.assertEqual(len(self.calls()), 1)
        self.assertEqual(self.cli("drive", jobs, "--day", "Feb 3").returncode, cf.EXIT_USAGE)

    def test_a_dry_drain_leaves_the_real_drain_its_queue(self):
        """FL2: a rehearsal writes no launched list the real drain reads."""
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\nbeta 020 docs/brief.md\n")
        r = self.cli("drain", "--max", "1", "--dry-run")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        kit = os.path.join(self.tmp, "kit")
        self.assertEqual([f for f in os.listdir(kit) if f.startswith("launched")], [])
        r = self.cli("drain", "--max", "2")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(len(self.calls()), 2)

    def test_a_pick_that_never_starts_comes_off_the_list_and_counts(self):
        """FL2: an early end is not a launch; three in a row stop the drain,
        and a drain that ran nothing does not exit 0."""
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/not-pushed.md\n")
        r = self.cli("drain", "--max", "1")
        self.assertEqual(r.returncode, cf.EXIT_SETUP, r.stdout + r.stderr)
        self.assertIn("DRAIN EXIT: failures", r.stdout)
        log = rd(os.path.join(self.tmp, "kit", "driver.log"))
        self.assertEqual(log.count("ended before its session started"), 3)
        (launched,) = [f for f in os.listdir(os.path.join(self.tmp, "kit")) if f.startswith("launched-")]
        self.assertEqual(rd(os.path.join(self.tmp, "kit", launched)), "")
        self.assertEqual(self.calls(), [])

    def test_a_new_session_has_its_id_before_it_prints(self):
        """FL3: the id is chosen up front, so a session that dies silent still has one."""
        q = self.cfg["queue"]
        q["take"] = [self.queue, "take", "{REPO}:{ITEM}", "{SESSION}"]
        self.write_cfg()
        wr(os.path.join(self.tmp, "queue.txt"), "beta 010 docs/brief.md\n")
        r = self.cli("drain", "--max", "1", env={**self.env, "FAKE_SILENT": "1"})
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        argv = self.calls()[0]["argv"]
        sid = argv[argv.index("--session-id") + 1]
        self.assertRegex(sid, r"^[0-9a-f-]{36}$")
        self.assertEqual(rd(os.path.join(self.tmp, "take.log")).split(), ["beta:010", sid])
        out = "".join(rd(os.path.join(self.tmp, "kit", "logs", f)) for f in
                      os.listdir(os.path.join(self.tmp, "kit", "logs")) if f.startswith("pass-"))
        self.assertIn(f"session={sid}", out.split("START", 1)[1].splitlines()[0])
        self.assertIn(f"result=ERROR session={sid}", out)

    def test_check_says_when_a_permission_mode_is_set(self):
        """FL10: a bypass is named loudly, any other widening plainly, none not at all."""
        r = self.cli("check")
        self.assertIn("PERMISSIONS: BYPASS", r.stdout)
        self.cfg["claude_args"] = ["--permission-mode", "acceptEdits"]
        self.write_cfg()
        r = self.cli("check")
        self.assertIn("PERMISSIONS: every session starts with --permission-mode acceptEdits", r.stdout)
        self.assertNotIn("BYPASS", r.stdout)
        self.cfg["claude_args"] = []
        self.write_cfg()
        self.assertNotIn("PERMISSIONS", self.cli("check").stdout)
        self.cfg["settings"] = {"permissions": {"allow": ["Bash(make *)"]}}
        self.write_cfg()
        self.assertIn("PERMISSIONS: every session starts with settings allow Bash(make *)", self.cli("check").stdout)
        self.cfg["settings"] = {"permissions": {"defaultMode": "bypassPermissions"}}
        self.write_cfg()
        self.assertIn("PERMISSIONS: BYPASS", self.cli("check").stdout)

    def test_check_says_the_config_is_the_whole_grant(self):
        """210/560: check names the user-level grants left out, the hooks kept
        and dropped, the appended instructions, and that a repo's own settings
        still load."""
        self.user_settings(self.USER, claude_md="rules\n")
        self.cfg["drop_hooks"] = ["noisy.py"]
        self.write_cfg()
        out = self.cli("check").stdout
        self.assertIn("GRANT: the config is the whole grant. No user-level settings load (--setting-sources "
                      "project,local)", out)
        self.assertIn("Left out: allow (2 rule(s)); defaultMode auto; additionalDirectories /elsewhere.", out)
        self.assertIn("Kept: deny 1 rule(s), ask 1 rule(s), 1 hook command(s), effortLevel, enabledPlugins, env.",
                      out)
        self.assertIn("HOOK dropped: PreToolUse mcp__.* (approves tool calls)", out)
        self.assertIn("HOOK dropped: PreToolUse Bash (drop_hooks 'noisy.py')", out)
        self.assertIn("HOOK kept: PreToolUse Bash: python3 /guards/secretguard.py", out)
        self.assertIn("INSTRUCTIONS: " + os.path.join(self.env["CLAUDE_CONFIG_DIR"], "CLAUDE.md") + " is appended",
                      out)
        self.assertIn("REPO SETTINGS: a repo's own .claude/settings.json", out)

    def test_check_names_the_placeholders_nothing_fills(self):
        """FL12: unset placeholders are named before a launch refuses them."""
        wr(self.prompt, "Pass {ITEM} {BRIEF} {REVIEW_LOG} under {APPROVAL} in {WT}\n")
        r = self.cli("check")
        self.assertEqual(r.returncode, cf.EXIT_GUARD, r.stdout + r.stderr)
        self.assertIn("UNSET: {APPROVAL}", r.stdout)
        self.cfg["vars"]["APPROVAL"] = "yes"
        self.write_cfg()
        self.assertEqual(self.cli("check").returncode, 0)
        task = os.path.join(self.tmp, "task.md")
        wr(task, "Do {TASK} for {REPO}, resume {SESSION} item {ITEM}\n")
        r = self.cli("check", "--prompt", task)
        self.assertEqual(r.returncode, cf.EXIT_GUARD)
        self.assertIn("UNSET: {TASK}", r.stdout)
        self.assertIn("filled only by pass or resume: {ITEM}", r.stdout)
        self.assertEqual(self.cli("check", "--prompt", task, "--set", "TASK=x").returncode, 0)

    def test_a_refused_release_keeps_the_pass_worktree_and_exits_2(self):
        """FL13: a pass whose release is refused keeps its worktree."""
        wr(self.prompt, "Pass {ITEM}\n")
        r = self.cli("pass", "beta", "010", "docs/brief.md", env={**self.env, "FAKE_QUEUE_RC_RELEASE": "1"})
        self.assertEqual(r.returncode, cf.EXIT_CLAIM, r.stdout + r.stderr)
        self.assertIn("release refused", r.stdout)
        self.assertEqual(len(self.worktrees()), 1)

    def test_a_fold_releases_and_puts_its_worktree_away(self):
        """FL13: run --in WT --item ITEM is a fold: a clean end releases the
        claim and removes the adopted worktree; an unclean one keeps both."""
        wt = os.path.join(self.tmp, "wt", "pass-0101", "beta")
        os.makedirs(os.path.dirname(wt))
        sh("git", "worktree", "add", "-q", "--detach", wt, "origin/main", cwd=os.path.join(self.tmp, "src", "beta"))
        r = self.cli("run", "beta", "--prompt", self.prompt, "--in", wt, "--item", "020",
                     env={**self.env, "FAKE_RESULT": "FAILED"})
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue(os.path.isdir(wt))
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "release.log")))
        wr(self.prompt, "Fold {ITEM} with {REVIEW_LOG}\n")
        r = self.cli("run", "beta", "--prompt", self.prompt, "--in", wt, "--item", "020")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        want = cf.review_log({"kit_dir": os.path.join(self.tmp, "kit")}, "beta", "020")
        self.assertEqual(self.calls()[-1]["argv"][-1], f"Fold 020 with {want}\n", "a fold gets the pass's log")
        self.assertEqual(rd(os.path.join(self.tmp, "release.log")).split(), ["beta:020"])
        self.assertFalse(os.path.isdir(wt))
        r = self.cli("run", "beta", "--prompt", self.prompt, "--item", "020")
        self.assertEqual(r.returncode, cf.EXIT_USAGE, "--item without --in")

    def test_review_logs_never_collide_and_a_fresh_pass_inherits_none(self):
        """FL15: distinct pairs get distinct logs; a log left by an earlier
        pass is moved aside before a new pass on the item starts."""
        kit = {"kit_dir": os.path.join(self.tmp, "kit")}
        self.assertNotEqual(cf.review_log(kit, "app-web", "010"), cf.review_log(kit, "app", "web/010"))
        stale = cf.review_log(kit, "beta", "030")
        os.makedirs(os.path.dirname(stale))
        wr(stale, "an earlier reviewer's account\n")
        wr(os.path.join(self.tmp, "queue.txt"), "beta 030 docs/brief.md\n")
        wr(self.prompt, "Log {REVIEW_LOG}\n")
        r = self.cli("drain")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(os.path.exists(stale))
        (moved,) = os.listdir(os.path.join(self.tmp, "kit", "review-logs", "withdrawn"))
        self.assertTrue(moved.endswith(os.path.basename(stale)))

    def test_review_log_hash_is_sha2_and_earlier_names_are_still_found(self):
        """115/500: the log name hashes with SHA-256; a log a pass left under
        the SHA-1 or the hashless name is still the one pass_log finds, the
        newer earlier name first, and the current name wins once it exists."""
        import hashlib
        kit = {"kit_dir": os.path.join(self.tmp, "kit")}
        cur = cf.review_log(kit, "beta", "030")
        self.assertTrue(cur.endswith("-" + hashlib.sha256(b"beta\x00030").hexdigest()[:8] + ".md"))
        hashless, sha1 = cf.review_log(kit, "beta", "030", legacy=True)
        self.assertEqual(cf.pass_log(kit, "beta", "030"), cur)
        os.makedirs(os.path.dirname(cur))
        wr(hashless, "oldest\n")
        self.assertEqual(cf.pass_log(kit, "beta", "030"), hashless)
        wr(sha1, "older\n")
        self.assertEqual(cf.pass_log(kit, "beta", "030"), sha1)
        wr(cur, "current\n")
        self.assertEqual(cf.pass_log(kit, "beta", "030"), cur)

    def test_ranked_is_not_called_dry_or_after_the_reset(self):
        """FL16: a rehearsal and a drain past its reset never call queue.ranked."""
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        r = self.cli("drain", "--dry-run")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "ranked.log")))
        self.cfg["reset_utc"] = "2000-01-01T00:00"
        self.write_cfg()
        r = self.cli("drain")
        self.assertEqual(r.returncode, cf.EXIT_RESET, r.stdout + r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "ranked.log")))

    def test_bad_inputs_are_refused_with_a_reason(self):
        """FL17: a repo given as a path, --set with no '=', a resume worktree
        not named for its repo or missing."""
        r = self.cli("run", "src/alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, cf.EXIT_USAGE, r.stderr)
        r = self.cli("run", "alpha", "--prompt", self.prompt, "--set", "NOEQUALS")
        self.assertEqual(r.returncode, cf.EXIT_USAGE, r.stderr)
        self.assertIn("expected K=V", r.stderr)
        wt = os.path.join(self.tmp, "wt", "pass-0101", "beta")
        os.makedirs(os.path.dirname(wt))
        sh("git", "worktree", "add", "-q", "--detach", wt, "origin/main", cwd=os.path.join(self.tmp, "src", "beta"))
        for repo, path in (("alpha", wt), ("beta", wt + "-missing")):
            r = self.cli("resume", repo, path, "sess-1", "--prompt", self.prompt)
            self.assertEqual(r.returncode, cf.EXIT_SETUP, r.stderr)
            self.assertNotIn("Traceback", r.stderr)
        self.assertEqual(self.calls(), [])

    def test_resume_without_an_item_calls_no_queue_command(self):
        """FL17: no --item, no release and no ended call with an empty item."""
        self.cfg["queue"]["ended"] = [self.queue, "ended", "{REPO}:{ITEM}"]
        self.write_cfg()
        wt = os.path.join(self.tmp, "wt", "pass-0101", "beta")
        os.makedirs(os.path.dirname(wt))
        sh("git", "worktree", "add", "-q", "--detach", wt, "origin/main", cwd=os.path.join(self.tmp, "src", "beta"))
        r = self.cli("resume", "beta", wt, "sess-1", "--prompt", self.prompt)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "ended.log")))
        self.assertTrue(os.path.isdir(wt))
        argv = self.calls()[0]["argv"]
        self.assertEqual(argv[argv.index("--model") + 1], "model-pass", "a resume names its model")

    def test_two_resumes_of_one_session_cannot_run_at_once(self):
        """FL17: the second is refused (exit 2) and starts nothing."""
        wt = os.path.join(self.tmp, "wt", "pass-0101", "beta")
        os.makedirs(os.path.dirname(wt))
        sh("git", "worktree", "add", "-q", "--detach", wt, "origin/main", cwd=os.path.join(self.tmp, "src", "beta"))
        lock = os.path.join(self.tmp, "kit", "locks", "resume-sess-1.lock")
        with cf.FileLock(lock, "held by the test"):
            r = self.cli("resume", "beta", wt, "sess-1", "--prompt", self.prompt)
        self.assertEqual(r.returncode, cf.EXIT_CLAIM, r.stdout + r.stderr)
        self.assertIn("another resume of session sess-1", r.stderr)
        self.assertEqual(self.calls(), [])

    def test_max_0_is_a_ceiling_of_0(self):
        """FL17: --max 0 holds every start; it never falls back to the config."""
        with mock.patch.object(cf, "drain", return_value=0) as d:
            self.assertEqual(cf.main(["--config", self.cfgpath, "drain", "--max", "0"]), 0)
        self.assertEqual(d.call_args[0][2], 0)
        self.assertEqual(cf.main(["--config", self.cfgpath, "drain", "--max", "-1"]), cf.EXIT_USAGE)

    def test_a_public_prompt_naming_a_joined_private_name_is_refused(self):
        """FL23 end to end: the worktree parent <label>-<HHMM> carries the name."""
        self.cfg["private_names"] = ["privroot"]
        self.write_cfg()
        r = self.cli("run", "alpha", "--prompt", self.prompt, "--label", "privroot")
        self.assertEqual(r.returncode, cf.EXIT_GUARD, r.stdout + r.stderr)
        self.assertIn("privroot", r.stderr)
        self.assertEqual(self.calls(), [])

    def test_a_session_past_its_time_limit_is_ended(self):
        """FL25: a session that does not exit is ended at its limit, read as
        TIMEOUT, and keeps its worktree."""
        self.cfg["session_timeout_minutes"] = 0.02
        self.write_cfg()
        t0 = time.time()
        r = self.cli("run", "alpha", "--prompt", self.prompt, env={**self.env, "FAKE_SLEEP": "60"})
        self.assertLess(time.time() - t0, 45)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("TIMEOUT", r.stdout)
        self.assertIn(f"rc={cf.TIMEOUT_RC} result=TIMEOUT", r.stdout)
        self.assertEqual(len(self.worktrees()), 1)

    def test_a_jobs_file_whose_labels_repeat_is_refused_before_anything_starts(self):
        """210/450: the label keys the result file; a repeat is refused at load."""
        jobs = os.path.join(self.tmp, "jobs.tsv")
        wr(jobs, f"alpha\tsweep\t{self.prompt}\nbeta\tother\t{self.prompt}\n"
                 f"beta\tsweep\t{self.prompt}\n")
        r = self.cli("drive", jobs)
        self.assertEqual(r.returncode, cf.EXIT_USAGE, r.stdout + r.stderr)
        self.assertIn("label 'sweep' on lines 1, 3", r.stderr)
        self.assertEqual(self.calls(), [])
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "kit", "driver.log")))


    # ---- plan: the read-only reading of the queue ----

    EVIDENCE = [{"repo": "alpha", "item": "010", "brief": "docs/brief.md", "title": "Check the alpha guard",
                 "fits": ["local", "batch"], "his_words": "first, please", "dates_ahead": ["2030-01-06"]},
                {"repo": "beta", "item": "020", "brief": "docs/brief.md", "title": "Check the beta write path",
                 "fits": ["local"]}]
    OWED = [{"repo": "beta", "item": "030", "title": "Review the beta export", "why": "its item says one is owed"}]

    def queue_json(self, evidence=None, owed=None):
        wr(os.path.join(self.tmp, "evidence.json"), json.dumps(self.EVIDENCE if evidence is None else evidence))
        wr(os.path.join(self.tmp, "owed.json"), json.dumps(self.OWED if owed is None else owed))

    def plan_cfg(self, owed=True, fetch=False):
        self.cfg["queue"]["evidence"] = [self.queue, "evidence"] + (["{FETCH}"] if fetch else [])
        if owed:
            self.cfg["queue"]["owed"] = [self.queue, "owed"] + (["{FETCH}"] if fetch else [])
        self.write_cfg()

    def not_called(self):
        """The queue commands a plan must never call leave no trace."""
        for name in ("ranked.log", "take.log", "release.log", "ended.log", "next.called"):
            self.assertFalse(os.path.exists(os.path.join(self.tmp, name)), name)
        kit = os.path.join(self.tmp, "kit")
        self.assertEqual([f for f in os.listdir(kit) if f.startswith("launched")], [])
        self.assertEqual(os.listdir(os.path.join(self.tmp, "wt")), [])
        self.assertEqual(self.calls(), [])

    def pass_log_pair(self, name, result="DONE", cost=None, ms=None, turns=None, rc=0, is_error=False):
        """A drain pass's .out (START and END lines) and its claude -p JSON log."""
        logs = os.path.join(self.tmp, "kit", "logs")
        os.makedirs(logs, exist_ok=True)
        jlog = os.path.join(logs, name + ".json")
        body = {"session_id": "s-" + name, "result": f"REPO: x\nRESULT: {result}"}
        for k, v in (("total_cost_usd", cost), ("duration_ms", ms), ("num_turns", turns)):
            if v is not None:
                body[k] = v
        if is_error:
            body.update(is_error=True, subtype="error_during_execution")
        wr(jlog, json.dumps(body))
        wr(os.path.join(logs, f"pass-{name}-000000.out"),
           f"START 2030-01-01T00:00:00Z {name} model=m session=s-{name} wt=/x/{name} log={jlog}\n"
           f"END 2030-01-01T00:10:00Z rc={rc} result={result} session=s-{name} out=/x\n")

    def test_plan_prints_the_evidence_and_the_owed_list(self):
        self.queue_json()
        self.plan_cfg()
        r = self.cli("plan")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        for want in ("Check the alpha guard", "Check the beta write path", "local, batch",
                     "Review the beta export", "its item says one is owed", "NOT YET BRIEFED: 1",
                     "COST HISTORY", "local: no measurement"):
            self.assertIn(want, r.stdout)
        self.not_called()

    def test_plan_never_calls_ranked_take_next_release_or_ended(self):
        """The marker files prove it: every other queue command leaves one."""
        self.queue_json()
        self.plan_cfg()
        self.cfg["queue"]["ended"] = [self.queue, "ended", "{REPO}:{ITEM}"]
        self.write_cfg()
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        for extra in ([], ["--json"], ["--fetch"]):
            self.assertEqual(self.cli("plan", *extra).returncode, 0)
        self.not_called()
        # and the marker works: a real drain does leave them
        self.assertEqual(self.cli("drain", "--max", "1").returncode, 0)
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "ranked.log")))
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "next.called")))

    def test_plan_json_shape(self):
        self.queue_json()
        self.plan_cfg()
        r = self.cli("plan", "--json")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        d = json.loads(r.stdout)
        self.assertEqual(sorted(d), ["evidence", "history", "notes", "owed"])
        self.assertEqual(d["evidence"], self.EVIDENCE)  # passed through untouched, in the queue's order
        self.assertEqual(d["owed"], self.OWED)
        self.assertEqual(sorted(d["history"]["routes"]), ["batch", "local"])
        self.assertEqual(d["history"]["routes"]["batch"], {"measured": False, "note": "no measurement"})
        self.assertFalse(d["history"]["routes"]["local"]["measured"])
        self.assertIsInstance(d["notes"], list)

    def test_plan_owed_is_null_when_not_configured(self):
        self.queue_json()
        self.plan_cfg(owed=False)
        d = json.loads(self.cli("plan", "--json").stdout)
        self.assertIsNone(d["owed"])
        self.assertTrue(any("queue.owed is not configured" in n for n in d["notes"]))
        self.assertIn("not read (queue.owed is not configured)", self.cli("plan").stdout)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "owed.log")))

    def test_a_failing_evidence_command_exits_1_plainly(self):
        self.queue_json()
        self.plan_cfg()
        r = self.cli("plan", env={**self.env, "FAKE_QUEUE_RC_EVIDENCE": "3"})
        self.assertEqual(r.returncode, cf.EXIT_SETUP, r.stdout + r.stderr)
        self.assertIn("queue.evidence failed (rc=3)", r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        r = self.cli("plan", env={**self.env, "FAKE_QUEUE_RC_OWED": "4"})
        self.assertEqual(r.returncode, cf.EXIT_SETUP, r.stdout + r.stderr)
        self.assertIn("queue.owed failed (rc=4)", r.stderr)

    def test_evidence_that_is_not_the_json_it_should_be_exits_1(self):
        self.plan_cfg()
        for text, said in (("not json", "did not print JSON"), ('{"repo": "a"}', "JSON array of objects"),
                           ('[{"repo": "alpha", "item": "1", "brief": "b"}]', "has no title")):
            wr(os.path.join(self.tmp, "evidence.json"), text)
            wr(os.path.join(self.tmp, "owed.json"), "[]")
            r = self.cli("plan")
            self.assertEqual(r.returncode, cf.EXIT_SETUP, (text, r.stdout, r.stderr))
            self.assertIn(said, r.stderr)
            self.assertNotIn("Traceback", r.stderr)

    def test_plan_without_queue_evidence_is_a_usage_refusal(self):
        r = self.cli("plan")
        self.assertEqual(r.returncode, cf.EXIT_USAGE, r.stdout + r.stderr)
        self.assertIn("queue.evidence", r.stderr)

    def test_fetch_fills_the_placeholder_or_drops_it(self):
        self.queue_json()
        self.plan_cfg(fetch=True)
        self.cli("plan")
        self.cli("plan", "--fetch")
        self.assertEqual(rd(os.path.join(self.tmp, "evidence.log")), "\n--fetch\n")
        self.assertEqual(rd(os.path.join(self.tmp, "owed.log")), "\n--fetch\n")

    def test_fetch_with_no_placeholder_is_said_not_silently_dropped(self):
        self.queue_json()
        self.plan_cfg()
        d = json.loads(self.cli("plan", "--fetch", "--json").stdout)
        self.assertTrue(any("nothing was fetched" in n for n in d["notes"]))
        self.assertEqual(rd(os.path.join(self.tmp, "evidence.log")), "\n")

    def test_cost_history_from_the_pass_logs(self):
        self.queue_json()
        self.plan_cfg()
        self.pass_log_pair("a-1", cost=2.0, ms=60000, turns=10)
        self.pass_log_pair("a-2", cost=4.0, ms=120000, turns=30)
        self.pass_log_pair("a-3", cost=9.0, ms=240000, turns=50)
        self.pass_log_pair("a-4", result="ERROR", cost=99.0, ms=1, turns=1, rc=1)       # not clean
        self.pass_log_pair("a-5", result="DONE", cost=77.0, is_error=True)             # flagged: not clean
        self.pass_log_pair("a-6", result="UNLANDED", cost=55.0)                         # clean text, unlanded
        d = json.loads(self.cli("plan", "--json").stdout)
        local = d["history"]["routes"]["local"]
        self.assertTrue(local["measured"], local)
        self.assertEqual((local["passes_seen"], local["clean"]), (6, 3))
        self.assertEqual(local["cost_usd"], {"n": 3, "median": 4.0, "max": 9.0})
        self.assertEqual(local["duration_s"], {"n": 3, "median": 120.0, "max": 240.0})
        self.assertEqual(local["turns"], {"n": 3, "median": 30, "max": 50})
        self.assertEqual(d["history"]["routes"]["batch"]["note"], "no measurement")
        text = self.cli("plan").stdout
        self.assertIn("3 clean pass(es) of 6 seen", text)
        self.assertIn("cost: median 4.0 USD, max 9.0 USD (n=3)", text)
        self.not_called()

    def test_cost_history_says_no_measurement_with_no_logs_or_no_cost(self):
        self.queue_json()
        self.plan_cfg()
        d = json.loads(self.cli("plan", "--json").stdout)
        self.assertEqual(d["history"]["routes"]["local"]["note"], "no measurement")
        self.pass_log_pair("b-1")  # clean, but the log carries no cost fields
        local = json.loads(self.cli("plan", "--json").stdout)["history"]["routes"]["local"]
        self.assertFalse(local["measured"])
        self.assertEqual((local["passes_seen"], local["clean"]), (1, 1))
        self.assertIn("no measurement", self.cli("plan").stdout)

    def test_a_dry_drain_prints_the_plan_and_still_does_not_call_ranked(self):
        self.queue_json()
        self.plan_cfg()
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        r = self.cli("drain", "--max", "1", "--dry-run")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        lines = r.stdout.splitlines()
        plan_lines = [l for l in lines if l.startswith("DRY plan:")]
        self.assertTrue(any("Check the alpha guard" in l for l in plan_lines), r.stdout)
        self.assertTrue(any("Review the beta export" in l for l in plan_lines), r.stdout)
        last_plan = max(i for i, l in enumerate(lines) if l.startswith("DRY plan:"))
        self.assertLess(last_plan, lines.index("DRY queue.ranked not called"))
        # the rehearsed launches print into each pass's own .out, after the reading
        self.assertEqual(self.calls(), [])
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "ranked.log")))
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "take.log")))
        self.assertEqual(self.calls(), [])

    def test_a_dry_drain_without_evidence_says_so_and_carries_on(self):
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        r = self.cli("drain", "--max", "1", "--dry-run")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual([l for l in r.stdout.splitlines() if l.startswith("DRY plan:")],
                         ["DRY plan: queue.evidence is not configured; no plan reading (carrying on)"])
        self.assertIn("DRY queue.ranked not called", r.stdout)

    def test_a_dry_drain_with_failing_evidence_reports_it_and_carries_on(self):
        self.queue_json()
        self.plan_cfg()
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        r = self.cli("drain", "--max", "1", "--dry-run", env={**self.env, "FAKE_QUEUE_RC_EVIDENCE": "3"})
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("DRY plan: FAILED", r.stdout)
        self.assertIn("DRY queue.ranked not called", r.stdout)

    def test_a_real_drain_does_not_read_the_plan(self):
        self.queue_json()
        self.plan_cfg()
        wr(os.path.join(self.tmp, "queue.txt"), "alpha 010 docs/brief.md\n")
        r = self.cli("drain", "--max", "1")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("plan:", r.stdout)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "evidence.log")))


class ResultWords(unittest.TestCase):
    """FL14: a RESULT line is read by its known phrase or its first word."""
    known = ("DONE", "SKIPPED", "BUDGET EXHAUSTED")

    def test_plain_endings_read_as_their_first_word(self):
        for text, want in (("RESULT: SKIPPED NEEDS LIVE WRITE", "SKIPPED"),
                           ("RESULT: DONE WITH FINDINGS", "DONE"),
                           ("RESULT: `DONE`", "DONE"),
                           ("**RESULT:** DONE", "DONE"),
                           ("**RESULT: BUDGET EXHAUSTED** at act 1", "BUDGET EXHAUSTED"),
                           ("RESULT: <DONE|SKIPPED>", "")):
            self.assertEqual(cf.result_word(text, self.known), want, text)

    def test_the_last_result_line_is_the_verdict(self):
        self.assertEqual(cf.result_word("RESULT: FAILED\nmore\nRESULT: DONE\n", self.known), "DONE")


class ErrorEnds(unittest.TestCase):
    """FL1: a nonzero exit or an error flag is never a clean end."""

    def log(self, obj):
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json") as f:
            f.write(json.dumps(obj))
        self.addCleanup(os.remove, f.name)
        return f.name

    def test_a_nonzero_exit_reads_as_error_whatever_the_text(self):
        path = self.log({"session_id": "s1", "result": "ITEM: a:1\nRESULT: DONE"})
        self.assertEqual(cf.harvest(path, rc=1)[2], "ERROR")
        self.assertEqual(cf.harvest(path, rc=cf.TIMEOUT_RC)[2], "TIMEOUT")
        self.assertEqual(cf.harvest(path, rc=0)[2], "DONE")

    def test_an_error_flag_reads_as_error(self):
        for extra in ({"is_error": True}, {"subtype": "error_during_execution"}):
            path = self.log({"session_id": "s1", "result": "RESULT: DONE", **extra})
            self.assertEqual(cf.harvest(path)[2], "ERROR", extra)

    def test_a_stop_word_survives_an_error_end(self):
        path = self.log({"session_id": "s1", "result": "RESULT: BUDGET EXHAUSTED at act 1", "is_error": True})
        self.assertEqual(cf.harvest(path, rc=1)[2], "BUDGET EXHAUSTED")

    def test_an_error_end_never_reads_the_transcript(self):
        tmp = tempfile.mkdtemp(prefix="ccfleet-err-")
        self.addCleanup(subprocess.run, ["rm", "-rf", tmp])
        d = os.path.join(tmp, "projects", "-x")
        os.makedirs(d)
        wr(os.path.join(d, "s9.jsonl"), json.dumps({"type": "assistant", "timestamp": "2026-01-01T11:00:00Z",
                                                     "message": {"content": "ITEM: a:1\nRESULT: DONE"}}) + "\n")
        path = self.log({"session_id": "s9", "result": "usage limit reached"})
        with mock.patch.dict(os.environ, {"CLAUDE_CONFIG_DIR": tmp}):
            self.assertEqual(cf.harvest(path, rc=0)[2], "DONE", "the control: a clean end takes the fallback")
            self.assertEqual(cf.harvest(path, rc=1)[2], "ERROR")


class PrivateNameForms(unittest.TestCase):
    """FL23: only letters and digits continue a word, so the forms ccfleet
    itself builds around a name are caught."""
    cfg = {"private_names": ["privroot"], "repos": {"client-x": {"visibility": "private"}}}

    def test_joined_forms_are_caught(self):
        for text in ("/wts/privroot-1430/app", "/kits/privroot-kit/scratch/", "privroot_notes",
                     "atelier--privroot", "held/atelier--client-x--brief.md", "privroot.md"):
            self.assertTrue(cf.private_hits(self.cfg, text, "PUBLIC"), text)

    def test_a_longer_word_is_not_the_name(self):
        for text in ("privroots", "unprivroot", "privroot2", "client-xy"):
            self.assertEqual(cf.private_hits(self.cfg, text, "PUBLIC"), [], text)


class Locks(unittest.TestCase):
    """FL17: the driver lock cannot be taken twice, a dead holder leaves no
    stale lock, and an unwritable kit_dir is a refusal, not a traceback."""

    def setUp(self):
        self.kit = tempfile.mkdtemp(prefix="ccfleet-lock-")
        self.addCleanup(subprocess.run, ["rm", "-rf", self.kit])

    def test_a_second_taker_is_refused(self):
        with cf.DriverLock(self.kit):
            with self.assertRaises(cf.Refusal) as e:
                with cf.DriverLock(self.kit):
                    pass
            self.assertEqual(e.exception.code, cf.EXIT_SETUP)
            self.assertIn("one driver per kit_dir", str(e.exception))
        with cf.DriverLock(self.kit):  # released on exit
            pass

    def test_a_dead_holders_pid_is_no_lock(self):
        wr(os.path.join(self.kit, "driver.pid"), "999999")
        with cf.DriverLock(self.kit):
            self.assertEqual(rd(os.path.join(self.kit, "driver.pid")), str(os.getpid()))

    @unittest.skipIf(os.geteuid() == 0, "root ignores file modes")
    def test_an_unwritable_kit_dir_is_a_refusal(self):
        locked = os.path.join(self.kit, "ro")
        os.makedirs(locked)
        os.chmod(locked, 0o500)
        self.addCleanup(os.chmod, locked, 0o700)
        with self.assertRaises(cf.Refusal) as e:
            with cf.DriverLock(os.path.join(locked, "kit")):
                pass
        self.assertEqual(e.exception.code, cf.EXIT_SETUP)


class Children(unittest.TestCase):
    """FL17 and FL25: a dead driver's still-running children hold slots, and a
    stopping driver reports a hung child rather than wait forever."""

    def setUp(self):
        self.kit = tempfile.mkdtemp(prefix="ccfleet-kids-")
        self.addCleanup(subprocess.run, ["rm", "-rf", self.kit])
        self.cfg = {"kit_dir": self.kit, "session_timeout_minutes": 1}

    def test_an_earlier_drivers_live_child_holds_a_slot(self):
        kid = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)", "ccfleet-pass"])
        other = subprocess.Popen(["sleep", "60"])
        for p in (kid, other):
            self.addCleanup(p.wait)
            self.addCleanup(p.kill)
        wr(os.path.join(self.kit, "children.tsv"),
           f"{kid.pid}\t1\talpha 010\n{other.pid}\t1\tnot ours\n999999\t1\tgone\n")
        w = cf.Watch(self.cfg)
        self.assertEqual(w.held(), 1)
        self.assertIn("alpha 010", rd(os.path.join(self.kit, "driver.log")))
        kid.kill()
        kid.wait()
        self.assertEqual(w.held(), 0)

    def test_a_stopping_driver_gives_up_a_hung_child(self):
        w = cf.Watch(self.cfg)
        w.limit = 0
        p = mock.Mock(pid=4242)
        running = {p: {"label": "beta 020", "t0": time.time() - 5}}
        self.assertEqual(w.hung(running, stopping=False), [])
        self.assertIn(p, running, "not stopping: reported, still counted")
        self.assertEqual(w.hung(running, stopping=True), ["beta 020"])
        self.assertEqual(running, {})
        self.assertEqual(rd(os.path.join(self.kit, "driver.log")).count("hung: beta 020"), 1)


class Config(unittest.TestCase):
    """FL17: a config that cannot be read is exit 64 with a reason."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ccfleet-cfg-")
        self.addCleanup(subprocess.run, ["rm", "-rf", self.tmp])

    def run_check(self, text=None):
        path = os.path.join(self.tmp, "cfg.json")
        if text is not None:
            wr(path, text)
        return subprocess.run([sys.executable, TOOL, "--config", path, "check"], capture_output=True, text=True,
                              stdin=subprocess.DEVNULL,
                              env={**os.environ, "CLAUDE_CONFIG_DIR": os.path.join(self.tmp, "claude-config")})

    def test_unreadable_configs_exit_64(self):
        good = {"kit_dir": self.tmp, "repos_root": self.tmp, "worktrees_root": self.tmp, "default_model": "m"}
        for text, said in ((None, "cannot read"), ("{not json", "not valid JSON"), ("[]", "JSON object"),
                           (json.dumps({**good, "reset_utc": "Monday noon"}), "reset_utc"),
                           (json.dumps({**good, "claude_args": "--x"}), "claude_args")):
            r = self.run_check(text)
            self.assertEqual(r.returncode, cf.EXIT_USAGE, (text, r.stderr))
            self.assertIn(said, r.stderr)
            self.assertNotIn("Traceback", r.stderr)

    def test_the_example_config_loads_and_bypasses_nothing(self):
        cfg = cf.load_config(os.path.join(HERE, "ccfleet.example.json"))
        self.assertEqual(cf.permission_args(cfg)[1], False, "FL10: the example must not model the bypass")

    # What each shipped prompt gets from ccfleet's own command (beyond
    # ALWAYS_FILLED), and what its skill says is set per job or per call
    # (--set or a jobs field) rather than in the config's vars.
    SHIPPED = {
        "review/orchestrator-prompt.md": (cf.PASS_FILLED, set()),
        "review/resume-prompt.md": (cf.RESUME_FILLED, {"AGENT", "STATE"}),
        "review/fold-prompt.md": ({"ITEM", "REVIEW_LOG"}, {"BRIEF", "HELD"}),
        "fleet/worker-prompt.md": (set(), set()),
        "fleet/adopt-prompt.md": (set(), set()),
        "fleet/task-prompt.md": (set(), {"TASK"}),
        "fleet/brief-prompt.md": (set(), {"ITEM", "SUBJECT", "SOURCE", "QUOTE", "NOTE"}),
    }
    # A skill is a subject folder: a router (SKILL.md) and one file per action.
    # The variables table of a subject's prompts lives in the action that
    # fills them, not in the router.
    ACTION_FILE = {"review": "run.md", "fleet": "sweep.md"}

    def test_the_example_vars_fill_every_shipped_prompt(self):
        """FL12: an adopter who copies the example config, and sets what each
        skill names per job or per call, leaves no placeholder of any shipped
        prompt unfilled; every per-call name is in its skill's table."""
        cfg = cf.load_config(os.path.join(HERE, "ccfleet.example.json"))
        skills = os.path.join(os.path.dirname(HERE), "skills")
        shipped = {f"{d}/{f}" for d in sorted(self.ACTION_FILE)
                   for f in os.listdir(os.path.join(skills, d)) if f.endswith("-prompt.md")}
        self.assertEqual(shipped, set(self.SHIPPED), "a prompt was added or removed: list it here")
        for rel, (by_command, per_call) in sorted(self.SHIPPED.items()):
            names = set(cf.PLACEHOLDER.findall(rd(os.path.join(skills, rel))))
            unset = names - cf.ALWAYS_FILLED - by_command - per_call - set(cfg["vars"])
            self.assertEqual(sorted(unset), [], rel)
            subject = rel.split("/")[0]
            self.assertTrue(os.path.isfile(os.path.join(skills, subject, "SKILL.md")), f"{subject}: no router")
            skill = rd(os.path.join(skills, subject, self.ACTION_FILE[subject]))
            for name in sorted(per_call | (names - cf.ALWAYS_FILLED - by_command)):
                self.assertIn(f"`{name}`", skill,
                              f"{rel}: {name} is not in {self.ACTION_FILE[subject]}'s variables table")


class HelpAndManual(unittest.TestCase):
    """The two-register convention: --help is a digest that points at the man
    page, and the page covers every flag --help prints."""
    SUBCOMMANDS = ["check", "gate", "run", "drive", "drain", "plan", "pass", "resume"]

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
