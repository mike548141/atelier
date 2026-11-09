"""Stdlib-only tests for pdlistscan (no pytest needed): `python3 -m unittest`.

Board `160/630`, slice 3 of `320/810`. Real throwaway repos, because the scan
reads `.atelier-floor.json`, the list file and `git ls-files`. The date is
patched in process."""

import contextlib
import datetime
import io
import json
import subprocess
import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path

import pdlistscan as p

LIST = """# Personal data

## PD1 — the handle

- **Data:** `examplehandle`
- **Why held:** attribution.
- **Granted by:** his words.
- **May stand in:** `README.md`, `docs/records/*.md`, `docs/PERSONAL-DATA.md`.
"""

MARKER_LINE = "text <!-- leakscan:allow:email: a fixture address -->\n"


class Fixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="pdlistscan-test-")
        self.root = Path(self._tmp.name).resolve()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "test@example.com")  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
        self.git("config", "user.name", "Test")

    def tearDown(self):
        self._tmp.cleanup()

    def git(self, *args):
        subprocess.run(["git", "-C", str(self.root), *args], check=True,
                       capture_output=True, text=True)

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def config(self, visibility=None):
        d = {"docs": "docs"}
        if visibility:
            d["visibility"] = visibility
        self.write(".atelier-floor.json", json.dumps(d))

    def commit_all(self):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "c")

    def run_main(self, *argv, on=None):
        when = on if on is not None else p.PERSONAL_DATA_WARN_UNTIL - datetime.timedelta(days=30)
        out = io.StringIO()
        with unittest.mock.patch.object(p, "_utc_today", return_value=when), \
                contextlib.redirect_stdout(out):
            code = p.main(["--root", str(self.root), *argv])
        return code, out.getvalue()


class ScopeTest(Fixture):
    def test_a_private_repo_is_out_of_scope_and_says_so(self):
        self.config("private")
        self.write("a.md", MARKER_LINE)
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, out)
        self.assertIn("not in scope", out)

    def test_a_repo_with_no_visibility_key_is_out_of_scope(self):
        self.config()
        self.write("a.md", MARKER_LINE)
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, out)
        self.assertIn("not in scope", out)

    def test_a_repo_with_no_config_is_out_of_scope(self):
        self.write("a.md", MARKER_LINE)
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, out)

    def test_an_unreadable_config_is_a_broken_scan(self):
        self.write(".atelier-floor.json", "{not json")
        self.write("a.md", "x\n")
        self.commit_all()
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            code, _ = self.run_main()
        self.assertEqual(code, 2)


class PublicRepoTest(Fixture):
    def setUp(self):
        super().setUp()
        self.config("public")
        self.write("docs/PERSONAL-DATA.md", LIST)
        self.write("README.md", "hello\n")

    def test_clean_when_nothing_strays(self):
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, out)
        self.assertIn("clean", out)

    def test_a_missing_list_is_a_finding(self):
        (self.root / "docs/PERSONAL-DATA.md").unlink()
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 1, out)
        self.assertIn("no-list", out)

    def test_a_marker_in_a_named_place_is_fine(self):
        self.write("docs/records/a.md", MARKER_LINE)
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, out)

    def test_a_marker_in_an_unnamed_place_is_a_finding(self):
        self.write("docs/other.md", MARKER_LINE)
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 1, out)
        self.assertIn("unlisted-marker", out)
        self.assertIn("docs/other.md:1", out)

    def test_a_network_only_marker_is_not_a_finding(self):
        self.write("docs/other.md", "x <!-- leakscan:allow:ipv4: a doc range -->\n")
        self.commit_all()
        code, _ = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0)

    def test_a_listed_string_in_an_unnamed_place_is_a_finding(self):
        self.write("docs/other.md", "written by examplehandle today\n")
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 1, out)
        self.assertIn("unlisted-holder", out)
        self.assertIn("PD1", out)

    def test_a_listed_string_in_a_named_place_is_fine(self):
        self.write("docs/records/b.md", "by examplehandle\n")
        self.commit_all()
        code, _ = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0)

    def test_the_list_itself_is_not_read_for_its_own_strings(self):
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, out)

    def test_an_unpinned_entry_contributes_no_strings(self):
        self.write("docs/PERSONAL-DATA.md", LIST.replace(
            "`examplehandle`", "`Given` (not pinned to files by the test)"))
        self.write("docs/other.md", "Given goes here\n")
        self.commit_all()
        code, _ = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0)

    def test_tools_are_exempt_only_with_the_mechanism_present(self):
        self.write("tools/x.py", MARKER_LINE)
        self.commit_all()
        code, _ = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 1, "a child's tools/ is read")
        self.write("tools/leakscan.py", "# the scanner\n")
        self.commit_all()
        code, _ = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, "atelier's own fixtures are not counted")

    def test_an_untracked_file_is_not_read(self):
        self.commit_all()
        self.write("docs/untracked.md", MARKER_LINE)
        code, _ = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0)

    def test_it_warns_before_the_date_and_blocks_from_it(self):
        self.write("docs/other.md", MARKER_LINE)
        self.commit_all()
        before = p.PERSONAL_DATA_WARN_UNTIL - datetime.timedelta(days=1)
        code, out = self.run_main(on=before)
        self.assertEqual(code, 0, out)
        self.assertIn("blocking from", out)
        self.assertIn("pdlistscan advisory: 1 finding(s)", out)
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 1, out)
        self.assertIn("pdlistscan advisory: 0 finding(s)", out)

    def test_warn_passes_on_the_date(self):
        self.write("docs/other.md", MARKER_LINE)
        self.commit_all()
        code, out = self.run_main("--warn", on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, out)
        self.assertIn("pdlistscan advisory: 1 finding(s)", out)

    def test_json_shape(self):
        self.write("docs/other.md", MARKER_LINE)
        self.commit_all()
        code, out = self.run_main("--json", on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 1)
        d = json.loads(out)
        self.assertTrue(d["in_scope"])
        self.assertTrue(d["blocking"])
        self.assertEqual(d["findings"][0]["kind"], "unlisted-marker")


class CoverageLineTest(Fixture):
    """115/130: the run says what it opened, on the findings path as on the
    clean one; a repo that is not public says it is out of scope instead."""

    def test_clean_and_findings_runs_both_count_what_they_read(self):
        self.config("public")
        self.write("docs/PERSONAL-DATA.md", LIST)
        self.write("README.md", "hello\n")
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, out)
        # the floor config and the README; the list itself is never read
        self.assertIn("  coverage: 2 tracked file(s) opened \u00b7 2 line(s) read",
                      out)
        self.assertNotIn("scanned nothing", out)
        self.write("docs/other.md", MARKER_LINE)
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 1, out)
        self.assertIn("unlisted-marker", out)
        self.assertIn("coverage: 3 tracked file(s) opened", out)

    def test_a_private_repo_says_not_in_scope_with_no_alarm(self):
        self.config("private")
        self.write("a.md", MARKER_LINE)
        self.commit_all()
        code, out = self.run_main(on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual(code, 0, out)
        self.assertIn("  coverage: 0 tracked file(s) opened \u00b7 0 line(s) read "
                      "\u2014 not in scope here: this repo does not declare "
                      "public visibility.", out)
        self.assertNotIn("scanned nothing", out)

    def test_json_carries_the_same_coverage(self):
        self.config("public")
        self.write("docs/PERSONAL-DATA.md", LIST)
        self.write("README.md", "hello\n")
        self.commit_all()
        code, out = self.run_main("--json", on=p.PERSONAL_DATA_WARN_UNTIL)
        self.assertEqual({"files_opened": 2, "lines_read": 2,
                          "scanned_nothing": False, "in_scope": True},
                         json.loads(out)["coverage"])


class DateAndSelftest(unittest.TestCase):
    def test_personal_scopes_are_real_leakscan_rules(self):
        import leakscan
        names = {r.name for r in leakscan.STRUCTURAL + leakscan.WITHDRAWN} | {"local-term"}
        self.assertEqual(p.PERSONAL_SCOPES - names, set())

    def test_the_date_is_read_strictly_before(self):
        d = p.PERSONAL_DATA_WARN_UNTIL
        self.assertTrue(p.warn_only_today(d - datetime.timedelta(days=1)))
        self.assertFalse(p.warn_only_today(d))

    def test_selftest_passes(self):
        r = subprocess.run([sys.executable, p.__file__, "--selftest"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("selftest OK", r.stdout)


if __name__ == "__main__":
    unittest.main()
