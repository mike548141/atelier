"""Stdlib-only tests for leakscan (no pytest needed): `python3 -m unittest`."""

import re
import pathlib
import unittest

import leakscan as ls


def scan(text, terms=None):
    return ls.scan_text("t", text, terms or [])


def rules(text, terms=None):
    return {f.rule for f in scan(text, terms)}


class Structural(unittest.TestCase):
    def test_email(self):
        self.assertIn("email", rules("reach me at a.b@example.co.nz please"))

    def test_mac(self):
        self.assertIn("mac-address", rules("bssid 00:11:22:33:44:55"))

    def test_private_key_header(self):
        self.assertIn("private-key-header",
                      rules("-----BEGIN OPENSSH PRIVATE KEY-----"))

    def test_aws_key(self):
        self.assertIn("aws-access-key-id", rules("AKIAIOSFODNN7EXAMPLE"))

    def test_jwt(self):
        tok = "eyJhbGciOi.eyJzdWIiOi.SflKxwRJSM"
        self.assertIn("jwt", rules(f"token {tok}"))

    def test_ipv4_flagged(self):
        self.assertIn("ipv4", rules("gateway 10.1.3.5"))

    def test_ipv4_testnet_safe(self):
        # RFC 5737 doc range must not trip — docs legitimately use it.
        self.assertNotIn("ipv4", rules("example 192.0.2.44 in the manual"))

    def test_ipv4_unspecified_safe(self):
        self.assertNotIn("ipv4", rules("syslog target 0.0.0.0 disables it"))

    def test_semver_not_ipv4(self):
        self.assertNotIn("ipv4", rules("bumped to version 1.2.3 today"))

    def test_coordinates(self):
        self.assertIn("coordinates", rules("home at 12.3456, 98.7654"))

    def test_nz_address(self):
        self.assertIn("nz-address", rules("742 Evergreen Terrace is the place"))


class LocalTerms(unittest.TestCase):
    def terms(self, *words):
        return [(w, re.compile(r"\b" + re.escape(w) + r"\b", re.IGNORECASE))
                for w in words]

    def test_literal_word_boundary(self):
        self.assertIn("local-term", rules("call Bart about it", self.terms("Bart")))

    def test_case_insensitive(self):
        self.assertIn("local-term", rules("BART said so", self.terms("Bart")))

    def test_no_partial_word_match(self):
        # 'Bart' must not match inside 'Bartender'.
        self.assertNotIn("local-term", rules("a Bartender shift", self.terms("Bart")))

    def test_no_terms_means_structural_only(self):
        self.assertNotIn("local-term", rules("Bart here", []))


class Disable(unittest.TestCase):
    def test_disabled_rule_skipped(self):
        self.assertIn("ipv4", rules("gateway 10.0.0.5 here"))  # baseline: enabled
        fs = ls.scan_text("t", "gateway 10.0.0.5 here", [], frozenset({"ipv4"}))
        self.assertEqual([], fs)

    def test_disable_keeps_other_rules(self):
        fs = ls.scan_text("t", "10.0.0.1 and a.b@c.com", [], frozenset({"ipv4"}))
        got = {f.rule for f in fs}
        self.assertNotIn("ipv4", got)
        self.assertIn("email", got)

    def test_local_terms_survive_disable(self):
        terms = [("Acme", re.compile(r"\bAcme\b", re.IGNORECASE))]
        fs = ls.scan_text("t", "Acme at 10.0.0.1", terms,
                          frozenset({"ipv4", "email", "mac-address"}))
        self.assertEqual({"local-term"}, {f.rule for f in fs})


class Allow(unittest.TestCase):
    def test_inline_allow_marker_exempts_line(self):
        self.assertEqual([], scan("secret a.b@example.com  # leakscan:allow: doc"))

    # Rule (c) — reasoned. A marker with no reason is a mention, not an
    # exemption. This is the 2026-08-05 tightening: it used to exempt.
    def test_bare_marker_without_reason_does_not_exempt(self):
        self.assertIn("email", rules("a.b@example.com  # leakscan:allow"))

    def test_marker_with_empty_reason_does_not_exempt(self):
        self.assertIn("email", rules("a.b@example.com  # leakscan:allow:"))

    def test_prose_mention_of_the_marker_does_not_exempt(self):
        self.assertIn("email",
                      rules("we discussed the leakscan:allow marker; a.b@example.com"))

    # Rule (a) — narrow. A marker written for one rule must not silently
    # exempt a different leak sitting on the same line.
    def test_scoped_marker_exempts_only_its_own_rule(self):
        found = rules("host 172.16.31.7 mac aa:bb:cc:dd:ee:ff  "
                      "# leakscan:allow:ipv4: rendered example")
        self.assertNotIn("ipv4", found)
        self.assertIn("mac-address", found)

    def test_unscoped_marker_still_exempts_every_structural_rule(self):
        self.assertEqual([], scan("host 172.16.31.7 mac aa:bb:cc:dd:ee:ff  "
                                  "# leakscan:allow: whole line is a fixture"))

    def test_scoped_marker_naming_no_real_rule_exempts_nothing(self):
        # A typo fails CLOSED: the finding still reports rather than the
        # marker silently covering everything or nothing being checked.
        self.assertIn("ipv4",
                      rules("host 172.16.31.7  # leakscan:allow:ipv44: typo"))

    def test_reason_containing_a_colon_still_parses_as_unscoped(self):
        self.assertEqual([], scan("a.b@example.com  # leakscan:allow: see ADR 0005: public"))

    # D1 (Mike ruled 2026-08-04) — an allow-marker exempts STRUCTURAL rules
    # only; the machine-local term list is the highest-confidence layer and
    # always runs.
    def test_allow_marker_does_not_silence_the_local_term_list(self):
        terms = [("Wairarapa", re.compile(r"\bWairarapa\b", re.IGNORECASE))]
        found = scan("Wairarapa a.b@example.com  # leakscan:allow: doc", terms)
        self.assertEqual(["local-term"], [f.rule for f in found])


class Suppression(unittest.TestCase):
    """Rule (b) — a suppressed finding is counted, never silently dropped."""

    def test_marker_suppressions_are_counted_per_rule(self):
        tally = ls.Tally()
        ls.scan_text("t", "host 172.16.31.7  # leakscan:allow: fixture\n"
                          "mail a.b@example.com  # leakscan:allow: fixture\n",
                     [], frozenset(), tally)
        self.assertEqual({"ipv4": 1, "email": 1}, tally.by_marker)
        self.assertEqual(2, tally.marker_total)

    def test_clean_scan_with_no_suppressions_reports_zeros(self):
        # Known zeros are printed, so two runs can be read side by side.
        summary = ls.Tally().summary()
        self.assertIn("0 by allow-marker", summary)
        self.assertIn("0 file(s) by .leakscanignore", summary)
        self.assertIn("0 rule(s) disabled", summary)

    def test_summary_names_the_disabled_rules(self):
        self.assertIn("ipv4", ls.Tally(disabled_rules=("ipv4",)).summary())

    def test_render_reports_suppression_on_a_clean_run(self):
        tally = ls.Tally()
        tally.note_marker("email")
        out = ls.render_human([], None, True, tally)
        self.assertIn("clean", out)
        self.assertIn("1 by allow-marker", out)


class LoadTerms(unittest.TestCase):
    def test_missing_list_warns(self):
        terms, warning = ls.load_local_terms(None)
        self.assertEqual([], terms)
        self.assertIsNotNone(warning)

    def test_regex_prefix(self):
        import tempfile, os
        fd, path = tempfile.mkstemp()
        try:
            with os.fdopen(fd, "w") as fh:
                fh.write("# a comment\nregex:ACME-\\d{4}\nPlainName\n")
            terms, warning = ls.load_local_terms(ls.Path(path))
            self.assertIsNone(warning)
            self.assertEqual(2, len(terms))
            hits = rules("ticket ACME-1234 for PlainName", terms)
            self.assertIn("local-term", hits)
        finally:
            os.remove(path)


class Ignore(unittest.TestCase):
    def test_exact_glob(self):
        self.assertTrue(ls._ignored("tools/test_leakscan.py", ["tools/test_leakscan.py"]))

    def test_subtree_glob(self):
        # a bare dir/prefix glob matches everything beneath it
        self.assertTrue(ls._ignored("tiki/tests/fixtures/x.yaml", ["tiki/tests/"]))
        self.assertTrue(ls._ignored("tiki/tests/fixtures/x.yaml", ["tiki/tests"]))

    def test_non_match(self):
        self.assertFalse(ls._ignored("src/real.py", ["tools/test_leakscan.py"]))


class Redact(unittest.TestCase):
    def test_short_masked(self):
        self.assertEqual("a****", ls.redact("abcde"))

    def test_long_summarised(self):
        out = ls.redact("supersecretvalue")
        self.assertNotIn("secret", out)
        self.assertIn("chars", out)


class RequireTerms(unittest.TestCase):
    """Review B5: to automation, a degraded structural-only exit-0 pass is
    indistinguishable from full cover; --require-terms makes it fail closed."""

    def _run(self, argv):
        import os, tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as td:
            absent = str(ls.Path(td) / "absent-terms.txt")
            env = {k: v for k, v in os.environ.items()
                   if k != "ATELIER_LEAKSCAN_TERMS"}
            with mock.patch.dict(os.environ, env, clear=True), \
                 mock.patch.object(ls, "DEFAULT_LOCAL_TERMS", absent):
                return ls.main(argv + ["--root", td, td])

    def test_require_terms_fails_closed_without_list(self):
        self.assertEqual(2, self._run(["--require-terms"]))

    def test_default_still_degrades_to_pass(self):
        # the peer-adopter case: no list, no flag → structural-only, exit 0
        self.assertEqual(0, self._run([]))


class WholeTree(unittest.TestCase):
    """Whole-tree walk guards from the 2026-07-11 child-CI-floor review
    (findings N1–N3) — same class as the secretscan pins: no masked content
    dirs, no phantom-success on a bad path, ignore hatch CWD-independent."""

    def setUp(self):
        import shutil, tempfile
        self.tmp = ls.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        # A present-but-empty terms file keeps main() off any real
        # machine-local term list — structural rules are the point here.
        self.terms = self.tmp / "terms.txt"
        self.terms.write_text("")

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _main(self, argv):
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            return ls.main(argv + ["--terms", str(self.terms)])

    def test_content_dir_named_build_is_walked(self):
        # Regression (N1): `build`/`dist` are NOT hardcode-skipped — a content
        # dir sharing the name (atelier's own docs/build/) must be scanned.
        self._write("docs/build/note.md", "gateway is 10.20.30.40 today\n")
        fs = ls.scan_paths([self.tmp], self.tmp, [])
        self.assertEqual(["ipv4"], [f.rule for f in fs])

    def test_nonexistent_path_is_an_error_not_a_pass(self):
        # Regression (N2), the linkscan L1 class.
        self.assertEqual(2, self._main(["--root", str(self.tmp),
                                        str(self.tmp / "gone")]))

    def test_ignore_hatch_lives_when_cwd_is_not_root(self):
        # Regression (N3): CWD = workspace, root = repo (the floor.yml shape);
        # the repo's root-relative .leakscanignore globs must still match.
        import os
        self._write("repo/docs/fixture.md", "gateway is 10.20.30.40 today\n")
        old = os.getcwd()
        os.chdir(self.tmp)
        try:
            self.assertEqual(1, self._main(["--root", "repo", "repo"]))
            self._write("repo/.leakscanignore", "docs/fixture.md\n")
            self.assertEqual(0, self._main(["--root", "repo", "repo"]))
        finally:
            os.chdir(old)


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ls._selftest())


class StagedAbsolutePathTest(unittest.TestCase):
    """An absolute path in --staged mode must be REFUSED, not silently obeyed.

    git lists staged paths relative to the repo root, so an absolute path
    matches no prefix: the filter empties the staged set and the scan exits 0
    having covered nothing. A boundary scan that covered nothing is
    indistinguishable from one that found nothing wrong — the silent-success
    class this tool already closes for a missing path (linkscan L1).

    Found for real on 2026-07-25: tools/floor.py's first draft rendered absolute
    paths on the staged plane and every boundary check passed green.
    """

    def _run(self, *args):
        import subprocess, sys
        return subprocess.run(
            [sys.executable, str(pathlib.Path(__file__).resolve().parent / "leakscan.py"), *args],
            capture_output=True, text=True)

    def test_absolute_staged_path_is_refused(self):
        r = self._run("--staged", "--root", "/tmp", "/tmp/anything")
        self.assertEqual(r.returncode, 2, "must be an environment error, not a pass")
        self.assertIn("absolute", r.stderr.lower())

    def test_error_names_the_working_form(self):
        """A refusal that doesn't say what to do instead just gets --no-verify'd."""
        r = self._run("--staged", "--root", "/tmp", "/tmp/anything")
        self.assertIn("tiki/", r.stderr)


if __name__ == "__main__":
    unittest.main()
