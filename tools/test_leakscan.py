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


class Redact(unittest.TestCase):
    def test_short_masked(self):
        self.assertEqual("a****", ls.redact("abcde"))

    def test_long_summarised(self):
        out = ls.redact("supersecretvalue")
        self.assertNotIn("secret", out)
        self.assertIn("chars", out)


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ls._selftest())


if __name__ == "__main__":
    unittest.main()
