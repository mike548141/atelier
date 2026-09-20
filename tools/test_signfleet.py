"""Stdlib-only tests for signfleet (no pytest): `python3 -m unittest`.

The load-bearing test here is `Detects.test_unsigned_child_fails`. A fleet probe
that has only ever printed "pass" is not proven — it could be passing because it
looks at nothing. So the suite builds a throwaway atelier + child where the
commits are genuinely unsigned, and asserts the probe goes RED. Everything else
guards the paths that decide whether a child is even looked at, because a silent
`skip` is the failure mode that would make this tool lie by omission.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import signfleet as sf
import memprobe

TOOLS_DIR = Path(__file__).resolve().parent


def _run(cwd, *args, env=None):
    e = dict(os.environ)
    e.update({
        "GIT_AUTHOR_NAME": "T", "GIT_AUTHOR_EMAIL": "t@example.test",  # leakscan:allow: RFC 2606 reserved test domain, throwaway repo fixture
        "GIT_COMMITTER_NAME": "T", "GIT_COMMITTER_EMAIL": "t@example.test",  # leakscan:allow: RFC 2606 reserved test domain, throwaway repo fixture
    })
    if env:
        e.update(env)
    return subprocess.run(["git", *args], cwd=cwd, env=e,
                          capture_output=True, text=True, check=True)


# A syntactically valid allowed_signers naming a key that signs nothing here, so
# every real commit in these tests fails verification. That is the point: it
# proves the probe reports failure rather than skipping. Public key material only.
TRUST = ("signfleet-selftest@atelier ssh-ed25519 "  # leakscan:allow: fictional test principal
         "AAAAC3NzaC1lZDI1NTE5AAAAIH83ur6OGBroCHBjw+NivPdhPWyVp5SVKOhTbZkGnruT\n")  # secretscan:allow: throwaway public key, not a credential

FLOOR = 'env:\n  SIGN_BOUNDARY: "{boundary}"\n\njobs:\n  floor:\n    runs-on: ubuntu-latest\n'


class TempRepo:
    def __init__(self):
        self.dir = tempfile.mkdtemp()
        _run(self.dir, "init", "-q", "-b", "main")
        _run(self.dir, "config", "commit.gpgsign", "false")

    def commit(self, msg):
        fn = os.path.join(self.dir, "f")
        with open(fn, "a") as f:
            f.write(msg + "\n")
        _run(self.dir, "add", "f")
        _run(self.dir, "commit", "-q", "-m", msg)
        return _run(self.dir, "rev-parse", "HEAD").stdout.strip()

    def write(self, rel, text):
        p = Path(self.dir) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p


def make_atelier(with_trust=True):
    """A throwaway atelier whose HEAD carries allowed_signers, so a child pinned
    at that SHA resolves a trust list the way the real fleet does."""
    a = TempRepo()
    if with_trust:
        a.write("allowed_signers", TRUST)
        _run(a.dir, "add", "allowed_signers")
    else:
        a.write("README.md", "no trust list yet\n")
        _run(a.dir, "add", "README.md")
    _run(a.dir, "commit", "-q", "-m", "seed")
    return a, _run(a.dir, "rev-parse", "HEAD").stdout.strip()


def make_child(pin, boundary="", extra_commits=2):
    c = TempRepo()
    c.write("CLAUDE.md", f"# child\n\nDoctrine pinned `atelier@{pin}`\n")
    c.write(".github/workflows/floor.yml", FLOOR.format(boundary=boundary))
    _run(c.dir, "add", ".")
    c.commit("base")
    for i in range(extra_commits):
        c.commit(f"work {i}")
    return c


class Selftest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(sf.main(["--selftest"]), 0)


class BoundaryParse(unittest.TestCase):
    def _b(self, text):
        with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as f:
            f.write(text)
            p = Path(f.name)
        try:
            return sf.read_boundary(p)
        finally:
            p.unlink(missing_ok=True)

    def test_quoted(self):
        self.assertEqual(self._b('  SIGN_BOUNDARY: "26a8bb6"\n'), "26a8bb6")

    def test_trailing_comment(self):
        self.assertEqual(self._b('  SIGN_BOUNDARY: "f53d645"  # last unsigned\n'), "f53d645")

    def test_unquoted(self):
        self.assertEqual(self._b("  SIGN_BOUNDARY: abc1234\n"), "abc1234")

    def test_empty_is_all_history_not_absent(self):
        # "" and None mean different things; conflating them would silently switch
        # a born-signed repo from "verify everything" to "skip".
        self.assertEqual(self._b('  SIGN_BOUNDARY: ""\n'), "")
        self.assertIsNone(self._b("env:\n  OTHER: 1\n"))

    def test_missing_file(self):
        self.assertIsNone(sf.read_boundary(Path("/nonexistent/floor.yml")))


class Classify(unittest.TestCase):
    def test_table(self):
        self.assertEqual(sf.classify(0, 5), sf.STATUS_PASS)
        self.assertEqual(sf.classify(1, 5), sf.STATUS_FAIL)
        self.assertEqual(sf.classify(3, 3), sf.STATUS_FAIL)

    def test_empty_range_passes(self):
        # Nothing after the boundary is an honest pass, not a skip.
        self.assertEqual(sf.classify(0, 0), sf.STATUS_PASS)

    def test_only_fail_is_actionable(self):
        self.assertIn(sf.STATUS_FAIL, sf.ACTIONABLE)
        self.assertNotIn(sf.STATUS_SKIP, sf.ACTIONABLE)
        self.assertNotIn(sf.STATUS_ERROR, sf.ACTIONABLE)


class Detects(unittest.TestCase):
    """The suite's reason to exist: prove the probe can go red."""

    def test_unsigned_child_fails(self):
        atelier, head = make_atelier()
        child = make_child(head, boundary="")
        with tempfile.TemporaryDirectory() as td:
            info = sf.evaluate(Path(atelier.dir), Path(child.dir), Path(td))
        self.assertEqual(info.status, sf.STATUS_FAIL,
                         f"expected FAIL on unsigned commits, got {info.status}: {info.reason}")
        self.assertGreater(info.bad, 0)
        self.assertTrue(info.bad_shas, "a failing child must name the offending commits")

    def test_boundary_excludes_earlier_commits(self):
        # Moving the boundary past the bad commits is the real-world fix; the probe
        # must reflect it, or the fix could never be verified.
        atelier, head = make_atelier()
        child = make_child(head, boundary="", extra_commits=2)
        tip = _run(child.dir, "rev-parse", "HEAD").stdout.strip()
        child.write(".github/workflows/floor.yml", FLOOR.format(boundary=tip))
        _run(child.dir, "add", ".")
        with tempfile.TemporaryDirectory() as td:
            info = sf.evaluate(Path(atelier.dir), Path(child.dir), Path(td))
        # Nothing after the boundary yet -> nothing to fail on.
        self.assertEqual(info.commits, 0)
        self.assertEqual(info.status, sf.STATUS_PASS)


class Skips(unittest.TestCase):
    """Each skip reason must be reported, never silently treated as a pass."""

    def test_no_pin(self):
        atelier, head = make_atelier()
        c = TempRepo()
        c.write("CLAUDE.md", "# child with no pin\n")
        _run(c.dir, "add", ".")
        c.commit("base")
        with tempfile.TemporaryDirectory() as td:
            info = sf.evaluate(Path(atelier.dir), Path(c.dir), Path(td))
        self.assertEqual(info.status, sf.STATUS_SKIP)
        self.assertIn("pin", info.reason)

    def test_no_floor_yml(self):
        atelier, head = make_atelier()
        c = TempRepo()
        c.write("CLAUDE.md", f"pinned `atelier@{head}`\n")
        _run(c.dir, "add", ".")
        c.commit("base")
        with tempfile.TemporaryDirectory() as td:
            info = sf.evaluate(Path(atelier.dir), Path(c.dir), Path(td))
        self.assertEqual(info.status, sf.STATUS_SKIP)
        self.assertIn("floor.yml", info.reason)

    def test_pin_predates_allowed_signers(self):
        # Mirrors the child's own CI, which warns and passes rather than redding.
        atelier, head = make_atelier(with_trust=False)
        child = make_child(head)
        with tempfile.TemporaryDirectory() as td:
            info = sf.evaluate(Path(atelier.dir), Path(child.dir), Path(td))
        self.assertEqual(info.status, sf.STATUS_SKIP)
        self.assertIn("predates", info.reason)


class Render(unittest.TestCase):
    def test_reports_failure_and_deferred_honestly(self):
        infos = [
            sf.ChildSign("good", "/p/good", pin="a" * 7, boundary="", status=sf.STATUS_PASS,
                         commits=3, good=3),
            sf.ChildSign("bad", "/p/bad", pin="b" * 7, boundary="", status=sf.STATUS_FAIL,
                         commits=2, good=1, bad=1, bad_shas=["deadbeef01"]),
            sf.ChildSign("srv", "/p/srv", pin="c" * 7, boundary="", status=sf.STATUS_PASS,
                         commits=1, good=0, deferred=1),
        ]
        out = sf.render(infos, Path("/atelier"))
        self.assertIn("would FAIL", out)
        self.assertIn("deadbeef01", out)
        # A deferred commit is NOT verified here and the output must say so.
        self.assertIn("deferred to the gh plane", out)

    def test_skips_are_not_counted_as_green(self):
        infos = [sf.ChildSign("s", "/p/s", status=sf.STATUS_SKIP, reason="no atelier pin")]
        out = sf.render(infos, Path("/atelier"))
        self.assertIn("not a green result", out)

    def test_empty_fleet_is_not_a_pass(self):
        out = sf.render([], Path("/atelier"))
        self.assertIn("no atelier children", out)


class SizeCapTest(unittest.TestCase):
    """020/380 — unit-level: `read_boundary` refuses an oversized floor.yml
    without the cost of a subprocess."""

    def test_read_boundary_refuses_oversized_file(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "floor.yml"
            p.write_text("env:\n  SIGN_BOUNDARY: \"\"\n"
                         + "x" * (sf.MAX_FLOOR_YML_BYTES + 1024))
            self.assertIsNone(sf.read_boundary(p))

    def test_read_boundary_still_reads_under_cap(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "floor.yml"
            p.write_text('  SIGN_BOUNDARY: "abc1234"\n')
            self.assertEqual("abc1234", sf.read_boundary(p))


class BoundedMemory(unittest.TestCase):
    """020/380 — extending 020/370's ruling to the fleet tools. signfleet's
    discovery is the same one-level `pins.discover()` floorfleet uses, and
    per-child it read a `floor.yml` WHOLE (`read_boundary`) — a single
    oversized one scaled peak memory with that one file's size (measured
    while building this fix: ~14 MB of extra peak RSS for a 7 MB larger
    floor.yml), now capped by `MAX_FLOOR_YML_BYTES`.

    Every sibling here is SYNTHETIC, built under this test's own temp
    directory and passed via `--root` — never the real siblings beside this
    checkout. `--atelier` points at THIS worktree, a real git repo (needed
    so `git show <pin>:allowed_signers` has something to resolve against,
    even though every synthetic pin here is bogus and the child is expected
    to end up `skip`/`error` — `read_boundary` already ran by then, which is
    the half this test measures). Runs the CLI as a SUBPROCESS via
    `memprobe.run_and_measure` and reads peak RSS back from the kernel —
    see `tools/memprobe.py`."""

    SIGNFLEET = str(TOOLS_DIR / "signfleet.py")
    ATELIER = str(TOOLS_DIR.parent)

    def _build_siblings(self, root: Path, n: int,
                        big_yml_bytes: int = 0) -> None:
        root.mkdir(parents=True, exist_ok=True)
        for i in range(n):
            d = root / f"sibling{i}"
            (d / ".git").mkdir(parents=True)
            (d / ".github" / "workflows").mkdir(parents=True)
            (d / "CLAUDE.md").write_text(
                f"# sibling{i}\n\npinned `atelier@" + "a" * 40 + "`\n")
            yml_filler = (("# " + "y" * big_yml_bytes + "\n")
                         if (big_yml_bytes and i == 0) else "")
            (d / ".github" / "workflows" / "floor.yml").write_text(
                "env:\n  SIGN_BOUNDARY: \"\"\n" + yml_filler)

    def _peak_rss_for(self, n: int, big_yml_bytes: int = 0) -> int:
        root = Path(tempfile.mkdtemp(prefix="signfleet-mem-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        self._build_siblings(root, n, big_yml_bytes)
        result = memprobe.run_and_measure(
            [sys.executable, self.SIGNFLEET, "--atelier", self.ATELIER,
             "--root", str(root)],
            timeout=120, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        return result.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_sibling_count(self):
        small_peak = self._peak_rss_for(10)
        large_peak = self._peak_rss_for(100)
        growth = large_peak - small_peak
        self.assertLess(
            growth, 30 * 1024 * 1024,
            f"peak RSS grew {growth / 1e6:.1f} MB for 90 more sibling "
            f"directories (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB).")

    def test_peak_memory_does_not_scale_with_one_huge_floor_yml(self):
        small_peak = self._peak_rss_for(5, big_yml_bytes=1 * 1024 * 1024)
        large_peak = self._peak_rss_for(
            5, big_yml_bytes=sf.MAX_FLOOR_YML_BYTES + (1024 * 1024))
        growth = large_peak - small_peak
        self.assertLess(
            growth, 15 * 1024 * 1024,
            f"peak RSS grew {growth / 1e6:.1f} MB when the larger floor.yml "
            f"crossed MAX_FLOOR_YML_BYTES (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB) — it should have been refused, "
            "not read whole.")


if __name__ == "__main__":
    unittest.main()
