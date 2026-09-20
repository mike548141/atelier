"""Stdlib-only tests for conflictscan (no pytest needed): `python3 -m unittest`."""

import contextlib
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import conflictscan as cs
import memprobe

TOOLS_DIR = Path(__file__).resolve().parent


def scan(text):
    return cs.scan_text("t", text)


def kinds(text):
    return [f.kind for f in scan(text)]


class OpenerAndCloser(unittest.TestCase):
    """OPENER/CLOSER are unconditional findings — no state gate, unlike
    SEPARATOR/BASE (see AmbiguityGate below)."""

    def test_opener_alone_flags(self):
        self.assertEqual(["opener"], kinds("<<<<<<< HEAD\n"))

    def test_closer_alone_flags_even_with_no_opener(self):
        # A malformed/truncated file (only the tail of a diff was captured)
        # still flags — the shape is unambiguous on its own.
        self.assertEqual(["closer"], kinds(">>>>>>> branch\n"))

    def test_opener_requires_trailing_space(self):
        # Fewer/more than seven `<` characters, or none of the boilerplate
        # after the marker, is not the shape.
        self.assertEqual([], scan("<<<<<< HEAD\n"))
        self.assertEqual([], scan("<<<<<<<HEAD\n"))

    def test_full_conflict_all_four_lines_flag(self):
        text = "\n".join([
            "before",
            "<<<<<<< HEAD",
            "ours",
            "=======",
            "theirs",
            ">>>>>>> feature",
            "after",
        ]) + "\n"
        self.assertEqual(["opener", "separator", "closer"], kinds(text))


class AmbiguityGate(unittest.TestCase):
    """THE `=======` AMBIGUITY — a bare separator is also a valid Markdown/
    RST setext underline. The rule is exact-length AND in-conflict-state,
    both at once (see the module docstring)."""

    def test_standalone_setext_heading_is_clean(self):
        self.assertEqual([], scan("Legend\n=======\n\nbody\n"))

    def test_seven_char_heading_coincidence_is_still_clean(self):
        # Exactly seven characters above the underline — the length check
        # alone could not distinguish this from a real separator; the state
        # gate is what keeps it clean (no opener precedes it).
        self.assertEqual(7, len("Heading"[:7]))
        self.assertEqual([], scan("Heading\n=======\n"))

    def test_separator_after_opener_flags(self):
        self.assertEqual(["opener", "separator"],
                         kinds("<<<<<<< HEAD\n=======\n"))

    def test_separator_after_closer_no_longer_in_conflict(self):
        # The closer resets state — a setext heading appearing LATER in the
        # same file, after the conflict has been closed, must not flag.
        text = "<<<<<<< HEAD\n=======\n>>>>>>> x\n\nLegend\n=======\n"
        self.assertEqual(["opener", "separator", "closer"], kinds(text))

    def test_more_or_fewer_than_seven_equals_never_flags(self):
        # `wrapscan`'s own doctrine files use `===` and longer runs for
        # setext headings; only the exact seven-character shape is even a
        # CANDIDATE, and only inside an open region. The opener itself still
        # flags (see OpenerAndCloser) — it is the SEPARATOR that must not.
        self.assertEqual(["opener"], kinds("<<<<<<< HEAD\n======\n"))
        self.assertEqual(["opener"], kinds("<<<<<<< HEAD\n========\n"))

    def test_trailing_cr_still_matches(self):
        self.assertEqual(["opener", "separator"],
                         kinds("<<<<<<< HEAD\r\n=======\r\n"))


class Diff3Base(unittest.TestCase):
    def test_base_marker_inside_conflict_flags(self):
        text = "<<<<<<< HEAD\n||||||| merged common ancestors\n=======\n>>>>>>> x\n"
        self.assertEqual(["opener", "base", "separator", "closer"], kinds(text))

    def test_base_marker_outside_conflict_is_clean(self):
        self.assertEqual([], scan("||||||| stray line, no opener anywhere\n"))


class UnclosedResidual(unittest.TestCase):
    """Honest, stated trade: an unclosed opener leaves the REST of the file
    treated as still-open, so a later setext heading also flags. Accepted
    because a file that opens a conflict and never closes it is already the
    failure this scanner exists to catch (see the module docstring)."""

    def test_unclosed_opener_flags_a_later_setext_heading_too(self):
        text = "<<<<<<< HEAD\nours, never resolved\n\nLegend\n=======\n"
        self.assertEqual(["opener", "separator"], kinds(text))


class InlineQuoteIsClean(unittest.TestCase):
    """The markers appearing MID-LINE (not anchored at line start) never
    match — this is the item's own worked case, and the reason a doc that
    quotes them inline needs no allow-marker at all."""

    def test_backtick_quoted_inline_markers_do_not_flag(self):
        text = ("the markers are `<<<<<<< HEAD`, `=======`, "
                "`>>>>>>> sha` — all inline\n")
        self.assertEqual([], scan(text))


class AllowMarker(unittest.TestCase):
    def test_reasoned_marker_exempts_and_is_counted(self):
        tally = cs.Tally()
        found = cs.scan_text(
            "t", "<<<<<<< HEAD  <!-- conflictscan:allow: doc example -->\n",
            tally)
        self.assertEqual([], found)
        self.assertEqual(1, tally.marker_total)
        self.assertEqual({"opener": 1}, tally.by_marker)

    def test_bare_marker_without_reason_does_not_exempt(self):
        found = scan("<<<<<<< HEAD  <!-- conflictscan:allow -->\n")
        self.assertEqual(1, len(found))

    def test_prose_mention_does_not_exempt(self):
        found = scan("<<<<<<< HEAD  we discussed conflictscan:allow here\n")
        self.assertEqual(1, len(found))


class BinarySkip(unittest.TestCase):
    def test_null_byte_file_is_skipped(self):
        self.assertTrue(cs._looks_binary(b"\x00" + b"<<<<<<< HEAD\n"))

    def test_ordinary_text_is_not_binary(self):
        self.assertFalse(cs._looks_binary(b"<<<<<<< HEAD\n"))


class Ignore(unittest.TestCase):
    def test_exact_glob(self):
        self.assertTrue(cs._ignored("docs/fixture.md", ["docs/fixture.md"]))

    def test_subtree_glob(self):
        self.assertTrue(cs._ignored("docs/sessions/x.md", ["docs/sessions/"]))

    def test_non_match(self):
        self.assertFalse(cs._ignored("docs/real.md", ["docs/fixture.md"]))


class WholeTree(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _main(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            return cs.main(argv)

    def test_all_file_types_are_scanned_not_just_markdown(self):
        # Unlike datescan/wrapscan/spellscan, conflictscan is NOT
        # Markdown-only: a merge can fence a marker into any tracked file.
        self._write("src/app.py", "<<<<<<< HEAD\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))

    def test_defaults_to_whole_repo_not_docs_subdir(self):
        self._write("README.md", "<<<<<<< HEAD\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))

    def test_clean_tree_exits_zero(self):
        self._write("docs/note.md", "# OK\n\nLegend\n=======\n\nnothing open.\n")
        self.assertEqual(0, self._main(["--root", str(self.tmp)]))

    def test_nonexistent_path_is_an_error_not_a_pass(self):
        self.assertEqual(
            2, self._main(["--root", str(self.tmp), str(self.tmp / "gone")]))

    def test_conflictscanignore_exempts_path(self):
        self._write("docs/note.md", "<<<<<<< HEAD\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))
        self._write(".conflictscanignore",
                    "# a reasoned fixture exemption\ndocs/note.md\n")
        self.assertEqual(0, self._main(["--root", str(self.tmp)]))

    def test_unreasoned_ignore_glob_is_a_config_error(self):
        self._write("docs/note.md", "clean\n")
        self._write(".conflictscanignore", "docs/note.md\n")
        self.assertEqual(2, self._main(["--root", str(self.tmp)]))

    def test_binary_file_is_skipped_not_scanned(self):
        p = self.tmp / "blob.bin"
        p.write_bytes(b"\x00\x01<<<<<<< HEAD\n")
        self.assertEqual(0, self._main(["--root", str(self.tmp)]))

    def test_json_output_shape(self):
        import json
        self._write("note.md", "<<<<<<< HEAD\n")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = cs.main(["--json", "--root", str(self.tmp)])
        self.assertEqual(1, code)
        payload = json.loads(out.getvalue())
        self.assertFalse(payload["clean"])
        self.assertEqual(1, len(payload["findings"]))
        self.assertEqual("opener", payload["findings"][0]["kind"])


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, cs._selftest())


class StagedAbsolutePathTest(unittest.TestCase):
    """Matches secretscan's/leakscan's own guard: an absolute path in
    --staged mode matches no repo-relative prefix git reports, so a naive
    implementation would silently scan nothing and exit 0."""

    def _run(self, *argv):
        return subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "conflictscan.py"),
             *argv],
            capture_output=True, text=True)

    def test_absolute_staged_path_is_refused(self):
        r = self._run("--staged", "--root", "/tmp", "/tmp/anything")
        self.assertEqual(2, r.returncode)
        self.assertIn("repo-relative", r.stderr)


def _git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True, check=True,
        env={**os.environ,
             "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid",  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
             "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"})  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo


class StagedRealGitRepo(unittest.TestCase):
    """Drives an actual `git add`/staged diff, the way the pre-commit hook
    would — proves `staged_added_lines` reads the index, not the worktree
    or an unrelated tree (matches the discipline `test_precommit.py` and the
    mixed-root suite already hold every other scanner to)."""

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo, ignore_errors=True)
        _git(self.repo, "init", "-q")
        self._old_cwd = os.getcwd()
        os.chdir(self.repo)

    def tearDown(self):
        os.chdir(self._old_cwd)

    def _main(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            return cs.main(argv)

    def test_staged_addition_of_a_conflict_marker_blocks(self):
        (self.repo / "note.md").write_text("<<<<<<< HEAD\n=======\n>>>>>>> x\n")
        _git(self.repo, "add", "note.md")
        self.assertEqual(1, self._main(["--staged", "--root", str(self.repo)]))

    def test_staged_clean_file_passes(self):
        (self.repo / "note.md").write_text("# fine\n\nLegend\n=======\n")
        _git(self.repo, "add", "note.md")
        self.assertEqual(0, self._main(["--staged", "--root", str(self.repo)]))

    def test_unstaged_marker_is_invisible_to_staged_mode(self):
        # By design (matches secretscan/leakscan): --staged reads the INDEX,
        # not the worktree — an edit that was never `git add`-ed is not part
        # of the commit this hook is guarding.
        (self.repo / "tracked.md").write_text("clean\n")
        _git(self.repo, "add", "tracked.md")
        _git(self.repo, "commit", "-q", "-m", "init")
        (self.repo / "tracked.md").write_text("clean\n<<<<<<< HEAD\n")
        self.assertEqual(0, self._main(["--staged", "--root", str(self.repo)]))


class BoundedMemory(unittest.TestCase):
    """020/380 — the same class of defect `020/370` fixed in `secretscan`,
    applied here: peak memory must be bounded by a constant that does not
    grow with the size of the input. Mike's ruling, verbatim: "it should not
    matter how much it scans it should no have this affect."

    Runs the real CLI as a SUBPROCESS via `memprobe.run_and_measure` and
    reads its peak RSS back from the kernel — `tracemalloc` only sees the
    Python heap, not the whole OS process (see `tools/memprobe.py`'s module
    docstring).

    Content is plain filler prose with no conflict-marker-shaped line
    anywhere, so both runs produce zero findings — the only thing that
    differs between a small and a large run is how many bytes there are to
    read."""

    CONFLICTSCAN = str(TOOLS_DIR / "conflictscan.py")
    SMALL_BYTES = 1 * 1024 * 1024
    LARGE_BYTES = 8 * 1024 * 1024
    # Grounded in the FIX's design, not fitted to a measurement
    # (`ground-numeric-limits`): the one piece of per-file state the
    # streaming reader ever buffers is a single window of one physical
    # line, capped at `LINE_WINDOW_BYTES + LINE_WINDOW_OVERLAP` (~4.06 MiB)
    # — see `conflictscan._iter_numbered_lines`. Both runs produce zero
    # findings, so growth between them should be close to zero. Allowing
    # 4x that window leaves generous headroom for interpreter/allocator
    # noise while staying far below what a whole-file-buffered
    # implementation shows for this size delta.
    GROWTH_BOUND_BYTES = 4 * (cs.LINE_WINDOW_BYTES + cs.LINE_WINDOW_OVERLAP)

    @staticmethod
    def _build(target_bytes: int, path: Path) -> None:
        with open(path, "w") as f:
            written = 0
            i = 0
            while written < target_bytes:
                line = f"this is filler line number {i} - no conflict marker here at all\n"
                f.write(line)
                written += len(line)
                i += 1

    def _peak_rss_for(self, size_bytes: int) -> int:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        self._build(size_bytes, tmp / "data.txt")
        result = memprobe.run_and_measure(
            [sys.executable, self.CONFLICTSCAN, "--root", str(tmp), str(tmp)],
            timeout=60, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        self.assertEqual(0, result.returncode,
                         "filler content must not itself flag anything")
        return result.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_input_size(self):
        small_peak = self._peak_rss_for(self.SMALL_BYTES)
        large_peak = self._peak_rss_for(self.LARGE_BYTES)
        growth = large_peak - small_peak
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for a "
            f"{(self.LARGE_BYTES - self.SMALL_BYTES) / 1e6:.1f} MB larger input "
            f"(small={small_peak / 1e6:.1f} MB, large={large_peak / 1e6:.1f} MB) "
            "— memory is scaling with input size again (020/380).")


class LinkedWorktreeSkipped(unittest.TestCase):
    """020/160 (E9): `_walk_files` must prune a directory whose `.git` entry
    is a regular FILE (`gitdir: <path>`, the linked-worktree/submodule
    marker) — not just one literally named `.git` that is a directory.
    Before this fix a session's own gitignored `.claude/worktrees/<name>/`
    grew into a full second checkout of the tree that the walk descended
    into anyway, double-counting every finding (measured in `faves`
    2026-08-15)."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _found(self):
        return {str(p.relative_to(self.tmp))
                for p in cs._walk_files(self.tmp)}

    def test_linked_worktree_directory_is_pruned(self):
        self._write("real.txt", "content\n")
        self._write(".claude/worktrees/wt1/.git",
                    "gitdir: /elsewhere/.git/worktrees/wt1\n")
        self._write(".claude/worktrees/wt1/real.txt", "content\n")
        found = self._found()
        self.assertIn("real.txt", found)
        self.assertNotIn(".claude/worktrees/wt1/real.txt", found)
        self.assertNotIn(".claude/worktrees/wt1/.git", found)

    def test_independent_nested_repos_own_git_dir_still_pruned(self):
        """Unaffected by this fix: a nested repo whose `.git` is a
        DIRECTORY, not a linked worktree, was already excluded by the
        existing skip-dir-names rule matching the bare name `.git` at any
        depth inside it — this pins that it still holds."""
        self._write("nested/.git/objects/pack/dummy", "not real git data\n")
        self._write("nested/real.txt", "content\n")
        found = self._found()
        self.assertIn("nested/real.txt", found)
        self.assertNotIn("nested/.git/objects/pack/dummy", found)

    def test_ordinary_dotgit_file_is_treated_as_a_marker_too(self):
        """Deliberate, not a bug: the check is file-ness only, never
        content (see `_walk_files`'s comment) — a bare regular file
        literally named `.git` anywhere is treated as a worktree/submodule
        marker and prunes its parent, even holding no real `gitdir:` line
        as here. Accepted cost of the item's own stated minimum fix:
        nothing else legitimately creates a file with that exact name."""
        self._write("weird/.git", "not a real worktree marker\n")
        self._write("weird/real.txt", "content\n")
        found = self._found()
        self.assertNotIn("weird/real.txt", found)


if __name__ == "__main__":
    unittest.main()
