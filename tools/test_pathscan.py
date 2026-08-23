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


class RootAnchoredTokenSkippedWhole(unittest.TestCase):
    """E8 — reported by a child repo 2026-08-09, fixed 2026-08-10.

    The docstring has always claimed a leading-`/` root-anchored mention is
    SKIPPED. It was skipped only when the path held no hyphen: the lookbehind
    excluded `/`, `\\w`, `.`, `*` and `?` but NOT `-`, so a match could resync
    mid-token at the first hyphen and emit a truncated path nobody wrote.
    `/.well-known/security.txt` came out as `known/security.txt` and was
    reported missing against a file that plainly existed.

    Same shape as `test_wildcard_does_not_split_the_token` above, and the
    same invariant closes both: the lookbehind must exclude EVERY character
    the token class accepts, plus `/`. These tests pin the invariant from
    both sides — a root-anchored token is skipped WHOLE, and a hyphenated
    token that is NOT root-anchored is still caught."""

    def _findings(self, text):
        return ps.scan_text(ps.Path("/nonexistent-root-xyz/t.md"),
                            ps.Path("/nonexistent-root-xyz"), text)

    def test_reported_case_yields_no_truncated_candidate(self):
        got = cand("Published at /.well-known/security.txt on the site.")
        self.assertNotIn("known/security.txt", got)
        self.assertEqual([], got)

    def test_hyphen_in_any_earlier_segment_resyncs(self):
        # Not dot-directories at large: ANY hyphen before the last `/`.
        self.assertEqual([], cand("see /docs/some-dir/x.md here"))
        self.assertEqual([], cand("see /a/b-c/d.md here"))

    def test_unhyphenated_root_anchored_still_skipped(self):
        # This shape was ALREADY skipped — the bug hid behind it, because the
        # docstring's claim read as true whenever the path had no hyphen.
        self.assertEqual([], cand("see /docs/x.md here"))

    def test_blanked_placeholder_tail_is_skipped(self):
        # The docstring names this exact case ("the tail of a just-blanked
        # `<placeholder>`") as skipped. It was not: blanking `<plugin-path>`
        # left `/.claude-plugin/plugin.json`, which resynced to
        # `plugin/plugin.json`. Live on this repo's own review corpus.
        got = cand("run `<plugin-path>/.claude-plugin/plugin.json` to check")
        self.assertNotIn("plugin/plugin.json", got)
        self.assertEqual([], got)

    def test_home_anchored_path_is_skipped(self):
        # `~/.claude/skills/create-repo/SKILL.md` resynced to `repo/SKILL.md`
        # — six live findings on this repo's own records, all of them this.
        got = cand("see `~/.claude/skills/create-repo/SKILL.md` for it")
        self.assertNotIn("repo/SKILL.md", got)

    def test_hyphenated_relative_paths_still_candidates(self):
        # The other direction: the fix must not blind the scanner to the
        # ordinary hyphenated paths this house writes constantly.
        self.assertIn("site/.well-known/sbom.json",
                      cand("see site/.well-known/sbom.json for the SBOM"))
        self.assertIn("tools/pre-commit.sample",
                      cand("see `tools/pre-commit.sample` here"))
        self.assertIn("docs/reviews/2026-07-26-2215-pathscan-s2-cold.md",
                      cand("see docs/reviews/2026-07-26-2215-pathscan-s2-cold.md"))

    def test_token_starting_at_a_hyphen_still_matches(self):
        # The lookbehind change must not swallow a token whose run BEGINS
        # with a hyphen — the char before the hyphen is what is tested, and
        # a markdown bullet's space clears it.
        self.assertIn("docs/method/x.md", cand("- docs/method/x.md"))

    def test_broken_hyphenated_path_still_flagged(self):
        # End-to-end, the load-bearing negative: a genuinely broken relative
        # path with a hyphen must still produce a finding. If this ever goes
        # quiet the fix has over-reached into a blanket hyphen exemption.
        findings = self._findings("see `docs/some-dir/ghost.md` for the rule\n")
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/some-dir/ghost.md", findings[0].target)

    def test_genuinely_broken_root_anchored_path_is_the_accepted_cost(self):
        # Stated plainly rather than rounded away: skipping WHOLE means a
        # root-anchored mention that IS broken also goes unflagged. That is
        # the docstring's named false negative, unchanged by this fix — the
        # defect was the truncation, never the skip. Widening the scanner to
        # resolve root-anchored paths is a separate design decision, and one
        # that would not have helped the reporting repo either: its
        # `/.well-known/…` mentions are published site URLs, not repo paths.
        self.assertEqual([], self._findings("see /docs/no-such-dir/ghost.md\n"))


class RootAnchoredEndToEnd(unittest.TestCase):
    """E8's minimal repro as the reporting child repo ran it, end to end over
    a real tree: the two relative mentions resolve, and the root-anchored one
    no longer invents a missing path beside them."""

    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ps.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def test_child_repo_repro_scans_clean(self):
        self._write("site/.well-known/sbom.json", "{}\n")
        self._write("site/.well-known/security.txt", "contact\n")
        self._write("docs/note.md",
                    "See site/.well-known/sbom.json for the SBOM.\n"
                    "See site/.well-known/security.txt for contact.\n"
                    "Published at /.well-known/security.txt on the site.\n")
        self.assertEqual([], ps.scan_paths([self.tmp / "docs"], self.tmp))


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


class DocumentedBlindSpots(unittest.TestCase):
    """Characterisation tests for the limits the module docstring NAMES
    (PS2, PS6, PS7). These pin documented behaviour, not desired behaviour —
    if one of them starts failing the docstring is what needs updating."""

    def _findings(self, text):
        return ps.scan_text(ps.Path("/nonexistent-root-xyz/t.md"),
                            ps.Path("/nonexistent-root-xyz"), text)

    def test_bold_wrapped_path_is_invisible(self):
        # PS2: the lookbehind excludes `*`, so no match starts inside `**`.
        self.assertEqual([], cand("see **docs/ghost.md** for the rule"))

    def test_underscore_wrapped_path_is_invisible(self):
        # PS2: `_` is a word character, so the token starts at the `_`.
        self.assertNotIn("docs/ghost.md", cand("see _docs/ghost.md_ here"))

    def test_bold_plus_backticks_is_caught(self):
        # PS2's stated exception — backticks give a clean boundary.
        self.assertIn("docs/ghost.md", cand("see **`docs/ghost.md`** here"))

    def test_todo_about_something_else_masks_a_real_break(self):
        # PS6: the stub cue is LINE-level; this is its cost, documented.
        self.assertEqual(
            [], self._findings("fix `docs/ghost.md` — TODO tidy the prose\n"))

    def test_indented_code_block_is_scanned(self):
        # PS7: only FENCED blocks are exempt. An indented block is scanned.
        findings = self._findings("prose\n\n    see `docs/ghost.md` indented\n")
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/ghost.md", findings[0].target)


class DatePlaceholderExemption(unittest.TestCase):
    """PS3: a token carrying a literal uppercase `YYYY`/`HHMM` segment is a
    naming-convention TEMPLATE, not a claim that such a file exists. Live on
    docs/build/templates/docs/decisions/template.md, where the token also
    sits inside a `<...>` placeholder span that WRAPS across a line break —
    so the line-local blanking pass never sees it."""

    def test_full_date_time_template_exempt(self):
        self.assertEqual(
            [], cand("queued — docs/reviews/YYYY-MM-DD-HHMM-slug.md · or ·"))

    def test_yyyy_alone_exempt(self):
        self.assertEqual([], cand("see `docs/sessions/YYYY-MM-DD-slug.md`"))

    def test_hhmm_alone_exempt(self):
        self.assertEqual([], cand("see `docs/reviews/HHMM-slug.md`"))

    def test_lowercase_is_not_a_cue(self):
        # Case-SENSITIVE by design: `yyyy` in a real filename must not buy
        # a silent exemption.
        self.assertIn("docs/notes/yyyy-thing.md",
                      cand("see `docs/notes/yyyy-thing.md`"))

    def test_mm_dd_alone_are_not_cues(self):
        # Deliberately narrow — two-letter uppercase runs occur in real
        # filenames, so MM/DD alone must not exempt.
        self.assertIn("docs/method/MM-DD.md", cand("see `docs/method/MM-DD.md`"))


class DirectoryIndexRetry(unittest.TestCase):
    """Deferred-Q2 counsel: an EXTENSIONLESS token is retried with
    `.md`/`.markdown` appended under every anchor — GitHub's directory-index
    convention (`tools/README` is really `tools/README.md`). Monotone-safe:
    the retry can only drop findings, never invent one."""

    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ps.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def test_bare_readme_resolves_to_md(self):
        self._write("tools/README.md", "# tools\n")
        self._write("docs/note.md", "see `tools/README` for the index\n")
        self.assertEqual([], ps.scan_paths([self.tmp / "docs"], self.tmp))

    def test_bare_readme_resolves_to_markdown(self):
        self._write("tools/README.markdown", "# tools\n")
        self._write("docs/note.md", "see `tools/README` for the index\n")
        self.assertEqual([], ps.scan_paths([self.tmp / "docs"], self.tmp))

    def test_extensionless_with_no_md_still_flagged(self):
        # The retry is not a blanket pass: nothing on disk, still a finding.
        self._write("docs/note.md", "see `docs/decisions/0001` for the call\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/decisions/0001", findings[0].target)

    def test_token_with_extension_is_not_retried(self):
        # `tools/ghost.py` must NOT be satisfied by `tools/ghost.py.md`.
        self._write("tools/ghost.py.md", "# decoy\n")
        self._write("docs/note.md", "see `tools/ghost.py` here\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("tools/ghost.py", findings[0].target)


class RootFileDocsRelativeAnchor(unittest.TestCase):
    """PS1 — anchor 4. A file with NO `docs/` ancestor (a ROOT file) writes
    docs-relative shorthand exactly as a file inside docs/ does, but has no
    enclosing docs/ for anchor 3 to find. `<root>/docs` is that anchor.
    Mutually exclusive with anchor 3 by construction."""

    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ps.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def test_root_readme_resolves_docs_relative_shorthand(self):
        # The live shape: README.md:51 writes `method/REVIEW.md`, meaning
        # docs/method/REVIEW.md — 51 of 64 doctrine-surface findings were
        # this one shape before anchor 4.
        self._write("docs/method/REVIEW.md", "# review\n")
        self._write("README.md", "see `method/REVIEW.md` for the rules\n")
        self.assertEqual(
            [], ps.scan_paths([self.tmp / "README.md"], self.tmp))

    def test_non_root_file_outside_docs_also_gets_the_anchor(self):
        # The rule is "no docs/ ancestor", not "at the repo root" — a file
        # under tools/ writes the same shorthand.
        self._write("docs/method/REVIEW.md", "# review\n")
        self._write("tools/README.md", "see `method/REVIEW.md` here\n")
        self.assertEqual(
            [], ps.scan_paths([self.tmp / "tools" / "README.md"], self.tmp))

    def test_root_file_still_flags_a_genuine_break(self):
        # Anchor 4 widens resolution; it must not blanket-pass.
        self._write("docs/method/REVIEW.md", "# review\n")
        self._write("README.md", "see `method/GHOST.md` for the rules\n")
        findings = ps.scan_paths([self.tmp / "README.md"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("method/GHOST.md", findings[0].target)

    def test_finding_detail_names_the_anchor_actually_tried(self):
        self._write("README.md", "see `method/GHOST.md` for the rules\n")
        findings = ps.scan_paths([self.tmp / "README.md"], self.tmp)
        self.assertIn("docs-relative shorthand", findings[0].detail)

    def test_doc_under_docs_keeps_the_enclosing_anchor_wording(self):
        self._write("docs/note.md", "see `method/GHOST.md` here\n")
        findings = ps.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertIn("outermost enclosing docs/", findings[0].detail)

    def test_root_level_markdown_is_scannable(self):
        # PS4 prep: the gate scope the review recommends is the doctrine
        # surface PLUS root-level *.md, so root files must scan as explicit
        # targets even though the DEFAULT scope is docs/ only.
        self._write("README.md", "see `tools/ghost.py` from the root\n")
        findings = ps.scan_paths([self.tmp / "README.md"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("README.md", findings[0].path)


class DualResolution(unittest.TestCase):
    """A bare-prose path resolves if it exists under ANY of four anchors —
    the scan root, the linking file's own directory, and then EITHER its
    outermost enclosing docs/ directory (a file under docs/) OR
    `<root>/docs` (a file outside it) — see module docstring, THE CHECK
    step 5, and RootFileDocsRelativeAnchor above for the fourth. Found
    necessary by running this scanner over atelier's own corpus:
    docs/build/REPO-STANDARD.md routinely drops the `docs/` prefix and
    writes `method/RECORD.md`, meaning `docs/method/RECORD.md` — NOT
    sibling-relative to its own directory (docs/build/), which has no
    method/ child — while README.md at the repo root writes the same
    target root-relative as `docs/method/RECORD.md`. Every anchor that
    applies must be tried."""

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

    def test_records_are_excluded_by_default_when_a_dir_expands(self):
        """FR2 (ruled 2026-08-23): records name the tree as it stood when
        written and can never come clean — a child's default scope must not
        pull them in. Dead paths in records: invisible by default."""
        self._write("docs/reviews/old-review.md", "see `tools/ghost.py`\n")
        self._write("docs/sessions/old-session.md", "see `tools/ghost.py`\n")
        self._write("docs/SESSIONS.md", "see `tools/ghost.py`\n")
        self._write("docs/live.md", "all real: `docs/SESSIONS.md`\n")
        self.assertEqual(0, self._main(["--root", str(self.tmp)]))

    def test_include_records_selects_them(self):
        self._write("docs/reviews/old-review.md", "see `tools/ghost.py`\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp),
                                        "--include-records"]))

    def test_a_record_named_explicitly_is_always_scanned(self):
        self._write("docs/reviews/old-review.md", "see `tools/ghost.py`\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp),
                                        str(self.tmp / "docs/reviews/old-review.md")]))

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


class Allowances(unittest.TestCase):
    """GUARDS.md — narrow, noisy, reasoned, declared.

    (Moved above the __main__ block 2026-08-06, PD1: defined after
    `unittest.main()` by the 0228793 merge, these ran under discovery but
    were silently dropped by a direct `python3 tools/test_pathscan.py`
    run.)"""

    def test_html_comment_close_is_not_a_reason(self):
        self.assertIsNone(ps.parse_allow("x <!-- pathscan:allow: -->"))
        self.assertEqual("", ps.parse_allow("x <!-- pathscan:allow: real reason -->"))

    def test_bare_marker_without_reason_is_not_an_allowance(self):
        self.assertIsNone(ps.parse_allow("x <!-- pathscan:allow -->"))

    def test_clean_tally_reports_known_zeros(self):
        summary = ps.Tally().summary()
        self.assertIn("0 by allow-marker", summary)
        self.assertIn("0 file(s) by .pathscanignore", summary)


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ps._selftest())


if __name__ == "__main__":
    unittest.main()
