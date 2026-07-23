"""Stdlib-only tests for wrapscan (no pytest needed): `python3 -m unittest`."""

import unittest

import wrapscan as ws


def scan(text, limit=ws.LINE_LIMIT):
    return ws.scan_text("t", text, limit)


def lengths(text, limit=ws.LINE_LIMIT):
    return [f.length for f in scan(text, limit)]


class BoundaryLength(unittest.TestCase):
    def test_exactly_85_is_clean(self):
        self.assertEqual([], scan("a" * 85))

    def test_86_is_flagged_when_not_exempt(self):
        # 86 plain letters with no whitespace at all is one unbreakable
        # token (nowhere it could have wrapped) — the exemption applies.
        # A real over-length *prose* line (many words) must still flag.
        prose = "word " * 15 + "more words here to push it over eighty five columns"
        self.assertGreater(len(prose), 85)
        self.assertTrue(lengths(prose))

    def test_84_is_clean(self):
        self.assertEqual([], scan("b" * 84))

    def test_finding_reports_true_length(self):
        prose = "w " * 50  # 100 chars, many wrap points, genuinely over-wrapped
        fs = scan(prose)
        self.assertEqual([100], [f.length for f in fs])


class FencedCodeExemption(unittest.TestCase):
    def test_fenced_block_exempt(self):
        text = "prose\n```\n" + ("c" * 90) + "\n```\nmore prose\n"
        self.assertEqual([], scan(text))

    def test_tilde_fence_exempt(self):
        text = "prose\n~~~\n" + ("c" * 90) + "\n~~~\nmore prose\n"
        self.assertEqual([], scan(text))

    def test_content_outside_fence_still_checked(self):
        prose = "word " * 20  # over limit, real wrap points
        text = "```\n" + ("c" * 90) + "\n```\n" + prose + "\n"
        self.assertTrue(lengths(text))


class IndentedCodeExemption(unittest.TestCase):
    def test_four_space_indent_exempt(self):
        self.assertEqual([], scan("    " + "c" * 90))

    def test_tab_indent_exempt(self):
        self.assertEqual([], scan("\t" + "c" * 90))

    def test_three_space_indent_not_exempt(self):
        # Under CommonMark's own threshold — not indented code, still prose.
        line = "   " + "word " * 20
        self.assertTrue(lengths(line))

    def test_blank_indented_line_not_flagged_as_code_or_anything(self):
        self.assertEqual([], scan("    \n"))


class TableRowExemption(unittest.TestCase):
    def test_table_row_with_pipes_exempt(self):
        self.assertEqual([], scan("| " + "c" * 90 + " |"))

    def test_row_without_pipe_still_checked(self):
        prose = "word " * 20
        self.assertTrue(lengths(prose))


class HeadingExemption(unittest.TestCase):
    def test_atx_heading_exempt(self):
        self.assertEqual([], scan("# " + "h" * 90))

    def test_deep_atx_heading_exempt(self):
        self.assertEqual([], scan("###### " + "h" * 90))

    def test_hash_in_prose_not_a_heading(self):
        # A '#' not at line start (after whitespace) is not a heading.
        prose = "word " * 15 + "#hashtag " + "word " * 5
        self.assertTrue(lengths(prose))


class ReferenceLinkDefinitionExemption(unittest.TestCase):
    def test_ref_link_definition_exempt(self):
        self.assertEqual(
            [], scan("[ref]: https://example.invalid/" + "p" * 90))

    def test_non_ref_line_with_brackets_still_checked(self):
        prose = "See [this thing] over here: " + "word " * 15
        self.assertTrue(lengths(prose))


class SingleUnbreakableTokenExemption(unittest.TestCase):
    def test_trailing_url_exempt(self):
        line = "See the doc at " + "a" * 90
        self.assertEqual([], scan(line))

    def test_whole_line_one_token_exempt(self):
        # No whitespace anywhere — nowhere it could have wrapped.
        self.assertEqual([], scan("y" * 86))

    def test_multiword_overflow_flagged(self):
        # A real wrap point still exists inside the overflow region itself.
        line = "w" * 87 + " ww"
        self.assertTrue(lengths(line))

    def test_short_trailing_token_after_many_words_is_exempt(self):
        # Per the heuristic as specified: the overflow region is judged on
        # its own — if the tail past the limit is a single token, it is
        # exempt even though earlier words in the line wrapped fine. This is
        # the documented, accepted trade-off (see module header).
        line = "word " * 17 + "xx"
        self.assertEqual([], scan(line))


class AllowMarker(unittest.TestCase):
    def test_inline_allow_marker_exempts_line(self):
        line = ("word " * 20) + " <!-- wrapscan:allow: selftest fixture -->"
        self.assertEqual([], scan(line))


class FailOpenGuard(unittest.TestCase):
    def test_empty_file_is_clean_not_a_crash(self):
        self.assertEqual([], scan(""))

    def test_whitespace_only_file_is_clean(self):
        self.assertEqual([], scan("\n\n   \n"))

    def test_malformed_unclosed_fence_does_not_crash(self):
        # An unterminated fence must not raise, and must not silently
        # swallow prose outside it that was never inside the (never-closed)
        # fence to begin with.
        text = "```\nunclosed fence forever\n" + ("word " * 20)
        # Everything after the opening fence is treated as inside it (fails
        # toward under-flagging, the house's stated preference), but the
        # call itself must not raise and must not be mistaken for "clean and
        # safe" — an empty result here is a known, accepted trade-off, not a
        # crash, which is what this guard actually proves.
        try:
            result = scan(text)
        except Exception as e:  # pragma: no cover - the guard is the point
            self.fail(f"malformed input must not crash: {e!r}")
        self.assertIsInstance(result, list)


class Limit(unittest.TestCase):
    def test_custom_limit_respected(self):
        # Multi-word so a tighter limit finds a real wrap point inside the
        # (now-)overflow — a single unbreakable blob would exempt regardless
        # of the limit and defeat the point of this test.
        line = "word " * 10
        self.assertEqual([], scan(line, limit=60))
        self.assertTrue(lengths(line, limit=40))


class Ignore(unittest.TestCase):
    def test_exact_glob(self):
        self.assertTrue(ws._ignored("docs/fixture.md", ["docs/fixture.md"]))

    def test_subtree_glob(self):
        self.assertTrue(ws._ignored("docs/sessions/x.md", ["docs/sessions/"]))
        self.assertTrue(ws._ignored("docs/sessions/x.md", ["docs/sessions"]))

    def test_non_match(self):
        self.assertFalse(ws._ignored("docs/real.md", ["docs/fixture.md"]))


class WholeTree(unittest.TestCase):
    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ws.Path(tempfile.mkdtemp())
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
            return ws.main(argv)

    def test_defaults_to_docs_subdir(self):
        long_prose = "word " * 20
        self._write("README.md", long_prose + " outside docs\n")
        self._write("docs/note.md", long_prose + " inside docs\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))
        findings = ws.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/note.md", findings[0].path)

    def test_falls_back_to_root_when_no_docs_dir(self):
        self._write("note.md", ("word " * 20) + " no docs dir here\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))

    def test_nonexistent_path_is_an_error_not_a_pass(self):
        self.assertEqual(
            2, self._main(["--root", str(self.tmp), str(self.tmp / "gone")]))

    def test_warn_always_exits_zero(self):
        self._write("docs/note.md", ("word " * 20) + "\n")
        self.assertEqual(
            0, self._main(["--warn", "--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_without_warn_findings_exit_one(self):
        self._write("docs/note.md", ("word " * 20) + "\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_clean_tree_exits_zero(self):
        self._write("docs/note.md", "# OK\n\nShort line only.\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_wrapscanignore_exempts_path(self):
        self._write("docs/note.md", ("word " * 20) + "\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))
        self._write(".wrapscanignore", "docs/note.md\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_non_markdown_files_skipped(self):
        self._write("docs/note.txt", ("word " * 20) + "\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_custom_limit_via_cli(self):
        self._write("docs/note.md", ("word " * 10) + "\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), "--limit", "40",
                           str(self.tmp / "docs")]))


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ws._selftest())


if __name__ == "__main__":
    unittest.main()
