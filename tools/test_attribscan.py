"""Stdlib-only tests for attribscan (no pytest needed): `python3 -m unittest`.

Board `320/100`, the second slice of `320/810`. Detector cases over text; the
planes over a real throwaway repo, because `--staged` and `--against` read git.
The date is patched in process (a subprocess cannot see the patch)."""

import contextlib
import datetime
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path

import attribscan as a


def _hits(text: str) -> list:
    return a.scan_text(text, "x.md")


class DetectorTest(unittest.TestCase):
    def test_the_words_the_item_names_all_fire(self):
        for text in (
            "The port-forward, ruled 2026-08-23: to the proxy only.\n",
            "This is the owner's ruling on the matter.\n",
            "See his instruction above.\n",
            "- [x] ruled by him\n",
            "He directed the change.\n",
            "The principal's directive stands.\n",
            "See Ngaio's ruling on that.\n",
        ):
            with self.subTest(text=text):
                self.assertEqual(len(_hits(text)), 1, text)

    def test_other_senses_of_the_word_do_not_fire(self):
        for text in (
            "We ruled that out early.\n",
            "It was ruled out.\n",
            "ruled-out options\n",
            "That decision was overruled later.\n",
            "A ruling in general is a kind of record.\n",
            "The agent's instruction set.\n",
            "Claude's instruction was unclear.\n",
        ):
            with self.subTest(text=text):
                self.assertEqual(_hits(text), [], text)

    def test_a_quotation_nearby_clears_it(self):
        for text in (
            'He ruled, in his words: "Build the check".\n',
            'Ruled 2026-09-19: “Build the check.”\n',
            'RULED (via the device): *"Build the check"*.\n',
            'Ruled 2026-09-19,\nin his words:\n"Build the check".\n',
        ):
            with self.subTest(text=text):
                self.assertEqual(_hits(text), [], text)

    def test_a_blockquote_nearby_clears_it(self):
        self.assertEqual(_hits("His ruling, 2026-09-19:\n> Build the check\n"), [])

    def test_a_citation_clears_it(self):
        for text in (
            "Ruled: see ADR 0005.\n",
            "Ruled, see docs/decisions/0005-going-public.md.\n",
            "Ruled at the close, see docs/sessions/2026-10-03-log.md.\n",
            "Ruled in the transcript of that sitting.\n",
            "Ruled in session 722ac2e2 at the close.\n",
        ):
            with self.subTest(text=text):
                self.assertEqual(_hits(text), [], text)

    def test_a_demotion_clears_it(self):
        for text in (
            "Ruled by nobody: this is an agent's decision.\n",
            "Ruled 2026-11-10, the run's choice, not his.\n",
            "Ruled here is the worker's own reading.\n",
        ):
            with self.subTest(text=text):
                self.assertEqual(_hits(text), [], text)

    def test_inline_code_and_fences_are_not_attributions(self):
        for text in ("Phrase `ruled 2026-08-23` is the example.\n",
                     "```\nruled 2026-08-23\n```\n",
                     "~~~~\nruled 2026-08-23\n~~~~\n"):
            with self.subTest(text=text):
                self.assertEqual(_hits(text), [], text)

    def test_a_blockquote_line_is_not_an_attribution(self):
        self.assertEqual(_hits("> ruled 2026-08-23\n"), [])

    def test_a_quote_in_code_is_not_evidence(self):
        self.assertEqual(len(_hits('Ruled here, see `"Build"`.\n')), 1)

    def test_the_block_stops_at_a_blank_line(self):
        self.assertEqual(len(_hits('Ruled 2026-08-23.\n\n"Build the check".\n')), 1)

    def test_the_block_stops_at_another_list_item(self):
        self.assertEqual(len(_hits('- Ruled 2026-08-23.\n- "Build the check"\n')), 1)
        self.assertEqual(len(_hits('- "Build the check"\n- Ruled 2026-08-23.\n')), 1)

    def test_the_block_reaches_up_to_the_item_that_opens_it(self):
        self.assertEqual(_hits('- "Build the check" he said\n  and that was\n  ruled here.\n'), [])

    def test_the_block_stops_at_a_heading(self):
        self.assertEqual(len(_hits('## "Build the check"\nRuled 2026-08-23.\n')), 1)

    def test_the_window_is_capped(self):
        text = "Ruled 2026-08-23.\nA\nB\nC\nD\n" + '"Build the check"\n'
        self.assertEqual(len(_hits(text)), 1)

    def test_the_allow_marker(self):
        self.assertEqual(_hits("Ruled 2026-08-23. <!-- attribscan:allow: a worked example -->\n"), [])
        self.assertEqual(len(_hits("Ruled 2026-08-23. <!-- attribscan:allow -->\n")), 1)

    def test_a_finding_names_its_line(self):
        f = _hits("Line.\n\nRuled 2026-08-23.\n")[0]
        self.assertEqual(f.line, 3)
        self.assertEqual(f.path, "x.md")
        self.assertEqual(f.word.lower(), "ruled")


class DateTest(unittest.TestCase):
    def test_the_date_is_read_strictly_before(self):
        d = a.ATTRIBUTION_WARN_UNTIL
        self.assertTrue(a.warn_only_today(d - datetime.timedelta(days=1)))
        self.assertFalse(a.warn_only_today(d))
        self.assertFalse(a.warn_only_today(d + datetime.timedelta(days=1)))


class RepoFixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="attribscan-test-")
        self.root = Path(self._tmp.name).resolve()
        (self.root / "docs").mkdir()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "test@example.com")  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
        self.git("config", "user.name", "Test")
        self.old_cwd = os.getcwd()
        os.chdir(self.root)

    def tearDown(self):
        os.chdir(self.old_cwd)
        self._tmp.cleanup()

    def git(self, *args):
        subprocess.run(["git", "-C", str(self.root), *args], check=True,
                       capture_output=True, text=True)

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def commit_all(self, msg="c"):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", msg)

    def run_main(self, *argv, on=None):
        when = on if on is not None else a.ATTRIBUTION_WARN_UNTIL - datetime.timedelta(days=30)
        out = io.StringIO()
        with unittest.mock.patch.object(a, "_utc_today", return_value=when), \
                contextlib.redirect_stdout(out):
            code = a.main(list(argv))
        return code, out.getvalue()


class StagedPlaneTest(RepoFixture):
    def test_only_added_lines_are_read(self):
        self.write("docs/a.md", "Old line, ruled 2026-01-01.\n\nNext.\n")
        self.commit_all()
        self.write("docs/a.md", "Old line, ruled 2026-01-01.\n\nNext.\n\nNew, ruled 2026-11-10.\n")
        self.git("add", "docs/a.md")
        code, out = self.run_main("--staged", "--root", str(self.root), "docs")
        self.assertEqual(code, 0, out)
        self.assertEqual(out.count("docs/a.md:"), 1, out)
        self.assertIn("docs/a.md:5", out)

    def test_an_added_line_with_a_quote_on_a_context_line_clears(self):
        self.write("docs/a.md", 'His words were "Build the check".\n')
        self.commit_all()
        self.write("docs/a.md", 'His words were "Build the check".\nRuled 2026-11-10.\n')
        self.git("add", "docs/a.md")
        code, out = self.run_main("--staged", "--root", str(self.root), "docs")
        self.assertEqual(code, 0)
        self.assertIn("clean", out)

    def test_outside_scope_is_not_read(self):
        self.write("docs/keep.md", "tracked\n")
        self.write("other/a.md", "start\n")
        self.commit_all()
        self.write("other/a.md", "start\nRuled 2026-11-10.\n")
        self.git("add", "other/a.md")
        code, out = self.run_main("--staged", "--root", str(self.root), "docs",
                                   on=a.ATTRIBUTION_WARN_UNTIL)
        self.assertEqual(code, 0, out)

    def test_it_warns_before_the_date_and_blocks_from_it(self):
        self.write("docs/a.md", "start\n")
        self.commit_all()
        self.write("docs/a.md", "start\n\nRuled 2026-11-10.\n")
        self.git("add", "docs/a.md")
        before = a.ATTRIBUTION_WARN_UNTIL - datetime.timedelta(days=1)
        code, out = self.run_main("--staged", "--root", str(self.root), "docs", on=before)
        self.assertEqual(code, 0, out)
        self.assertIn("blocking from", out)
        self.assertIn("attribscan advisory: 1 finding(s)", out)
        code, out = self.run_main("--staged", "--root", str(self.root), "docs",
                                  on=a.ATTRIBUTION_WARN_UNTIL)
        self.assertEqual(code, 1, out)
        self.assertIn("commit blocked", out)
        self.assertIn("attribscan advisory: 0 finding(s)", out)

    def test_warn_passes_on_the_date_and_counts_as_advisory(self):
        self.write("docs/a.md", "start\n")
        self.commit_all()
        self.write("docs/a.md", "start\n\nRuled 2026-11-10.\n")
        self.git("add", "docs/a.md")
        code, out = self.run_main("--warn", "--staged", "--root", str(self.root), "docs",
                                  on=a.ATTRIBUTION_WARN_UNTIL)
        self.assertEqual(code, 0, out)
        self.assertIn("attribscan advisory: 1 finding(s)", out)

    def test_a_generated_board_index_is_skipped(self):
        self.write("docs/roadmap/x.md", "item\n")
        self.write("docs/ROADMAP.md", "index\n")
        self.commit_all()
        self.write("docs/ROADMAP.md", "index\nRuled 2026-11-10.\n")
        self.git("add", "docs/ROADMAP.md")
        code, _ = self.run_main("--staged", "--root", str(self.root), "docs",
                                on=a.ATTRIBUTION_WARN_UNTIL)
        self.assertEqual(code, 0)

    def test_a_board_item_is_read(self):
        self.write("docs/roadmap/x.md", "item\n")
        self.commit_all()
        self.write("docs/roadmap/x.md", "item\n\nRuled 2026-11-10.\n")
        self.git("add", "docs/roadmap/x.md")
        code, _ = self.run_main("--staged", "--root", str(self.root), "docs",
                                on=a.ATTRIBUTION_WARN_UNTIL)
        self.assertEqual(code, 1)


class AgainstPlaneTest(RepoFixture):
    def test_reads_lines_added_since_the_revision_only(self):
        self.write("docs/a.md", "Old, ruled 2026-01-01.\n\nKept.\n")
        self.commit_all()
        self.write("docs/a.md", "Old, ruled 2026-01-01.\n\nKept.\n\nNew, ruled 2026-11-10.\n")
        self.commit_all()
        code, out = self.run_main("--against", "HEAD^", "--root", str(self.root),
                                  str(self.root / "docs"), on=a.ATTRIBUTION_WARN_UNTIL)
        self.assertEqual(code, 1, out)
        self.assertEqual(out.count("docs/a.md:"), 1, out)

    def test_a_first_commit_passes_and_says_so(self):
        self.write("docs/a.md", "Ruled 2026-01-01.\n")
        self.commit_all()
        code, out = self.run_main("--against", "HEAD^", "--root", str(self.root), "docs",
                                  on=a.ATTRIBUTION_WARN_UNTIL)
        self.assertEqual(code, 0, out)
        self.assertIn("first commit", out)

    def test_an_unresolvable_revision_is_a_broken_scan(self):
        self.write("docs/a.md", "start\n")
        self.commit_all()
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            code, _ = self.run_main("--against", "not-a-rev", "--root", str(self.root), "docs")
        self.assertEqual(code, 2)

    def test_a_non_markdown_file_is_not_read(self):
        self.write("docs/a.py", "x = 1\n")
        self.commit_all()
        self.write("docs/a.py", "x = 1\n# Ruled 2026-11-10.\n")
        self.commit_all()
        code, _ = self.run_main("--against", "HEAD^", "--root", str(self.root), "docs",
                                on=a.ATTRIBUTION_WARN_UNTIL)
        self.assertEqual(code, 0)


class TreePlaneTest(RepoFixture):
    def test_whole_tree_is_report_only_on_the_date(self):
        self.write("docs/a.md", "Ruled 2026-11-10.\n")
        self.write("docs/b.md", "Clean.\n")
        self.commit_all()
        code, out = self.run_main("--root", str(self.root), "docs",
                                  on=a.ATTRIBUTION_WARN_UNTIL)
        self.assertEqual(code, 0, out)
        self.assertIn("1 of 2 file(s)", out)

    def test_json_counts_the_share(self):
        self.write("docs/a.md", "Ruled 2026-11-10.\n")
        self.write("docs/b.md", "Clean.\n")
        self.commit_all()
        code, out = self.run_main("--json", "--root", str(self.root), "docs")
        self.assertEqual(code, 0)
        d = json.loads(out)
        self.assertEqual(d["files_with_findings"], 1)
        self.assertEqual(d["scanned_files"], 2)

    def test_an_excerpt_cannot_carry_a_control_character(self):
        self.write("docs/a.md", "Ruled here \x1b[31mred\x1b[0m.\n")
        self.commit_all()
        code, out = self.run_main("--root", str(self.root), "docs")
        self.assertEqual(code, 0)
        self.assertNotIn("\x1b", out)


class CoverageLineTest(RepoFixture):
    """115/130: a run says how many files it opened and lines it read, on the
    findings path as on the clean one, and a run over nothing says so."""

    def test_clean_and_findings_runs_both_print_the_counts(self):
        self.write("docs/a.md", "Clean.\nStill clean.\n")
        self.commit_all()
        code, out = self.run_main("--root", str(self.root), "docs")
        self.assertEqual(code, 0)
        self.assertIn("  coverage: 1 file(s) opened \u00b7 2 line(s) read", out)
        self.assertNotIn("scanned nothing", out)
        self.write("docs/b.md", "Ruled 2026-11-10.\n")
        self.commit_all()
        code, out = self.run_main("--root", str(self.root), "docs")
        self.assertEqual(code, 0)
        self.assertIn("unquoted attribution", out)
        self.assertIn("  coverage: 2 file(s) opened \u00b7 3 line(s) read", out)

    def test_a_run_over_nothing_says_so_and_exits_as_before(self):
        self.write("docs/a.txt", "not markdown\n")
        self.commit_all()
        code, out = self.run_main("--root", str(self.root), "docs")
        self.assertEqual(code, 0)
        self.assertIn("coverage: 0 file(s) opened \u00b7 0 line(s) read", out)
        self.assertIn("scanned nothing", out)

    def test_the_against_plane_counts_the_files_it_read(self):
        self.write("docs/a.md", "One.\n")
        self.commit_all("first")
        self.write("docs/a.md", "One.\nTwo.\n")
        self.commit_all("second")
        code, out = self.run_main("--root", str(self.root), "--against", "HEAD^")
        self.assertEqual(code, 0)
        self.assertIn("coverage: 1 file(s) opened \u00b7 2 line(s) read", out)

    def test_json_carries_the_same_coverage(self):
        self.write("docs/a.md", "Clean.\n")
        self.commit_all()
        code, out = self.run_main("--json", "--root", str(self.root), "docs")
        self.assertEqual({"files_opened": 1, "lines_read": 1,
                          "scanned_nothing": False},
                         json.loads(out)["coverage"])


class SelftestPin(unittest.TestCase):
    def test_selftest_passes(self):
        r = subprocess.run([sys.executable, a.__file__, "--selftest"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("selftest OK", r.stdout)


if __name__ == "__main__":
    unittest.main()
