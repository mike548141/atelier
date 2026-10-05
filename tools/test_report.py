"""Tests for the shared exit-code contract and report lines
(`tools/report.py`, `115/080` part 3).

Two jobs, as `test_allowmarker.py` does for the marker grammar. (1) Test each
helper against literal strings, so the module's own contract has a proof that
does not route through any one scanner (FW3: a shared module with no test of
its own is proven eleven times through its callers, or not at all). (2) Pin
the lines each converted scanner prints, as literals: what a scanner prints is
a contract with every child (they float on atelier's floor at `main`), so a
shared edit that changes any one scanner's line must fail here, loudly, before
it reaches a child's CI.

Two divergences between scanners are pinned AS THEY ARE — not endorsed:
datescan prints no tally on its findings path, and indexscan's over-cap line
carries no cap clause. Unifying either changes output, which this part does
not do.
"""

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report  # noqa: E402

CAP = "the 50000-finding cap (counted, not listed)"


def _stderr_of(fn, *args, **kwargs):
    buf = io.StringIO()
    with contextlib.redirect_stderr(buf):
        rc = fn(*args, **kwargs)
    return rc, buf.getvalue()


class TestExitContract(unittest.TestCase):
    def test_codes(self):
        self.assertEqual((report.EXIT_CLEAN, report.EXIT_FINDINGS,
                          report.EXIT_BROKEN), (0, 1, 2))

    def test_exit_code_reads_truthiness(self):
        for blocking, want in ((0, 0), (1, 1), (7, 1), ([], 0), (["f"], 1),
                               (False, 0), (True, 1)):
            self.assertEqual(report.exit_code(blocking), want, blocking)

    def test_warn_always_exits_zero(self):
        self.assertEqual(report.exit_code(5, warn=True), 0)
        self.assertEqual(report.exit_code(0, warn=True), 0)

    def test_broken_prints_one_prefixed_line_and_exits_two(self):
        rc, err = _stderr_of(report.broken, "demoscan", "it broke")
        self.assertEqual((rc, err), (2, "demoscan: it broke\n"))

    def test_guarded_main_passes_the_run_code_through(self):
        for code in (0, 1, 2):
            rc, err = _stderr_of(report.guarded_main, "demoscan",
                                 lambda argv, c=code: c, None, (ValueError,))
            self.assertEqual((rc, err), (code, ""))

    def test_guarded_main_turns_a_config_error_into_exit_two(self):
        def run(argv):
            raise KeyError("bad glob")
        rc, err = _stderr_of(report.guarded_main, "demoscan", run, ["x"],
                             (ValueError, KeyError))
        self.assertEqual((rc, err), (2, "demoscan: 'bad glob'\n"))

    def test_guarded_main_never_swallows_other_errors(self):
        def run(argv):
            raise RuntimeError("a defect, not a config error")
        with self.assertRaises(RuntimeError):
            report.guarded_main("demoscan", run, None, (ValueError,))

    def test_guarded_main_hands_argv_through(self):
        seen = []
        report.guarded_main("demoscan", lambda argv: seen.append(argv) or 0,
                            ["--root", "."], (ValueError,))
        self.assertEqual(seen, [["--root", "."]])


class TestBrokenScanLines(unittest.TestCase):
    def test_resolve_targets(self):
        root = Path("/r")
        self.assertEqual(report.resolve_targets(root, ["docs", "/abs/x", "/r"]),
                         [Path("/r/docs"), Path("/abs/x"), Path("/r")])
        self.assertEqual(report.resolve_targets(root, []), [])

    def test_missing_root(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertIsNone(report.refuse_missing_root("d", Path(td), td))
            rc, err = _stderr_of(report.refuse_missing_root, "d",
                                 Path(td) / "gone", "gone")
        self.assertEqual((rc, err), (2, "d: root does not exist: gone\n"))

    def test_missing_paths_names_every_one(self):
        with tempfile.TemporaryDirectory() as td:
            t = Path(td)
            self.assertIsNone(report.refuse_missing_paths("d", [t]))
            rc, err = _stderr_of(report.refuse_missing_paths, "d",
                                 [t, t / "a", t / "b"])
        self.assertEqual(rc, 2)
        self.assertEqual(err, f"d: path does not exist: {t / 'a'}, {t / 'b'}\n")

    def test_cannot_read(self):
        e = OSError(13, "Permission denied", "docs/x.md")
        rc, err = _stderr_of(report.cannot_read, "d", e)
        self.assertEqual((rc, err), (2, "d: cannot read docs/x.md: Permission denied\n"))

    def test_git_diff_failed(self):
        rc, err = _stderr_of(report.git_diff_failed, "d", RuntimeError("boom"))
        self.assertEqual((rc, err), (2, "d: git diff failed: boom\n"))

    def test_absolute_staged_refused_with_the_guards_own_example(self):
        self.assertIsNone(report.refuse_absolute_staged("d", ["src/", "a.py"], "src/"))
        self.assertIsNone(report.refuse_absolute_staged("d", [], "src/"))
        rc, err = _stderr_of(report.refuse_absolute_staged, "d",
                             ["ok/", "/abs/one", "/abs/two"], "sub/")
        self.assertEqual(rc, 2)
        self.assertEqual(err, (
            "d: --staged needs repo-relative path(s), got absolute: "
            "/abs/one, /abs/two\n"
            "  git lists staged paths relative to the repo root, so an absolute "
            "path matches nothing\n"
            "  and the scan would pass while covering nothing. Pass e.g. "
            "'sub/' instead.\n"))


class TestReportLines(unittest.TestCase):
    def test_heads(self):
        self.assertEqual(report.clean_head("d", "all good."), "✓ d clean — all good.")
        self.assertEqual(report.findings_head("d", 3), "✗ d: 3 finding(s).")
        self.assertEqual(report.findings_head("d", 1, noun="thing(s)",
                                              tail=" — blocked.\n"),
                         "✗ d: 1 thing(s) — blocked.\n")

    def test_cap_part_and_over_cap_line(self):
        self.assertEqual(report.cap_part(0, 7),
                         "0 beyond the 7-finding cap (counted, not listed)")
        self.assertEqual(report.over_cap_line(4, 7),
                         "  …and 4 more finding(s), counted but not listed "
                         "(past the 7-finding memory cap).")
        self.assertEqual(report.over_cap_line(4, 7, noun="x(s)", indent="   "),
                         "   …and 4 more x(s), counted but not listed "
                         "(past the 7-finding memory cap).")

    def test_suppressed_line_keeps_the_callers_order_and_zeros(self):
        self.assertEqual(report.suppressed_line(["0 b", "0 a"]),
                         "  suppressed: 0 b · 0 a")
        self.assertEqual(report.suppressed_line(["1 only"]), "  suppressed: 1 only")

    def test_breakdown_sorted_and_only_when_non_empty(self):
        self.assertEqual(report.suppressed_line(["x"], breakdown={}), "  suppressed: x")
        self.assertEqual(report.suppressed_line(["x"], breakdown={"zz": 1, "aa": 2}),
                         "  suppressed: x\n    allow-marker breakdown: aa×2, zz×1")

    def test_disabled_follows_the_breakdown(self):
        self.assertEqual(report.suppressed_line(["x"], disabled=()), "  suppressed: x")
        self.assertEqual(
            report.suppressed_line(["x"], breakdown={"r": 1}, disabled=("a", "b")),
            "  suppressed: x\n    allow-marker breakdown: r×1\n    disabled: a, b")
        self.assertEqual(report.suppressed_line(["x"], disabled=["a"]),
                         "  suppressed: x\n    disabled: a")

    def test_warn_notice(self):
        self.assertEqual(report.WARN_NOTICE,
                         "\n  (--warn: advisory only — not blocking this build.)")


class TestScannerLinePins(unittest.TestCase):
    """Each converted scanner's lines, as literals. A shared edit that moves
    any one of them fails here."""

    def test_conflictscan(self):
        import conflictscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      f".conflictscanignore · 0 beyond {CAP}")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ conflictscan clean — no conflict markers found.")
        t.findings_over_cap = 3
        lines = m.render_human([], t).splitlines()
        self.assertEqual(lines[0], "✗ conflictscan: 3 finding(s) — commit blocked.")
        self.assertEqual(lines[1], "  …and 3 more finding(s), counted but not listed "
                                   "(past the 50000-finding memory cap).")

    def test_linkscan(self):
        import linkscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      f".linkscanignore · 0 beyond {CAP}")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ linkscan clean — every internal link resolves.")
        t.findings_over_cap = 3
        lines = m.render_human([], t).splitlines()
        self.assertEqual(lines[:3], ["✗ linkscan: 3 broken internal link(s).", "",
                                     "  …and 3 more broken link(s), counted but not "
                                     "listed (past the 50000-finding memory cap)."])

    def test_datescan(self):
        import datescan as m
        t = m.Tally()
        t.note_marker("b")
        t.note_marker("a")
        self.assertEqual(t.summary(), "  suppressed: 2 by allow-marker · 0 file(s) by "
                                      ".datescanignore · 0 over-long line(s) scanned "
                                      "truncated\n    allow-marker breakdown: a×1, b×1")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ datescan clean — no relative-time words or non-ISO "
                         "dates found.")
        out = m.render_human([m.Finding("a.md", 1, "k", "w", "d")], t)
        self.assertEqual(out.splitlines()[0], "✗ datescan: 1 finding(s).")
        self.assertNotIn("suppressed:", out)  # pinned as-is, not endorsed

    def test_wrapscan(self):
        import wrapscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      ".wrapscanignore · 0 over-long line(s) scanned "
                                      "truncated")
        self.assertEqual(m.render_human([], 85, t).splitlines()[0],
                         "✓ wrapscan clean — no prose lines over 85 columns.")
        out = m.render_human([m.Finding("a.md", 1, 99, "x", "d")], 85, t)
        self.assertEqual(out.splitlines()[0],
                         "✗ wrapscan: 1 finding(s) (limit 85 columns).")

    def test_spellscan(self):
        import spellscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      ".spellscanignore · 0 over-long line(s) scanned "
                                      "truncated")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ spellscan clean — no US spellings found.")
        out = m.render_human([m.Finding("a.md", 1, "us-spelling", "color",
                                        "colour", "d")], t)
        self.assertEqual(out.splitlines()[0], "✗ spellscan: 1 finding(s).")

    def test_pathscan(self):
        import pathscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      ".pathscanignore · 0 record file(s) excluded by "
                                      f"default · 0 beyond {CAP}")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ pathscan clean — every candidate repo-path reference "
                         "resolves.")
        t.findings_over_cap = 3
        lines = m.render_human([], t).splitlines()
        self.assertEqual(lines[:2], ["✗ pathscan: 3 finding(s).",
                                     "  …and 3 more finding(s), counted but not "
                                     "listed (past the 50000-finding memory cap)."])

    def test_indexscan(self):
        import indexscan as m
        t = m.Tally()
        self.assertEqual(t.summary(),
                         "  checked: 0 declaration(s) in 0 index file(s), 0 entr(ies) "
                         "mapped\n  suppressed: 0 by allow-marker · 0 by exclude= · "
                         "0 by before= · 0 file(s) by .indexscanignore · "
                         f"0 beyond {CAP}")
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ indexscan clean — no index declares a mapped directory "
                         "(nothing to check; adoption is opt-in per index).")
        t.declarations = 1
        self.assertEqual(m.render_human([], t).splitlines()[0],
                         "✓ indexscan clean — every mapped entry is named by its index.")
        t.findings_over_cap = 3
        lines = m.render_human([], t).splitlines()
        # The over-cap line carries no cap clause — pinned as-is, not endorsed.
        self.assertEqual(lines[:2], ["✗ indexscan: 3 finding(s).",
                                     "  …and 3 more finding(s), counted but not listed."])

    def test_secretscan(self):
        import secretscan as m
        t = m.Tally(disabled_rules=("assigned",))
        self.assertEqual(t.summary(),
                         "  suppressed: 0 by allow-marker · 0 file(s) by .secretscanignore"
                         " · 1 rule(s) disabled · 0 public-key fingerprint(s) · 0 by "
                         "public-key line · 0 by published-url token · "
                         f"0 beyond {CAP}\n    disabled: assigned")
        t.note_marker("r")
        self.assertIn("\n    allow-marker breakdown: r×1\n    disabled: assigned",
                      t.summary())
        self.assertEqual(m.render_human([], m.Tally()).splitlines()[0],
                         "✓ secretscan clean — no credentials in the scanned lines.")
        t = m.Tally()
        t.blocking_over_cap = 3
        lines = m.render_human([], t).splitlines()
        self.assertEqual(lines[:3], ["✗ secretscan: 3 finding(s) — commit blocked.", "",
                                     "  …and 3 more blocking finding(s), counted but "
                                     "not listed (past the 50000-finding memory cap)."])
        self.assertEqual(m._render_advisory([], 2)[-1],
                         "   …and 2 more advisory finding(s), counted but not listed "
                         "(past the 50000-finding memory cap).")

    def test_leakscan(self):
        import leakscan as m
        t = m.Tally()
        self.assertEqual(t.summary(), "  suppressed: 0 by allow-marker · 0 file(s) by "
                                      ".leakscanignore · 0 rule(s) disabled · "
                                      f"0 beyond {CAP}")
        self.assertEqual(m.render_human([], None, True, t).splitlines()[0],
                         "✓ leakscan clean (structural + local).")
        t.findings_over_cap = 3
        lines = m.render_human([], None, False, t).splitlines()
        self.assertEqual(lines[:3], ["✗ leakscan: 3 finding(s) — commit blocked.", "",
                                     "  …and 3 more finding(s), counted but not "
                                     "listed (past the 50000-finding memory cap)."])

    def test_sizescan(self):
        import sizescan as m
        self.assertEqual(m._suppression_line(1, 2),
                         "  suppressed: 1 file(s) by sizescan:allow header · "
                         "2 file(s) by .sizescanignore")
        self.assertEqual(m.render_human([]),
                         "✓ sizescan clean — no relocatable cold content on the hot "
                         "path; archive stores hold no live markers.\n"
                         "  suppressed: 0 file(s) by sizescan:allow header · "
                         "0 file(s) by .sizescanignore")

    def test_licenscan(self):
        import licenscan as m
        rep = m.Report(repo_license="MIT")
        supp = ("  suppressed: 0 declaration(s) by allow-marker · 0 file(s) by "
                ".licenscanignore · 0 file(s) over 8 MiB scanned truncated")
        self.assertEqual(m.render_human(rep),
                         "✓ licenscan clean — repo licence MIT, all declarations "
                         "agree.\n" + supp)
        rep.findings.append(m.Finding("mismatch", "high", "msg", "a.txt", 3))
        lines = m.render_human(rep).splitlines()
        self.assertEqual(lines[0], "✗ licenscan: 1 finding(s) — repo licence MIT. "
                                   "Publish blocked.")
        self.assertIn(supp, lines)

    def test_reviewscan(self):
        import reviewscan as m
        with tempfile.TemporaryDirectory() as td:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = m.run([Path(td)], Path(td), False)
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue(),
                         f"✓ reviewscan clean — 0 post-{m.BOUNDARY} decision record(s) "
                         "carry a review line; 0 review brief(s) keep deferred "
                         "material out of the brief.\n"
                         "  suppressed: 0 record(s) by allow-marker\n")


class TestFindingIdHelpers(unittest.TestCase):
    """`115/080`: the namespaced finding ID, its line form and its JSON field."""

    def test_finding_id(self):
        self.assertEqual(report.finding_id("demoscan", "some-kind"), "demoscan:some-kind")

    def test_with_id_appends_and_leaves_the_line_alone(self):
        self.assertEqual(report.with_id("  a.md:1  [k] x → y", "demoscan", "k"),
                         "  a.md:1  [k] x → y  [demoscan:k]")

    def test_finding_dicts_adds_id_last(self):
        from dataclasses import dataclass

        @dataclass
        class F:
            path: str
            kind: str
        got = report.finding_dicts("demoscan", [F("a.md", "k")], lambda f: f.kind)
        self.assertEqual(got, [{"path": "a.md", "kind": "k", "id": "demoscan:k"}])
        self.assertEqual(list(got[0]), ["path", "kind", "id"])


class TestFindingLinePins(unittest.TestCase):
    """One finding line per scanner that prints an ID, as a literal: the line
    as it was before `115/080` plus `  [<scanner>:<kind>]`."""

    def line(self, out, prefix):
        return next(ln for ln in out.splitlines() if ln.startswith(prefix))

    def test_secretscan(self):
        import secretscan as m
        f = m.Finding("a.txt", 3, "aws-access-key-id", "named", "high", "AKIA… (20 chars)")
        self.assertEqual(self.line(m.render_human([f]), "  a.txt"),
                         "  a.txt:3  [high/named] aws-access-key-id → AKIA… (20 chars)"
                         "  [secretscan:aws-access-key-id]")
        f = m.Finding("b.txt", 4, m.LOW_VARIETY_RULE, "entropy", "medium", "abc…", "advisory")
        self.assertEqual(self.line(m.render_human([f]), "     b.txt"),
                         "     b.txt:4  [advisory/entropy] low-variety-entropy → abc…"
                         "  [secretscan:low-variety-entropy]")

    def test_leakscan(self):
        import leakscan as m
        out = m.render_human([m.Finding("a.txt", 1, "email", "structural", "high", "a.b…nz"),
                              m.Finding("n.txt", 0, "local-term", "local", "high", "term:ab…")],
                             None, True)
        self.assertEqual(self.line(out, "  a.txt"),
                         "  a.txt:1  [high/structural] email → a.b…nz  [leakscan:email]")
        self.assertEqual(self.line(out, "  n.txt"),
                         "  n.txt (in the path name)  [high/local] local-term → term:ab…"
                         "  [leakscan:local-term]")

    def test_linkscan(self):
        import linkscan as m
        out = m.render_human([m.Finding("a.md", 1, "missing-file", "x.md", "gone")])
        self.assertEqual(self.line(out, "  a.md"),
                         "  a.md:1  [missing-file] x.md → gone  [linkscan:missing-file]")

    def test_datescan(self):
        import datescan as m
        out = m.render_human([m.Finding("a.md", 1, "relative-time-word", "today", "d")])
        self.assertEqual(self.line(out, "  a.md"),
                         "  a.md:1  [relative-time-word] 'today' → d"
                         "  [datescan:relative-time-word]")

    def test_spellscan_names_the_word(self):
        import spellscan as m
        out = m.render_human([m.Finding("a.md", 1, "us-spelling", "Color", "Colour", "d")])
        self.assertEqual(self.line(out, "  a.md"),
                         "  a.md:1  [us-spelling] 'Color' → 'Colour'  [spellscan:color]")

    def test_pathscan(self):
        import pathscan as m
        out = m.render_human([m.Finding("a.md", 2, "missing-path", "x/y.py", "gone")])
        self.assertEqual(self.line(out, "  a.md"),
                         "  a.md:2  [missing-path] x/y.py → gone  [pathscan:missing-path]")

    def test_licenscan(self):
        import licenscan as m
        rep = m.Report(repo_license="MIT")
        rep.findings.append(m.Finding("mismatch", "high", "msg", "a.txt", 3))
        rep.findings.append(m.Finding("no-license", "high", "none"))
        out = m.render_human(rep)
        self.assertEqual(self.line(out, "  a.txt"),
                         "  a.txt:3  [high/mismatch] msg  [licenscan:mismatch]")
        self.assertEqual(self.line(out, "  [high/no"),
                         "  [high/no-license] none  [licenscan:no-license]")

    def test_sizescan_per_kind_lines(self):
        import sizescan as m
        out = m.render_human([m.Finding("ROADMAP.md", 320, 2, 300, 20, "", True)])
        self.assertIn("      → 2 completed [x] item(s) to harvest [cold-content, gated]"
                      "  [sizescan:cold-content]", out.splitlines())
        self.assertIn("      → over the ~300-line reference (+20) [size-advisory]"
                      "  [sizescan:size-advisory]", out.splitlines())

    def test_pointerscan(self):
        import pointerscan as m
        with tempfile.TemporaryDirectory() as td:
            board = Path(td) / "docs" / "roadmap"
            board.mkdir(parents=True)
            (board / "a.md").write_text(m._SPEC_LANDED)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                m.main(["--root", td, "docs"])
        self.assertIn("  docs/roadmap/a.md:1  [state] ", buf.getvalue())
        self.assertIn("  [pointerscan:state]\n", buf.getvalue())


class TestFindingIdRoundTrip(unittest.TestCase):
    """The ID's kind is exactly the scope that scanner's marker accepts: run
    each scanner for real, read each finding's `id` from `--json`, put that
    kind in a marker, run again, and the finding — only it — is gone."""

    TOOLS = Path(__file__).resolve().parent
    KEY = "AKIA" + "IOSFODNN7EXAMPLE"      # built from parts: this file is scanned
    MAIL = "a.b" + "@" + "example.co.nz"

    def run_json(self, name, args, env=None):
        import json
        import os
        import subprocess
        p = subprocess.run([sys.executable, str(self.TOOLS / f"{name}.py"), *args,
                            "--json"], capture_output=True, text=True,
                           env=dict(os.environ, **(env or {})))
        self.assertIn(p.returncode, (0, 1), p.stderr)
        found = json.loads(p.stdout)["findings"]
        return sorted(i for f in found for i in (f.get("ids") or [f["id"]]))

    def round_trip(self, name, files, marked, args, env=None):
        """`files` maps rel path -> body; `marked(kind)` gives the same map
        with a marker scoped to `kind`."""
        with tempfile.TemporaryDirectory() as td:
            def write(m):
                for rel, body in m.items():
                    p = Path(td, rel)
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(body)
            write(files)
            ids = self.run_json(name, args(td), env)
            self.assertTrue(ids, f"{name}: the fixture must produce a finding")
            for fid in sorted(set(ids)):
                scanner, kind = fid.split(":", 1)
                self.assertEqual(scanner, name)
                write(marked(kind))
                after = self.run_json(name, args(td), env)
                self.assertNotIn(fid, after, f"{name}: a marker scoped to {kind!r}")
                self.assertEqual(after, [i for i in ids if i != fid])
                write(files)

    def test_secretscan(self):
        self.round_trip(
            "secretscan", {"a.txt": f"key {self.KEY}\n"},
            lambda k: {"a.txt": f"key {self.KEY}  # secretscan" f":allow:{k}: fixture\n"},
            lambda r: ["--root", r, r])

    def test_leakscan(self):
        with tempfile.TemporaryDirectory() as t:
            terms = Path(t) / "terms.txt"
            terms.write_text("")
            self.round_trip(
                "leakscan", {"a.txt": f"reach {self.MAIL} now\n"},
                lambda k: {"a.txt": f"reach {self.MAIL} now  # leakscan" f":allow:{k}: fixture\n"},
                lambda r: ["--root", r, r], {"ATELIER_LEAKSCAN_TERMS": str(terms)})

    def test_markdown_scanners(self):
        for name, body in (("linkscan", "See [x](missing.md)."),
                           ("datescan", "Done yesterday."),
                           ("spellscan", "The color is red."),
                           ("pathscan", "See `tools/ghost.py` here.")):
            with self.subTest(scanner=name):
                self.round_trip(
                    name, {"tools/real.py": "x\n", "a.md": body + "\n"},
                    lambda k, n=name, b=body: {
                        "a.md": f"{b}  <!-- {n}" f":allow:{k}: fixture -->\n"},
                    lambda r: ["--root", r, r])

    def test_licenscan(self):
        lic = "Apache License\nVersion 2.0, January 2004\n"
        self.round_trip(
            "licenscan", {"LICENSE": lic, "pyproject.toml": 'license = "MIT"\n'},
            lambda k: {"pyproject.toml": f'license = "MIT"  # licenscan' f':allow:{k}: x\n'},
            lambda r: [r])

    def test_sizescan(self):
        body = "- [x] done\n" + "- [ ] open\n" * 310
        self.round_trip(
            "sizescan", {"ROADMAP.md": "# R\n" + body},
            lambda k: {"ROADMAP.md": f"<!-- sizescan" f":allow:{k}: fixture -->\n" + body},
            lambda r: ["--check", "--root", r, r])

    def test_pointerscan(self):
        import pointerscan as m
        head, _, rest = m._SPEC_LIVE.partition("\n")
        self.round_trip(
            "pointerscan", {"docs/roadmap/a.md": m._SPEC_LIVE},
            lambda k: {"docs/roadmap/a.md": f"{head}  pointerscan" f":allow:{k}: x\n{rest}"},
            lambda r: ["--root", r, "docs"])


if __name__ == "__main__":
    unittest.main()
