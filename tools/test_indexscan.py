"""Tests for indexscan — a hand-maintained index names every file it maps.

Board `200/010`. Covers both directions (unlisted here; listed-but-missing
deferred to linkscan, pinned below so the deferral cannot rot silently), the
`exclude=`/`before=` scope, the allow marker and its staleness, the config
errors `--warn` must never soften, the undeclared-repo pass that makes the
registry line safe to float to every child, and the registry wiring itself.
Stdlib only.
"""

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import floor  # noqa: E402
import indexscan  # noqa: E402
import linkscan  # noqa: E402


def run(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = indexscan.main(argv)
    return code, out.getvalue(), err.getvalue()


class Fixture(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name).resolve()

    def tearDown(self):
        self._td.cleanup()

    def write(self, rel, text="x\n"):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def scan(self):
        tally = indexscan.Tally()
        findings = indexscan.scan_paths([self.root], self.root, tally)
        return sorted((f.kind, f.entry) for f in findings), tally


class Unlisted(Fixture):
    def test_an_unlisted_file_is_a_finding_and_a_linked_one_is_not(self):
        self.write("docs/log/a.md")
        self.write("docs/log/b.md")
        self.write("docs/LOG.md", "# Log\n<!-- indexscan:maps dir=log match=*.md -->\n"
                   "- [a](log/a.md)\n")
        got, tally = self.scan()
        self.assertEqual(got, [("unlisted", "docs/log/b.md")])
        self.assertEqual((tally.indexes, tally.declarations, tally.entries), (1, 1, 2))

    def test_a_code_span_names_a_catalogue_entry(self):
        self.write("tools/one.py")
        self.write("tools/two.py")
        self.write("tools/README.md", "# t\n<!-- indexscan:maps dir=. match=*.py -->\n"
                   "## `one.py` — first\n| `tools/two.py --flag` | second |\n")
        got, _ = self.scan()
        self.assertEqual(got, [])

    def test_a_directory_entry_is_listed_by_a_link_into_it(self):
        self.write("inst/tool/README.md")
        self.write("inst/other/main.py")
        self.write("inst/README.md", "# i\n<!-- indexscan:maps dir=. match=* -->\n"
                   "[tool](tool/README.md)\n")
        got, _ = self.scan()
        self.assertEqual(got, [("unlisted", "inst/other")])

    def test_the_index_file_itself_is_never_an_entry(self):
        self.write("d/README.md", "# d\n<!-- indexscan:maps dir=. match=*.md -->\n")
        got, _ = self.scan()
        self.assertEqual(got, [])

    def test_a_fenced_link_is_an_example_not_a_listing(self):
        self.write("d/x/a.md")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=x match=*.md -->\n"
                   "```\n[a](x/a.md)\n```\n")
        got, _ = self.scan()
        self.assertEqual(got, [("unlisted", "d/x/a.md")])

    def test_a_root_relative_link_resolves_against_root(self):
        self.write("d/x/a.md")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=x match=*.md -->\n"
                   "[a](/d/x/a.md)\n")
        got, _ = self.scan()
        self.assertEqual(got, [])

    def test_several_declarations_in_one_index(self):
        self.write("d/a/1.md")
        self.write("d/b/2.md")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=a match=*.md -->\n"
                   "<!-- indexscan:maps dir=b match=*.md -->\n[1](a/1.md)\n")
        got, tally = self.scan()
        self.assertEqual(got, [("unlisted", "d/b/2.md")])
        self.assertEqual(tally.declarations, 2)

    def test_a_vanished_directory_is_a_finding_not_a_crash(self):
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=gone match=*.md -->\n")
        got, _ = self.scan()
        self.assertEqual(got, [("missing-dir", "d/gone")])

    def test_findings_exit_1_and_warn_exits_0(self):
        self.write("d/x/a.md")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=x match=*.md -->\n")
        self.assertEqual(run(["--root", str(self.root)])[0], 1)
        code, out, _ = run(["--warn", "--root", str(self.root)])
        self.assertEqual(code, 0)
        self.assertIn("unlisted", out)
        self.assertIn("advisory only", out)

    def test_json_carries_the_counts(self):
        self.write("d/x/a.md")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=x match=*.md -->\n")
        code, out, _ = run(["--json", "--root", str(self.root)])
        doc = json.loads(out)
        self.assertFalse(doc["clean"])
        self.assertEqual(doc["checked"]["declarations"], 1)
        self.assertEqual(set(doc["suppressed"]),
                         {"by_allow_marker", "by_exclude", "by_before",
                          "files_by_ignore_glob"})

    def test_ignored_files_inside_git_are_not_entries(self):
        """The shared walk is git-aware: a gitignored file can never be
        committed, so it can never be an entry an index owes a line to."""
        if subprocess.run(["git", "--version"], capture_output=True).returncode:
            self.skipTest("git unavailable")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.write(".gitignore", "*.tmp\n")
        self.write("d/x/a.md")
        self.write("d/x/scratch.tmp")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=x match=* -->\n[a](x/a.md)\n")
        got, _ = self.scan()
        self.assertEqual(got, [])


class ListedButMissingIsLinkscans(Fixture):
    """The other direction is deferred, not dropped: a dangling index link is
    linkscan's finding (enforced, both planes). Pinned here so a change to
    either tool that opens the gap reds this test."""

    def test_a_dangling_index_link_is_caught_by_linkscan_not_indexscan(self):
        self.write("d/x/a.md")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=x match=*.md -->\n"
                   "[a](x/a.md)\n[gone](x/gone.md)\n")
        got, _ = self.scan()
        self.assertEqual(got, [])
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = linkscan.main(["--root", str(self.root), str(self.root / "d")])
        self.assertEqual(code, 1)
        self.assertIn("gone.md", out.getvalue())


class Exclusion(Fixture):
    def test_exclude_glob_is_counted_not_reported(self):
        self.write("d/x/a.md")
        self.write("d/x/template.md")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=x match=*.md "
                   "exclude=template.md -->\n[a](x/a.md)\n")
        got, tally = self.scan()
        self.assertEqual(got, [])
        self.assertEqual(tally.by_exclude, 1)

    def test_before_makes_old_dated_records_blameless(self):
        self.write("d/x/2026-01-05-old.md")
        self.write("d/x/2026-03-01-new.md")
        self.write("d/x/undated.md")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=x match=*.md "
                   "before=2026-02-01 -->\n")
        got, tally = self.scan()
        self.assertEqual(got, [("unlisted", "d/x/2026-03-01-new.md"),
                               ("unlisted", "d/x/undated.md")])
        self.assertEqual(tally.by_before, 1)


class AllowMarker(Fixture):
    def _index(self, marker):
        self.write("d/x/a.md")
        self.write("d/x/b.md")
        self.write("d/I.md", "# i\n<!-- indexscan:maps dir=x match=*.md -->\n"
                   f"{marker}\n[a](x/a.md)\n")

    def test_a_reasoned_marker_exempts_exactly_one_entry(self):
        self._index("<!-- indexscan:allow: b.md owed by a fixture finding -->")
        got, tally = self.scan()
        self.assertEqual(got, [])
        self.assertEqual(tally.by_marker, 1)

    def test_a_marker_with_no_reason_exempts_nothing(self):
        self._index("<!-- indexscan:allow: b.md -->")
        got, tally = self.scan()
        self.assertEqual(got, [("unlisted", "d/x/b.md")])
        self.assertEqual(tally.by_marker, 0)

    def test_a_marker_for_a_listed_entry_is_stale(self):
        self._index("<!-- indexscan:allow: a.md was owed, now listed -->\n[b](x/b.md)")
        got, _ = self.scan()
        self.assertEqual(got, [("stale-allow", "a.md")])

    def test_a_marker_for_a_missing_entry_is_stale(self):
        self._index("<!-- indexscan:allow: nope.md never existed -->\n[b](x/b.md)")
        got, _ = self.scan()
        self.assertEqual(got, [("stale-allow", "nope.md")])

    def test_the_shared_grammar_parses_it(self):
        self.assertEqual(indexscan.parse_allow("indexscan:allow: f.py why so"),
                         ("f.py", "why so"))
        self.assertIsNone(indexscan.parse_allow("indexscan:allow: <entry> <reason>"))
        self.assertIsNone(indexscan.parse_allow("indexscan:allow:"))


class Declarations(Fixture):
    def test_quoted_syntax_is_not_a_declaration(self):
        self.write("d/x/a.md")
        self.write("d/I.md", "# i\nWrite `<!-- indexscan:maps dir=x match=*.md -->`.\n"
                   "```\n<!-- indexscan:maps dir=x match=*.md -->\n```\n")
        got, tally = self.scan()
        self.assertEqual(got, [])
        self.assertEqual(tally.declarations, 0)

    def test_config_errors_exit_2_even_under_warn(self):
        cases = {
            "unknown key": "<!-- indexscan:maps dir=x match=*.md exlude=y -->",
            "missing match": "<!-- indexscan:maps dir=x -->",
            "escapes root": "<!-- indexscan:maps dir=../../.. match=* -->",
            "absolute dir": "<!-- indexscan:maps dir=/etc match=* -->",
            "bad date": "<!-- indexscan:maps dir=x match=* before=2026-02-30 -->",
            "not key=value": "<!-- indexscan:maps dir=x match=* stray -->",
            "unclosed": "<!-- indexscan:maps dir=x match=*",
            "repeated key": "<!-- indexscan:maps dir=x dir=y match=* -->",
        }
        for label, line in cases.items():
            with self.subTest(label):
                self.write("d/I.md", f"# i\n{line}\n")
                (self.root / "d" / "x").mkdir(parents=True, exist_ok=True)
                code, _, err = run(["--warn", "--root", str(self.root)])
                self.assertEqual(code, 2, err)
                self.assertIn("d/I.md:2", err)

    def test_an_unreasoned_ignore_glob_exits_2(self):
        self.write(".indexscanignore", "fixtures/\n")
        self.assertEqual(run(["--root", str(self.root)])[0], 2)

    def test_a_reasoned_ignore_glob_skips_a_fixture_index(self):
        self.write(".indexscanignore", "fixtures/  # quotes the syntax raw\n")
        self.write("fixtures/I.md", "<!-- indexscan:maps dir=gone match=* -->\n")
        got, tally = self.scan()
        self.assertEqual(got, [])
        self.assertEqual(tally.files_by_glob, 1)

    def test_a_missing_path_argument_exits_2(self):
        self.assertEqual(run(["--root", str(self.root), "nope"])[0], 2)


class UndeclaredRepo(Fixture):
    """Children float on floor.py@main: the registry line reaches every child
    on its next run. It must check nothing — and pass — until a child
    declares an index."""

    def test_an_undeclared_repo_passes_and_says_it_checked_nothing(self):
        self.write("README.md", "# r\n[a](docs/a.md)\n")
        self.write("docs/a.md")
        self.write("docs/sessions/2026-01-01-x.md")
        for argv in (["--root", str(self.root)],
                     ["--warn", "--root", str(self.root), str(self.root)]):
            code, out, _ = run(argv)
            self.assertEqual(code, 0)
            self.assertIn("no index declares", out)
            self.assertIn("0 declaration(s)", out)

    def test_the_floor_runs_it_clean_on_an_undeclared_repo(self):
        self.write("docs/a.md", "# a\n")
        for plane in ("ci", "hook"):
            with self.subTest(plane=plane):
                if plane == "hook":
                    subprocess.run(["git", "init", "-q", str(self.root)], check=True)
                r = subprocess.run(
                    [sys.executable, str(TOOLS_DIR / "floor.py"), "--plane", plane,
                     "--root", str(self.root), "--tools", str(TOOLS_DIR), "--json"],
                    capture_output=True, text=True, cwd=self.root)
                results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
                self.assertEqual(results["indexscan"]["state"], "warn-only")
                self.assertEqual(results["indexscan"]["rc"], 0, r.stderr)


class Registry(unittest.TestCase):
    def test_registered_warn_only_on_both_planes(self):
        s = floor.BY_NAME["indexscan"]
        for argv in (s.hook, s.ci, s.advisory):
            self.assertIn("--warn", argv)
        self.assertTrue(s.warns_only("hook") and s.warns_only("ci"))
        self.assertEqual(s.default_scope, "root")
        self.assertFalse(s.opt_in)

    def test_selftest_passes(self):
        r = subprocess.run([sys.executable, str(TOOLS_DIR / "indexscan.py"),
                            "--selftest"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class AtelierAdoption(unittest.TestCase):
    """atelier declares its own indexes (the census named them). Pinned so a
    declaration deleted in passing is noticed — an index that silently stops
    declaring is a check that silently stops running."""

    def test_atelier_declares_its_four_indexes(self):
        repo = TOOLS_DIR.parent
        for rel in ("docs/decisions/README.md", "tools/README.md",
                    "instruments/README.md", "docs/SESSIONS.md"):
            with self.subTest(index=rel):
                decls, _ = indexscan.discover(repo / rel, rel)
                self.assertTrue(decls, f"{rel} carries no indexscan:maps line")


if __name__ == "__main__":
    unittest.main()
