"""Tests for tools/harvestscan.py — the roadmap-deletion guard (roadmap B4).

The failure this guards is the only one in its family that LOSES work: an item
removed from ROADMAP.md that arrives nowhere. `sizescan` catches the two
adjacent states, and both are visible in a single file; this one exists only as
a difference between two versions, which is why no existing check can see it.

The tests are shaped around the reason the obvious implementation was rejected.
Title-matching was measured at a near-total false-positive rate because a
healthy roadmap rewrites titles and re-homes items constantly — so the cases
that matter most here are the ones that must NOT fire: a retitle, a rewrite, an
absorption into a larger item, and a review pointer closing out.

Zero third-party deps, same as the rest of the suite.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import harvestscan  # noqa: E402

ITEM = ("**Schedule the conformance check.** floorfleet is the instrument that "
        "turns hoping the policy propagated into knowing it did, and nothing "
        "runs it automatically today. Four options were costed.")


def item(body: str, marker: str = "[ ]") -> str:
    return f"- {marker} {body}\n"


class MustNotFireTest(unittest.TestCase):
    """False positives are the whole risk. Every one of these is a HEALTHY edit
    that a naive implementation reports as a deletion."""

    def test_a_verbatim_harvest_survives(self):
        self.assertEqual(
            harvestscan.vanished(item(ITEM), [harvestscan.normalise(ITEM)]), [])

    def test_a_retitle_survives(self):
        """The case that makes title-matching useless: same work, new heading."""
        retitled = ITEM.replace("**Schedule the conformance check.**",
                                "**Put the conformance check on a schedule.**")
        self.assertEqual(
            harvestscan.vanished(item(ITEM),
                                 [harvestscan.normalise(retitled)]), [])

    def test_an_item_absorbed_into_a_larger_one_survives(self):
        """Why containment, not Jaccard. Items get merged and grown; Jaccard
        punishes that by the size of what was ADDED, so a healthy expansion
        reads as a deletion."""
        grown = (ITEM + " Additionally, here are four hundred further words of "
                 "new reasoning about tokens, runners, schedules, permissions, "
                 "credentials, rotation, blast radius and secret stores that "
                 "did not exist in the original item at all.")
        self.assertEqual(
            harvestscan.vanished(item(ITEM), [harvestscan.normalise(grown)]), [])

    def test_bookkeeping_churn_alone_does_not_read_as_deletion(self):
        """An item moving from queued to reviewed changes most of its words and
        none of its work. Measured: this drove 42% -> 31% of the firing rate."""
        before = ("**C1 — advisory takes a reason and an expiry.** "
                  "(claimed 2026-07-28-1233, wt: c1-advisory) An advisory "
                  "declaration can sit indefinitely, which is the honour it "
                  "manually decay in a new costume.")
        after = ("**C1 — advisory takes a reason and an expiry.** REVIEWED "
                 "2026-07-28, rule-4 cold pass, verdict 0 MAJOR, cycle closed. "
                 "An advisory declaration can sit indefinitely, the honour it "
                 "manually decay in a new costume.")
        self.assertEqual(
            harvestscan.vanished(item(before), [harvestscan.normalise(after)]),
            [])

    def test_a_review_pointer_closing_out_is_not_a_loss(self):
        """A pointer is refs-only by the ROADMAP's own definition, so it holds
        no work-content to lose, and it is SUPPOSED to disappear when its cycle
        closes. Reporting it is reporting the mechanism working."""
        pointer = ("**Review queued — the estate-root naming rule, widened.** "
                   "Self-authored doctrine so a rule-4 pass is owed; delta is "
                   "PROPAGATION.md and the intent record is the session entry.")
        self.assertEqual(harvestscan.vanished(item(pointer, "⏳"), []), [])
        # ...and the same body under an ordinary checkbox is still a pointer,
        # because the lead words say so.
        self.assertEqual(harvestscan.vanished(item(pointer), []), [])

    def test_an_item_too_short_to_fingerprint_is_skipped_not_guessed(self):
        self.assertEqual(harvestscan.vanished(item("fix the thing"), []), [])


class MustFireTest(unittest.TestCase):
    def test_an_item_with_no_surviving_relative_is_reported(self):
        unrelated = ("licence classifiers and SPDX headers in vendored source "
                     "files, trove metadata, proprietary LicenseRef modes")
        gone = harvestscan.vanished(item(ITEM),
                                    [harvestscan.normalise(unrelated)])
        self.assertEqual(len(gone), 1)
        self.assertIn("conformance", gone[0][1])

    def test_an_item_removed_with_nothing_else_present_is_reported(self):
        self.assertEqual(len(harvestscan.vanished(item(ITEM), [])), 1)


class ParseTest(unittest.TestCase):
    def test_all_four_state_markers_parse(self):
        text = "- [ ] one\n- [x] two\n- [~] three\n- ⏳ four\n"
        self.assertEqual(len(harvestscan.parse_items(text)), 4)

    def test_continuation_lines_belong_to_their_item(self):
        text = ("- [ ] the title\n"
                "      an indented continuation carrying the real content\n"
                "      and another line of it\n")
        items = harvestscan.parse_items(text)
        self.assertEqual(len(items), 1)
        self.assertIn("real content", items[0][2])

    def test_the_marker_is_carried_so_pointers_can_be_told_apart(self):
        self.assertEqual(harvestscan.parse_items("- ⏳ x\n")[0][1], "⏳")
        self.assertEqual(harvestscan.parse_items("- [x] y\n")[0][1], "[x]")


class SimilarityTest(unittest.TestCase):
    def test_containment_is_asymmetric_and_that_is_the_point(self):
        small, large = ["a", "b"], ["a", "b", "c", "d", "e", "f"]
        self.assertEqual(harvestscan.similarity(small, large), 1.0)
        self.assertLess(harvestscan.similarity(large, small), 1.0)

    def test_empty_never_matches(self):
        self.assertEqual(harvestscan.similarity([], ["a"]), 0.0)
        self.assertEqual(harvestscan.similarity(["a"], []), 0.0)


class PointerExclusionTest(unittest.TestCase):
    """HV2 — the exclusion is `pointerscan`'s test now, not a second copy.

    The copy that lived here read the marker or the item's first six words. The
    recorded corpus has four pointer shapes and that saw two, so the exclusion
    was forgiving items nothing then policed — a fail-open, and the reason the
    cold pass made these two build together."""

    def test_the_two_tools_cannot_disagree(self):
        """Delegation, proved by changing the answer at the source: narrow
        pointerscan's test and this file's exclusion narrows with it. A second
        copy here would pass every other test in this class and still drift."""
        import pointerscan
        original = pointerscan.is_pointer
        try:
            pointerscan.is_pointer = lambda marker, body: False
            self.assertFalse(harvestscan.is_pointer("⏳", "anything"))
        finally:
            pointerscan.is_pointer = original
        self.assertTrue(harvestscan.is_pointer("⏳", "anything"))

    def test_a_shape_the_old_copy_missed_is_now_excluded(self):
        """Shape (c): the obligation stated mid-body, in an emphasis run, with
        no marker glyph anywhere. Six-lead-words never saw it."""
        body = ("REVIEWED 2026-07-26: PASS-WITH-FINDINGS. **ADR 0008 review "
                "owed** — self-authored, so this session may not review it, "
                "and the delta is the enforcement propagation rollout.")
        self.assertEqual(harvestscan.vanished(item(body), []), [])

    def test_an_ordinary_work_item_is_still_reported(self):
        """The exclusion widened; it must not have swallowed the guard."""
        self.assertEqual(len(harvestscan.vanished(item(ITEM), [])), 1)


class GitBackedTest(unittest.TestCase):
    """HV1 + HV3 + HV4 need a real repo: the gate, the widened survivor search
    and the staged plane are all git questions."""

    def _repo(self, td):
        root = Path(td)
        def g(*a):
            subprocess.run(["git", "-C", str(root), *a], check=True,
                           capture_output=True)
        g("init", "-q", "-b", "main")
        g("config", "user.email", "t@example.invalid")  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
        g("config", "user.name", "T")
        g("config", "commit.gpgsign", "false")
        (root / "docs").mkdir()
        (root / "docs" / "sessions").mkdir()
        return root, g

    def test_the_index_is_what_the_hook_reads(self):
        """HV4. The old wording said "staged/working" as if interchangeable;
        survivors came from the working tree only. An item deleted from the
        roadmap and harvested in an UNSTAGED edit has not survived anything the
        commit is about to make."""
        with tempfile.TemporaryDirectory() as td:
            root, g = self._repo(td)
            (root / "docs" / "ROADMAP.md").write_text(item(ITEM))
            (root / "docs" / "ROADMAP-DONE.md").write_text("# done\n")
            g("add", "-A")
            g("commit", "-qm", "start")
            # Stage the removal; write the harvest but do NOT stage it.
            (root / "docs" / "ROADMAP.md").write_text("# empty\n")
            g("add", "docs/ROADMAP.md")
            (root / "docs" / "ROADMAP-DONE.md").write_text(item(ITEM))
            staged = harvestscan.scan(root, "HEAD", source=harvestscan.INDEX)
            self.assertEqual(len(staged), 1, "the index has no survivor")
            working = harvestscan.scan(root, "HEAD",
                                       source=harvestscan.WORKTREE)
            self.assertEqual(working, [], "the working tree does")

    def test_the_survivor_search_reaches_session_records(self):
        """HV3. The docstring claimed "anywhere in the tracked records" while
        the search was two files, so an item harvested into a session record
        read as vanished."""
        with tempfile.TemporaryDirectory() as td:
            root, g = self._repo(td)
            (root / "docs" / "ROADMAP.md").write_text(item(ITEM))
            g("add", "-A")
            g("commit", "-qm", "start")
            (root / "docs" / "ROADMAP.md").write_text("# empty\n")
            (root / "docs" / "sessions" / "2026-08-04-0000-x.md").write_text(
                f"## What happened\n\n{ITEM}\n")
            g("add", "-A")
            narrow = harvestscan.scan(root, "HEAD",
                                      stores=harvestscan.DEFAULT_RECORDS,
                                      source=harvestscan.INDEX)
            self.assertEqual(len(narrow), 1)
            wide = harvestscan.scan(root, "HEAD", source=harvestscan.INDEX)
            self.assertEqual(wide, [], "the session record IS the harvest")

    def test_a_harvest_written_as_PROSE_counts_as_a_survivor(self):
        """The half of HV3 that made the widening real. A harvest into a session
        record is almost never a checkbox item — it is a paragraph in a
        write-up — so widening the FILE list without widening the extractor was
        measurably inert: over the whole history it changed the firing set by
        exactly nothing."""
        with tempfile.TemporaryDirectory() as td:
            root, g = self._repo(td)
            (root / "docs" / "ROADMAP.md").write_text(item(ITEM))
            g("add", "-A")
            g("commit", "-qm", "start")
            (root / "docs" / "ROADMAP.md").write_text("# empty\n")
            (root / "docs" / "sessions" / "2026-08-04-0000-x.md").write_text(
                f"## What happened\n\n{ITEM}\n")     # prose, no bullet
            g("add", "-A")
            self.assertEqual(
                harvestscan.scan(root, "HEAD", source=harvestscan.INDEX), [])

    def test_the_roadmap_itself_is_read_as_items_never_as_prose(self):
        """Deliberately asymmetric. Fingerprinting the WATCHED roadmap's own
        prose would let a removed item 'survive' in a section heading's
        narration — a false negative in the one file the guard exists for."""
        with tempfile.TemporaryDirectory() as td:
            root, g = self._repo(td)
            (root / "docs" / "ROADMAP.md").write_text(item(ITEM))
            g("add", "-A")
            g("commit", "-qm", "start")
            # The item goes; a PARAGRAPH of the same words stays behind.
            (root / "docs" / "ROADMAP.md").write_text(f"## Notes\n\n{ITEM}\n")
            g("add", "-A")
            self.assertEqual(
                len(harvestscan.scan(root, "HEAD", source=harvestscan.INDEX)), 1)

    def test_only_tracked_files_count_as_survivors(self):
        """An untracked scratch file is not a record. Letting one count would
        be a guard passing on content nobody is committing."""
        with tempfile.TemporaryDirectory() as td:
            root, g = self._repo(td)
            (root / "docs" / "ROADMAP.md").write_text(item(ITEM))
            g("add", "-A")
            g("commit", "-qm", "start")
            (root / "docs" / "ROADMAP.md").write_text("# empty\n")
            g("add", "docs/ROADMAP.md")
            (root / "docs" / "sessions" / "scratch.md").write_text(ITEM)
            self.assertEqual(
                len(harvestscan.scan(root, "HEAD",
                                     source=harvestscan.INDEX)), 1)

    def test_net_line_loss_counts_removals_minus_additions(self):
        """HV1's scope is NET loss, not delete-only: the incident this guard
        exists for was +48/-184, and a delete-only scope would have missed it.
        The sign convention is what that turns on."""
        with tempfile.TemporaryDirectory() as td:
            root, g = self._repo(td)
            (root / "docs" / "ROADMAP.md").write_text("x\n" * 100)
            g("add", "-A")
            g("commit", "-qm", "start")
            (root / "docs" / "ROADMAP.md").write_text("y\n" * 20)
            g("add", "-A")
            loss = harvestscan.net_line_loss(
                root, harvestscan.GATE_RECORDS, "HEAD", harvestscan.INDEX)
            self.assertEqual(loss, 80)
            # ...and a commit that GROWS the roadmap has negative loss, so it
            # can never pass the gate however large it is.
            (root / "docs" / "ROADMAP.md").write_text("z\n" * 500)
            g("add", "-A")
            self.assertLess(harvestscan.net_line_loss(
                root, harvestscan.GATE_RECORDS, "HEAD", harvestscan.INDEX), 0)


class InvocationTest(unittest.TestCase):
    def _run(self, *args):
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "harvestscan.py"), *args],
            capture_output=True, text=True)

    def test_selftest_passes(self):
        self.assertEqual(self._run("--selftest").returncode, 0)

    def test_it_never_fails_a_build(self):
        """Advisory by construction, and now that it is IN the registry this is
        the contract it went in under (HV1: warn-only, never blocking)."""
        with tempfile.TemporaryDirectory() as td:
            r = self._run("--root", td, ".")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_the_bulk_gate_says_when_it_is_out_of_scope(self):
        """A guard that silently does nothing is indistinguishable from one
        that ran and found nothing. It says which."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            subprocess.run(["git", "-C", str(root), "init", "-q", "-b", "main"],
                           check=True, capture_output=True)
            r = self._run("--root", str(root), "--staged",
                          "--only-bulk-deletes")
            self.assertEqual(r.returncode, 0)
            self.assertIn("not in scope", r.stdout)

    def test_a_missing_root_is_an_error_not_a_silent_pass(self):
        self.assertEqual(self._run("--root", "/no/such/dir").returncode, 2)


if __name__ == "__main__":
    unittest.main()
