"""Stdlib-only tests for linkscan (no pytest needed): `python3 -m unittest`.

Pure-logic parts (slugify, heading extraction, code-stripping, target split) are
unit-tested directly. The end-to-end parts build a throwaway doc tree under a tmp
dir and drive scan_paths(), so path resolution (relative + root-relative), anchor
validation (same-file + cross-file), and the code/fence/allow skips are proven
against the real filesystem, not a mock."""

import tempfile
import unittest
from pathlib import Path

import linkscan


class Slugify(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(linkscan.slugify("Hello World"), "hello-world")

    def test_strips_inline_formatting(self):
        self.assertEqual(linkscan.slugify("`code` and **bold**"), "code-and-bold")

    def test_link_in_heading_uses_text(self):
        self.assertEqual(linkscan.slugify("[See docs](x.md)"), "see-docs")

    def test_punct_and_emdash(self):
        self.assertEqual(linkscan.slugify("A—B! (c)"), "ab-c")

    def test_duplicate_headings_get_suffixes(self):
        text = "# Notes\n## Notes\n### Notes\n"
        self.assertEqual(linkscan.heading_slugs(text), {"notes", "notes-1", "notes-2"})

    def test_headings_in_fence_ignored(self):
        text = "# Real\n```\n# Fake\n```\n## Also Real\n"
        self.assertEqual(linkscan.heading_slugs(text), {"real", "also-real"})


class InlineCode(unittest.TestCase):
    def test_strips_backtick_span(self):
        self.assertEqual(linkscan._strip_inline_code("a `x](y)` b").strip("ab "),
                         "")  # the span becomes blanks, no ']( ' survives

    def test_link_inside_code_not_yielded(self):
        text = "start\n`[nope](gone.md)` and [yes](there.md)\n"
        got = [d for _, d in linkscan.iter_links(text)]
        self.assertEqual(got, ["there.md"])

    def test_allow_marker_skips_line(self):
        text = "[dangling](gone.md) <!-- linkscan:allow: intentional -->\n"
        self.assertEqual(list(linkscan.iter_links(text)), [])


class TargetSplit(unittest.TestCase):
    def test_path_and_anchor(self):
        self.assertEqual(linkscan.split_target("a/b.md#sec"), ("a/b.md", "sec"))

    def test_same_file_anchor(self):
        self.assertEqual(linkscan.split_target("#sec"), ("", "sec"))

    def test_percent_decoded(self):
        self.assertEqual(linkscan.split_target("a%20b.md")[0], "a b.md")

    def test_external_detected(self):
        for ext in ("https://x", "http://x", "mailto:a@b.c", "tel:123", "//host/x"):
            self.assertTrue(linkscan.is_external(ext), ext)
        for internal in ("a.md", "../a.md", "/a.md", "#sec", "a.md#sec"):
            self.assertFalse(linkscan.is_external(internal), internal)


class Angle(unittest.TestCase):
    def test_bracketed_destination_with_space(self):
        text = "[x](<a b.md>)\n"
        self.assertEqual([d for _, d in linkscan.iter_links(text)], ["a b.md"])

    def test_title_is_stripped(self):
        text = '[x](target.md "a title")\n'
        self.assertEqual([d for _, d in linkscan.iter_links(text)], ["target.md"])


class EndToEnd(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="linkscan-test-"))
        (self.tmp / "docs").mkdir()
        (self.tmp / "target.md").write_text("# Real Heading\n\nbody\n")
        (self.tmp / "docs" / "child.md").write_text("# Child\n## A Point\n")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _write(self, rel, body):
        p = self.tmp / rel
        p.write_text(body)
        return p

    def test_clean_tree(self):
        self._write("index.md",
                    "# Top\n## S\n"
                    "[f](target.md)\n"
                    "[a](target.md#real-heading)\n"
                    "[same](#s)\n"
                    "[down](docs/child.md#a-point)\n"
                    "[ext](https://example.com)\n"
                    "[line](target.md#L9)\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_missing_file(self):
        self._write("index.md", "# T\n[x](gone.md)\n")
        fs = linkscan.scan_paths([self.tmp], self.tmp)
        self.assertEqual(len(fs), 1)
        self.assertEqual(fs[0].kind, "missing-file")

    def test_missing_cross_file_anchor(self):
        self._write("index.md", "# T\n[x](target.md#ghost)\n")
        fs = linkscan.scan_paths([self.tmp], self.tmp)
        self.assertEqual([f.kind for f in fs], ["missing-anchor"])

    def test_missing_same_file_anchor(self):
        self._write("index.md", "# T\n[x](#ghost)\n")
        fs = linkscan.scan_paths([self.tmp], self.tmp)
        self.assertEqual([f.kind for f in fs], ["missing-anchor"])

    def test_relative_up_and_down_resolve(self):
        # a doc in docs/ links up to root and across
        self._write("docs/deep.md", "# D\n[up](../target.md)\n[sib](child.md#a-point)\n")
        self.assertEqual(linkscan.scan_paths([self.tmp / "docs" / "deep.md"], self.tmp), [])

    def test_root_relative_link(self):
        self._write("docs/deep.md", "# D\n[abs](/target.md)\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_link_to_directory_ok(self):
        self._write("index.md", "# T\n[dir](docs/)\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_anchor_into_nonmarkdown_not_validated(self):
        (self.tmp / "code.py").write_text("x = 1\n")
        self._write("index.md", "# T\n[src](code.py#L1)\n[src2](code.py#anything)\n")
        # neither anchor is validated for a non-markdown target; file exists → clean
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_ignore_glob(self):
        self._write("skip.md", "# T\n[x](gone.md)\n")
        (self.tmp / ".linkscanignore").write_text("skip.md\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_fenced_link_skipped(self):
        self._write("index.md", "# T\n```\n[x](gone.md)\n```\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_content_dir_named_build_is_walked(self):
        # Regression: `build`/`dist` are NOT hardcode-skipped — a content dir
        # sharing the name (atelier's own docs/build/ doctrine layer) must be
        # scanned, not masked. A repo with a real build-output dir uses
        # .linkscanignore instead.
        (self.tmp / "docs" / "build").mkdir(parents=True)
        self._write("docs/build/note.md", "# B\n[x](gone.md)\n")
        fs = linkscan.scan_paths([self.tmp], self.tmp)
        self.assertEqual([f.kind for f in fs], ["missing-file"])

    def test_selftest_passes(self):
        self.assertEqual(linkscan._selftest(), 0)


class ReviewFindings(unittest.TestCase):
    """Pins for the 2026-07-10 Fable review findings (L1–L10): each was a
    live-proven false negative, false positive, or silent green before the fix."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="linkscan-review-"))

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _write(self, rel, body):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body)
        return p

    # L1 — a typo'd path arg must never scan nothing and report clean.
    def test_nonexistent_path_arg_is_usage_error(self):
        self.assertEqual(linkscan.main([str(self.tmp / "no-such-dir")]), 2)

    def test_nonexistent_root_is_usage_error(self):
        self.assertEqual(
            linkscan.main(["--root", str(self.tmp / "no-such-root"),
                           str(self.tmp)]), 2)

    # L2 — a case-mismatched link passes exists() on APFS but 404s on GitHub.
    def test_case_mismatch_flagged(self):
        self._write("Target.md", "# H\n")
        self._write("doc.md", "# D\n[x](target.md)\n")
        fs = linkscan.scan_paths([self.tmp], self.tmp)
        self.assertEqual([f.kind for f in fs], ["missing-file"])

    # L3 — a link resolving above the scan root exists locally, 404s on GitHub.
    def test_link_escaping_root_flagged(self):
        (self.tmp / "outside.md").write_text("# O\n")
        repo = self.tmp / "repo"
        repo.mkdir()
        (repo / "doc.md").write_text("# D\n[x](../outside.md)\n")
        fs = linkscan.scan_paths([repo], repo)
        self.assertEqual([f.kind for f in fs], ["outside-root"])

    # L4 — GitHub fragment matching is exact; a wrong-case anchor is a break.
    def test_wrong_case_anchor_flagged_with_hint(self):
        self._write("doc.md", "# T\n## A Section\n[x](#A-Section)\n")
        fs = linkscan.scan_paths([self.tmp], self.tmp)
        self.assertEqual([f.kind for f in fs], ["missing-anchor"])
        self.assertIn("#a-section", fs[0].detail)

    def test_exact_anchor_still_passes(self):
        self._write("t.md", "# Real Heading\n")
        self._write("doc.md", "# D\n[x](t.md#real-heading)\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    # L4 — the slugger keeps literal underscores (GitHub does).
    def test_snake_case_heading_anchor(self):
        self._write("doc.md", "# T\n## snake_case name\n[x](#snake_case-name)\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_underscore_emphasis_unwrapped(self):
        self.assertEqual(linkscan.slugify("_Emph_ text"), "emph-text")

    # L5 — a destination with balanced parens is a legal filename.
    def test_paren_destination_resolves(self):
        self._write("a(1).md", "# H\n")
        self._write("doc.md", "# D\n[x](a(1).md)\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_paren_destination_missing_reports_full_dest(self):
        self._write("doc.md", "# D\n[x](gone(1).md)\n")
        fs = linkscan.scan_paths([self.tmp], self.tmp)
        self.assertEqual([(f.kind, f.target) for f in fs],
                         [("missing-file", "gone(1).md")])

    # L6 — setext headings mint real GitHub anchors.
    def test_setext_heading_anchor_resolves(self):
        self._write("t.md", "Real Setext Heading\n===================\n\nbody\n")
        self._write("doc.md", "# D\n[x](t.md#real-setext-heading)\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_divider_after_blank_is_not_a_heading(self):
        # the house `---` verdict divider (blank line above) mints no anchor
        slugs = linkscan.heading_slugs("# T\n\nprose\n\n---\n\nmore\n")
        self.assertEqual(slugs, {"t"})

    # L7 — fence tracking is length- and info-string-aware.
    def test_four_backtick_fence_keeps_inner_example_as_code(self):
        self._write("doc.md",
                    "# D\n\n````markdown\n```\n[example](fake.md)\n```\n````\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_info_string_line_does_not_close_a_fence(self):
        self._write("doc.md",
                    "# D\n\n```\n```python\n[example](fake.md)\n```\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_unclosed_fence_swallows_to_eof(self):
        # matches GitHub: an unclosed fence is code to end-of-file
        self._write("doc.md", "# D\n```\n[gone](missing.md)\n")
        self.assertEqual(linkscan.scan_paths([self.tmp], self.tmp), [])

    def test_real_break_after_closed_nested_fence_still_flags(self):
        self._write("doc.md",
                    "# D\n\n````\n```\n[ex](fake.md)\n```\n````\n\n[gone](missing.md)\n")
        fs = linkscan.scan_paths([self.tmp], self.tmp)
        self.assertEqual([(f.kind, f.target) for f in fs],
                         [("missing-file", "missing.md")])


if __name__ == "__main__":
    unittest.main()
