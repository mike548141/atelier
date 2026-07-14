"""Stdlib-only tests for sizescan (no pytest needed): `python3 -m unittest`.

Pure-logic parts (count_lines, budget_for) are unit-tested directly. The
end-to-end parts build a throwaway tree under a tmp dir and drive scan_paths() /
main(), so the budgeted-set selection (growth stores skipped, reference docs
unbudgeted, root-only READMEs), the escape hatches, and the advisory-vs-`--check`
exit contract are proven against the real filesystem, not a mock."""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import sizescan


class CountLines(unittest.TestCase):
    def test_trailing_newline_not_counted_as_extra(self):
        self.assertEqual(sizescan.count_lines("a\nb\n"), 2)
        self.assertEqual(sizescan.count_lines("a\nb"), 2)

    def test_empty(self):
        self.assertEqual(sizescan.count_lines(""), 0)

    def test_crlf(self):
        self.assertEqual(sizescan.count_lines("a\r\nb\r\n"), 2)


class BudgetFor(unittest.TestCase):
    def test_default_for_current_truth_basename(self):
        self.assertEqual(sizescan.budget_for("body\n", "ROADMAP.md"),
                         sizescan.DEFAULT_BUDGETS["ROADMAP.md"])

    def test_unbudgeted_basename_is_none(self):
        self.assertIsNone(sizescan.budget_for("body\n", "PRINCIPLES.md"))
        self.assertIsNone(sizescan.budget_for("body\n", "CHANGELOG.md"))

    def test_inline_override_wins(self):
        self.assertEqual(sizescan.budget_for("sizescan:budget=42\n", "ROADMAP.md"), 42)

    def test_inline_override_accepts_colon_and_space(self):
        self.assertEqual(sizescan.budget_for("<!-- sizescan:budget: 900 -->", "SESSIONS.md"), 900)
        self.assertEqual(sizescan.budget_for("sizescan:budget 55", "README.md"), 55)


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

    def flagged(self):
        return sorted(f.path.replace("\\", "/")
                      for f in sizescan.scan_paths([self.tmp], self.tmp))


class Selection(_TreeTest):
    def test_over_budget_current_truth_flags(self):
        self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] + 1)
        self.assertIn("docs/ROADMAP.md", self.flagged())

    def test_under_budget_passes(self):
        self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] - 1)
        self.assertEqual(self.flagged(), [])

    def test_exactly_at_budget_passes(self):
        self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"])
        self.assertEqual(self.flagged(), [])

    def test_growth_stores_never_budgeted(self):
        big = 5000
        self.write("docs/ROADMAP-DONE.md", big)
        self.write("docs/SPECS.md", big)
        self.write("CHANGELOG.md", big)
        self.assertEqual(self.flagged(), [])

    def test_reference_doc_not_budgeted(self):
        self.write("docs/PRINCIPLES.md", 5000)
        self.assertEqual(self.flagged(), [])

    def test_budgeted_basename_inside_growth_store_ignored(self):
        # an ARCHITECTURE.md snapshotted under _archive/ is history, not current
        self.write("_archive/ARCHITECTURE.md", 5000)
        self.write("docs/reviews/README.md", 5000)
        self.assertEqual(self.flagged(), [])

    def test_root_readme_budgeted_nested_readme_not(self):
        self.write("README.md", sizescan.DEFAULT_BUDGETS["README.md"] + 1)
        self.write("tools/README.md", 5000)
        self.assertEqual(self.flagged(), ["README.md"])

    def test_roadmap_budgeted_wherever_it_lives(self):
        # singular-by-name files aren't root-only: docs/ROADMAP.md still counts
        self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] + 1)
        self.assertEqual(self.flagged(), ["docs/ROADMAP.md"])


class Hatches(_TreeTest):
    def test_allow_marker_exempts_file(self):
        p = self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] + 50)
        p.write_text(f"<!-- {sizescan.ALLOW_MARKER}: living doc -->\n" + p.read_text())
        self.assertEqual(self.flagged(), [])

    def test_inline_budget_override_raises_ceiling(self):
        p = self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] + 50)
        p.write_text("<!-- sizescan:budget=100000 -->\n" + p.read_text())
        self.assertEqual(self.flagged(), [])

    def test_sizescanignore_glob_skips(self):
        self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] + 50)
        (self.tmp / ".sizescanignore").write_text("docs/ROADMAP.md\n")
        self.assertEqual(self.flagged(), [])


class ExitContract(_TreeTest):
    def _run(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = sizescan.main([*args, "--root", str(self.tmp), str(self.tmp)])
        return code, buf.getvalue()

    def test_advisory_default_exit_zero_even_when_over(self):
        self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] + 1)
        code, out = self._run()
        self.assertEqual(code, 0)          # advisory: reports but does not fail
        self.assertIn("over budget", out)

    def test_check_flag_exits_one_when_over(self):
        self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] + 1)
        code, _ = self._run("--check")
        self.assertEqual(code, 1)          # opt-in gate: teeth

    def test_check_flag_exits_zero_when_clean(self):
        self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] - 1)
        code, _ = self._run("--check")
        self.assertEqual(code, 0)

    def test_json_output(self):
        self.write("docs/ROADMAP.md", sizescan.DEFAULT_BUDGETS["ROADMAP.md"] + 1)
        code, out = self._run("--json")
        import json
        data = json.loads(out)
        self.assertFalse(data["clean"])
        self.assertEqual(data["findings"][0]["path"].replace("\\", "/"), "docs/ROADMAP.md")


class UsageErrors(unittest.TestCase):
    def test_missing_path_is_error_not_pass(self):
        # a typo'd path scanning nothing must never read as a clean pass
        code = sizescan.main(["/no/such/path/xyz", "--root", "."])
        self.assertEqual(code, 2)

    def test_selftest_passes(self):
        self.assertEqual(sizescan._selftest(), 0)


if __name__ == "__main__":
    unittest.main()
