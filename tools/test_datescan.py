"""Stdlib-only tests for datescan (no pytest needed): `python3 -m unittest`."""

import unittest

import datescan as ds


def scan(text):
    return ds.scan_text("t", text)


def kinds(text):
    return [f.kind for f in scan(text)]


class RelativeTimeWords(unittest.TestCase):
    def test_today_flagged(self):
        self.assertIn("relative-time-word", kinds("we shipped today"))

    def test_yesterday_flagged(self):
        self.assertIn("relative-time-word", kinds("filed yesterday"))

    def test_multiword_phrase_flagged(self):
        self.assertIn("relative-time-word", kinds("closed last week"))
        self.assertIn("relative-time-word", kinds("due next month"))
        self.assertIn("relative-time-word", kinds("started this year"))

    def test_case_insensitive(self):
        self.assertIn("relative-time-word", kinds("Today was the day"))
        self.assertIn("relative-time-word", kinds("TOMORROW we ship"))

    def test_word_boundary_no_partial_match(self):
        # "today" must not match inside a longer word.
        self.assertNotIn("relative-time-word", kinds("the todayapp shipped"))

    def test_iso_date_alone_is_clean(self):
        self.assertEqual([], scan("stamped 2026-07-23, no relative words"))


class QuotedMentionExemption(unittest.TestCase):
    def test_double_quoted_mention_exempt(self):
        # The S3 rule's own worked-example shape.
        self.assertEqual(
            [], scan('no relative-time words ("today", "yesterday", "last week")'))

    def test_single_quoted_mention_exempt(self):
        self.assertEqual([], scan("the word 'tomorrow' is banned here"))

    def test_curly_quoted_mention_exempt(self):
        self.assertEqual([], scan("the word “today” is banned here"))

    def test_unquoted_use_still_flagged(self):
        self.assertIn("relative-time-word", kinds("we will ship tomorrow"))

    def test_mismatched_quotes_not_exempt(self):
        # Opening quote with no matching close — not a clean mention, still a use.
        self.assertIn("relative-time-word", kinds('the plan today" is set'))


class CodeAndQuoteExemptions(unittest.TestCase):
    def test_inline_code_span_exempt(self):
        self.assertEqual([], scan("`tomorrow` is just an example in code"))

    def test_fenced_block_exempt(self):
        text = "prose\n```\nshipped tomorrow in this fenced block\n```\nmore prose\n"
        self.assertEqual([], scan(text))

    def test_blockquote_exempt(self):
        self.assertEqual([], scan("> this happened yesterday, quoted verbatim"))

    def test_blockquote_with_leading_space_exempt(self):
        self.assertEqual([], scan("   > indented quote says today"))


class AllowMarker(unittest.TestCase):
    def test_inline_allow_marker_exempts_line(self):
        self.assertEqual(
            [], scan("shipped today  <!-- datescan:allow: selftest fixture -->"))


class NonIsoDates(unittest.TestCase):
    def test_slash_date_flagged(self):
        fs = scan("filed on 23/07/2026 by hand")
        self.assertEqual(["non-iso-date"], [f.kind for f in fs])
        self.assertEqual("23/07/2026", fs[0].match)

    def test_month_day_year_flagged(self):
        self.assertIn("non-iso-date", kinds("filed on July 23, 2026 by hand"))

    def test_day_month_year_flagged(self):
        self.assertIn("non-iso-date", kinds("filed on 23 July 2026 by hand"))

    def test_abbreviated_month_flagged(self):
        self.assertIn("non-iso-date", kinds("filed on Jul 23, 2026 by hand"))

    def test_ordinal_day_month_year_flagged(self):
        self.assertIn("non-iso-date", kinds("closed the 23rd of July 2026"))

    def test_fraction_is_not_a_date(self):
        # A single slash (a fraction, a ratio) must not false-positive as a
        # slash-date — the pattern requires two slashes.
        self.assertEqual([], scan("reduced scope by 3/4 of the work"))

    def test_iso_date_is_not_flagged_as_non_iso(self):
        self.assertEqual([], scan("stamped 2026-07-23 correctly"))


class InvalidIsoDates(unittest.TestCase):
    def test_bad_month_flagged(self):
        fs = scan("bogus date 2026-13-01 here")
        self.assertEqual(["invalid-iso-date"], [f.kind for f in fs])

    def test_bad_day_flagged(self):
        self.assertIn("invalid-iso-date", kinds("bogus date 2026-02-40 here"))

    def test_valid_date_clean(self):
        self.assertEqual([], scan("stamped 2026-07-23 correctly"))

    def test_leap_day_valid(self):
        self.assertEqual([], scan("stamped 2024-02-29 correctly"))

    def test_non_leap_feb29_invalid(self):
        self.assertIn("invalid-iso-date", kinds("stamped 2026-02-29 wrongly"))

    def test_placeholder_template_text_not_flagged(self):
        # A literal YYYY-MM-DD placeholder has no digits to capture.
        self.assertEqual([], scan("use the YYYY-MM-DD format"))


class Ignore(unittest.TestCase):
    def test_exact_glob(self):
        self.assertTrue(ds._ignored("docs/fixture.md", ["docs/fixture.md"]))

    def test_subtree_glob(self):
        self.assertTrue(ds._ignored("docs/sessions/x.md", ["docs/sessions/"]))
        self.assertTrue(ds._ignored("docs/sessions/x.md", ["docs/sessions"]))

    def test_non_match(self):
        self.assertFalse(ds._ignored("docs/real.md", ["docs/fixture.md"]))


class WholeTree(unittest.TestCase):
    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ds.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _main(self, argv):
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            return ds.main(argv)

    def test_defaults_to_docs_subdir(self):
        # No paths given: default scope is <root>/docs, not the whole tree —
        # a relative-time word outside docs/ must not be flagged.
        self._write("README.md", "shipped today outside docs\n")
        self._write("docs/note.md", "shipped today inside docs\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))
        findings = ds.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/note.md", findings[0].path)

    def test_falls_back_to_root_when_no_docs_dir(self):
        self._write("note.md", "shipped today, no docs dir here\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))

    def test_nonexistent_path_is_an_error_not_a_pass(self):
        self.assertEqual(
            2, self._main(["--root", str(self.tmp), str(self.tmp / "gone")]))

    def test_warn_always_exits_zero(self):
        self._write("docs/note.md", "shipped today\n")
        self.assertEqual(
            0, self._main(["--warn", "--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_without_warn_findings_exit_one(self):
        self._write("docs/note.md", "shipped today\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_clean_tree_exits_zero(self):
        self._write("docs/note.md", "stamped 2026-07-23, all absolute\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_datescanignore_exempts_path(self):
        self._write("docs/note.md", "shipped today\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))
        self._write(".datescanignore", "docs/note.md\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_non_markdown_files_skipped(self):
        self._write("docs/note.txt", "shipped today, not markdown\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ds._selftest())


if __name__ == "__main__":
    unittest.main()
