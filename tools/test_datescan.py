"""Stdlib-only tests for datescan (no pytest needed): `python3 -m unittest`."""

import unittest

try:
    # `python3 -m unittest tools.test_datescan` from the repo root — tools/
    # is a namespace package (no __init__.py needed), so this is a proper
    # package-relative import (DSR7).
    from . import datescan as ds
except ImportError:
    # `cd tools && python3 -m unittest test_datescan` (or `discover -s
    # tools`, what CI uses) — no parent package in scope, so fall back to
    # the plain top-level import.
    import datescan as ds


def scan(text):
    return ds.scan_text("t", text)


def kinds(text):
    return [f.kind for f in scan(text)]


class RelativeTimeWords(unittest.TestCase):
    def test_yesterday_flagged(self):
        self.assertIn("relative-time-word", kinds("filed yesterday"))

    def test_multiword_phrase_flagged(self):
        self.assertIn("relative-time-word", kinds("closed last week"))
        self.assertIn("relative-time-word", kinds("due next month"))
        self.assertIn("relative-time-word", kinds("started this year"))

    def test_case_insensitive(self):
        self.assertIn("relative-time-word", kinds("Filed Yesterday, not today"))
        self.assertIn("relative-time-word", kinds("TOMORROW we ship"))

    def test_word_boundary_no_partial_match(self):
        # "today" must not match inside a longer word (still checked via the
        # separate TODAY_RX path, see TodayNarrowing below).
        self.assertNotIn("relative-time-word", kinds("the todayapp shipped"))

    def test_iso_date_alone_is_clean(self):
        self.assertEqual([], scan("stamped 2026-07-23, no relative words"))


class TodayNarrowing(unittest.TestCase):
    """DSR3: "today" is checked separately from the rest of the denylist,
    narrowed to date-adjacent contexts, because the reviewed corpus found it
    used overwhelmingly as a "currently" hedge rather than a calendar-date
    claim (51 of 57 relative-word hits in the ~60-finding baseline)."""

    def test_currently_sense_not_flagged(self):
        # The dominant corpus shape: a weak-anchor hedge, not a date claim.
        self.assertEqual(
            [], scan("this approach is still correct today"))
        self.assertEqual(
            [], scan("we shipped today"))
        self.assertEqual(
            [], scan("Today was the day the plan changed"))

    def test_date_cue_word_flags_today(self):
        # "stamped"/"dated"/"dating" nearby is the strongest cue that
        # "today" is standing in for a real calendar date.
        self.assertIn(
            "relative-time-word", kinds("stamped today, all fields correct"))
        self.assertIn(
            "relative-time-word", kinds("this record is dated today"))

    def test_as_of_cue_flags_today(self):
        self.assertIn(
            "relative-time-word", kinds("as of today the migration is done"))

    def test_iso_date_on_same_line_flags_today(self):
        # Pairing "today" with a real date on the same line is itself
        # evidence "today" is being used as one.
        self.assertIn(
            "relative-time-word", kinds("today, 2026-07-23, we shipped"))

    def test_todays_possessive_with_date_cue_flagged(self):
        self.assertIn(
            "relative-time-word", kinds("today's date is 2026-07-23"))

    def test_bare_today_far_from_cue_not_flagged(self):
        # Honest limit (DSR3): a genuine bare calendar-date claim with no
        # cue word and no ISO date on the same line now scans clean — a
        # deliberate, documented trade against the dominant noise source.
        self.assertEqual([], scan("filed today"))


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
        # Opening quote with no matching close — not a clean mention, still
        # a use. Uses "yesterday" (unaffected by the today-only DSR3
        # narrowing) so this test stays about the quote-span logic alone.
        self.assertIn("relative-time-word", kinds('the plan yesterday" is set'))

    def test_multiword_quoted_phrase_exempt(self):
        # DSR4: the original adjacency-only check only exempted a word
        # immediately flanked by quote chars, so a multi-word banned phrase
        # inside a longer quoted example — the doc's OWN banned-phrase list,
        # e.g. EVIDENCE.md's `"new this year"` — was wrongly caught. The
        # opening quote here sits before "new", not immediately before the
        # matched phrase "this year".
        self.assertEqual(
            [], scan('banned phrases include "new this year" in the list'))

    def test_multiword_quoted_phrase_single_quotes_exempt(self):
        self.assertEqual(
            [], scan("banned phrases include 'new this year' in the list"))

    def test_quoted_phrase_followed_by_unquoted_use_still_flagged(self):
        # The span check must not swallow a genuine use just because an
        # earlier, unrelated quoted mention appears on the same line.
        fs = scan('the doc bans "this year" but we still shipped this year')
        self.assertEqual(["relative-time-word"], [f.kind for f in fs])


class CodeAndQuoteExemptions(unittest.TestCase):
    def test_inline_code_span_exempt(self):
        self.assertEqual([], scan("`tomorrow` is just an example in code"))

    def test_fenced_block_exempt(self):
        text = "prose\n```\nshipped tomorrow in this fenced block\n```\nmore prose\n"
        self.assertEqual([], scan(text))

    def test_indented_code_block_exempt(self):
        # DSR6: only fenced code was exempt before this fix; a 4-space
        # CommonMark indented code block was not.
        text = "prose\n\n    shipped tomorrow in this indented block\n\nmore prose\n"
        self.assertEqual([], scan(text))

    def test_three_space_indent_not_exempt(self):
        # Below the 4-column CommonMark threshold — still ordinary prose.
        self.assertIn(
            "relative-time-word", kinds("   shipped tomorrow, only 3 spaces in"))

    def test_blockquote_exempt(self):
        self.assertEqual([], scan("> this happened yesterday, quoted verbatim"))

    def test_blockquote_with_leading_space_exempt(self):
        self.assertEqual([], scan("   > indented quote says yesterday"))


class AllowMarker(unittest.TestCase):
    def test_inline_allow_marker_exempts_line(self):
        self.assertEqual(
            [], scan("filed yesterday  <!-- datescan:allow: selftest fixture -->"))

    def test_empty_reason_not_exempt(self):
        # DSR8: a bare marker with no reason after it must not exempt.
        self.assertIn(
            "relative-time-word",
            kinds("filed yesterday  <!-- datescan:allow -->"))
        self.assertIn(
            "relative-time-word",
            kinds("filed yesterday  <!-- datescan:allow: -->"))

    def test_mere_mention_of_marker_not_exempt(self):
        # DSR8: prose that just mentions the marker text, with no
        # colon-and-reason, must not silently exempt the whole line.
        self.assertIn(
            "relative-time-word",
            kinds("we discussed the datescan:allow marker; filed yesterday"))

    def test_marker_requires_word_boundary(self):
        # DSR8: the marker embedded inside a longer token must not match.
        self.assertIn(
            "relative-time-word",
            kinds("xdatescan:allow: reason  filed yesterday"))


class NonIsoDates(unittest.TestCase):
    def test_slash_date_flagged(self):
        fs = scan("filed on 23/07/2026 by hand")
        self.assertEqual(["non-iso-date"], [f.kind for f in fs])
        self.assertEqual("23/07/2026", fs[0].match)

    def test_numeral_triple_not_a_date_not_flagged(self):
        # DSR2: the slash-date pattern used to match any numeral triple,
        # false-firing on a session number like `23/26/27` (26 is not a
        # plausible month or day-with-swapped-fields either).
        self.assertEqual([], scan("session 23/26/27 was the queue run"))

    def test_dash_date_flagged(self):
        # DSR5: dash DD-MM-YYYY, a form that scanned clean before this fix.
        fs = scan("filed on 23-07-2026 by hand")
        self.assertEqual(["non-iso-date"], [f.kind for f in fs])
        self.assertEqual("23-07-2026", fs[0].match)

    def test_dash_numeral_triple_not_a_date_not_flagged(self):
        # 26/27 is not a plausible (day, month) pair in either field order,
        # even though the shape (NN-NN-YYYY) matches the dash-date pattern.
        self.assertEqual([], scan("range 26-27-2026 is not a date"))

    def test_dash_date_not_confused_with_iso(self):
        # An ISO date (YYYY-MM-DD) must still be read as clean/valid ISO,
        # not double-flagged as a dash-date too.
        fs = scan("stamped 2026-07-23 correctly")
        self.assertEqual([], fs)

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
        # a relative-time word outside docs/ must not be flagged. Uses
        # "yesterday" (unaffected by the today-only DSR3 narrowing) so this
        # test stays about path-scoping, not today's cue heuristic.
        self._write("README.md", "shipped yesterday outside docs\n")
        self._write("docs/note.md", "shipped yesterday inside docs\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))
        findings = ds.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/note.md", findings[0].path)

    def test_falls_back_to_root_when_no_docs_dir(self):
        self._write("note.md", "shipped yesterday, no docs dir here\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))

    def test_nonexistent_path_is_an_error_not_a_pass(self):
        self.assertEqual(
            2, self._main(["--root", str(self.tmp), str(self.tmp / "gone")]))

    def test_warn_always_exits_zero(self):
        self._write("docs/note.md", "shipped yesterday\n")
        self.assertEqual(
            0, self._main(["--warn", "--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_without_warn_findings_exit_one(self):
        self._write("docs/note.md", "shipped yesterday\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_clean_tree_exits_zero(self):
        self._write("docs/note.md", "stamped 2026-07-23, all absolute\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_datescanignore_exempts_path(self):
        self._write("docs/note.md", "shipped yesterday\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))
        self._write(".datescanignore", "docs/note.md\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_non_markdown_files_skipped(self):
        self._write("docs/note.txt", "shipped yesterday, not markdown\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ds._selftest())


if __name__ == "__main__":
    unittest.main()


class Allowances(unittest.TestCase):
    """GUARDS.md — narrow, noisy, reasoned."""

    def test_scoped_marker_exempts_only_its_own_kind(self):
        # A marker written for the relative-time word must not also exempt a
        # non-ISO date sitting on the same line.
        got = kinds("filed yesterday on 03/04/2026  "
                    "<!-- datescan:allow:relative-time-word: quoting a source -->")
        self.assertNotIn("relative-time-word", got)
        self.assertIn("non-iso-date", got)

    def test_unscoped_marker_still_exempts_everything_on_the_line(self):
        self.assertEqual([], kinds("filed yesterday on 03/04/2026  "
                                   "<!-- datescan:allow: verbatim quotation -->"))

    def test_suppressions_are_counted_per_kind(self):
        tally = ds.Tally()
        ds.scan_text("t", "filed yesterday  <!-- datescan:allow: quoted -->\n", tally)
        self.assertEqual({"relative-time-word": 1}, tally.by_marker)

    def test_html_comment_close_is_not_a_reason(self):
        # `\S` would accept `-->` as the reason; the house form needs `\w`.
        self.assertIsNone(ds.parse_allow("x <!-- datescan:allow: -->"))
        self.assertEqual("", ds.parse_allow("x <!-- datescan:allow: real reason -->"))

    def test_clean_tally_reports_known_zeros(self):
        self.assertIn("0 by allow-marker", ds.Tally().summary())
