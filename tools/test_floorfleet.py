"""Tests for tools/floorfleet.py — the estate conformance board.

This tool is the answer to "how do we know the policy actually landed, for
current and future repos". Its whole value is that it reports absences, so the
failure that matters is not a crash — it is a **false green**: a repo reported as
wired when it is not, or reported at all when it should have been flagged.

The classification tests below are all shaped around that. In particular:

  - A correctly-wired child's floor.yml has a HEADER that talks about scanners
    (it explains why it names none). If prose counted, every correctly-wired
    repo would report as a stale vendored copy — the tool would be exactly wrong,
    everywhere, and loudly enough that someone would switch it off.
  - An adopter pointing at their own atelier fork is still wired. The doctrine
    travels; the GitHub account is this estate's instance of it.

Zero third-party deps, same as the rest of the suite.
"""

import base64
import contextlib
import inspect
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import floorfleet  # noqa: E402
import leakscan  # noqa: E402  — to pin that the board reuses its term lookup

THIN_CALLER = """\
name: floor

# THIS FILE NAMES NO SCANNER, AND THAT IS THE POINT. It used to be a 247-line
# copy listing secretscan.py, leakscan.py, sizescan.py and the rest.
jobs:
  floor:
    uses: mike548141/atelier/.github/workflows/floor.yml@main
    with:
      sign-boundary: ""
"""

VENDORED = """\
name: floor
jobs:
  floor:
    steps:
      - name: secretscan
        run: python3 atelier/tools/secretscan.py --root repo repo
      - name: leakscan
        run: python3 atelier/tools/leakscan.py --root repo repo
"""


class ClassifyTest(unittest.TestCase):
    def test_thin_caller_is_wired(self):
        self.assertEqual(floorfleet.classify(THIN_CALLER)[0], "wired")

    def test_header_prose_naming_scanners_does_not_read_as_vendored(self):
        """The single most dangerous false positive: the shipped template's own
        header explains that it names no scanner, by naming several. If comments
        counted, every correctly-wired repo in the estate would report red."""
        self.assertIn("secretscan.py", THIN_CALLER, "fixture must exercise this")
        self.assertEqual(floorfleet.classify(THIN_CALLER)[0], "wired")

    def test_vendored_copy_is_flagged(self):
        state, detail = floorfleet.classify(VENDORED)
        self.assertEqual(state, "vendored")
        self.assertIn("stale", detail)

    def test_pinned_caller_is_distinguished_from_floating(self):
        """A pin is a legitimate, deliberate choice — but it freezes propagation,
        so it must not be reported identically to a floating caller."""
        state, detail = floorfleet.classify(THIN_CALLER.replace("@main", "@abc1234"))
        self.assertEqual(state, "pinned")
        self.assertIn("frozen", detail)

    def test_adopter_fork_is_still_wired(self):
        forked = THIN_CALLER.replace("mike548141", "another-owner")
        self.assertEqual(floorfleet.classify(forked)[0], "wired")

    def test_absent_floor_is_flagged(self):
        state, detail = floorfleet.classify(None)
        self.assertEqual(state, "absent")
        self.assertIn("enforces nothing", detail)

    def test_unrecognised_floor_is_not_silently_green(self):
        """Neither a caller nor a copy. Reporting this as wired would be the
        false green the whole tool exists to prevent."""
        state, _ = floorfleet.classify("name: floor\njobs:\n  x:\n    steps: []\n")
        self.assertEqual(state, "unknown")
        self.assertNotIn(state, ("wired", "pinned"))

    def test_only_wired_and_pinned_count_as_ok(self):
        for state in ("vendored", "absent", "unknown"):
            info = floorfleet.ChildFloor("r", "/r", state, "")
            self.assertFalse(info.ok, f"{state} must not count as conforming")
        for state in ("wired", "pinned"):
            info = floorfleet.ChildFloor("r", "/r", state, "")
            self.assertTrue(info.ok)


class EvaluateTest(unittest.TestCase):
    """Reading a real repo directory, including its declarations."""

    def _repo(self, tmp: str, floor: str | None, config: dict | None = None) -> Path:
        repo = Path(tmp) / "child"
        (repo / ".github" / "workflows").mkdir(parents=True)
        if floor is not None:
            (repo / ".github" / "workflows" / "floor.yml").write_text(floor)
        if config is not None:
            (repo / floorfleet.CONFIG_PATH).write_text(json.dumps(config))
        return repo

    def test_reports_declared_opt_outs(self):
        """The declarations are the point of making non-enforcement visible —
        if the board didn't surface them, declaring would be no better than
        deleting a line."""
        with tempfile.TemporaryDirectory() as td:
            repo = self._repo(td, THIN_CALLER, {
                "advisory": ["wrapscan"],
                "disabled": {"spellscan": "no prose in this repo"},
            })
            info = floorfleet.evaluate(repo, remote=False)
        self.assertEqual(info.state, "wired")
        # Pre-C1 bare-list spelling: empty why and empty review-by, which is
        # exactly what marks it unmigrated on the board.
        self.assertEqual(info.advisory, {"wrapscan": ("", "")})
        self.assertEqual(info.disabled, {"spellscan": "no prose in this repo"})

    def test_reports_a_repos_own_declared_checks(self):
        """A local check is the one class of check no OTHER repo's board will
        ever mention — its code is repo-specific by construction. If the board
        skipped it, the estate's only view of that rule would be the repo
        itself, which is the pre-ADR-0008 position in miniature."""
        with tempfile.TemporaryDirectory() as td:
            repo = self._repo(td, THIN_CALLER, {
                "local": {"tripwire": {"run": "tools/tripwire.py",
                                       "why": "estate tokens never enter a commit"}},
            })
            info = floorfleet.evaluate(repo, remote=False)
        self.assertEqual(info.local, {"tripwire": "estate tokens never enter a commit"})
        self.assertIn("➕ tripwire local", floorfleet.render([info], remote=False))

    def test_reports_cover_reductions_not_only_removals(self):
        """ADR 0008 cold pass, EP1/EP2: `scope` and `flags` narrow a check
        without removing it, and were the one softening no board read — so a
        boundary check could be reduced to a subtree, or to nothing, and read
        green estate-wide. floor.py's own docstring claimed otherwise."""
        with tempfile.TemporaryDirectory() as td:
            repo = self._repo(td, THIN_CALLER, {
                "scope": {"leakscan": ["subtree/"]},
                "flags": {"leakscan": ["--disable", "ipv4"]},
            })
            info = floorfleet.evaluate(repo, remote=False)
        self.assertEqual(info.scope, {"leakscan": ["subtree/"]})
        self.assertEqual(info.flags, {"leakscan": ["--disable", "ipv4"]})
        board = floorfleet.render([info], remote=False)
        self.assertIn("🔎 leakscan scoped to subtree/", board)
        self.assertIn("🔧 leakscan flags --disable ipv4", board)

    def test_a_moved_records_tree_is_reported_but_the_default_is_not(self):
        """A non-default `docs` silently re-points every docs-scoped check. The
        default is the other half: printing it for all 13 children would be
        noise that buries the one child that moved."""
        with tempfile.TemporaryDirectory() as td:
            moved = floorfleet.evaluate(
                self._repo(td, THIN_CALLER, {"docs": "records"}), remote=False)
        with tempfile.TemporaryDirectory() as td:
            plain = floorfleet.evaluate(
                self._repo(td, THIN_CALLER, {"docs": floorfleet.DEFAULT_DOCS}),
                remote=False)
        self.assertIn("📁 records tree is records", floorfleet.render([moved], False))
        self.assertNotIn("📁", floorfleet.render([plain], False))

    def test_a_malformed_scope_block_does_not_crash_the_board(self):
        """Same contract as the local block below: report what the config SAYS,
        stay readable against a malformed one, and let floor.py do the blocking
        where the repo actually is."""
        with tempfile.TemporaryDirectory() as td:
            repo = self._repo(td, THIN_CALLER,
                              {"scope": {"a": 7, "b": "bare-string"}, "flags": []})
            info = floorfleet.evaluate(repo, remote=False)
        self.assertEqual(info.scope, {"b": ["bare-string"]})
        self.assertEqual(info.flags, {})

    def test_a_malformed_local_block_does_not_crash_the_board(self):
        """floor.py blocks on a bad config, where the repo is. This tool reads
        text off a default branch and must still render the other 12 children —
        a board that dies on one repo's typo reports nothing about any of them."""
        with tempfile.TemporaryDirectory() as td:
            repo = self._repo(td, THIN_CALLER, {"local": {"t": "not-an-object"}})
            info = floorfleet.evaluate(repo, remote=False)
        self.assertEqual(info.local, {"t": ""})
        self.assertIn("no reason declared", floorfleet.render([info], remote=False))

    def test_unreadable_config_is_surfaced_not_swallowed(self):
        with tempfile.TemporaryDirectory() as td:
            repo = self._repo(td, THIN_CALLER)
            (repo / floorfleet.CONFIG_PATH).write_text("{ broken")
            info = floorfleet.evaluate(repo, remote=False)
        self.assertIn("unreadable", info.detail)

    def test_a_repo_with_no_declarations_file_still_renders(self):
        """Found while applying FS1. `advisory` was initialised as a bare list
        and only became the C1 dict when a config was read, so a child carrying
        no `.atelier-floor.json` crashed `render` with an AttributeError — the
        board taken down by the very absence it exists to report. Every child on
        this estate happens to carry the file, so nothing walked the path."""
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "bare"
            repo.mkdir()
            info = floorfleet.evaluate(repo, remote=False)
        self.assertEqual(info.advisory, {})
        self.assertIn("bare", floorfleet.render([info], remote=False))

    def test_missing_floor_reports_absent(self):
        with tempfile.TemporaryDirectory() as td:
            info = floorfleet.evaluate(self._repo(td, None), remote=False)
        self.assertEqual(info.state, "absent")


class TrackedShimTest(unittest.TestCase):
    """The tracked shim is a file in the REPO, so unlike the installed hook it
    is answerable on the remote plane. This is the half of the hook question
    git actually transports; only core.hooksPath stays machine-local."""

    def _repo(self, tmp: str, shim: str | None) -> Path:
        repo = Path(tmp) / "child"
        (repo / ".github" / "workflows").mkdir(parents=True)
        (repo / ".github" / "workflows" / "floor.yml").write_text(THIN_CALLER)
        if shim is not None:
            p = repo / floorfleet.SHIM_PATH
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(shim)
        return repo

    def test_shim_routing_through_the_registry_is_current(self):
        with tempfile.TemporaryDirectory() as td:
            repo = self._repo(td, "#!/bin/sh\nexec python3 tools/floor.py --plane hook\n")
            self.assertEqual(floorfleet.evaluate(repo, remote=False).shim, "current")

    def test_shim_naming_scanners_itself_is_legacy(self):
        # The same distinction classify() draws for the workflow: a copy that
        # will go stale is not the same as calling the one registry.
        with tempfile.TemporaryDirectory() as td:
            repo = self._repo(td, "#!/bin/sh\npython3 tools/secretscan.py --staged\n")
            self.assertEqual(floorfleet.evaluate(repo, remote=False).shim, "legacy")

    def test_no_tracked_shim_is_absent(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(floorfleet.evaluate(self._repo(td, None), remote=False).shim,
                             "absent")

    def test_shim_gap_is_named_and_kept_distinct_from_the_local_hook(self):
        # The two must not blur: one travels with a clone, the other never does,
        # and a reader who conflates them will over-claim on the remote plane.
        infos = [floorfleet.ChildFloor("a", "/a", "wired", "ok",
                                       hook="none", shim="absent")]
        out = floorfleet.render(infos, remote=True)
        self.assertIn("Tracked shim missing or stale", out)
        self.assertIn("Local hook gaps", out)
        self.assertIn("core.hooksPath never", out)

    def test_a_current_shim_reports_no_gap(self):
        infos = [floorfleet.ChildFloor("a", "/a", "wired", "ok",
                                       hook="tracked", shim="current")]
        out = floorfleet.render(infos, remote=True)
        self.assertNotIn("Tracked shim missing", out)


class ParentRowTest(unittest.TestCase):
    """atelier's own conformance — roadmap A5b.

    Discovery walks CHILDREN, so the repo that defines the floor was the one
    repo the board never checked. A parent that quietly dropped its own floor
    is exactly what ADR 0008 says enumeration must catch, and nothing would
    have. A5a was the other half of the same defect, where the parent genuinely
    was not running the floor it ships."""

    def _atelier(self, ci_body: str) -> Path:
        td = tempfile.mkdtemp()
        root = Path(td) / "atelier"
        (root / ".github" / "workflows").mkdir(parents=True)
        # The reusable workflow the children call. It proves nothing about
        # whether the parent runs the floor over ITSELF, which is the point.
        (root / ".github" / "workflows" / "floor.yml").write_text(
            "jobs:\n  floor:\n    steps:\n"
            "      - run: python3 atelier/tools/floor.py --plane ci --root repo\n")
        (root / ".github" / "workflows" / "ci.yml").write_text(ci_body)
        return root

    def test_a_parent_that_runs_its_own_floor_is_wired(self):
        root = self._atelier("jobs:\n  t:\n    steps:\n"
                             "      - run: python3 tools/floor.py --plane ci --root .\n")
        info = floorfleet.evaluate_parent(root)
        self.assertEqual(info.state, "wired")
        self.assertTrue(info.ok)
        self.assertTrue(info.is_parent)

    def test_a_parent_that_ships_the_floor_and_drops_it_is_caught(self):
        root = self._atelier("jobs:\n  t:\n    steps:\n      - run: echo nothing\n")
        info = floorfleet.evaluate_parent(root)
        self.assertEqual(info.state, "absent")
        self.assertFalse(info.ok, "--check must red on this")
        self.assertIn("does not run it", info.detail)

    def test_the_reusable_workflow_alone_does_not_count_as_conformance(self):
        """floor.yml runs the floor over the CALLER's tree, never the parent's.
        Reading it as proof would be the exact self-exemption A5a was."""
        root = self._atelier("jobs:\n  t:\n    steps:\n      - run: echo nothing\n")
        self.assertEqual(floorfleet.evaluate_parent(root).state, "absent")

    def test_the_parent_is_not_counted_among_the_children(self):
        parent = floorfleet.ChildFloor(name="atelier (parent)", path="/a",
                                       state="wired", detail="d", is_parent=True)
        child = floorfleet.ChildFloor(name="kid", path="/k",
                                      state="wired", detail="d")
        board = floorfleet.render([parent, child], remote=False)
        self.assertIn("all 1 children", board)
        # ...and it leads the board: a reader wants the parent and the failures
        # before the rows that are fine.
        rows = [ln for ln in board.splitlines() if "wired" in ln]
        self.assertIn("(parent)", rows[0])

    def test_the_parents_remedy_is_stated_separately(self):
        """The "wire a thin caller" advice does not fit the parent — it holds
        the reusable workflow rather than calling one."""
        parent = floorfleet.ChildFloor(name="atelier (parent)", path="/a",
                                       state="absent", detail="d", is_parent=True)
        board = floorfleet.render([parent], remote=False)
        self.assertIn("PARENT's remedy is different", board)
        self.assertIn("--plane ci --root .", board)

    def test_the_row_is_named_for_the_repo_not_the_worktree(self):
        """This repo's own doctrine says take a worktree for write-heavy work,
        so the naive basename would mislabel the parent row on exactly the
        sessions most likely to be changing the floor."""
        with tempfile.TemporaryDirectory() as td:
            main = Path(td) / "atelier"
            main.mkdir()
            subprocess.run(["git", "-C", str(main), "init", "-q"], check=True)
            (main / "f").write_text("x")
            for args in (["add", "f"],
                         ["-c", "user.email=t@example.invalid",  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
                          "-c", "user.name=t", "commit", "-qm", "x"]):
                subprocess.run(["git", "-C", str(main), *args], check=True)
            wt = Path(td) / "wt-scratch-name"
            subprocess.run(["git", "-C", str(main), "worktree", "add", "-q",
                            str(wt), "-b", "scratch"], check=True)
            self.assertEqual(floorfleet._repo_name(wt), "atelier")


class TermsStateTest(unittest.TestCase):
    """The personal-data half of leakscan, reported as a MACHINE fact.

    A per-child column would have been the wrong shape: the term list lives in
    ~/.claude/, outside every repo, so it is identical for all of them. It goes
    on the board once, and it is what turns "the hook has full cover" from an
    inference off the block into something an operator can see first."""

    def _render_with(self, terms: str | None) -> str:
        env = dict(os.environ)
        env.pop("ATELIER_LEAKSCAN_TERMS", None)
        if terms is not None:
            env["ATELIER_LEAKSCAN_TERMS"] = terms
        else:
            env["HOME"] = tempfile.mkdtemp()
        with mock.patch.dict(os.environ, env, clear=True):
            return floorfleet.render([], remote=False)

    def test_a_present_list_is_reported_as_full_cover(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "terms.txt"
            p.write_text("zzz-nonsense-term\n", encoding="utf-8")
            board = self._render_with(str(p))
        self.assertIn("✅ personal-data term list", board)
        self.assertIn("full cover on this machine", board)

    def test_an_absent_list_is_reported_with_the_remedy(self):
        board = self._render_with(None)
        self.assertIn("❌ personal-data term list", board)
        # Naming the consequence matters as much as the state: an operator who
        # reads only "absent" does not know their next commit will block.
        self.assertIn("BLOCKS", board)
        self.assertIn("leakscan-terms.example.txt", board)

    def test_the_board_asks_leakscan_rather_than_reimplementing_the_lookup(self):
        """Two lookups that can disagree is the two-lists bug this whole design
        exists to avoid — the board would report cover the scanner does not have."""
        self.assertIs(floorfleet.leakscan.resolve_terms_path,
                      leakscan.resolve_terms_path)


class RenderTest(unittest.TestCase):
    def test_unguarded_repos_are_named_not_just_counted(self):
        infos = [
            floorfleet.ChildFloor("good", "/good", "wired", "ok"),
            floorfleet.ChildFloor("bad", "/bad", "vendored", "will go stale"),
        ]
        out = floorfleet.render(infos, remote=False)
        self.assertIn("bad", out)
        self.assertIn("1 of 2", out)

    def test_all_clear_states_the_count(self):
        infos = [floorfleet.ChildFloor("a", "/a", "wired", "ok")]
        self.assertIn("all 1 children", floorfleet.render(infos, remote=False))


class InvocationTest(unittest.TestCase):
    def _run(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "floorfleet.py"), *args],
            capture_output=True, text=True,
        )

    def test_selftest_passes(self):
        self.assertEqual(self._run("--selftest").returncode, 0)

    def test_check_exits_nonzero_on_an_unguarded_child(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "child"
            (repo / ".github" / "workflows").mkdir(parents=True)
            (repo / ".github" / "workflows" / "floor.yml").write_text(VENDORED)
            r = self._run("--child", str(repo), "--check",
                          "--atelier", str(TOOLS_DIR.parent))
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)

    def test_nothing_discovered_is_an_error_not_a_green(self):
        """Fail-safe: an estate we could not enumerate must never read as
        'everything is fine'."""
        with tempfile.TemporaryDirectory() as td:
            r = self._run("--root", td, "--atelier", str(TOOLS_DIR.parent))
            self.assertEqual(r.returncode, 2)


class AdvisoryAgeingTest(unittest.TestCase):
    """C1 — the board is the whole forcing function for an expired advisory,
    because nothing blocks on a review date (ruled 2026-07-28). If it does not
    distinguish live from expired from unmigrated, the ruling has no teeth
    anywhere."""

    def test_both_spellings_are_read(self):
        self.assertEqual(floorfleet._advisories(["wrapscan"]),
                         {"wrapscan": ("", "")})
        self.assertEqual(
            floorfleet._advisories({"wrapscan": {"why": "adopting",
                                                 "review-by": "2026-12-01"}}),
            {"wrapscan": ("adopting", "2026-12-01")})

    def test_a_malformed_declaration_stays_readable(self):
        """Same contract as everything else the board reads: report what the
        config says, never crash on one. floor.py is what blocks on a bad
        config, and it runs where the repo is."""
        self.assertEqual(floorfleet._advisories("wrapscan"), {})
        self.assertEqual(floorfleet._advisories({"wrapscan": 7}),
                         {"wrapscan": ("", "")})

    def test_days_over_counts_rather_than_just_saying_expired(self):
        """'Expired' reads identically on day one and day two hundred, and it
        is the second that means the declaration was abandoned."""
        self.assertEqual(floorfleet._days_over("2026-07-01", "2026-07-01"), "today")
        self.assertEqual(floorfleet._days_over("2026-07-01", "2026-07-02"), "1 day over")
        self.assertEqual(floorfleet._days_over("2026-07-01", "2026-07-31"), "30 days over")
        self.assertEqual(floorfleet._days_over("nonsense", "2026-07-31"),
                         "date unreadable")

    def test_scope_paths_read_from_either_spelling(self):
        """A1(b)'s object form must not blind the 🔎 cover-reduction line — a
        board that stopped showing a narrowed boundary scope because the config
        gained a key would be the EP1/EP2 defect returning by the back door."""
        self.assertEqual(floorfleet._scope_paths({"leakscan": ["tiki/"]}),
                         {"leakscan": ["tiki/"]})
        self.assertEqual(
            floorfleet._scope_paths({"leakscan": {"paths": ["tiki/"],
                                                  "why": "vendor tree"}}),
            {"leakscan": ["tiki/"]})
        self.assertEqual(floorfleet._scope_paths({"leakscan": "tiki/"}),
                         {"leakscan": ["tiki/"]})

    def _render_one(self, advisory):
        info = floorfleet.ChildFloor(name="child", path="/x", state="wired",
                                     detail="calls atelier's floor @main",
                                     advisory=advisory)
        return floorfleet.render([info], remote=False)

    def test_the_three_states_render_differently(self):
        live = self._render_one({"wrapscan": ("adopting", "2999-01-01")})
        self.assertIn("advisory until 2999-01-01", live)
        self.assertNotIn("🔴", live)

        expired = self._render_one({"wrapscan": ("adopting", "2020-01-01")})
        self.assertIn("🔴", expired)
        self.assertIn("EXPIRED 2020-01-01", expired)
        self.assertIn("days over", expired)

        legacy = self._render_one({"wrapscan": ("", "")})
        self.assertIn("🟡", legacy)
        self.assertIn("migrate it", legacy)


class ParentWiringTest(unittest.TestCase):
    """TA5 — the parent classifier must read live YAML, not commented-out YAML.

    The board exists to catch a parent quietly dropping the floor it ships
    (A5b). Commenting a step out is the ordinary way anyone disables one, so a
    classifier that matches inside comments is green at the exact moment it is
    supposed to be red."""

    def test_a_commented_out_invocation_is_not_wired(self):
        yml = ("jobs:\n  floor:\n    steps:\n"
               "      # - run: python3 tools/floor.py --plane ci --root .\n")
        self.assertIsNone(
            floorfleet.PARENT_RUN_RE.search(floorfleet._live_yaml(yml)))

    def test_a_live_invocation_is_still_wired(self):
        yml = ("jobs:\n  floor:\n    steps:\n"
               "      - run: python3 tools/floor.py --plane ci --root .\n")
        self.assertIsNotNone(
            floorfleet.PARENT_RUN_RE.search(floorfleet._live_yaml(yml)))

    def test_a_trailing_comment_cannot_manufacture_a_match(self):
        """The half a line-start check would miss: a live step whose trailing
        comment mentions the invocation it replaced."""
        yml = "      - run: echo hi  # was: floor.py --plane ci --root .\n"
        self.assertIsNone(
            floorfleet.PARENT_RUN_RE.search(floorfleet._live_yaml(yml)))

    def test_a_hash_inside_quotes_is_not_a_comment(self):
        """And the over-correction: stripping every `#` would blind the
        classifier to a real step that happens to echo one."""
        yml = ('      - run: echo "#" && python3 tools/floor.py --plane ci\n')
        self.assertIsNotNone(
            floorfleet.PARENT_RUN_RE.search(floorfleet._live_yaml(yml)))


class WorktreeDiscoveryTest(unittest.TestCase):
    """TA7 — the board must work from a worktree, the mode this repo's own
    doctrine prescribes for write-heavy work. The default search root was the
    checkout's parent, which inside a worktree is `.claude/worktrees/` — so the
    board reported "no atelier children found" precisely when someone was
    changing the floor."""

    def test_main_checkout_resolves_through_a_worktree(self):
        with tempfile.TemporaryDirectory() as td:
            main = Path(td) / "estate" / "repo"
            main.mkdir(parents=True)
            # Identity without an address SHAPE: git takes any string here, and
            # a literal example address is what leakscan is built to stop —
            # including in test fixtures, where it is just as committed.
            for cmd in (["init", "-q"], ["config", "user.email", "fixture"],
                        ["config", "user.name", "fixture"]):
                subprocess.run(["git", "-C", str(main), *cmd], check=True,
                               capture_output=True)
            (main / "f").write_text("x")
            subprocess.run(["git", "-C", str(main), "add", "f"], check=True,
                           capture_output=True)
            subprocess.run(["git", "-C", str(main), "commit", "-qm", "i"],
                           check=True, capture_output=True)
            wt = main / ".claude" / "worktrees" / "scratch"
            subprocess.run(["git", "-C", str(main), "worktree", "add", "-q",
                            str(wt), "-b", "scratch"], check=True, capture_output=True)

            self.assertEqual(floorfleet.main_checkout(wt).resolve(), main.resolve())
            # The search root that follows from it: beside the main checkout,
            # where siblings actually live — not inside .claude/worktrees/.
            self.assertEqual(floorfleet.main_checkout(wt).parent.resolve(),
                             (Path(td) / "estate").resolve())
            # And it must be an identity for an ordinary checkout.
            self.assertEqual(floorfleet.main_checkout(main).resolve(), main.resolve())

    def test_a_non_repo_directory_falls_back_to_itself(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(floorfleet.main_checkout(Path(td)), Path(td))


class RunStatusTest(unittest.TestCase):
    """--status: the COMPLIANCE half (roadmap B2 + B3).

    The defect these close is one defect: a board that answers 'is the floor
    wired' while reading as though it answered 'is the floor working'. On the
    first live run of this code, 5 of 14 repos reported `wired ✅` and had been
    RED on their default branch for three days. Wiring is a fact about a FILE;
    a file cannot tell you the runner was ever switched on, or that it passed.

    `classify_run` is pure so every branch is driven offline — the selftest does
    that. What is tested here is the layer around it: that the gathering asks
    the right questions, that a missing permission degrades honestly instead of
    turning into a green, and that the exit code widens only when asked."""

    def _read(self, responses: dict):
        """Stand in for `gh api`, keyed by a substring of the endpoint.

        Longest key first: the runs endpoint contains the workflows endpoint as
        a prefix, so insertion order would silently hand the listing's payload
        to the runs call and every green case would read as `no-runs`."""
        def fake(path: str, *jq: str):
            for key in sorted(responses, key=len, reverse=True):
                if key in path:
                    return responses[key]
            return None
        return fake

    def _run_state(self, responses: dict, workflow: str = "floor.yml"):
        with mock.patch.object(floorfleet, "_slug", return_value="o/r"), \
             mock.patch.object(floorfleet, "_gh_json",
                               side_effect=self._read(responses)):
            return floorfleet.read_run(Path("/repo"), workflow)

    RUNS_KEY = "actions/workflows/floor.yml/runs"
    GREEN = {"workflow_runs": [{"status": "completed", "conclusion": "success",
                                "head_sha": "aaaa1111"}]}
    LISTING = {"workflows": [{"path": ".github/workflows/floor.yml",
                              "state": "active"}]}

    def test_a_green_run_on_the_current_head_is_passing(self):
        state, _, authority = self._run_state({
            "actions/permissions": {"enabled": True},
            "actions/workflows": self.LISTING,
            self.RUNS_KEY: self.GREEN,
            # The real payload shape. An earlier draft of this fixture returned
            # the bare sha, which is what the buggy `--jq .sha` call LOOKED like
            # it produced — so the mock agreed with the defect and the test
            # passed over it. A fixture that models the wrong contract proves
            # the wrong thing.
            "commits/main": {"sha": "aaaa1111"},
            "repos/o/r": {"default_branch": "main"},
        })
        self.assertEqual(state, "passing")
        self.assertEqual(authority, "repo-switch")

    def test_a_red_floor_is_not_reported_as_wired_and_fine(self):
        """The live finding, pinned: this is the case that was invisible."""
        state, detail, _ = self._run_state({
            "actions/permissions": {"enabled": True},
            "actions/workflows": self.LISTING,
            self.RUNS_KEY: {"workflow_runs": [
                {"status": "completed", "conclusion": "failure",
                 "head_sha": "aaaa1111"}]},
            "repos/o/r": {"default_branch": "main"},
        })
        self.assertEqual(state, "failing")
        self.assertIn("RED", detail)

    def test_actions_disabled_for_the_repo_is_read_authoritatively(self):
        state, detail, authority = self._run_state({
            "actions/permissions": {"enabled": False},
        })
        self.assertEqual(state, "actions-off")
        self.assertEqual(authority, "repo-switch")
        self.assertIn("DISABLED", detail)

    def test_a_missing_administration_permission_degrades_it_does_not_green(self):
        """B3's blind spot must stay closed on a token that CANNOT read the
        repo-level Actions switch — otherwise closing it would have cost a
        repo-settings permission across the whole private estate."""
        state, detail, authority = self._run_state({
            # No `actions/permissions` key: the read 403s and returns None.
            "actions/workflows": self.LISTING,
            self.RUNS_KEY: {"workflow_runs": []},
            "repos/o/r": {"default_branch": "main"},
        })
        self.assertEqual(state, "no-runs")
        self.assertEqual(authority, "inferred")
        self.assertNotIn(state, ("passing",))
        self.assertIn("NEVER run", detail)

    def test_a_workflow_disabled_by_hand_is_caught_without_the_switch(self):
        state, _, _ = self._run_state({
            "actions/workflows": {"workflows": [
                {"path": ".github/workflows/floor.yml",
                 "state": "disabled_manually"}]},
            self.RUNS_KEY: {"workflow_runs": []},
            "repos/o/r": {"default_branch": "main"},
        })
        self.assertEqual(state, "actions-off")

    def test_a_green_run_on_an_older_commit_is_behind_not_passing(self):
        state, detail, _ = self._run_state({
            "actions/permissions": {"enabled": True},
            "actions/workflows": self.LISTING,
            self.RUNS_KEY: self.GREEN,
            "repos/o/r": {"default_branch": "main"},
            "commits/main": {"sha": "bbbb2222"},
        })
        self.assertEqual(state, "behind")
        self.assertIn("unscanned", detail)

    def test_a_repo_with_no_remote_is_unknown_not_green(self):
        with mock.patch.object(floorfleet, "_slug", return_value=None):
            state, _, _ = floorfleet.read_run(Path("/repo"), "floor.yml")
        self.assertEqual(state, "unknown")

    def test_only_passing_counts_as_green(self):
        for state in ("failing", "actions-off", "no-runs", "unregistered",
                      "behind", "no-result", "running", "unknown"):
            info = floorfleet.ChildFloor("x", "/x", "wired", "", run=state)
            self.assertFalse(info.green, f"{state} must not count as green")
        self.assertTrue(
            floorfleet.ChildFloor("x", "/x", "wired", "", run="passing").green)

    def test_conformance_and_compliance_are_reported_separately(self):
        infos = [floorfleet.ChildFloor("a", "/a", "wired", "ok", run="failing",
                                       run_detail="RED"),
                 floorfleet.ChildFloor("b", "/b", "wired", "ok", run="passing",
                                       run_detail="green")]
        out = floorfleet.render(infos, remote=True, status=True)
        # Both claims present, and neither swallowed by the other.
        self.assertIn("all 2 children call atelier's floor", out)
        self.assertIn("NOT PROVEN GREEN", out)
        self.assertIn("1 of 2", out)

    def test_inferred_authority_is_declared_on_the_board(self):
        infos = [floorfleet.ChildFloor("a", "/a", "wired", "ok", run="passing",
                                       run_authority="inferred")]
        out = floorfleet.render(infos, remote=True, status=True)
        self.assertIn("INFERRED", out)
        self.assertIn("Administration", out)

    def test_a_read_authority_is_not_advertised_as_a_caveat(self):
        infos = [floorfleet.ChildFloor("a", "/a", "wired", "ok", run="passing",
                                       run_authority="repo-switch")]
        self.assertNotIn("INFERRED",
                         floorfleet.render(infos, remote=True, status=True))

    def test_an_unwired_repo_is_not_counted_under_wired_but_not_green(self):
        """FS2. `unproven` filtered every row, so a repo with no floor at all —
        run `unregistered` — was counted in the sentence that says 'are wired
        but NOT PROVEN GREEN'. The line built to be read first misdescribed
        exactly the worst rows."""
        infos = [floorfleet.ChildFloor("a", "/a", "wired", "ok", run="passing",
                                       run_detail="green"),
                 floorfleet.ChildFloor("b", "/b", "absent", "no floor.yml",
                                       run="unregistered",
                                       run_detail="never landed")]
        out = floorfleet.render(infos, remote=True, status=True)
        # The old line: "1 of 2 repo(s) are wired but NOT PROVEN GREEN",
        # counting the repo that is not wired at all.
        self.assertNotIn("NOT PROVEN GREEN", out)
        # The wired one is green, so the wired half is clean...
        self.assertIn("all 1 wired floor(s) are GREEN", out)
        # ...and the unwired one is still impossible to miss, in the
        # conformance block where it belongs, plus a note so the wired-only
        # denominator can never read as the whole estate.
        self.assertIn("1 of 2 repo(s) are NOT running atelier's floor", out)
        self.assertIn("not wired at all", out)

    def test_a_wired_but_red_repo_is_still_counted(self):
        infos = [floorfleet.ChildFloor("a", "/a", "wired", "ok", run="failing",
                                       run_detail="RED"),
                 floorfleet.ChildFloor("b", "/b", "absent", "no floor.yml",
                                       run="unregistered", run_detail="none")]
        out = floorfleet.render(infos, remote=True, status=True)
        self.assertIn("1 of 1 WIRED repo(s) are NOT PROVEN GREEN", out)

    def test_the_no_status_sentinel_collapses_to_conformance(self):
        """FS5's contract, as a unit test as well as a selftest leg: `run == ""`
        means --status was not asked for, NOT `unknown`, so `green` is `ok`."""
        self.assertTrue(
            floorfleet.ChildFloor("a", "/a", "wired", "", run="").green)
        self.assertFalse(
            floorfleet.ChildFloor("a", "/a", "absent", "", run="").green)
        self.assertIn("was not asked for", floorfleet.ChildFloor.green.__doc__)

    def test_read_run_is_annotated_with_what_it_returns(self):
        """FS4: annotated `tuple[str, str]`, returning three on every path."""
        hints = floorfleet.read_run.__annotations__
        self.assertEqual(str(hints["return"]).count("str"), 3)

    def test_without_status_the_board_is_unchanged(self):
        """--check's existing meaning must not move under anyone standing on
        it: conformance alone, exactly as before."""
        infos = [floorfleet.ChildFloor("a", "/a", "wired", "ok")]
        out = floorfleet.render(infos, remote=False)
        self.assertNotIn("run:", out)
        self.assertNotIn("PROVEN GREEN", out)


class RemoteDiscoveryTest(unittest.TestCase):
    """--from-github (roadmap B1): enumerate the estate from GitHub, not from
    whatever happens to be cloned beside this checkout.

    B1 assumed the scheduled conformance check was small wiring because
    `--remote` was assumed to be remote end-to-end. It was not: `--remote` read
    CONTENT remotely and still DISCOVERED children by listing directories, so on
    a GitHub runner it would have found nothing. Same shape as the defect this
    whole programme keeps finding — a check that looks like it covers something
    and does not."""

    @staticmethod
    def _reads(mapping):
        """Stand in for the CLAUDE.md read, keyed by slug.

        Values are (outcome, text) pairs — the three-outcome contract. A plain
        `None` return is exactly the conflation FS1(b) is about, so this helper
        will not let a test express one by accident."""
        def fake(slug, rel):
            return mapping.get(slug, (floorfleet.READ_MISSING, None))
        return fake

    PINNED = (floorfleet.READ_OK, "pin: atelier@abc1234")

    def test_both_listings_are_unioned_because_either_alone_under_enumerates(self):
        """The live failure: `users/{owner}/repos` returns PUBLIC repos only —
        4 of 20 on this estate. A tool whose claim is enumeration must never
        quietly enumerate a quarter of the estate."""
        public = [{"full_name": "o/pub", "archived": False}]
        private = [{"full_name": "o/priv", "archived": False}]

        def listings(path):
            return public if path.startswith("users/") else private

        with mock.patch.object(floorfleet, "_gh_list", side_effect=listings), \
             mock.patch.object(floorfleet, "_read_remote_slug_result",
                               return_value=self.PINNED):
            found = floorfleet.discover_github("o")
        self.assertEqual(sorted(s for s, _ in found.children),
                         ["o/priv", "o/pub"])
        self.assertEqual(found.outsiders, [])

    def test_repos_from_another_account_are_not_counted_as_this_estate(self):
        with mock.patch.object(floorfleet, "_gh_list",
                               return_value=[{"full_name": "someone/else"}]), \
             mock.patch.object(floorfleet, "_read_remote_slug_result",
                               return_value=self.PINNED):
            found = floorfleet.discover_github("o")
        self.assertEqual(found.children, [])
        self.assertEqual(found.outsiders, [])

    def test_a_repo_without_a_pin_is_an_outsider_not_a_child(self):
        """An outsider is a repo we READ and found no pin in — nothing weaker.
        This test used to assert `None ⇒ outsider`, which baked the FS1(b)
        conflation into the suite: it agreed that a refused read was a scope
        decision."""
        repos = [{"full_name": "o/child"}, {"full_name": "o/stranger"}]

        with mock.patch.object(floorfleet, "_gh_list", return_value=repos), \
             mock.patch.object(
                 floorfleet, "_read_remote_slug_result",
                 side_effect=self._reads({
                     "o/child": (floorfleet.READ_OK, "atelier@abc1234"),
                     "o/stranger": (floorfleet.READ_OK, "no pin here"),
                 })):
            found = floorfleet.discover_github("o")
        self.assertEqual([s for s, _ in found.children], ["o/child"])
        self.assertEqual(found.outsiders, ["o/stranger"])
        self.assertEqual(found.unreadable, [])

    def test_a_repo_with_no_claude_md_at_all_is_still_an_outsider(self):
        """404 IS an answer: the repo was readable and the file is not there.
        Separating unreadable from unpinned must not turn every unenrolled repo
        into an `unknown` row — that would be the same defect mirrored."""
        with mock.patch.object(floorfleet, "_gh_list",
                               return_value=[{"full_name": "o/stranger"}]), \
             mock.patch.object(
                 floorfleet, "_read_remote_slug_result",
                 return_value=(floorfleet.READ_MISSING, None)):
            found = floorfleet.discover_github("o")
        self.assertEqual(found.outsiders, ["o/stranger"])
        self.assertEqual(found.unreadable, [])

    def test_an_unreadable_claude_md_is_unknown_not_unenrolled(self):
        """FS1(b). A 403, a rate limit or a transient error is a read we could
        not make. Listing it as 'carries no atelier pin' is a confident wrong
        claim about a repo nobody could see — and it is this tool's own posture
        (`a read we could not make must never become a pass`) inverted."""
        repos = [{"full_name": "o/child"}, {"full_name": "o/refused"}]

        with mock.patch.object(floorfleet, "_gh_list", return_value=repos), \
             mock.patch.object(
                 floorfleet, "_read_remote_slug_result",
                 side_effect=self._reads({
                     "o/child": (floorfleet.READ_OK, "atelier@abc1234"),
                     "o/refused": (floorfleet.READ_FAILED, None),
                 })):
            found = floorfleet.discover_github("o")
        self.assertEqual([s for s, _ in found.children], ["o/child"])
        self.assertEqual(found.unreadable, ["o/refused"])
        self.assertNotIn("o/refused", found.outsiders)

    def test_an_unreadable_repo_is_a_red_row_not_a_silence(self):
        row = floorfleet.unreadable_row("o/refused", status=True)
        self.assertEqual(row.state, "unknown")
        self.assertFalse(row.ok)      # so --check exits 1 on it
        self.assertFalse(row.green)
        out = floorfleet.render([row], remote=True, status=True)
        self.assertIn("o/refused", out)
        self.assertIn("NOT running atelier's floor", out)

    def test_archived_repos_are_skipped_and_counted(self):
        """Skipping is deliberate; skipping SILENTLY is FS3. A
        decommissioned-but-still-pinned child otherwise leaves no line at all,
        on the board whose doctrine is that absences raise their hands."""
        with mock.patch.object(floorfleet, "_gh_list", return_value=[
                {"full_name": "o/old", "archived": True}]), \
             mock.patch.object(floorfleet, "_read_remote_slug_result",
                               return_value=self.PINNED):
            found = floorfleet.discover_github("o")
        self.assertEqual((found.children, found.outsiders), ([], []))
        self.assertEqual(found.archived, 1)

    def test_the_archived_skip_gets_a_footer_line(self):
        found = floorfleet.Discovery(archived=2, listings=[
            floorfleet.Listing("users/o/repos", "public repos only", 4, False),
            floorfleet.Listing("user/repos", "public + private", 20, True)])
        out = floorfleet.render([floorfleet.ChildFloor("a", "/a", "wired", "ok")],
                                remote=True, discovery=found)
        self.assertIn("2 archived repo(s) skipped", out)


class DiscoveryAuthorityTest(unittest.TestCase):
    """FS1(a): discovery declares WHICH listings answered and with how many.

    The run column has declared its authority since B3 (`repo-switch` vs
    `inferred`); discovery declared nothing, and the empty-estate guard fires
    only at ZERO children — so a token seeing some-but-not-all repos rendered a
    smaller, cleaner board with fewer reds and said nothing about it."""

    LISTINGS = [floorfleet.Listing("users/o/repos", "public repos only", 4,
                                   False),
                floorfleet.Listing("user/repos", "public + private", 20, True)]

    def _render(self, discovery):
        return floorfleet.render(
            [floorfleet.ChildFloor("a", "/a", "wired", "ok")],
            remote=True, discovery=discovery)

    def test_each_listing_is_named_with_its_count(self):
        out = self._render(floorfleet.Discovery(listings=self.LISTINGS))
        self.assertIn("Discovery authority", out)
        self.assertIn("users/o/repos", out)
        self.assertIn("4 repo(s)", out)
        self.assertIn("user/repos", out)
        self.assertIn("20 repo(s)", out)

    def test_an_empty_private_capable_listing_is_a_loud_warning(self):
        """The partial-sight case that used to render clean: the guard only
        fires at zero children, and four public repos are not zero."""
        blind = floorfleet.Discovery(listings=[
            floorfleet.Listing("users/o/repos", "public repos only", 4, False),
            floorfleet.Listing("user/repos", "public + private", 0, True)])
        self.assertTrue(blind.private_blind)
        out = self._render(blind)
        self.assertIn("PRIVATE-CAPABLE listing returned NOTHING", out)
        # And the remedy names the grant, not just the permissions (FS1).
        self.assertIn("ALL", out)
        self.assertIn("repositories owned by the account", out)

    def test_a_listing_that_answered_raises_no_caveat(self):
        out = self._render(floorfleet.Discovery(listings=self.LISTINGS))
        self.assertNotIn("returned NOTHING", out)

    def test_local_discovery_prints_no_github_authority_block(self):
        out = floorfleet.render(
            [floorfleet.ChildFloor("a", "/a", "wired", "ok")], remote=False)
        self.assertNotIn("Discovery authority", out)

    def test_unreadable_repos_are_declared_in_the_footer(self):
        out = self._render(floorfleet.Discovery(listings=self.LISTINGS,
                                                unreadable=["o/refused"]))
        self.assertIn("1 repo(s) unreadable", out)

    def test_the_counts_print_even_at_zero(self):
        """A known zero is a fact. A line that appears only when it is non-zero
        has to be noticed to be read, and two runs stop being comparable."""
        out = self._render(floorfleet.Discovery(listings=self.LISTINGS))
        self.assertIn("0 archived repo(s) skipped", out)
        self.assertIn("0 repo(s) unreadable", out)

    def test_from_github_end_to_end_puts_an_unreadable_repo_on_the_board(self):
        """The wiring, not just the pieces: a repo discovery could not read
        must reach the printed board as a row and must red `--check`. Before
        FS1 it reached the board as a line in the *unenrolled* list — a
        confident claim that it had chosen not to adopt the floor."""
        found = floorfleet.Discovery(
            children=[("o/child", "atelier@abc1234")],
            outsiders=["o/stranger"], unreadable=["o/refused"],
            listings=self.LISTINGS, archived=1)

        def content(child, rel):
            return THIN_CALLER if rel == floorfleet.FLOOR_PATH else None

        buf = io.StringIO()
        with mock.patch.object(floorfleet, "discover_github",
                               return_value=found), \
             mock.patch.object(floorfleet, "_read_remote", side_effect=content), \
             contextlib.redirect_stdout(buf):
            code = floorfleet.main(["--atelier", str(TOOLS_DIR.parent),
                                    "--from-github", "o", "--check"])
        out = buf.getvalue()
        self.assertIn("o/refused", out)
        self.assertIn("NOT running atelier's floor", out)
        self.assertIn("Discovery authority", out)
        self.assertIn("1 archived repo(s) skipped", out)
        # ...and it is NOT in the unenrolled list, which is the claim we cannot
        # make about a repo we could not read.
        unenrolled = out.split("carry no atelier pin")[-1]
        self.assertIn("o/stranger", unenrolled)
        self.assertNotIn("o/refused", unenrolled)
        self.assertEqual(code, 1)

    def test_the_grant_requirement_is_stated_where_a_consumer_reads_it(self):
        """The token spec leg of FS1: a consumer wiring a scheduled run must be
        told the grant scope, not only the permissions — a named-list grant
        cannot see repo 14, so a new child reads as nothing rather than red."""
        def flat(text):
            return " ".join(text.split())  # both are wrapped for reading

        self.assertIn("ALL repositories owned by the account",
                      flat(floorfleet.build_parser().format_help()))
        self.assertIn("ALL repositories owned by the account",
                      flat(floorfleet.__doc__))

    def test_a_stub_checkout_answers_the_slug_lookup(self):
        """Everything downstream asks a directory for its origin remote, so the
        stub has to satisfy exactly that and nothing more."""
        with tempfile.TemporaryDirectory() as td:
            d = floorfleet.stub_checkout(Path(td), "o/thing", "atelier@abc1234")
            self.assertEqual(floorfleet._slug(d), "o/thing")
            self.assertIn("atelier@abc1234",
                          (d / "CLAUDE.md").read_text(encoding="utf-8"))

    def test_the_local_hook_column_is_unavailable_not_absent(self):
        info = floorfleet.ChildFloor("a", "/a", "wired", "ok", hook="n/a")
        out = floorfleet.render([info], remote=True)
        self.assertIn("hook:n/a", out)
        # ...and must not be swept into the gap list, which would be a false red
        # on every row in this mode.
        self.assertNotIn("Local hook gaps", out)


class GhReadTest(unittest.TestCase):
    def test_a_scalar_jq_projection_is_not_parseable_as_json(self):
        """Regression. `_gh_json(path, '.sha')` printed a BARE sha — not valid
        JSON — so the parse failed, the caller read None as 'head unknown', and
        the `behind` check was inert on its first live run without ever
        erroring. The helper takes no --jq at all now; this pins why."""
        self.assertEqual(
            len(inspect.signature(floorfleet._gh_json).parameters), 1)
        with self.assertRaises(ValueError):
            json.loads("a8f667e26e29e765e0be276a2edefaeb5ac9047c")

    def test_a_failed_read_is_none_not_a_guess(self):
        fail = subprocess.CompletedProcess([], 1, stdout="", stderr="boom")
        with mock.patch.object(subprocess, "run", return_value=fail):
            self.assertIsNone(floorfleet._gh_json("repos/o/r"))
            self.assertEqual(floorfleet._gh_list("user/repos"), [])

    def _content(self, code, stdout="", stderr=""):
        done = subprocess.CompletedProcess([], code, stdout=stdout,
                                           stderr=stderr)
        with mock.patch.object(subprocess, "run", return_value=done):
            return floorfleet._read_remote_slug_result("o/r", "CLAUDE.md")

    def test_a_404_is_an_answer_and_says_the_file_is_missing(self):
        self.assertEqual(self._content(1, stderr="gh: Not Found (HTTP 404)"),
                         (floorfleet.READ_MISSING, None))

    def test_a_403_is_not_an_answer(self):
        """The FS1(b) split at its source. 403, rate limit, 5xx and a failure
        with no HTTP status at all (no gh, no network, not authenticated) are
        all reads we could not make — and this tool never lets one of those
        become a claim."""
        for stderr in ("gh: Resource not accessible (HTTP 403)",
                       "gh: API rate limit exceeded (HTTP 403)",
                       "gh: Server Error (HTTP 502)",
                       "dial tcp: lookup api.github.com: no such host"):
            self.assertEqual(self._content(1, stderr=stderr)[0],
                             floorfleet.READ_FAILED, stderr)

    def test_a_successful_read_is_decoded(self):
        payload = base64.b64encode(b"atelier@abc1234").decode()
        self.assertEqual(self._content(0, stdout=payload + "\n"),
                         (floorfleet.READ_OK, "atelier@abc1234"))

    def test_undecodable_content_is_a_failed_read_not_an_empty_one(self):
        self.assertEqual(self._content(0, stdout="!!!not base64!!!")[0],
                         floorfleet.READ_FAILED)

    def test_the_thin_wrapper_still_collapses_to_text_or_none(self):
        """The content reads keep the two-outcome shape on purpose: an absent
        floor.yml and an unreadable one both classify as not-wired."""
        with mock.patch.object(floorfleet, "_read_remote_slug_result",
                               return_value=(floorfleet.READ_FAILED, None)):
            self.assertIsNone(floorfleet._read_remote_slug("o/r", "x"))


if __name__ == "__main__":
    unittest.main()
