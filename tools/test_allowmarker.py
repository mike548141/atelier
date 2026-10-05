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

import importlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allowmarker as am  # noqa: E402

M = "demoscan:allow"


class TestMarkerGrammar(unittest.TestCase):
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

    def test_single_scope_group_name_is_parameter(self):
        rx = am.marker_rx(M, scope="one", group="rule")
        self.assertEqual(am.scope_of(rx, f"{M}:r1: why", "rule"), "r1")
        with self.assertRaises(IndexError):
            am.scope_of(rx, f"{M}:r1: why", "kind")

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
    "indexscan": {"ALLOW_RX": r"\bindexscan:allow:[ \t]*(?P<reason>" + _REASON + ")"},
    "wrapscan": {"ALLOW_RX": r"\bwrapscan:allow:[ \t]*(?P<reason>" + _REASON + ")"},
    "datescan": {
        "ALLOW_MARKER_RX": r"\bdatescan:allow:\s*" + _REASON,
        "ALLOW_SCOPE_RX": r"\bdatescan:allow(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>" + _REASON + ")"},
    "pathscan": {
        "ALLOW_MARKER_RX": r"\bpathscan:allow:\s*" + _REASON,
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
                     if "import allowmarker" in p.read_text(encoding="utf-8")}
        self.assertEqual(importers, set(_PIN))

    def test_scoped_parsers_keep_their_result_types(self):
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
            (root / name).write_text(text, encoding="utf-8", newline="")
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

    def test_ignored_matches_glob_or_directory_prefix(self):
        self.assertTrue(am.ignored("docs/a.md", ["docs/*.md"]))
        self.assertTrue(am.ignored("docs/sub/a.md", ["docs/"]))
        self.assertTrue(am.ignored("docs/sub/a.md", ["docs"]))
        self.assertFalse(am.ignored("other/a.md", ["docs/"]))
        self.assertFalse(am.ignored("a.md", []))


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
