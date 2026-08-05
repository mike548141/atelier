"""Stdlib-only tests for stampscan (no pytest needed): `python3 -m unittest`."""

import unittest

try:
    # `python3 -m unittest tools.test_stampscan` from the repo root — tools/
    # is a namespace package (no __init__.py needed), so this is a proper
    # package-relative import (matches datescan's DSR7 wart).
    from . import stampscan as ss
except ImportError:
    # `cd tools && python3 -m unittest test_stampscan` (or `discover -s
    # tools`, what CI uses) — no parent package in scope, so fall back to
    # the plain top-level import.
    import stampscan as ss


def _parent_text(region_lines, region="floor"):
    return ("# Parent\n\nSome prose above.\n\n"
            f"<!-- {region}:begin -->\n"
            + "\n".join(region_lines) + "\n"
            f"<!-- {region}:end -->\n\nSome prose below.\n")


def _child_text(payload_lines, source="docs/PARENT.md", region="floor",
                 narrow=None):
    attrs = f"source={source} region={region}"
    if narrow is not None:
        attrs += f" narrow={narrow}"
    return (f"<!-- stamp:begin {attrs} -->\n"
            + "\n".join(payload_lines) + "\n"
            "<!-- stamp:end -->\n")


def _write(tmp, rel, text):
    p = tmp / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


class ExtractRegion(unittest.TestCase):
    def test_extracts_lines_between_markers(self):
        text = _parent_text(["a", "b", "c"])
        self.assertEqual(["a", "b", "c"], ss.extract_region(text, "floor"))

    def test_missing_region_returns_none(self):
        text = _parent_text(["a", "b"], region="floor")
        self.assertIsNone(ss.extract_region(text, "other"))

    def test_missing_end_returns_none(self):
        text = "<!-- floor:begin -->\na\nb\n"
        self.assertIsNone(ss.extract_region(text, "floor"))

    def test_fenced_presentation_is_stripped(self):
        text = ("<!-- floor:begin -->\n"
                "```markdown\n"
                "a\nb\nc\n"
                "```\n"
                "<!-- floor:end -->\n")
        self.assertEqual(["a", "b", "c"], ss.extract_region(text, "floor"))

    def test_tilde_fence_is_stripped(self):
        text = ("<!-- floor:begin -->\n"
                "~~~\na\nb\n~~~\n"
                "<!-- floor:end -->\n")
        self.assertEqual(["a", "b"], ss.extract_region(text, "floor"))

    def test_no_fence_left_untouched(self):
        text = _parent_text(["a", "b"])
        self.assertEqual(["a", "b"], ss.extract_region(text, "floor"))


class FindStampBlocks(unittest.TestCase):
    def test_single_block(self):
        text = _child_text(["a", "b"])
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual([], malformed)
        self.assertEqual(1, len(blocks))
        self.assertEqual("docs/PARENT.md", blocks[0].source)
        self.assertEqual("floor", blocks[0].region)
        self.assertIsNone(blocks[0].narrow)
        self.assertEqual(["a", "b"], blocks[0].payload)

    def test_narrow_attribute_captured(self):
        text = _child_text(["a"], narrow="repo-specific-reason")
        blocks, _ = ss.find_stamp_blocks("t.md", text)
        self.assertEqual("repo-specific-reason", blocks[0].narrow)

    def test_unterminated_stamp_is_malformed(self):
        text = "<!-- stamp:begin source=x.md region=floor -->\na\nb\n"
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual([], blocks)
        self.assertEqual(1, len(malformed))
        self.assertEqual("malformed", malformed[0].kind)

    def test_nested_begin_is_malformed(self):
        text = ("<!-- stamp:begin source=x.md region=floor -->\n"
                "a\n"
                "<!-- stamp:begin source=y.md region=other -->\n"
                "b\n"
                "<!-- stamp:end -->\n")
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual(1, len(malformed))
        self.assertEqual(1, len(blocks))  # the second (innermost) closes cleanly

    def test_stray_end_is_malformed(self):
        text = "prose\n<!-- stamp:end -->\nmore prose\n"
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual([], blocks)
        self.assertEqual(1, len(malformed))

    def test_no_stamps_no_blocks_no_malformed(self):
        blocks, malformed = ss.find_stamp_blocks("t.md", "just prose\nnothing here\n")
        self.assertEqual([], blocks)
        self.assertEqual([], malformed)

    def test_allow_marker_on_begin_line(self):
        text = ("<!-- stamp:begin source=x.md region=floor -->"
                "  <!-- stampscan:allow: migrating -->\n"
                "a\n<!-- stamp:end -->\n")
        blocks, _ = ss.find_stamp_blocks("t.md", text)
        self.assertTrue(blocks[0].allow)

    def test_allow_marker_in_payload(self):
        text = ("<!-- stamp:begin source=x.md region=floor -->\n"
                "a  <!-- stampscan:allow: migrating -->\nb\n"
                "<!-- stamp:end -->\n")
        blocks, _ = ss.find_stamp_blocks("t.md", text)
        self.assertTrue(blocks[0].allow)

    def test_no_allow_marker_false(self):
        text = _child_text(["a", "b"])
        blocks, _ = ss.find_stamp_blocks("t.md", text)
        self.assertFalse(blocks[0].allow)


class OrderedSubsequence(unittest.TestCase):
    def test_equal_is_subsequence(self):
        self.assertTrue(ss._is_ordered_subsequence(["a", "b"], ["a", "b"]))

    def test_proper_subset_in_order(self):
        self.assertTrue(ss._is_ordered_subsequence(["a", "c"], ["a", "b", "c"]))

    def test_reordered_not_subsequence(self):
        self.assertFalse(ss._is_ordered_subsequence(["c", "a"], ["a", "b", "c"]))

    def test_extra_line_not_subsequence(self):
        self.assertFalse(ss._is_ordered_subsequence(["a", "x", "b"], ["a", "b"]))

    def test_empty_is_subsequence_of_anything(self):
        self.assertTrue(ss._is_ordered_subsequence([], ["a", "b"]))


class EvaluateBlock(unittest.TestCase):
    """The core disposition matrix: identical / legitimate-narrow /
    silent-drop / contradiction / allow-skip."""

    def _block(self, payload, narrow=None, allow=False):
        return ss.StampBlock(path="t.md", line=1, source="p.md",
                              region="floor", narrow=narrow,
                              payload=payload, allow=allow)

    def test_identical_is_clean(self):
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(self._block(["a", "b", "c"]), canonical)
        self.assertEqual("identical", f.kind)

    def test_trailing_whitespace_ignored_for_identical(self):
        canonical = ["a  ", "b"]
        f = ss.evaluate_block(self._block(["a", "b   "]), canonical)
        self.assertEqual("identical", f.kind)

    def test_legitimate_narrow_declared_subset(self):
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(
            self._block(["a", "c"], narrow="dropping-b-deliberately"),
            canonical)
        self.assertEqual("narrow", f.kind)

    def test_silent_drop_without_narrow_is_drift(self):
        # The exact same subset shape as the legitimate-narrow case above,
        # but with no narrow= declared — this is the load-bearing
        # distinction this scanner makes (see module header).
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(self._block(["a", "c"]), canonical)
        self.assertEqual("drift", f.kind)

    def test_contradiction_reworded_line_is_drift(self):
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(self._block(["a", "B REWORDED", "c"]), canonical)
        self.assertEqual("drift", f.kind)

    def test_contradiction_with_narrow_declared_still_drift(self):
        # Declaring narrow= does not excuse an actual addition/reword — only
        # a genuine ordered subset counts as "legitimate".
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(
            self._block(["a", "B REWORDED", "c"], narrow="anything"),
            canonical)
        self.assertEqual("drift", f.kind)

    def test_added_line_is_drift(self):
        canonical = ["a", "b"]
        f = ss.evaluate_block(self._block(["a", "b", "c"]), canonical)
        self.assertEqual("drift", f.kind)

    def test_reordered_lines_is_drift(self):
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(self._block(["c", "a", "b"]), canonical)
        self.assertEqual("drift", f.kind)

    def test_allow_marker_skips_regardless_of_content(self):
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(
            self._block(["x", "y", "z"], allow=True), canonical)
        self.assertEqual("skipped", f.kind)


class ScanPaths(unittest.TestCase):
    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ss.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_identical_pair_is_clean(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child.md", _child_text(["a", "b"]))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["identical"], [f.kind for f in findings])

    def test_missing_source_is_config_error(self):
        _write(self.tmp, "docs/child.md",
               _child_text(["a"], source="docs/NOPE.md"))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["missing-source"], [f.kind for f in findings])

    def test_missing_region_is_config_error(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a"], region="floor"))
        _write(self.tmp, "docs/child.md",
               _child_text(["a"], region="nonexistent"))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["missing-region"], [f.kind for f in findings])

    def test_ignorefile_exempts_path(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child.md", _child_text(["a"]))  # silent drop
        findings = ss.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(["drift"], [f.kind for f in findings])
        _write(self.tmp, ".stampscanignore", "# a reasoned fixture exemption\ndocs/child.md\n")
        findings = ss.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual([], findings)

    def test_non_markdown_files_skipped(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a"]))
        _write(self.tmp, "docs/child.txt", _child_text(["a", "b"]))
        findings = ss.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual([], findings)

    def test_multiple_stamps_same_source_cached_and_evaluated(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child1.md", _child_text(["a", "b"]))
        _write(self.tmp, "docs/child2.md", _child_text(["a"]))  # silent drop
        findings = ss.scan_paths([self.tmp / "docs"], self.tmp)
        kinds = sorted(f.kind for f in findings)
        self.assertEqual(["drift", "identical"], kinds)


class MainCli(unittest.TestCase):
    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ss.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _main(self, argv):
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            return ss.main(argv)

    def test_clean_scan_exits_zero(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child.md", _child_text(["a", "b"]))
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_drift_without_warn_exits_one(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child.md", _child_text(["a"]))  # silent drop
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_drift_with_warn_exits_zero(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child.md", _child_text(["a"]))  # silent drop
        self.assertEqual(
            0, self._main(["--warn", "--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_config_error_exits_two_without_warn(self):
        _write(self.tmp, "docs/child.md",
               _child_text(["a"], source="docs/NOPE.md"))
        self.assertEqual(
            2, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_config_error_exits_two_even_with_warn(self):
        # The fail-safe property under test: --warn must NEVER downgrade a
        # config error (a broken scan is not a pass).
        _write(self.tmp, "docs/child.md",
               _child_text(["a"], source="docs/NOPE.md"))
        self.assertEqual(
            2, self._main(["--warn", "--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_nonexistent_scan_path_is_config_error(self):
        self.assertEqual(
            2, self._main(["--root", str(self.tmp), str(self.tmp / "gone")]))

    def test_nonexistent_root_is_config_error(self):
        self.assertEqual(
            2, self._main(["--root", str(self.tmp / "gone-root")]))

    def test_no_stamps_found_is_clean(self):
        _write(self.tmp, "docs/note.md", "just ordinary prose\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_json_output_is_valid(self):
        import contextlib
        import io
        import json as json_mod
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child.md", _child_text(["a", "b"]))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = ss.main(["--json", "--root", str(self.tmp), str(self.tmp / "docs")])
        self.assertEqual(0, code)
        data = json_mod.loads(buf.getvalue())
        self.assertTrue(data["clean"])
        self.assertEqual(1, len(data["findings"]))

    def test_defaults_to_docs_subdir(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child.md", _child_text(["a"]))  # silent drop, inside docs
        _write(self.tmp, "README.md",
               _child_text(["x"], source="docs/PARENT.md"))  # outside docs, must be ignored by default scope
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ss._selftest())


if __name__ == "__main__":
    unittest.main()
