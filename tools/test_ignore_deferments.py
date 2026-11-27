"""Stdlib-only tests for the `review-by` reader in the eleven ignore-file
scanners that adopted it after `wrapscan` (board `110/060`, slice 2).

`wrapscan` has its own class in `test_wrapscan.py`; this module runs the same
five checks over every other adopter, so a scanner that loses the wiring fails
by name:

  - the count line prints every run, known zeros included;
  - a lapsed date and an unreadable date each print a 🟡 line, a future date
    prints none;
  - warn-only: the exit status is exactly what it is with no dates at all,
    both on a clean tree and on a tree the scanner blocks;
  - `--json` carries `deferments`;
  - an unreasoned glob still refuses first (exit 2).

`LineMarkerAdopters` runs the line-marker form (part 4, a `review-by` in a
`<guard>:allow:` marker's reason) over the eight scanners that read it, and
`MarkerReviewByReader` pins the shared reader.

Run: `python3 -m unittest discover -s tools -p test_ignore_deferments.py`.
"""

import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import allowmarker  # noqa: E402
import conflictscan  # noqa: E402
import datescan  # noqa: E402
import indexscan  # noqa: E402
import leakscan  # noqa: E402
import licenscan  # noqa: E402
import linkscan  # noqa: E402
import pathscan  # noqa: E402
import secretscan  # noqa: E402
import sizescan  # noqa: E402
import spellscan  # noqa: E402
import stampscan  # noqa: E402
import wrapscan  # noqa: E402

# The ignore file's lines. Line numbers matter: the assertions below name them.
#   2  lapsed (stanza above the glob)    4  future (trailing reason)
#   7  unreadable                        10 plain reason, no date
DATED = ("# drafts, fix them. review-by: 2020-01-01\ndocs/drafts/\n\n"
         "docs/later/  # review-by: 2999-12-31\n\n"
         "# review-by: soon\ndocs/bad/\n\n# plain reason\ndocs/plain/\n")
PLAIN = "# plain reason\ndocs/plain/\n"


def _write(root, rel, text):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def _clean_docs(root):
    _write(root, "docs/ok.md", "A short, plain line.\n")


# Per scanner: the module, its ignore file, the argv for a run over `root`, a
# builder for a clean tree and one for a tree the scanner blocks on (None where
# the scanner is report-only by default and a block needs a flag, noted).
def _argv_root_flag(root, *extra):
    return ["--root", str(root), *extra]


def _dirty_conflict(root):
    _write(root, "docs/bad.md", "<<<<<<< HEAD\nx\n=======\ny\n>>>>>>> b\n")


def _dirty_date(root):
    _write(root, "docs/bad.md", "We did it yesterday.\n")


def _dirty_link(root):
    _write(root, "docs/bad.md", "See [x](missing.md).\n")


def _dirty_path(root):
    _write(root, "docs/bad.md", "See `docs/nope/missing.md`.\n")


def _dirty_spell(root):
    _write(root, "docs/bad.md", "The color of it.\n")


def _dirty_secret(root):
    # Built from pieces so this file's own text trips neither secret scanner.
    token = "ghp_" + "a1B2c3D4e5F6" + "g7H8i9J0k1L2" + "m3N4o5P6q7R8"
    _write(root, "a.txt", f'key = "{token}"\n')


def _dirty_leak(root):
    addr = "someone.real" + "@" + "gmail" + ".com"   # pieces: see above
    _write(root, "b.txt", f"contact: {addr}\n")


def _licence_tree(root):
    _write(root, "LICENSE", "MIT License\n\nPermission is hereby granted, "
                            "free of charge, to any person obtaining a copy\n")


def _dirty_licence(root):
    _licence_tree(root)
    _write(root, "x.py", "# SPDX-License-Identifier: GPL-3.0-only\n")  # licenscan:allow: test fixture, not a real header


def _dirty_index(root):
    _write(root, "docs/log/a.md", "x\n")
    _write(root, "docs/log/b.md", "x\n")
    _write(root, "docs/LOG.md", "# Log\n<!-- indexscan:maps dir=log match=*.md -->\n"
                                "- [a](log/a.md)\n")


def _dirty_size(root):
    _write(root, "docs/ROADMAP.md", "- [ ] open\n- [x] done one\n- [x] done two\n")


def _dirty_stamp(root):
    _write(root, "docs/PARENT.md", "<!-- floor:begin -->\n- one\n- two\n<!-- floor:end -->\n")
    _write(root, "docs/child.md",
           "<!-- stamp:begin source=docs/PARENT.md region=floor -->\n"
           "- one\n- changed\n<!-- stamp:end -->\n")


def _spec(name, mod, ignore, dirty, argv=None, clean=_clean_docs, check=False):
    return dict(name=name, mod=mod, ignore=ignore, dirty=dirty, clean=clean,
                argv=argv or (lambda root, extra=(): _argv_root_flag(root, *extra)),
                check=check)


def _argv_licence(root, extra=()):
    return [*extra, str(root)]


def _argv_size(root, extra=()):
    return ["--root", str(root), "--check", *extra]


def _argv_leak(root, extra=()):
    # An empty local-terms file: never read the machine's own list.
    terms = root.parent / (root.name + "-terms.txt")
    terms.write_text("", encoding="utf-8")
    return ["--root", str(root), "--terms", str(terms), *extra]


SPECS = [
    _spec("conflictscan", conflictscan, ".conflictscanignore", _dirty_conflict),
    _spec("datescan", datescan, ".datescanignore", _dirty_date),
    _spec("indexscan", indexscan, ".indexscanignore", _dirty_index),
    _spec("leakscan", leakscan, ".leakscanignore", _dirty_leak, argv=_argv_leak),
    _spec("licenscan", licenscan, ".licenscanignore", _dirty_licence,
          argv=_argv_licence, clean=_licence_tree),
    _spec("linkscan", linkscan, ".linkscanignore", _dirty_link),
    _spec("pathscan", pathscan, ".pathscanignore", _dirty_path),
    _spec("secretscan", secretscan, ".secretscanignore", _dirty_secret),
    _spec("sizescan", sizescan, ".sizescanignore", _dirty_size, argv=_argv_size),
    _spec("spellscan", spellscan, ".spellscanignore", _dirty_spell),
    _spec("stampscan", stampscan, ".stampscanignore", _dirty_stamp),
]


class Adopters(unittest.TestCase):
    """One tree per scan; every adopter through the same checks."""

    def _tree(self, spec, dirty=False):
        root = Path(tempfile.mkdtemp(prefix=f"{spec['name']}-reviewby-")).resolve()
        self.addCleanup(shutil.rmtree, root, True)
        self.addCleanup(lambda: (root.parent / (root.name + "-terms.txt")).unlink(
            missing_ok=True))
        spec["clean"](root)
        if dirty:
            spec["dirty"](root)
        return root

    def _run(self, spec, root, *extra):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = spec["mod"].main(spec["argv"](root, extra))
        return rc, out.getvalue()

    def test_summary_counts_dated_lapsed_and_malformed(self):
        for spec in SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                (root / spec["ignore"]).write_text(DATED, encoding="utf-8")
                rc, out = self._run(spec, root)
                self.assertEqual(0, rc, out)
                self.assertIn("  deferments: 2 deferment(s) with review-by · "
                              "1 lapsed · 1 malformed", out)
                self.assertIn(f"🟡 {spec['ignore']}:2 'docs/drafts/' review-by "
                              "2020-01-01 LAPSED", out)
                self.assertIn(f"🟡 {spec['ignore']}:7 'docs/bad/' review-by "
                              "unreadable: 'soon'", out)
                # The future date and the plain reason are quiet.
                self.assertNotIn("docs/later/", out)
                self.assertNotIn("docs/plain/", out)

    def test_a_future_date_alone_is_quiet(self):
        for spec in SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                (root / spec["ignore"]).write_text(
                    "docs/later/  # review-by: 2999-12-31\n", encoding="utf-8")
                rc, out = self._run(spec, root)
                self.assertEqual(0, rc, out)
                self.assertIn("  deferments: 1 deferment(s) with review-by · "
                              "0 lapsed · 0 malformed", out)
                self.assertNotIn("🟡 " + spec["ignore"], out)

    def test_no_ignore_file_prints_known_zeros(self):
        for spec in SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                rc, out = self._run(spec, root)
                self.assertEqual(0, rc, out)
                self.assertIn("  deferments: 0 deferment(s) with review-by · "
                              "0 lapsed · 0 malformed", out)

    def test_a_lapsed_date_never_changes_the_exit_status(self):
        for spec in SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec, dirty=True)
                (root / spec["ignore"]).write_text(PLAIN, encoding="utf-8")
                rc_plain, out_plain = self._run(spec, root)
                self.assertEqual(1, rc_plain, out_plain)   # the fixture really blocks
                (root / spec["ignore"]).write_text(DATED, encoding="utf-8")
                rc_dated, out_dated = self._run(spec, root)
                self.assertEqual(rc_plain, rc_dated, out_dated)
                self.assertIn("1 lapsed · 1 malformed", out_dated)

    def test_json_carries_the_deferments(self):
        for spec in SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                (root / spec["ignore"]).write_text(DATED, encoding="utf-8")
                rc, out = self._run(spec, root, "--json")
                self.assertEqual(0, rc, out)
                got = json.loads(out)["deferments"]
                self.assertEqual([2, 4, 7], [d["line"] for d in got])
                self.assertEqual([True, False, False], [d["lapsed"] for d in got])
                self.assertEqual(["soon"], got[2]["malformed"])

    def test_json_without_an_ignore_file_is_an_empty_list(self):
        for spec in SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                rc, out = self._run(spec, root, "--json")
                self.assertEqual(0, rc, out)
                self.assertEqual([], json.loads(out)["deferments"])

    def test_an_unreasoned_glob_still_refuses_first(self):
        for spec in SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                (root / spec["ignore"]).write_text("docs/x/\n", encoding="utf-8")
                rc, out = self._run(spec, root)
                self.assertEqual(2, rc, out)


class LeakscanBinaries(unittest.TestCase):
    """leakscan reads `.leakscanbinaries` too: one count line over both files,
    each file's 🟡 lines naming their own file, and `file` in the JSON."""

    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="leakscan-binaries-")).resolve()
        self.addCleanup(shutil.rmtree, self.root, True)
        self.terms = self.root.parent / (self.root.name + "-terms.txt")
        self.terms.write_text("", encoding="utf-8")
        self.addCleanup(self.terms.unlink, missing_ok=True)
        _write(self.root, "docs/ok.md", "Plain.\n")
        _write(self.root, ".leakscanignore",
               "# gone soon. review-by: 2020-01-01\ndocs/old/\n")
        # Entries here are never matched (no such binary): the date reader
        # judges the comments, so a lapsed date is read from a real-shaped line.
        _write(self.root, ".leakscanbinaries",
               "# the logo, redraw it. review-by: 2020-02-02\n"
               + "ab" * 32 + "  assets/logo.png\n")

    def _run(self, *extra):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            rc = leakscan.main(["--root", str(self.root), "--terms", str(self.terms),
                                *extra])
        return rc, out.getvalue()

    def test_both_files_count_on_one_line(self):
        rc, out = self._run()
        self.assertIn("  deferments: 2 deferment(s) with review-by · 2 lapsed · "
                      "0 malformed", out)
        self.assertIn("🟡 .leakscanignore:2 'docs/old/' review-by 2020-01-01 LAPSED", out)
        self.assertIn("🟡 .leakscanbinaries:2 ", out)
        self.assertIn("review-by 2020-02-02 LAPSED", out)
        self.assertEqual(1, out.count("  deferments:"))

    def test_json_names_the_file_in_each_entry(self):
        rc, out = self._run("--json")
        got = json.loads(out)["deferments"]
        self.assertEqual([".leakscanignore", ".leakscanbinaries"],
                         [d["file"] for d in got])

    def test_a_lapsed_binary_date_does_not_change_the_exit_status(self):
        rc_dated, _ = self._run()
        (self.root / ".leakscanbinaries").write_text(
            "# the logo, redraw it.\n" + "ab" * 32 + "  assets/logo.png\n",
            encoding="utf-8")
        rc_plain, _ = self._run()
        self.assertEqual(rc_plain, rc_dated)


# ------------------------------------------------ line markers (part 4) --
#
# `review-by: YYYY-MM-DD` in a line marker's reason. Each fixture line carries a
# finding its scanner would block on, exempted by a marker whose reason is the
# argument. The marker word is joined from pieces (`name + ":allow"`) so this
# file's own lines carry no marker for the floor to read.

def _marker(name, reason, comment=True):
    m = name + ":allow: " + reason
    return f"<!-- {m} -->" if comment else m


def _marked_wrap(reason):
    return "docs/a.md", "x " * 70 + _marker("wrapscan", reason) + "\n"


def _marked_date(reason):
    return "docs/a.md", "We did it yesterday. " + _marker("datescan", reason) + "\n"


def _marked_link(reason):
    return "docs/a.md", "See [x](missing.md). " + _marker("linkscan", reason) + "\n"


def _marked_path(reason):
    return "docs/a.md", ("See `docs/nope/missing.md`. "
                         + _marker("pathscan", reason) + "\n")


def _marked_spell(reason):
    return "docs/a.md", "The color of it. " + _marker("spellscan", reason) + "\n"


def _marked_secret(reason):
    token = "ghp_" + "a1B2c3D4e5F6" + "g7H8i9J0k1L2" + "m3N4o5P6q7R8"
    return "c.txt", f'key = "{token}"  # ' + _marker("secretscan", reason, False) + "\n"


def _marked_leak(reason):
    addr = "someone.real" + "@" + "gmail" + ".com"
    return "c.txt", f"contact: {addr}  " + _marker("leakscan", reason, False) + "\n"


def _marked_conflict(reason):
    return "docs/a.md", "<<<<<<< HEAD " + _marker("conflictscan", reason, False) + "\n"


def _dirty_wrap(root):
    _write(root, "docs/bad.md", "y " * 70 + "\n")


MARKER_SPECS = [
    _spec("wrapscan", wrapscan, ".wrapscanignore", _dirty_wrap),
    _spec("datescan", datescan, ".datescanignore", _dirty_date),
    _spec("linkscan", linkscan, ".linkscanignore", _dirty_link),
    _spec("pathscan", pathscan, ".pathscanignore", _dirty_path),
    _spec("spellscan", spellscan, ".spellscanignore", _dirty_spell),
    _spec("secretscan", secretscan, ".secretscanignore", _dirty_secret),
    _spec("leakscan", leakscan, ".leakscanignore", _dirty_leak, argv=_argv_leak),
    _spec("conflictscan", conflictscan, ".conflictscanignore", _dirty_conflict),
]
_MARKED = {"wrapscan": _marked_wrap, "datescan": _marked_date,
           "linkscan": _marked_link, "pathscan": _marked_path,
           "spellscan": _marked_spell, "secretscan": _marked_secret,
           "leakscan": _marked_leak, "conflictscan": _marked_conflict}


class LineMarkerAdopters(unittest.TestCase):
    """The eight scanners that read `review-by` in a line marker's reason
    (110/060 part 4): reported on the same `deferments:` line and in the same
    `--json` field, warn-only, and never a change to what the marker exempts."""

    _tree = Adopters._tree
    _run = Adopters._run

    def _marked(self, spec, root, reason):
        rel, text = _MARKED[spec["name"]](reason)
        _write(root, rel, text)
        return rel

    def test_a_lapsed_marker_date_is_reported(self):
        for spec in MARKER_SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                rel = self._marked(spec, root, "kept for now, review-by: 2020-01-01")
                rc, out = self._run(spec, root)
                self.assertEqual(0, rc, out)
                self.assertIn("  deferments: 1 deferment(s) with review-by · "
                              "1 lapsed · 0 malformed", out)
                self.assertIn(f"🟡 {rel}:1 {spec['name']}:allow review-by "
                              "2020-01-01 LAPSED", out)

    def test_an_unreadable_marker_date_is_reported(self):
        for spec in MARKER_SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                rel = self._marked(spec, root, "kept for now, review-by: soon")
                rc, out = self._run(spec, root)
                self.assertEqual(0, rc, out)
                self.assertIn("0 lapsed · 1 malformed", out)
                self.assertIn(f"🟡 {rel}:1 {spec['name']}:allow review-by "
                              "unreadable: 'soon'", out)

    def test_a_future_or_absent_date_is_quiet(self):
        for spec in MARKER_SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                rel = self._marked(spec, root, "kept for now, review-by: 2999-12-31")
                rc, out = self._run(spec, root)
                self.assertIn("  deferments: 1 deferment(s) with review-by · "
                              "0 lapsed · 0 malformed", out)
                self.assertNotIn(f"🟡 {rel}", out)
                self._marked(spec, root, "kept for now")
                rc, out = self._run(spec, root)
                self.assertIn("  deferments: 0 deferment(s) with review-by · "
                              "0 lapsed · 0 malformed", out)

    def test_warn_only_and_the_exemption_is_unchanged(self):
        # The same tree with the marker's reason dated (lapsed, unreadable)
        # and undated: identical exit status and identical `suppressed:` line,
        # on a tree the scanner passes and on one it blocks.
        for spec in MARKER_SPECS:
            for dirty in (False, True):
                with self.subTest(spec["name"], dirty=dirty):
                    root = self._tree(spec, dirty=dirty)
                    runs = []
                    for reason in ("kept for now",
                                   "kept for now, review-by: 2020-01-01",
                                   "kept for now, review-by: soon"):
                        self._marked(spec, root, reason)
                        rc, out = self._run(spec, root)
                        supp = [ln for ln in out.splitlines()
                                if ln.startswith("  suppressed:")]
                        runs.append((rc, supp))
                    self.assertEqual(1 if dirty else 0, runs[0][0], runs)
                    self.assertEqual(runs[0], runs[1])
                    self.assertEqual(runs[0], runs[2])

    def test_json_carries_the_marker_deferment(self):
        for spec in MARKER_SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                rel = self._marked(spec, root, "kept for now, review-by: 2020-01-01")
                rc, out = self._run(spec, root, "--json")
                self.assertEqual(0, rc, out)
                self.assertEqual(
                    [{"file": rel, "line": 1, "marker": spec["name"] + ":allow",
                      "review_by": "2020-01-01", "lapsed": True, "malformed": []}],
                    json.loads(out)["deferments"])

    def test_glob_and_marker_deferments_share_one_count_line(self):
        for spec in MARKER_SPECS:
            with self.subTest(spec["name"]):
                root = self._tree(spec)
                self._marked(spec, root, "kept for now, review-by: 2020-01-01")
                (root / spec["ignore"]).write_text(DATED, encoding="utf-8")
                rc, out = self._run(spec, root)
                self.assertEqual(0, rc, out)
                self.assertEqual(1, out.count("  deferments:"))
                self.assertIn("  deferments: 3 deferment(s) with review-by · "
                              "2 lapsed · 1 malformed", out)


class MarkerReviewByReader(unittest.TestCase):
    """`allowmarker.marker_review_by`: the reason a counted marker carries,
    read by the glob reader's own token rules."""

    am = allowmarker
    W = allowmarker.marker_rx("wrap" + "scan:allow")
    L = allowmarker.marker_rx("leak" + "scan:allow", scope="list", group="rule")
    B = allowmarker.marker_rx("block" + "scan:allow", sep=allowmarker.SEP_ANY_SPACE,
                              named_reason=False)

    def read(self, rx, text):
        return self.am.marker_review_by(rx, text)

    def test_reads_the_date_up_to_a_comment_closer(self):
        w = "wrap" + "scan:allow: "
        self.assertEqual(("2027-01-31", ()),
                         self.read(self.W, f"x <!-- {w}why review-by: 2027-01-31 -->"))
        self.assertEqual(("2027-01-31", ()),
                         self.read(self.W, f"x <!-- {w}why review-by: 2027-01-31-->"))

    def test_no_date_and_no_counted_marker_read_as_none(self):
        w = "wrap" + "scan:allow:"
        self.assertIsNone(self.read(self.W, f"x <!-- {w} why -->"))
        # A marker with no reason counts for nothing, so its line's date is not its own.
        self.assertIsNone(self.read(self.W, f"x <!-- {w} --> review-by: 2020-01-01"))

    def test_a_date_in_a_code_span_is_a_mention(self):
        w = "wrap" + "scan:allow: "
        self.assertIsNone(self.read(self.W, f"x <!-- {w}why `review-by: 2020-01-01` -->"))

    def test_a_second_marker_keeps_its_own_reason(self):
        line = ("a " + "leak" + "scan:allow:email: fixture review-by: 2020-01-01; "
                + "secret" + "scan:allow: x review-by: 2030-01-01")
        self.assertEqual(("2020-01-01", ()), self.read(self.L, line))

    def test_two_dates_or_a_bad_one_are_malformed(self):
        w = "wrap" + "scan:allow: "
        self.assertEqual((None, ("2020-01-01", "2021-01-01")), self.read(
            self.W, f"<!-- {w}x review-by: 2020-01-01 review-by: 2021-01-01 -->"))
        self.assertEqual((None, ("2026-02-30",)), self.read(
            self.W, f"<!-- {w}x review-by: 2026-02-30 -->"))

    def test_a_reason_on_the_next_line_is_read_there(self):
        b = "block" + "scan:allow:"
        self.assertEqual(("2020-05-05", ()), self.read(
            self.B, f"<!-- {b}\n  moving review-by: 2020-05-05 -->"))

    def test_record_keeps_one_entry_per_file_line(self):
        w = "wrap" + "scan:allow: "
        into = []
        text = f"<!-- {w}x review-by: 2020-01-01 -->"
        for _ in range(3):
            self.am.record_marker_deferment(into, self.W, text, "d/a.md", 4,
                                            "2026-01-01")
        self.assertEqual(1, len(into))
        self.assertEqual(("d/a.md", 4, True), (into[0].path, into[0].line,
                                               into[0].lapsed))


if __name__ == "__main__":
    unittest.main()
