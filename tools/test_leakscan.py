"""Stdlib-only tests for leakscan (no pytest needed): `python3 -m unittest`."""

import re
import pathlib
import unittest

import leakscan as ls


def scan(text, terms=None):
    return ls.scan_text("t", text, terms or [])


def rules(text, terms=None):
    return {f.rule for f in scan(text, terms)}


# ===========================================================================
# THE PII CANARY SUITE — personal-data KEY SHAPES that must ALWAYS flag.
#
# CONTRACT: a canary going quiet is a DETECTION REGRESSION, never a fixture to
# update casually. If a change to the key vocabulary or to placeholder
# suppression makes one of these pass clean, the change is wrong until a
# principal rules otherwise — do not edit the canary to match the new
# behaviour, and do not delete one to make a suite green.
#
# Why it exists (G1, ruled 2026-08-04, modelled on secretscan's SF3 suite): the
# key-context layer is the ONLY cover for a whole class of personal data — date
# of birth, bank account, passport, licence, NHI, plate, next of kin — because
# the sweep's don't-add list rules out detecting any of them by shape. There is
# no second net underneath. And this rule ships WITH a suppression (placeholder
# values), which is exactly the arrangement that let secretscan's SF1 slip: a
# new exemption silently un-flagged a whole credential family and no corpus
# re-scan could see it. These are the shapes a corpus of one estate cannot
# prove.
#
# Every value here is SYNTHETIC and deliberately constructed to survive
# placeholder suppression — a canary that the tool's own suppression eats is a
# canary that proves nothing. Adding a family is welcome. Removing or weakening
# one is a decision, not a refactor.
# ===========================================================================
PII_CANARIES = (
    # --- date of birth: three spellings of the key, since a key vocabulary
    # that only knows the underscored form knows almost nothing.
    ("dob, spelled out", "date_of_birth: 1984-02-29"),
    ("dob, abbreviated", "DOB = 29/02/1984"),
    ("dob, camelCase key", "birthDate: 1984-02-29"),

    # --- financial: the hyphenated NZ shape has its own structural rule; the
    # COMPACT digit form is key-context-only by ruling, so this is its only net.
    ("bank account, hyphenated", "bank_account: 12-3456-7890123-00"),
    ("bank account, compact digits", "account_number = 1234567890123456"),
    ("card number under a key", "card_number: 4111111111111111"),
    ("card verification value", "cvv = 987"),
    ("iban under a key", "iban: GB82WEST12345698765432"),

    # --- government identifiers: letters-plus-digits is the shape of a SKU, so
    # the key name is the whole of the evidence here.
    ("passport", "passport_number: ZZ000000"),
    ("driver licence", "drivers_licence: ZZ999999"),
    ("nhi", "nhi_number: ZZZ0008"),
    ("ird number", "ird_number: 123456789"),
    ("tax file number", "tax_file_number: 987654321"),
    ("social security number", "ssn: 123-45-6789"),

    # --- health: the class with no shape at all.
    ("medication", "medication: amoxicillin"),
    ("prescription", "prescription: amoxicillin-500"),
    ("allergy", "allergies: shellfish"),
    ("blood type", "blood_type: O-negative"),
    ("patient name", "patient_name: Jane"),

    # --- people and places attached to a person.
    ("next of kin", "next_of_kin: Jane"),
    ("emergency contact", "emergency_contact: 021 555 1234"),
    ("maiden name", "maiden_name: Jane"),
    ("home address", "home_address: 12 Nowhere"),
    ("home address, camelCase key", "homeAddress: 12"),

    # --- vehicle.
    ("number plate", "number_plate: ZZZ999"),
    ("rego", "rego = ZZZ999"),

    # --- quoted value, the config-file spelling.
    ("quoted value", 'passport = "ZZ000000"'),
)


class PIICanarySuite(unittest.TestCase):
    """Standing detection canaries — see the CONTRACT comment above.

    Asserts the KEY-CONTEXT rule specifically, not merely "something flagged":
    several canaries also trip a structural rule by coincidence, and a canary
    that passes because a different rule happened to catch it would hide the
    exact regression this suite exists to catch."""

    def test_every_canary_flags_by_key_context(self):
        for name, line in PII_CANARIES:
            with self.subTest(canary=name):
                self.assertIn(
                    "pii-key-context", rules(line),
                    f"CANARY WENT QUIET: {name!r} no longer flags on key "
                    f"context. This is a detection regression in the rule or "
                    f"its placeholder suppression, not a stale fixture — fix "
                    f"the rule, do not edit this canary.")

    def test_canary_set_is_not_silently_shrunk(self):
        """Deleting a canary is the easy way to make this suite green again.

        The count is pinned so doing it has to be deliberate: raise the number
        when you ADD a family, and treat any need to lower it as a decision for
        a principal, with the reason written down."""
        self.assertGreaterEqual(len(PII_CANARIES), 27)
        self.assertEqual(len(set(PII_CANARIES)), len(PII_CANARIES),
                         "duplicate canary")


# The other direction: a documented, templated or fill-me value under the SAME
# keys must stay quiet, or the rule fires on every example config in the repo
# and gets disabled within a week.
PII_PLACEHOLDERS = (
    ("angle-bracket template", "dob: <date-of-birth>"),
    ("format spec", "dob: yyyy-mm-dd"),
    ("to-be-decided", "passport_number: TBD"),
    ("unknown", "dob: unknown"),
    ("env indirection", "bank_account: ${BANK_ACCOUNT}"),
    ("shell indirection", "emergency_contact: $CONTACT"),
    ("secret-store indirection", "card_number: !secret card"),
    ("example marker", "passport_number: EXAMPLE123"),
    ("explicit placeholder", "medication: placeholder-drug"),
    ("not applicable", "nhi_number: n/a"),
    ("redaction", "ird_number: [redacted]"),
    ("repeated fill character", "number_plate: XXXX"),
    ("fictional marker", "patient_name: fictional-person"),
)


class PIIPlaceholderSuppression(unittest.TestCase):
    """G1's other half — the suppression that keeps the key-context rule from
    firing on documentation. Paired with the canaries deliberately: the two
    suites are each other's guard rails, so widening one has to face the
    other."""

    def test_placeholders_do_not_flag(self):
        for name, line in PII_PLACEHOLDERS:
            with self.subTest(placeholder=name):
                self.assertNotIn("pii-key-context", rules(line))

    def test_placeholder_set_is_not_silently_shrunk(self):
        self.assertGreaterEqual(len(PII_PLACEHOLDERS), 13)


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

    # A reason that OPENS by quoting the flagged token is the clearest way to
    # write one, and for a while it silently exempted nothing: the first
    # character had to be `\w`, so a leading quote made the whole marker
    # unparseable and the finding still blocked. Found 2026-08-09 when a public
    # child's floor went red on a line whose marker had read correctly to every
    # human who reviewed it. Silent, because a voided marker and an absent one
    # produce identical output.
    def test_reason_may_open_with_a_quote(self):
        self.assertEqual([], scan('host 172.16.31.7  '
                                  '# leakscan:allow: "172.16.31.7" is a doc fixture'))
        self.assertEqual([], scan("host 172.16.31.7  "
                                  "# leakscan:allow: '172.16.31.7' is a doc fixture"))

    def test_reason_may_open_with_a_typographic_quote(self):
        self.assertEqual([], scan("host 172.16.31.7  "
                                  "# leakscan:allow: “172.16.31.7” is a fixture"))

    # The guard the quote fix must not weaken: an EMPTY marker still exempts
    # nothing, including the commonest Markdown spelling where the comment
    # closer follows the colon.
    def test_marker_closed_by_a_html_comment_still_does_not_exempt(self):
        self.assertIn("email",
                      rules("a.b@example.com  <!-- leakscan:allow: -->"))

    # D1 (Mike ruled 2026-08-04) — an allow-marker exempts STRUCTURAL rules
    # only; the machine-local term list is the highest-confidence layer and
    # always runs.
    def test_allow_marker_does_not_silence_the_local_term_list(self):
        terms = [("Wairarapa", re.compile(r"\bWairarapa\b", re.IGNORECASE))]
        found = scan("Wairarapa a.b@example.com  # leakscan:allow: doc", terms)
        self.assertEqual(["local-term"], [f.rule for f in found])

    # The one deliberate hatch (Mike ruled 2026-08-09): a scope NAMING
    # `local-term` — the human judging exactly that layer, on the record —
    # exempts term hits on the line. D1's accidental route stays closed.
    def test_a_scope_naming_local_term_exempts_the_term_hit(self):
        terms = [("Wairarapa", re.compile(r"\bWairarapa\b", re.IGNORECASE))]
        found = scan("Wairarapa  # leakscan:allow:local-term: published here",
                     terms)
        self.assertEqual([], found)

    def test_the_local_term_scope_is_counted_never_silent(self):
        terms = [("Wairarapa", re.compile(r"\bWairarapa\b", re.IGNORECASE))]
        tally = ls.Tally()
        ls.scan_text("t", "Wairarapa  # leakscan:allow:local-term: published",
                     terms, frozenset(), tally)
        self.assertEqual({"local-term": 1}, tally.by_marker)

    def test_comma_scopes_compose_across_layers(self):
        # The forcing case's real shape: a published identity line needs the
        # structural email rule AND the term layer exempted, one marker, each
        # covered rule named.
        terms = [("Wairarapa", re.compile(r"\bWairarapa\b", re.IGNORECASE))]
        line = ("Wairarapa a.b@example.com  "
                "# leakscan:allow:email,local-term: published worked example")
        self.assertEqual([], scan(line, terms))

    def test_a_local_term_scope_does_not_drag_structural_rules_with_it(self):
        terms = [("Wairarapa", re.compile(r"\bWairarapa\b", re.IGNORECASE))]
        found = scan("Wairarapa a.b@example.com  "
                     "# leakscan:allow:local-term: name is public, email is not",
                     terms)
        self.assertEqual(["email"], [f.rule for f in found])

    def test_a_local_term_scope_without_a_reason_exempts_nothing(self):
        terms = [("Wairarapa", re.compile(r"\bWairarapa\b", re.IGNORECASE))]
        found = scan("Wairarapa  # leakscan:allow:local-term:", terms)
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
            self._write("repo/.leakscanignore", "# a reasoned fixture exemption\ndocs/fixture.md\n")
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


class IgnoreFileReasons(unittest.TestCase):
    """GUARDS.md rule (c) — an ignore glob is the widest allowance a scanner
    grants, so it is the last place an unexplained exemption should be
    possible. Enforced 2026-08-05; previously any bare glob was honoured."""

    def setUp(self):
        import tempfile, shutil
        self.tmp = pathlib.Path(tempfile.mkdtemp(prefix="leakscan-ign-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def _write(self, body):
        (self.tmp / ".leakscanignore").write_text(body, encoding="utf-8")
        return ls.load_ignore_globs(self.tmp)

    def test_stanza_comment_is_a_reason(self):
        self.assertEqual(["docs/x.md"], self._write("# frozen history\ndocs/x.md\n"))

    def test_trailing_comment_is_a_reason(self):
        self.assertEqual(["docs/x.md"], self._write("docs/x.md  # frozen history\n"))

    def test_several_globs_share_one_stanza_comment(self):
        # The live files do this: one reason covering a group of globs.
        self.assertEqual(["a.md", "b.md"], self._write("# both are fixtures\na.md\nb.md\n"))

    def test_bare_glob_with_no_reason_is_refused(self):
        with self.assertRaises(ls.IgnoreFileError):
            self._write("docs/x.md\n")

    def test_blank_line_ends_the_stanza(self):
        # A comment cannot reason a glob it has been separated from.
        with self.assertRaises(ls.IgnoreFileError):
            self._write("# covers the one below\na.md\n\nb.md\n")

    def test_error_names_every_unreasoned_line(self):
        with self.assertRaises(ls.IgnoreFileError) as cm:
            self._write("a.md\nb.md\n")
        self.assertEqual(2, len(cm.exception.entries))

    def test_main_exits_2_on_an_unreasoned_ignore_file(self):
        # A broken scan is not a pass.
        (self.tmp / ".leakscanignore").write_text("docs/x.md\n", encoding="utf-8")
        (self.tmp / "doc.md").write_text("clean\n", encoding="utf-8")
        self.assertEqual(2, ls.main(["--root", str(self.tmp), str(self.tmp)]))


class IPv6Shape(unittest.TestCase):
    """D2 (ruled 2026-08-04, and E4 with it) — the rule took any THREE
    colon-separated hex-ish groups, which is also `HH:MM:SS`, a port map, a
    ratio and a hex colour triplet. Now it requires `::` or four-plus groups.
    Both directions pinned, because a tightening is the one kind of change
    that can quietly become a hole."""

    # --- must PASS (the false-positive class the sweep measured)
    def test_two_clock_times_do_not_flag(self):
        self.assertNotIn("ipv6", rules("ran 03:04:05 to 03:04:09"))

    def test_single_clock_time_does_not_flag(self):
        self.assertNotIn("ipv6", rules("elapsed 12:34:56 total"))

    def test_port_map_does_not_flag(self):
        self.assertNotIn("ipv6", rules("ports 8080:80:443 in compose"))

    def test_ratio_does_not_flag(self):
        self.assertNotIn("ipv6", rules("mix ratio 16:9:4 by volume"))

    def test_hex_colour_triplet_does_not_flag(self):
        self.assertNotIn("ipv6", rules("colour aa:bb:cc on the swatch"))

    def test_python_slice_does_not_flag(self):
        # The compressed form needs TWO hex groups, so `a[::2]` is not an
        # address. `::1` and the bare unspecified address are out for the same
        # reason — they carry no topology.
        self.assertNotIn("ipv6", rules("take every second item a[::2] here"))

    def test_scope_resolution_does_not_flag(self):
        self.assertNotIn("ipv6", rules("std::vector<int> holds them"))

    # --- must FLAG (real addresses, including the ULA shape the estate uses)
    def test_full_eight_group_address_flags(self):
        self.assertIn("ipv6",
                      rules("host 2001:0db8:85a3:0000:0000:8a2e:0370:7334"))

    def test_four_group_address_flags(self):
        self.assertIn("ipv6", rules("prefix fd00:1234:5678:9abc"))

    def test_compressed_address_flags(self):
        self.assertIn("ipv6", rules("gw fe80::1c2d:3e4f:5a6b:7c8d"))

    def test_ula_with_trailing_compression_flags(self):
        self.assertIn("ipv6", rules("ula fd12:3456:789a::1"))

    def test_leading_compression_flags(self):
        self.assertIn("ipv6", rules("addr ::abcd:1234 on the link"))


class IPv4SafeSet(unittest.TestCase):
    """D3 + D6 (ruled 2026-08-04): widen the safe set to the addresses that
    carry no topology, and match fixed values EXACTLY."""

    def test_netmasks_are_safe(self):
        for mask in ("255.255.255.0", "255.255.0.0", "255.0.0.0",
                     "255.255.254.0", "255.255.255.252"):
            with self.subTest(mask=mask):
                self.assertNotIn("ipv4", rules(f"netmask {mask} applies"))

    def test_broadcast_and_unspecified_are_safe(self):
        self.assertNotIn("ipv4", rules("broadcast 255.255.255.255"))
        self.assertNotIn("ipv4", rules("bind 0.0.0.0 for all interfaces"))

    def test_loopback_net_is_safe(self):
        self.assertNotIn("ipv4", rules("listening on 127.0.0.1 only"))

    def test_public_resolvers_are_safe(self):
        for r in ("8.8.8.8", "8.8.4.4", "1.1.1.1", "9.9.9.9",
                  "208.67.222.222"):
            with self.subTest(resolver=r):
                self.assertNotIn("ipv4", rules(f"upstream {r} configured"))

    # --- the safe set must not become a hole
    def test_private_space_still_flags(self):
        for addr in ("10.1.2.3", "192.168.1.1", "172.16.31.7", "100.64.1.1",
                     "169.254.1.1"):
            with self.subTest(addr=addr):
                self.assertIn("ipv4", rules(f"gateway {addr} here"))

    def test_d6_exact_match_not_prefix(self):
        # The old startswith test exempted anything BEGINNING with the
        # unspecified address, so a longer final octet rode in free.
        self.assertIn("ipv4", rules("odd literal 0.0.0.05 in a config"))

    def test_doc_ranges_still_match_by_prefix(self):
        # These are network prefixes, so prefix matching is the correct
        # semantics for them and stays.
        self.assertNotIn("ipv4", rules("example 198.51.100.7 in the manual"))


class AddressSuffixGuard(unittest.TestCase):
    """D4 (ruled 2026-08-04) — abbreviated and bare-word suffixes need at least
    one capitalised word in front of them."""

    def test_bare_abbreviation_does_not_flag(self):
        for line in ("see 3 St for the count", "figure 1 Dr in the paper",
                     "row 2 Ave of the table", "item 4 Pl below"):
            with self.subTest(line=line):
                self.assertNotIn("nz-address", rules(line))

    def test_bare_ordinary_word_suffix_does_not_flag(self):
        for line in ("the 2 Green fields", "5 Way options", "3 Close calls",
                     "12 Hill sections", "7 Place holders"):
            with self.subTest(line=line):
                self.assertNotIn("nz-address", rules(line))

    def test_named_street_still_flags_with_an_abbreviation(self):
        self.assertIn("nz-address", rules("12 Fictional St, Wellington"))

    def test_two_word_street_name_still_flags(self):
        self.assertIn("nz-address", rules("28 Some Other Hill is the place"))

    def test_distinctive_full_word_suffix_keeps_the_permissive_form(self):
        # Not narrowed: these suffixes are distinctive enough on their own.
        self.assertIn("nz-address", rules("742 Terrace was the answer"))
        self.assertIn("nz-address", rules("742 Evergreen Terrace"))


class MacIPv6Dedupe(unittest.TestCase):
    """D5 (ruled 2026-08-04) — one span, one finding. A duplicated finding
    teaches a reader to skim, which is how a real second finding gets missed."""

    def test_mac_reports_once(self):
        self.assertEqual(["mac-address"],
                         [f.rule for f in scan("bssid aa:bb:cc:dd:ee:ff")])

    def test_a_real_ipv6_on_the_same_line_still_reports(self):
        got = [f.rule for f in scan("aa:bb:cc:dd:ee:ff and fd00:1:2:3:4:5")]
        self.assertIn("mac-address", got)
        self.assertIn("ipv6", got)

    def test_disabling_the_shadowing_rule_leaves_no_blind_spot(self):
        # If mac-address is off, the ipv6 rule must step back in rather than
        # the span vanishing from both.
        fs = ls.scan_text("t", "bssid aa:bb:cc:dd:ee:ff", [],
                          frozenset({"mac-address"}))
        self.assertEqual(["ipv6"], [f.rule for f in fs])

    def test_an_exempted_mac_is_not_re_reported_as_ipv6(self):
        # The marker was written for the MAC; the ipv6 rule must not undo it.
        self.assertEqual([], scan("bssid aa:bb:cc:dd:ee:ff  "
                                  "# leakscan:allow: fixture"))


class FinancialIdentifiers(unittest.TestCase):
    """G4 (ruled 2026-08-04) — Luhn-checked cards, mod-97 IBANs, and the NZ
    hyphenated bank-account shape. Bare-digit forms stay key-context-only."""

    # 4111111111111111 is the industry-standard test card; no real number is
    # used anywhere in this suite.
    def test_bare_card_number_flags(self):
        self.assertIn("payment-card", rules("card 4111111111111111 on file"))

    def test_space_grouped_card_flags(self):
        self.assertIn("payment-card", rules("card 4111 1111 1111 1111"))

    def test_hyphen_grouped_card_flags(self):
        self.assertIn("payment-card", rules("card 4111-1111-1111-1111"))

    def test_fifteen_digit_card_flags(self):
        self.assertIn("payment-card", rules("card 378282246310005"))

    def test_failed_luhn_does_not_flag(self):
        self.assertNotIn("payment-card", rules("ref 4111111111111112 here"))

    def test_non_card_digit_run_does_not_flag(self):
        # Passes no check digit, and would be the don't-add list's bare-digit
        # rule if it did.
        self.assertNotIn("payment-card", rules("id 1234567890123456"))

    def test_long_id_with_a_bad_issuer_prefix_does_not_flag(self):
        # Luhn-valid but starts outside the payment-card industry range.
        self.assertNotIn("payment-card", rules("seq 7992739871000019"))

    def test_iban_flags(self):
        self.assertIn("iban", rules("pay to GB82WEST12345698765432 please"))

    def test_iban_with_a_bad_checksum_does_not_flag(self):
        self.assertNotIn("iban", rules("code AB12CDEFGHIJKLMNOPQR here"))

    def test_uppercase_identifier_does_not_flag_as_iban(self):
        self.assertNotIn("iban", rules("const XX99ABCDEFGHIJKLMN = 1"))

    def test_nz_bank_account_flags(self):
        self.assertIn("nz-bank-account", rules("acct 12-3456-7890123-00"))

    def test_nz_bank_account_three_digit_suffix_flags(self):
        self.assertIn("nz-bank-account", rules("acct 12-3456-7890123-000"))

    def test_compact_bank_digits_stay_key_context_only(self):
        # The ruling: the compact form must NOT be a standalone rule.
        found = rules("the number 1234567890123456 appeared")
        self.assertNotIn("nz-bank-account", found)
        self.assertNotIn("pii-key-context", found)
        self.assertIn("pii-key-context", rules("bank_account: 1234567890123456"))

    def test_bare_ird_digits_stay_key_context_only(self):
        self.assertEqual(set(), rules("the number 123456789 appeared"))
        self.assertIn("pii-key-context", rules("ird_number: 123456789"))


class BracketedPhone(unittest.TestCase):
    """G7 (ruled 2026-08-04) — the bracketed area-code form, the one common NZ
    spelling the rule missed."""

    def test_bracketed_landline_flags(self):
        self.assertIn("nz-phone", rules("call (04) 555 1234 today"))

    def test_bracketed_mobile_prefix_flags(self):
        self.assertIn("nz-phone", rules("call (021) 555 1234 today"))

    def test_bracketed_without_a_space_flags(self):
        self.assertIn("nz-phone", rules("call (09)555 1234"))

    def test_unbracketed_forms_still_flag(self):
        for line in ("+64 21 555 1234", "021 555 1234", "09 555 1234"):
            with self.subTest(line=line):
                self.assertIn("nz-phone", rules(f"ring {line} now"))


class PathScanning(unittest.TestCase):
    """G2 (ruled 2026-08-04) — the repo-relative PATH runs through the same
    rule set, reported at line 0. Measured cost when proposed: zero findings
    over this repo's 390 tracked paths."""

    def test_a_leak_in_the_file_name_is_found(self):
        fs = ls.scan_path_name("logs/10.1.2.3.txt", [])
        self.assertEqual(["ipv4"], [f.rule for f in fs])

    def test_path_findings_report_at_line_zero(self):
        fs = ls.scan_path_name("notes/a.b@example.com.md", [])
        self.assertEqual([0], [f.line for f in fs])

    def test_ordinary_repo_paths_are_clean(self):
        for rel in ("docs/method/00-APEX.md", "tools/leakscan.py",
                    "docs/sessions/2026-08-03-2050-leakscan-pii-sweep.md",
                    "docs/decisions/0005-make-atelier-public.md",
                    ".github/workflows/floor.yml"):
            with self.subTest(rel=rel):
                self.assertEqual([], ls.scan_path_name(rel, []))

    def test_local_terms_run_over_the_path_too(self):
        terms = [("Acme", re.compile(r"\bAcme\b", re.IGNORECASE))]
        fs = ls.scan_path_name("docs/Acme.md", terms)
        self.assertEqual(["local-term"], [f.rule for f in fs])

    def test_render_names_the_path_rather_than_a_line_number(self):
        out = ls.render_human(ls.scan_path_name("logs/10.1.2.3.txt", []),
                              None, True)
        self.assertIn("in the path name", out)

    def test_whole_tree_scan_reads_the_name_of_a_binary_it_cannot_read(self):
        import shutil, tempfile
        tmp = ls.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        (tmp / "10.1.2.3.bin").write_bytes(b"\x00\x01\x02binary")
        fs = ls.scan_paths([tmp], tmp, [])
        self.assertEqual(["ipv4"], [f.rule for f in fs])


class DerivedTermForms(unittest.TestCase):
    """G6 (ruled 2026-08-04) — OPT-IN derivation of a listed name's slug,
    camel, snake and split forms. A name leaks as a slug far more often than as
    the canonical spaced literal; the sweep probed every derived form and all
    of them passed clean."""

    def forms(self, term):
        return [(term, ls.derived_form_regex(term))]

    def test_derived_forms_match(self):
        terms = self.forms("Jane Q Public")
        for text in ("jane-q-public", "jane_q_public", "jane.q.public",
                     "janeQPublic", "JaneQPublic", "janeqpublic",
                     "Jane  Q  Public", "Jane Q Public"):
            with self.subTest(form=text):
                self.assertIn("local-term", rules(f"see {text} today", terms))

    def test_derivation_still_respects_word_boundaries(self):
        self.assertNotIn("local-term",
                         rules("a Bartender shift", self.forms("Bart")))

    def test_a_different_name_does_not_match(self):
        self.assertNotIn("local-term",
                         rules("jane-public here", self.forms("Jane Q Public")))

    def test_derivation_is_opt_in_not_the_default(self):
        # The plain literal form must be UNCHANGED — an operator who did not
        # ask for derivation does not silently get it.
        plain = [("Jane Q Public",
                  re.compile(r"\bJane Q Public\b", re.IGNORECASE))]
        self.assertNotIn("local-term", rules("jane-q-public", plain))

    def test_forms_prefix_parses_from_a_term_file(self):
        import os, tempfile
        fd, path = tempfile.mkstemp()
        try:
            with os.fdopen(fd, "w") as fh:
                fh.write("# a comment\nforms:Jane Q Public\nPlainName\n")
            terms, warning = ls.load_local_terms(ls.Path(path))
            self.assertIsNone(warning)
            self.assertEqual(2, len(terms))
            self.assertIn("local-term", rules("file jane-q-public.md", terms))
            self.assertNotIn("local-term", rules("plain-name here", terms))
        finally:
            os.remove(path)
