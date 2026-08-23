"""One test for the mixed-root defect, parametrised over every scanner that
takes both `--root` and a path list.

THE DEFECT. A relative path argument became `Path(p)`, which resolves against
the process's **cwd**. `--root` was used for everything else the run depends
on — the `.<tool>ignore` lookup, the repo-relative anchors, the `docs/`
default. So a run given `--root X docs/thing.md` from inside repo Y read **Y's
file under X's rules**, reported confidently, and nothing in the output said
which tree either half came from. Every child repo carries `docs/ROADMAP.md`,
`docs/method/`, `docs/SESSIONS.md` under the same names by design, so the path
collision the silent case needs is guaranteed rather than unlucky.

WHY ONE TEST AND NOT ELEVEN. The fix is one line copied into eleven tools
(`pointerscan` already had it right), and eleven hand-written tests are eleven
things to forget when a twelfth tool joins. Parametrised over the mains, this
is also the regression guard for the shared scanner harness if `115/080` ever
lands.

WHY THE FIXTURE IS AN *ABSENT* FILE. It needs no per-tool knowledge of what
each scanner considers a finding, and it fails loudly in the one direction that
matters: every one of these tools exits 2 on a target that does not exist, so
a correctly-rooted run **cannot** exit 0 here. A tool still reading cwd finds
the file, scans it, and exits 0 or 1 — never 2. A green run is impossible while
any tool reads the caller's cwd, which is the property the item asked for.

The second test pins the same defect from the other side, with content rather
than absence: both trees carry the path, only one carries the violation.

Zero third-party deps, same as the rest of the suite.
"""

import io
import contextlib
import os
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

# Every scanner taking both --root and a path list. `board`, `publishscan` and
# `harvestscan` accept a path list and ignore it (their unit is the repo) and
# `coldsweep` walks from root, so none of the four can hold this defect;
# `pointerscan` is the tool the fix was copied FROM and is here to keep it
# honest.
SCANNERS = (
    "datescan", "leakscan", "linkscan", "pathscan", "plainscan", "pointerscan",
    "reviewscan", "secretscan", "sizescan", "spellscan", "stampscan",
    "wrapscan",
)

PROBE = "docs/probe.md"


def run_main(name: str, argv: list[str]) -> int:
    """Call a scanner's main with its chatter captured."""
    module = __import__(name)
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        return module.main(argv)


class MixedRoot(unittest.TestCase):
    def setUp(self):
        self._root_td = tempfile.TemporaryDirectory()
        self._cwd_td = tempfile.TemporaryDirectory()
        self.root = Path(self._root_td.name)
        self.cwd = Path(self._cwd_td.name)
        for tree in (self.root, self.cwd):
            (tree / "docs").mkdir(parents=True)
        self._was = Path.cwd()
        os.chdir(self.cwd)

    def tearDown(self):
        os.chdir(self._was)
        self._root_td.cleanup()
        self._cwd_td.cleanup()

    def test_relative_target_resolves_against_root_not_cwd(self):
        # The path exists ONLY in the tree the caller is standing in.
        (self.cwd / PROBE).write_text("# a probe\n\nshort lines.\n",
                                      encoding="utf-8")
        for name in SCANNERS:
            with self.subTest(scanner=name):
                code = run_main(name, ["--root", str(self.root), PROBE])
                self.assertEqual(
                    code, 2,
                    f"{name} resolved {PROBE} against the caller's cwd — it "
                    "scanned the wrong tree and did not say so")

    def test_absolute_target_is_still_taken_as_given(self):
        # --root must not silently re-home a path the caller spelled in full.
        target = self.cwd / PROBE
        target.write_text("# a probe\n\nshort lines.\n", encoding="utf-8")
        for name in SCANNERS:
            with self.subTest(scanner=name):
                code = run_main(name, ["--root", str(self.root), str(target)])
                self.assertNotEqual(
                    code, 2,
                    f"{name} rewrote an absolute target under --root and then "
                    "could not find it")

    def test_the_finding_comes_from_the_root_trees_file(self):
        # Content, not absence: both trees carry the path, and only one of them
        # breaks the rule. Whichever file the tool actually read decides the
        # exit code, so the code names the tree.
        # Spaces matter: wrapscan exempts a long unbreakable token (a URL, a
        # generated line), so a 200-column run of `x` would pass and prove
        # nothing about which file was read.
        wide = "word " * 45 + "\n"
        (self.cwd / PROBE).write_text("# probe\n\nshort.\n", encoding="utf-8")
        (self.root / PROBE).write_text(f"# probe\n\n{wide}", encoding="utf-8")
        self.assertEqual(
            run_main("wrapscan", ["--root", str(self.root), PROBE]), 1,
            "wrapscan read the caller's clean file instead of the root "
            "tree's over-wide one")

        # Swap the trees: the same command must now pass, for the same reason.
        (self.cwd / PROBE).write_text(f"# probe\n\n{wide}", encoding="utf-8")
        (self.root / PROBE).write_text("# probe\n\nshort.\n", encoding="utf-8")
        self.assertEqual(
            run_main("wrapscan", ["--root", str(self.root), PROBE]), 0,
            "wrapscan read the caller's over-wide file instead of the root "
            "tree's clean one")


if __name__ == "__main__":
    unittest.main()
