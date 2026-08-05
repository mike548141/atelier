"""Stdlib-only tests for pathscan (no pytest needed): `python3 -m unittest`."""

import unittest

try:
    # `python3 -m unittest tools.test_pathscan` from the repo root — tools/
    # is a namespace package (no __init__.py needed), so this is a proper
    # package-relative import.
    from . import pathscan as ps
except ImportError:
    # `cd tools && python3 -m unittest test_pathscan` (what CI uses) — no
    # parent package in scope, fall back to the plain top-level import.
    import pathscan as ps


def cand(line):
    return list(ps.iter_candidates(line))


class CandidateDetection(unittest.TestCase):
    def test_known_top_dir_prefix_is_candidate(self):
        self.assertIn("docs/method/00-APEX.md", cand("see docs/method/00-APEX.md"))

    def test_known_extension_suffix_is_candidate_without_top_dir(self):
        self.assertIn("some/other/thing.py", cand("see some/other/thing.py"))

    def test_backtick_wrapped_path_is_candidate(self):
        self.assertIn("tools/pathscan.py", cand("see `tools/pathscan.py` here"))

    def test_no_slash_never_a_candidate(self):
        # A single-segment mention (no directory) never matches — the token
        # regex requires at least one '/', a deliberate floor against
        # flagging every dotted abbreviation/version as a "path".
        self.assertEqual([], cand("see LICENSE and CLAUDE.md and v1.2.3"))

    def test_fraction_not_a_candidate(self):
        self.assertEqual([], cand("reduced scope by 3/4 of the work"))

    def test_unrelated_slashed_prose_without_cue_not_a_candidate(self):
        # Neither a known top-dir prefix nor a known extension suffix.
        self.assertEqual([], cand("this/that is not a path we recognise"))

    def test_trailing_sentence_period_trimmed(self):
        self.assertIn("tools/pathscan.py", cand("See `tools/pathscan.py`."))

    def test_double_trailing_dot_left_alone(self):
        got = cand("a stray docs/x.md..")
        self.assertTrue(got == [] or got[0] != "docs/x.md")


class GlobExemption(unittest.TestCase):
    def test_glob_star_exempt(self):
        self.assertEqual([], cand("try `src/**/*.go` as an example"))

    def test_glob_question_mark_exempt(self):
        self.assertEqual([], cand("docs/method/ch?.md is a glob-ish example"))

    def test_wildcard_does_not_split_the_token(self):
        # Regression: the lookbehind must exclude `*`/`?` too, not just
        # \w/./ — otherwise a match can spuriously START right after the
        # wildcard, splitting e.g. `toolu_*.txt/.json` into a truncated
        # `.txt/.json` candidate that then dodges the glob-placeholder
        # filter entirely (found live on this repo's own baseline run).
        got = cand("older `<uuid>/toolu_*.txt/.json` files")
        self.assertNotIn(".txt/.json", got)
        self.assertEqual([], got)


class EllipsisExemption(unittest.TestCase):
    def test_unicode_ellipsis_exempt(self):
        self.assertEqual([], cand("see `docs/reviews/2026-07-10-…` for detail"))

    def test_ascii_ellipsis_exempt(self):
        self.assertEqual([], cand("see `docs/reviews/2026-07-10-...` for detail"))

    def test_no_ellipsis_still_a_candidate(self):
        self.assertIn("docs/reviews/2026-07-10-atelier-foundation.md",
                     cand("see `docs/reviews/2026-07-10-atelier-foundation.md`"))


class PathToThingExemption(unittest.TestCase):
    def test_path_to_thing_exempt(self):
        self.assertEqual([], cand("copy from `path/to/thing.md` as a placeholder"))

    def test_path_to_thing_case_insensitive(self):
        self.assertEqual([], cand("copy from `Path/To/Thing.md` as a placeholder"))


class AngleBracketExemption(unittest.TestCase):
    def test_angle_bracket_placeholder_exempt(self):
        self.assertEqual([], cand("see <repo>/docs/foo.md for the pattern"))

    def test_bare_angle_bracket_alone_exempt(self):
        # The <name> placeholder itself never becomes a candidate (no slash
        # inside it); a real path elsewhere on the same line still is.
        self.assertEqual(
            ["docs/method/00-APEX.md"],
            cand("fill in <name> then docs/method/00-APEX.md"))


class UrlExemption(unittest.TestCase):
    def test_https_url_exempt(self):
        self.assertEqual([], cand("see https://example.com/tools/real.py here"))

    def test_mailto_exempt(self):
        self.assertEqual([], cand("mailto:someone/docs/x.md is not a path"))

    def test_protocol_relative_exempt(self):
        self.assertEqual([], cand("see //example.com/docs/x.md here"))


class MarkdownLinkDestinationSkipped(unittest.TestCase):
    def test_link_destination_not_a_candidate(self):
        # This is linkscan's job — pathscan must not re-check it.
        self.assertEqual([], cand("a [broken link](tools/also-ghost.py) here"))

    def test_link_text_still_scanned(self):
        # The visible link TEXT, if backtick-wrapped, is still in scope.
        got = cand("[see `tools/pathscan.py`](tools/pathscan.py)")
        self.assertEqual(["tools/pathscan.py"], got)


class FencedCodeExemption(unittest.TestCase):
    def test_fenced_block_skipped_wholesale(self):
        text = "prose\n```\n`tools/ghost.py` inside a fenced example\n```\nmore\n"
        findings = ps.scan_text(ps.Path("/nonexistent-root-xyz/t.md"), ps.Path("/nonexistent-root-xyz"), text)
        self.assertEqual([], findings)


class StubExemption(unittest.TestCase):
    """The stub cue (TODO / "(none yet)") is a LINE-level exemption applied
    in scan_text, not a per-candidate filter — iter_candidates() alone still
    yields the token; the line as a whole is skipped before that even runs."""

    def _findings(self, text):
        return ps.scan_text(ps.Path("/nonexistent-root-xyz/t.md"), ps.Path("/nonexistent-root-xyz"), text)

    def test_todo_cue_exempts_line(self):
        self.assertEqual(
            [], self._findings("`docs/future/plan.md` is not built yet <!-- TODO -->\n"))

    def test_none_yet_cue_exempts_line(self):
        self.assertEqual(
            [], self._findings("`docs/future/plan.md` is a stub (none yet)\n"))

    def test_none_yet_case_insensitive(self):
        self.assertEqual(
            [], self._findings("`docs/future/plan.md` is a stub (None Yet)\n"))

    def test_cue_on_other_line_does_not_exempt(self):
        # Narrowed to the SAME line only — a stated, deliberate limit.
        text = ("`docs/future/plan.md` is coming.\n"
                "(none yet) — see the line above.\n")
        findings = ps.scan_text(ps.Path("/nonexistent-root-xyz/t.md"), ps.Path("/nonexistent-root-xyz"), text)
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/future/plan.md", findings[0].target)


class AllowMarker(unittest.TestCase):
    def test_allow_marker_with_reason_exempts_line(self):
        text = "`tools/ghost.py` is fine <!-- pathscan:allow: intentional example -->\n"
        findings = ps.scan_text(ps.Path("/nonexistent-root-xyz/t.md"), ps.Path("/nonexistent-root-xyz"), text)
        self.assertEqual([], findings)

    def test_empty_reason_not_exempt(self):
        text = "`tools/ghost.py` <!-- pathscan:allow -->\n"
        findings = ps.scan_text(ps.Path("/nonexistent-root-xyz/t.md"), ps.Path("/nonexistent-root-xyz"), text)
        self.assertEqual(1, len(findings))

    def test_mere_mention_of_marker_not_exempt(self):
        text = "we discussed the pathscan:allow marker; see `tools/ghost.py`\n"
        findings = ps.scan_text(ps.Path("/nonexistent-root-xyz/t.md"), ps.Path("/nonexistent-root-xyz"), text)
        self.assertEqual(1, len(findings))

    def test_marker_requires_word_boundary(self):
        text = "xpathscan:allow: reason `tools/ghost.py`\n"
        findings = ps.scan_text(ps.Path("/nonexistent-root-xyz/t.md"), ps.Path("/nonexistent-root-xyz"), text)
        self.assertEqual(1, len(findings))


class DualResolution(unittest.TestCase):
    """A bare-prose path resolves if it exists under ANY of three anchors —
    the scan root, the linking file's own directory, or its nearest
    enclosing docs/ directory (module docstring, THE CHECK step 5) — found
    necessary by running this scanner over atelier's own corpus:
    docs/build/REPO-STANDARD.md routinely drops the `docs/` prefix and
    writes `method/RECORD.md`, meaning `docs/method/RECORD.md` — NOT
    sibling-relative to its own directory (docs/build/), which has no
    method/ child — while README.md at the repo root writes the same
    target root-relative as `docs/method/RECORD.md`. All three anchors
    must be tried."""

    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ps.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def test_resolves_root_relative_from_nested_doc(self):
        self._write("tools/real.py", "# real\n")
        self._write("docs/sub/note.md", "see `tools/real.py` from a nested doc\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual([], findings)

    def test_resolves_directory_relative_when_prefix_dropped(self):
        # The corpus-observed shape: a doc INSIDE docs/ names a sibling path
        # without repeating the docs/ prefix. Root-relative alone would
        # falsely flag this; the directory-relative fallback is what saves it.
        self._write("docs/other/thing.md", "# thing\n")
        self._write("docs/note.md", "see `other/thing.md` from its sibling\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual([], findings)

    def test_resolves_via_nearest_docs_ancestor_when_nested_deep(self):
        # The DOMINANT real-corpus shape: a file two levels under docs/
        # (docs/deep/sub/) still writes `method/far.md` meaning
        # `docs/method/far.md` — not relative to ITS OWN directory
        # (docs/deep/sub/, which has no method/ child).
        self._write("docs/method/far.md", "# far\n")
        self._write("docs/deep/sub/note.md", "see `method/far.md` from deep down\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual([], findings)

    def test_uses_outermost_docs_ancestor_not_nearest(self):
        # Found live on atelier's own corpus: docs/build/templates/docs/ is
        # itself a nested dir literally named "docs" (repo-craft scaffolding
        # that mimics a CHILD repo's docs/ folder). A file under it has TWO
        # ancestors named "docs" — the OUTER (real) one is the correct
        # anchor, not the inner (templated) one, which has no method/ child.
        self._write("docs/method/far.md", "# far\n")
        self._write("docs/templates/docs/child.md", "see `method/far.md` here\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual([], findings)

    def test_neither_resolution_still_flags(self):
        # Widening to three anchors can only DROP findings, never invent
        # one: a path absent under all three is still a real finding.
        self._write("docs/note.md", "see `other/ghost.md` from nowhere real\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("other/ghost.md", findings[0].target)

    def test_directory_target_resolves(self):
        (self.tmp / "docs" / "method").mkdir(parents=True)
        self._write("docs/note.md", "see the `docs/method/` directory\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual([], findings)

    def test_missing_directory_flagged(self):
        self._write("docs/note.md", "see the `docs/decisions/` directory\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/decisions", findings[0].target)


class Ignore(unittest.TestCase):
    def test_exact_glob(self):
        self.assertTrue(ps._ignored("docs/fixture.md", ["docs/fixture.md"]))

    def test_subtree_glob(self):
        self.assertTrue(ps._ignored("docs/sessions/x.md", ["docs/sessions/"]))
        self.assertTrue(ps._ignored("docs/sessions/x.md", ["docs/sessions"]))

    def test_non_match(self):
        self.assertFalse(ps._ignored("docs/real.md", ["docs/fixture.md"]))


class WholeTreeAndExitCodes(unittest.TestCase):
    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ps.Path(tempfile.mkdtemp())
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
            return ps.main(argv)

    def test_defaults_to_docs_subdir(self):
        self._write("README.md", "see `tools/ghost.py` outside docs\n")
        self._write("docs/note.md", "see `tools/ghost.py` inside docs\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/note.md", findings[0].path)

    def test_falls_back_to_root_when_no_docs_dir(self):
        self._write("note.md", "see `tools/ghost.py`, no docs dir here\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))

    def test_nonexistent_path_is_an_error_not_a_pass(self):
        self.assertEqual(
            2, self._main(["--root", str(self.tmp), str(self.tmp / "gone")]))

    def test_nonexistent_root_is_an_error(self):
        self.assertEqual(2, self._main(["--root", str(self.tmp / "gone-root")]))

    def test_warn_always_exits_zero(self):
        self._write("docs/note.md", "see `tools/ghost.py`\n")
        self.assertEqual(
            0, self._main(["--warn", "--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_without_warn_findings_exit_one(self):
        self._write("docs/note.md", "see `tools/ghost.py`\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_clean_tree_exits_zero(self):
        self._write("tools/real.py", "# real\n")
        self._write("docs/note.md", "see `tools/real.py`, which exists\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_pathscanignore_exempts_path(self):
        self._write("docs/note.md", "see `tools/ghost.py`\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))
        self._write(".pathscanignore", "# a reasoned fixture exemption\ndocs/note.md\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_non_markdown_files_skipped(self):
        self._write("docs/note.txt", "see `tools/ghost.py`, not markdown\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_json_output_shape(self):
        import contextlib
        import io
        import json
        self._write("docs/note.md", "see `tools/ghost.py`\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ps.main(["--json", "--root", str(self.tmp), str(self.tmp / "docs")])
        payload = json.loads(buf.getvalue())
        self.assertFalse(payload["clean"])
        self.assertEqual(1, len(payload["findings"]))
        self.assertEqual("missing-path", payload["findings"][0]["kind"])


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ps._selftest())


if __name__ == "__main__":
    unittest.main()


class Allowances(unittest.TestCase):
    """GUARDS.md — narrow, noisy, reasoned."""

    def test_html_comment_close_is_not_a_reason(self):
        self.assertIsNone(ps.parse_allow("x <!-- pathscan:allow: -->"))
        self.assertEqual("", ps.parse_allow("x <!-- pathscan:allow: real reason -->"))

    def test_bare_marker_without_reason_is_not_an_allowance(self):
        self.assertIsNone(ps.parse_allow("x <!-- pathscan:allow -->"))

    def test_clean_tally_reports_known_zeros(self):
        summary = ps.Tally().summary()
        self.assertIn("0 by allow-marker", summary)
        self.assertIn("0 file(s) by .pathscanignore", summary)
