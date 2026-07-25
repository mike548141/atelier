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

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import floorfleet  # noqa: E402

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
        self.assertEqual(info.advisory, ["wrapscan"])
        self.assertEqual(info.disabled, {"spellscan": "no prose in this repo"})

    def test_unreadable_config_is_surfaced_not_swallowed(self):
        with tempfile.TemporaryDirectory() as td:
            repo = self._repo(td, THIN_CALLER)
            (repo / floorfleet.CONFIG_PATH).write_text("{ broken")
            info = floorfleet.evaluate(repo, remote=False)
        self.assertIn("unreadable", info.detail)

    def test_missing_floor_reports_absent(self):
        with tempfile.TemporaryDirectory() as td:
            info = floorfleet.evaluate(self._repo(td, None), remote=False)
        self.assertEqual(info.state, "absent")


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


if __name__ == "__main__":
    unittest.main()
