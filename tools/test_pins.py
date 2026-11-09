"""Stdlib-only tests for pins (no pytest needed): `python3 -m unittest`.

Pure-logic parts (pin parse, status classification) are unit-tested directly.
The git-touching parts build a throwaway atelier + child repos under a tmp dir
and drive evaluate()/discover() end-to-end, so the ancestry maths is proven
against real git — including the ahead/diverged/unknown cases the live two-child
fleet can't exhibit."""

import json
import os
import re
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
        base = ["--atelier", str(self.atelier), "--root", str(self.parent), "--head"]
        self._child("ros", self.head)
        args = pins.build_parser().parse_args(base)
        self.assertEqual(pins.cmd_report(args), 0)  # only child is current
        self._child("faves", self.c1)
        args = pins.build_parser().parse_args(base + ["--check"])
        self.assertEqual(pins.cmd_report(args), 1)  # now one is behind


class PublishedMainlineReference(unittest.TestCase):
    """160/310 HF3 — the fleet view is measured against the published
    mainline after a fetch, not the local checkout's HEAD. A stale local
    checkout made a pin at the true tip read "ahead" or "unknown" (`320/260`),
    and a failed fetch must be *no result*, never an empty "all current"."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="pins-ref-"))
        self.parent = self.tmp / "estate"
        self.parent.mkdir()
        self.origin = self.tmp / "origin.git"
        git(["init", "-q", "--bare", "-b", "main", str(self.origin)], self.tmp)
        # the publisher advances origin; atelier is a clone left one behind
        self.pub = self.tmp / "pub"
        git(["clone", "-q", str(self.origin), str(self.pub)], self.tmp)
        git(["config", "user.email", "t@example.com"], self.pub)  # leakscan:allow: fictional test fixture
        git(["config", "user.name", "Test"], self.pub)
        self._commit(self.pub, "one")
        git(["push", "-q", "origin", "main"], self.pub)
        self.atelier = self.parent / "atelier"
        git(["clone", "-q", str(self.origin), str(self.atelier)], self.tmp)
        self.old = sha(self.atelier)
        self._commit(self.pub, "two")
        git(["push", "-q", "origin", "main"], self.pub)
        self.tip = sha(self.pub)
        child = self.parent / "ros"
        child.mkdir()
        git(["init", "-q", "-b", "main"], child)
        (child / "CLAUDE.md").write_text(f"(pinned `atelier@{self.tip[:7]}`)\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _commit(self, repo, name):
        (repo / name).write_text(name + "\n")
        git(["add", "--", name], repo)
        git(["-c", "user.email=t@example.com", "-c", "user.name=Test",  # leakscan:allow: fictional test fixture
             "commit", "-qm", name], repo)

    def _run(self, *extra):
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "pins.py"), "--atelier", str(self.atelier),
             "--root", str(self.parent), "--json", *extra],
            capture_output=True, text=True)

    def test_default_fetches_and_measures_against_origin_main(self):
        # A stale local HEAD would call the child (pinned at the true tip)
        # unknown; the fetched mainline calls it current.
        proc = self._run()
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["ref"], "origin/main")
        self.assertEqual(payload["head"], self.tip)
        self.assertEqual(payload["children"][0]["status"], pins.STATUS_CURRENT)

    def test_head_is_the_explicit_offline_choice(self):
        proc = self._run("--head")
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["ref"], "HEAD")
        self.assertEqual(payload["head"], self.old)
        self.assertEqual(payload["children"][0]["status"], pins.STATUS_UNKNOWN)

    def test_failed_fetch_is_no_result_not_no_drift(self):
        shutil.move(str(self.origin), str(self.origin) + ".gone")
        proc = self._run()
        self.assertEqual(proc.returncode, 2, proc.stdout)
        self.assertIn("no result, not no drift", proc.stderr)
        self.assertIn("--head", proc.stderr)
        self.assertEqual(proc.stdout.strip(), "")

    def test_remote_not_named_origin_is_refused_with_the_assumption_stated(self):
        git(["remote", "rename", "origin", "upstream"], self.atelier)
        proc = self._run()
        self.assertEqual(proc.returncode, 2, proc.stdout)
        self.assertIn("origin", proc.stderr)


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
        # pins reads a child's floor copy with stampscan's own comparison, so
        # stampscan and the three modules it imports travel with it.
        for name in ("pins.py", "stampscan.py", "filewalk.py", "allowmarker.py", "report.py"):
            shutil.copy(Path(__file__).resolve().parent / name, tools_dir / name)
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
            [sys.executable, str(script), "--root", str(self.empty_root), "--head",
             "--json"],
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
            [sys.executable, str(script), "--root", str(self.empty_root), "--head"],
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

    # A hang guard, NOT a performance bound (160/950 QU3). This class pins
    # MEMORY; a wall-clock limit tight enough to matter on an idle machine
    # (60 s) tripped under a loaded one (load 14-53 stretched the full suite
    # from about 440 s to about 1200 s) and the red read as a memory defect.
    # Ten minutes is far above any observed load-inflated run and still stops
    # a scan that has really hung.
    HANG_GUARD_SECONDS = 600

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
            timeout=self.HANG_GUARD_SECONDS,
            rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(
            result.timed_out,
            f"scan did not finish in {self.HANG_GUARD_SECONDS} s. This is a "
            "hang guard: under heavy machine load a slow scan is NOT the "
            "memory defect this class pins; re-run on a quieter machine "
            "before reading it as one.")
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

# ---------------------------------------------------------------------------
# 160/340 — the floor-copy report.
#
# SYNTHETIC repos only, built under a temp dir: nothing here reads a real child
# or the real atelier checkout. The comparison is stampscan's (find_stamp_blocks,
# extract_region, evaluate_block); these tests pin the parts pins adds: the
# reference being the floor at the child's OWN pin, the four placeholders put
# back, the dated cut-off, and the states a copy that cannot be compared gets.

import datetime  # noqa: E402
from unittest import mock  # noqa: E402

FLOOR_V1 = [
    "## Doctrine — inherited from atelier (pinned `atelier@<SHA>`)",
    "",
    "- **Rule one:** keep the safety rule verbatim.",
    "- **Source & drift:** canonical doctrine is `<atelier-path>/docs/method/`.",
    "  Run `git -C \"<atelier-path>\" log --oneline <SHA>..origin/main`.",
    "- **This repo's visibility:** <visibility fact>. Verify:",
    "  `gh repo view <owner/repo> --json visibility`.",
]
FLOOR_V2 = FLOOR_V1[:2] + ["- **Rule one:** keep the safety rule verbatim, always."] + FLOOR_V1[3:]


def propagation(region):
    return ("# PROPAGATION\n\nprose\n\n<!-- floor:begin -->\n```markdown\n"
            + "\n".join(region) + "\n```\n<!-- floor:end -->\n\ntail\n")


def filled(region, sha, visibility="PRIVATE by design. It holds only examples,\n  so it is never published"):
    text = "\n".join(region)
    for token, value in (("<SHA>", sha[:7]), ("<atelier-path>", "../atelier"),
                         ("<visibility fact>", visibility), ("<owner/repo>", "example/child")):
        text = text.replace(token, value)
    return text


def stamped(block_text, begin="<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor -->"):
    return f"# child\n\n{begin}\n{block_text}\n<!-- stamp:end -->\n\nmore\n"


class FloorCopyReport(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="pins-copy-"))
        self.parent = self.tmp / "estate"
        self.parent.mkdir()
        self.atelier = self.parent / "atelier"
        self.atelier.mkdir()
        git(["init", "-q", "-b", "main"], self.atelier)
        git(["config", "user.email", "t@example.com"], self.atelier)  # leakscan:allow: fictional test fixture
        git(["config", "user.name", "Test"], self.atelier)
        (self.atelier / "docs" / "method").mkdir(parents=True)
        self.prop = self.atelier / "docs" / "method" / "PROPAGATION.md"
        self.v0 = self._commit_text("no region yet\n")          # a pin before the region was marked
        self.v1 = self._commit_text(propagation(FLOOR_V1))
        self.v2 = self._commit_text(propagation(FLOOR_V2))      # the floor moved after v1
        self.head = self.v2

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _commit_text(self, text):
        self.prop.write_text(text)
        git(["add", "-A"], self.atelier)
        git(["commit", "-qm", "c"], self.atelier)
        return sha(self.atelier)

    def _child(self, name, pin, claude_md):
        d = self.parent / name
        d.mkdir()
        git(["init", "-q", "-b", "main"], d)
        (d / "CLAUDE.md").write_text(claude_md)
        return d

    def _eval(self, d):
        return pins.evaluate(self.atelier, self.head, d, want_log=False)

    def _run(self, *extra, today=None):
        args = pins.build_parser().parse_args(
            ["--atelier", str(self.atelier), "--root", str(self.parent), "--head", *extra])
        with mock.patch.object(pins, "_utc_today", return_value=today or datetime.date(2026, 11, 9)):
            return pins.cmd_report(args)

    def test_a_verbatim_copy_with_its_placeholders_filled_reads_identical(self):
        d = self._child("a", self.v2, stamped(filled(FLOOR_V2, self.v2)))
        info = self._eval(d)
        self.assertEqual(info.copy, pins.COPY_IDENTICAL, info.copy_detail)
        self.assertFalse(info.floor_moved)

    def test_a_child_at_an_older_pin_is_compared_with_the_floor_at_its_own_pin(self):
        # Verbatim to what it pinned (v1), though the floor has since moved to v2.
        d = self._child("old", self.v1, stamped(filled(FLOOR_V1, self.v1)))
        info = self._eval(d)
        self.assertEqual(info.copy, pins.COPY_IDENTICAL, info.copy_detail)
        self.assertTrue(info.floor_moved, "and the report says the floor has moved since")
        self.assertEqual(info.status, pins.STATUS_BEHIND, "staleness is the pin column's job")
        # The same copy judged against TODAY's text would differ: the wrong reference.
        today = stampscan_check(filled(FLOOR_V1, self.v1), FLOOR_V2)
        self.assertEqual(today, pins.COPY_DRIFT)

    def test_a_copy_that_differs_from_its_own_pin_is_drift(self):
        reworded = filled(FLOOR_V1, self.v1).replace("keep the safety rule verbatim", "keep the safety rule")
        info = self._eval(self._child("edited", self.v1, stamped(reworded)))
        self.assertEqual(info.copy, pins.COPY_DRIFT)
        self.assertIn("keep the safety rule", info.copy_detail)

    def test_a_dropped_line_and_a_narrow_declaration_are_still_drift(self):
        dropped = "\n".join(filled(FLOOR_V1, self.v1).split("\n")[:3])
        begin = "<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor narrow=we-left-it-out -->"
        info = self._eval(self._child("short", self.v1, stamped(dropped, begin)))
        self.assertEqual(info.copy, pins.COPY_DRIFT, "the floor is verbatim; narrow= buys nothing")

    def test_an_unfilled_placeholder_is_drift_and_names_the_line(self):
        raw = f"(pinned `atelier@{self.v1[:7]}`)\n" + stamped("\n".join(FLOOR_V1))
        info = self._eval(self._child("raw", self.v1, raw))
        self.assertEqual(info.copy, pins.COPY_DRIFT)

    def test_states_that_cannot_be_compared_are_reported_not_failed(self):
        unstamped = self._eval(self._child("plain", self.v1, f"(pinned `atelier@{self.v1[:7]}`)\n"))
        self.assertEqual(unstamped.copy, pins.COPY_UNSTAMPED)
        old = self._eval(self._child("ancient", self.v0, f"(pinned `atelier@{self.v0[:7]}`)\n"))
        self.assertEqual(old.copy, pins.COPY_NO_REFERENCE, "the pin predates the region markers")
        unknown = self._eval(self._child("lost", "deadbeef", "(pinned `atelier@deadbeef`)\n"))
        self.assertEqual(unknown.copy, pins.COPY_NO_REFERENCE)
        allowed = stamped(filled(FLOOR_V1, self.v1) + "\n<!-- stampscan:allow: reason -->")
        # 160/340 FV2: a marker inside a floor stamp no longer switches the
        # comparison off, so the added line is a difference like any other.
        self.assertEqual(self._eval(self._child("allowed", self.v1, allowed)).copy, pins.COPY_DRIFT)
        broken = f"(pinned `atelier@{self.v1[:7]}`)\n<!-- stamp:begin source=x region=floor -->\nno end\n"
        self.assertEqual(self._eval(self._child("broken", self.v1, broken)).copy, pins.COPY_MALFORMED)
        for info in (unstamped, old, unknown):
            self.assertFalse(pins.copy_blocks(info, datetime.date(2027, 1, 1)), "only drift ever blocks")

    def test_report_only_before_the_date_blocking_from_it(self):
        reworded = filled(FLOOR_V2, self.v2).replace("always", "sometimes")
        self._child("edited", self.v2, stamped(reworded))
        self._child("good", self.v2, stamped(filled(FLOOR_V2, self.v2)))
        self.assertEqual(pins.COPY_BLOCKS_FROM, datetime.date(2026, 12, 9))
        before = self._run("--check", today=datetime.date(2026, 12, 8))
        # `edited` is current, so before the cut-off nothing at all is red.
        self.assertEqual(before, 0, "report-only: a differing copy does not move the exit code")
        after = self._run("--check", today=datetime.date(2026, 12, 9))
        self.assertEqual(after, 1, "from the date the same comparison fails the check")
        self.assertFalse(pins.copy_blocking(datetime.date(2026, 12, 8)))
        self.assertTrue(pins.copy_blocking(datetime.date(2026, 12, 9)))

    def test_the_date_and_the_differing_repos_are_printed_and_in_the_json(self):
        self._child("edited", self.v2, stamped(filled(FLOOR_V2, self.v2).replace("always", "sometimes")))
        out = self.tmp / "out.txt"
        with mock.patch.object(pins, "_utc_today", return_value=datetime.date(2026, 11, 9)), \
                open(out, "w") as fh, mock.patch.object(sys, "stdout", fh):
            pins.cmd_report(pins.build_parser().parse_args(
                ["--atelier", str(self.atelier), "--root", str(self.parent), "--head"]))
            pins.cmd_report(pins.build_parser().parse_args(
                ["--atelier", str(self.atelier), "--root", str(self.parent), "--head", "--json"]))
        text = out.read_text()
        self.assertIn("report-only until 2026-12-09", text)
        self.assertIn("1 of 1 copies differ", text)
        payload = json.loads(text[text.index("{"):])
        self.assertEqual(payload["floor_copy"], {"blocks_from": "2026-12-09", "blocking": False,
                                                 "differing": ["edited"]})
        self.assertEqual(payload["children"][0]["copy"], "drift")

    def test_the_four_placeholders_are_the_only_angle_tokens_in_the_real_floor_region(self):
        # If the floor gains a fifth placeholder, filling it would silently stop
        # working; this fails first. Reads atelier's own PROPAGATION.md (the one
        # this script lives in), never a child.
        import stampscan
        text = (TOOLS_DIR.parent / "docs" / "method" / "PROPAGATION.md").read_text()
        region = stampscan.extract_region(text, "floor")
        tokens = set(re.findall(r"<[A-Za-z][^<>]*>", "\n".join(region)))
        self.assertEqual(tokens, set(pins.COPY_PLACEHOLDERS))


def stampscan_check(child_text, canonical_region):
    """What the comparison says of `child_text` against an arbitrary region: the
    wrong-reference control for the older-pin test."""
    state, _ = pins.check_copy("x/CLAUDE.md", stamped(child_text), canonical_region)
    return state
