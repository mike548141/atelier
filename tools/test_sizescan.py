"""Stdlib-only tests for sizescan (no pytest needed): `python3 -m unittest`.

Pure-logic parts (count_lines, reference_for, cold_item_count) are unit-tested
directly. The end-to-end parts build a throwaway tree under a tmp dir and drive
scan_paths() / main(), so the metered-set selection (growth stores skipped,
reference docs unmetered, root-only READMEs), the escape hatches, and the
cold-content-gate-vs-advisory exit contract are proven against the real
filesystem, not a mock.

The gate model (Mike's 2026-07-20 ruling, reworked 2026-07-20): `--check` fails
ONLY on relocatable cold content — a completed `[x]` item on the hot path, whose
fix is a lossless move to ROADMAP-DONE.md. A file that is merely *long* from live
current-truth is advisory, never a build failure — cost is size × read-frequency,
and there is nothing to relocate in an all-open roadmap."""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import sizescan

R = sizescan.SIZE_REFERENCE["ROADMAP.md"]


def _cold(n_open=1, n_done=0):
    """A checkbox-worklog body with n_open live items and n_done cold `[x]` ones."""
    return "".join(["- [ ] open item\n"] * n_open + ["- [x] done item\n"] * n_done)


class CountLines(unittest.TestCase):
    def test_trailing_newline_not_counted_as_extra(self):
        self.assertEqual(sizescan.count_lines("a\nb\n"), 2)
        self.assertEqual(sizescan.count_lines("a\nb"), 2)

    def test_empty(self):
        self.assertEqual(sizescan.count_lines(""), 0)

    def test_crlf(self):
        self.assertEqual(sizescan.count_lines("a\r\nb\r\n"), 2)


class ReferenceFor(unittest.TestCase):
    def test_default_for_current_truth_basename(self):
        self.assertEqual(sizescan.reference_for("body\n", "ROADMAP.md"),
                         sizescan.SIZE_REFERENCE["ROADMAP.md"])

    def test_unmetered_basename_is_none(self):
        self.assertIsNone(sizescan.reference_for("body\n", "PRINCIPLES.md"))
        self.assertIsNone(sizescan.reference_for("body\n", "CHANGELOG.md"))

    def test_inline_override_wins(self):
        self.assertEqual(sizescan.reference_for("sizescan:budget=42\n", "ROADMAP.md"), 42)

    def test_inline_override_accepts_colon_and_space(self):
        self.assertEqual(sizescan.reference_for("<!-- sizescan:budget: 900 -->", "SESSIONS.md"), 900)
        self.assertEqual(sizescan.reference_for("sizescan:budget 55", "README.md"), 55)


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
    def test_over_reference_current_truth_flags_advisory(self):
        self.write("docs/ROADMAP.md", R + 1)
        f = self.finding("docs/ROADMAP.md")
        self.assertIsNotNone(f)
        self.assertFalse(f.gated)          # long but all-current: advisory, not gated
        self.assertEqual(f.cold_items, 0)

    def test_under_reference_no_cold_is_silent(self):
        self.write("docs/ROADMAP.md", R - 1)
        self.assertEqual(self.flagged(), [])

    def test_exactly_at_reference_is_silent(self):
        self.write("docs/ROADMAP.md", R)
        self.assertEqual(self.flagged(), [])

    def test_small_file_with_cold_content_flags_and_gates(self):
        # size is irrelevant — a done item on the hot path is what matters
        self.write_text("docs/ROADMAP.md", _cold(1, 2))
        f = self.finding("docs/ROADMAP.md")
        self.assertIsNotNone(f)
        self.assertTrue(f.gated)
        self.assertEqual(f.cold_items, 2)
        self.assertEqual(f.over, 0)        # small: no size advisory, just the gate

    def test_growth_stores_never_metered(self):
        self.write("docs/ROADMAP-DONE.md", 5000)
        self.write("docs/SPECS.md", 5000)
        self.write("CHANGELOG.md", 5000)
        self.assertEqual(self.flagged(), [])

    def test_reference_doc_not_metered(self):
        self.write("docs/PRINCIPLES.md", 5000)
        self.assertEqual(self.flagged(), [])

    def test_metered_basename_inside_growth_store_ignored(self):
        self.write("_archive/ARCHITECTURE.md", 5000)
        self.write("docs/reviews/README.md", 5000)
        self.assertEqual(self.flagged(), [])

    def test_root_readme_metered_nested_readme_not(self):
        self.write("README.md", R + 1)
        self.write("tools/README.md", 5000)
        self.assertEqual(self.flagged(), ["README.md"])

    def test_roadmap_metered_wherever_it_lives(self):
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

    def test_header_allow_marker_exempts_everything(self):
        # allow exempts BOTH the advisory and the cold-content gate
        self.write_text("docs/ROADMAP.md",
                        f"<!-- {sizescan.ALLOW_MARKER}: living doc -->\n" + _cold(1, 5))
        self.assertEqual(self.flagged(), [])

    def test_overlapping_paths_do_not_double_report(self):
        # F4: dedup by resolved path
        self.write_text("docs/ROADMAP.md", _cold(1, 1))
        findings = sizescan.scan_paths([self.tmp, self.tmp / "docs"], self.tmp)
        paths = [f.path.replace("\\", "/") for f in findings]
        self.assertEqual(paths.count("docs/ROADMAP.md"), 1)

    def test_budget_override_quiets_advisory_but_not_the_gate(self):
        # a huge budget silences the size nudge; it must NOT hide cold content
        self.write_text("docs/ROADMAP.md",
                        "<!-- sizescan:budget=100000 -->\n" + _cold(R, 2))
        f = self.finding("docs/ROADMAP.md")
        self.assertIsNotNone(f)
        self.assertEqual(f.over, 0)        # advisory quieted
        self.assertTrue(f.gated)           # gate stands
        self.assertEqual(f.cold_items, 2)

    def test_budget_override_silences_advisory_only_file(self):
        # a long all-current file with a grounded budget goes fully silent
        self.write_text("docs/ROADMAP.md",
                        "<!-- sizescan:budget=100000 -->\n" + _cold(R + 50, 0))
        self.assertEqual(self.flagged(), [])

    def test_sizescanignore_glob_skips(self):
        self.write_text("docs/ROADMAP.md", _cold(1, 5))
        (self.tmp / ".sizescanignore").write_text("docs/ROADMAP.md\n")
        self.assertEqual(self.flagged(), [])


class ExitContract(_TreeTest):
    def _run(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = sizescan.main([*args, "--root", str(self.tmp), str(self.tmp)])
        return code, buf.getvalue()

    def test_advisory_default_exit_zero_even_with_cold_content(self):
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
        # THE reversal: fulsome live current-truth is never a build failure
        self.write_text("docs/ROADMAP.md", _cold(R + 50, 0))
        code, out = self._run("--check")
        self.assertEqual(code, 0)
        self.assertIn("[size-advisory]", out)

    def test_check_exits_zero_when_no_cold_content(self):
        self.write_text("docs/ROADMAP.md", _cold(R - 1, 0))
        code, _ = self._run("--check")
        self.assertEqual(code, 0)

    def test_check_size_advisory_reports_but_exits_zero(self):
        self.write("ARCHITECTURE.md",
                   sizescan.SIZE_REFERENCE["ARCHITECTURE.md"] + 40)
        code, out = self._run("--check")
        self.assertEqual(code, 0)          # long judgement doc: never gate-failing
        self.assertIn("ARCHITECTURE.md", out)
        self.assertIn("[size-advisory]", out)

    def test_check_cold_content_wins_over_advisory(self):
        self.write("ARCHITECTURE.md",
                   sizescan.SIZE_REFERENCE["ARCHITECTURE.md"] + 40)   # advisory only
        self.write_text("docs/ROADMAP.md", _cold(1, 1))              # cold → gate
        code, out = self._run("--check")
        self.assertEqual(code, 1)
        self.assertIn("[cold-content, gated]", out)
        self.assertIn("[size-advisory]", out)

    def test_gate_is_cold_content_not_a_static_file_set(self):
        # Pin the doctrine: gating is driven by relocatable cold content, so a
        # long all-current ROADMAP/SESSIONS does not gate, but any file's [x]
        # items would. There is no static GATED set to drift.
        self.assertFalse(hasattr(sizescan, "GATED"))
        self.write_text("docs/SESSIONS.md", "x\n" * (sizescan.SIZE_REFERENCE["SESSIONS.md"] + 5))
        code, _ = self._run("--check")
        self.assertEqual(code, 0)          # a big index (no [x]) is advisory only

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

    # HI-F2: a fence still open at EOF gets no quoting immunity — the
    # swallowed tail is counted, fail-safe. A properly closed fence keeps
    # its contents quoted (the existing prose/fence test above).
    def test_unclosed_fence_does_not_swallow_live_markers(self):
        self.write_text("docs/ROADMAP-DONE.md",
                        "```\nunclosed example\n- [ ] live after stray fence\n"
                        "- [~] another\n")
        self.assertEqual(self.finding("docs/ROADMAP-DONE.md").live_items, 2)

    def test_archive_store_never_size_metered(self):
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


if __name__ == "__main__":
    unittest.main()
