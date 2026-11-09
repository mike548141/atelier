"""Tests for the shared allow-marker grammar and ignore-file loader
(`tools/allowmarker.py`, `115/080` part 2).

Two jobs. (1) Pin the mechanism's parameters: each combination accepts what
it accepted before single-sourcing and rejects what it rejected. (2) Pin each
scanner's PARAMETERS — the point of the extraction is that a per-guard
difference is now a visible argument, so a test that every scanner still
compiles the exact pattern it carried before is the guard against the
2026-08-09 failure (a shared edit silently voiding live markers). A voided
marker reads exactly like an absent one, so only a pattern pin catches it.
"""

import contextlib
import datetime
import importlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allowmarker as am  # noqa: E402

M = "demoscan:allow"

# Two dates either side of the malformed-marker grace. Every test that depends
# on which side of it a run falls pins the clock, so the suite reads the same
# on 2026-11-09 and on 2027-01-01.
DURING = datetime.date(2026, 11, 9)
AFTER = am.MALFORMED_GRACE_UNTIL


def at(day):
    """Run the body with allowmarker's clock at `day` and its warnings muted
    and forgotten, so tests neither leak nor depend on each other's."""
    stack = contextlib.ExitStack()
    stack.enter_context(mock.patch.object(am, "_utc_today", return_value=day))
    stack.enter_context(mock.patch.object(am, "_WARNED", set()))
    stack.enter_context(mock.patch.object(am, "_NOTED", set()))
    stack.enter_context(contextlib.redirect_stderr(io.StringIO()))
    return stack


class TestMarkerGrammar(unittest.TestCase):
    """The grammar as it reads DURING the malformed-marker grace: a broken
    scoped marker still reads as the unscoped form (and warns). The strict
    read, after the date, is `TestMalformedMarkers`."""

    def setUp(self):
        stack = at(DURING)
        stack.__enter__()
        self.addCleanup(stack.__exit__, None, None, None)

    def test_unscoped_same_line_named_reason(self):
        rx = am.marker_rx(M)
        self.assertTrue(am.present(rx, f"x <!-- {M}: because -->"))
        self.assertTrue(am.present(rx, f"{M}:\t\"quoted"))
        self.assertTrue(am.present(rx, f"{M}:_under"))
        for bad in (f"{M}", f"{M}:", f"{M}: ", f"<!-- {M}: -->", f"{M}:-->",
                    f"x{M}: why", f"other:allow: why",
                    f"{M.upper()}: why", f"{M}\n: why"):
            self.assertFalse(am.present(rx, bad), bad)

    def test_unscoped_form_reads_a_scope_as_the_reason(self):
        # Existing behaviour, pinned not endorsed: with no scope group the text
        # after the colon is simply the reason, so a scoped spelling is accepted.
        self.assertTrue(am.present(am.marker_rx(M), f"{M}:rule: why"))

    def test_scope_without_reason_reads_as_unscoped_with_scope_as_reason(self):
        # Existing behaviour, pinned not endorsed (reported to the principal):
        # `m:allow:kind` with no trailing reason backtracks to the unscoped
        # form, whose reason is the word `kind`, so it exempts EVERYTHING.
        rx = am.marker_rx(M, scope="one", group="kind")
        self.assertEqual(am.scope_of(rx, f"{M}:relative-time"), "")
        rx = am.marker_rx(M, scope="list", group="rule")
        self.assertEqual(am.scopes_of(rx, f"{M}:a,b"), frozenset())

    def test_unscoped_same_line_does_not_cross_newline(self):
        rx = am.marker_rx(M)
        self.assertFalse(am.present(rx, f"{M}:\nreason on next line"))

    def test_any_space_separator_crosses_newline(self):
        # The one behavioural difference among the unscoped forms: `\s*`.
        rx = am.marker_rx(M, sep=am.SEP_ANY_SPACE, named_reason=False)
        self.assertTrue(am.present(rx, f"{M}:\nreason on next line"))
        self.assertTrue(am.present(rx, f"{M}: why"))
        self.assertFalse(am.present(rx, f"{M}:"))
        self.assertFalse(am.present(rx, f"{M}"))
        self.assertIsNone(rx.search(f"{M}: why").groupdict().get("reason"))

    def test_single_scope(self):
        rx = am.marker_rx(M, scope="one", group="kind")
        self.assertEqual(am.scope_of(rx, f"{M}: why"), "")
        self.assertEqual(am.scope_of(rx, f"{M}:relative-time: why"), "relative-time")
        self.assertEqual(am.scope_of(rx, f"{M}:x_Y-9: why"), "x_Y-9")
        # No reason -> a mention, not an exemption.
        self.assertEqual(am.scope_of(rx, f"{M}:relative-time: "), "")
        self.assertIsNone(am.scope_of(rx, f"{M}"))
        # A comma is not part of a single scope: the optional group backs off
        # and the whole tail is read as the (unscoped) reason.
        self.assertEqual(am.scope_of(rx, f"{M}:a,b: why"), "")

    def test_scope_group_name_is_single_sourced(self):
        # AM8: the pattern remembers the group it was built with, so a reader
        # can neither ask for another (the old IndexError mid-scan) nor drift
        # from it. A stale group argument is ignored.
        rx = am.marker_rx(M, scope="one", group="rule")
        self.assertEqual(am.scope_of(rx, f"{M}:r1: why"), "r1")
        self.assertEqual(am.scope_of(rx, f"{M}:r1: why", "rule"), "r1")
        self.assertEqual(am.scope_of(rx, f"{M}:r1: why", "kind"), "r1")
        rx = am.marker_rx(M, scope="list", group="kind")
        self.assertEqual(am.scopes_of(rx, f"{M}:a,b: why"), frozenset({"a", "b"}))
        self.assertEqual(am.scopes_of(rx, f"{M}:a: why", "rule"), frozenset({"a"}))

    def test_list_scope(self):
        rx = am.marker_rx(M, scope="list", group="rule")
        self.assertEqual(am.scopes_of(rx, f"{M}: why"), frozenset())
        self.assertEqual(am.scopes_of(rx, f"{M}:a: why"), frozenset({"a"}))
        self.assertEqual(am.scopes_of(rx, f"{M}:a,b-c: why"), frozenset({"a", "b-c"}))
        # A trailing comma backs off to the unscoped form; a leading one is no reason.
        self.assertEqual(am.scopes_of(rx, f"{M}:a,: why"), frozenset())
        self.assertIsNone(am.scopes_of(rx, f"{M}:,a: why"))
        self.assertIsNone(am.scopes_of(rx, f"{M}:,: "))

    def test_reason_first_character_class(self):
        rx = am.marker_rx(M)
        for ch in ("a", "Z", "0", "_", '"', "'", "“", "‘"):
            self.assertTrue(am.present(rx, f"{M}: {ch}x"), ch)
        for ch in ("-", "<", "(", "#", "."):
            self.assertFalse(am.present(rx, f"{M}: {ch}x"), ch)

    def test_unknown_scope_mode_is_refused(self):
        with self.assertRaises(ValueError):
            am.marker_rx(M, scope="several")


# scanner -> {attribute: (marker-attribute, kwargs)}. The single place the
# per-guard parameters are written down; each row pins the pattern the scanner
# compiled BEFORE the extraction, as a literal.
_REASON = r"[\w\"\'“‘]"
_PIN = {
    "conflictscan": {"ALLOW_RX": r"\bconflictscan:allow:[ \t]*(?P<reason>" + _REASON + ")"},
    # Scoped since 320/430: `:date-mismatch:` is the line-bound form.
    "indexscan": {"ALLOW_RX": r"\bindexscan:allow(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "wrapscan": {"ALLOW_RX": r"\bwrapscan:allow:[ \t]*(?P<reason>" + _REASON + ")"},
    "datescan": {
        "ALLOW_SCOPE_RX": r"\bdatescan:allow(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "pathscan": {
        "ALLOW_SCOPE_RX": r"\bpathscan:allow(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "stampscan": {"ALLOW_MARKER_RX": r"\bstampscan:allow:\s*" + _REASON},
    "leakscan": {"ALLOW_RX": r"\bleakscan:allow(?::(?P<rule>[A-Za-z0-9_-]+(?:,[A-Za-z0-9_-]+)*))?:[ \t]*(?P<reason>"
                             + _REASON + ")"},
    "secretscan": {"ALLOW_RX": r"\bsecretscan:allow(?::(?P<rule>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "spellscan": {"ALLOW_RX": r"\bspellscan:allow(?::(?P<rule>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "linkscan": {"ALLOW_RX": r"\blinkscan:allow(?::(?P<rule>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "licenscan": {"ALLOW_RX": r"\blicenscan:allow(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "sizescan": {"ALLOW_RX": r"\bsizescan:allow(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "pointerscan": {"ALLOW_RX": r"\bpointerscan:allow(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "reviewscan": {"ALLOW_RX": r"\breviewscan:allow(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    # blockscan spelled its quote class `[\w\"'“‘]` (no backslash before the
    # apostrophe); the two are the same character set, pinned as the shared form.
    "blockscan": {"ALLOW_MARKER_RX": r"\bblockscan:allow:\s*" + _REASON},
    "attribscan": {"ALLOW_RX": r"\battribscan:allow:\s*" + _REASON},
}


class TestScannerParametersPinned(unittest.TestCase):
    def test_every_scanner_compiles_its_pre_extraction_pattern(self):
        for name, attrs in _PIN.items():
            mod = importlib.import_module(name)
            for attr, literal in attrs.items():
                with self.subTest(scanner=name, attr=attr):
                    self.assertEqual(getattr(mod, attr).pattern, literal)

    def test_pins_cover_every_scanner_that_imports_the_module(self):
        tools = Path(__file__).resolve().parent
        importers = {p.stem for p in tools.glob("*scan.py")
                     if not p.name.startswith("test_")
                     and "import allowmarker" in p.read_text(encoding="utf-8")}
        self.assertEqual(importers, set(_PIN))

    def test_scoped_parsers_keep_their_result_types(self):
        with at(DURING):    # the unparseable cases below print a stderr note (110/010)
            self._scoped_parsers_keep_their_result_types()

    def _scoped_parsers_keep_their_result_types(self):
        import leakscan, conflictscan, wrapscan, datescan, secretscan  # noqa: E401
        self.assertEqual(leakscan.parse_allow("leakscan:allow:email,local-term: r"),
                         frozenset({"email", "local-term"}))
        self.assertEqual(leakscan.parse_allow("leakscan:allow: r"), frozenset())
        self.assertIsNone(leakscan.parse_allow("leakscan:allow:"))
        self.assertIs(conflictscan.parse_allow("conflictscan:allow: r"), True)
        self.assertIs(conflictscan.parse_allow("conflictscan:allow"), False)
        self.assertIs(wrapscan.parse_allow("wrapscan:allow: r"), True)
        self.assertEqual(datescan.parse_allow("datescan:allow:relative-time: r"), "relative-time")
        self.assertEqual(datescan.parse_allow("datescan:allow: r"), "")
        self.assertIsNone(datescan.parse_allow("datescan:allow"))
        self.assertEqual(secretscan.parse_allow("secretscan:allow:assigned: r"), "assigned")

    def test_ignore_wrappers_pass_their_own_filename(self):
        for name in ("conflictscan", "datescan", "indexscan", "leakscan", "licenscan", "linkscan", "pathscan",
                     "secretscan", "sizescan", "spellscan", "stampscan", "wrapscan"):
            mod = importlib.import_module(name)
            with self.subTest(scanner=name), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                (root / f".{name}ignore").write_text("docs/x.md\n", encoding="utf-8")
                with self.assertRaises(am.IgnoreFileError) as cm:
                    mod.load_ignore_globs(root)
                self.assertEqual(cm.exception.filename, f".{name}ignore")
                self.assertIs(mod.IgnoreFileError, am.IgnoreFileError)


class TestIgnoreFile(unittest.TestCase):
    def load(self, text, name=".demoscanignore"):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / name).write_bytes(text.encode("utf-8"))  # no newline translation
            return am.load_ignore_globs(root, name)

    def test_absent_file_is_no_globs(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(am.load_ignore_globs(Path(td), ".demoscanignore"), [])

    def test_trailing_reason(self):
        self.assertEqual(self.load("a/b.md # why\n"), ["a/b.md"])

    def test_stanza_reason_covers_following_globs_until_blank(self):
        self.assertEqual(self.load("# why\na.md\nb.md\n"), ["a.md", "b.md"])
        with self.assertRaises(am.IgnoreFileError) as cm:
            self.load("# why\na.md\n\nb.md\n")
        self.assertEqual(cm.exception.entries, [(4, "b.md")])

    def test_bare_glob_is_a_config_error(self):
        with self.assertRaises(am.IgnoreFileError) as cm:
            self.load("a.md\n")
        self.assertEqual(cm.exception.entries, [(1, "a.md")])
        self.assertIn(".demoscanignore: 1 glob(s) with no stated reason", str(cm.exception))

    def test_empty_trailing_reason_is_unreasoned(self):
        with self.assertRaises(am.IgnoreFileError):
            self.load("a.md #\n")
        with self.assertRaises(am.IgnoreFileError):
            self.load("a.md #   \n")

    def test_hash_without_space_still_splits(self):
        # Unlike publishscan's stricter loader, this one splits on the first '#'.
        self.assertEqual(self.load("a.md#why\n"), ["a.md"])

    def test_comment_only_and_blank_lines_yield_nothing(self):
        self.assertEqual(self.load("# a\n\n   \n#\n # b\n"), [])

    def test_all_unreasoned_are_reported_together(self):
        with self.assertRaises(am.IgnoreFileError) as cm:
            self.load("a.md\n\nb.md\n")
        self.assertEqual(cm.exception.entries, [(1, "a.md"), (3, "b.md")])

    def test_crlf_lines(self):
        self.assertEqual(self.load("# why\r\na.md\r\n\r\nb.md # r\r\n"), ["a.md", "b.md"])

    def test_glob_that_is_only_a_hash_is_skipped(self):
        self.assertEqual(self.load("# x\n#\n"), [])

    def test_reasoned_lines_return_the_reason_text(self):
        # The grammar `.leakscanbinaries` (G3) reuses: same presence test,
        # and the reason text itself, trailing first, else the stanza's.
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "x"
            f.write_text("# brand\n#\n# assets\na.png\nb.png # own\n\nc.png\n#\nd.png\n",
                         encoding="utf-8")
            self.assertEqual(am.read_reasoned_lines(f),
                             [(4, "a.png", "brand assets"), (5, "b.png", "own"),
                              (7, "c.png", None), (9, "d.png", "")])
            self.assertEqual(am.read_reasoned_lines(Path(td) / "absent"), [])

    def test_a_glob_with_control_or_bidi_characters_is_not_echoed_raw(self):
        # 160/480 AM9: the error echoes the glob; through any scanner's `main`
        # the message passes report.broken, which drops C0/C1 controls and the
        # bidi override/isolate set (160/730 RT3). Pinned here for the loader.
        hostile = "docs/\u202egnp.md\x1b[2J"
        with tempfile.TemporaryDirectory() as td:
            Path(td, ".leakscanignore").write_text(hostile + "\n", encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", str(Path(am.__file__).parent / "leakscan.py"),
                                "--root", td, td], capture_output=True, text=True)
        self.assertEqual(2, r.returncode, r.stdout + r.stderr)
        self.assertIn("no stated reason", r.stderr)
        for bad in ("\u202e", "\x1b"):
            self.assertNotIn(bad, r.stderr)

    def test_ignored_matches_glob_or_directory_prefix(self):
        self.assertTrue(am.ignored("docs/a.md", ["docs/*.md"]))
        self.assertTrue(am.ignored("docs/sub/a.md", ["docs/"]))
        self.assertTrue(am.ignored("docs/sub/a.md", ["docs"]))
        self.assertFalse(am.ignored("other/a.md", ["docs/"]))
        self.assertFalse(am.ignored("a.md", []))

    def test_fnmatch_semantics_are_not_gitignores(self):
        # 160/480 AM6: the ignore files call themselves "gitignore-style"; they
        # are not. Pinned as the stated behaviour, so a change is deliberate.
        self.assertTrue(am.ignored("docs/sub/a.md", ["docs/*.md"]))   # * crosses /
        self.assertFalse(am.ignored("docs/a.md", ["/docs/a.md"]))     # leading / never matches
        self.assertFalse(am.ignored("a.md", ["!a.md"]))               # ! is a literal
        self.assertFalse(am.ignored("x.md", ["**/x.md"]))             # no top-level match
        self.assertTrue(am.ignored("docs/x.md", ["**/x.md"]))


class TestMalformedMarkers(unittest.TestCase):
    """160/480 AM2 (and LK1, the same finding): a scoped marker whose scope is
    broken used to back off to the unscoped form and exempt every rule on its
    line. Mike, 2026-11-09: "Strict, with a warning period". Before
    `MALFORMED_GRACE_UNTIL` it still exempts and warns; from it, nothing."""

    ONE = am.marker_rx(M, scope="one", group="kind")
    LIST = am.marker_rx(M, scope="list", group="rule")
    # Each is a scoped marker that failed to parse as one.
    BROKEN = (
        f"{M}:ipv4:",                      # scope, no reason
        f"{M}:ipv4: ",                     # scope, blank reason
        f"x <!-- {M}:ipv4: -->",           # scope, comment closer for a reason
        f"{M}:email, ipv4: why",           # a space inside the scope
        f"{M}:a,: why",                    # a trailing comma
        f"{M}:e.mail: why",                # a stray character in the scope
    )
    # Each is a marker that parses as intended and must never be flagged.
    FINE = (
        f"{M}:ipv4: why",
        f"{M}: why",
        f"{M}: why: more",                 # a colon inside the reason
        f"{M}: see ADR 0005: public",
        f"{M}:ipv4: why: more",
    )

    def test_during_the_grace_a_broken_marker_still_exempts_and_warns(self):
        for text in self.BROKEN:
            with self.subTest(text=text), at(DURING):
                err = io.StringIO()
                with contextlib.redirect_stderr(err):
                    got = am.scope_of(self.ONE, text)
                self.assertIn(got, ("",), text)      # the old whole-unit read
                self.assertIn("malformed allow-marker", err.getvalue())
                self.assertIn(am.MALFORMED_GRACE_UNTIL.isoformat(), err.getvalue())

    def test_after_the_grace_a_broken_marker_exempts_nothing(self):
        for text in self.BROKEN:
            with self.subTest(text=text), at(AFTER):
                self.assertIsNone(am.scope_of(self.ONE, text))
                self.assertIsNone(am.scopes_of(self.LIST, text))

    def test_the_grace_ends_on_the_date_itself(self):
        with at(AFTER - datetime.timedelta(days=1)):
            self.assertTrue(am.in_malformed_grace())
            self.assertEqual("", am.scope_of(self.ONE, f"{M}:ipv4:"))
        with at(AFTER):
            self.assertFalse(am.in_malformed_grace())
            self.assertIsNone(am.scope_of(self.ONE, f"{M}:ipv4:"))
        self.assertEqual(AFTER, datetime.date(2026, 12, 9))

    def test_a_well_formed_marker_is_never_flagged_on_either_side(self):
        for day in (DURING, AFTER):
            for text in self.FINE:
                with self.subTest(day=day, text=text), at(day):
                    err = io.StringIO()
                    with contextlib.redirect_stderr(err):
                        self.assertIsNotNone(am.scope_of(self.ONE, text), text)
                        self.assertIsNotNone(am.scopes_of(self.LIST, text), text)
                    self.assertEqual("", err.getvalue(), text)

    def test_scopes_are_read_as_written_on_either_side(self):
        for day in (DURING, AFTER):
            with at(day):
                self.assertEqual("ipv4", am.scope_of(self.ONE, f"{M}:ipv4: why"))
                self.assertEqual(frozenset({"a", "b"}),
                                 am.scopes_of(self.LIST, f"{M}:a,b: why"))
                self.assertEqual("", am.scope_of(self.ONE, f"{M}: why"))

    def test_a_comma_list_is_malformed_for_a_single_scope_scanner(self):
        with at(AFTER):
            self.assertIsNone(am.scope_of(self.ONE, f"{M}:a,b: why"))
            self.assertEqual(frozenset({"a", "b"}),
                             am.scopes_of(self.LIST, f"{M}:a,b: why"))

    def test_after_the_grace_a_later_well_formed_marker_still_counts(self):
        text = f"{M}:ipv4: <!-- {M}:email: real reason -->"
        with at(AFTER):
            self.assertEqual("email", am.scope_of(self.ONE, text.replace(
                f"{M}:ipv4: <", f"{M}:ipv4:; <")))   # first is broken, second counts

    def test_the_warning_is_printed_once_per_distinct_marker(self):
        with at(DURING):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                for _ in range(3):
                    am.scope_of(self.ONE, f"{M}:ipv4:")
                am.scope_of(self.ONE, f"{M}:email:")
            self.assertEqual(2, err.getvalue().count("malformed allow-marker"))
            self.assertEqual([f"{M}:email:", f"{M}:ipv4:"], am.malformed_seen())

    def test_an_unscoped_pattern_has_no_malformed_notion(self):
        # conflictscan / wrapscan read the text after the colon as the reason.
        rx = am.marker_rx(M)
        with at(AFTER):
            self.assertTrue(am.present(rx, f"{M}:ipv4:"[:-1] + ": why"))
            self.assertTrue(am.present(rx, f"{M}:foo: why"))

    def test_a_bare_scope_word_with_no_second_colon_is_unchanged(self):
        # The one shape this cannot tell from `m:allow:reason` (a reason with no
        # leading space); named in the README, not silently changed.
        with at(AFTER):
            self.assertEqual("", am.scope_of(self.ONE, f"{M}:relative-time"))

    def test_the_cut_off_is_a_constant_with_no_override(self):
        src = (Path(am.__file__)).read_text(encoding="utf-8")
        self.assertFalse("os.environ" in src or "getenv(" in src or "argv" in
                         src.split("def census")[0])


class TestUnparseableNote(unittest.TestCase):
    """110/010: a marker that parses as nothing reads like no marker, so a line
    that carries the marker word outside a code span but no allowance gets a
    one-line stderr note. A note only: no result and no exit status moves."""

    ONE = am.marker_rx(M, scope="one", group="kind")
    LIST = am.marker_rx(M, scope="list", group="rule")
    UNSCOPED = am.marker_rx(M)
    ANYSPACE = am.marker_rx(M, sep=am.SEP_ANY_SPACE, named_reason=False)

    def run_read(self, fn, rx, text, day=DURING):
        with at(day):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                got = fn(rx, text)
            return got, err.getvalue(), am.unparseable_seen()

    def test_every_reader_notes_a_marker_with_no_reason(self):
        text = f"x = 1  # {M}"
        for fn, rx in ((am.scope_of, self.ONE), (am.scopes_of, self.LIST),
                       (am.present, self.UNSCOPED), (am.present, self.ANYSPACE)):
            with self.subTest(rx=rx.pattern):
                got, err, seen = self.run_read(fn, rx, text)
                self.assertFalse(got)
                self.assertIn("present but unparseable", err)
                self.assertEqual(1, err.count("\n"))
                self.assertEqual([M], seen)

    def test_the_note_shows_the_head_and_never_the_line(self):
        _, err, _ = self.run_read(am.scope_of, self.ONE,
                                  f"password = hunter2  # {M}:ipv4:")
        self.assertIn(f"`{M}:ipv4:`", err)
        self.assertNotIn("hunter2", err)

    def test_a_good_marker_is_never_noted(self):
        for fn, rx, text in ((am.scope_of, self.ONE, f"{M}:ipv4: why"),
                             (am.scopes_of, self.LIST, f"{M}: why"),
                             (am.present, self.UNSCOPED, f"{M}: why"),
                             (am.present, self.ANYSPACE, f"{M}:\nwhy")):
            with self.subTest(text=text):
                got, err, seen = self.run_read(fn, rx, text)
                self.assertTrue(got is not None and got is not False)
                self.assertEqual(("", []), (err, seen))

    def test_a_line_without_the_word_is_silent(self):
        for fn, rx in ((am.scope_of, self.ONE), (am.present, self.UNSCOPED)):
            got, err, seen = self.run_read(fn, rx, "nothing to see")
            self.assertEqual(("", []), (err, seen))

    def test_a_mention_in_a_code_span_is_silent(self):
        for fn, rx in ((am.scope_of, self.ONE), (am.scopes_of, self.LIST),
                       (am.present, self.UNSCOPED)):
            _, err, seen = self.run_read(fn, rx, f"write `{M}: <reason>` to allow")
            self.assertEqual(("", []), (err, seen))

    def test_a_broken_scoped_marker_is_noted_after_the_grace_only(self):
        # During the grace it still allows (and warns as malformed); after it,
        # it allows nothing, which is exactly when the reader needs telling.
        got, err, seen = self.run_read(am.scope_of, self.ONE, f"{M}:ipv4:", DURING)
        self.assertEqual("", got)
        self.assertNotIn("unparseable", err)
        got, err, seen = self.run_read(am.scope_of, self.ONE, f"{M}:ipv4:", AFTER)
        self.assertIsNone(got)
        self.assertIn("present but unparseable", err)

    def test_the_note_is_printed_once_per_distinct_head(self):
        with at(DURING):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                for _ in range(3):
                    am.scope_of(self.ONE, f"{M}")
                am.scope_of(self.ONE, f"{M}:")
            self.assertEqual(2, err.getvalue().count("present but unparseable"))
            self.assertEqual(sorted([M, f"{M}:"]), am.unparseable_seen())

    def test_the_head_is_bounded_and_printable(self):
        _, err, seen = self.run_read(am.scope_of, self.ONE,
                                     f"{M}:!\u202e" + "!" * 200)
        self.assertEqual(1, len(seen))
        self.assertLessEqual(len(seen[0]), len(M) + 40)
        self.assertTrue(seen[0].isascii())

    def test_a_code_string_naming_the_marker_is_not_an_attempt(self):
        for text in (f'if "{M}" in line:', f"x = '{M}'", f"({M})", f"{M}, then"):
            _, err, seen = self.run_read(am.scope_of, self.ONE, text)
            self.assertEqual(("", []), (err, seen), text)


class TestCodeSpans(unittest.TestCase):
    """160/480 AM3: a mention of the syntax inside an inline code span is not a
    marker. stampscan alone did this before; now every reader does."""

    ONE = am.marker_rx(M, scope="one", group="kind")
    LIST = am.marker_rx(M, scope="list", group="rule")
    UNSCOPED = am.marker_rx(M)
    ANYSPACE = am.marker_rx(M, sep=am.SEP_ANY_SPACE, named_reason=False)

    def test_blanking_keeps_length_and_leaves_plain_text(self):
        for text in ("no ticks", f"`{M}: why`", f"a `b` c ``d`e`` f", "x ` unmatched",
                     "line one\n`two`\nthree\n"):
            self.assertEqual(len(text), len(am.blank_code_spans(text)), text)
        self.assertEqual("no ticks", am.blank_code_spans("no ticks"))
        self.assertEqual("x ` unmatched", am.blank_code_spans("x ` unmatched"))
        self.assertEqual("a" + " " * 5 + "c", am.blank_code_spans("a `b` c"))
        self.assertEqual("a" + " " * 9 + "f", am.blank_code_spans("a ``d`e`` f"))

    def test_a_mention_in_a_code_span_exempts_nothing_in_every_reader(self):
        with at(DURING):
            text = f"the line `{M}:ipv4: because`"
            self.assertIsNone(am.scope_of(self.ONE, text))
            self.assertIsNone(am.scopes_of(self.LIST, text))
            self.assertFalse(am.present(self.UNSCOPED, text))
            self.assertFalse(am.present(self.ANYSPACE, text))

    def test_a_marker_outside_the_span_still_counts(self):
        with at(DURING):
            text = f"the line `code` <!-- {M}:ipv4: because -->"
            self.assertEqual("ipv4", am.scope_of(self.ONE, text))
            self.assertEqual(frozenset({"ipv4"}), am.scopes_of(self.LIST, text))
            self.assertTrue(am.present(self.UNSCOPED, text))

    def test_an_unmatched_backtick_hides_nothing(self):
        with at(DURING):
            self.assertEqual("", am.scope_of(self.ONE, f"it`s <!-- {M}: because -->"))

    def test_a_multiline_text_is_blanked_line_by_line(self):
        with at(DURING):
            self.assertFalse(am.present(self.ANYSPACE, f"`{M}: why`\nnext line"))
            self.assertTrue(am.present(self.ANYSPACE, f"`x`\n{M}:\nwhy"))
            # A line is the unit: a span that would cross a newline is not one.
            self.assertTrue(am.present(self.ANYSPACE, f"`{M}:\nwhy`"))


class TestUnknownScopeTally(unittest.TestCase):
    """160/480 AM10: a scope naming no rule is silently inert in the
    rule-matching scanners (the finding it was written for still reports), so
    the suppression tally counts it and a typo shows even on a clean run."""

    def test_the_helper(self):
        known = {"email", "Ipv4"}
        self.assertFalse(am.names_no_rule(None, known))
        self.assertFalse(am.names_no_rule("", known))
        self.assertFalse(am.names_no_rule(frozenset(), known))
        self.assertFalse(am.names_no_rule("email", known))
        self.assertFalse(am.names_no_rule("IPV4", known))
        self.assertTrue(am.names_no_rule("emial", known))
        self.assertTrue(am.names_no_rule(frozenset({"email", "emial"}), known))

    def test_each_rule_matching_scanner_counts_a_typo_and_not_a_real_scope(self):
        import datescan, leakscan, linkscan, secretscan, spellscan
        cases = (
            ("leakscan", lambda t, tally: leakscan.scan_text("t", t, [], frozenset(), tally),
             "x  # leakscan:allow:ipv44: typo", "x  # leakscan:allow:ipv4: real"),
            ("secretscan", lambda t, tally: secretscan.scan_text("t", t, frozenset(), tally),
             "x  # secretscan:allow:not-a-rule: typo", "x  # secretscan:allow:assigned: real"),
            ("spellscan", lambda t, tally: spellscan.scan_text("t", t, tally),
             "color <!-- spellscan:allow:colour: typo -->", "color <!-- spellscan:allow:color: real -->"),
            ("datescan", lambda t, tally: datescan.scan_text("t", t, tally),
             "today <!-- datescan:allow:relative-time: typo -->",
             "today <!-- datescan:allow:relative-time-word: real -->"),
        )
        for name, run, typo, real in cases:
            mod = importlib.import_module(name)
            with self.subTest(scanner=name):
                t = mod.Tally()
                run(typo, t)
                self.assertEqual(1, t.unknown_scope_markers)
                self.assertIn("1 marker(s) naming no rule", t.summary())
                t = mod.Tally()
                run(real, t)
                self.assertEqual(0, t.unknown_scope_markers)
                self.assertIn("0 marker(s) naming no rule", t.summary())
                t = mod.Tally()
                run("plain line", t)
                self.assertEqual(0, t.unknown_scope_markers)

    def test_linkscan_counts_a_typo(self):
        import linkscan
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "a.md").write_text(
                "[x](ghost.md) <!-- linkscan:allow:missing-fil: typo -->\n"
                "[y](ghost2.md) <!-- linkscan:allow:missing-file: real -->\n",
                encoding="utf-8")
            t = linkscan.Tally()
            linkscan.scan_paths([root], root, t)
        self.assertEqual(1, t.unknown_scope_markers)
        self.assertIn("1 marker(s) naming no rule", t.summary())

    def test_the_json_surface_carries_it(self):
        with tempfile.TemporaryDirectory() as td:
            Path(td, "a.md").write_text("color <!-- spellscan:allow:colour: typo -->\n",
                                        encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", str(Path(am.__file__).parent / "spellscan.py"),
                                "--json", "--root", td, td], capture_output=True, text=True)
        import json
        self.assertEqual(1, json.loads(r.stdout)["suppressed"]["markers_naming_no_rule"], r.stderr)


class TestCensus(unittest.TestCase):
    def test_census_lists_malformed_markers_and_skips_good_ones_and_code(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "a.md").write_text(
                "ok <!-- leakscan:allow:ipv4: because -->\n"
                "bad <!-- leakscan:allow:ipv4: -->\n"
                "bad2 leakscan:allow:email, ipv4: why\n"
                "doc `leakscan:allow:ipv4:` in code\n"
                "plain leakscan:allow: reason\n"
                "list leakscan:allow:email,ipv4: ok\n"
                "one secretscan:allow:a,b: a list for a one-scope scanner\n",
                encoding="utf-8")
            rows = am.census(root)
            self.assertEqual([("a.md", 2, "leakscan:allow:ipv4:"),
                              ("a.md", 3, "leakscan:allow:email, ipv4:"),
                              ("a.md", 7, "secretscan:allow:a,b:")], rows)

    def test_the_cli_reports_and_exits_zero(self):
        with tempfile.TemporaryDirectory() as td:
            Path(td, "a.md").write_text("x leakscan:allow:ipv4:\n", encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", str(Path(am.__file__)),
                                "--census", "--root", td],
                               capture_output=True, text=True)
            self.assertEqual(0, r.returncode, r.stderr)
            self.assertIn("a.md:1: leakscan:allow:ipv4:", r.stdout)
            self.assertIn("1 malformed scoped marker", r.stdout)


class TestCovers(unittest.TestCase):
    """115/080's additive scope rule for the scanners that used to read a
    scope and ignore it (licenscan, sizescan, pointerscan)."""

    K = frozenset({"alpha", "beta"})

    def test_no_marker_covers_nothing(self):
        self.assertFalse(am.covers(None, "alpha", self.K))
        self.assertFalse(am.is_blanket(None, self.K))

    def test_the_unscoped_form_covers_every_kind(self):
        self.assertTrue(am.covers("", "alpha", self.K))
        self.assertTrue(am.covers("", "beta", self.K))
        self.assertTrue(am.is_blanket("", self.K))

    def test_a_named_kind_covers_only_itself(self):
        self.assertTrue(am.covers("alpha", "alpha", self.K))
        self.assertFalse(am.covers("alpha", "beta", self.K))
        self.assertFalse(am.is_blanket("alpha", self.K))

    def test_a_scope_naming_no_kind_still_covers_every_kind(self):
        # Existing, not endorsed: the 115/230 item-1 class, kept so that no
        # live marker narrows until that item is ruled.
        self.assertTrue(am.covers("gamma", "alpha", self.K))
        self.assertTrue(am.is_blanket("gamma", self.K))

    def test_the_scanners_using_it_declare_their_kinds(self):
        import licenscan
        import pointerscan
        import sizescan
        self.assertEqual(sizescan.FINDING_KINDS,
                         {"cold-content", "harvest-integrity", "size-advisory"})
        self.assertEqual(pointerscan.FINDING_KINDS, {"grammar", "cycle", "state"})
        self.assertEqual(licenscan.FINDING_KINDS,
                         {"no-license", "unknown-license", "mismatch", "incompatible",
                          "unknown-declaration", "expect-mismatch"})


if __name__ == "__main__":
    unittest.main()
