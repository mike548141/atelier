"""Stdlib-only tests for pins (no pytest needed): `python3 -m unittest`.

Pure-logic parts (pin parse, status classification) are unit-tested directly.
The git-touching parts build a throwaway atelier + child repos under a tmp dir
and drive evaluate()/discover() end-to-end, so the ancestry maths is proven
against real git — including the ahead/diverged/unknown cases the live two-child
fleet can't exhibit."""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import pins
import memprobe

TOOLS_DIR = Path(__file__).resolve().parent


def git(args, cwd):
    subprocess.run(["git", *args], cwd=str(cwd), check=True,
                   capture_output=True, text=True)


def sha(repo, ref="HEAD"):
    return subprocess.run(["git", "-C", str(repo), "rev-parse", ref],
                          capture_output=True, text=True, check=True).stdout.strip()


class PureLogic(unittest.TestCase):
    def test_classification_table(self):
        self.assertEqual(pins.classify(False, False, False, False), pins.STATUS_UNKNOWN)
        self.assertEqual(pins.classify(True, True, True, True), pins.STATUS_CURRENT)
        self.assertEqual(pins.classify(True, False, True, False), pins.STATUS_BEHIND)
        self.assertEqual(pins.classify(True, False, False, True), pins.STATUS_AHEAD)
        self.assertEqual(pins.classify(True, False, False, False), pins.STATUS_DIVERGED)

    def test_pin_parse_first_wins(self):
        tmp = Path(tempfile.mkdtemp(prefix="pins-md-"))
        md = tmp / "CLAUDE.md"
        md.write_text("intro\n(pinned `atelier@7f5abd0`)\n"
                      "later: git ... atelier@0000000..HEAD\n")  # leakscan:allow: atelier pin syntax, not an email
        self.assertEqual(pins.read_pin(md), "7f5abd0")

    def test_pin_parse_absent(self):
        tmp = Path(tempfile.mkdtemp(prefix="pins-md-"))
        md = tmp / "CLAUDE.md"
        md.write_text("this child has no pin at all\n")
        self.assertIsNone(pins.read_pin(md))

    def test_pin_parse_full_sha(self):
        tmp = Path(tempfile.mkdtemp(prefix="pins-md-"))
        md = tmp / "CLAUDE.md"
        md.write_text("pinned `atelier@" + "a" * 40 + "`\n")
        self.assertEqual(pins.read_pin(md), "a" * 40)

    def test_selftest_passes(self):
        self.assertEqual(pins._selftest(), 0)


class RealRepos(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="pins-test-")
        self.parent = Path(self.tmp) / "estate"
        self.parent.mkdir()
        # the atelier repo with three commits: c1 (old pin), c2 (mid), HEAD
        self.atelier = self.parent / "atelier"
        self.atelier.mkdir()
        self._init(self.atelier)
        self._commit(self.atelier, "one", "c1")
        self.c1 = sha(self.atelier)
        self._commit(self.atelier, "two", "c2")
        self.c2 = sha(self.atelier)
        self._commit(self.atelier, "three", "c3")
        self.head = sha(self.atelier)

    def tearDown(self):
        subprocess.run(["rm", "-rf", self.tmp])

    def _init(self, repo):
        git(["init", "-q", "-b", "main"], repo)
        git(["config", "user.email", "t@example.com"], repo)  # leakscan:allow: fictional test fixture
        git(["config", "user.name", "Test"], repo)

    def _commit(self, repo, fname, msg):
        (repo / fname).write_text(msg + "\n")
        git(["add", "-A"], repo)
        git(["commit", "-qm", msg], repo)

    def _child(self, name, pin_sha):
        d = self.parent / name
        d.mkdir()
        self._init(d)
        (d / "CLAUDE.md").write_text(f"# {name}\n(pinned `atelier@{pin_sha[:7]}`)\n")
        self._commit(d, "seed", "seed")
        return d

    def test_current(self):
        d = self._child("ros", self.head)
        info = pins.evaluate(self.atelier, self.head, d, want_log=False)
        self.assertEqual(info.status, pins.STATUS_CURRENT)
        self.assertEqual(info.behind, 0)

    def test_behind_counts_and_logs(self):
        d = self._child("faves", self.c1)
        info = pins.evaluate(self.atelier, self.head, d, want_log=True)
        self.assertEqual(info.status, pins.STATUS_BEHIND)
        self.assertEqual(info.behind, 2)
        self.assertEqual(len(info.log), 2)

    def test_unknown_pin(self):
        d = self._child("weird", "deadbeef")
        info = pins.evaluate(self.atelier, self.head, d, want_log=False)
        self.assertEqual(info.status, pins.STATUS_UNKNOWN)

    def test_no_pin(self):
        d = self.parent / "nopin"
        d.mkdir()
        self._init(d)
        (d / "CLAUDE.md").write_text("no doctrine block here\n")
        self._commit(d, "seed", "seed")
        info = pins.evaluate(self.atelier, self.head, d, want_log=False)
        self.assertEqual(info.status, pins.STATUS_NO_PIN)

    def test_ahead(self):
        # child pins a commit newer than the atelier HEAD we measure against
        ahead_sha = self.head
        older = self.c2
        d = self._child("future", ahead_sha)
        info = pins.evaluate(self.atelier, older, d, want_log=False)
        self.assertEqual(info.status, pins.STATUS_AHEAD)
        self.assertEqual(info.ahead, 1)

    def test_discover_finds_pinned_children_only(self):
        self._child("ros", self.head)
        self._child("faves", self.c1)
        # a sibling git repo with no pin must not be discovered
        plain = self.parent / "docker-heap"
        plain.mkdir()
        self._init(plain)
        (plain / "README.md").write_text("no claude md\n")
        self._commit(plain, "seed", "seed")
        found = {p.name for p in pins.discover([self.parent], self.atelier)}
        self.assertEqual(found, {"ros", "faves"})
        self.assertNotIn("atelier", found)  # parent excluded

    def test_report_exit_codes(self):
        # --atelier points at the throwaway repo (default would resolve to the
        # real atelier this script lives in, which doesn't know these SHAs).
        base = ["--atelier", str(self.atelier), "--root", str(self.parent)]
        self._child("ros", self.head)
        args = pins.build_parser().parse_args(base)
        self.assertEqual(pins.cmd_report(args), 0)  # only child is current
        self._child("faves", self.c1)
        args = pins.build_parser().parse_args(base + ["--check"])
        self.assertEqual(pins.cmd_report(args), 1)  # now one is behind


class WorktreeResolution(unittest.TestCase):
    """PU-5: `pins` run from a worktree resolved `resolve_atelier()` to the
    WORKTREE (a worktree is a real, distinct `--show-toplevel`), so `discover()`
    walked the worktree's parent directory instead of atelier's siblings and
    reported that wrong root's contents as the whole fleet, silently.

    A real `git worktree add` layout, not a mock: the failure mode is entirely
    about what `--show-toplevel` and `--git-common-dir` answer for a genuine
    linked worktree, which only real git can exercise honestly."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="pins-wt-test-")
        self.main = Path(self.tmp) / "atelier-main"
        self.main.mkdir()
        git(["init", "-q", "-b", "main"], self.main)
        git(["config", "user.email", "t@example.com"], self.main)  # leakscan:allow: fictional test fixture
        git(["config", "user.name", "Test"], self.main)
        # Ship the real pins.py inside the fixture repo, so the worktree
        # checked out from it carries a real, runnable copy at its OWN path —
        # exactly the shape that matters: __file__ resolves inside the
        # worktree, not the main checkout, when the script runs from there.
        tools_dir = self.main / "tools"
        tools_dir.mkdir()
        real_pins = Path(__file__).resolve().parent / "pins.py"
        shutil.copy(real_pins, tools_dir / "pins.py")
        self._commit(self.main, "seed.txt", "seed")
        self.worktree = Path(self.tmp) / "wt"
        subprocess.run(["git", "worktree", "add", "-q", str(self.worktree),
                       "-b", "test-wt"], cwd=str(self.main), check=True,
                      capture_output=True, text=True)
        self.empty_root = Path(self.tmp) / "empty-root"
        self.empty_root.mkdir()

    def tearDown(self):
        subprocess.run(["git", "worktree", "remove", "--force", str(self.worktree)],
                       cwd=str(self.main), check=False, capture_output=True, text=True)
        subprocess.run(["rm", "-rf", self.tmp])

    def _commit(self, repo, fname, msg):
        (repo / fname).write_text(msg + "\n")
        git(["add", "-A"], repo)
        git(["commit", "-qm", msg], repo)

    def test_main_checkout_from_worktree_is_the_main_repo(self):
        self.assertEqual(pins.main_checkout(self.worktree).resolve(),
                         self.main.resolve())
        # And from the main checkout itself, main_checkout is a no-op.
        self.assertEqual(pins.main_checkout(self.main).resolve(),
                         self.main.resolve())

    def test_resolve_atelier_from_worktree_finds_main_checkout_not_worktree(self):
        # Exercises the real on-disk script's OWN __file__ resolution, run with
        # cwd inside the worktree and no --atelier override — the exact call
        # shape PU-5 was filed against.
        script = self.worktree / "tools" / "pins.py"
        proc = subprocess.run(
            [sys.executable, str(script), "--root", str(self.empty_root), "--json"],
            cwd=str(self.worktree), capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(Path(payload["atelier"]).resolve(), self.main.resolve())
        self.assertNotEqual(Path(payload["atelier"]).resolve(),
                            self.worktree.resolve())

    def test_plain_output_names_the_search_root(self):
        # The visibility half of the fix: a reader must be able to see WHERE
        # discovery looked and how many it found, not just trust a denominator.
        script = self.worktree / "tools" / "pins.py"
        proc = subprocess.run(
            [sys.executable, str(script), "--root", str(self.empty_root)],
            cwd=str(self.worktree), capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn(str(self.empty_root), proc.stdout)
        self.assertIn("0 found", proc.stdout)


class ReadPinSizeCap(unittest.TestCase):
    """020/380 — `read_pin` refuses to read an oversized CLAUDE.md whole
    (`pins.MAX_CLAUDE_MD_BYTES`), reporting to stderr rather than silently
    misreading it as "no pin". Unit-level: proves the gate fires without the
    cost of a subprocess."""

    def test_oversized_claude_md_is_not_read(self):
        tmp = Path(tempfile.mkdtemp(prefix="pins-cap-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        md = tmp / "CLAUDE.md"
        md.write_text("pinned `atelier@" + "a" * 40 + "`\n"
                      + "x" * (pins.MAX_CLAUDE_MD_BYTES + 1024))
        self.assertIsNone(pins.read_pin(md))

    def test_under_cap_still_reads(self):
        tmp = Path(tempfile.mkdtemp(prefix="pins-cap-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        md = tmp / "CLAUDE.md"
        md.write_text("pinned `atelier@" + "a" * 40 + "`\n")
        self.assertEqual(pins.read_pin(md), "a" * 40)


class BoundedMemory(unittest.TestCase):
    """020/380 — extending 020/370's ruling to the fleet tools. `pins`
    (unlike a tree-walking guard) only walks ONE level of a search root and
    reads a single named file (CLAUDE.md) per candidate, so growth with
    SIBLING COUNT was never expected to be the failure mode here — proven
    below anyway, alongside the real one: a single oversized CLAUDE.md
    scaled peak memory with that ONE file's size (measured while building
    this fix: ~15 MB of extra peak RSS for an 8 MB CLAUDE.md over a 1 MB
    twin), now capped by `MAX_CLAUDE_MD_BYTES`.

    Every sibling here is SYNTHETIC, built under this test's own temp
    directory — never the real siblings beside this checkout (the hard
    safety rule this board item itself exists to enforce). Runs the real
    CLI as a SUBPROCESS via `memprobe.run_and_measure` and reads peak RSS
    back from the kernel — see `tools/memprobe.py`."""

    PINS = str(TOOLS_DIR / "pins.py")

    def _build_atelier(self) -> tuple[Path, str]:
        tmp = Path(tempfile.mkdtemp(prefix="pins-mem-atelier-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        git(["init", "-q", "-b", "main"], tmp)
        git(["config", "user.email", "t@example.com"], tmp)  # leakscan:allow: fictional test fixture
        git(["config", "user.name", "Test"], tmp)
        (tmp / "f").write_text("one\n")
        git(["add", "-A"], tmp)
        git(["commit", "-qm", "one"], tmp)
        return tmp, sha(tmp)

    def _build_siblings(self, root: Path, n: int, head: str,
                        big_claude_bytes: int = 0) -> None:
        root.mkdir(parents=True, exist_ok=True)
        for i in range(n):
            d = root / f"sibling{i}"
            (d / ".git").mkdir(parents=True)  # discover() only checks .exists()
            filler = "x" * big_claude_bytes if (big_claude_bytes and i == 0) else ""
            (d / "CLAUDE.md").write_text(
                f"# sibling{i}\n\npinned `atelier@{head}`\n" + filler + "\n")

    def _peak_rss_for(self, n: int, atelier: Path,
                      big_claude_bytes: int = 0) -> int:
        root = Path(tempfile.mkdtemp(prefix="pins-mem-siblings-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        self._build_siblings(root, n, sha(atelier), big_claude_bytes)
        result = memprobe.run_and_measure(
            [sys.executable, self.PINS, "--atelier", str(atelier),
             "--root", str(root)],
            timeout=60, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        return result.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_sibling_count(self):
        atelier, _ = self._build_atelier()
        small_peak = self._peak_rss_for(20, atelier)
        large_peak = self._peak_rss_for(200, atelier)
        growth = large_peak - small_peak
        # 180 extra tiny directory entries and CLAUDE.md reads cost a few KB
        # each at most — generous headroom over that, tight enough to still
        # catch a real per-sibling leak.
        self.assertLess(
            growth, 20 * 1024 * 1024,
            f"peak RSS grew {growth / 1e6:.1f} MB for 180 more sibling "
            f"directories (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB).")

    def test_peak_memory_does_not_scale_with_one_huge_claude_md(self):
        atelier, _ = self._build_atelier()
        small_peak = self._peak_rss_for(5, atelier, big_claude_bytes=1 * 1024 * 1024)
        large_peak = self._peak_rss_for(
            5, atelier, big_claude_bytes=pins.MAX_CLAUDE_MD_BYTES + (1024 * 1024))
        growth = large_peak - small_peak
        # The "large" fixture is now OVER the cap, so it must be refused —
        # this pins the fix, not just a smaller multiplier. Bound is
        # generous (a few MB of interpreter/allocator noise), never the
        # multi-MB-per-extra-MB growth the old whole-file read showed.
        self.assertLess(
            growth, 10 * 1024 * 1024,
            f"peak RSS grew {growth / 1e6:.1f} MB when the larger CLAUDE.md "
            f"crossed MAX_CLAUDE_MD_BYTES (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB) — it should have been refused, "
            "not read whole.")


if __name__ == "__main__":
    unittest.main()
