"""Tests for the shared exit-code contract and report lines
(`tools/report.py`, `115/080` part 3).

Two jobs, as `test_allowmarker.py` does for the marker grammar. (1) Test each
helper against literal strings, so the module's own contract has a proof that
does not route through any one scanner (FW3: a shared module with no test of
its own is proven eleven times through its callers, or not at all). (2) Pin
the lines each converted scanner prints, as literals: what a scanner prints is
a contract with every child (they float on atelier's floor at `main`), so a
shared edit that changes any one scanner's line must fail here, loudly, before
it reaches a child's CI.

Two divergences between scanners are pinned AS THEY ARE — not endorsed:
datescan prints no tally on its findings path, and indexscan's over-cap line
carries no cap clause. Unifying either changes output, which this part does
not do.
"""

import contextlib
import inspect
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import unittest
import unittest.mock
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report  # noqa: E402

CAP = "the 50000-finding cap (counted, not listed)"


def _stderr_of(fn, *args, **kwargs):
    buf = io.StringIO()
    with contextlib.redirect_stderr(buf):
        rc = fn(*args, **kwargs)
    return rc, buf.getvalue()


class TestExitContract(unittest.TestCase):
    def test_codes(self):
        self.assertEqual((report.EXIT_CLEAN, report.EXIT_FINDINGS,
                          report.EXIT_BROKEN), (0, 1, 2))

    def test_exit_code_reads_truthiness(self):
        for blocking, want in ((0, 0), (1, 1), (7, 1), ([], 0), (["f"], 1),
                               (False, 0), (True, 1)):
            self.assertEqual(report.exit_code(blocking), want, blocking)

    def test_warn_always_exits_zero(self):
        self.assertEqual(report.exit_code(5, warn=True), 0)
        self.assertEqual(report.exit_code(0, warn=True), 0)

    def test_broken_prints_one_prefixed_line_and_exits_two(self):
        rc, err = _stderr_of(report.broken, "demoscan", "it broke")
        self.assertEqual((rc, err), (2, "demoscan: it broke\n"))

    def test_guarded_main_passes_the_run_code_through(self):
        for code in (0, 1, 2):
            rc, err = _stderr_of(report.guarded_main, "demoscan",
                                 lambda argv, c=code: c, None, (ValueError,))
            self.assertEqual((rc, err), (code, ""))

    def test_guarded_main_turns_a_config_error_into_exit_two(self):
        def run(argv):
            raise KeyError("bad glob")
        rc, err = _stderr_of(report.guarded_main, "demoscan", run, ["x"],
                             (ValueError, KeyError))
        self.assertEqual((rc, err), (2, "demoscan: 'bad glob'\n"))

    def test_guarded_main_reports_other_errors_as_a_broken_scan(self):
        """RT4 (160/730): a crash is a broken scan (2), not "findings" (1),
        and it is not swallowed: the traceback is printed in full."""
        def run(argv):
            raise RuntimeError("a defect, not a config error")
        rc, err = _stderr_of(report.guarded_main, "demoscan", run, None,
                             (ValueError,))
        self.assertEqual(2, rc)
        self.assertIn("Traceback (most recent call last)", err)
        self.assertIn("RuntimeError: a defect, not a config error", err)
        self.assertIn("demoscan: internal error", err)

    def test_guarded_main_turns_an_unreadable_file_into_the_cannot_read_line(self):
        """RT4a (160/730): an unreadable ignore file used to be a traceback and
        Python's exit 1 on four guards."""
        def run(argv):
            raise PermissionError(13, "Permission denied", "/r/.xignore")
        rc, err = _stderr_of(report.guarded_main, "demoscan", run, None,
                             (ValueError,))
        self.assertEqual((2, "demoscan: cannot read /r/.xignore: "
                             "Permission denied\n"), (rc, err))

    def test_guarded_main_an_oserror_naming_no_file_is_a_traceback_and_two(self):
        def run(argv):
            raise OSError("something else")
        rc, err = _stderr_of(report.guarded_main, "demoscan", run, None,
                             (ValueError,))
        self.assertEqual(2, rc)
        self.assertIn("Traceback", err)

    def test_guarded_main_lets_usage_exits_and_interrupts_through(self):
        for exc in (SystemExit(2), KeyboardInterrupt()):
            def run(argv, exc=exc):
                raise exc
            with self.assertRaises(type(exc)):
                report.guarded_main("demoscan", run, None, (ValueError,))

    def test_broken_strips_control_and_bidi_characters(self):
        """RT3 (160/730): a path or an ignore-file glob reaches the terminal."""
        rc, err = _stderr_of(report.broken, "demoscan",
                             "bad \x1b[2J\x1b[H\x07path \u202eevil\x9b\x7f end")
        self.assertEqual(2, rc)
        self.assertEqual("demoscan: bad [2J[Hpath evil end\n", err)

    def test_broken_keeps_newlines_and_ordinary_text(self):
        rc, err = _stderr_of(report.broken, "d", "line one\n  line two t\u014dhutu")
        self.assertEqual("d: line one\n  line two t\u014dhutu\n", err)

    def test_every_helper_that_prints_goes_through_broken(self):
        for fn, args in ((report.cannot_read, ("d", OSError(13, "denied\x1b[2J", "a\x1bb"))),
                         (report.refuse_missing_paths, ("d", [Path("x\x1b[2Jy")]))):
            rc, err = _stderr_of(fn, *args)
            self.assertEqual(2, rc)
            self.assertNotIn("\x1b", err)

    def test_exit_code_is_typed_int_or_bool(self):
        self.assertIn("int | bool", str(inspect.signature(report.exit_code)))

    def test_is_vanished_names_the_race_and_nothing_else(self):
        self.assertTrue(report.is_vanished(FileNotFoundError(2, "gone")))
        self.assertTrue(report.is_vanished(NotADirectoryError(20, "x")))
        self.assertTrue(report.is_vanished(IsADirectoryError(21, "x")))
        self.assertFalse(report.is_vanished(PermissionError(13, "denied")))
        self.assertFalse(report.is_vanished(OSError(5, "I/O error")))

    def test_guarded_main_hands_argv_through(self):
        seen = []
        report.guarded_main("demoscan", lambda argv: seen.append(argv) or 0,
                            ["--root", "."], (ValueError,))
        self.assertEqual(seen, [["--root", "."]])


class TestBrokenScanLines(unittest.TestCase):
    def test_resolve_targets(self):
        root = Path("/r")
        self.assertEqual(report.resolve_targets(root, ["docs", "/abs/x", "/r"]),
                         [Path("/r/docs"), Path("/abs/x"), Path("/r")])
        self.assertEqual(report.resolve_targets(root, []), [])

    def test_advisory_count_line_is_the_wording_floor_reads(self):
        """RT6 (160/730): one home for the line `floor.advisory_count_rx`
        parses; secretscan, leakscan and licenscan all build it here."""
        import floor
        import leakscan
        import licenscan
        import secretscan
        for name, mod in (("secretscan", secretscan), ("leakscan", leakscan),
                          ("licenscan", licenscan)):
            for n in (0, 1, 77):
                line = report.advisory_count_line(name, n)
                self.assertEqual(line, mod.advisory_count_line(n))
                self.assertEqual(n, floor._read_advisory_count(
                    "finding line\n" + line + "\n", name))
        self.assertEqual("  x advisory: 3 finding(s) \u2014 reported, not blocking.",
                         report.advisory_count_line("x", 3))

    def test_the_privately_spelt_lines_are_recorded_in_the_module_docstring(self):
        doc = " ".join(report.__doc__.split())
        for needle in ("LINES STILL SPELT PRIVATELY", "licenscan", "publishscan",
                       "reviewscan", "stampscan"):
            self.assertIn(needle, doc)

    def test_note_empty_scope_speaks_only_when_a_scope_left_nothing(self):
        """RT2 (160/730): the spelling refusals (115/360, 160/950) were already
        in; this is the residual 'clean over zero files' line."""
        rc, err = _stderr_of(lambda: report.note_empty_scope("d", 3, 0, ["docs/"]))
        self.assertIn("none of the 3 staged file(s) is in the --staged scope (docs/)", err)
        self.assertIn("nothing was scanned", err)
        for args in ((3, 2, ["docs/"]), (0, 0, ["docs/"]), (3, 0, []), (3, 3, [])):
            rc, err = _stderr_of(lambda a=args: report.note_empty_scope("d", *a))
            self.assertEqual("", err, args)

    def test_scope_staged_notes_an_empty_scope_without_changing_the_result(self):
        staged = {"a.txt": {1}, "b/c.txt": {2}}
        with unittest.mock.patch.object(report, "resolve_staged_scope",
                                        return_value=(None, frozenset({"zzz"}))):
            result, err = _stderr_of(report.scope_staged, "d", staged,
                                     ["docs/"], "x/")
        self.assertEqual((None, {}), result)
        self.assertIn("nothing was scanned", err)

    def test_refuse_escaping_targets(self):
        """RT7 (160/730): a relative target must stay under --root."""
        root = Path("/r")
        for ok in ([], ["docs"], ["docs/../src"], ["./docs"], ["/abs/x"],
                   ["/elsewhere/../x"], ["."], ["a/b/../.."]):
            self.assertIsNone(report.refuse_escaping_targets("d", root, ok), ok)
        for bad in (["../x"], ["docs/../../x"], ["a/b/../../.."], ["..", "docs"]):
            rc, err = _stderr_of(report.refuse_escaping_targets, "d", root, bad)
            self.assertEqual(2, rc, bad)
            self.assertIn("climb out of --root", err)
        rc, err = _stderr_of(report.refuse_escaping_targets, "d",
                             Path("/r"), ["../r-sibling/x"])
        self.assertEqual(2, rc)

    def test_missing_root(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertIsNone(report.refuse_missing_root("d", Path(td), td))
            rc, err = _stderr_of(report.refuse_missing_root, "d",
                                 Path(td) / "gone", "gone")
        self.assertEqual((rc, err), (2, "d: root does not exist: gone\n"))

    def test_missing_paths_names_every_one(self):
        with tempfile.TemporaryDirectory() as td:
            t = Path(td)
            self.assertIsNone(report.refuse_missing_paths("d", [t]))
            rc, err = _stderr_of(report.refuse_missing_paths, "d",
                                 [t, t / "a", t / "b"])
        self.assertEqual(rc, 2)
        self.assertEqual(err, f"d: path does not exist: {t / 'a'}, {t / 'b'}\n")

    def test_cannot_read(self):
        e = OSError(13, "Permission denied", "docs/x.md")
        rc, err = _stderr_of(report.cannot_read, "d", e)
        self.assertEqual((rc, err), (2, "d: cannot read docs/x.md: Permission denied\n"))

    def test_git_diff_failed(self):
        rc, err = _stderr_of(report.git_diff_failed, "d", RuntimeError("boom"))
        self.assertEqual((rc, err), (2, "d: git diff failed: boom\n"))

    def test_absolute_staged_refused_with_the_guards_own_example(self):
        self.assertIsNone(report.refuse_absolute_staged("d", ["src/", "a.py"], "src/"))
        self.assertIsNone(report.refuse_absolute_staged("d", [], "src/"))
        rc, err = _stderr_of(report.refuse_absolute_staged, "d",
                             ["ok/", "/abs/one", "/abs/two"], "sub/")
        self.assertEqual(rc, 2)
        self.assertEqual(err, (
            "d: --staged needs repo-relative path(s), got absolute: "
            "/abs/one, /abs/two\n"
            "  git lists staged paths relative to the repo root, so an absolute "
            "path matches nothing\n"
            "  and the scan would pass while covering nothing. Pass e.g. "
            "'sub/' instead.\n"))


class StagedScopeResolution(unittest.TestCase):
    """115/360 + 160/950 — what a `--staged` positional names is decided by
    git, in a real repo, never by a prefix compare against a spelling."""

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo, ignore_errors=True)
        self.git("init", "-q")
        old = os.getcwd()
        os.chdir(self.repo)
        self.addCleanup(os.chdir, old)
        for d in ("docs", "src", "docs-extra", "gone"):
            (self.repo / d).mkdir()
        for f in ("docs/a.md", "src/b.py", "docs-extra/x.md", "gone/g.md",
                  "src/moved.py", "top.md"):
            (self.repo / f).write_text(f + "\n")
        self.git("add", "--", ".")
        self.git("commit", "-q", "-m", "seed")
        # Now stage a change: modify docs/a.md, add docs/new.md, delete the
        # whole `gone/` directory, rename src/moved.py away.
        (self.repo / "docs/a.md").write_text("changed\n")
        (self.repo / "docs/new.md").write_text("new\n")
        self.git("rm", "-q", "--", "gone/g.md")
        self.git("mv", "src/moved.py", "docs/moved.py")
        self.git("add", "--", "docs/a.md", "docs/new.md")
        self.staged = {"docs/a.md": 1, "docs/new.md": 1, "docs/moved.py": 1,
                       "docs-extra/x.md": 1, "top.md": 1}

    def git(self, *args):
        subprocess.run(
            ["git", "-C", str(self.repo), "-c", "user.name=t",
             "-c", "user.email=t", "-c", "commit.gpgsign=false", *args],
            check=True, capture_output=True)

    def scope(self, *p):
        return report.scope_staged("d", self.staged, p, "src/")

    def test_dot_slash_and_empty_are_no_restriction_or_the_same_path(self):
        self.assertEqual((None, self.staged), self.scope("."))
        self.assertEqual((None, self.staged), self.scope("./"))
        self.assertEqual((None, self.staged), self.scope())
        want = {"docs/a.md": 1, "docs/new.md": 1, "docs/moved.py": 1}
        self.assertEqual((None, want), self.scope("./docs"))
        self.assertEqual((None, want), self.scope("docs//"))
        self.assertEqual((None, {"top.md": 1}), self.scope("./top.md"))

    def test_the_prefix_is_a_directory_not_a_name_prefix(self):
        """160/950 QS4: `docs` is `docs/`, never `docs-extra/`."""
        rc, got = self.scope("docs")
        self.assertNotIn("docs-extra/x.md", got)
        self.assertEqual((None, {"docs-extra/x.md": 1}), self.scope("docs-extra"))

    def test_an_exact_file_is_that_file(self):
        self.assertEqual((None, {"docs/a.md": 1}), self.scope("docs/a.md"))

    def test_a_tracked_scope_with_nothing_staged_is_not_refused(self):
        self.assertEqual((None, {}), self.scope("src"))

    def test_a_scope_whose_files_this_commit_removes_still_resolves(self):
        """`gone/` is no longer in the index; the commit deletes it. A removal
        under a scope is under it (leakscan's removed list is cut by this)."""
        rc, allowed = report.resolve_staged_scope("d", ["gone"], "src/")
        self.assertIsNone(rc)
        self.assertEqual(frozenset({"gone/g.md"}), allowed)

    def test_a_rename_is_under_both_its_scopes(self):
        rc, allowed = report.resolve_staged_scope("d", ["src/moved.py"], "src/")
        self.assertIsNone(rc)
        self.assertEqual(frozenset({"src/moved.py"}), allowed)
        rc, allowed = report.resolve_staged_scope("d", ["docs/moved.py"], "src/")
        self.assertEqual(frozenset({"docs/moved.py"}), allowed)

    def test_a_name_git_does_not_know_is_refused(self):
        """160/950 QS1/QS2: typo, case variant, literal glob, `~`."""
        for bad in ("nowhere", "Docs", "DOCS/a.md", "docs/*", "docs/?.md",
                    "~/docs", "docs/A.md"):
            with self.subTest(bad=bad):
                (rc, _), err = _stderr_of(report.scope_staged, "d",
                                          self.staged, [bad], "src/")
                self.assertEqual(2, rc)
                self.assertIn("d: --staged path(s) name nothing git knows: "
                              + bad, err)
                self.assertIn("'src/'", err)

    def test_a_unicode_variant_is_resolved_by_git_or_refused_never_empty(self):
        d = "caf\u00e9"
        (self.repo / d).mkdir()
        (self.repo / d / "c.md").write_text("c\n")
        self.git("add", "--", d + "/c.md")
        staged = {d + "/c.md": 1}
        nfd = unicodedata.normalize("NFD", d)
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            rc, got = report.scope_staged("d", staged, [nfd], "src/")
        self.assertIn(rc, (None, 2))
        if rc is None:
            self.assertEqual(staged, got)

    def test_a_subdirectory_cwd_reads_root_relative_spellings(self):
        os.chdir(self.repo / "docs")
        self.assertEqual((None, {"docs/a.md": 1}),
                         report.scope_staged("d", self.staged, ["docs/a.md"],
                                             "src/"))
        (rc, _), _err = _stderr_of(report.scope_staged, "d", self.staged,
                                   ["a.md"], "src/")
        self.assertEqual(2, rc)

    def test_the_environment_cannot_turn_a_path_into_a_glob(self):
        with unittest.mock.patch.dict(os.environ, {
                "GIT_LITERAL_PATHSPECS": "1", "GIT_GLOB_PATHSPECS": "1",
                "GIT_ICASE_PATHSPECS": "1"}):
            self.assertEqual((None, {"docs/a.md": 1}), self.scope("docs/a.md"))
            (rc, _), _err = _stderr_of(report.scope_staged, "d", self.staged,
                                       ["Docs"], "src/")
            self.assertEqual(2, rc)

    def test_a_path_leaving_the_repo_is_refused(self):
        for bad in ("..", "../x", "./../x", "docs/../../x"):
            (rc, _), err = _stderr_of(report.scope_staged, "d", self.staged,
                                      [bad], "src/")
            self.assertEqual(2, rc, bad)
            self.assertIn("climb out of the repo", err)

    def test_the_spelling_is_normalised_as_posix_whatever_the_host(self):
        """160/950 QS10: git's paths are POSIX, so the reader must not use the
        host's `os.path` (`docs\\sub` on a backslash host matches nothing)."""
        src = inspect.getsource(report.resolve_staged_scope)
        self.assertIn("posixpath.normpath", src)
        self.assertNotIn("os.path.normpath", src)
        self.assertEqual((None, {"docs/a.md": 1}),
                         self.scope("docs/sub/../a.md"))

    def test_git_failure_is_a_broken_scan_not_a_pass(self):
        with unittest.mock.patch.object(
                report, "_git_scope_names",
                side_effect=subprocess.CalledProcessError(128, "git")):
            (rc, _), err = _stderr_of(report.scope_staged, "d", self.staged,
                                      ["docs"], "src/")
        self.assertEqual(2, rc)
        self.assertIn("git diff failed", err)

    def test_the_cwd_repo_must_be_the_root_repo(self):
        self.assertIsNone(report.refuse_other_repo("d", self.repo))
        os.chdir(self.repo / "docs")
        self.assertIsNone(report.refuse_other_repo("d", self.repo))
        other = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, other, ignore_errors=True)
        subprocess.run(["git", "-C", str(other), "init", "-q"], check=True)
        os.chdir(other)
        rc, err = _stderr_of(report.refuse_other_repo, "d", self.repo)
        self.assertEqual(2, rc)
        self.assertIn("is not the repo --root names", err)
        self.assertIn(os.path.realpath(other), err)
        plain = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, plain, ignore_errors=True)
        os.chdir(plain)
        rc, err = _stderr_of(report.refuse_other_repo, "d", self.repo)
        self.assertEqual(2, rc)
        self.assertIn("not inside a git repo", err)


class TestReportLines(unittest.TestCase):
    def test_heads(self):
        self.assertEqual(report.clean_head("d", "all good."), "✓ d clean — all good.")
        self.assertEqual(report.findings_head("d", 3), "✗ d: 3 finding(s).")
        self.assertEqual(report.findings_head("d", 1, noun="thing(s)",
                                              tail=" — blocked.\n"),
                         "✗ d: 1 thing(s) — blocked.\n")

    def test_cap_part_and_over_cap_line(self):
        self.assertEqual(report.cap_part(0, 7),
                         "0 beyond the 7-finding cap (counted, not listed)")
        self.assertEqual(report.over_cap_line(4, 7),
                         "  …and 4 more finding(s), counted but not listed "
                         "(past the 7-finding memory cap).")
        self.assertEqual(report.over_cap_line(4, 7, noun="x(s)", indent="   "),
                         "   …and 4 more x(s), counted but not listed "
                         "(past the 7-finding memory cap).")

    def test_suppressed_line_keeps_the_callers_order_and_zeros(self):
        self.assertEqual(report.suppressed_line(["0 b", "0 a"]),
                         "  suppressed: 0 b · 0 a")
        self.assertEqual(report.suppressed_line(["1 only"]), "  suppressed: 1 only")

    def test_breakdown_sorted_and_only_when_non_empty(self):
        self.assertEqual(report.suppressed_line(["x"], breakdown={}), "  suppressed: x")
        self.assertEqual(report.suppressed_line(["x"], breakdown={"zz": 1, "aa": 2}),
                         "  suppressed: x\n    allow-marker breakdown: aa×2, zz×1")

    def test_disabled_follows_the_breakdown(self):
        self.assertEqual(report.suppressed_line(["x"], disabled=()), "  suppressed: x")
        self.assertEqual(
            report.suppressed_line(["x"], breakdown={"r": 1}, disabled=("a", "b")),
            "  suppressed: x\n    allow-marker breakdown: r×1\n    disabled: a, b")
        self.assertEqual(report.suppressed_line(["x"], disabled=["a"]),
                         "  suppressed: x\n    disabled: a")

    def test_warn_notice(self):
        self.assertEqual(report.WARN_NOTICE,
                         "\n  (--warn: advisory only — not blocking this build.)")


class TestScannerLinePins(unittest.TestCase):
    """Each converted scanner's lines, as literals. A shared edit that moves
    any one of them fails here."""

    def test_conflictscan(self):
        import conflictscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      f".conflictscanignore · 0 beyond {CAP}")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ conflictscan clean — no conflict markers found.")
        t.findings_over_cap = 3
        lines = m.render_human([], t).splitlines()
        self.assertEqual(lines[0], "✗ conflictscan: 3 finding(s) — commit blocked.")
        self.assertEqual(lines[1], "  …and 3 more finding(s), counted but not listed "
                                   "(past the 50000-finding memory cap).")

    def test_linkscan(self):
        import linkscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      f".linkscanignore · 0 beyond {CAP}"
                                      " · 0 marker(s) naming no rule")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ linkscan clean — every internal link resolves.")
        t.findings_over_cap = 3
        lines = m.render_human([], t).splitlines()
        self.assertEqual(lines[:3], ["✗ linkscan: 3 broken internal link(s).", "",
                                     "  …and 3 more broken link(s), counted but not "
                                     "listed (past the 50000-finding memory cap)."])

    def test_datescan(self):
        import datescan as m
        t = m.Tally()
        t.note_marker("b")
        t.note_marker("a")
        self.assertEqual(t.summary(), "  suppressed: 2 by allow-marker · 0 file(s) by "
                                      ".datescanignore · 0 over-long line(s) scanned "
                                      "truncated · 0 marker(s) naming no rule"
                                      "\n    allow-marker breakdown: a×1, b×1")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ datescan clean — no relative-time words or non-ISO "
                         "dates found.")
        out = m.render_human([m.Finding("a.md", 1, "k", "w", "d")], t)
        self.assertEqual(out.splitlines()[0], "✗ datescan: 1 finding(s).")
        self.assertNotIn("suppressed:", out)  # pinned as-is, not endorsed

    def test_wrapscan(self):
        import wrapscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      ".wrapscanignore · 0 over-long line(s) scanned "
                                      "truncated")
        self.assertEqual(m.render_human([], 85, t).splitlines()[0],
                         "✓ wrapscan clean — no prose lines over 85 columns.")
        out = m.render_human([m.Finding("a.md", 1, 99, "x", "d")], 85, t)
        self.assertEqual(out.splitlines()[0],
                         "✗ wrapscan: 1 finding(s) (limit 85 columns).")

    def test_spellscan(self):
        import spellscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      ".spellscanignore · 0 over-long line(s) scanned "
                                      "truncated · 0 marker(s) naming no rule")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ spellscan clean — no US spellings found.")
        out = m.render_human([m.Finding("a.md", 1, "us-spelling", "color",
                                        "colour", "d")], t)
        self.assertEqual(out.splitlines()[0], "✗ spellscan: 1 finding(s).")

    def test_pathscan(self):
        import pathscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      ".pathscanignore · 0 record file(s) excluded by "
                                      f"default · 0 beyond {CAP}")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ pathscan clean — every candidate repo-path reference "
                         "resolves.")
        t.findings_over_cap = 3
        lines = m.render_human([], t).splitlines()
        self.assertEqual(lines[:2], ["✗ pathscan: 3 finding(s).",
                                     "  …and 3 more finding(s), counted but not "
                                     "listed (past the 50000-finding memory cap)."])

    def test_indexscan(self):
        import indexscan as m
        t = m.Tally()
        self.assertEqual(t.summary(),
                         "  checked: 0 declaration(s) in 0 index file(s), 0 entr(ies) "
                         "mapped, 0 dated index line(s) compared\n"
                         "  suppressed: 0 by allow-marker · 0 by exclude= · "
                         "0 by before= · 0 file(s) by .indexscanignore · "
                         f"0 beyond {CAP}")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ indexscan clean — no index declares a mapped directory "
                         "(nothing to check; adoption is opt-in per index).")
        t.declarations = 1
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ indexscan clean — every mapped entry is named by its index "
                         "and no dated line predates its file.")
        t.findings_over_cap = 3
        lines = m.render_human([], t).splitlines()
        # The over-cap line carries no cap clause — pinned as-is, not endorsed.
        self.assertEqual(lines[:2], ["✗ indexscan: 3 finding(s).",
                                     "  …and 3 more finding(s), counted but not listed."])

    def test_secretscan(self):
        import secretscan as m
        t = m.Tally(disabled_rules=("assigned",))
        self.assertEqual(t.summary(),
                         "  suppressed: 0 by allow-marker · 0 file(s) by .secretscanignore"
                         " · 1 rule(s) disabled · 0 public-key fingerprint(s) · 0 by "
                         "public-key line · 0 by published-url token · "
                         f"0 beyond {CAP} · 0 marker(s) naming no rule"
                         "\n    disabled: assigned")
        t.note_marker("r")
        self.assertIn("\n    allow-marker breakdown: r×1\n    disabled: assigned",
                      t.summary())
        self.assertEqual(m.render_human([], m.Tally()).splitlines()[0],
                         "✓ secretscan clean — no credentials in the scanned lines.")
        t = m.Tally()
        t.blocking_over_cap = 3
        lines = m.render_human([], t).splitlines()
        self.assertEqual(lines[:3], ["✗ secretscan: 3 finding(s) — commit blocked.", "",
                                     "  …and 3 more blocking finding(s), counted but "
                                     "not listed (past the 50000-finding memory cap)."])
        self.assertEqual(m._render_advisory([], 2)[-1],
                         "   …and 2 more advisory finding(s), counted but not listed "
                         "(past the 50000-finding memory cap).")

    def test_leakscan(self):
        import leakscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      ".leakscanignore · 0 rule(s) disabled · "
                                      "0 binary file(s) by .leakscanbinaries · "
                                      "0 untracked binary file(s) not gated · "
                                      "0 G3 finding(s) warned, not blocking, before "
                                      f"{m.BINARY_GRACE_UNTIL.isoformat()} · "
                                      "0 type-level metadata entr(y/ies) warned, "
                                      "not blocking, before "
                                      f"{m.TYPE_LEVEL_UNTIL.isoformat()} · "
                                      "0 manifest line(s) with no who/when warned, "
                                      "not blocking · "
                                      f"0 beyond {CAP} · "
                                      "0 marker(s) naming no rule")
        self.assertEqual(m.render_human([], None, True, t).splitlines()[0],
                         "✓ leakscan clean (structural + local).")
        t.findings_over_cap = 3
        lines = m.render_human([], None, False, t).splitlines()
        self.assertEqual(lines[:3], ["✗ leakscan: 3 finding(s) — commit blocked.", "",
                                     "  …and 3 more finding(s), counted but not "
                                     "listed (past the 50000-finding memory cap)."])

    def test_sizescan(self):
        import sizescan as m
        self.assertEqual(m._suppression_line(1, 2, 0, 3),
                         "  suppressed: 1 file(s) by sizescan:allow header · "
                         "2 file(s) by .sizescanignore · "
                         "3 inert hatch(es) (exempt nothing) · "
                         "0 beyond the 50000-finding cap (counted, not listed)")
        self.assertEqual(m.render_human([]),
                         "✓ sizescan clean — no relocatable cold content on the hot "
                         "path; archive stores hold no live markers.\n"
                         "  suppressed: 0 file(s) by sizescan:allow header · "
                         "0 file(s) by .sizescanignore · "
                         "0 inert hatch(es) (exempt nothing) · "
                         "0 beyond the 50000-finding cap (counted, not listed)")

    def test_licenscan(self):
        import licenscan as m
        rep = m.Report(repo_license="MIT")
        supp = ("  suppressed: 0 declaration(s) by allow-marker · 0 file(s) by "
                ".licenscanignore · 0 file(s) over 8 MiB scanned truncated")
        count = "  licenscan advisory: 0 finding(s) — reported, not blocking."
        self.assertEqual(m.render_human(rep),
                         "✓ licenscan clean — repo licence MIT, all declarations "
                         "agree.\n" + supp + "\n" + count)
        rep.findings.append(m.Finding("mismatch", "high", "msg", "a.txt", 3))
        lines = m.render_human(rep).splitlines()
        self.assertEqual(lines[0], "✗ licenscan: 1 finding(s) — repo licence MIT. "
                                   "Publish blocked.")
        self.assertIn(supp, lines)
        self.assertIn(count, lines)

    def test_reviewscan(self):
        import reviewscan as m
        with tempfile.TemporaryDirectory() as td:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = m.run([Path(td)], Path(td), False)
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue(),
                         f"✓ reviewscan clean — 0 post-{m.BOUNDARY} decision record(s) "
                         "carry a review line; 0 review brief(s) keep deferred "
                         "material out of the brief.\n"
                         "  suppressed: 0 record(s) by allow-marker\n")


class TestFindingIdHelpers(unittest.TestCase):
    """`115/080`: the namespaced finding ID, its line form and its JSON field."""

    def test_finding_id(self):
        self.assertEqual(report.finding_id("demoscan", "some-kind"), "demoscan:some-kind")

    def test_with_id_appends_and_leaves_the_line_alone(self):
        self.assertEqual(report.with_id("  a.md:1  [k] x → y", "demoscan", "k"),
                         "  a.md:1  [k] x → y  [demoscan:k]")

    def test_finding_dicts_adds_id_last(self):
        from dataclasses import dataclass

        @dataclass
        class F:
            path: str
            kind: str
        got = report.finding_dicts("demoscan", [F("a.md", "k")], lambda f: f.kind)
        self.assertEqual(got, [{"path": "a.md", "kind": "k", "id": "demoscan:k"}])
        self.assertEqual(list(got[0]), ["path", "kind", "id"])


class TestFindingLinePins(unittest.TestCase):
    """One finding line per scanner that prints an ID, as a literal: the line
    as it was before `115/080` plus `  [<scanner>:<kind>]`."""

    def line(self, out, prefix):
        return next(ln for ln in out.splitlines() if ln.startswith(prefix))

    def test_secretscan(self):
        import secretscan as m
        f = m.Finding("a.txt", 3, "aws-access-key-id", "named", "high", "AKIA… (20 chars)")
        self.assertEqual(self.line(m.render_human([f]), "  a.txt"),
                         "  a.txt:3  [high/named] aws-access-key-id → AKIA… (20 chars)"
                         "  [secretscan:aws-access-key-id]")
        f = m.Finding("b.txt", 4, m.LOW_VARIETY_RULE, "entropy", "medium", "abc…", "advisory")
        self.assertEqual(self.line(m.render_human([f]), "     b.txt"),
                         "     b.txt:4  [advisory/entropy] low-variety-entropy → abc…"
                         "  [secretscan:low-variety-entropy]")

    def test_leakscan(self):
        import leakscan as m
        out = m.render_human([m.Finding("a.txt", 1, "email", "structural", "high", "a.b…nz"),
                              m.Finding("n.txt", 0, "local-term", "local", "high", "term:ab…")],
                             None, True)
        self.assertEqual(self.line(out, "  a.txt"),
                         "  a.txt:1  [high/structural] email → a.b…nz  [leakscan:email]")
        self.assertEqual(self.line(out, "  n.txt"),
                         "  n.txt (in the path name)  [high/local] local-term → term:ab…"
                         "  [leakscan:local-term]")

    def test_linkscan(self):
        import linkscan as m
        out = m.render_human([m.Finding("a.md", 1, "missing-file", "x.md", "gone")])
        self.assertEqual(self.line(out, "  a.md"),
                         "  a.md:1  [missing-file] x.md → gone  [linkscan:missing-file]")

    def test_datescan(self):
        import datescan as m
        out = m.render_human([m.Finding("a.md", 1, "relative-time-word", "today", "d")])
        self.assertEqual(self.line(out, "  a.md"),
                         "  a.md:1  [relative-time-word] 'today' → d"
                         "  [datescan:relative-time-word]")

    def test_spellscan_names_the_word(self):
        import spellscan as m
        out = m.render_human([m.Finding("a.md", 1, "us-spelling", "Color", "Colour", "d")])
        self.assertEqual(self.line(out, "  a.md"),
                         "  a.md:1  [us-spelling] 'Color' → 'Colour'  [spellscan:color]")

    def test_pathscan(self):
        import pathscan as m
        out = m.render_human([m.Finding("a.md", 2, "missing-path", "x/y.py", "gone")])
        self.assertEqual(self.line(out, "  a.md"),
                         "  a.md:2  [missing-path] x/y.py → gone  [pathscan:missing-path]")

    def test_licenscan(self):
        import licenscan as m
        rep = m.Report(repo_license="MIT")
        rep.findings.append(m.Finding("mismatch", "high", "msg", "a.txt", 3))
        rep.findings.append(m.Finding("no-license", "high", "none"))
        out = m.render_human(rep)
        self.assertEqual(self.line(out, "  a.txt"),
                         "  a.txt:3  [high/mismatch] msg  [licenscan:mismatch]")
        self.assertEqual(self.line(out, "  [high/no"),
                         "  [high/no-license] none  [licenscan:no-license]")

    def test_sizescan_per_kind_lines(self):
        import sizescan as m
        out = m.render_human([m.Finding("ROADMAP.md", 320, 2, "", True),
                              m.Finding("ROADMAP-DONE.md", 9, 0, "", True, 1)])
        self.assertIn("      → 2 completed [x] item(s) to harvest [cold-content, gated]"
                      "  [sizescan:cold-content]", out.splitlines())
        self.assertIn("      → 1 live state marker(s) ([ ]/[~]/⏳ list items) in an "
                      "archive store [harvest-integrity, gated]"
                      "  [sizescan:harvest-integrity]", out.splitlines())
        self.assertNotIn("size-advisory", out)

    def test_pointerscan(self):
        import pointerscan as m
        with tempfile.TemporaryDirectory() as td:
            board = Path(td) / "docs" / "roadmap"
            board.mkdir(parents=True)
            (board / "a.md").write_text(m._SPEC_LANDED)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                m.main(["--root", td, "docs"])
        self.assertIn("  docs/roadmap/a.md:1  [state] ", buf.getvalue())
        self.assertIn("  [pointerscan:state]\n", buf.getvalue())


class TestFindingIdRoundTrip(unittest.TestCase):
    """The ID's kind is exactly the scope that scanner's marker accepts: run
    each scanner for real, read each finding's `id` from `--json`, put that
    kind in a marker, run again, and the finding — only it — is gone."""

    TOOLS = Path(__file__).resolve().parent
    KEY = "AKIA" + "IOSFODNN7EXAMPLE"      # built from parts: this file is scanned
    MAIL = "a.b" + "@" + "example.co.nz"

    def run_json(self, name, args, env=None):
        import json
        import os
        import subprocess
        p = subprocess.run([sys.executable, str(self.TOOLS / f"{name}.py"), *args,
                            "--json"], capture_output=True, text=True,
                           env=dict(os.environ, **(env or {})))
        self.assertIn(p.returncode, (0, 1), p.stderr)
        found = json.loads(p.stdout)["findings"]
        return sorted(i for f in found for i in (f.get("ids") or [f["id"]]))

    def round_trip(self, name, files, marked, args, env=None, unexemptable=()):
        """`files` maps rel path -> body; `marked(kind)` gives the same map
        with a marker scoped to `kind`. A kind in `unexemptable` is one that
        NO marker may exempt (sizescan's `cold-content`, 115/270 a): its ID
        must survive the marker, and the other IDs be unaffected."""
        with tempfile.TemporaryDirectory() as td:
            def write(m):
                for rel, body in m.items():
                    p = Path(td, rel)
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(body)
            write(files)
            ids = self.run_json(name, args(td), env)
            self.assertTrue(ids, f"{name}: the fixture must produce a finding")
            for fid in sorted(set(ids)):
                scanner, kind = fid.split(":", 1)
                self.assertEqual(scanner, name)
                write(marked(kind))
                after = self.run_json(name, args(td), env)
                if kind in unexemptable:
                    self.assertEqual(after, ids, f"{name}: {kind!r} must stand")
                    write(files)
                    continue
                self.assertNotIn(fid, after, f"{name}: a marker scoped to {kind!r}")
                self.assertEqual(after, [i for i in ids if i != fid])
                write(files)

    def test_secretscan(self):
        self.round_trip(
            "secretscan", {"a.txt": f"key {self.KEY}\n"},
            lambda k: {"a.txt": f"key {self.KEY}  # secretscan" f":allow:{k}: fixture\n"},
            lambda r: ["--root", r, r])

    def test_leakscan(self):
        with tempfile.TemporaryDirectory() as t:
            terms = Path(t) / "terms.txt"
            terms.write_text("")
            self.round_trip(
                "leakscan", {"a.txt": f"reach {self.MAIL} now\n"},
                lambda k: {"a.txt": f"reach {self.MAIL} now  # leakscan" f":allow:{k}: fixture\n"},
                lambda r: ["--root", r, r], {"ATELIER_LEAKSCAN_TERMS": str(terms)})

    def test_markdown_scanners(self):
        for name, body in (("linkscan", "See [x](missing.md)."),
                           ("datescan", "Done yesterday."),
                           ("spellscan", "The color is red."),
                           ("pathscan", "See `tools/ghost.py` here.")):
            with self.subTest(scanner=name):
                self.round_trip(
                    name, {"tools/real.py": "x\n", "a.md": body + "\n"},
                    lambda k, n=name, b=body: {
                        "a.md": f"{b}  <!-- {n}" f":allow:{k}: fixture -->\n"},
                    lambda r: ["--root", r, r])

    def test_licenscan(self):
        lic = "Apache License\nVersion 2.0, January 2004\n"
        self.round_trip(
            "licenscan", {"LICENSE": lic, "pyproject.toml": 'license = "MIT"\n'},
            lambda k: {"pyproject.toml": f'license = "MIT"  # licenscan' f':allow:{k}: x\n'},
            lambda r: [r])

    def test_sizescan(self):
        # two kinds: a completed item on the roadmap (no marker may exempt it)
        # and a live item in an archive store (the one thing a marker can)
        road = "- [x] done\n- [ ] open\n"
        done = "- [x] harvested\n- [ ] buried\n"
        self.round_trip(
            "sizescan", {"ROADMAP.md": "# R\n" + road, "ROADMAP-DONE.md": "# D\n" + done},
            lambda k: {"ROADMAP.md": f"<!-- sizescan" f":allow:{k}: fixture -->\n" + road,
                       "ROADMAP-DONE.md": f"<!-- sizescan" f":allow:{k}: fixture -->\n" + done},
            lambda r: ["--check", "--root", r, r], unexemptable=("cold-content",))

    def test_pointerscan(self):
        import pointerscan as m
        head, _, rest = m._SPEC_LIVE.partition("\n")
        self.round_trip(
            "pointerscan", {"docs/roadmap/a.md": m._SPEC_LIVE},
            lambda k: {"docs/roadmap/a.md": f"{head}  pointerscan" f":allow:{k}: x\n{rest}"},
            lambda r: ["--root", r, "docs"])


class TestGitPathReading(unittest.TestCase):
    """115/260 — the helpers that read git's path output. Literal strings, as
    git writes them (each spelling was captured from real git)."""

    def test_unquote_c_escapes(self):
        for quoted, plain in [
            (r"a\tb", "a\tb"), (r"a\nb", "a\nb"), (r"a\"b", 'a"b'),
            (r"a\\b", "a\\b"), (r"\a\b\f\r\v", "\a\b\f\r\v"),
            ("plain", "plain"), ("", ""),
        ]:
            with self.subTest(quoted=quoted):
                self.assertEqual(plain, report.unquote_c(quoted))

    def test_unquote_c_octal_is_utf8_bytes(self):
        # core.quotePath=true spells a non-ASCII byte as three octal digits.
        self.assertEqual("café/x", report.unquote_c(r"caf\303\251/x"))
        self.assertEqual("中文", report.unquote_c(r"\344\270\255\346\226\207"))
        # Raw and escaped spellings mix, and agree.
        self.assertEqual("café\t", report.unquote_c("café\\t"))

    def test_unquote_c_never_raises_on_odd_input(self):
        self.assertEqual("�", report.unquote_c(r"\377"))   # not UTF-8
        self.assertEqual("a\\", report.unquote_c("a\\"))        # lone backslash
        self.assertEqual("\\q", report.unquote_c(r"\q"))        # unknown escape
        self.assertEqual("\\400", report.unquote_c(r"\400"))    # not a byte

    def test_diff_header_path_plain(self):
        self.assertEqual("a/b.txt", report.diff_header_path("+++ b/a/b.txt"))
        self.assertEqual("café/a.txt",
                         report.diff_header_path("+++ b/café/a.txt"))

    def test_diff_header_path_strips_the_space_marker_tab(self):
        self.assertEqual("sp ace.txt",
                         report.diff_header_path("+++ b/sp ace.txt\t"))
        self.assertEqual('say "hi".md',
                         report.diff_header_path('+++ "b/say \\"hi\\".md"\t'))

    def test_diff_header_path_quoted(self):
        for header, path in [
            ('+++ "b/say \\"hi\\".md"', 'say "hi".md'),
            ('+++ "b/tab\\tname.md"', "tab\tname.md"),
            ('+++ "b/back\\\\slash.md"', "back\\slash.md"),
            ('+++ "b/nl\\nx.md"', "nl\nx.md"),
            ('+++ "b/caf\\303\\251/a.txt"', "café/a.txt"),
        ]:
            with self.subTest(header=header):
                self.assertEqual(path, report.diff_header_path(header))

    def test_diff_header_path_ignores_everything_else(self):
        for line in ["+++ /dev/null", "+++ a/x", "+++ x", "++ b/x",
                     "+++b/x", "--- b/x", "+text", " +++ b/x", "", '+++ "b/',
                     '+++ "b/x']:
            with self.subTest(line=line):
                self.assertIsNone(report.diff_header_path(line))

    def test_nul_paths(self):
        raw = b"a.md\0caf\xc3\xa9/b.md\0say \"hi\".md\0tab\tname.md\0"
        self.assertEqual(
            ["a.md", "café/b.md", 'say "hi".md', "tab\tname.md"],
            report.nul_paths(raw))
        self.assertEqual([], report.nul_paths(b""))
        self.assertEqual(["x"], report.nul_paths(b"x"))      # no trailing NUL

    def test_nul_paths_keep_undecodable_names_round_trippable(self):
        (name,) = report.nul_paths(b"bad\xff.md\0")
        self.assertEqual(b"bad\xff.md", os.fsencode(name))


class ParseAddedLinesTest(unittest.TestCase):
    """115/280 — the one reader of the staged diff. An ADDED line whose text
    begins `++ ` prints as `+++ …`, which three guards took for a file header.
    The reader follows the diff's structure (the hunk counts), so a header is
    only ever what git wrote between `diff --git` and a file's first `@@`.
    Fixtures are REAL `git diff` output from a scratch repo, not hand-typed."""

    GIT_ENV = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid",  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
               "GIT_COMMITTER_NAME": "t",
               "GIT_COMMITTER_EMAIL": "t@example.invalid"}  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(__import__("shutil").rmtree, self.repo,
                        ignore_errors=True)
        self.git("init", "-q")
        old = os.getcwd()
        os.chdir(self.repo)
        self.addCleanup(os.chdir, old)

    def git(self, *args):
        import subprocess
        return subprocess.run(["git", "-C", str(self.repo), "-c", "commit.gpgsign=false", *args], check=True,
                              capture_output=True,
                              env={**os.environ, **self.GIT_ENV}).stdout

    def put(self, name, data):
        p = self.repo / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data if isinstance(data, bytes) else data.encode())

    def commit_base(self):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")

    def staged(self):
        return list(report.staged_added())

    def raw_diff(self):
        """The staged diff exactly as the guards read it, but WITHOUT the
        added/copied/modified/renamed filter, so deletions are in it too."""
        cmd = [a for a in report.STAGED_DIFF_CMD[1:]
               if not a.startswith("--diff-filter")]
        return self.git(*cmd)

    def test_multi_file_rename_quoted_new_deleted_binary_and_mode(self):
        base = "".join(f"keep {i}\n" for i in range(1, 30))
        self.put("a.md", "".join(f"line {i}\n" for i in range(1, 41)))
        self.put("rename_me.txt", base)
        self.put("café/n.md", "one\ntwo\nthree\n")
        self.put("gone.txt", "bye\n")
        self.put("tab\tname.md", "x\n")
        self.put("sp ace/f.md", "y\n")
        self.put("mode.sh", "echo hi\n")
        self.commit_base()
        lines = [f"line {i}\n" for i in range(1, 41)]
        lines[2] = "changed 3\n"
        lines.insert(30, "inserted\n")
        self.put("a.md", "".join(lines))
        self.put("new.py", "print(1)\nprint(2)\n")
        self.git("mv", "rename_me.txt", "renamed.txt")
        self.put("renamed.txt", base + "tail\n")
        self.put("café/n.md", "one\nTWO\nthree\nfour\n")
        self.put("tab\tname.md", "x\nsecond\n")
        self.put("sp ace/f.md", "y\nz\n")
        (self.repo / "gone.txt").unlink()
        self.put("blob.bin", b"\x00\x01\xff" * 20)
        os.chmod(self.repo / "mode.sh", 0o755)
        self.git("add", "-A")
        self.assertEqual([
            ("a.md", 3, "changed 3"),
            ("a.md", 31, "inserted"),
            ("café/n.md", 2, "TWO"),
            ("café/n.md", 4, "four"),
            ("new.py", 1, "print(1)"),
            ("new.py", 2, "print(2)"),
            ("renamed.txt", 30, "tail"),
            ("sp ace/f.md", 2, "z"),
            ("tab\tname.md", 2, "second"),
        ], sorted(self.staged()))
        # With deletions left IN the diff (`+++ /dev/null`, a hunk of only
        # removed lines) the reader still reads every file the same.
        self.assertIn(b"+++ /dev/null", self.raw_diff())
        self.assertEqual(sorted(self.staged()),
                         sorted(report.parse_added_lines(self.raw_diff())))

    def test_a_posed_header_inside_a_hunk_moves_nothing(self):
        self.put("x.md", "base\n")
        self.commit_base()
        self.put("x.md", "base\n++ b/docs/ignored.md\nreal\n+++ b/other.md\n")
        self.put("y.md", "++ b/x.md\nafter\n")
        self.git("add", "-A")
        self.assertEqual([
            ("x.md", 2, "++ b/docs/ignored.md"),
            ("x.md", 3, "real"),
            ("x.md", 4, "+++ b/other.md"),
            ("y.md", 1, "++ b/x.md"),
            ("y.md", 2, "after"),
        ], sorted(self.staged()))

    def test_a_posed_quoted_header_and_dev_null_move_nothing(self):
        self.put("x.md", '++ "b/docs/ignored.md"\n++ /dev/null\nreal\n')
        self.git("add", "-A")
        self.assertEqual([
            ("x.md", 1, '++ "b/docs/ignored.md"'),
            ("x.md", 2, "++ /dev/null"),
            ("x.md", 3, "real"),
        ], self.staged())

    def test_a_posed_diff_and_hunk_header_in_added_text_move_nothing(self):
        self.put("x.md", "diff --git a/z b/z\n@@ -1 +1 @@\n+++ b/z\nreal\n")
        self.git("add", "-A")
        self.assertEqual(["diff --git a/z b/z", "@@ -1 +1 @@", "+++ b/z",
                          "real"], [t for _, _, t in self.staged()])
        self.assertEqual({"x.md"}, {p for p, _, _ in self.staged()})

    def test_line_separators_inside_a_line_do_not_split_it(self):
        # `str.splitlines` breaks on these; an added line's own text must
        # never start a line of the diff.
        for sep in ("\x0c", "\x0b", "\x1c", "\x85", " ", "\r"):
            with self.subTest(sep=repr(sep)):
                self.put("x.md", f"a{sep}+++ b/docs/ignored.md\nreal\n")
                self.git("add", "-A")
                self.assertEqual(
                    [("x.md", 1, f"a{sep}+++ b/docs/ignored.md"),
                     ("x.md", 2, "real")], self.staged())

    def test_crlf_files_lose_only_the_line_ending(self):
        self.put("x.md", "one\r\ntwo\r\n")
        self.git("add", "-A")
        self.assertEqual([("x.md", 1, "one"), ("x.md", 2, "two")],
                         self.staged())

    def test_no_newline_marker_and_one_line_counts(self):
        self.put("x.md", "a\nb\nc")
        self.commit_base()
        self.put("x.md", "a\nB\nc2")
        self.git("add", "-A")
        self.assertIn(b"\\ No newline at end of file", self.raw_diff())
        self.assertEqual([("x.md", 2, "B"), ("x.md", 3, "c2")], self.staged())

    def test_configured_prefixes_do_not_change_what_is_read(self):
        self.put("x.md", "base\n")
        self.commit_base()
        self.put("x.md", "base\nnew\n")
        self.git("add", "-A")
        for setting in ("diff.noprefix=true", "diff.mnemonicPrefix=true"):
            with self.subTest(setting=setting):
                self.git("config", *setting.split("="))
                self.assertEqual([("x.md", 2, "new")], self.staged())

    def test_nothing_staged_is_empty(self):
        self.assertEqual([], self.staged())

    def test_a_diff_that_is_not_git_shaped_is_refused_not_guessed(self):
        for name, raw in [
            ("hunk before any file", b"@@ -0,0 +1 @@\n+x\n"),
            ("hunk without counts", b"diff --git a/x b/x\n+++ b/x\n@@ nope\n"),
            ("body line of no kind",
             b"diff --git a/x b/x\n+++ b/x\n@@ -0,0 +1 @@\nzzz\n"),
            ("hunk longer than its counts",
             b"diff --git a/x b/x\n+++ b/x\n@@ -0,0 +1 @@\n+a\n+b\n+++ b/y\n"),
            ("ends inside a hunk",
             b"diff --git a/x b/x\n+++ b/x\n@@ -0,0 +1,2 @@\n+a\n"),
            ("header not b/ or /dev/null",
             b"diff --git a/x b/x\n+++ w/x\n@@ -0,0 +1 @@\n+a\n"),
        ]:
            with self.subTest(name=name):
                with self.assertRaises(report.DiffReadError):
                    list(report.parse_added_lines(raw))

    def test_a_hunk_longer_than_its_counts_is_the_posed_header_case(self):
        # The same diff, count-correct: the `+++ b/y` is body, not a header.
        raw = (b"diff --git a/x b/x\n+++ b/x\n@@ -0,0 +1,2 @@\n+a\n+++ b/y\n")
        self.assertEqual([("x", 1, "a"), ("x", 2, "++ b/y")],
                         list(report.parse_added_lines(raw)))


if __name__ == "__main__":
    unittest.main()
