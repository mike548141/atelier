"""Stdlib-only tests for leakscan (no pytest needed): `python3 -m unittest`."""

import re
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


if __name__ == "__main__":
    unittest.main()
