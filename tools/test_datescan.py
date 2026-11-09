"""Stdlib-only tests for datescan (no pytest needed): `python3 -m unittest`."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import memprobe

TOOLS_DIR = Path(__file__).resolve().parent

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
    """The kinds that BLOCK. A report-only finding (115/090: a blockquoted
    line) never blocks, so it is not here; see `advisory`."""
    return [f.kind for f in scan(text) if f.blocks]


def blocking(text):
    return [f for f in scan(text) if f.blocks]


def advisory(text):
    return [f for f in scan(text) if not f.blocks]


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

    # 115/090: a blockquoted line still never BLOCKS; it now reports.
    def test_blockquote_exempt(self):
        self.assertEqual([], blocking("> this happened yesterday, quoted verbatim"))

    def test_blockquote_with_leading_space_exempt(self):
        self.assertEqual([], blocking("   > indented quote says yesterday"))


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
        self._write(".datescanignore", "# a reasoned fixture exemption\ndocs/note.md\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_non_markdown_files_skipped(self):
        self._write("docs/note.txt", "shipped yesterday, not markdown\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ds._selftest())


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
                for p in ds._walk_files(self.tmp)}

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


class Allowances(unittest.TestCase):
    """GUARDS.md — narrow, noisy, reasoned, declared."""

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


class BoundedMemory(unittest.TestCase):
    """020/380 — applying 020/370's bounded-memory fix to datescan. Mike's
    ruling, verbatim: "it should not matter how much it scans it should no
    have this affect". Measured BEFORE this fix (see the board item's own
    before/after table): a 23 MB larger many-line docs file drove ~95 MB of
    peak-RSS growth, and a 23 MB larger SINGLE-line file drove ~268 MB — both
    from the old `read_text()` whole-file string plus `text.splitlines()`
    whole-file list, the same double-materialization shape secretscan's
    `020/370` fixed.

    Runs the real CLI as a SUBPROCESS via `memprobe.run_and_measure` and
    reads peak RSS back from the kernel — `tracemalloc` only sees the Python
    heap, not the whole OS process (see `tools/memprobe.py`).

    Content is plain filler prose with no relative-time word, non-ISO date,
    or invalid-ISO-date shape anywhere, so both runs produce zero findings —
    the only thing that differs is how many bytes there are to read."""

    DATESCAN = str(TOOLS_DIR / "datescan.py")
    SMALL_BYTES = 1 * 1024 * 1024
    LARGE_BYTES = 8 * 1024 * 1024
    # Grounded in the FIX's design (`ground-numeric-limits`), not fitted to a
    # measurement, and a LITERAL rather than a reference to
    # `ds._READ_CHUNK_BYTES`/`_MAX_LINE_BYTES` — this test must still MEASURE
    # a real blow-up (not just fail an AttributeError at import) if ever run
    # against the pre-fix module, which carries neither constant. The only
    # per-file state the fix's `_content_lines_from_file` ever holds is one
    # read chunk in flight (1 MiB) plus one physical line capped at 8 KiB.
    # Both runs produce zero findings, so growth should be close to zero; 8x
    # that fixed per-file state leaves generous headroom for interpreter/
    # allocator noise while staying far below what the pre-fix whole-file-read
    # code showed for this size delta (measured, while building this fix, at
    # ~95 MB for a many-line file and ~268 MB for a single-line file — facts
    # recorded for context, not what set this number).
    GROWTH_BOUND_BYTES = 8 * (1 * 1024 * 1024 + 8 * 1024)

    @staticmethod
    def _build_many_line(target_bytes: int, path: Path) -> None:
        with open(path, "w") as f:
            written = 0
            i = 0
            while written < target_bytes:
                line = f"this is filler prose line number {i} with no relative dates here\n"
                f.write(line)
                written += len(line)
                i += 1

    @staticmethod
    def _build_one_line(target_bytes: int, path: Path) -> None:
        with open(path, "w") as f:
            f.write("x" * target_bytes)
            f.write("\n")

    def _peak_rss_for(self, builder, size_bytes: int) -> int:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        docs = tmp / "docs"
        docs.mkdir()
        builder(size_bytes, docs / "note.md")
        # Safety (020/370's own incident: a probe thrashed the principal's
        # machine doing exactly this kind of measurement): hard-kill well
        # short of the 1 GB line, and a ceiling so a regression that
        # reintroduces catastrophic behaviour fails the test instead of
        # hanging CI.
        result = memprobe.run_and_measure(
            [sys.executable, self.DATESCAN, "--root", str(tmp), str(docs)],
            timeout=60, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        self.assertEqual(0, result.returncode,
                         "filler content must not itself flag anything")
        return result.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_many_line_file_size(self):
        small_peak = self._peak_rss_for(self._build_many_line, self.SMALL_BYTES)
        large_peak = self._peak_rss_for(self._build_many_line, self.LARGE_BYTES)
        growth = large_peak - small_peak
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for a "
            f"{(self.LARGE_BYTES - self.SMALL_BYTES) / 1e6:.1f} MB larger "
            f"many-line file (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB) — memory is scaling with "
            "input size again (020/380).")

    def test_peak_memory_does_not_scale_with_single_line_length(self):
        small_peak = self._peak_rss_for(self._build_one_line, self.SMALL_BYTES)
        large_peak = self._peak_rss_for(self._build_one_line, self.LARGE_BYTES)
        growth = large_peak - small_peak
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for a "
            f"{(self.LARGE_BYTES - self.SMALL_BYTES) / 1e6:.1f} MB longer "
            f"single line (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB) — memory is scaling with "
            "input size again (020/380).")


# --- 115/090: the report-only tier ------------------------------------------

# Every check that BLOCKED when the report-only tier was built, one fixture
# each. A check leaving this list is a narrowing of the gate, and that is the
# principal's decision, never a refactor's: the tier was granted on the
# condition that nothing that blocks today stops blocking (Mike's answer of
# 2026-11-03 on 115/090, "Carry on to datescan").
RELATIVE_TERMS_AT_115_090 = (
    "tonight", "tomorrow", "yesterday",
    "last night", "last week", "last month", "last year",
    "next week", "next month", "next year",
    "this week", "this month", "this year",
    "the other day", "a few days ago", "a few weeks ago", "a few months ago",
)
BLOCKING_AT_115_090 = (
    *(("relative-time-word", f"It happened {t} here.") for t in RELATIVE_TERMS_AT_115_090),
    ("relative-time-word", "Dated today, all fields correct."),
    ("relative-time-word", "Stamped today, all fields correct."),
    ("relative-time-word", "The figures as of today hold."),
    ("relative-time-word", "Today (2026-07-23) it shipped."),
    ("non-iso-date", "Filed on 23/07/2026 by hand."),
    ("non-iso-date", "Filed on 23-07-2026 by hand."),
    ("non-iso-date", "Filed on July 23, 2026 by hand."),
    ("non-iso-date", "Filed on 23 July 2026 by hand."),
    ("invalid-iso-date", "Bogus date 2026-13-40 here."),
)


class _Cli(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        (self.tmp / "docs").mkdir()

    def run_cli(self, text, *extra):
        import contextlib
        import io
        (self.tmp / "docs" / "a.md").write_text(text + "\n", encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = ds.main(["--root", str(self.tmp), *extra])
        return rc, out.getvalue()

    def run_json(self, text, *extra):
        import json
        rc, out = self.run_cli(text, "--json", *extra)
        return rc, json.loads(out)


class CoverageLine(_Cli):
    """115/130 - a clean run says how much it opened; a run over nothing says
    so in words, and the exit status is the same either way."""

    def test_clean_run_counts_files_and_lines(self):
        rc, out = self.run_cli("# T\n\nStamped 2026-07-23.")
        self.assertEqual(0, rc)
        self.assertIn("  coverage: 1 file(s) opened \u00b7 3 line(s) read", out)
        self.assertNotIn("scanned nothing", out)

    def test_findings_run_prints_the_coverage_line_too(self):
        rc, out = self.run_cli("# T\n\nShipped yesterday.")
        self.assertEqual(1, rc)
        self.assertIn("relative-time-word", out)
        self.assertIn("  coverage: 1 file(s) opened \u00b7 3 line(s) read", out)

    def test_run_over_nothing_says_scanned_nothing_and_still_exits_0(self):
        import contextlib
        import io
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = ds.main(["--root", str(self.tmp)])
        self.assertEqual(0, rc)
        self.assertIn("coverage: 0 file(s) opened \u00b7 0 line(s) read", out.getvalue())
        self.assertIn("scanned nothing", out.getvalue())

    def test_json_carries_the_same_coverage(self):
        rc, out = self.run_json("# T\n\nStamped 2026-07-23.")
        self.assertEqual({"files_opened": 1, "lines_read": 3,
                          "scanned_nothing": False}, out["coverage"])


class BlockingSetPinned(_Cli):
    """The blocking set cannot shrink (115/090)."""

    def test_every_relative_term_that_blocked_is_still_on_the_list(self):
        self.assertEqual(set(RELATIVE_TERMS_AT_115_090), set(ds.RELATIVE_TIME_TERMS))

    def test_every_pinned_check_blocks_its_fixture(self):
        for kind, text in BLOCKING_AT_115_090:
            with self.subTest(text=text):
                self.assertIn(kind, kinds(text))
                rc, out = self.run_json(text)
                self.assertEqual(1, rc)
                self.assertIn(kind, {f["kind"] for f in out["findings"]})
                self.assertEqual(0, out["counts"]["advisory"])
                self.assertTrue(out["blocked"])

    def test_a_finding_that_does_not_say_blocks(self):
        self.assertTrue(ds.Finding("p", 1, "relative-time-word", "x", "d").blocks)

    def test_only_a_blockquoted_line_builds_a_report_only_finding(self):
        # Every pinned fixture, written as prose, blocks and reports nothing;
        # the same fixture behind `>` reports and blocks nothing.
        for kind, text in BLOCKING_AT_115_090:
            with self.subTest(text=text):
                self.assertEqual([], advisory(text))
                quoted = scan("> " + text)
                self.assertEqual([], [f for f in quoted if f.blocks])
                self.assertEqual([(kind, ds.WHERE_BLOCKQUOTE)],
                                 [(f.kind, f.where) for f in quoted])


class BlockquoteReports(_Cli):
    """A blockquoted line reports its dating without blocking (115/090)."""

    def test_alone_it_exits_clean_and_is_listed(self):
        rc, out = self.run_cli("> 🎯 Decide this by next week.")
        self.assertEqual(0, rc)
        self.assertIn("✓ datescan clean", out)
        self.assertIn("  datescan advisory: 1 finding(s) — reported, not blocking.", out)
        self.assertIn("🟡 REPORT-ONLY FINDINGS", out)
        self.assertRegex(out, r"docs/a\.md:1  \[advisory/blockquote\] "
                              r"\[relative-time-word\] 'next week' .*"
                              r"\[datescan:relative-time-word\]")

    def test_the_count_line_prints_its_zero(self):
        rc, out = self.run_cli("Stamped 2026-07-23.")
        self.assertEqual(0, rc)
        self.assertIn("  datescan advisory: 0 finding(s) — reported, not blocking.", out)
        self.assertNotIn("REPORT-ONLY", out)

    def test_beside_a_blocking_finding_the_scan_still_blocks(self):
        rc, out = self.run_cli("> quoted 23/07/2026\nIt landed last week.")
        self.assertEqual(1, rc)
        self.assertIn("✗ datescan: 1 finding(s).", out)
        self.assertIn("  datescan advisory: 1 finding(s) — reported, not blocking.", out)

    def test_json_keeps_blocking_and_report_only_apart(self):
        rc, out = self.run_json("> quoted 23/07/2026\nIt landed last week.")
        self.assertEqual(1, rc)
        self.assertFalse(out["clean"])
        self.assertTrue(out["blocked"])
        self.assertEqual({"blocking": 1, "advisory": 1}, out["counts"])
        self.assertEqual(["relative-time-word"], [f["kind"] for f in out["findings"]])
        adv = out["advisory"]["findings"]
        self.assertEqual(["non-iso-date"], [f["kind"] for f in adv])
        self.assertEqual(("advisory", "blockquote"), (adv[0]["response"], adv[0]["where"]))
        self.assertEqual("datescan:non-iso-date", adv[0]["id"])

    def test_clean_keeps_its_meaning_on_a_report_only_run(self):
        rc, out = self.run_json("> it shipped yesterday")
        self.assertEqual(0, rc)
        self.assertTrue(out["clean"])
        self.assertFalse(out["blocked"])
        self.assertEqual([], out["findings"])

    def test_warn_still_exits_zero_and_still_counts(self):
        rc, out = self.run_cli("> it shipped yesterday\nfiled tomorrow", "--warn")
        self.assertEqual(0, rc)
        self.assertIn("datescan advisory: 1 finding(s)", out)

    def test_an_allow_marker_exempts_a_report_only_hit_and_is_counted(self):
        rc, out = self.run_cli(
            "> yesterday  <!-- datescan:allow:relative-time-word: quoted source -->")
        self.assertEqual(0, rc)
        self.assertIn("datescan advisory: 0 finding(s)", out)
        self.assertIn("1 by allow-marker", out)

    def test_a_marker_for_another_kind_leaves_it_reported(self):
        rc, out = self.run_cli(
            "> yesterday  <!-- datescan:allow:non-iso-date: quoted source -->")
        self.assertIn("datescan advisory: 1 finding(s)", out)

    def test_an_ignore_glob_exempts_it(self):
        (self.tmp / ".datescanignore").write_text(
            "# a quoted source, kept as written\ndocs/a.md\n", encoding="utf-8")
        rc, out = self.run_cli("> it shipped yesterday")
        self.assertIn("datescan advisory: 0 finding(s)", out)

    def test_code_stays_exempt_inside_and_beside_a_blockquote(self):
        for text in ("> the `yesterday` token", "    > yesterday, indented code",
                     "```\n> yesterday\n```"):
            with self.subTest(text=text):
                self.assertEqual([], scan(text))

    def test_a_quoted_mention_stays_exempt_in_a_blockquote(self):
        self.assertEqual([], scan('> the rule bans "yesterday" and "last week"'))

    def test_a_bare_today_is_not_reported_in_a_blockquote_either(self):
        # Left out on purpose: see datescan.off-rules.design.md § 3.
        self.assertEqual([], scan("> Filed today."))
        self.assertEqual([], scan("Filed today."))


def _git(repo, *args):
    import os
    import subprocess
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True, check=True,
        env={**os.environ,
             "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid",  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
             "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"})  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo


class StagedPlaneBase(unittest.TestCase):
    """Shared plumbing for the 320/600 `--staged` tests: a throwaway git repo
    the test drives with real `git add`, entered by cwd as the hook does."""
    MOD = None

    def setUp(self):
        import os
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo, ignore_errors=True)
        _git(self.repo, "init", "-q")
        self._old_cwd = os.getcwd()
        os.chdir(self.repo)
        self.addCleanup(os.chdir, self._old_cwd)

    def _write(self, rel, text):
        p = self.repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _main(self, *args):
        import contextlib
        import io
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = self.MOD.main([*args])
        return rc, out.getvalue()

    def _run(self, *extra):
        return self._main("--staged", "--root", str(self.repo), *extra)

    def _add(self, *paths):
        _git(self.repo, "add", *paths)

    def _commit(self, *paths):
        _git(self.repo, "add", *paths)
        _git(self.repo, "commit", "-q", "-m", "c")


class StagedPlane(StagedPlaneBase):
    """320/600, slice 2: `--staged` reads the INDEX, and only the lines a commit
    adds. Pairs a false block with a false pass, because fixing one direction
    alone is how the other gets missed."""
    MOD = ds
    BAD = "It landed last week.\n"
    GOOD = "Stamped 2026-07-23.\n"

    def test_false_block_an_unstaged_draft_does_not_block(self):
        self._write("docs/a.md", self.GOOD)
        self._commit("docs/a.md")
        self._write("docs/a.md", self.GOOD + "also fine\n")
        self._add("docs/a.md")
        self._write("docs/draft.md", self.BAD)          # never staged
        rc, out = self._run("docs")
        self.assertEqual(0, rc, out)
        # ...and the working-tree plane still sees it, so the test is not vacuous.
        self.assertEqual(1, self._main("--root", str(self.repo), "docs")[0])

    def test_false_pass_a_staged_defect_fixed_on_disk_still_blocks(self):
        self._write("docs/c.md", self.BAD)
        self._add("docs/c.md")
        self._write("docs/c.md", self.GOOD)             # fixed after `git add`
        rc, out = self._run("docs")
        self.assertEqual(1, rc, out)
        self.assertIn("docs/c.md:1", out)

    def test_a_staged_clean_file_passes(self):
        self._write("docs/ok.md", self.GOOD)
        self._add("docs/ok.md")
        self.assertEqual(0, self._run("docs")[0])

    def test_only_added_lines_report_not_a_defect_already_in_the_file(self):
        self._write("docs/old.md", self.BAD)
        self._commit("docs/old.md")
        self._write("docs/old.md", self.BAD + self.GOOD)
        self._add("docs/old.md")
        self.assertEqual(0, self._run("docs")[0])

    def test_an_added_defect_in_an_edited_file_reports_its_real_line(self):
        self._write("docs/e.md", self.GOOD + self.GOOD)
        self._commit("docs/e.md")
        self._write("docs/e.md", self.GOOD + self.GOOD + self.BAD)
        self._add("docs/e.md")
        rc, out = self._run("docs")
        self.assertEqual(1, rc, out)
        self.assertIn("docs/e.md:3", out)

    def test_fence_context_comes_from_the_whole_staged_file(self):
        # The added line sits inside a fence opened by an UNCHANGED line above
        # it. Scanning added lines alone would call it prose and block.
        self._write("docs/f.md", "```\n" + self.GOOD + "```\n")
        self._commit("docs/f.md")
        self._write("docs/f.md", "```\n" + self.GOOD + self.BAD + "```\n")
        self._add("docs/f.md")
        self.assertEqual(0, self._run("docs")[0])

    def test_scope_narrows_the_staged_set(self):
        self._write("notes/x.md", self.BAD)
        self._add("notes/x.md")
        # A scope must name a path git knows (160/950): `docs` is tracked, with
        # nothing wrong staged under it, so it narrows the set to a clean pass.
        self._write("docs/ok.md", "Fine.\n")
        self._add("docs/ok.md")
        self.assertEqual(0, self._run("docs")[0])
        self.assertEqual(1, self._run("notes")[0])
        self.assertEqual(1, self._run()[0])
        self.assertEqual(2, self._run("nowhere")[0])   # names nothing git knows

    def test_an_absolute_scope_is_refused_not_passed(self):
        self._write("docs/x.md", self.BAD)
        self._add("docs/x.md")
        self.assertEqual(2, self._run(str(self.repo / "docs"))[0])

    def test_ignore_glob_still_applies(self):
        self._write("docs/frozen/z.md", self.BAD)
        self._write(".datescanignore",
                    "# frozen record, kept as written\ndocs/frozen/**\n")
        self._add("docs/frozen/z.md")
        self.assertEqual(0, self._run("docs")[0])

    def test_json_mode_reports_the_staged_finding(self):
        import json
        self._write("docs/j.md", self.BAD)
        self._add("docs/j.md")
        rc, out = self._run("docs", "--json")
        self.assertEqual(1, rc)
        self.assertEqual("docs/j.md", json.loads(out)["findings"][0]["path"])

    def test_a_report_only_hit_on_an_added_line_reports_and_passes(self):
        # 115/090: the hook plane reports a blockquoted hit the commit adds,
        # and only an added one, without blocking.
        self._write("docs/q.md", "> old callout, due next week\n")
        self._commit("docs/q.md")
        self._write("docs/q.md", "> old callout, due next week\n"
                                 "> new callout, due next month\n")
        self._add("docs/q.md")
        rc, out = self._run("docs")
        self.assertEqual(0, rc, out)
        self.assertIn("datescan advisory: 1 finding(s)", out)
        self.assertIn("docs/q.md:2", out)
        self.assertNotIn("docs/q.md:1", out)

    def test_a_large_staged_file_is_streamed_whole(self):
        # More than a pipe buffer, with the defect on the last line: the blob
        # is read to its end, not cut short (a short read would pass it).
        self._write("docs/big.md", (self.GOOD * 20000) + self.BAD)
        self._add("docs/big.md")
        rc, out = self._run("docs")
        self.assertEqual(1, rc, out)
        self.assertIn("docs/big.md:20001", out)


if __name__ == "__main__":
    unittest.main()
