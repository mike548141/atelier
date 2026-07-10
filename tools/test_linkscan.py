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

    def test_selftest_passes(self):
        self.assertEqual(linkscan._selftest(), 0)


if __name__ == "__main__":
    unittest.main()
