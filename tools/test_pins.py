"""Stdlib-only tests for pins (no pytest needed): `python3 -m unittest`.

Pure-logic parts (pin parse, status classification) are unit-tested directly.
The git-touching parts build a throwaway atelier + child repos under a tmp dir
and drive evaluate()/discover() end-to-end, so the ancestry maths is proven
against real git — including the ahead/diverged/unknown cases the live two-child
fleet can't exhibit."""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

import pins


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


if __name__ == "__main__":
    unittest.main()
