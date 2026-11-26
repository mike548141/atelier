"""Tests for the ccfleet findings of the DP cold pass (210/630) on the session
settings copy, the reference queue and the instructions file's imports:
DP3, DP4, DP5 (mutants M1, M8, M9, M11), DP8 and DP18. They borrow the
throwaway repos (alpha public, beta private), stand-in claude and helpers of
test_ccfleet, imported, not copied. Every name here is fictional."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import test_ccfleet as base  # noqa: E402  (its classes are borrowed, not imported, so they run once)

cf, TOOL, md, wr, rd = base.cf, base.TOOL, base.md, base.wr, base.rd


class DPSettings(unittest.TestCase):
    """DP3, DP4, DP5 (M1, M8, M9) and DP18, end to end on test_ccfleet's
    fixtures."""
    setUp, tearDown = base.EndToEnd.setUp, base.EndToEnd.tearDown
    write_cfg, cli, calls, worktrees = (base.EndToEnd.write_cfg, base.EndToEnd.cli, base.EndToEnd.calls,
                                        base.EndToEnd.worktrees)
    new_wt = base.Wave2.new_wt
    wait_for, start_pass = base.RKLifecycle.wait_for, base.RKLifecycle.start_pass
    instructions, appended = base.RKImports.instructions, staticmethod(base.RKImports.appended)

    def settings_of(self, call):
        return json.loads(call["files"]["--settings"])

    # ----- DP3 -----

    def test_dp3_every_session_denies_reading_the_folder_of_copies_and_records(self):
        """DP3: public and private sessions alike deny Read of
        <kit_dir>/settings/ and <kit_dir>/sessions/, by the path the config
        names and by its real path (the kit folder is reached through a link
        here, so the two differ)."""
        real = os.path.join(self.tmp, "kit-real")
        os.makedirs(real)
        link = os.path.join(self.tmp, "kit-link")
        os.symlink(real, link)
        self.cfg["kit_dir"] = link
        self.write_cfg()
        self.instructions(md("Shared rules.", "@CLAUDE-private.md"), {"CLAUDE-private.md": "Private rules.\n"})
        for repo in ("alpha", "beta"):
            r = self.cli("run", repo, "--prompt", self.prompt)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        for call in self.calls():
            deny = self.settings_of(call)["permissions"]["deny"]
            for d in ("settings", "sessions"):
                for root in (link, os.path.realpath(real)):
                    self.assertIn(f"Read(/{os.path.join(root, d)}/**)", deny, (call["cwd"], deny))

    # ----- DP4 -----

    def test_dp4_auto_memory_is_off_for_a_public_or_unknown_repo_only(self):
        """DP4: a public repo's launch, and an unknown repo's settings copy,
        switch auto memory off by the setting and by the variable; a private
        repo's copy carries neither."""
        self.cfg["env"] = {"FLEET": "1"}
        self.write_cfg()
        for repo in ("alpha", "beta"):
            r = self.cli("run", repo, "--prompt", self.prompt)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        public, private = (self.settings_of(c) for c in self.calls())
        self.assertIs(public.get("autoMemoryEnabled"), False, public)
        self.assertEqual(public["env"], {"CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1"}, public)
        self.assertNotIn("autoMemoryEnabled", private)
        self.assertNotIn("CLAUDE_CODE_DISABLE_AUTO_MEMORY", private.get("env", {}))
        # An unknown repo's copy, written as the launch writes it.
        cfg = cf.load_config(self.cfgpath)
        with mock.patch.dict(os.environ, {"CLAUDE_CONFIG_DIR": self.env["CLAUDE_CONFIG_DIR"]}):
            spath, _ = cf.session_files(cfg, "sess-unknown", "UNKNOWN")
        try:
            unknown = json.loads(rd(spath))
        finally:
            os.remove(spath)
        self.assertIs(unknown.get("autoMemoryEnabled"), False, unknown)
        self.assertEqual(unknown["env"]["CLAUDE_CODE_DISABLE_AUTO_MEMORY"], "1")

    # ----- DP5: M8 -----

    def test_dp5_m8_an_import_in_a_linked_config_folder_is_denied_by_both_names(self):
        """M8: the deny rule is written for the path the import resolves to
        and for its real path; a config folder reached through a link has two
        names, and each is denied."""
        real = os.path.join(self.tmp, "config-real")
        link = os.path.join(self.tmp, "config-link")
        os.makedirs(real)
        os.symlink(real, link)
        self.env["CLAUDE_CONFIG_DIR"] = link
        self.instructions(md("Shared rules.", "@CLAUDE-private.md"), {"CLAUDE-private.md": "Private rules.\n"})
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        deny = self.settings_of(self.calls()[0])["permissions"]["deny"]
        self.assertIn("Read(/" + os.path.join(link, "CLAUDE-private.md") + ")", deny)
        self.assertIn("Read(/" + os.path.join(os.path.realpath(real), "CLAUDE-private.md") + ")", deny)

    # ----- DP5: M1 and M9, beside a session a signal left running -----

    def signalled_pass(self):
        """A pass on beta whose launcher a SIGTERM stopped: its session runs on.
        Returns (session id, its two copies' paths, its worktree, kit)."""
        wr(self.prompt, "Pass {ITEM}\n")
        conf = self.env["CLAUDE_CONFIG_DIR"]
        os.makedirs(conf, exist_ok=True)
        wr(os.path.join(conf, "CLAUDE.md"), "rules\n")
        kit = {"kit_dir": os.path.join(self.tmp, "kit")}
        p, out, sid = self.start_pass({**self.env, "FAKE_SLEEP": "30"})
        self.wait_for(lambda: cf.live_session(kit, sid) and self.calls(), "the session to start")
        p.send_signal(subprocess.signal.SIGTERM)
        self.assertEqual(p.wait(timeout=30), 128 + subprocess.signal.SIGTERM)
        sdir = os.path.join(self.tmp, "kit", "settings")
        copies = sorted(os.path.join(sdir, n) for n in os.listdir(sdir) if n.startswith(sid + "."))
        self.assertEqual(len(copies), 2, copies)
        (wt,) = self.worktrees()
        pid = cf.live_session(kit, sid)
        self.assertTrue(pid, "the session runs on")
        self.addCleanup(lambda: subprocess.run(["kill", "-KILL", f"-{pid}"], capture_output=True))
        return sid, copies, wt, kit

    def test_dp5_m1_an_unrelated_launch_keeps_a_running_sessions_copies(self):
        """M1: a launch's sweep leaves the copies a live session record holds,
        though their launcher is gone."""
        sid, copies, _, kit = self.signalled_pass()
        other = os.path.join(self.tmp, "other.md")
        wr(other, "Work on {REPO}.\n")
        r = self.cli("run", "alpha", "--prompt", other)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(len(self.calls()), 2, "the unrelated launch ran, and with it the sweep")
        self.assertTrue(cf.live_session(kit, sid), "the signalled session still ran through the sweep")
        for c in copies:
            self.assertTrue(os.path.exists(c), c)

    def test_dp5_m9_a_resume_of_another_session_is_refused_beside_a_live_one(self):
        """M9: a resume into a worktree a live session runs in is refused,
        whatever session id it resumes."""
        sid, _, wt, _ = self.signalled_pass()
        r = self.cli("resume", "beta", wt, "sess-other", "--prompt", self.prompt)
        self.assertEqual(r.returncode, cf.EXIT_CLAIM, r.stdout + r.stderr)
        self.assertIn(f"session {sid} still runs in", r.stderr)
        self.assertEqual(len(self.calls()), 1, "only the pass's own session started")

    # ----- DP18 -----

    SHAPES = md("Shared rules.", "1. @one.md", "> @two.md", "## @three.md", "- [ ] @four.md",
                "@five.md and more text", "See @six.md, then go on.", "`@seven.md` is a code span",
                "mail someone@example.invalid")  # leakscan:allow:email: a reserved, fictional address
    FILES = {f"{n}.md": f"Body of {n}.\n" for n in ("one", "two", "three", "four", "five", "six", "seven")}

    def test_dp18_every_import_shape_is_withheld_and_denied_and_check_counts_them(self):
        """DP18: a numbered item, a block quote, a heading and a task-list item
        are import lines (inlined for a private repo); an import followed by
        other text or inside a sentence is withheld from a public repo's
        session and denied; a code span is no import; `check` counts six and
        says what each visibility gets."""
        d = self.instructions(self.SHAPES, self.FILES)
        r = self.cli("run", "alpha", "--prompt", self.prompt)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        call = self.calls()[0]
        text = self.appended(call)
        for n in ("one", "two", "three", "four", "five", "six"):
            self.assertNotIn(f"{n}.md", text, text)
            self.assertNotIn(f"Body of {n}.", text)
            self.assertIn("Read(/" + os.path.join(d, f"{n}.md") + ")", self.settings_of(call)["permissions"]["deny"])
        self.assertIn(f"{cf.WITHHELD_TOKEN} and more text", text)
        self.assertIn(f"See {cf.WITHHELD_TOKEN} then go on.", text)
        self.assertIn("`@seven.md` is a code span", text)
        self.assertIn("mail someone@example.invalid", text)  # leakscan:allow:email: a reserved, fictional address
        self.assertEqual(text.count(cf.WITHHELD_IMPORT), 4)
        r = self.cli("run", "beta", "--prompt", self.prompt)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        private = self.appended(self.calls()[1])
        for n in ("one", "two", "three", "four"):
            self.assertIn(f"Body of {n}.", private)
        self.assertIn("@five.md and more text", private, "left as text for a private session")
        out = self.cli("check").stdout
        self.assertIn("Imports found: 6.", out)
        self.assertIn("INSTRUCTIONS IMPORT: @one.md -> " + os.path.join(d, "one.md") + ": inlined for a private "
                      "repo's session; withheld, and Read of it denied, for a public or unknown one's", out)
        self.assertIn("INSTRUCTIONS IMPORT: @six.md, -> " + os.path.join(d, "six.md") + ": inside a line of text",
                      out)


class DPQueue(unittest.TestCase):
    """DP5 (M11) and DP8 on the reference queue: `take` makes the checks
    `next` makes, and `next` offers by route, fit and writer."""
    setUp, tearDown = base.EndToEnd.setUp, base.EndToEnd.tearDown
    write_cfg, cli, calls = base.EndToEnd.write_cfg, base.EndToEnd.cli, base.EndToEnd.calls
    REF = base.RKGrant.REF
    ref_queue, ref, seal, GOOD = base.RKGrant.ref_queue, base.RKGrant.ref, base.RKGrant.seal, base.RKGrant.GOOD

    TWO = {"local": {"open": True, "lapses_utc": "2099-01-01T00:00"},
           "credit": {"open": True, "lapses_utc": "2099-02-01T00:00"}}

    def add_review(self, **r):
        state = json.loads(rd(self.state))
        state["reviews"].append({"repo": "alpha", "brief": "docs/brief.md", "title": "t", **r})
        wr(self.state, json.dumps(state))

    def offers(self, route, by="orch-1"):
        skip = os.path.join(self.tmp, f"skip-{route}.txt")
        wr(skip, "")
        out = []
        for _ in range(6):
            r = self.ref("next", "--skip-file", skip, "--by", by, "--route", route)
            self.assertEqual(r.returncode, 0, r.stderr)
            if not r.stdout.strip():
                return out
            out.append(":".join(r.stdout.split("\t")[:2]))
            wr(skip, r.stdout, mode="a")
        return out

    def take(self, target, *more, by="orch-1"):
        return self.ref("take", target, "--by", by, "--brief", "docs/brief.md", *more)

    def test_dp5_m11_a_review_briefed_after_the_seal_runs_on_local_only(self):
        """M11: a review briefed after the seal that fits both routes is
        offered last on the local route and not at all on another."""
        self.ref_queue(routes=self.TWO)
        self.assertEqual(self.seal(self.GOOD).returncode, 0)
        self.add_review(item="030", fits=["credit", "local"], briefed_by="writer-2")
        self.assertEqual(self.offers("local"), ["alpha:010", "beta:020", "alpha:030"])
        self.assertEqual(self.offers("credit"), [], "an unplanned pass on another route")
        self.assertNotEqual(self.take("alpha:030", "--route", "credit").returncode, 0)

    def test_dp8_next_and_take_keep_the_route_the_fit_and_the_writer_rule(self):
        self.ref_queue(routes=self.TWO)
        self.assertEqual(self.seal(self.GOOD).returncode, 0)
        # The sealing run writes a brief after it sealed: not its to run.
        self.add_review(item="040", fits=["local"], briefed_by="orch-1")
        # Briefed after the seal for the credit route only.
        self.add_review(item="050", fits=["credit"], briefed_by="writer-2")
        self.assertEqual(self.offers("local"), ["alpha:010", "beta:020"])
        for item, said in (("040", "briefed by this session"), ("050", "not fitting local")):
            r = self.take(f"alpha:{item}")
            self.assertEqual(r.returncode, 1, (item, r.stderr))
            self.assertIn(said, r.stderr)
        self.assertEqual(self.take("alpha:010").returncode, 0, "the control: a local review is taken")
        # Sealed to credit, which lapses after local: the spill is open by the
        # lapse times, but a review that does not fit local never spills.
        reviews = [{"repo": "alpha", "item": "060", "brief": "docs/brief.md", "title": "t", "fits": ["credit"],
                    "briefed_by": "w"},
                   {"repo": "beta", "item": "070", "brief": "docs/brief.md", "title": "t",
                    "fits": ["credit", "local"], "briefed_by": "w"}]
        ranking = [{"repo": "alpha", "item": "060", "route": "credit", "why": "first"},
                   {"repo": "beta", "item": "070", "route": "credit", "why": "second"}]
        self.ref_queue(reviews=reviews, routes=self.TWO)
        self.assertEqual(self.seal(ranking).returncode, 0)
        self.assertEqual(self.offers("local"), ["beta:070"], "only the spill that fits local")
        self.assertEqual(self.take("alpha:060").returncode, 1)
        # Sealed to credit, which lapses first: credit keeps it, by `next`
        # and by `take`, and so by a pass started by hand.
        early = {"local": {"open": True, "lapses_utc": "2099-02-01T00:00"},
                 "credit": {"open": True, "lapses_utc": "2099-01-01T00:00"}}
        self.ref_queue(reviews=reviews, routes=early)
        self.assertEqual(self.seal(ranking).returncode, 0)
        self.assertEqual(self.offers("local"), [])
        r = self.cli("pass", "beta", "070", "docs/brief.md")
        self.assertEqual(r.returncode, cf.EXIT_CLAIM, r.stdout + r.stderr)
        self.assertIn("is not route local's to run now", r.stdout)
        self.assertEqual(self.calls(), [], "no session started")
        self.assertEqual(self.take("beta:070", "--route", "credit").returncode, 0, "credit takes its own")


if __name__ == "__main__":
    unittest.main()
