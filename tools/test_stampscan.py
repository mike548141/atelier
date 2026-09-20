"""Stdlib-only tests for stampscan (no pytest needed): `python3 -m unittest`."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

try:
    from . import memprobe
except ImportError:
    import memprobe

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


class CodeContextBlindness(unittest.TestCase):
    """2026-07-26 cold pass ST1/ST7 — the wiring blocker. A document that
    merely DOCUMENTS the marker syntax is not a stamp. Markers are recognised
    only outside fenced code blocks and outside inline `code spans`, and both
    markers are anchored at line start."""

    def test_fenced_marker_pair_is_not_a_stamp(self):
        text = ("# How stamps work\n\n"
                "```markdown\n"
                "<!-- stamp:begin source=docs/PARENT.md region=floor -->\n"
                "...the inlined block...\n"
                "<!-- stamp:end -->\n"
                "```\n")
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual([], blocks)
        self.assertEqual([], malformed)

    def test_tilde_fenced_marker_pair_is_not_a_stamp(self):
        text = ("~~~\n"
                "<!-- stamp:begin source=x.md region=floor -->\n"
                "<!-- stamp:end -->\n"
                "~~~\n")
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual([], blocks)
        self.assertEqual([], malformed)

    def test_inline_code_mention_of_end_marker_is_not_a_stray_end(self):
        """The exact shape that reddened the floor: a brief writing
        `` `<!-- stamp:end -->` `` in prose used to read as a stray end."""
        text = "The closer is `<!-- stamp:end -->`, written on its own line.\n"
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual([], blocks)
        self.assertEqual([], malformed)

    def test_inline_code_mention_of_begin_marker_is_not_a_stamp(self):
        text = "Open with `<!-- stamp:begin source=x region=y -->` at line start.\n"
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual([], blocks)
        self.assertEqual([], malformed)

    def test_end_marker_is_anchored_at_line_start(self):
        """ST7: an end marker trailing other content no longer closes a
        stamp — the compromise that forced the unanchored regex is gone."""
        text = ("<!-- stamp:begin source=x.md region=floor -->\n"
                "a\n"
                "---<!-- stamp:end -->\n")
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual([], blocks)
        self.assertEqual(1, len(malformed))
        self.assertIn("never closed", malformed[0].detail)

    def test_stripped_lines_still_enter_the_payload_verbatim(self):
        """Recognition-only: a payload line carrying a code span or a whole
        fenced example is compared character for character, unchanged."""
        text = ("<!-- stamp:begin source=x.md region=floor -->\n"
                "run `python3 tools/floor.py --plane ci`\n"
                "```sh\n"
                "echo hi\n"
                "```\n"
                "<!-- stamp:end -->\n")
        blocks, malformed = ss.find_stamp_blocks("t.md", text)
        self.assertEqual([], malformed)
        self.assertEqual(
            ["run `python3 tools/floor.py --plane ci`",
             "```sh", "echo hi", "```"],
            blocks[0].payload)

    def test_documented_syntax_in_a_real_scan_is_clean(self):
        import shutil
        import tempfile
        tmp = ss.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        _write(tmp, "docs/about.md",
               "Wrap the block in `<!-- stamp:begin ... -->` and "
               "`<!-- stamp:end -->`.\n\n"
               "```markdown\n"
               "<!-- stamp:begin source=docs/GONE.md region=floor -->\n"
               "<!-- stamp:end -->\n"
               "```\n")
        self.assertEqual([], ss.scan_paths([tmp / "docs"], tmp))


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

    def test_empty_payload_with_narrow_is_drift(self):
        """ST2, ruled 2026-08-04: narrowing to NOTHING is not a narrowing —
        one token must not vacate a whole inlined floor and report clean."""
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(
            self._block([], narrow="we-dropped-everything"), canonical)
        self.assertEqual("drift", f.kind)
        self.assertIn("0 of 3", f.detail)

    def test_empty_payload_without_narrow_is_drift(self):
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(self._block([]), canonical)
        self.assertEqual("drift", f.kind)

    def test_blank_only_payload_with_narrow_is_drift(self):
        """The boundary is what SURVIVES normalisation — a payload of blank
        lines trims to empty and must not slip past as a narrow."""
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(self._block(["", "   ", ""], narrow="x"),
                              canonical)
        self.assertEqual("drift", f.kind)

    def test_genuine_partial_narrow_still_passes(self):
        """The other direction of ST2: keeping ONE canonical line, in order,
        with a declared reason, is still a legitimate narrow."""
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(self._block(["b"], narrow="only-b-applies-here"),
                              canonical)
        self.assertEqual("narrow", f.kind)
        self.assertIn("1 of 3", f.detail)

    def test_empty_child_against_empty_canonical_is_identical(self):
        """An empty canonical region genuinely has nothing to keep — that is
        equality, not a vacated floor."""
        f = ss.evaluate_block(self._block([], narrow="x"), [])
        self.assertEqual("identical", f.kind)

    def test_allow_marker_skips_regardless_of_content(self):
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(
            self._block(["x", "y", "z"], allow=True), canonical)
        self.assertEqual("skipped", f.kind)


class FloorIsVerbatim(unittest.TestCase):
    """Board 115/030, ruled 2026-09-19: "Floor copy verbatim." The one
    canonical (source, region) pair — docs/method/PROPAGATION.md's `floor`
    region — carries no legitimate narrowing at all: `narrow=` on a genuine
    ordered subset reds there exactly like an undeclared silent drop.
    Non-floor regions (including ones merely NAMED "floor", as the rest of
    this test suite's fixtures are) are unaffected."""

    def _floor_block(self, payload, narrow=None):
        return ss.StampBlock(path="t.md", line=1, source=ss.FLOOR_SOURCE,
                              region=ss.FLOOR_REGION, narrow=narrow,
                              payload=payload, allow=False)

    def test_floor_narrow_declared_subset_is_drift(self):
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(
            self._floor_block(["a", "c"], narrow="dropping-b-deliberately"),
            canonical)
        self.assertEqual("drift", f.kind)
        self.assertIn("narrow=", f.detail)
        self.assertIn("verbatim", f.detail)

    def test_floor_verbatim_copy_is_identical(self):
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(self._floor_block(["a", "b", "c"]), canonical)
        self.assertEqual("identical", f.kind)

    def test_floor_compressed_without_narrow_is_drift(self):
        """A silent drop on the floor was already red before this change —
        confirm it still is."""
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(self._floor_block(["a", "c"]), canonical)
        self.assertEqual("drift", f.kind)

    def test_floor_reworded_line_is_drift_regardless_of_narrow(self):
        """A genuine reword/compression (not an ordered subsequence) was
        already red before this change — confirm it still is, narrow= or
        not."""
        canonical = ["a", "b", "c"]
        f = ss.evaluate_block(
            self._floor_block(["a", "b, compressed", "c"], narrow="x"),
            canonical)
        self.assertEqual("drift", f.kind)

    def test_floor_identified_by_pair_not_region_name_alone(self):
        """A block merely NAMED region="floor" but pointing at an unrelated
        source is not the atelier safety floor — today's narrow= pass
        behaviour is unaffected. (This is what every other fixture in this
        file already relies on: they default to region="floor" as a generic
        example name, unconnected to PROPAGATION.md.)"""
        canonical = ["a", "b", "c"]
        block = ss.StampBlock(path="t.md", line=1, source="docs/PARENT.md",
                              region="floor", narrow="dropping-b-deliberately",
                              payload=["a", "c"], allow=False)
        self.assertFalse(ss._is_floor_block(block))
        f = ss.evaluate_block(block, canonical)
        self.assertEqual("narrow", f.kind)

    def test_floor_identified_by_pair_not_source_alone(self):
        """Conversely, the right source with a DIFFERENT region name is not
        the floor either — the pair, not either half alone, is the key."""
        block = ss.StampBlock(path="t.md", line=1, source=ss.FLOOR_SOURCE,
                              region="other-region", narrow="x",
                              payload=["a", "c"], allow=False)
        self.assertFalse(ss._is_floor_block(block))
        f = ss.evaluate_block(block, ["a", "b", "c"])
        self.assertEqual("narrow", f.kind)


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

    def test_traversal_source_is_a_config_error(self):
        """ST4: `root / source` accepts `../`. A stamp may only point at a
        file inside the scanned tree."""
        outside = self.tmp.parent / f"{self.tmp.name}-outside"
        outside.mkdir()
        self.addCleanup(lambda: __import__("shutil").rmtree(
            outside, ignore_errors=True))
        (outside / "SECRET.md").write_text(_parent_text(["TOP-SECRET-LINE"]))
        _write(self.tmp, "docs/child.md",
               _child_text(["x"], source=f"../{outside.name}/SECRET.md"))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["unconfined-source"], [f.kind for f in findings])
        # And nothing from the out-of-root file is echoed back.
        self.assertNotIn("TOP-SECRET-LINE", findings[0].detail)

    def test_absolute_source_is_a_config_error(self):
        """pathlib silently DISCARDS the root for an absolute right-hand
        side, so this escaped without ever looking like traversal."""
        outside = self.tmp.parent / f"{self.tmp.name}-abs"
        outside.mkdir()
        self.addCleanup(lambda: __import__("shutil").rmtree(
            outside, ignore_errors=True))
        (outside / "SECRET.md").write_text(_parent_text(["a"]))
        _write(self.tmp, "docs/child.md",
               _child_text(["a"], source=str(outside / "SECRET.md")))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["unconfined-source"], [f.kind for f in findings])

    def test_in_root_source_still_resolves(self):
        """The confinement check must not break the ordinary case, including
        a source reached by a path with a `..` segment that stays inside."""
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child.md",
               _child_text(["a", "b"], source="docs/sub/../PARENT.md"))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["identical"], [f.kind for f in findings])

    def test_multiple_stamps_same_source_cached_and_evaluated(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child1.md", _child_text(["a", "b"]))
        _write(self.tmp, "docs/child2.md", _child_text(["a"]))  # silent drop
        findings = ss.scan_paths([self.tmp / "docs"], self.tmp)
        kinds = sorted(f.kind for f in findings)
        self.assertEqual(["drift", "identical"], kinds)

    def test_real_floor_pair_with_narrow_reds_end_to_end(self):
        """The full scan_paths path (source resolution + region extraction),
        not just evaluate_block in isolation, against the real
        docs/method/PROPAGATION.md path stampscan resolves in production."""
        _write(self.tmp, "docs/method/PROPAGATION.md", _parent_text(["a", "b", "c"]))
        _write(self.tmp, "docs/child.md",
               _child_text(["a", "c"], source="docs/method/PROPAGATION.md",
                           narrow="dropping-b"))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["drift"], [f.kind for f in findings])

    def test_real_floor_pair_verbatim_is_clean_end_to_end(self):
        _write(self.tmp, "docs/method/PROPAGATION.md", _parent_text(["a", "b", "c"]))
        _write(self.tmp, "docs/child.md",
               _child_text(["a", "b", "c"], source="docs/method/PROPAGATION.md"))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["identical"], [f.kind for f in findings])


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

    def test_unconfined_source_exits_two_even_with_warn(self):
        outside = self.tmp.parent / f"{self.tmp.name}-cli"
        outside.mkdir()
        self.addCleanup(lambda: __import__("shutil").rmtree(
            outside, ignore_errors=True))
        (outside / "SECRET.md").write_text(_parent_text(["a"]))
        _write(self.tmp, "docs/child.md",
               _child_text(["a"], source=f"../{outside.name}/SECRET.md"))
        self.assertEqual(
            2, self._main(["--warn", "--root", str(self.tmp),
                           str(self.tmp / "docs")]))

    def test_empty_narrow_drift_exits_one_without_warn(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(self.tmp, "docs/child.md",
               _child_text([], narrow="dropped-the-lot"))
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

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


class RenderHuman(unittest.TestCase):
    def _note(self, path, kind="identical"):
        return ss.Finding(path, 1, kind, "p.md", "floor", "detail")

    def test_note_kinds_are_de_duplicated(self):
        """ST6c: the summary names WHICH dispositions occurred, not one
        repeat per block — 'identical, identical, identical' was noise."""
        out = ss.render_human([self._note("a.md"), self._note("b.md"),
                               self._note("c.md")])
        self.assertIn("(3 note(s): identical)", out)

    def test_distinct_note_kinds_all_named(self):
        out = ss.render_human([self._note("a.md", "identical"),
                               self._note("b.md", "narrow"),
                               self._note("c.md", "narrow")])
        self.assertIn("(3 note(s): identical, narrow)", out)


class CanonicalSideCodeContext(unittest.TestCase):
    """SD1 (ruled 2026-08-06): region extraction reads the same code-stripped
    view the stamp-marker hunt does. A fenced EXAMPLE of the region markers
    above the real region used to bind first — an identical copy then read
    as drift against the example's text."""

    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ss.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_fenced_example_above_real_region_does_not_bind(self):
        _write(self.tmp, "docs/PARENT.md",
               "# Parent\n\nHow to mark a region:\n\n"
               "```markdown\n"
               "<!-- floor:begin -->\nEXAMPLE TEXT ONLY\n<!-- floor:end -->\n"
               "```\n\nThe real region:\n\n"
               "<!-- floor:begin -->\n- real one\n- real two\n<!-- floor:end -->\n")
        _write(self.tmp, "docs/child.md", _child_text(["- real one", "- real two"]))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["identical"], [f.kind for f in findings])

    def test_inline_code_mention_of_region_marker_does_not_bind(self):
        _write(self.tmp, "docs/PARENT.md",
               "The pair is `<!-- floor:begin -->` and `<!-- floor:end -->`.\n\n"
               "<!-- floor:begin -->\n- real one\n<!-- floor:end -->\n")
        _write(self.tmp, "docs/child.md", _child_text(["- real one"]))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["identical"], [f.kind for f in findings])

    def test_region_only_inside_a_fence_is_missing(self):
        # The must-fail direction: markers that exist ONLY as a fenced
        # example resolve nothing — fail-safe config error, not a match
        # against example text.
        _write(self.tmp, "docs/PARENT.md",
               "```markdown\n"
               "<!-- floor:begin -->\nEXAMPLE\n<!-- floor:end -->\n"
               "```\n")
        _write(self.tmp, "docs/child.md", _child_text(["EXAMPLE"]))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["missing-region"], [f.kind for f in findings])

    def test_fenced_presentation_of_region_content_still_extracts(self):
        # The live PROPAGATION.md shape must keep working: markers outside a
        # fence, content inside it — the fence is presentational and
        # stripped, the content extracts verbatim.
        _write(self.tmp, "docs/PARENT.md",
               "<!-- floor:begin -->\n```\n- real one\n- real two\n```\n"
               "<!-- floor:end -->\n")
        _write(self.tmp, "docs/child.md", _child_text(["- real one", "- real two"]))
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["identical"], [f.kind for f in findings])


class NarrowReason(unittest.TestCase):
    """SD4 (ruled 2026-08-06): a whitespace-only `narrow=` is not a
    declaration."""

    def test_whitespace_only_narrow_is_not_a_declaration(self):
        m = ss._STAMP_BEGIN_RX.match(
            "<!-- stamp:begin source=docs/P.md region=floor narrow= -->")
        self.assertIsNotNone(m)          # the marker still parses…
        self.assertIsNone(ss._narrow_of(m))  # …the declaration is void

    def test_real_narrow_reason_still_parses(self):
        m = ss._STAMP_BEGIN_RX.match(
            "<!-- stamp:begin source=docs/P.md region=floor narrow=repo-x omits it -->")
        self.assertEqual("repo-x omits it", ss._narrow_of(m))

    def test_whitespace_narrow_subset_reds_as_silent_drop(self):
        import shutil
        import tempfile
        tmp = ss.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        _write(tmp, "docs/PARENT.md", _parent_text(["a", "b"]))
        _write(tmp, "docs/child.md",
               "<!-- stamp:begin source=docs/PARENT.md region=floor narrow= -->\n"
               "a\n<!-- stamp:end -->\n")
        findings = ss.scan_paths([tmp / "docs" / "child.md"], tmp)
        self.assertEqual(["drift"], [f.kind for f in findings])


class SuppressionTally(unittest.TestCase):
    """SD3 (ruled 2026-08-06): rule (b) — known zeros printed, and files
    skipped wholesale by `.stampscanignore` are counted, not silent."""

    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ss.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_clean_output_prints_known_zeros(self):
        out = ss.render_human([])
        self.assertIn("suppressed: 0 block(s) by allow-marker", out)
        self.assertIn("0 file(s) by .stampscanignore", out)

    def test_ignore_glob_skips_are_counted(self):
        (self.tmp / ".stampscanignore").write_text(
            "# probe store, quotes markers raw\ndocs/reviews/\n")
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a"]))
        _write(self.tmp, "docs/reviews/raw.md", _child_text(["ghost"]))
        _write(self.tmp, "docs/child.md", _child_text(["a"]))
        skipped: list[int] = []
        findings = ss.scan_paths([self.tmp / "docs"], self.tmp, skipped)
        self.assertEqual(["identical"], [f.kind for f in findings])
        self.assertEqual(1, len(skipped))
        out = ss.render_human(findings, len(skipped))
        self.assertIn("1 file(s) by .stampscanignore", out)

    def test_allow_skipped_blocks_are_counted(self):
        _write(self.tmp, "docs/PARENT.md", _parent_text(["a"]))
        _write(self.tmp, "docs/child.md",
               "<!-- stamp:begin source=docs/PARENT.md region=floor -->\n"
               "ghost\n<!-- stampscan:allow: probe fixture -->\n"
               "<!-- stamp:end -->\n")
        findings = ss.scan_paths([self.tmp / "docs" / "child.md"], self.tmp)
        self.assertEqual(["skipped"], [f.kind for f in findings])
        self.assertIn("suppressed: 1 block(s) by allow-marker",
                      ss.render_human(findings))


class BoundedMemory(unittest.TestCase):
    """020/380 — extending 020/370's ruling to stampscan. Mike's ruling,
    verbatim: "it should not matter how much it scans it should no have this
    affect". Measured BEFORE this fix (see the board item's own before/after
    table): a whole `md.read_text()` per candidate file, immediately re-split
    via `text.splitlines()` inside `_content_lines`, drove ~29 MB of peak-RSS
    growth for a 7 MB larger many-line docs file, and a SINGLE 8 MB line grew
    peak RSS 3.6x over its 1 MB twin (112 MB vs 31 MB) — the same
    double-materialization shape secretscan's/spellscan's `020/370`/`020/380`
    fixes removed. The file walk itself was also the old `rglob("*")` funnelled
    through a list comprehension (`iter_markdown`), forcing the ENTIRE subtree
    to be enumerated and held before a single file was scanned.

    Runs the real CLI as a SUBPROCESS via `memprobe.run_and_measure` and reads
    peak RSS back from the kernel — see `tools/memprobe.py`. Content is plain
    filler prose (or ordinary stamped-block drift, for the many-findings case)
    with no config errors, so growth is attributable to input size alone."""

    STAMPSCAN = str(Path(ss.__file__).resolve())
    SMALL_BYTES = 1 * 1024 * 1024
    LARGE_BYTES = 8 * 1024 * 1024
    # Grounded in the fix's design (`stampscan._MAX_LINE_BYTES` plus one read
    # chunk in flight), not fitted to a measurement — matching every sibling
    # scanner's identical-shape bound (spellscan/sizescan's own
    # `8 * (1 MiB + 8 KiB)`).
    GROWTH_BOUND_BYTES = 8 * (1 * 1024 * 1024 + 8 * 1024)

    def _run(self, root: Path, *extra: str) -> "memprobe.ProbeResult":
        return memprobe.run_and_measure(
            [sys.executable, self.STAMPSCAN, "--root", str(root),
             str(root / "docs"), *extra],
            timeout=90, rss_limit_bytes=900 * 1024 * 1024)

    def _tmp_docs(self) -> Path:
        tmp = Path(tempfile.mkdtemp(prefix="stampscan-mem-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        (tmp / "docs").mkdir()
        return tmp

    def _peak_for_many_line(self, size_bytes: int) -> int:
        tmp = self._tmp_docs()
        with open(tmp / "docs" / "note.md", "w") as f:
            written = 0
            i = 0
            while written < size_bytes:
                line = f"this is filler prose line number {i} nothing here\n"
                f.write(line)
                written += len(line)
                i += 1
        r = self._run(tmp)
        self.assertFalse(r.timed_out, "scan did not finish in time")
        self.assertFalse(r.killed_over_limit, "scan exceeded the safety limit")
        self.assertEqual(0, r.returncode, "filler content must not flag anything")
        return r.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_many_line_file_size(self):
        small_peak = self._peak_for_many_line(self.SMALL_BYTES)
        large_peak = self._peak_for_many_line(self.LARGE_BYTES)
        growth = large_peak - small_peak
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for a "
            f"{(self.LARGE_BYTES - self.SMALL_BYTES) / 1e6:.1f} MB larger "
            f"many-line file (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB) — memory is scaling with "
            "input size again (020/370's class).")

    def _peak_for_one_huge_line(self, size_bytes: int) -> int:
        tmp = self._tmp_docs()
        (tmp / "docs" / "note.md").write_text("x" * size_bytes + "\n")
        r = self._run(tmp)
        self.assertFalse(r.timed_out, "scan did not finish in time")
        self.assertFalse(r.killed_over_limit, "scan exceeded the safety limit")
        self.assertEqual(0, r.returncode)
        return r.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_one_huge_line(self):
        small_peak = self._peak_for_one_huge_line(self.SMALL_BYTES)
        large_peak = self._peak_for_one_huge_line(self.LARGE_BYTES)
        growth = large_peak - small_peak
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for a single physical "
            f"line growing from {self.SMALL_BYTES / 1e6:.1f} MB to "
            f"{self.LARGE_BYTES / 1e6:.1f} MB (small={small_peak / 1e6:.1f} "
            f"MB, large={large_peak / 1e6:.1f} MB) — a pathological one-line "
            "file must be bounded by `_MAX_LINE_BYTES`, not scale with the "
            "line's own length.")

    def test_peak_memory_does_not_scale_with_file_count(self):
        """The old `rglob("*")` list comprehension enumerated (and held) the
        ENTIRE subtree before scanning a single file — this proves the
        `_walk_files` fix streams the walk instead."""
        def peak_for(n: int) -> int:
            tmp = self._tmp_docs()
            for i in range(n):
                (tmp / "docs" / f"f{i}.md").write_text(
                    f"# doc {i}\n\nsome prose here.\n")
            r = self._run(tmp)
            self.assertFalse(r.timed_out)
            self.assertFalse(r.killed_over_limit)
            self.assertEqual(0, r.returncode)
            return r.peak_rss_bytes

        small_peak = peak_for(200)
        large_peak = peak_for(2000)
        growth = large_peak - small_peak
        # 1800 extra `Path` objects and tiny file reads cost a few KB each at
        # most — generous headroom over what even an un-pruned walk's list of
        # Path objects would cost, while still catching a real per-file leak.
        self.assertLess(
            growth, 20 * 1024 * 1024,
            f"peak RSS grew {growth / 1e6:.1f} MB for 1800 more small files "
            f"(small={small_peak / 1e6:.1f} MB, large={large_peak / 1e6:.1f} "
            "MB) — the file count is scaling memory, not just I/O.")

    def test_peak_memory_does_not_scale_with_finding_count(self):
        """A tree of many drifting stamped blocks — many findings held at
        once, none of them individually large."""
        def peak_for(n: int) -> int:
            tmp = self._tmp_docs()
            (tmp / "docs" / "PARENT.md").write_text(
                "# Parent\n\n<!-- floor:begin -->\n- item one\n- item two\n"
                "- item three\n<!-- floor:end -->\n")
            for i in range(n):
                (tmp / "docs" / f"child{i}.md").write_text(
                    "<!-- stamp:begin source=docs/PARENT.md region=floor -->\n"
                    "- item one\n- item DIFFERENT\n- item three\n"
                    "<!-- stamp:end -->\n")
            r = self._run(tmp, "--warn")
            self.assertFalse(r.timed_out)
            self.assertFalse(r.killed_over_limit)
            self.assertEqual(0, r.returncode)
            return r.peak_rss_bytes

        small_peak = peak_for(200)
        large_peak = peak_for(2000)
        growth = large_peak - small_peak
        self.assertLess(
            growth, 20 * 1024 * 1024,
            f"peak RSS grew {growth / 1e6:.1f} MB for 1800 more drift "
            f"findings (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB).")


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ss._selftest())


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
                for p in ss._walk_files(self.tmp)}

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
