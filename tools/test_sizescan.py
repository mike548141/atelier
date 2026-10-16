"""Stdlib-only tests for sizescan (no pytest needed): `python3 -m unittest`.

Pure-logic parts (cold_item_count, live_item_count) are unit-tested directly.
The end-to-end parts build a throwaway tree under a tmp dir and drive
scan_paths() / main(), so the candidate selection (growth stores skipped,
reference docs unread, root-only READMEs), the escape hatches, inert-hatch
naming and the gate exit contract are proven against the real filesystem, not a
mock.

The gate model (Mike's 2026-07-20 ruling, reworked 2026-07-20): `--check` fails
ONLY on relocatable cold content — a completed `[x]` item on the hot path, whose
fix is a lossless move to ROADMAP-DONE.md — and on live state in an archive
store. A file that is merely *long* from live current-truth is not reported at
all: the size advisory was removed (115/270 c, Mike's ruling 2026-10-05 and his
answer of 2026-10-16), and there is nothing to relocate in an all-open
roadmap."""

import io
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import sizescan
import memprobe

TOOLS_DIR = Path(__file__).resolve().parent

# A length far past anything the retired size advisory ever flagged (its class
# references ran 200 to 300). It is a fixture for "a long file is silent", not a
# limit: nothing in sizescan reads a number like it any more.
LONG = 5000


def _cold(n_open=1, n_done=0):
    """A checkbox-worklog body with n_open live items and n_done cold `[x]` ones."""
    return "".join(["- [ ] open item\n"] * n_open + ["- [x] done item\n"] * n_done)


class NoSizeCheck(unittest.TestCase):
    """115/270 c: the size advisory is gone, and with it every name it had."""

    def test_the_reference_points_and_helpers_are_gone(self):
        for name in ("SIZE_REFERENCE", "reference_for", "count_lines",
                     "_BUDGET_MARKER", "_STORE_HINT"):
            self.assertFalse(hasattr(sizescan, name), name)

    def test_a_finding_carries_no_size_fields(self):
        names = set(sizescan.Finding.__dataclass_fields__)
        self.assertFalse(names & {"reference", "over"}, names)


class ColdItemCount(unittest.TestCase):
    def test_counts_done_checkbox_items(self):
        self.assertEqual(sizescan.cold_item_count(_cold(2, 3), "ROADMAP.md"), 3)

    def test_caps_and_indent_counted(self):
        self.assertEqual(
            sizescan.cold_item_count("  - [x] indented\n- [X] caps\n* [x] star\n", "ROADMAP.md"), 3)

    def test_all_bullet_markers_counted(self):
        # -, *, +, and ordered (1. / 1)) are all Markdown list bullets; a done
        # item written in any of them is still relocatable cold content.
        self.assertEqual(
            sizescan.cold_item_count("+ [x] plus\n1. [x] ordered\n2) [x] paren\n", "ROADMAP.md"), 3)

    def test_checkbox_inside_code_fence_not_counted(self):
        # a [x] inside a fenced block is a quoted example (e.g. docs showing the
        # worklog syntax), not a harvestable work item — fenced regions are skipped.
        body = "- [x] real done item\n```\n- [x] quoted example\n- [x] another\n```\n"
        self.assertEqual(sizescan.cold_item_count(body, "ROADMAP.md"), 1)
        self.assertEqual(
            sizescan.cold_item_count("~~~\n- [x] tilde-fenced\n~~~\n", "ROADMAP.md"), 0)

    def test_unclosed_fence_does_not_swallow_cold_items(self):
        # HI-F2: an unclosed fence gets no quoting immunity — same fail-safe
        # as the harvest-integrity counter (shared _count_list_items).
        body = "```\nstray fence\n- [x] done but swallowed\n"
        self.assertEqual(sizescan.cold_item_count(body, "ROADMAP.md"), 1)

    def test_cold_marker_between_stray_fence_and_snippet_counts(self):
        # HA2: unbalanced delimiters recount the whole file — parity with
        # the live counter via the shared _count_list_items.
        body = "```\n- [x] buried done\n```\ncode line\n```\ntail\n"
        self.assertEqual(sizescan.cold_item_count(body, "ROADMAP.md"), 1)

    def test_open_claimed_review_states_not_cold(self):
        body = "- [ ] open\n- [~] claimed\n- ⏳ review queued\n"
        self.assertEqual(sizescan.cold_item_count(body, "ROADMAP.md"), 0)

    def test_prose_mention_of_bracket_x_not_counted(self):
        self.assertEqual(
            sizescan.cold_item_count("checkbox states: [x] done, in a sentence\n", "ROADMAP.md"), 0)

    def test_only_checkbox_worklog_files_count(self):
        # a [x] in a README or session index is prose, not a harvestable work item
        self.assertEqual(sizescan.cold_item_count("- [x] done\n", "README.md"), 0)
        self.assertEqual(sizescan.cold_item_count("- [x] done\n", "SESSIONS.md"), 0)


class _TreeTest(unittest.TestCase):
    """Base: a tmp repo whose files are written per-test, then scanned."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="sizescan-test-"))
        (self.tmp / "docs").mkdir()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write(self, rel, n_lines):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("x\n" * n_lines)
        return p

    def write_text(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def flagged(self):
        return sorted(f.path.replace("\\", "/")
                      for f in sizescan.scan_paths([self.tmp], self.tmp))

    def finding(self, rel):
        for f in sizescan.scan_paths([self.tmp], self.tmp):
            if f.path.replace("\\", "/") == rel:
                return f
        return None


class Selection(_TreeTest):
    def test_a_long_all_open_roadmap_is_silent(self):
        # 115/270 c: length is never reported, however far it runs
        self.write_text("docs/ROADMAP.md", _cold(LONG, 0))
        self.assertEqual(self.flagged(), [])

    def test_every_current_truth_file_is_silent_at_any_length(self):
        for rel in ("docs/ROADMAP.md", "docs/SESSIONS.md", "README.md",
                    "ARCHITECTURE.md", "CLAUDE.md"):
            self.write(rel, LONG)
        self.assertEqual(self.flagged(), [])

    def test_small_file_with_cold_content_flags_and_gates(self):
        # size is irrelevant — a done item on the hot path is what matters
        self.write_text("docs/ROADMAP.md", _cold(1, 2))
        f = self.finding("docs/ROADMAP.md")
        self.assertIsNotNone(f)
        self.assertTrue(f.gated)
        self.assertEqual(f.cold_items, 2)

    def test_a_long_roadmap_with_cold_content_reports_its_length_as_context(self):
        self.write_text("docs/ROADMAP.md", _cold(LONG, 1))
        f = self.finding("docs/ROADMAP.md")
        self.assertEqual((f.lines, f.cold_items, f.gated), (LONG + 1, 1, True))

    def test_growth_stores_never_flagged_for_size(self):
        self.write("docs/ROADMAP-DONE.md", 5000)
        self.write("docs/SPECS.md", 5000)
        self.write("CHANGELOG.md", 5000)
        self.assertEqual(self.flagged(), [])

    def test_reference_doc_not_read(self):
        self.write("docs/PRINCIPLES.md", 5000)
        self.assertEqual(self.flagged(), [])

    def test_hot_path_basename_inside_growth_store_ignored(self):
        self.write_text("_archive/ROADMAP.md", _cold(1, 3))
        self.write("_archive/ARCHITECTURE.md", 5000)
        self.write("docs/reviews/README.md", 5000)
        self.assertEqual(self.flagged(), [])

    def test_root_readme_read_nested_readme_not(self):
        # only the root README is a current-truth file; a hatch left in it is
        # named (below), a nested one is not even looked at
        self.write_text("README.md", f"<!-- {sizescan.ALLOW_MARKER}: long -->\n")
        self.write_text("tools/README.md", f"<!-- {sizescan.ALLOW_MARKER}: long -->\n")
        inert = []
        sizescan.scan_paths([self.tmp], self.tmp, None, inert)
        self.assertEqual([h.path for h in inert], ["README.md"])

    def test_roadmap_read_wherever_it_lives(self):
        self.write_text("docs/ROADMAP.md", _cold(1, 1))
        self.assertEqual(self.flagged(), ["docs/ROADMAP.md"])


class FailOpenF1(unittest.TestCase):
    """F1 (MAJOR): skip-dir names must be matched relative to the scan base, not
    the absolute path — else a repo living under a store-named ancestor has every
    file skipped and reports clean (fail-open)."""

    def _repo_under(self, ancestor):
        base = Path(tempfile.mkdtemp(prefix="sizescan-f1-"))
        repo = base / ancestor / "myrepo"
        (repo / "docs").mkdir(parents=True)
        (repo / "docs" / "ROADMAP.md").write_text(_cold(1, 2))
        return base, repo

    def _assert_flags(self, ancestor):
        base, repo = self._repo_under(ancestor)
        try:
            flagged = [f.path.replace("\\", "/") for f in sizescan.scan_paths([repo], repo)]
            self.assertIn("docs/ROADMAP.md", flagged,
                          f"repo under {ancestor}/ was skipped (fail-open)")
        finally:
            import shutil
            shutil.rmtree(base, ignore_errors=True)

    def test_under_archive_ancestor_still_scanned(self):
        self._assert_flags("archive")

    def test_under_reviews_ancestor_still_scanned(self):
        self._assert_flags("reviews")

    def test_real_store_dir_inside_repo_still_skipped(self):
        base = Path(tempfile.mkdtemp(prefix="sizescan-f1b-"))
        try:
            (base / "docs" / "reviews").mkdir(parents=True)
            (base / "docs" / "reviews" / "README.md").write_text("x\n" * 5000)
            self.assertEqual(sizescan.scan_paths([base], base), [])
        finally:
            import shutil
            shutil.rmtree(base, ignore_errors=True)


class Hatches(_TreeTest):
    def test_body_only_marker_mention_does_not_exempt(self):
        # F2: a marker mentioned below the header must not silently exempt
        self.write_text("docs/ROADMAP.md",
                        ("prose\n" * 20) + "we set sizescan:allow here in discussion\n"
                        + _cold(1, 2))
        self.assertEqual(self.flagged(), ["docs/ROADMAP.md"])
        self.assertEqual(self.finding("docs/ROADMAP.md").cold_hatches, [])

    def test_header_allow_marker_does_not_exempt_the_gate_and_is_named(self):
        # 115/270 a, Mike's ruling: no hatch silences cold content. The report
        # says it was present, and (115/270 c) that it is inert.
        self.write_text("docs/ROADMAP.md",
                        f"<!-- {sizescan.ALLOW_MARKER}: living doc -->\n"
                        + _cold(LONG, 5))
        f = self.finding("docs/ROADMAP.md")
        self.assertIsNotNone(f)
        self.assertTrue(f.gated)
        self.assertEqual(f.cold_items, 5)
        self.assertEqual(f.cold_hatches, [f"{sizescan.ALLOW_MARKER} header (unscoped)"])

    def test_cold_content_scope_does_not_exempt_the_gate(self):
        self.write_text("docs/ROADMAP.md",
                        f"<!-- {sizescan.ALLOW_MARKER}:cold-content: harvested -->\n"
                        + _cold(1, 3))
        f = self.finding("docs/ROADMAP.md")
        self.assertIsNotNone(f)
        self.assertTrue(f.gated)
        self.assertEqual(f.cold_items, 3)
        self.assertEqual(f.cold_hatches,
                         [f"{sizescan.ALLOW_MARKER}:cold-content header"])

    def test_a_scope_for_another_kind_is_inert_on_a_roadmap_too(self):
        # 115/270 c: it used to quiet the size advisory, which is gone, so a
        # `size-advisory` scope now does nothing and the report says so.
        self.write_text("docs/ROADMAP.md",
                        f"<!-- {sizescan.ALLOW_MARKER}:size-advisory: long -->\n"
                        + _cold(1, 2))
        self.assertEqual(self.finding("docs/ROADMAP.md").cold_hatches,
                         [f"{sizescan.ALLOW_MARKER}:size-advisory header"])

    def test_overlapping_paths_do_not_double_report(self):
        # F4: dedup by resolved path
        self.write_text("docs/ROADMAP.md", _cold(1, 1))
        findings = sizescan.scan_paths([self.tmp, self.tmp / "docs"], self.tmp)
        paths = [f.path.replace("\\", "/") for f in findings]
        self.assertEqual(paths.count("docs/ROADMAP.md"), 1)

    def test_budget_marker_is_inert_and_does_not_hide_cold_content(self):
        # the retired override: nothing reads its number, the gate stands, and
        # the marker is named so it is not mistaken for something live
        self.write_text("docs/ROADMAP.md",
                        "<!-- sizescan:budget=100000 -->\n" + _cold(1, 2))
        f = self.finding("docs/ROADMAP.md")
        self.assertTrue(f.gated)
        self.assertEqual(f.cold_items, 2)
        self.assertEqual(f.cold_hatches, ["sizescan:budget header"])

    def test_sizescanignore_glob_does_not_exempt_the_gate_and_is_named(self):
        # The ignored hot-path file is still read: its cold content gates.
        self.write_text("docs/ROADMAP.md", _cold(1, 5))
        (self.tmp / ".sizescanignore").write_text("# a reasoned fixture exemption\ndocs/ROADMAP.md\n")
        f = self.finding("docs/ROADMAP.md")
        self.assertIsNotNone(f)
        self.assertTrue(f.gated)
        self.assertEqual(f.cold_items, 5)
        self.assertEqual(f.cold_hatches, [".sizescanignore glob"])

    def test_sizescanignore_glob_over_a_clean_roadmap_is_inert_not_a_suppression(self):
        # it skipped such a file once (and counted it); now it exempts nothing,
        # so it is an inert hatch and is NOT counted as a file suppressed
        self.write_text("docs/ROADMAP.md", _cold(3, 0))
        (self.tmp / ".sizescanignore").write_text("# a reasoned fixture exemption\ndocs/ROADMAP.md\n")
        counts, inert = {}, []
        self.assertEqual(sizescan.scan_paths([self.tmp], self.tmp, counts, inert), [])
        self.assertEqual(counts["files_by_glob"], 0)
        self.assertEqual(counts["inert_hatches"], 1)
        self.assertEqual([(h.path, h.hatch) for h in inert],
                         [("docs/ROADMAP.md", ".sizescanignore glob")])

    def test_sizescanignore_still_skips_an_archive_store_wholesale(self):
        # the one place a glob still has an effect
        self.write_text("docs/ROADMAP-DONE.md", "- [ ] parked here\n")
        (self.tmp / ".sizescanignore").write_text("# a reasoned fixture exemption\ndocs/ROADMAP-DONE.md\n")
        counts, inert = {}, []
        self.assertEqual(sizescan.scan_paths([self.tmp], self.tmp, counts, inert), [])
        self.assertEqual((counts["files_by_glob"], counts["inert_hatches"], inert),
                         (1, 0, []))

    def test_check_exits_1_through_every_hatch_and_says_so(self):
        (self.tmp / ".sizescanignore").write_text("# a reasoned fixture exemption\nignored/*\n")
        for rel, head, named in (
                ("docs/ROADMAP.md", f"<!-- {sizescan.ALLOW_MARKER}: x -->\n",
                 f"{sizescan.ALLOW_MARKER} header (unscoped)"),
                ("docs/ROADMAP.md",
                 f"<!-- {sizescan.ALLOW_MARKER}:cold-content: x -->\n",
                 f"{sizescan.ALLOW_MARKER}:cold-content header"),
                ("ignored/ROADMAP.md", "", ".sizescanignore glob")):
            with self.subTest(hatch=named):
                self.write_text(rel, head + _cold(1, 1))
                buf = io.StringIO()
                with redirect_stdout(buf):
                    code = sizescan.main(["--check", "--root", str(self.tmp),
                                          str(self.tmp)])
                self.assertEqual(code, 1)
                self.assertIn(f"note: {named} present", buf.getvalue())
                self.assertIn("cannot exempt cold content", buf.getvalue())
                (self.tmp / rel).unlink()


class InertHatches(_TreeTest):
    """115/270 c: with the size advisory gone, a hatch that quieted it exempts
    nothing. It must never be accepted in silence, and must never change a
    verdict or an exit code."""

    def scan(self):
        counts, inert = {}, []
        found = sizescan.scan_paths([self.tmp], self.tmp, counts, inert)
        return found, counts, sorted((h.path, h.hatch) for h in inert)

    def run_main(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = sizescan.main([*args, "--root", str(self.tmp), str(self.tmp)])
        return code, buf.getvalue()

    def test_a_stale_allow_marker_on_a_non_roadmap_hot_file_is_named(self):
        for rel in ("docs/SESSIONS.md", "ARCHITECTURE.md", "README.md", "CLAUDE.md"):
            self.write_text(rel, f"<!-- {sizescan.ALLOW_MARKER}: long -->\n" + "x\n" * 40)
        found, counts, inert = self.scan()
        self.assertEqual(found, [])
        self.assertEqual(counts["inert_hatches"], 4)
        self.assertEqual([h for _, h in inert],
                         [f"{sizescan.ALLOW_MARKER} header (unscoped)"] * 4)
        self.assertEqual(counts["files_allowed"], 0)    # suppresses nothing

    def test_a_stale_budget_marker_is_named(self):
        self.write_text("docs/SESSIONS.md", "<!-- sizescan:budget: 900 -->\n")
        self.assertEqual(self.scan()[2],
                         [("docs/SESSIONS.md", "sizescan:budget header")])

    def test_a_clean_roadmap_with_a_stale_allow_is_clean_but_names_it(self):
        self.write_text("docs/ROADMAP.md",
                        f"<!-- {sizescan.ALLOW_MARKER}: long -->\n" + _cold(LONG, 0))
        code, out = self.run_main("--check")
        self.assertEqual(code, 0)
        self.assertIn("sizescan clean", out)
        self.assertIn("Inert hatches", out)
        self.assertIn(f"docs/ROADMAP.md: {sizescan.ALLOW_MARKER} header (unscoped)", out)
        self.assertIn("1 inert hatch(es) (exempt nothing)", out)

    def test_a_hatch_on_a_cold_finding_is_named_once_and_counted_once(self):
        self.write_text("docs/ROADMAP.md",
                        f"<!-- {sizescan.ALLOW_MARKER}: x -->\n" + _cold(1, 1))
        code, out = self.run_main("--check")
        self.assertEqual(code, 1)
        self.assertEqual(out.count(f"{sizescan.ALLOW_MARKER} header (unscoped)"), 1)
        self.assertNotIn("Inert hatches", out)
        self.assertIn("1 inert hatch(es) (exempt nothing)", out)

    def test_a_marker_that_still_exempts_is_not_inert(self):
        # unscoped, or `harvest-integrity`, on an archive store: the one live use
        for scope in ("", ":harvest-integrity"):
            with self.subTest(scope=scope):
                self.write_text("docs/ROADMAP-DONE.md",
                                f"<!-- {sizescan.ALLOW_MARKER}{scope}: parked -->\n- [ ] parked\n")
                found, counts, inert = self.scan()
                self.assertEqual((found, inert, counts["files_allowed"]), ([], [], 1))

    def test_a_scope_that_does_not_cover_an_archive_store_is_inert_and_does_not_exempt(self):
        # `cold-content` never exempted it; the retired `size-advisory` must not
        # be misread as the unscoped form (which would exempt it)
        for scope in ("cold-content", "size-advisory"):
            with self.subTest(scope=scope):
                self.write_text("docs/ROADMAP-DONE.md",
                                f"<!-- {sizescan.ALLOW_MARKER}:{scope}: parked -->\n- [ ] parked\n")
                found, counts, inert = self.scan()
                self.assertEqual([f.path for f in found], ["docs/ROADMAP-DONE.md"])
                self.assertEqual(inert, [("docs/ROADMAP-DONE.md",
                                          f"{sizescan.ALLOW_MARKER}:{scope} header")])
                self.assertEqual(counts["files_allowed"], 0)

    def test_inert_hatches_never_change_an_exit_code(self):
        self.write_text("docs/SESSIONS.md",
                        f"<!-- {sizescan.ALLOW_MARKER}: x -->\n<!-- sizescan:budget=9 -->\n")
        self.write_text("docs/ROADMAP.md", _cold(2, 0))
        (self.tmp / ".sizescanignore").write_text("# fixture\ndocs/ROADMAP.md\n")
        self.assertEqual(self.run_main("--check")[0], 0)
        self.write_text("docs/ROADMAP.md", _cold(2, 1))
        self.assertEqual(self.run_main("--check")[0], 1)
        self.assertEqual(self.run_main()[0], 0)

    def test_json_carries_them_with_a_known_zero(self):
        import json
        self.write_text("docs/ROADMAP.md", _cold(1, 0))
        self.assertEqual(json.loads(self.run_main("--json")[1])["inert_hatches"], [])
        self.write_text("README.md", f"<!-- {sizescan.ALLOW_MARKER}: x -->\n")
        self.assertEqual(json.loads(self.run_main("--json")[1])["inert_hatches"],
                         [{"path": "README.md",
                           "hatch": f"{sizescan.ALLOW_MARKER} header (unscoped)"}])

    def test_a_hot_file_is_read_for_its_header_only(self):
        # a huge stale-marker file costs one chunk, not a full pass, and a
        # marker past the header (line 16 on) is a mention, not a hatch
        self.write_text("ARCHITECTURE.md",
                        "x\n" * 15 + f"<!-- {sizescan.ALLOW_MARKER}: late -->\n")
        self.assertEqual(self.scan()[2], [])


class ColdItemListing(_TreeTest):
    """115/270 b: the finding names each completed item, so no session has to
    infer them. Bounded the way every scanner's findings are."""

    def test_names_each_item_by_line_and_text(self):
        self.write_text("docs/ROADMAP.md",
                        "# Roadmap\n"
                        "- [ ] open\n"
                        "- [x] 🔎 **First done thing** with detail\n"
                        "      continuation line\n"
                        "  * [X] nested done\n"
                        "1. [x] ordered done\n")
        f = self.finding("docs/ROADMAP.md")
        self.assertEqual([(i.line, i.title) for i in f.cold_listed],
                         [(3, "🔎 **First done thing** with detail"),
                          (5, "nested done"), (6, "ordered done")])
        self.assertEqual(f.cold_items, 3)

    def test_lines_inside_a_fence_are_not_listed(self):
        self.write_text("docs/ROADMAP.md",
                        "```\n- [x] quoted\n```\n- [x] real\n")
        self.assertEqual([(i.line, i.title)
                          for i in self.finding("docs/ROADMAP.md").cold_listed],
                         [(4, "real")])

    def test_unclosed_fence_recount_lists_from_the_second_pass_only(self):
        self.write_text("docs/ROADMAP.md", "- [x] a\n```\n- [x] b\n")
        f = self.finding("docs/ROADMAP.md")
        self.assertEqual([(i.line, i.title) for i in f.cold_listed],
                         [(1, "a"), (3, "b")])
        self.assertEqual(f.cold_items, 2)

    def test_long_title_is_truncated_to_fit_the_column_limit(self):
        self.write_text("docs/ROADMAP.md", "- [x] " + "word " * 100 + "\n")
        title = self.finding("docs/ROADMAP.md").cold_listed[0].title
        self.assertEqual(len(title), sizescan._TITLE_CHARS)
        self.assertTrue(title.endswith("…"))

    def test_empty_item_text_is_stated_not_blank(self):
        self.write_text("docs/ROADMAP.md", "- [x]\n")
        self.assertEqual(self.finding("docs/ROADMAP.md").cold_listed[0].title,
                         "(no text)")

    def test_report_lists_every_item_within_85_columns(self):
        self.write_text("docs/ROADMAP.md",
                        "- [ ] open\n- [x] " + "long " * 40 + "\n- [x] short\n")
        buf = io.StringIO()
        with redirect_stdout(buf):
            sizescan.main(["--root", str(self.tmp), str(self.tmp)])
        out = buf.getvalue()
        self.assertIn("completed items counted (line: item):", out)
        self.assertIn("          line 3: short", out)
        for ln in out.splitlines():
            if ln.startswith("          line "):
                self.assertLessEqual(len(ln), 85, ln)

    def test_cap_holds_and_the_rest_are_counted_not_listed(self):
        self.write_text("docs/ROADMAP.md", _cold(1, 5))
        old = sizescan.MAX_MATERIALIZED_FINDINGS
        sizescan.MAX_MATERIALIZED_FINDINGS = 3
        self.addCleanup(setattr, sizescan, "MAX_MATERIALIZED_FINDINGS", old)
        counts = {}
        f = sizescan.scan_paths([self.tmp], self.tmp, counts)[0]
        self.assertEqual(f.cold_items, 5)            # the true count survives
        self.assertEqual(len(f.cold_listed), 3)
        self.assertEqual(counts["cold_over_cap"], 2)
        out = sizescan.render_human([f], cold_over_cap=2)
        self.assertIn("  …and 2 more completed item(s)", out)
        self.assertIn("counted but not listed (past the 3-finding memory cap)", out)
        self.assertIn("2 beyond the 3-finding cap (counted, not listed)", out)

    def test_cap_is_run_wide_across_files(self):
        self.write_text("docs/ROADMAP.md", _cold(1, 2))
        self.write_text("sub/docs/ROADMAP.md", _cold(1, 2))
        old = sizescan.MAX_MATERIALIZED_FINDINGS
        sizescan.MAX_MATERIALIZED_FINDINGS = 3
        self.addCleanup(setattr, sizescan, "MAX_MATERIALIZED_FINDINGS", old)
        counts = {}
        found = sizescan.scan_paths([self.tmp], self.tmp, counts)
        self.assertEqual(sum(len(f.cold_listed) for f in found), 3)
        self.assertEqual(counts["cold_over_cap"], 1)

    def test_json_carries_the_items_and_a_known_zero_over_cap(self):
        import json
        self.write_text("docs/ROADMAP.md", "- [ ] o\n- [x] done\n")
        buf = io.StringIO()
        with redirect_stdout(buf):
            sizescan.main(["--json", "--root", str(self.tmp), str(self.tmp)])
        data = json.loads(buf.getvalue())
        self.assertEqual(data["cold_items_over_cap"], 0)
        f0 = data["findings"][0]
        self.assertEqual(f0["cold_listed"], [{"line": 2, "title": "done"}])
        self.assertEqual(f0["cold_hatches"], [])


class ExitContract(_TreeTest):
    def _run(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = sizescan.main([*args, "--root", str(self.tmp), str(self.tmp)])
        return code, buf.getvalue()

    def test_default_exit_zero_even_with_cold_content(self):
        self.write_text("docs/ROADMAP.md", _cold(1, 2))
        code, out = self._run()
        self.assertEqual(code, 0)          # no --check: reports but never fails
        self.assertIn("cold-content", out)

    def test_check_gates_on_cold_content(self):
        self.write_text("docs/ROADMAP.md", _cold(1, 1))
        code, out = self._run("--check")
        self.assertEqual(code, 1)          # a [x] item on the hot path has teeth
        self.assertIn("[cold-content, gated]", out)

    def test_check_does_not_gate_a_long_all_open_roadmap(self):
        # THE reversal: fulsome live current-truth is never a build failure,
        # and (115/270 c) is not even mentioned
        self.write_text("docs/ROADMAP.md", _cold(LONG, 0))
        code, out = self._run("--check")
        self.assertEqual(code, 0)
        self.assertIn("sizescan clean", out)
        self.assertNotIn("size", out.replace("sizescan", ""))

    def test_check_exits_zero_when_no_cold_content(self):
        self.write_text("docs/ROADMAP.md", _cold(10, 0))
        code, _ = self._run("--check")
        self.assertEqual(code, 0)

    def test_check_never_reports_a_long_judgement_doc(self):
        self.write("ARCHITECTURE.md", LONG)
        code, out = self._run("--check")
        self.assertEqual(code, 0)
        self.assertNotIn("ARCHITECTURE.md", out)

    def test_check_cold_content_is_the_only_finding_beside_a_long_file(self):
        self.write("ARCHITECTURE.md", LONG)                      # silent
        self.write_text("docs/ROADMAP.md", _cold(1, 1))          # cold → gate
        code, out = self._run("--check")
        self.assertEqual(code, 1)
        self.assertIn("[cold-content, gated]", out)
        self.assertNotIn("ARCHITECTURE.md", out)
        self.assertIn("1 file(s) flagged", out)

    def test_gate_is_cold_content_not_a_static_file_set(self):
        # Pin the doctrine: gating is driven by relocatable cold content, so a
        # long all-current ROADMAP/SESSIONS does not gate, but any file's [x]
        # items would. There is no static GATED set to drift.
        self.assertFalse(hasattr(sizescan, "GATED"))
        self.write_text("docs/SESSIONS.md", "x\n" * LONG)
        code, _ = self._run("--check")
        self.assertEqual(code, 0)          # a big index (no [x]) is not reported

    def test_json_output(self):
        self.write_text("docs/ROADMAP.md", _cold(1, 1))
        code, out = self._run("--json")
        import json
        data = json.loads(out)
        self.assertFalse(data["clean"])
        f0 = data["findings"][0]
        self.assertEqual(f0["path"].replace("\\", "/"), "docs/ROADMAP.md")
        self.assertEqual(f0["cold_items"], 1)
        self.assertTrue(f0["gated"])
        self.assertFalse({"reference", "over"} & set(f0))


class HarvestIntegrity(_TreeTest):
    """The archive-integrity gate (Mike's ruling, 2026-07-22): the named
    archive stores (*-DONE.md, *-ARCHIVE.md) record finished history, so a
    live state marker there — [ ] / [~] / a ⏳ list item — gates under
    --check. The box grammar is a work-owed tri-state: [x] means no more
    work owed (delivered, superseded, or declined — disposition in the
    item's text), so [x]-with-commentary is the ONLY resting state. The
    four situations are the principal's own taxonomy from the design."""

    # Situation 1: a top-level non-completed item in the archive.
    def test_open_item_in_archive_gates(self):
        self.write_text("docs/ROADMAP-DONE.md", "- [x] fine\n- [ ] buried\n")
        f = self.finding("docs/ROADMAP-DONE.md")
        self.assertIsNotNone(f)
        self.assertTrue(f.gated)
        self.assertEqual(f.live_items, 1)

    # Situation 2: a live parent over all-completed children (the real
    # incident: delivered, never flipped — or a parent that was only ever a
    # heading; which remedy applies is the investigate step, not the scan).
    def test_live_parent_over_done_children_gates_on_parent(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        "- [ ] parent item\n"
                        "      - [x] child one DONE\n"
                        "      - [x] child two DONE\n")
        self.assertEqual(self.finding("docs/ROADMAP-DONE.md").live_items, 1)

    # Situation 3: a live parent with mixed children — every live line
    # counts, parent and children alike (a botched harvest, most likely).
    def test_live_parent_with_mixed_children_counts_each_live_line(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        "- [ ] parent item\n"
                        "      - [x] child done\n"
                        "      - [ ] child open\n"
                        "      - [~] child claimed\n")
        self.assertEqual(self.finding("docs/ROADMAP-DONE.md").live_items, 3)

    # Situation 4: a stray live child under a completed parent.
    def test_live_child_under_done_parent_gates(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        "- [x] parent DONE\n      - [ ] child open\n")
        self.assertEqual(self.finding("docs/ROADMAP-DONE.md").live_items, 1)

    def test_all_three_live_markers_gate(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        "- [ ] open\n- [~] claimed\n- ⏳ queued review\n")
        self.assertEqual(self.finding("docs/ROADMAP-DONE.md").live_items, 3)

    def test_superseded_archives_as_x_with_disposition_note(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        "- [x] old idea **dropped 2026-07-22: superseded by "
                        "the v2 design — no more work owed**\n")
        self.assertEqual(self.flagged(), [])

    def test_prose_backtick_and_fenced_mentions_do_not_fire(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        "taken from the `⏳` queue by a non-author\n"
                        "prose about the [ ] state and a [~] claim\n"
                        "```\n- [ ] quoted example\n- ⏳ quoted queue item\n```\n")
        self.assertEqual(self.flagged(), [])

    def test_sessions_archive_store_also_checked(self):
        self.write_text("docs/SESSIONS-ARCHIVE.md", "- [~] stranded claim\n")
        self.assertEqual(self.finding("docs/SESSIONS-ARCHIVE.md").live_items, 1)

    # HI-F1: the growth-store directory skip bounds METERING, never integrity —
    # a store inside `sessions/`, `_archive/`, etc. is checked wherever it
    # lives. Before the fix these were silently invisible and the clean banner
    # overclaimed ("archive stores hold no live markers" over files never read).
    def test_archive_store_inside_sessions_dir_still_checked(self):
        self.write_text("docs/sessions/SESSIONS-ARCHIVE.md", "- [ ] buried\n")
        f = self.finding("docs/sessions/SESSIONS-ARCHIVE.md")
        self.assertIsNotNone(f)
        self.assertTrue(f.gated)
        self.assertEqual(f.live_items, 1)

    def test_archive_store_inside_underscore_archive_dir_still_checked(self):
        self.write_text("docs/_archive/ROADMAP-DONE.md", "- [~] buried claim\n")
        self.assertEqual(
            self.finding("docs/_archive/ROADMAP-DONE.md").live_items, 1)

    def test_clean_archive_store_inside_skipped_dir_stays_silent(self):
        self.write_text("docs/_archive/ROADMAP-DONE.md", "- [x] finished\n")
        self.assertEqual(self.flagged(), [])

    # HA1: the HI-F1 bypass reaches growth-store dirs ONLY — a non-content
    # dir (vendored code, virtualenvs, VCS internals, caches) is never
    # scanned at all: a vendored package's store-named file is not this
    # repo's record, and integrity-checking it reds the build on a file the
    # repo owner doesn't own.
    def test_store_under_node_modules_never_scanned(self):
        self.write_text("node_modules/somepkg/ROADMAP-DONE.md",
                        "- [ ] vendor todo\n")
        self.assertEqual(self.flagged(), [])

    def test_store_under_venv_never_scanned(self):
        self.write_text(".venv/lib/NOTES-ARCHIVE.md", "- [~] venv claim\n")
        self.assertEqual(self.flagged(), [])

    # HI-F2: a fence still open at EOF gets no quoting immunity — the
    # swallowed tail is counted, fail-safe. A properly closed fence keeps
    # its contents quoted (the existing prose/fence test above).
    def test_unclosed_fence_does_not_swallow_live_markers(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        "```\nunclosed example\n- [ ] live after stray fence\n"
                        "- [~] another\n")
        self.assertEqual(self.finding("docs/ROADMAP-DONE.md").live_items, 2)

    # HA2: one stray delimiter shifts every pairing after it — a marker
    # between the stray fence and a later legit snippet was silently cleared
    # by the tail-only fix. Unbalanced delimiters at EOF now recount the
    # whole file with fences ignored, so the buried marker surfaces.
    def test_marker_between_stray_fence_and_later_snippet_counts(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        "```\n- [ ] buried real item\n```\n"
                        "ssh host uptime\n```\nprose tail\n")
        self.assertEqual(self.finding("docs/ROADMAP-DONE.md").live_items, 1)

    def test_archive_store_is_never_flagged_for_size(self):
        self.write_text("docs/ROADMAP-DONE.md", "- [x] done\n" + "x\n" * 3000)
        self.assertEqual(self.flagged(), [])

    def test_live_markers_on_the_roadmap_do_not_gate(self):
        self.write_text("docs/ROADMAP.md", _cold(n_open=3))
        self.assertEqual(self.flagged(), [])

    def test_allow_marker_exempts_archive_store(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        f"<!-- {sizescan.ALLOW_MARKER}: migration in flight -->\n"
                        "- [ ] deliberately parked here\n")
        self.assertEqual(self.flagged(), [])

    def test_check_exit_contract_gates_on_archive_marker(self):
        self.write_text("docs/ROADMAP-DONE.md", "- [ ] buried\n")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(
                sizescan.main(["--check", str(self.tmp), "--root", str(self.tmp)]), 1)
            self.assertEqual(
                sizescan.main([str(self.tmp), "--root", str(self.tmp)]), 0)


class UsageErrors(unittest.TestCase):
    def test_missing_path_is_error_not_pass(self):
        code = sizescan.main(["/no/such/path/xyz", "--root", "."])
        self.assertEqual(code, 2)

    def test_selftest_passes(self):
        self.assertEqual(sizescan._selftest(), 0)


class LinkedWorktreeSkipped(unittest.TestCase):
    """020/160 (E9): `_walk_files` must prune a directory whose `.git` entry
    is a regular FILE (`gitdir: <path>`, the linked-worktree/submodule
    marker) — not just one literally named `.git` that is a directory.
    Before this fix a session's own gitignored `.claude/worktrees/<name>/`
    grew into a full second checkout of the tree that the walk descended
    into anyway, double-reporting every file (measured in `faves`
    2026-08-15, the item's own reported symptom #3: sizescan double-reports
    the same files in the hook's own output)."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _found(self):
        return {str(p.relative_to(self.tmp))
                for p in sizescan._walk_files(self.tmp)}

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


_MARK = "sizescan" + ":allow"   # built from parts: no source line is a marker


class ScopedMarker(unittest.TestCase):
    """115/080: a header marker scoped to one kind exempts that kind only
    (AM4); since 115/270 the only kind a marker can still exempt is an archive
    store's `harvest-integrity`, so everything else it says is inert."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)

    def scan(self, marker):
        (self.tmp / "ROADMAP.md").write_text(
            f"<!-- {marker} -->\n" + _cold(n_open=5, n_done=2))
        (self.tmp / "ROADMAP-DONE.md").write_text(
            f"<!-- {marker} -->\n" + _cold(n_open=1, n_done=1))
        counts = {}
        found = {f.path: f for f in sizescan.scan_paths([self.tmp], self.tmp, counts)}
        return found, counts["files_allowed"]

    def test_size_advisory_scope_keeps_both_gates(self):
        # retired kind: read as scoped to something that no longer exists, so it
        # exempts neither the cold content nor the archive store
        found, allowed = self.scan(f"{_MARK}:size-advisory: long by design")
        hot = found["ROADMAP.md"]
        self.assertEqual((hot.cold_items, hot.gated), (2, True))
        self.assertIn("ROADMAP-DONE.md", found)
        self.assertEqual(allowed, 0)

    def test_cold_content_scope_no_longer_exempts_the_gate(self):
        # 115/270 a: it used to take the gate away; it takes nothing away
        found, _ = self.scan(f"{_MARK}:cold-content: harvested elsewhere")
        hot = found["ROADMAP.md"]
        self.assertEqual((hot.cold_items, hot.gated), (2, True))
        self.assertIn("ROADMAP-DONE.md", found)

    def test_harvest_integrity_scope_covers_only_the_archive_store(self):
        found, allowed = self.scan(f"{_MARK}:harvest-integrity: open on purpose")
        self.assertNotIn("ROADMAP-DONE.md", found)
        self.assertEqual(found["ROADMAP.md"].cold_items, 2)
        self.assertEqual(allowed, 1)       # only the store was exempted

    def test_the_unscoped_form_and_an_unknown_scope_exempt_only_the_archive_store(self):
        for marker in (f"{_MARK}: living doc", f"{_MARK}:living-doc: why"):
            found, allowed = self.scan(marker)
            self.assertEqual(set(found), {"ROADMAP.md"})   # the store is exempt
            hot = found["ROADMAP.md"]
            self.assertEqual((hot.cold_items, hot.gated), (2, True))
            self.assertEqual(allowed, 1)


class Allowances(unittest.TestCase):
    """GUARDS.md rule (c) — a marker with no reason is a mention."""

    def test_bare_marker_without_reason_is_not_an_allowance(self):
        self.assertIsNone(sizescan.parse_allow("# sizescan:allow"))
        self.assertIsNone(sizescan.parse_allow("# sizescan:allow:"))

    def test_marker_with_reason_allows(self):
        self.assertEqual("", sizescan.parse_allow("# sizescan:allow: an index"))


class BoundedMemory(unittest.TestCase):
    """020/380 — applying 020/370's bounded-memory fix to sizescan. Mike's
    ruling, verbatim: "it should not matter how much it scans it should no
    have this affect". Measured BEFORE this fix (see the board item's own
    before/after table): a growth-store file (`ROADMAP-DONE.md`, deliberately
    unbounded by design — it is where harvested content is meant to
    accumulate) drove ~110 MB of peak-RSS growth for a 23 MB larger input,
    via the old `p.read_text()` + repeated `text.splitlines()` passes in
    `count_lines`/`cold_item_count`/`live_item_count` — the same
    whole-file-held-more-than-once shape secretscan's `020/370` fixed.

    Runs the real CLI as a SUBPROCESS via `memprobe.run_and_measure` and
    reads peak RSS back from the kernel — `tracemalloc` only sees the
    Python heap, not the whole OS process (see `tools/memprobe.py`).

    Content is a big archive-store file with no harvest-integrity defects
    (`_scan_file_metrics` finds nothing to flag either way), so the two runs
    differ only in how many bytes there are to read."""

    SIZESCAN = str(TOOLS_DIR / "sizescan.py")
    SMALL_BYTES = 1 * 1024 * 1024
    LARGE_BYTES = 8 * 1024 * 1024
    # Grounded in the FIX's design (`ground-numeric-limits`), not fitted to a
    # measurement, and deliberately a LITERAL here rather than a reference to
    # `sizescan._READ_CHUNK_BYTES`/`_MAX_LINE_BYTES` — this test must still
    # MEASURE a real blow-up (not just fail an AttributeError at import) if
    # ever run against the pre-fix module, which carries neither constant.
    # The only per-file state the fix's `_scan_file_metrics` ever holds is
    # one read chunk in flight (1 MiB) plus one physical line capped at 8 KiB
    # (see `sizescan._iter_physical_lines`). Both runs produce a clean
    # (unflagged) file, so growth between them should be close to zero; 8x
    # that fixed per-file state leaves generous headroom for interpreter/
    # allocator noise while staying far below what the pre-fix whole-file-read
    # code showed for this size delta (measured, while building this fix, at
    # ~110 MB for a 23 MB delta — a fact recorded for context, not what set
    # this number).
    GROWTH_BOUND_BYTES = 8 * (1 * 1024 * 1024 + 8 * 1024)

    @staticmethod
    def _build(target_bytes: int, path: Path) -> None:
        with open(path, "w") as f:
            written = 0
            i = 0
            while written < target_bytes:
                line = f"- [x] harvested item number {i} — nothing live here\n"
                f.write(line)
                written += len(line)
                i += 1

    def _peak_rss_for(self, size_bytes: int) -> int:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        docs = tmp / "docs"
        docs.mkdir()
        self._build(size_bytes, docs / "ROADMAP-DONE.md")
        # Safety (020/370's own incident: a probe thrashed the principal's
        # machine doing exactly this kind of measurement): hard-kill well
        # short of the 1 GB line, and a ceiling so a regression that
        # reintroduces catastrophic behaviour fails the test instead of
        # hanging CI.
        result = memprobe.run_and_measure(
            [sys.executable, self.SIZESCAN, "--root", str(tmp), str(tmp)],
            timeout=60, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        self.assertEqual(0, result.returncode,
                         "an all-[x], no-live-marker archive store must not gate")
        return result.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_archive_store_size(self):
        small_peak = self._peak_rss_for(self.SMALL_BYTES)
        large_peak = self._peak_rss_for(self.LARGE_BYTES)
        growth = large_peak - small_peak
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for a "
            f"{(self.LARGE_BYTES - self.SMALL_BYTES) / 1e6:.1f} MB larger "
            f"archive store (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB) — memory is scaling with "
            "input size again (020/380).")


if __name__ == "__main__":
    unittest.main()
