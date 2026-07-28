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


class InvocationTest(unittest.TestCase):
    def _run(self, *args):
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "harvestscan.py"), *args],
            capture_output=True, text=True)

    def test_selftest_passes(self):
        self.assertEqual(self._run("--selftest").returncode, 0)

    def test_it_never_fails_a_build(self):
        """Advisory by construction. It is not wired anywhere yet, and if it
        ever is, this is the contract it goes in under."""
        with tempfile.TemporaryDirectory() as td:
            r = self._run("--root", td, ".")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_missing_root_is_an_error_not_a_silent_pass(self):
        self.assertEqual(self._run("--root", "/no/such/dir").returncode, 2)


if __name__ == "__main__":
    unittest.main()
