"""Stdlib-only tests for leakscan (no pytest needed): `python3 -m unittest`."""

import contextlib
import datetime
import io
import json
import os
import re
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import unittest
import unittest.mock
from pathlib import Path

import allowmarker
import leakscan as ls
import memprobe
import test_support_regex as rxsupport

REPO_ROOT = Path(__file__).resolve().parent.parent

TOOLS_DIR = Path(__file__).resolve().parent


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


def blocking(fs):
    return {f.rule for f in fs if f.blocks}


def reporting(fs):
    return {f.rule for f in fs if not f.blocks}


class Disable(unittest.TestCase):
    """115/090: a disabled rule REPORTS instead of being skipped. Before it,
    `--disable` dropped the rule's hits unseen."""

    def test_disabled_rule_reports_without_blocking(self):
        self.assertIn("ipv4", blocking(scan("gateway 10.0.0.5 here")))  # baseline
        fs = ls.scan_text("t", "gateway 10.0.0.5 here", [], frozenset({"ipv4"}))
        self.assertEqual((set(), {"ipv4"}), (blocking(fs), reporting(fs)))

    def test_disable_keeps_other_rules_blocking(self):
        fs = ls.scan_text("t", "10.0.0.1 and a.b@c.com", [], frozenset({"ipv4"}))
        self.assertEqual({"email"}, blocking(fs))
        self.assertEqual({"ipv4"}, reporting(fs))

    def test_local_terms_survive_disable(self):
        terms = [("Acme", re.compile(r"\bAcme\b", re.IGNORECASE))]
        fs = ls.scan_text("t", "Acme at 10.0.0.1", terms,
                          frozenset({"ipv4", "email", "mac-address"}))
        self.assertEqual({"local-term"}, blocking(fs))
        self.assertEqual({"ipv4"}, reporting(fs))


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


class PluralInflection(unittest.TestCase):
    """Ruled 2026-09-18 (roadmap 320/240): a listed term must ALSO catch its
    plural and plural-possessive, always on, fails closed — a possessive was
    the live shape that evaded a correctly-listed term while the scanner
    reported the file clean. Synthetic terms only, per the queue-run brief."""

    def _terms(self, body):
        import tempfile, os
        fd, path = tempfile.mkstemp()
        try:
            with os.fdopen(fd, "w") as fh:
                fh.write(body)
            terms, warning = ls.load_local_terms(ls.Path(path))
            self.assertIsNone(warning)
            return terms
        finally:
            os.remove(path)

    def test_bare_term_still_matches(self):
        terms = self._terms("Xxxx\n")
        self.assertIn("local-term", rules("call Xxxx today", terms))

    def test_singular_possessive_matches(self):
        # \bXxxx\b already matched Xxxx's before this change (boundary sits
        # before the apostrophe regardless of what follows) — this pins that
        # so a future refactor can't silently lose it.
        terms = self._terms("Xxxx\n")
        self.assertIn("local-term", rules("read Xxxx's report", terms))

    def test_bare_plural_matches(self):
        terms = self._terms("Xxxx\n")
        self.assertIn("local-term", rules("the Xxxxs arrived", terms))

    def test_plural_possessive_matches(self):
        terms = self._terms("Xxxx\n")
        self.assertIn("local-term", rules("the Xxxxs' report", terms))

    def test_substring_inside_a_longer_word_still_does_not_match(self):
        # The inflection must not reopen the word-boundary gap it closed:
        # a term must still not match inside an unrelated longer word.
        terms = self._terms("ann\n")
        self.assertNotIn("local-term", rules("the annual review", terms))
        self.assertIn("local-term", rules("call ann today", terms))

    def test_forms_prefix_also_gets_the_plural_suffix(self):
        terms = self._terms("forms:Jane Q Public\n")
        self.assertIn("local-term", rules("see jane-q-publics today", terms))
        self.assertIn("local-term", rules("see jane-q-publics' report", terms))

    def test_regex_prefix_term_is_not_pluralised(self):
        # regex: is operator-authored verbatim and must be untouched by this.
        terms = self._terms("regex:Widget-\\d{3}\n")
        body, pattern = terms[0]
        self.assertEqual(pattern.pattern, "Widget-\\d{3}")


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


class CommitMessages(unittest.TestCase):
    """`--messages` (320/550): the same rule sets over a commit message, read
    only. A synthetic term in a temp list, so no real name enters the repo."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.terms = self.root / "terms.txt"
        self.terms.write_text("zephyrquill\n", encoding="utf-8")
        for args in (["init", "-q", "-b", "main"], ["config", "user.name", "t"],
                     ["config", "user.email", "t@example.invalid"],  # leakscan:allow: RFC-2606 fixture identity
                     ["config", "commit.gpgsign", "false"]):
            subprocess.run(["git", "-C", str(self.root), *args], check=True,
                           capture_output=True)

    def tearDown(self):
        self.tmp.cleanup()

    def _commit(self, name, message):
        (self.root / name).write_text("x\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", name], check=True,
                       capture_output=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-q", "-m", message],
                       check=True, capture_output=True)

    def _run(self, *argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = ls.main(["--root", str(self.root), "--terms", str(self.terms), *argv])
        return rc, out.getvalue()

    def test_a_body_hit_is_found_and_never_blocks(self):
        self._commit("a", "clean title\n\nthe body names zephyrquill here")
        rc, out = self._run("--messages")
        self.assertEqual(rc, 0, out)
        self.assertIn("1 finding(s) in 1 of 1", out)
        self.assertNotIn("zephyrquill", out, "a finding never prints the term")

    def test_an_authorship_trailer_is_not_a_finding(self):
        self._commit("a", "title\n\nbody\n\n"
                          "Co-Authored-By: Someone <noreply@example.invalid>")  # leakscan:allow: RFC-2606 fixture identity
        rc, out = self._run("--messages")
        self.assertEqual(rc, 0, out)
        self.assertIn("0 finding(s) in 0 of 1", out)

    def test_a_clean_log_reports_zero(self):
        self._commit("a", "clean title")
        rc, out = self._run("--messages")
        self.assertEqual(rc, 0, out)
        self.assertIn("0 finding(s) in 0 of 1", out)

    def test_a_range_reads_only_that_range(self):
        self._commit("a", "names zephyrquill")
        self._commit("b", "clean title")
        rc, out = self._run("--messages", "HEAD^..HEAD")
        self.assertEqual(rc, 0, out)
        self.assertIn("0 finding(s) in 0 of 1", out)

    def test_a_marker_in_a_message_exempts_nothing(self):
        self._commit("a", "x zephyrquill <!-- leakscan:allow:local-term: a reason -->")
        rc, out = self._run("--messages")
        self.assertEqual(rc, 0, out)
        self.assertIn("1 finding(s)", out)

    def test_an_unreadable_range_is_broken_not_clean(self):
        self._commit("a", "x")
        rc, _ = self._run("--messages", "nosuch..HEAD")
        self.assertEqual(rc, 2)

    def test_it_refuses_paths_and_staged(self):
        self.assertEqual(self._run("--messages", "--staged")[0], 2)
        self.assertEqual(self._run("--messages", "HEAD", "somepath")[0], 2)


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

    def test_an_explicit_terms_path_that_does_not_exist_is_an_error(self):
        """AP4 (ruled 2026-08-23): a mistyped dedicated-list path silently
        fell back to the default list — quieter cover on exactly the plane
        EP3 hardened against silent degradation. Explicit-but-missing is now
        exit 2, on both the flag and the env var."""
        self.assertEqual(2, self._run(["--terms", "/nonexistent/terms.txt"]))
        import os
        from unittest import mock
        with mock.patch.dict(os.environ,
                             {"ATELIER_LEAKSCAN_TERMS": "/nonexistent/t.txt"}):
            with self.assertRaises(ls.TermsPathError):
                ls.resolve_terms_path(None)

    def _run_capture(self, argv, env_terms=None):
        """(exit, stdout, stderr) with the machine's own list kept out of it."""
        import contextlib, io, os, tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as td:
            absent = str(ls.Path(td) / "absent-terms.txt")
            env = {k: v for k, v in os.environ.items()
                   if k != "ATELIER_LEAKSCAN_TERMS"}
            if env_terms is not None:
                env["ATELIER_LEAKSCAN_TERMS"] = env_terms
            out, err = io.StringIO(), io.StringIO()
            with mock.patch.dict(os.environ, env, clear=True), \
                 mock.patch.object(ls, "DEFAULT_LOCAL_TERMS", absent), \
                 contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                rc = ls.main(argv + ["--root", td, td])
            return rc, out.getvalue(), err.getvalue()

    def test_an_empty_term_list_is_refused_under_require_terms(self):
        """AR3: a zero-byte list (a failed sync, a truncated write) satisfied
        --require-terms, loaded nothing, and the pass line claimed local cover.
        Comments-only loads nothing either."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            for body in ("", "# just a comment\n\n"):
                f = ls.Path(td) / "t.txt"
                f.write_text(body)
                rc, out, err = self._run_capture(
                    ["--require-terms", "--terms", str(f)])
                self.assertEqual(2, rc, repr(body))
                self.assertIn("holds no terms", err)
                self.assertNotIn("clean", out)

    def test_an_empty_term_list_without_require_terms_is_structural_only(self):
        """The CI / fixture case must stay green, but must not claim cover: it
        degrades exactly as an absent list does, with a warning naming it."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            f = ls.Path(td) / "t.txt"
            f.write_text("")
            rc, out, err = self._run_capture(["--terms", str(f)])
        self.assertEqual(0, rc)
        self.assertIn("structural only", out)
        self.assertNotIn("structural + local", out)
        self.assertIn("holds no terms", out)

    def test_a_populated_term_list_still_claims_local_cover(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            f = ls.Path(td) / "t.txt"
            f.write_text("zzz-no-fixture-has-this\n")
            rc, out, err = self._run_capture(
                ["--require-terms", "--terms", str(f)])
        self.assertEqual(0, rc)
        self.assertIn("structural + local", out)

    def test_an_unreadable_term_list_is_exit_2_with_a_remedy(self):
        """AR3: a directory, or a mode-000 file, was a raw traceback and exit 1
        with no remedy -- the 'reaches for --no-verify' hazard."""
        import os, tempfile
        with tempfile.TemporaryDirectory() as td:
            d = ls.Path(td) / "adir"
            d.mkdir()
            rc, out, err = self._run_capture(["--terms", str(d)])
            self.assertEqual(2, rc)
            self.assertIn("cannot be read", err)
            self.assertIn("--terms", err)
            self.assertNotIn("Traceback", err)
            f = ls.Path(td) / "locked.txt"
            f.write_text("zzz\n")
            f.chmod(0)
            try:
                if not os.access(f, os.R_OK):    # root can read anything
                    rc, out, err = self._run_capture(["--terms", str(f)])
                    self.assertEqual(2, rc)
                    self.assertIn("cannot be read", err)
            finally:
                f.chmod(0o600)

    def test_an_empty_explicit_value_is_refused_under_require_terms_only(self):
        """AR3: `--terms ""` / `ATELIER_LEAKSCAN_TERMS=` under --require-terms
        fell through to the default list silently. Refused there; without the
        flag it still means 'not set' (CI routes an unset secret into the env
        var as an empty string, and CI holds no list)."""
        rc, out, err = self._run_capture(["--require-terms", "--terms", ""])
        self.assertEqual(2, rc)
        self.assertIn("set but empty", err)
        rc, out, err = self._run_capture(["--require-terms"], env_terms="")
        self.assertEqual(2, rc)
        self.assertIn("$ATELIER_LEAKSCAN_TERMS is set but empty", err)
        # without --require-terms: today's behaviour, structural-only exit 0
        self.assertEqual(0, self._run_capture(["--terms", ""])[0])
        self.assertEqual(0, self._run_capture([], env_terms="")[0])


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
        #
        # The target is spelled `.` rather than `repo` since 2026-08-23: a
        # relative target resolves against --root, so `repo` now means
        # `repo/repo` and exits 2 (loudly, which is the point — roadmap
        # 010/110). `.` is the root itself under either reading.
        import os
        self._write("repo/docs/fixture.md", "gateway is 10.20.30.40 today\n")
        old = os.getcwd()
        os.chdir(self.tmp)
        try:
            self.assertEqual(1, self._main(["--root", "repo", "."]))
            self._write("repo/.leakscanignore", "# a reasoned fixture exemption\ndocs/fixture.md\n")
            self.assertEqual(0, self._main(["--root", "repo", "."]))
            # And the mixed-root spelling is refused rather than silently
            # scanning the workspace: repo/repo does not exist.
            self.assertEqual(2, self._main(["--root", "repo", "repo"]))
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

    @classmethod
    def setUpClass(cls):
        # LK4: when the tree is not a git work tree (a source export), leakscan's
        # `git diff` fails first (exit 129, "git diff failed"), so these two
        # tests would fail on their message text and not on what they assert.
        r = subprocess.run(["git", "-C", str(REPO_ROOT), "rev-parse", "--git-dir"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            raise unittest.SkipTest("not inside a git work tree")

    def _run(self, *args):
        import subprocess, sys
        return subprocess.run(
            [sys.executable, str(pathlib.Path(__file__).resolve().parent / "leakscan.py"), *args],
            capture_output=True, text=True, cwd=REPO_ROOT)

    def test_absolute_staged_path_is_refused(self):
        r = self._run("--staged", "--root", str(REPO_ROOT), "/tmp/anything")
        self.assertEqual(r.returncode, 2, "must be an environment error, not a pass")
        self.assertIn("absolute", r.stderr.lower())

    def test_error_names_the_working_form(self):
        """A refusal that doesn't say what to do instead just gets --no-verify'd."""
        r = self._run("--staged", "--root", str(REPO_ROOT), "/tmp/anything")
        self.assertIn("tiki/", r.stderr)


class StagedQuotedPaths(unittest.TestCase):
    """115/260 — a staged file whose path git quotes was never scanned: its
    `+++ "b/…"` header did not start `+++ b/`, so its added lines belonged to
    no file and a leak in them reached the commit. Real git, each spelling git
    quotes: a non-ASCII directory, a double quote, a tab, a backslash. The
    term list is an EMPTY file, so only the structural shapes are in play."""

    NAMES = ["café/note.md", 'say "hi".md', "tab\tname.md",
             "back\\slash.md"]
    # Assembled so this file does not itself carry the shape it plants.
    LEAK = "-----BEGIN " + "RSA PRIVATE KEY-----\n"

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo, ignore_errors=True)
        self._git("init", "-q")
        empty = self.repo / "no-terms.txt"      # untracked; never staged
        empty.write_text("")
        env = unittest.mock.patch.dict(
            os.environ, {"ATELIER_LEAKSCAN_TERMS": str(empty)})
        env.start()
        self.addCleanup(env.stop)
        old = os.getcwd()
        os.chdir(self.repo)
        self.addCleanup(os.chdir, old)

    def _git(self, *args):
        return subprocess.run(["git", "-C", str(self.repo), "-c", "commit.gpgsign=false", *args],
                              capture_output=True, text=True, check=True)

    def _stage(self, name, text):
        p = self.repo / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        self._git("add", "--", name)

    def _main(self, *argv):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), \
                contextlib.redirect_stderr(io.StringIO()):
            return ls.main(["--staged", "--root", str(self.repo), *argv]), \
                buf.getvalue()

    def test_added_lines_are_keyed_by_the_real_path(self):
        for name in self.NAMES:
            with self.subTest(name=name):
                self._stage(name, "x\n")
                self.assertIn(name, ls.staged_added_lines())

    def test_a_planted_leak_is_found_and_the_path_reported_unquoted(self):
        for name in self.NAMES:
            with self.subTest(name=name):
                self._stage(name, "ok\n" + self.LEAK)
                code, out = self._main("--json")
                self.assertEqual(1, code)
                hits = {(f["path"], f["rule"])
                        for f in json.loads(out)["findings"]}
                self.assertIn((name, "private-key-header"), hits)
                self._git("rm", "-q", "-f", "--", name)

    def test_a_clean_quoted_path_still_passes(self):
        self._stage("café/ok.md", "# fine\n")
        code, _ = self._main()
        self.assertEqual(0, code)


class StagedPosedHeader(unittest.TestCase):
    """115/280 — an added line whose text begins `++ b/…` prints as `+++ b/…`,
    which `report.diff_header_path` accepts as a header. The old reader moved
    attribution to the posed (here ignored) path, hiding the leak after it, and
    dropped the posed line itself as "not an added line". The term list is an
    EMPTY file, so only the structural shapes are in play."""

    # Assembled so this file does not itself carry the shape it plants.
    LEAK = "-----BEGIN " + "RSA PRIVATE KEY-----"

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo, ignore_errors=True)
        self._git("init", "-q")
        empty = self.repo / "no-terms.txt"      # untracked; never staged
        empty.write_text("")
        (self.repo / ".leakscanignore").write_text(
            "docs/ignored.md  # fixture: the path the posed header names\n")
        env = unittest.mock.patch.dict(
            os.environ, {"ATELIER_LEAKSCAN_TERMS": str(empty)})
        env.start()
        self.addCleanup(env.stop)
        old = os.getcwd()
        os.chdir(self.repo)
        self.addCleanup(os.chdir, old)

    def _git(self, *args):
        return subprocess.run(["git", "-C", str(self.repo), "-c", "commit.gpgsign=false", *args],
                              capture_output=True, text=True, check=True)

    def _stage(self, name, text):
        p = self.repo / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        self._git("add", "--", name)

    def _paths(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), \
                contextlib.redirect_stderr(io.StringIO()):
            code = ls.main(["--staged", "--root", str(self.repo), "--json"])
        return code, sorted(f["path"] for f in json.loads(buf.getvalue())["findings"])

    def test_a_posed_ignored_header_does_not_hide_the_leak_after_it(self):
        self._stage("posed.md", f"ok\n++ b/docs/ignored.md\n{self.LEAK}\n")
        self.assertEqual(
            {"posed.md": [(1, "ok"), (2, "++ b/docs/ignored.md"),
                          (3, self.LEAK)]},
            ls.staged_added_lines())
        self.assertEqual((1, ["posed.md"]), self._paths())

    def test_a_posed_quoted_header_does_not_hide_it_either(self):
        self._stage("posed.md", f'++ "b/docs/ignored.md"\n{self.LEAK}\n')
        self.assertEqual((1, ["posed.md"]), self._paths())

    def test_a_posed_line_is_itself_scanned(self):
        self._stage("posed.md", f"++ {self.LEAK}\n")
        self.assertEqual((1, ["posed.md"]), self._paths())

    def test_a_real_ignored_file_is_still_ignored(self):
        self._stage("docs/ignored.md", self.LEAK + "\n")
        self.assertEqual((0, []), self._paths())


class StagedRealLineNumbers(unittest.TestCase):
    """115/300 — a finding on the staged plane is reported at its line in the
    file, not at its position among the file's added lines. The old code
    joined the added lines and numbered the blob from 1, so a leak staged on
    line 5 of a file whose lines 1-4 were already committed was reported at
    line 1. The term list is an EMPTY file, so only the structural shapes are
    in play."""

    # Assembled so this file does not itself carry the shape it plants.
    LEAK = "-----BEGIN " + "RSA PRIVATE KEY-----"

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo, ignore_errors=True)
        self._git("init", "-q")
        empty = self.repo / "no-terms.txt"      # untracked; never staged
        empty.write_text("")
        env = unittest.mock.patch.dict(
            os.environ, {"ATELIER_LEAKSCAN_TERMS": str(empty)})
        env.start()
        self.addCleanup(env.stop)
        old = os.getcwd()
        os.chdir(self.repo)
        self.addCleanup(os.chdir, old)

    def _git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.repo), "-c", "commit.gpgsign=false", *args],
            capture_output=True, text=True, check=True,
            env={**os.environ,
                 "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid",  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
                 "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"})  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo

    def _commit(self, name, lines):
        (self.repo / name).write_text("\n".join(lines) + "\n")
        self._git("add", "--", name)
        self._git("-c", "commit.gpgsign=false", "commit", "-q", "-m", "base")

    def _stage(self, name, lines):
        (self.repo / name).write_text("\n".join(lines) + "\n")
        self._git("add", "--", name)

    def _found(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), \
                contextlib.redirect_stderr(io.StringIO()):
            code = ls.main(["--staged", "--root", str(self.repo), "--json"])
        return code, [(f["path"], f["line"], f["rule"])
                      for f in json.loads(buf.getvalue())["findings"]]

    def test_a_leak_below_unchanged_lines_reports_its_file_line(self):
        base = ["a", "b", "c", "d"]
        self._commit("c.md", base)
        self._stage("c.md", base + [self.LEAK])
        self.assertEqual({"c.md": [(5, self.LEAK)]}, ls.staged_added_lines())
        self.assertEqual((1, [("c.md", 5, "private-key-header")]),
                         self._found())

    def test_findings_in_a_second_hunk_report_their_file_lines(self):
        base = [f"l{i}" for i in range(1, 31)]
        self._commit("two.md", base)
        # One leak on new line 5; 20 unchanged lines later (more than a
        # hunk's context, so git cuts a second hunk) another on line 26.
        new = base[:4] + [self.LEAK] + base[4:24] + [self.LEAK] + base[24:]
        self._stage("two.md", new)
        self.assertEqual((1, [("two.md", 5, "private-key-header"),
                              ("two.md", 26, "private-key-header")]),
                         self._found())

    def test_a_new_file_still_reports_from_line_one(self):
        self._stage("fresh.md", ["# title", self.LEAK])
        self.assertEqual((1, [("fresh.md", 2, "private-key-header")]),
                         self._found())


class LinkedWorktreeSkipped(unittest.TestCase):
    """020/160 (E9): `_walk_files` must prune a directory whose `.git` entry
    is a regular FILE (`gitdir: <path>`, the linked-worktree/submodule
    marker) — not just one literally named `.git` that is a directory.
    Before this fix a session's own gitignored `.claude/worktrees/<name>/`
    grew into a full second checkout of the tree that the walk descended
    into anyway, double-counting every finding. Measured in `faves`
    2026-08-15: `leakscan .` reported 101 findings and blocked a commit,
    every one already covered by `.leakscanignore` one layer up — the
    ignore file's root-relative globs cannot match inside the nested
    copy."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _found(self):
        return {str(p.relative_to(self.tmp))
                for p in ls._walk_files(self.tmp)}

    def test_linked_worktree_directory_is_pruned(self):
        self._write("real.txt", "content\n")
        self._write(".claude/worktrees/wt1/.git",
                    "gitdir: /elsewhere/.git/worktrees/wt1\n")
        self._write(".claude/worktrees/wt1/real.txt", "content\n")
        found = self._found()
        self.assertIn("real.txt", found)
        self.assertNotIn(".claude/worktrees/wt1/real.txt", found)
        self.assertNotIn(".claude/worktrees/wt1/.git", found)

    def test_independent_nested_repos_own_git_dir_still_pruned(self):
        """Unaffected by this fix: a nested repo whose `.git` is a
        DIRECTORY, not a linked worktree, was already excluded by the
        existing skip-dir-names rule matching the bare name `.git` at any
        depth inside it — this pins that it still holds."""
        self._write("nested/.git/objects/pack/dummy", "not real git data\n")
        self._write("nested/real.txt", "content\n")
        found = self._found()
        self.assertIn("nested/real.txt", found)
        self.assertNotIn("nested/.git/objects/pack/dummy", found)

    def test_ordinary_dotgit_file_is_treated_as_a_marker_too(self):
        """Deliberate, not a bug: the check is file-ness only, never
        content (see `_walk_files`'s comment) — a bare regular file
        literally named `.git` anywhere is treated as a worktree/submodule
        marker and prunes its parent, even holding no real `gitdir:` line
        as here. Accepted cost of the item's own stated minimum fix:
        nothing else legitimately creates a file with that exact name."""
        self._write("weird/.git", "not a real worktree marker\n")
        self._write("weird/real.txt", "content\n")
        found = self._found()
        self.assertNotIn("weird/real.txt", found)


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
        # the span vanishing from both. Since 115/090 the MAC also reports
        # (the residual the design note names): the span still BLOCKS as ipv6,
        # exactly as before.
        fs = ls.scan_text("t", "bssid aa:bb:cc:dd:ee:ff", [],
                          frozenset({"mac-address"}))
        self.assertEqual({"ipv6"}, blocking(fs))
        self.assertEqual({"mac-address"}, reporting(fs))

    def test_a_reporting_ipv6_is_shadowed_by_any_mac(self):
        # One span, one finding, among report-only rules too.
        for off in (frozenset({"ipv6"}), frozenset({"ipv6", "mac-address"})):
            fs = ls.scan_text("t", "bssid aa:bb:cc:dd:ee:ff", [], off)
            self.assertEqual(["mac-address"], [f.rule for f in fs], off)

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


class PhoneInsideHexDigest(unittest.TestCase):
    """Roadmap 320/470 — a digit run inside a 16+ character hex run is part of
    a digest, not a phone; a phone in prose keeps flagging."""

    SHA = ("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    # A digest whose interior holds a phone-shaped digit run between hex
    # letters, which the old lookarounds accepted.
    DIGEST = "9f86d081884c7d65" + "a031234567b" + "9a2ce5d1c6e4f0b3"

    def test_digit_run_inside_a_digest_is_not_a_phone(self):
        self.assertNotIn("nz-phone", rules(f'"sha256": "{self.DIGEST}"'))
        self.assertNotIn("nz-phone", rules(f"sha256 {self.DIGEST} done"))

    def test_the_old_behaviour_is_the_regression(self):
        # Without the guard the same line matched; pin that the shape does.
        m = [x for x in ls.STRUCTURAL if x.name == "nz-phone"][0]
        self.assertIsNotNone(m.regex.search(self.DIGEST))

    def test_real_digest_stays_clean(self):
        self.assertNotIn("nz-phone", rules(f"sha256 {self.SHA}"))

    def test_phone_in_prose_still_flags(self):
        self.assertIn("nz-phone", rules("ring 031234567 today"))
        self.assertIn("nz-phone", rules("ring 03 123 4567 today"))
        self.assertIn("nz-phone", rules("ring +64 21 555 1234 today"))

    def test_phone_beside_a_short_hex_word_still_flags(self):
        # `dead` / `beef` are hex words but nowhere near 16 characters.
        self.assertIn("nz-phone", rules("dead 031234567 beef"))
        self.assertIn("nz-phone", rules("id a031234567b is the line"))

    def test_spaced_phone_next_to_a_long_hex_run_still_flags(self):
        self.assertIn("nz-phone", rules(f"{self.SHA} 021 555 1234"))


class PhoneInsideBracketedByteField(unittest.TestCase):
    """Roadmap 320/850 — a device dump prints raw property bytes between angle
    brackets; an even-length run of hex digits and nothing else, wholly inside
    them, is a byte field and not a phone. A bracketed real-shaped number keeps
    flagging."""

    def _phone_matches(self, line):
        rx = [x for x in ls.STRUCTURAL if x.name == "nz-phone"][0].regex
        return rx.search(line) is not None

    def test_the_shape_matched_the_regex_before_the_guard(self):
        # Pin the regression: the bare regex hit these, so the guard is what
        # clears them.
        for line in ("<05000000>", "<031234567a>", "<091234567a>"):
            with self.subTest(line=line):
                self.assertTrue(self._phone_matches(line))

    def test_byte_fields_pass(self):
        for field in ("05000000", "0300000000000000", "091234567a",
                      "031234567a", "0400000000000000ffee"):
            with self.subTest(field=field):
                self.assertNotIn("nz-phone", rules(f"    \"IOCacheLine\" = <{field}>"))
                self.assertNotIn("nz-phone", rules(f"x = <{field}> y"))

    def test_byte_field_with_uppercase_hex_passes(self):
        self.assertNotIn("nz-phone", rules("v = <05000000AB00>"))

    def test_bracketed_real_shaped_numbers_still_flag(self):
        for text in ("<021 555 1234>", "<+64 21 555 1234>", "<09-555-1234>",
                     "<021-555-1234>", "<(04) 555 1234>"):
            with self.subTest(text=text):
                self.assertIn("nz-phone", rules(f"contact {text} today"))

    def test_bracketed_ten_digit_unseparated_mobile_still_flags(self):
        # Ten decimal digits is both a whole number of bytes and the one
        # unseparated NZ mobile length; it is kept as a phone.
        self.assertIn("nz-phone", rules("contact <0215551234> today"))

    def test_bracketed_odd_length_run_still_flags(self):
        # Nine digits is not whole bytes (a ten-digit run is the other case,
        # pinned above).
        self.assertIn("nz-phone", rules("contact <031234567> today"))

    def test_bracket_must_close_around_the_run(self):
        for line in ("ring <05000000 now", "ring 05000000> now",
                     "ring (05000000) now", "ring [05000000] now",
                     "ring <x05000000> now"):
            with self.subTest(line=line):
                self.assertIn("nz-phone", rules(line))

    def test_extra_text_inside_the_brackets_is_not_a_byte_field(self):
        self.assertIn("nz-phone", rules("ring <tel 05000000> now"))
        self.assertIn("nz-phone", rules("ring <05000000 05000000> now"))
        self.assertIn("nz-phone", rules("ring <05000000,> now"))

    def test_unbracketed_phones_unchanged(self):
        for line in ("ring 031234567 today", "ring 05000000 today",
                     "ring 0215551234 today"):
            with self.subTest(line=line):
                self.assertEqual(self._phone_matches(line),
                                 "nz-phone" in rules(line))


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
        # Since G3 the unread body blocks too (binary-unlisted); the name hit
        # is still reported on its own, at line 0.
        self.assertEqual(["ipv4"], [f.rule for f in fs if f.kind != "binary"])
        self.assertEqual(["binary-unlisted"], [f.rule for f in fs if f.kind == "binary"])


class MalformedScopedMarkers(unittest.TestCase):
    """160/480 AM2 and 160/110 LK1 (the same finding): a scoped marker with a
    broken scope used to back off to the unscoped form and exempt EVERY
    structural rule on its line, including a second leak the author never
    named. Mike, 2026-11-09: "Strict, with a warning period". The term list was
    never reachable by an unscoped marker (D1) and still is not."""

    # A line carrying two structural leaks, so a marker that exempts too much
    # is visible: an IPv4 address and an email.
    LEAK = "host 172.16.31.7 mail a.b@example.com  "
    SHAPES = {
        "scope with no reason": "# leakscan:allow:ipv4:",
        "scope with a blank reason": "# leakscan:allow:ipv4: ",
        "space inside a composed scope": "# leakscan:allow:email, ipv4: why",
        "trailing comma": "# leakscan:allow:ipv4,: why",
    }

    def run_at(self, day, text):
        with unittest.mock.patch.object(allowmarker, "_utc_today", return_value=day), \
                unittest.mock.patch.object(allowmarker, "_WARNED", set()), \
                contextlib.redirect_stderr(io.StringIO()) as err:
            return rules(text), err.getvalue()

    def test_after_the_grace_both_leaks_still_report(self):
        for name, marker in self.SHAPES.items():
            with self.subTest(shape=name):
                found, _ = self.run_at(allowmarker.MALFORMED_GRACE_UNTIL, self.LEAK + marker)
                self.assertEqual({"ipv4", "email"}, found)

    def test_during_the_grace_it_still_exempts_and_says_so(self):
        for name, marker in self.SHAPES.items():
            with self.subTest(shape=name):
                found, err = self.run_at(datetime.date(2026, 11, 9), self.LEAK + marker)
                self.assertEqual(set(), found)
                self.assertIn("malformed allow-marker", err)
                self.assertIn("2026-12-09", err)

    def test_a_well_formed_scoped_marker_is_untouched_on_both_sides(self):
        text = self.LEAK + "# leakscan:allow:ipv4: documentation address"
        for day in (datetime.date(2026, 11, 9), allowmarker.MALFORMED_GRACE_UNTIL):
            found, err = self.run_at(day, text)
            self.assertEqual({"email"}, found)
            self.assertEqual("", err)

    def test_a_broken_marker_never_reached_the_term_list(self):
        terms = [("Acme", re.compile(r"\bAcme\b", re.IGNORECASE))]
        for day in (datetime.date(2026, 11, 9), allowmarker.MALFORMED_GRACE_UNTIL):
            found, _ = self.run_at(day, "Acme 172.16.31.7  # leakscan:allow:ipv4:", )
            self.assertNotIn("local-term", found)      # the helper passes no terms
            with unittest.mock.patch.object(allowmarker, "_utc_today", return_value=day), \
                    contextlib.redirect_stderr(io.StringIO()):
                self.assertIn("local-term",
                              rules("Acme 172.16.31.7  # leakscan:allow:ipv4:", terms))


class TermNormalisation(unittest.TestCase):
    """160/110 LK2: a macron is one code point or a letter plus a combining
    mark. The two print the same, and a term typed one way must catch text
    typed the other. Constructed from code points so this file carries no
    decomposed text of its own."""

    NFC = "M\u0101ori"
    NFD = "Ma\u0304ori"

    def terms(self, spelling, prefix=""):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "terms.txt"
            f.write_text(prefix + spelling + "\n", encoding="utf-8")
            terms, warning = ls.load_local_terms(f)
        self.assertIsNone(warning)
        return terms

    def test_a_composed_term_catches_decomposed_text_and_back(self):
        for term_spelling, text_spelling in ((self.NFC, self.NFD), (self.NFD, self.NFC),
                                             (self.NFC, self.NFC), (self.NFD, self.NFD)):
            with self.subTest(term=ascii(term_spelling), text=ascii(text_spelling)):
                self.assertIn("local-term",
                              rules(f"see {text_spelling} here", self.terms(term_spelling)))

    def test_forms_terms_are_normalised_too(self):
        for text in (self.NFC, self.NFD):
            self.assertIn("local-term", rules(f"a {text.lower()} b",
                                              self.terms(self.NFD, prefix="forms:")))

    def test_a_regex_term_still_matches_what_it_matched_before(self):
        # Verbatim, as ever; plus the line is also tried in NFC, so a pattern
        # typed in the composed form now catches decomposed text.
        composed = [("x", re.compile(self.NFC, re.IGNORECASE))]
        self.assertIn("local-term", rules(f"see {self.NFC} here", composed))
        self.assertIn("local-term", rules(f"see {self.NFD} here", composed))
        decomposed = [("x", re.compile(self.NFD, re.IGNORECASE))]
        self.assertIn("local-term", rules(f"see {self.NFD} here", decomposed))

    def test_ascii_lines_are_returned_untouched(self):
        s = "plain ascii"
        self.assertIs(s, ls._nfc(s))
        self.assertNotIn("local-term", rules("nothing here", self.terms(self.NFC)))


class DerivedFormSeparators(unittest.TestCase):
    """160/110 LK3: a name spread across path components or tagged into an
    email local part evaded even a `forms:` term. The path plane reads
    slash-delimited paths, where `/` between name parts is the usual shape."""

    def forms(self, term):
        return [(term, ls.derived_form_regex(term))]

    def test_slash_and_plus_join_the_words(self):
        for text in ("jane/q/public.md", "docs/jane+q+public", "jane/q.public",
                     "jane-q-public", "jane_q_public"):
            with self.subTest(text=text):
                self.assertIn("local-term", rules(f"see {text} today", self.forms("Jane Q Public")))

    def test_the_path_plane_catches_a_name_split_across_directories(self):
        fs = ls.scan_path_name("people/jane/q/public/notes.md", self.forms("Jane Q Public"))
        self.assertEqual(["local-term"], [f.rule for f in fs])

    def test_boundaries_and_missing_words_still_hold(self):
        self.assertNotIn("local-term", rules("jane/public here", self.forms("Jane Q Public")))
        self.assertNotIn("local-term", rules("a Bartender shift", self.forms("Bart")))


class PathPlaneHonoursNoMarkers(unittest.TestCase):
    """160/110 LK6: the code's docstring and the E7 record say a path has no
    inline marker hatch, but `scan_path_name` reused `scan_text`, so a filename
    that spelt a marker and a reason exempted its own findings."""

    def test_a_filename_that_spells_a_marker_does_not_exempt_itself(self):
        name = "notes/a.b@example.com leakscan:allow: fixture.md"
        self.assertEqual(["email"], [f.rule for f in ls.scan_path_name(name, [])])
        # ... and the same text in a file body still does exempt (the hatch).
        self.assertEqual([], scan("a.b@example.com leakscan:allow: fixture"))

    def test_a_path_matching_a_term_is_not_exempted_by_a_scoped_marker(self):
        terms = [("Acme", re.compile(r"\bAcme\b", re.IGNORECASE))]
        fs = ls.scan_path_name("Acme leakscan:allow:local-term: x.md", terms)
        self.assertEqual(["local-term"], [f.rule for f in fs])


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


class BoundedMemory(unittest.TestCase):
    """020/380 — the same class of defect `020/370` fixed in `secretscan`,
    applied here: peak memory must be bounded by a constant that does not
    grow with the size of the input. Mike's ruling, verbatim: "it should not
    matter how much it scans it should no have this affect."

    Runs the real CLI as a SUBPROCESS via `memprobe.run_and_measure` and
    reads its peak RSS back from the kernel — `tracemalloc` only sees the
    Python heap, not the whole OS process (see `tools/memprobe.py`'s module
    docstring).

    Content is plain filler prose with no leak-shaped substring anywhere
    (no email, no IP, no PII-keyed line), so every run produces zero
    findings — the only thing that differs between a small and a large run
    is how many bytes there are to read."""

    LEAKSCAN = str(TOOLS_DIR / "leakscan.py")
    SMALL_BYTES = 1 * 1024 * 1024
    LARGE_BYTES = 8 * 1024 * 1024
    # Grounded in the FIX's design, not fitted to a measurement
    # (`ground-numeric-limits`): the one piece of per-file state the
    # streaming reader ever buffers is a single window of one physical
    # line, capped at `LINE_WINDOW_BYTES + LINE_WINDOW_OVERLAP` (~4.06 MiB)
    # — see `leakscan._iter_numbered_lines`. Both runs produce zero
    # findings (so `Tally.take_finding_slot`'s cap machinery is inert
    # here too) — growth between them should be close to zero. Allowing 4x
    # that window leaves generous headroom for interpreter/allocator noise
    # while staying far below what a whole-file-buffered implementation
    # shows for this size delta (the pre-fix code measured well over 2x
    # this bound while building the fix — recorded for context, not what
    # set the number).
    GROWTH_BOUND_BYTES = 4 * (ls.LINE_WINDOW_BYTES + ls.LINE_WINDOW_OVERLAP)

    # A present-but-empty terms file keeps the run off any real machine-local
    # term list, so only the structural engine (the thing under test) runs.
    @classmethod
    def setUpClass(cls):
        cls._terms_dir = Path(tempfile.mkdtemp())
        cls.terms_path = cls._terms_dir / "terms.txt"
        cls.terms_path.write_text("")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls._terms_dir, ignore_errors=True)

    @staticmethod
    def _build(target_bytes: int, path: Path) -> None:
        with open(path, "w") as f:
            written = 0
            i = 0
            while written < target_bytes:
                line = f"this is filler line number {i} — no leak-shaped content here at all\n"
                f.write(line)
                written += len(line)
                i += 1

    def _peak_rss_for(self, size_bytes: int) -> int:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        self._build(size_bytes, tmp / "data.txt")
        # Safety: a hard kill well short of the 1 GB line 020/370's own
        # incident treats as not to cross, and a 60s ceiling so a
        # regression that reintroduces catastrophic behaviour fails the
        # test instead of hanging CI.
        result = memprobe.run_and_measure(
            [sys.executable, self.LEAKSCAN, "--root", str(tmp), str(tmp),
             "--terms", str(self.terms_path)],
            timeout=60, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        self.assertEqual(0, result.returncode,
                         "filler content must not itself flag anything")
        return result.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_input_size(self):
        small_peak = self._peak_rss_for(self.SMALL_BYTES)
        large_peak = self._peak_rss_for(self.LARGE_BYTES)
        growth = large_peak - small_peak
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for a "
            f"{(self.LARGE_BYTES - self.SMALL_BYTES) / 1e6:.1f} MB larger input "
            f"(small={small_peak / 1e6:.1f} MB, large={large_peak / 1e6:.1f} MB) "
            "— memory is scaling with input size again (020/380).")


class ReaderLinear(unittest.TestCase):
    """110/140 — `_iter_numbered_lines` walks an offset instead of re-slicing
    the remaining buffer for every line. Two checks, neither timed (FW11):
    the new reader yields exactly what the old one did across chunk and
    window boundaries, and the characters it copies stay linear in the input.
    """

    @staticmethod
    def _old_reader(path):
        """The pre-110/140 loop, kept here as the oracle."""
        import codecs
        decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
        lineno = 1
        pending = ""
        with open(path, "rb") as fh:
            first_chunk = True
            while True:
                chunk = fh.read(ls.READ_CHUNK_BYTES)
                if first_chunk:
                    first_chunk = False
                    if ls._looks_binary(chunk):
                        return
                if not chunk:
                    break
                pending += decoder.decode(chunk)
                while True:
                    nl = pending.find("\n")
                    if nl == -1:
                        break
                    yield lineno, pending[:nl], True
                    pending = pending[nl + 1:]
                    lineno += 1
                if len(pending) >= ls.LINE_WINDOW_BYTES:
                    yield lineno, pending, False
                    pending = pending[-ls.LINE_WINDOW_OVERLAP:]
            pending += decoder.decode(b"", final=True)
            if pending:
                yield lineno, pending, True

    def _write(self, data: bytes) -> Path:
        d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d, True)
        p = d / "f.txt"
        p.write_bytes(data)
        return p

    def _small_windows(self):
        from unittest import mock
        for name, value in (("READ_CHUNK_BYTES", 64),
                            ("LINE_WINDOW_BYTES", 300),
                            ("LINE_WINDOW_OVERLAP", 20)):
            patcher = mock.patch.object(ls, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_new_reader_matches_old_across_boundaries(self):
        self._small_windows()
        cases = {
            "short lines": b"".join(b"line %d\n" % i for i in range(400)),
            "blank and crlf": b"\n\n\r\nabc\r\n\n" * 40,
            "no trailing newline": b"a\nbb\nccc",
            "only newlines": b"\n" * 200,
            "multibyte on edges": ("h\u00e9llo w\u00f6rld \u00fc\n" * 120).encode(),
            "invalid utf8": (b"ok\n\xff\xfe bad\n" * 80),
            "overlong then short": b"x" * 1000 + b"\n" + b"tail\n" * 50,
            "short then overlong": b"head\n" * 50 + b"y" * 1000,
            "chunk-sized lines": (b"z" * 63 + b"\n") * 30,
            "window-sized line": b"w" * 299 + b"\n" + b"w" * 300 + b"\n",
            "empty": b"",
        }
        for name, data in cases.items():
            with self.subTest(name):
                p = self._write(data)
                self.assertEqual(list(ls._iter_numbered_lines(p)),
                                 list(self._old_reader(p)))

    @staticmethod
    def _counting_decoder(counter, real_factory):

        class CountingStr(str):
            def __getitem__(self, key):
                out = str.__getitem__(self, key)
                if isinstance(key, slice):
                    counter[0] += len(out)
                    return CountingStr(out)
                return out

            def __add__(self, other):
                return CountingStr(str.__add__(self, other))

            def __radd__(self, other):
                return CountingStr(str.__add__(other, self))

        inner = real_factory("utf-8")(errors="replace")

        class Decoder:
            def decode(self, data, final=False):
                return CountingStr(inner.decode(data, final))
        return Decoder()

    def _copied(self, reader, path):
        import codecs as codecs_module
        from unittest import mock
        counter = [0]
        real = codecs_module.getincrementaldecoder
        with mock.patch.object(ls.codecs, "getincrementaldecoder",
                               lambda *a, **k: (lambda **kw: self._counting_decoder(counter, real))):
            n = sum(1 for _ in reader(path))
        return n, counter[0]

    def test_characters_copied_are_linear_in_the_input(self):
        # Many short lines per chunk is the shape that was quadratic. Count
        # the characters the reader slices instead of timing it.
        data = b"0123456789abcdef\n" * 20000          # 340 KB, 20k lines
        p = self._write(data)
        n, copied = self._copied(ls._iter_numbered_lines, p)
        self.assertEqual(n, 20000)
        self.assertLessEqual(copied, 3 * len(data),
                             f"reader sliced {copied} characters for "
                             f"{len(data)} of input: not linear (110/140)")
        # The oracle must fail the same bound, or the check proves nothing.
        _, old_copied = self._copied(self._old_reader, p)
        self.assertGreater(old_copied, 10 * len(data))


class GatesAreNecessary(unittest.TestCase):
    """110/130 (lever 4) — each per-rule pre-filter in `ls.GATES` is a cheap
    test that must be NECESSARY for its rule: if the rule's regex matches a
    line, the gate must pass that line. A gate that rejects a line its rule
    would match is a silent false negative in a boundary scanner, so this is
    proven three ways — gate-vs-regex on a corpus that exercises every gated
    rule, gated scan vs the same scan with every gate removed, and the
    structural facts the gates rest on. Every value is synthetic."""

    POSITIVES = (
        "-----BEGIN RSA PRIVATE KEY-----", "key AKIAABCDEFGHIJKLMNOP here",
        "tok eyJhbGciOiJI.eyJzdWIiOiIx.abcdefghij", "mail jane.doe@example.org now",
        "dob = 1984-02-29", "passport_number:\t'AB123456'", "birthDate:1984-02-29",
        "card 4111111111111111 on file", "4111-1111-1111-1111",
        "iban GB82WEST12345698765432 x", "mac aa:bb:cc:dd:ee:ff end",
        "AA-BB-CC-DD-EE-FF", "gateway 172.16.31.7 is the igw",
        "uplink fd00:1234:5678::abcd up", "2001:db8:0:0:0:0:0:1",
        "acct 12-3456-1234567-00 ok", "call 021 123 4567", "(04) 123 4567",
        "+6421 123 4567", "at 12 Cuba Street", "5 Oak Tce", "7a Kent Terrace",
        "loc -41.2865, 174.7762 pin", "ird 123-456-789 x",
        "medication: Foobarol", "home_address = 5-Main-Rd",
        "diagnosis: Foobaritis", "Diagnoses = 'Foo-bar'",
    )
    NOISE = (
        "d", "-", ":", "::", "=", " = ", ": ", "\"", "'", " ", "\t", ".", ",",
        "x", "key ", "1", "12", "123", "1234", "192.0.2.10", "255.255.255.0",
        "a::b", "1:2:3:4", "the", "Street", "Hill", "St", "@", "AKIA", ".eyJ",
        "PRIVATE KEY-----", "leakscan:allow: r", "leakscan:allow:ipv6: r",
        "leakscan:allow:email,mac-address: r", "leakscan:allow",
        "K", "ſ", "İ", "é",
    )

    @classmethod
    def lines(cls, n=6000):
        import random
        rng = random.Random(130)
        out = list(cls.POSITIVES) + list(cls.NOISE)
        alphabet = "abcxyzAKIZ0123456789:-.,@=_ '\"`;\t/+()[]{}"
        for _ in range(n):
            parts = [rng.choice(cls.NOISE) for _ in range(rng.randint(0, 3))]
            p = rng.choice(cls.POSITIVES)
            if rng.random() < .5 and p:           # a near miss: break one char
                i = rng.randrange(len(p))
                p = p[:i] + rng.choice((alphabet[rng.randrange(len(alphabet))], "")) + p[i + 1:]
            parts.insert(rng.randint(0, len(parts)), p)
            out.append("".join(parts))
        return out

    def test_every_gate_names_a_real_rule(self):
        # A typo'd name would be a rule silently running ungated forever.
        self.assertLessEqual(set(ls.GATES), {p.name for p in ls.ALL_RULES})

    def test_a_rule_that_matches_always_passes_its_gate(self):
        exercised = set()
        for line in self.lines():
            for pat in ls.ALL_RULES:
                gate = ls.GATES.get(pat.name)
                if gate is None or not pat.regex.search(line):
                    continue
                exercised.add(pat.name)
                self.assertTrue(gate(line),
                                f"gate for {pat.name} rejects a line it matches: {line!r}")
        # The corpus must reach every gated rule, or the check is vacuous.
        self.assertEqual(exercised, set(ls.GATES))

    def test_gated_scan_equals_ungated_scan(self):
        from unittest import mock
        import dataclasses
        lines = list(enumerate(self.lines(3000), start=1))
        for disabled in (frozenset(), frozenset({"ipv6"}), frozenset({"mac-address"}),
                         frozenset({"ipv6", "mac-address"}), frozenset({"ipv4", "email"})):
            t_gated = ls.Tally(disabled_rules=tuple(sorted(disabled)))
            gated = ls.scan_lines("p", lines, [], disabled, t_gated)
            # One home for the table (GT3): patching GATES and the memo is
            # enough, `_shadow_spans` and the scan loop both read it.
            with mock.patch.object(ls, "GATES", {}), \
                    mock.patch.object(ls, "_ACTIVE_CACHE", {}):
                t_plain = ls.Tally(disabled_rules=tuple(sorted(disabled)))
                plain = ls.scan_lines("p", lines, [], disabled, t_plain)
            self.assertTrue(plain, "the corpus must produce findings")
            self.assertEqual([dataclasses.asdict(f) for f in gated],
                             [dataclasses.asdict(f) for f in plain], disabled)
            self.assertEqual(t_gated.by_marker, t_plain.by_marker, disabled)

    def test_the_marker_regex_needs_the_marker_literal(self):
        # The `ALLOW_MARKER in line` guard in scan_lines rests on this: the
        # compiled marker pattern cannot match a line without the literal.
        for line in self.lines(2000):
            if ls.ALLOW_RX.search(line):
                self.assertIn(ls.ALLOW_MARKER, line)
        self.assertIsNotNone(ls.ALLOW_RX.search("x leakscan:allow: reason"))

    def test_the_key_context_gate_names_no_key(self):
        # Vocabulary-free by design: a key added to PII_KEY_RX tomorrow needs
        # no edit to the gate. Pin it with every canary shape the suite holds.
        for _label, line in PII_CANARIES:
            self.assertTrue(ls.GATES["pii-key-context"](line), line)

    def test_gates_hold_over_a_corpus_generated_from_the_regexes(self):
        """GT2 (160/720): the hand-kept corpus above covers a rule per RULE.
        This one is built from each gated rule's own regex, one line per
        alternative of every alternation, so a branch added to a rule under
        the same name is exercised the day it is added."""
        for pat in ls.ALL_RULES:
            gate = ls.GATES.get(pat.name)
            if gate is None:
                continue
            with self.subTest(pat.name):
                rx = getattr(pat.regex, "original", pat.regex)
                matched = [t for t in rxsupport.samples(rx) if rx.search(t)]
                self.assertTrue(matched, f"no sample of {pat.name} matches it: "
                                "extend test_support_regex or add a POSITIVE")
                for line in matched:
                    self.assertTrue(gate(line),
                                    f"gate for {pat.name} rejects {line!r}")

    def test_every_top_level_alternative_of_a_gated_rule_passes_its_gate(self):
        for pat in ls.ALL_RULES:
            gate = ls.GATES.get(pat.name)
            rx = getattr(pat.regex, "original", pat.regex)
            if gate is None:
                continue
            branches = rxsupport.top_level_branches(rx.pattern)
            if len(branches) < 2:
                continue
            for src in branches:
                brx = re.compile(src, rx.flags)
                got = [t for t in rxsupport.samples(brx) if brx.search(t)]
                with self.subTest(rule=pat.name, branch=src):
                    self.assertTrue(got)
                    self.assertTrue(all(gate(t) for t in got))

    # A rule that is case-insensitive needs a gate that is too. Only these two
    # are, and each gate is flag-aware for a stated reason.
    FLAG_AWARE_GATES = {
        "pii-key-context": "the gate tests the letter-free tail `[:=]\\s*...`",
        "diagnosis-key": "the gate's own regex carries (?i)",
    }

    def test_no_gated_rule_is_case_insensitive_unless_its_gate_is_flag_aware(self):
        """GT2 (b): the premise 'no rule carries (?i)' was a comment. A
        case-insensitive rule paired with a case-sensitive literal gate would
        reject every line differing only in case."""
        for pat in ls.ALL_RULES:
            rx = getattr(pat.regex, "original", pat.regex)
            if pat.gate is not None and rx.flags & re.IGNORECASE:
                self.assertIn(pat.name, self.FLAG_AWARE_GATES,
                              f"{pat.name} is case-insensitive with a gate not "
                              "declared flag-aware")
        for name in self.FLAG_AWARE_GATES:
            rx = getattr(ls.BY_NAME[name].regex, "original", ls.BY_NAME[name].regex)
            self.assertTrue(rx.flags & re.IGNORECASE, f"{name}: stale entry")

    def test_the_gate_is_declared_on_the_rule_and_the_table_is_derived(self):
        """GT3: one home. `GATES` is the rules' own gates, and the scan loop
        and the shadow spans both read it."""
        self.assertEqual(ls.GATES, {p.name: p.gate for p in ls.ALL_RULES
                                    if p.gate is not None})
        self.assertFalse(hasattr(ls, "_GATED"))
        from unittest import mock
        marker = lambda ln: False   # noqa: E731
        with mock.patch.object(ls, "GATES", {**ls.GATES, "mac-address": marker}), \
                mock.patch.object(ls, "_ACTIVE_CACHE", {}):
            active = {p.name: g for p, g, _b in ls._active_rules(frozenset())}
            self.assertIs(marker, active["mac-address"])
            # ipv6 is shadowed by mac-address; with the shadower's gate failing
            # it casts no span, and the same patched table decides that.
            self.assertEqual({}, ls._shadow_spans("aa:bb:cc:dd:ee:ff", frozenset()))

    def test_gates_leave_the_term_list_alone(self):
        # The gates guard STRUCTURAL rules only; a line no gate passes still
        # reaches the machine-local terms (D1).
        term = ("zzzterm", re.compile(r"\bzzzterm\b", re.IGNORECASE))
        fs = ls.scan_text("t", "plain words and zzzterm", [term])
        self.assertEqual([f.rule for f in fs], ["local-term"])


class StagedPositionalScope(unittest.TestCase):
    """115/360 — a staged positional is a repo-relative scope, and its
    spelling must not decide whether the scan runs. A bare `.` became the
    prefix `./`, matched no git path, emptied the set and printed clean over a
    planted finding. `.` now means no restriction, `./docs` means `docs`, and
    a path leaving the repo is refused. A scope that merely excludes every
    staged file is NOT refused: the hook plane passes the check's declared
    scope, and a commit touching only files outside it is a legitimate pass.
    Since 160/950 git decides what a positional names, so a spelling git does
    not know (a typo, the wrong case) is refused, never read as clean.
    """

    # Assembled so this file does not itself carry the shape it plants.
    BAD = "-----BEGIN " + "RSA PRIVATE KEY-----"

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo, ignore_errors=True)
        subprocess.run(["git", "-C", str(self.repo), "init", "-q"], check=True)
        empty = self.repo / "no-terms.txt"      # untracked; never staged
        empty.write_text("")
        env = unittest.mock.patch.dict(
            os.environ, {"ATELIER_LEAKSCAN_TERMS": str(empty)})
        env.start()
        self.addCleanup(env.stop)
        old = os.getcwd()
        os.chdir(self.repo)
        self.addCleanup(os.chdir, old)
        for d in ("docs", "src", "src-extra", "caf\u00e9"):
            (self.repo / d).mkdir()
        (self.repo / "src" / "keep.txt").write_text("kept\n")
        # `src` is tracked with nothing staged under it; `src-extra` shares
        # its name prefix and holds the planted finding (160/950 QS4/QU1).
        self._git("add", "--", "src/keep.txt")
        self._git("commit", "-q", "-m", "seed")
        (self.repo / "docs" / "a.txt").write_text(self.BAD + "\n")
        (self.repo / "src-extra" / "b.txt").write_text(self.BAD + "\n")
        (self.repo / "caf\u00e9" / "c.txt").write_text(self.BAD + "\n")
        self._git("add", "--", "docs/a.txt", "src-extra/b.txt", "caf\u00e9/c.txt")

    def _git(self, *args):
        # Host-independent: a fixture commit must not inherit the host's
        # signing or identity config (160/950 QS9).
        subprocess.run(
            ["git", "-C", str(self.repo), "-c", "user.name=t",
             "-c", "user.email=t",
             "-c", "commit.gpgsign=false", *args],
            check=True, capture_output=True)

    def _main(self, *paths):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = ls.main(["--staged", "--root", str(self.repo), *paths])
        return code, err.getvalue()

    def test_bare_dot_scans_the_staged_set(self):
        self.assertEqual(1, self._main(".")[0])
        self.assertEqual(1, self._main("./")[0])

    def test_dot_slash_prefix_means_the_same_path_without_it(self):
        self.assertEqual(1, self._main("./docs")[0])
        self.assertEqual(1, self._main("./docs/")[0])
        self.assertEqual(1, self._main("docs//")[0])
        self.assertEqual(1, self._main("docs")[0])

    def test_no_positional_still_scans(self):
        self.assertEqual(1, self._main()[0])

    def test_a_path_leaving_the_repo_is_refused(self):
        for p in ("..", "../x", "./../x", "docs/../../x"):
            with self.subTest(p=p):
                code, err = self._main(p)
                self.assertEqual(2, code, "an environment error, not a pass")
                self.assertIn("climb out of the repo", err)

    def test_prefix_boundary_is_a_directory_not_a_name_prefix(self):
        """`src` is the `src/` subtree, not every path starting `src`: the
        planted finding sits in `src-extra/` and a `src` scope must not reach
        it, while `src-extra` must (160/950 QS4)."""
        self.assertEqual(0, self._main("src")[0])
        self.assertEqual(1, self._main("src-extra")[0])
        self.assertEqual(1, self._main("src", "src-extra")[0])

    def test_an_exact_file_positional_is_that_file(self):
        """The file/directory distinction each guard copy must pin (QU1)."""
        self.assertEqual(1, self._main("docs/a.txt")[0])
        self.assertEqual(1, self._main("./docs/a.txt")[0])
        self.assertEqual(0, self._main("src/keep.txt")[0])

    def test_a_scope_with_nothing_staged_under_it_is_not_refused(self):
        """The hook plane's shape: a tracked directory this commit does not
        touch. Filtering to nothing here is scope, not spelling."""
        self.assertEqual(0, self._main("src")[0])
        self.assertEqual(0, self._main("./src")[0])

    def test_a_positional_git_does_not_know_is_refused(self):
        """160/950 QS1/QS2: a typo, a literal glob, an unexpanded `~`, or a
        spelling that differs from git's by CASE names no path git lists. It
        used to filter the set to nothing and exit 0 over a planted finding."""
        for p in ("no-such-dir", "docs/*", "~/docs", "Docs", "DOCS/a.txt",
                  "Docs/a.txt", "docs/A.txt"):
            with self.subTest(p=p):
                code, err = self._main(p)
                self.assertEqual(2, code, "an environment error, not a pass")
                self.assertIn("name nothing git knows", err)

    def test_one_unknown_positional_refuses_even_beside_a_known_one(self):
        code, err = self._main("docs", "Docs")
        self.assertEqual(2, code)
        self.assertIn("Docs", err)

    def test_a_unicode_variant_spelling_never_reads_clean(self):
        """160/950 QS1: the filesystem forgives a decomposed (NFD) spelling of
        the NFC directory git stores. Git resolves it (macOS precomposes) or
        the positional is refused; exit 0 over the planted finding is the bug."""
        nfd = unicodedata.normalize("NFD", "caf\u00e9")
        self.assertNotEqual(nfd, "caf\u00e9")
        for spelling in (nfd, nfd + "/c.txt"):
            with self.subTest(spelling=spelling):
                code, _err = self._main(spelling)
                self.assertIn(code, (1, 2))
        self.assertEqual(1, self._main("caf\u00e9")[0])

    def test_the_cwd_repo_must_be_the_root_repo(self):
        """160/950 QS3: the staged diff is the cwd repo's. A cwd in another
        repo with `--root` here read the wrong index and printed clean."""
        other = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, other, ignore_errors=True)
        subprocess.run(["git", "-C", str(other), "init", "-q"], check=True)
        os.chdir(other)
        for paths in ((), ("docs",)):
            with self.subTest(paths=paths):
                code, err = self._main(*paths)
                self.assertEqual(2, code, "an environment error, not a pass")
                self.assertIn("not the repo --root names", err)

    def test_a_subdirectory_cwd_reads_the_same_scope(self):
        """Positionals are repo-root-relative whatever the cwd (QS3)."""
        os.chdir(self.repo / "docs")
        self.assertEqual(1, self._main("docs")[0])
        self.assertEqual(1, self._main("docs/a.txt")[0])
        self.assertEqual(1, self._main(".")[0])
        code, err = self._main("a.txt")      # cwd-relative: not git's spelling
        self.assertEqual(2, code)
        self.assertIn("name nothing git knows", err)




# ===========================================================================
# G3 — binary media (Mike ruled BLOCKING 2026-08-04, funded 2026-08-09).
# Every fixture image is built here from bytes; every digest is computed at
# run time, so no literal hash sits in the file for secretscan to weigh.
# ===========================================================================
import hashlib as _hashlib  # noqa: E402
import struct as _struct  # noqa: E402
import subprocess as _subprocess  # noqa: E402
import zlib as _zlib  # noqa: E402
import datetime as _dt  # noqa: E402

# The G3 adoption grace ends on `BINARY_GRACE_UNTIL`. Gate tests that pin the
# BUILT behaviour run on that day (blocking); grace tests pick their own day.
_CUTOFF = ls.BINARY_GRACE_UNTIL
_BEFORE = _CUTOFF - _dt.timedelta(days=1)


@contextlib.contextmanager
def _chdir(path):
    """`contextlib.chdir` is 3.11+; the suite runs on the 3.9 a stock macOS
    carries too (160/950 QS9)."""
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)


def _on(day):
    """Run as if the UTC date were `day` — the only way to move the grace."""
    return unittest.mock.patch.object(ls, "_utc_today", return_value=day)


def _chunk(ctype, data):
    return (_struct.pack(">I", len(data)) + ctype + data
            + _struct.pack(">I", _zlib.crc32(ctype + data)))


def _png(*chunks):
    return (b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", bytes(13))
            + b"".join(_chunk(t, d) for t, d in chunks) + _chunk(b"IEND", b""))


def _jpeg(*segments):
    body = b"".join(b"\xff" + bytes([m]) + _struct.pack(">H", len(d) + 2) + d
                    for m, d in segments)
    return b"\xff\xd8" + body + b"\xff\xda\x00\x02" + b"\x00" * 8 + b"\xff\xd9"


def _webp(*chunks):
    body = b"WEBP" + b"".join(c + _struct.pack("<I", len(d)) + d + (b"\x00" if len(d) % 2 else b"")
                              for c, d in chunks)
    return b"RIFF" + _struct.pack("<I", len(body)) + body


_STUB_RX = re.compile(r"  # by=\S+ session=\S+ on=\d{4}-\d{2}-\d{2}$")


def _bare(text):
    """A `--binary-entries` listing without the who/when stub each line carries
    (160/980 GM5), for the tests that are about WHICH lines print."""
    return "\n".join(_STUB_RX.sub("", ln) for ln in text.splitlines())


def _sha(data, n=16):
    return _hashlib.sha256(data).hexdigest()[:n]


class _TreeCase(unittest.TestCase):
    def setUp(self):
        # Pinned to the day before the type-level cut-off (020/450), so a
        # fixture that keeps a whole set (`exif`) stays accepted whatever day
        # the suite runs; tests that care about the day patch it themselves.
        pin = _on(ls.TYPE_LEVEL_UNTIL - _dt.timedelta(days=1))
        pin.start()
        self.addCleanup(pin.stop)
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.terms = self.tmp.parent / f"{self.tmp.name}-terms.txt"
        self.terms.write_text("")
        self.addCleanup(self.terms.unlink)

    def put(self, rel, data):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(data, bytes):
            p.write_bytes(data)
        else:
            p.write_text(data)
        return data

    def manifest(self, text):
        self.put(ls.BINARY_MANIFEST, text)

    def scan(self, tally=None, paths=None):
        return ls.scan_paths(paths or [self.tmp], self.tmp, [], frozenset(), tally)

    def rules(self, **kw):
        return sorted(f.rule for f in self.scan(**kw))


class BinaryGate(_TreeCase):
    """The ruling's core: an unread binary BLOCKS until a reasoned, hash-bound
    entry accepts these exact bytes — and only these."""

    BLOB = b"\x00\x01\x02 opaque body"

    def test_an_unlisted_binary_blocks(self):
        self.put("assets/blob.bin", self.BLOB)
        fs = self.scan()
        self.assertEqual(["binary-unlisted"], [f.rule for f in fs])
        self.assertEqual(("assets/blob.bin", 0, "binary"), (fs[0].path, fs[0].line, fs[0].where))

    def test_a_listed_binary_with_matching_hash_passes_and_is_counted(self):
        self.put("assets/blob.bin", self.BLOB)
        self.manifest(f"# fixture body, reviewed\n{_sha(self.BLOB)}  assets/blob.bin\n")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual(1, tally.binaries_by_manifest)
        self.assertIn(f"1 binary file(s) by {ls.BINARY_MANIFEST}", tally.summary())

    def test_full_digest_and_sha256sum_binary_mode_both_parse(self):
        self.put("a.bin", self.BLOB)
        self.manifest(f"{_sha(self.BLOB, 64)} *a.bin  # reviewed fixture\n")
        self.assertEqual([], self.scan())

    def test_a_changed_binary_blocks_again(self):
        self.put("a.bin", self.BLOB)
        self.manifest(f"{_sha(self.BLOB)}  a.bin  # reviewed fixture\n")
        self.put("a.bin", self.BLOB + b" edited")
        fs = self.scan()
        self.assertEqual(["binary-changed"], [f.rule for f in fs])
        self.assertIn("line 1", fs[0].excerpt)

    def test_a_reasonless_entry_is_a_config_error(self):
        self.put("a.bin", self.BLOB)
        self.manifest(f"{_sha(self.BLOB)}  a.bin\n")
        with self.assertRaises(ls.BinaryManifestError) as cm:
            self.scan()
        self.assertIn("no stated reason", str(cm.exception))
        rc = ls.main(["--root", str(self.tmp), str(self.tmp), "--terms", str(self.terms)])
        self.assertEqual(2, rc)

    def test_malformed_entries_are_config_errors_reported_together(self):
        self.manifest("# reasons for all\n"
                      "abc123  short-digest.bin\n"
                      f"{_sha(self.BLOB)}:everything  a.bin\n"
                      f"{_sha(self.BLOB)}  b.bin\n"
                      f"{_sha(self.BLOB)}  b.bin\n")
        with self.assertRaises(ls.BinaryManifestError) as cm:
            ls.load_binary_manifest(self.tmp)
        msg = str(cm.exception)
        self.assertIn("3 problem(s)", msg)
        self.assertIn("unknown metadata set everything", msg)
        self.assertIn("already listed at line 4", msg)

    def test_a_text_file_is_unaffected(self):
        self.put("notes.md", "plain prose, nothing binary\n")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual((0, 0), (tally.binaries_by_manifest, tally.binaries_untracked))

    def test_an_ignore_glob_does_not_skip_the_gate_for_a_binary(self):
        # 160/980 GM9, Mike's answer 2026-11-08: the gate runs BEFORE the ignore
        # file for a binary. A glob is path-wide and blind to content, so a
        # reasoned glob over an image directory would pass every present and
        # future image unread; it cannot be the hatch.
        self.put("vendor/font.woff", self.BLOB)
        self.put(".leakscanignore", "vendor/  # third-party fonts, not ours\n")
        tally = ls.Tally()
        self.assertEqual(["binary-unlisted"], [f.rule for f in self.scan(tally=tally)])
        self.assertEqual(0, tally.files_by_glob)
        # ...and the hash-bound entry is what passes it, glob or no glob.
        self.manifest(f"{_sha(self.BLOB)}  vendor/font.woff  # vendored font, looked at\n")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual(1, tally.binaries_by_manifest)

    def test_an_ignore_glob_still_exempts_text_and_is_counted(self):
        self.put("vendor/readme.txt", "plain text, third party\n")
        self.put("vendor/a.bin", b"\x00ignored but gated")
        self.put(".leakscanignore", "vendor/  # third-party files, not ours\n")
        tally = ls.Tally()
        self.assertEqual(["binary-unlisted"], [f.rule for f in self.scan(tally=tally)])
        self.assertEqual(1, tally.files_by_glob)       # the text file only

    def test_an_entry_for_a_glob_ignored_file_that_is_gone_is_stale(self):
        self.put(".leakscanignore", "vendor/  # third-party files, not ours\n")
        self.manifest(f"{_sha(self.BLOB)}  vendor/gone.woff  # was vendored\n")
        self.assertEqual(["binary-stale-entry"], self.rules())

    def test_disable_cannot_switch_the_gate_off(self):
        # No quiet hatch: binary rules are not structural rules.
        rc = ls.main(["--root", str(self.tmp), str(self.tmp), "--terms", str(self.terms),
                      "--disable", "binary-unlisted"])
        self.assertEqual(2, rc)


class BinaryStaleEntries(_TreeCase):
    BLOB = b"\x00stale fixture"

    def test_an_entry_for_a_missing_file_blocks(self):
        self.manifest(f"{_sha(self.BLOB)}  gone.bin  # was a fixture\n")
        fs = self.scan()
        self.assertEqual(["binary-stale-entry"], [f.rule for f in fs])
        self.assertEqual((ls.BINARY_MANIFEST, 1), (fs[0].path, fs[0].line))
        self.assertIn("no such file", fs[0].excerpt)

    def test_an_entry_for_a_text_file_is_stale(self):
        self.put("doc.md", "text\n")
        self.manifest(f"{_sha(b'text')}  doc.md  # mistaken entry\n")
        fs = self.scan()
        self.assertEqual(["binary-stale-entry"], [f.rule for f in fs])
        self.assertIn("read as text", fs[0].excerpt)

    def test_staleness_is_judged_only_inside_the_scanned_paths(self):
        self.put("sub/ok.md", "text\n")
        self.manifest(f"{_sha(self.BLOB)}  elsewhere/gone.bin  # was a fixture\n")
        self.assertEqual([], self.scan(paths=[self.tmp / "sub"]))

    def test_a_renamed_binary_names_its_old_entry(self):
        self.put("new/name.bin", self.BLOB)
        self.manifest(f"{_sha(self.BLOB)}  old/name.bin  # reviewed fixture\n")
        fs = sorted(self.scan(), key=lambda f: f.rule)
        self.assertEqual(["binary-stale-entry", "binary-unlisted"], [f.rule for f in fs])
        self.assertIn("same bytes as the entry for old/name.bin", fs[1].excerpt)


class BinaryMetadata(_TreeCase):
    """Every metadata set present blocks until its own reasoned line keeps it
    (Mike, 2026-10-18: "only keep the metadata it has a need for"); text
    sets are scanned whether or not they are kept."""

    def _listed(self, rel, data, *sets):
        self.put(rel, data)
        d = _sha(data)
        self.manifest(f"{d}  {rel}  # synthetic test image, reviewed\n"
                      + "".join(f"{d}:{s}  {rel}  # test needs the {s} set\n"
                                for s in sets))

    def test_png_exif_blocks_even_when_the_pixels_are_listed(self):
        self._listed("i.png", _png((b"eXIf", b"MM\x00\x2a\x00\x00\x00\x08")))
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertIn("eXIf", fs[0].excerpt)

    def test_a_line_keeping_the_set_accepts_it(self):
        self._listed("i.png", _png((b"eXIf", b"MM\x00\x2a")), "exif")
        self.assertEqual([], self.scan())

    def test_an_unlisted_metadata_image_reports_both(self):
        self.put("i.png", _png((b"eXIf", b"MM\x00\x2a")))
        self.assertEqual(["binary-metadata", "binary-unlisted"], self.rules())

    def test_png_text_metadata_is_scanned_and_markers_inside_are_ignored(self):
        data = _png((b"tEXt", b"Author\x00a.b@example.com  # leakscan:allow: hidden"))
        self._listed("i.png", data, "png-text")
        fs = self.scan()
        self.assertEqual(["email"], [f.rule for f in fs])
        self.assertEqual("metadata PNG tEXt 'Author'", fs[0].where)

    def test_harmless_text_metadata_passes_only_once_its_set_is_kept(self):
        data = _png((b"tEXt", b"Software\x00www.inkscape.org"))
        self._listed("i.png", data)
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertTrue(fs[0].excerpt.startswith("png-text:"), fs[0].excerpt)
        self._listed("i.png", data, "png-text")
        self.assertEqual([], self.scan())

    def test_compressed_text_chunks_are_inflated_and_scanned(self):
        z = _png((b"zTXt", b"Comment\x00\x00" + _zlib.compress(b"call a.b@example.com")))
        self._listed("z.png", z, "png-text")
        self.assertEqual(["email"], self.rules())
        itxt = (b"XML:com.adobe.xmp\x00\x01\x00\x00\x00"
                + _zlib.compress(b"<dc:creator>a.b@example.com</dc:creator>"))
        self.put("z.png", b"plain text now\n")
        self._listed("x.png", _png((b"iTXt", itxt)), "xmp")
        self.assertEqual(["email"], self.rules())

    def test_a_decompression_bomb_reads_as_opaque(self):
        bomb = _png((b"zTXt", b"Comment\x00\x00"
                     + _zlib.compress(b"A" * (ls.META_SEGMENT_CAP + 10))))
        self._listed("b.png", bomb)
        self.assertEqual(["binary-metadata"], self.rules())

    def test_imagemagick_raw_profile_is_opaque(self):
        self._listed("r.png", _png((b"zTXt", b"Raw profile type exif\x00\x00"
                                    + _zlib.compress(b"\nexif\n  20\n4d4d002a"))))
        self.assertEqual(["binary-metadata"], self.rules())

    def test_a_png_that_cannot_be_walked_fails_closed(self):
        truncated = _png()[:-12] + b"\x00\x00\x10\x00tEXt"  # no IEND; chunk overruns
        self._listed("t.png", truncated)
        self.assertEqual(["binary-metadata"], self.rules())

    def test_jpeg_exif_blocks(self):
        self._listed("e.jpg", _jpeg((0xE0, b"JFIF\x00\x01\x01"), (0xE1, b"Exif\x00\x00MM")))
        self.assertEqual(["binary-metadata"], self.rules())

    def test_jpeg_iptc_blocks(self):
        self._listed("p.jpg", _jpeg((0xED, b"Photoshop 3.0\x008BIM")))
        self.assertEqual(["binary-metadata"], self.rules())

    def test_jpeg_xmp_and_comments_are_read(self):
        self._listed("x.jpg", _jpeg((0xE1, b"http://ns.adobe.com/xap/1.0/\x00<x>a.b@example.com</x>"),
                                    (0xFE, b"plain comment")), "xmp", "jpeg-comment")
        self.assertEqual(["email"], self.rules())

    def test_jpeg_without_metadata_needs_only_its_entry(self):
        self._listed("c.jpg", _jpeg((0xE0, b"JFIF\x00\x01\x01")))
        self.assertEqual([], self.scan())

    def test_webp_exif_blocks(self):
        self._listed("e.webp", _webp((b"VP8 ", b"\x00" * 10), (b"EXIF", b"MM\x00\x2a")))
        self.assertEqual(["binary-metadata"], self.rules())

    def test_webp_xmp_is_read(self):
        self._listed("x.webp", _webp((b"VP8 ", b"\x00" * 10), (b"XMP ", b"<x>a.b@example.com</x>")),
                     "xmp")
        self.assertEqual(["email"], self.rules())

    def test_inspect_media_ignores_other_formats(self):
        import io
        self.assertEqual((None, [], []), ls.inspect_media(io.BytesIO(b"GIF89a\x00\x00")))


def _tiff(ifd0=(), exif=(), gps=(), little=False, raw_ptr=None):
    """A synthetic TIFF/Exif block (the part after `Exif\\0\\0`): one IFD0 of
    `ifd0` tag numbers, plus an Exif IFD and a GPS IFD when given. Values are
    zero: only tag numbers are read."""
    e = "<" if little else ">"

    def ifd(tags, ptrs):
        entries = [(t, 0) for t in tags] + ptrs
        return (_struct.pack(e + "H", len(entries))
                + b"".join(_struct.pack(e + "HHII", t, 2, 1, v) for t, v in entries)
                + _struct.pack(e + "I", 0))

    sizes = [2 + 12 * (len(ifd0) + bool(exif) + bool(gps)) + 4,
             2 + 12 * len(exif) + 4, 2 + 12 * len(gps) + 4]
    at_exif = 8 + sizes[0]
    at_gps = at_exif + (sizes[1] if exif else 0)
    ptrs = ([(0x8769, at_exif)] if exif else []) + ([(0x8825, at_gps)] if gps else [])
    body = ifd(ifd0, ptrs) + (ifd(exif, []) if exif else b"") + (ifd(gps, []) if gps else b"")
    return (b"II*\x00" if little else b"MM\x00*") + _struct.pack(e + "I", 8) + body


MAKE, MODEL, SOFTWARE = 0x010F, 0x0110, 0x0131
LENS_MODEL, DATE_ORIG = 0xA434, 0x9003
GPS_LAT, GPS_LON = 0x0002, 0x0004


class ExifFieldParsing(unittest.TestCase):
    """020/450 — Exif and GPS tags read by NAME, tag numbers only, bounded."""

    def test_fields_are_named_from_each_ifd(self):
        blob = _tiff(ifd0=[MAKE, MODEL], exif=[LENS_MODEL, DATE_ORIG],
                     gps=[GPS_LAT, GPS_LON])
        self.assertEqual(
            ["exif:DateTimeOriginal", "exif:LensModel", "exif:Make", "exif:Model",
             "gps:GPSLatitude", "gps:GPSLongitude"], ls.exif_fields(blob))

    def test_either_byte_order_and_the_exif_prefix_read_alike(self):
        a = _tiff(ifd0=[MODEL], gps=[GPS_LAT])
        b = _tiff(ifd0=[MODEL], gps=[GPS_LAT], little=True)
        self.assertEqual(ls.exif_fields(a), ls.exif_fields(b))
        self.assertEqual(ls.exif_fields(a), ls.exif_fields(b"Exif\x00\x00" + a))

    def test_gps_tag_numbers_do_not_borrow_the_exif_names(self):
        # Tag 0x0002 is InteroperabilityVersion in an Exif IFD, GPSLatitude
        # in the GPS one: the IFD decides the name.
        self.assertEqual(["exif:InteroperabilityVersion"],
                         ls.exif_fields(_tiff(ifd0=[0x0002])))
        self.assertEqual(["gps:GPSLatitude"], ls.exif_fields(_tiff(gps=[0x0002])))

    def test_an_unnamed_tag_is_reported_by_its_number(self):
        self.assertEqual(["exif:0x9999"], ls.exif_fields(_tiff(ifd0=[0x9999])))
        self.assertEqual(["gps:0x0040"], ls.exif_fields(_tiff(gps=[0x0040])))

    def test_an_empty_block_has_no_fields(self):
        self.assertEqual([], ls.exif_fields(_tiff()))

    def test_what_cannot_be_walked_is_unknown(self):
        good = _tiff(ifd0=[MAKE, MODEL])
        for name, blob in (("empty", b""), ("short", b"MM\x00\x2a"),
                           ("bad magic", b"MM\x00\x2b" + good[4:]),
                           ("bad order", b"XX" + good[2:]),
                           ("ifd offset past the end", good[:4] + b"\x00\x00\xff\xff"),
                           ("truncated entries", good[:20])):
            with self.subTest(name):
                self.assertIn("exif:unknown", ls.exif_fields(blob))

    def test_a_truncated_block_still_names_what_it_did_hold(self):
        good = _tiff(ifd0=[MAKE, MODEL, SOFTWARE])
        got = ls.exif_fields(good[:8 + 2 + 12 * 2])    # two whole entries
        self.assertIn("exif:Make", got)
        self.assertIn("exif:unknown", got)

    def test_a_pointer_loop_terminates_and_is_not_an_error(self):
        # IFD0's Exif pointer points back at IFD0.
        blob = (b"MM\x00*" + _struct.pack(">I", 8) + _struct.pack(">H", 2)
                + _struct.pack(">HHII", MODEL, 2, 1, 0)
                + _struct.pack(">HHII", 0x8769, 4, 1, 8) + _struct.pack(">I", 0))
        self.assertEqual(["exif:Model"], ls.exif_fields(blob))

    def test_a_chain_longer_than_the_cap_fails_closed(self):
        # IFD1, IFD2, ... each pointing at the next: past 16 IFDs it is unknown.
        n = ls._EXIF_MAX_IFDS + 4
        size = 2 + 4
        blob = b"MM\x00*" + _struct.pack(">I", 8)
        for i in range(n):
            nxt = 8 + size * (i + 1) if i + 1 < n else 0
            blob += _struct.pack(">H", 0) + _struct.pack(">I", nxt)
        self.assertIn("exif:unknown", ls.exif_fields(blob))

    def test_a_huge_declared_count_is_bounded_not_allocated(self):
        blob = b"MM\x00*" + _struct.pack(">I", 8) + _struct.pack(">H", 0xFFFF)
        self.assertEqual(["exif:unknown"], ls.exif_fields(blob))

    def test_every_table_name_is_valid_where_it_is_used(self):
        for name in ("Model", "LensModel", "unknown", "0x9999"):
            self.assertTrue(ls.field_valid("exif", name), name)
        for name in ("GPSLatitude", "0x0040"):
            self.assertTrue(ls.field_valid("gps", name), name)
        for fs, name in (("exif", "model"), ("exif", "GPSLatitude"), ("gps", "Model"),
                         ("gps", "unknown"), ("iptc", "Model"), ("exif", "0x99")):
            self.assertFalse(ls.field_valid(fs, name), (fs, name))


class BinaryFieldLevel(_TreeCase):
    """020/450 — an entry names the Exif/GPS fields it keeps, under one
    reason; any field present and not named blocks, naming it."""

    def setUp(self):
        super().setUp()
        self.blob = _tiff(ifd0=[MAKE, MODEL], exif=[LENS_MODEL],
                          gps=[GPS_LAT, GPS_LON])
        self.png = _png((b"eXIf", self.blob))

    def keep(self, data, *scopes, rel="p.png"):
        self.put(rel, data)
        d = _sha(data)
        self.manifest(f"{d}  {rel}  # synthetic photo, reviewed\n"
                      + "".join(f"{d}:{s}  {rel}  # test needs {s}\n" for s in scopes))

    def test_every_unkept_field_is_named_in_the_block(self):
        self.keep(self.png)
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        for k in ("exif:Make", "exif:Model", "exif:LensModel",
                  "gps:GPSLatitude", "gps:GPSLongitude"):
            self.assertIn(k, fs[0].excerpt)

    def test_the_camera_model_kept_blocks_the_gps_beside_it(self):
        self.keep(self.png, "exif:Make,Model,LensModel")
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertIn("gps:GPSLatitude", fs[0].excerpt)
        self.assertIn("gps:GPSLongitude", fs[0].excerpt)
        self.assertNotIn("exif:Model", fs[0].excerpt)

    def test_naming_every_field_accepts_the_photo(self):
        self.keep(self.png, "exif:Make,Model,LensModel,gps:GPSLatitude,GPSLongitude")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual(1, tally.binaries_by_manifest)
        self.assertEqual([], tally.type_level_warnings)

    def test_fields_may_sit_on_separate_lines_with_their_own_reasons(self):
        self.keep(self.png, "exif:Make,Model,LensModel", "gps:GPSLatitude,GPSLongitude")
        self.assertEqual([], self.scan())

    def test_one_missing_field_is_the_only_one_named(self):
        self.keep(self.png, "exif:Make,Model,LensModel,gps:GPSLatitude")
        fs = self.scan()
        self.assertEqual(1, len(fs))
        self.assertIn("gps:GPSLongitude", fs[0].excerpt)
        self.assertNotIn("GPSLatitude", fs[0].excerpt)

    def test_a_field_the_file_lacks_is_a_stale_line(self):
        self.keep(self.png, "exif:Make,Model,LensModel,gps:GPSLatitude,GPSLongitude",
                  "exif:Software")
        fs = self.scan()
        self.assertEqual(["binary-stale-entry"], [f.rule for f in fs])
        self.assertIn("keeps exif:Software, which these bytes do not carry", fs[0].excerpt)

    def test_an_unnamed_tag_blocks_until_kept_by_number(self):
        data = _png((b"eXIf", _tiff(ifd0=[MODEL, 0x9999])))
        self.keep(data, "exif:Model")
        fs = self.scan()
        self.assertIn("exif:0x9999", fs[0].excerpt)
        self.keep(data, "exif:Model,0x9999")
        self.assertEqual([], self.scan())

    def test_an_undecodable_exif_blocks_as_unknown_until_named(self):
        data = _png((b"eXIf", b"MM\x00\x2a\x00\x00"))
        self.keep(data)
        self.assertIn("exif:unknown", self.scan()[0].excerpt)
        self.keep(data, "exif:unknown")
        self.assertEqual([], self.scan())

    def test_a_set_with_no_fields_needs_no_line(self):
        self.keep(_png((b"eXIf", _tiff())))
        self.assertEqual([], self.scan())

    def test_the_same_fields_in_jpeg_and_webp_and_a_raw_profile(self):
        raw = ("\nexif\n  %d\n" % len(self.blob)) + self.blob.hex()
        for rel, data in (
                ("p.jpg", _jpeg((0xE1, b"Exif\x00\x00" + self.blob))),
                ("p.webp", _webp((b"VP8 ", b"\x00" * 10), (b"EXIF", self.blob))),
                ("r.png", _png((b"zTXt", b"Raw profile type exif\x00\x00"
                                + _zlib.compress(raw.encode())))),
                ("r2.png", _png((b"tEXt", b"Raw profile type APP1\x00" + raw.encode())))):
            with self.subTest(rel):
                one = [self.tmp / rel]       # earlier subtests' files stay in the tree
                self.keep(data, rel=rel)
                fs = self.scan(paths=one)
                self.assertEqual(["binary-metadata"], [f.rule for f in fs])
                self.assertIn("gps:GPSLatitude", fs[0].excerpt)
                self.keep(data, "exif:Make,Model,LensModel,gps:GPSLatitude,GPSLongitude",
                          rel=rel)
                self.assertEqual([], self.scan(paths=one))

    def test_an_undecodable_raw_profile_is_exif_unknown(self):
        data = _png((b"tEXt", b"Raw profile type exif\x00\nexif\n  4\nzz"))
        self.keep(data)
        self.assertIn("exif:unknown", self.scan()[0].excerpt)

    def test_an_exif_past_the_cap_is_exif_unknown(self):
        big = _tiff(ifd0=[MODEL]) + b"\x00" * ls.META_SEGMENT_CAP
        self.keep(_png((b"eXIf", big)))
        self.assertIn("exif:unknown", self.scan()[0].excerpt)

    # -- type-level entries: accepted with a warning, then refused ----------

    def type_level(self):
        self.keep(self.png, "exif")

    def run_main(self, day, *extra):
        out, err = io.StringIO(), io.StringIO()
        with _on(day), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = ls.main(["--root", str(self.tmp), str(self.tmp),
                          "--terms", str(self.terms), *extra])
        return rc, out.getvalue(), err.getvalue()

    def test_the_type_level_cutoff_is_a_later_iso_date(self):
        self.assertIsInstance(ls.TYPE_LEVEL_UNTIL, _dt.date)
        self.assertGreaterEqual(ls.TYPE_LEVEL_UNTIL, _dt.date(2026, 12, 18))
        self.assertTrue(ls.in_type_level_grace(ls.TYPE_LEVEL_UNTIL - _dt.timedelta(days=1)))
        self.assertFalse(ls.in_type_level_grace(ls.TYPE_LEVEL_UNTIL))

    def test_a_type_level_line_still_keeps_the_set_with_a_warning(self):
        self.type_level()
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual(1, len(tally.type_level_warnings))
        w = tally.type_level_warnings[0]
        self.assertEqual(ls.TYPE_LEVEL_RULE, w.rule)
        for k in ("exif:Make", "exif:Model", "gps:GPSLatitude"):
            self.assertIn(k, w.excerpt)

    def test_the_warning_names_the_fields_the_date_and_the_remedy_and_exits_0(self):
        self.type_level()
        rc, out, _err = self.run_main(ls.TYPE_LEVEL_UNTIL - _dt.timedelta(days=1))
        self.assertEqual(0, rc, out)
        self.assertIn("WARNING ONLY until " + ls.TYPE_LEVEL_UNTIL.isoformat(), out)
        self.assertIn("gps:GPSLatitude", out)
        self.assertIn("name the fields instead", out)
        self.assertIn("1 type-level metadata entr(y/ies) warned", out)

    def test_from_the_cutoff_a_type_level_line_no_longer_keeps_the_set(self):
        self.type_level()
        rc, out, _err = self.run_main(ls.TYPE_LEVEL_UNTIL)
        self.assertEqual(1, rc, out)
        self.assertIn("binary-metadata", out)
        self.assertIn("no longer keeps it", out)
        self.assertIn("gps:GPSLatitude", out)
        self.assertNotIn("WARNING ONLY until " + ls.TYPE_LEVEL_UNTIL.isoformat(), out)

    def test_type_level_stays_valid_for_sets_whose_fields_are_not_read(self):
        data = _png((b"iCCP", b"p\x00\x00" + _zlib.compress(b"profile")))
        self.keep(data, "icc")
        with _on(ls.TYPE_LEVEL_UNTIL + _dt.timedelta(days=400)):
            self.assertEqual([], self.scan())

    def test_json_carries_the_type_level_warnings(self):
        self.type_level()
        rc, out, _err = self.run_main(ls.TYPE_LEVEL_UNTIL - _dt.timedelta(days=1), "--json")
        self.assertEqual(0, rc)
        doc = json.loads(out)
        self.assertEqual([], doc["findings"])
        self.assertTrue(doc["binary_type_level"]["active"])
        self.assertEqual(["leakscan:binary-type-level"],
                         [w["id"] for w in doc["binary_type_level"]["warnings"]])

    # -- the manifest grammar ----------------------------------------------

    def _refused(self, scope, needle):
        d = _sha(b"x")
        self.manifest(f"{d}  a.png  # ok\n{d}:{scope}  a.png  # need\n")
        with self.assertRaises(ls.BinaryManifestError) as cm:
            ls.load_binary_manifest(self.tmp)
        self.assertIn(needle, str(cm.exception))

    def test_scope_grammar_is_strict(self):
        self._refused("exif:Modle", "unknown exif field Modle")
        self._refused("gps:Model", "unknown gps field Model")
        self._refused("gps", "name them")
        self._refused("gps,exif:Model", "name them")
        self._refused("exif:", "unknown exif field")
        self._refused("icc:Profile", "'icc' has no fields to name")
        self._refused("exif:Model,Model", "list each metadata set once")
        self._refused("exif:Model,exif", "already keeps")
        self._refused("exif,gps:GPSLatitude", "already keeps")
        self._refused("exif:Model,icc,colour", "unknown metadata set colour")
        self._refused("exif:Model,colour", "unknown exif field colour")
        self._refused("exif:model", "unknown exif field model")

    def test_scope_grammar_accepts_the_documented_forms(self):
        for scope, want in (
                ("icc,xmp", ["icc", "xmp"]),
                ("exif", ["exif"]),
                ("exif:Model,LensModel", ["exif:Model", "exif:LensModel"]),
                ("exif:Model,gps:GPSLatitude,GPSLongitude",
                 ["exif:Model", "gps:GPSLatitude", "gps:GPSLongitude"]),
                ("exif:Model,icc", ["exif:Model", "icc"])):
            with self.subTest(scope):
                self.assertEqual((want, None), ls.parse_scope(scope))

    def test_a_field_and_its_whole_set_on_two_lines_are_refused(self):
        d = _sha(b"x")
        self.manifest(f"{d}  a.png  # ok\n{d}:exif:Model  a.png  # model\n"
                      f"{d}:exif  a.png  # all\n")
        with self.assertRaises(ls.BinaryManifestError) as cm:
            ls.load_binary_manifest(self.tmp)
        self.assertIn("already kept at line 2", str(cm.exception))

    def test_a_field_set_line_still_needs_its_own_reason(self):
        d = _sha(b"x")
        self.manifest(f"# reviewed\n{d}  a.png\n{d}:exif:Model  a.png\n")
        with self.assertRaises(ls.BinaryManifestError) as cm:
            ls.load_binary_manifest(self.tmp)
        self.assertIn("needs its own reason", str(cm.exception))

    # -- --binary-entries ---------------------------------------------------

    def listing(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = ls.main(["--root", str(self.tmp), "--binary-entries"])
        return rc, out.getvalue(), err.getvalue()

    def test_the_listing_prints_one_line_per_field(self):
        self.put("p.png", self.png)
        d = _sha(self.png)
        rc, out, err = self.listing()
        self.assertEqual(0, rc)
        self.assertEqual(
            sorted([f"{d}  p.png"] + [f"{d}:{k}  p.png" for k in (
                "exif:Make", "exif:Model", "exif:LensModel",
                "gps:GPSLatitude", "gps:GPSLongitude")]),
            sorted(_bare(out).splitlines()))
        self.assertIn("gps:GPSLatitude", err)
        self.assertIn(f"{d}:exif:Model,LensModel", err)

    def test_the_listing_lines_are_loadable_once_given_reasons_and_merged(self):
        self.put("p.png", self.png)
        d = _sha(self.png)
        self.manifest(f"{d}  p.png  # synthetic photo\n"
                      f"{d}:exif:Make,Model,LensModel  p.png  # the shop shows the camera\n"
                      f"{d}:gps:GPSLatitude,GPSLongitude  p.png  # the venue pin\n")
        self.assertEqual([], self.scan())
        self.assertEqual("", self.listing()[1])

    def test_a_type_level_line_is_migrated_by_the_listing(self):
        self.type_level()
        d = _sha(self.png)
        rc, out, err = self.listing()
        self.assertEqual(0, rc)
        lines = _bare(out).splitlines()
        self.assertIn(f"{d}:gps:GPSLatitude  p.png", lines)
        self.assertNotIn(f"{d}  p.png", lines)         # the file line still stands
        self.assertIn("type-level line for exif (line 2)", err)
        self.assertIn(ls.TYPE_LEVEL_UNTIL.isoformat(), err)


def _iim(*datasets):
    """IPTC IIM datasets `(record, dataset, value)` as bytes."""
    return b"".join(b"\x1c" + bytes([r, d]) + _struct.pack(">H", len(v)) + v
                    for r, d, v in datasets)


def _app13(iim, *other):
    """A Photoshop 3.0 APP13 payload: IPTC resource 0x0404 holding `iim`, then
    `other` `(resource id, bytes)` resources."""
    def res(rid, data):
        return (b"8BIM" + _struct.pack(">H", rid) + b"\x00\x00"
                + _struct.pack(">I", len(data)) + data + (b"\x00" if len(data) % 2 else b""))
    return b"Photoshop 3.0\x00" + res(0x0404, iim) + b"".join(res(i, d) for i, d in other)


_RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"


def _xmp(body="", attrs="", ns=""):
    """An XMP packet with one rdf:Description holding `attrs` (attribute-form
    properties) and `body` (element-form properties); `ns` adds declarations.
    dc and exif are always declared."""
    return (f'<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>'
            f'<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="{_RDF}">'
            f'<rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/" '
            f'xmlns:exif="http://ns.adobe.com/exif/1.0/" {ns} {attrs}>{body}'
            f'</rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>').encode()


class IptcFieldParsing(unittest.TestCase):
    """020/450 part 2 — IPTC datasets read by name, lengths only, bounded."""

    IIM = _iim((2, 80, b"Jane Q"), (2, 90, b"Springfield"), (2, 25, b"k1"), (2, 25, b"k2"))

    def test_datasets_are_named_once_each(self):
        self.assertEqual(["iptc:By-line", "iptc:City", "iptc:Keywords"],
                         ls.iptc_fields(_app13(self.IIM)))

    def test_bare_8bim_and_bare_iim_read_alike(self):
        want = ls.iptc_fields(_app13(self.IIM))
        self.assertEqual(want, ls.iptc_fields(_app13(self.IIM)[len(b"Photoshop 3.0\x00"):]))
        self.assertEqual(want, ls.iptc_fields(self.IIM))

    def test_an_unnamed_dataset_is_written_record_colon_number(self):
        self.assertEqual(["iptc:2:250"], ls.iptc_fields(_iim((2, 250, b"x"))))
        self.assertEqual(["iptc:3:010"], ls.iptc_fields(_iim((3, 10, b"x"))))

    def test_another_photoshop_resource_is_named_by_its_id(self):
        got = ls.iptc_fields(_app13(self.IIM, (0x03ED, b"abcd"), (0x0425, b"x" * 16)))
        self.assertIn("iptc:8BIM-0x03ED", got)
        self.assertIn("iptc:8BIM-0x0425", got)
        self.assertNotIn("iptc:unknown", got)

    def test_a_photoshop_block_with_no_iptc_has_no_dataset(self):
        self.assertEqual(["iptc:8BIM-0x03ED"],
                         ls.iptc_fields(b"Photoshop 3.0\x00" + _app13(b"")[14:][:0]
                                        + b"8BIM\x03\xed\x00\x00\x00\x00\x00\x02ab"))

    def test_an_extended_length_dataset_is_walked(self):
        ext = b"\x1c\x02\x78" + _struct.pack(">H", 0x8004) + _struct.pack(">I", 3) + b"abc"
        self.assertEqual(["iptc:Caption-Abstract"], ls.iptc_fields(ext))

    def test_trailing_zero_padding_is_not_an_error(self):
        self.assertEqual(["iptc:City"], ls.iptc_fields(_iim((2, 90, b"x")) + b"\x00\x00"))

    def test_what_cannot_be_walked_is_unknown(self):
        good = _app13(self.IIM)
        for name, blob in (("empty", b""), ("junk", b"not iptc"),
                           ("truncated dataset", good[:-3]),
                           ("bad marker", b"\x1c\x02\x5a\x00\x01x\x07"),
                           ("record 0", _iim((0, 1, b"x"))),
                           ("record 10", _iim((10, 1, b"x"))),
                           ("resource overruns", good[:20]),
                           ("garbage after a resource", good + b"zzzz"),
                           ("length field too long",
                            b"\x1c\x02\x78" + _struct.pack(">H", 0x8009) + b"x" * 9)):
            with self.subTest(name):
                self.assertIn("iptc:unknown", ls.iptc_fields(blob))

    def test_a_truncated_block_still_names_what_it_did_hold(self):
        got = ls.iptc_fields(_iim((2, 80, b"a"), (2, 90, b"b"))[:-3])
        self.assertIn("iptc:By-line", got)
        self.assertIn("iptc:unknown", got)

    def test_too_many_datasets_fail_closed(self):
        many = _iim(*[(2, 25, b"")] * (ls._IPTC_MAX_DATASETS + 1))
        self.assertIn("iptc:unknown", ls.iptc_fields(many))

    def test_too_many_resources_fail_closed(self):
        res = b"8BIM\x03\xed\x00\x00\x00\x00\x00\x00"
        self.assertIn("iptc:unknown", ls.iptc_fields(
            b"Photoshop 3.0\x00" + res * (ls._IPTC_MAX_RESOURCES + 1)))

    def test_every_dataset_name_is_valid_and_unique(self):
        names = list(ls.IPTC_DATASETS.values())
        self.assertEqual(len(names), len(set(names)))
        for n in names + ["unknown", "2:999", "8BIM-0x03ED"]:
            self.assertTrue(ls.field_valid("iptc", n), n)
        for n in ("by-line", "2:99", "22:099", "Model", "8BIM-0x3ed", ""):
            self.assertFalse(ls.field_valid("iptc", n), n)


class XmpFieldParsing(unittest.TestCase):
    """020/450 part 2 — XMP properties read by name from the RDF skeleton,
    stdlib expat, no entity expansion, bounded."""

    def test_element_and_attribute_properties_are_named(self):
        got = ls.xmp_fields(_xmp(
            body="<dc:creator><rdf:Seq><rdf:li>Jane</rdf:li></rdf:Seq></dc:creator>"
                 "<dc:title>T</dc:title>",
            attrs='exif:GPSLatitude="41,24N"'))
        self.assertEqual(["xmp:dc:creator", "xmp:dc:title", "xmp:exif:GPSLatitude"], got)

    def test_a_structure_is_one_field_not_its_members(self):
        got = ls.xmp_fields(_xmp(
            body='<exif:Flash rdf:parseType="Resource"><exif:Fired>True</exif:Fired>'
                 '</exif:Flash>'))
        self.assertEqual(["xmp:exif:Flash"], got)

    def test_rdf_syntax_attributes_and_xml_lang_are_not_properties(self):
        self.assertEqual(["xmp:dc:title"], ls.xmp_fields(_xmp(
            body='<dc:title xml:lang="en">T</dc:title>', attrs='xml:lang="en"')))

    def test_well_known_namespaces_use_their_usual_prefix(self):
        pkt = _xmp(ns='xmlns:zz="http://purl.org/dc/elements/1.1/" '
                      'xmlns:co="http://example.invalid/ns/"',
                   body="<zz:creator>a</zz:creator><co:Thing>b</co:Thing>")
        self.assertEqual(["xmp:co:Thing", "xmp:dc:creator"], ls.xmp_fields(pkt))

    def test_an_empty_packet_has_no_properties(self):
        self.assertEqual([], ls.xmp_fields(_xmp()))

    def test_a_utf8_byte_order_mark_is_accepted(self):
        self.assertEqual(["xmp:dc:title"],
                         ls.xmp_fields(b"\xef\xbb\xbf" + _xmp(body="<dc:title>t</dc:title>")))

    def test_what_cannot_be_read_is_unknown(self):
        good = _xmp(body="<dc:title>t</dc:title>")
        for name, blob in (
                ("empty", b""),
                ("not xml", b"just text"),
                ("truncated", good[:90]),
                ("no rdf", b'<x:xmpmeta xmlns:x="adobe:ns:meta/"/>'),
                ("wrong root", b"<a><b/></a>"),
                ("doctype", b'<!DOCTYPE a>' + good),
                ("entity declared", b'<!DOCTYPE a [<!ENTITY e "x">]>' + good),
                ("undefined entity", good.replace(b">t<", b">&e;<")),
                ("stray element under xmpmeta",
                 good.replace(b"</x:xmpmeta>", b"<x:other/></x:xmpmeta>")),
                ("non-Description under RDF",
                 good.replace(b"</rdf:RDF>", b"<dc:x/></rdf:RDF>")),
                ("unqualified attribute", _xmp(attrs='plain="1"')),
                ("default-namespace property",
                 _xmp(ns='xmlns="http://example.invalid/d"', body="<Thing>1</Thing>")),
                ("odd name", _xmp(ns='xmlns:q="http://example.invalid/q"',
                                  body="<q:caf\u00e9>1</q:caf\u00e9>".encode("utf-8").decode()))):
            with self.subTest(name):
                self.assertEqual(["xmp:unknown"], ls.xmp_fields(blob))

    def test_an_entity_bomb_is_refused_before_any_expansion(self):
        bomb = (b'<!DOCTYPE b [<!ENTITY a "aaaaaaaaaa"><!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;">'
                b'<!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;">]>' + _xmp(body="<dc:title>&c;</dc:title>"))
        self.assertEqual(["xmp:unknown"], ls.xmp_fields(bomb))

    def test_too_many_properties_fail_closed(self):
        n = ls._XMP_MAX_PROPERTIES + 1
        pkt = _xmp(body="".join(f"<dc:p{i}>x</dc:p{i}>" for i in range(n)))
        self.assertEqual(["xmp:unknown"], ls.xmp_fields(pkt))

    def test_field_names(self):
        for n in ("dc:creator", "exif:GPSLatitude", "Iptc4xmpExt:LocationShown", "unknown"):
            self.assertTrue(ls.field_valid("xmp", n), n)
        for n in ("creator", "dc:", ":creator", "dc:a:b", "1dc:x", "dc:caf\u00e9"):
            self.assertFalse(ls.field_valid("xmp", n), n)


class PngTextKeys(unittest.TestCase):
    def test_keywords_become_one_manifest_token(self):
        for kw, want in ((b"Author", "png-text:Author"),
                         (b"Creation Time", "png-text:Creation%20Time"),
                         (b"a:b,c", "png-text:a%3Ab%2Cc"),
                         (b"100%", "png-text:100%25"),
                         (b"caf\xe9", "png-text:caf%E9"),
                         (b"unknown", "png-text:%75nknown"),
                         (b"", "png-text:unknown"),
                         (b"x" * 80, "png-text:unknown")):
            with self.subTest(kw):
                self.assertEqual(want, ls.png_text_field(kw))
                self.assertTrue(ls.field_valid("png-text", want.split(":", 1)[1]), want)

    def test_a_keyword_cannot_pass_as_the_parse_failure_field(self):
        self.assertNotEqual(ls.png_text_field(b"unknown"), "png-text:unknown")

    def test_names(self):
        for n in ("Author", "Creation%20Time", "unknown", "a.b-c_d"):
            self.assertTrue(ls.field_valid("png-text", n), n)
        for n in ("Creation Time", "a:b", "%2", "", "x" * 300):
            self.assertFalse(ls.field_valid("png-text", n), n)


class BinaryFieldLevelOtherSets(_TreeCase):
    """020/450 part 2 — IPTC, XMP and PNG text kept field by field, with the
    same blocking, stale, type-level and listing behaviour as Exif."""

    SECRET = "ZEBRA-QUOKKA-VALUE"           # a value: it must never be printed

    def setUp(self):
        super().setUp()
        self.iim = _iim((2, 80, self.SECRET.encode()), (2, 90, b"Springfield"))
        self.jpg = _jpeg((0xED, _app13(self.iim)))
        self.xmp = _xmp(body=f"<dc:creator>{self.SECRET}</dc:creator>",
                        attrs='exif:GPSLatitude="41,24N"')
        self.png = _png((b"tEXt", b"Author\x00" + self.SECRET.encode()),
                        (b"tEXt", b"Creation Time\x002026-01-01"))

    def keep(self, data, *scopes, rel="p.bin"):
        self.put(rel, data)
        d = _sha(data)
        self.manifest(f"{d}  {rel}  # synthetic photo, reviewed\n"
                      + "".join(f"{d}:{s}  {rel}  # test needs {s}\n" for s in scopes))

    def run_main(self, day, *extra):
        out, err = io.StringIO(), io.StringIO()
        with _on(day), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = ls.main(["--root", str(self.tmp), str(self.tmp),
                          "--terms", str(self.terms), *extra])
        return rc, out.getvalue(), err.getvalue()

    # -- IPTC ----------------------------------------------------------------

    def test_iptc_unkept_fields_are_named_in_the_block(self):
        self.keep(self.jpg, rel="p.jpg")
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertIn("iptc:By-line", fs[0].excerpt)
        self.assertIn("iptc:City", fs[0].excerpt)

    def test_iptc_one_kept_field_leaves_the_other_blocking(self):
        self.keep(self.jpg, "iptc:City", rel="p.jpg")
        fs = self.scan()
        self.assertEqual(1, len(fs))
        self.assertIn("iptc:By-line", fs[0].excerpt)
        self.assertNotIn("iptc:City", fs[0].excerpt)

    def test_iptc_naming_every_field_accepts_it(self):
        self.keep(self.jpg, "iptc:By-line,City", rel="p.jpg")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual([], tally.type_level_warnings)

    def test_iptc_an_unnamed_dataset_blocks_until_kept_by_number(self):
        data = _jpeg((0xED, _app13(_iim((2, 90, b"x"), (2, 250, b"y")))))
        self.keep(data, "iptc:City", rel="p.jpg")
        self.assertIn("iptc:2:250", self.scan()[0].excerpt)
        self.keep(data, "iptc:City,2:250", rel="p.jpg")
        self.assertEqual([], self.scan())

    def test_iptc_an_unwalkable_block_is_unknown_until_named(self):
        data = _jpeg((0xED, b"Photoshop 3.0\x008BIM"))
        self.keep(data, rel="p.jpg")
        self.assertIn("iptc:unknown", self.scan()[0].excerpt)
        self.keep(data, "iptc:unknown", rel="p.jpg")
        self.assertEqual([], self.scan())

    def test_iptc_in_an_imagemagick_raw_profile(self):
        raw = ("\nIPTC\n  %d\n" % len(self.iim)) + self.iim.hex()
        data = _png((b"tEXt", b"Raw profile type iptc\x00" + raw.encode()))
        self.keep(data, rel="r.png")
        self.assertIn("iptc:By-line", self.scan()[0].excerpt)
        self.keep(data, "iptc:By-line,City", rel="r.png")
        self.assertEqual([], self.scan())

    def test_iptc_a_dataset_the_file_lacks_is_stale(self):
        self.keep(self.jpg, "iptc:By-line,City", "iptc:Headline", rel="p.jpg")
        fs = self.scan()
        self.assertEqual(["binary-stale-entry"], [f.rule for f in fs])
        self.assertIn("keeps iptc:Headline", fs[0].excerpt)

    # -- XMP -----------------------------------------------------------------

    def test_xmp_unkept_properties_are_named_in_the_block(self):
        self.keep(_png((b"iTXt", b"XML:com.adobe.xmp\x00\x00\x00\x00\x00" + self.xmp)),
                  rel="x.png")
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertIn("xmp:dc:creator", fs[0].excerpt)
        self.assertIn("xmp:exif:GPSLatitude", fs[0].excerpt)

    def test_xmp_the_gps_property_is_the_only_one_left_blocking(self):
        data = _jpeg((0xE1, b"http://ns.adobe.com/xap/1.0/\x00" + self.xmp))
        self.keep(data, "xmp:dc:creator", rel="x.jpg")
        fs = self.scan()
        self.assertEqual(1, len(fs))
        self.assertIn("xmp:exif:GPSLatitude", fs[0].excerpt)
        self.assertNotIn("dc:creator", fs[0].excerpt)
        self.keep(data, "xmp:dc:creator,xmp:exif:GPSLatitude", rel="x.jpg")
        self.assertEqual([], self.scan())

    def test_xmp_an_unparseable_packet_is_unknown_until_named(self):
        data = _webp((b"VP8 ", b"\x00" * 10), (b"XMP ", b"<x>not xmp</x>"))
        self.keep(data, rel="x.webp")
        self.assertIn("xmp:unknown", self.scan()[0].excerpt)
        self.keep(data, "xmp:unknown", rel="x.webp")
        self.assertEqual([], self.scan())

    def test_xmp_webp_and_raw_profile_read_alike(self):
        raw = ("\nxmp\n  %d\n" % len(self.xmp)) + self.xmp.hex()
        for rel, data in (
                ("x.webp", _webp((b"VP8 ", b"\x00" * 10), (b"XMP ", self.xmp))),
                ("r.png", _png((b"tEXt", b"Raw profile type xmp\x00" + raw.encode())))):
            with self.subTest(rel):
                one = [self.tmp / rel]
                self.keep(data, "xmp:dc:creator", rel=rel)
                self.assertIn("xmp:exif:GPSLatitude", self.scan(paths=one)[0].excerpt)
                self.keep(data, "xmp:dc:creator,xmp:exif:GPSLatitude", rel=rel)
                self.assertEqual([], self.scan(paths=one))

    def test_xmp_extended_packets_are_joined_before_they_are_read(self):
        half = self.xmp[:len(self.xmp) // 2]
        rest = self.xmp[len(self.xmp) // 2:]
        guid = b"0123456789ABCDEF0123456789ABCDEF"

        def piece(off, body):
            return (ls._XMP_EXT_NS + guid + _struct.pack(">II", len(self.xmp), off) + body)
        data = _jpeg((0xE1, piece(len(half), rest)), (0xE1, piece(0, half)))
        self.keep(data, rel="e.jpg")
        got = self.scan()[0].excerpt
        self.assertIn("xmp:dc:creator", got)
        self.assertNotIn("xmp:unknown", got)

    def test_xmp_a_short_extended_header_is_unknown(self):
        data = _jpeg((0xE1, ls._XMP_EXT_NS + b"short"))
        self.keep(data, rel="e.jpg")
        self.assertIn("xmp:unknown", self.scan()[0].excerpt)

    def test_xmp_text_is_still_scanned_whether_or_not_it_is_kept(self):
        pkt = _xmp(body="<dc:creator>a.b@example.com</dc:creator>")
        self.keep(_webp((b"VP8 ", b"\x00" * 10), (b"XMP ", pkt)), "xmp:dc:creator",
                  rel="x.webp")
        self.assertEqual(["email"], self.rules())

    # -- PNG text ------------------------------------------------------------

    def test_png_text_unkept_keywords_are_named_in_the_block(self):
        self.keep(self.png, rel="t.png")
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertIn("png-text:Author", fs[0].excerpt)
        self.assertIn("png-text:Creation%20Time", fs[0].excerpt)

    def test_png_text_keeping_one_keyword_leaves_the_other_blocking(self):
        self.keep(self.png, "png-text:Author", rel="t.png")
        fs = self.scan()
        self.assertEqual(1, len(fs))
        self.assertIn("png-text:Creation%20Time", fs[0].excerpt)
        self.keep(self.png, "png-text:Author,Creation%20Time", rel="t.png")
        self.assertEqual([], self.scan())

    def test_png_text_compressed_and_international_chunks_are_named_alike(self):
        data = _png((b"zTXt", b"Comment\x00\x00" + _zlib.compress(b"hello")),
                    (b"iTXt", b"Title\x00\x00\x00\x00\x00hello"))
        self.keep(data, "png-text:Comment,Title", rel="t.png")
        self.assertEqual([], self.scan())

    def test_png_text_an_overlong_keyword_is_unknown(self):
        data = _png((b"tEXt", b"x" * 90 + b"\x00v"))
        self.keep(data, rel="t.png")
        self.assertIn("png-text:unknown", self.scan()[0].excerpt)

    def test_png_text_a_keyword_called_unknown_is_not_the_parse_failure(self):
        data = _png((b"tEXt", b"unknown\x00v"))
        self.keep(data, "png-text:unknown", rel="t.png")
        self.assertEqual(["binary-metadata", "binary-stale-entry"], self.rules())
        self.keep(data, "png-text:%75nknown", rel="t.png")
        self.assertEqual([], self.scan())

    def test_png_text_past_the_field_cap_adds_unknown(self):
        chunks = [(b"tEXt", b"k%d\x00v" % i) for i in range(ls._FIELDS_PER_SET_CAP + 5)]
        self.keep(_png(*chunks), rel="t.png")
        self.assertIn("png-text:unknown", self.scan()[0].excerpt)

    # -- type-level lines: accepted with a warning, then refused -------------

    def test_a_type_level_line_warns_naming_the_fields_for_each_set(self):
        for rel, data, whole, want in (
                ("p.jpg", self.jpg, "iptc", ("iptc:By-line", "iptc:City")),
                ("x.webp", _webp((b"VP8 ", b"\x00" * 10), (b"XMP ", self.xmp)), "xmp",
                 ("xmp:dc:creator", "xmp:exif:GPSLatitude")),
                ("t.png", self.png, "png-text",
                 ("png-text:Author", "png-text:Creation%20Time"))):
            with self.subTest(whole):
                one = [self.tmp / rel]
                self.keep(data, whole, rel=rel)
                tally = ls.Tally()
                self.assertEqual([], self.scan(tally=tally, paths=one))
                self.assertEqual(1, len(tally.type_level_warnings))
                w = tally.type_level_warnings[0]
                self.assertEqual(ls.TYPE_LEVEL_RULE, w.rule)
                for k in want:
                    self.assertIn(k, w.excerpt)

    def test_the_warning_prints_with_the_date_and_remedy_and_exits_0(self):
        self.keep(self.jpg, "iptc", rel="p.jpg")
        rc, out, _err = self.run_main(ls.TYPE_LEVEL_UNTIL - _dt.timedelta(days=1))
        self.assertEqual(0, rc, out)
        self.assertIn("WARNING ONLY until " + ls.TYPE_LEVEL_UNTIL.isoformat(), out)
        self.assertIn("iptc:By-line", out)
        self.assertIn("name the fields instead", out)

    def test_from_the_cutoff_each_type_level_line_stops_keeping_its_set(self):
        for rel, data, whole in (("p.jpg", self.jpg, "iptc"),
                                 ("x.webp", _webp((b"VP8 ", b"\x00" * 10),
                                                  (b"XMP ", self.xmp)), "xmp"),
                                 ("t.png", self.png, "png-text")):
            with self.subTest(whole):
                for old in self.tmp.glob("*.*"):
                    old.unlink()
                self.keep(data, whole, rel=rel)
                rc, out, _err = self.run_main(ls.TYPE_LEVEL_UNTIL)
                self.assertEqual(1, rc, out)
                self.assertIn("no longer keeps it", out)
                self.assertIn(f"{whole}:", out)

    def test_icc_and_jpeg_comments_keep_their_type_level_lines_for_good(self):
        data = _png((b"iCCP", b"p\x00\x00" + _zlib.compress(b"profile")))
        self.keep(data, "icc", rel="i.png")
        with _on(ls.TYPE_LEVEL_UNTIL + _dt.timedelta(days=400)):
            self.assertEqual([], self.scan())

    # -- the manifest grammar --------------------------------------------------

    def _refused(self, scope, needle):
        d = _sha(b"x")
        self.manifest(f"{d}  a.png  # ok\n{d}:{scope}  a.png  # need\n")
        with self.assertRaises(ls.BinaryManifestError) as cm:
            ls.load_binary_manifest(self.tmp)
        self.assertIn(needle, str(cm.exception))

    def test_scope_grammar_for_the_new_sets_is_strict(self):
        self._refused("iptc:Byline", "unknown iptc field Byline")
        self._refused("iptc:By-line,By-line", "list each metadata set once")
        self._refused("iptc:City,iptc", "already keeps")
        self._refused("xmp:creator", "unknown xmp field creator")
        self._refused("xmp:dc:creator,dc:title", "write each xmp field in full")
        self._refused("xmp:dc:creator,title", "write each xmp field in full")
        self._refused("png-text:Creation%2", "unknown png-text field")
        self._refused("png-text:a:b", "unknown png-text field")
        self._refused("xmp,xmp:dc:creator", "already keeps")

    def test_scope_grammar_accepts_the_documented_forms(self):
        for scope, want in (
                ("iptc:By-line,City,2:250", ["iptc:By-line", "iptc:City", "iptc:2:250"]),
                ("iptc:2:080,2:090", ["iptc:2:080", "iptc:2:090"]),
                ("iptc:8BIM-0x03ED,iptc:unknown", ["iptc:8BIM-0x03ED", "iptc:unknown"]),
                ("xmp:dc:creator,xmp:exif:GPSLatitude",
                 ["xmp:dc:creator", "xmp:exif:GPSLatitude"]),
                ("xmp:dc:creator,exif:Make", ["xmp:dc:creator", "exif:Make"]),
                ("png-text:Author,Creation%20Time",
                 ["png-text:Author", "png-text:Creation%20Time"]),
                ("png-text:Author,icc", ["png-text:Author", "icc"]),
                ("exif:Model,iptc:City,xmp:dc:title,png-text:Title",
                 ["exif:Model", "iptc:City", "xmp:dc:title", "png-text:Title"])):
            with self.subTest(scope):
                self.assertEqual((want, None), ls.parse_scope(scope))

    def test_a_manifest_line_with_dots_and_percents_loads(self):
        data = _png((b"tEXt", b"Creation Time\x00v"), (b"tEXt", b"a.b\x00v"))
        self.keep(data, "png-text:Creation%20Time,a.b", rel="t.png")
        self.assertEqual([], self.scan())

    # -- --binary-entries and names-only output --------------------------------

    def listing(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = ls.main(["--root", str(self.tmp), "--binary-entries"])
        return rc, out.getvalue(), err.getvalue()

    def test_the_listing_prints_one_line_per_field_for_each_set(self):
        self.put("p.jpg", self.jpg)
        self.put("t.png", self.png)
        self.put("x.webp", _webp((b"VP8 ", b"\x00" * 10), (b"XMP ", self.xmp)))
        rc, out, _err = self.listing()
        self.assertEqual(0, rc)
        for k in ("iptc:By-line", "iptc:City", "png-text:Author",
                  "png-text:Creation%20Time", "xmp:dc:creator", "xmp:exif:GPSLatitude"):
            self.assertTrue(any(f":{k}  " in line for line in out.splitlines()), k)

    def test_the_listing_migrates_a_type_level_line(self):
        self.keep(self.jpg, "iptc", rel="p.jpg")
        d = _sha(self.jpg)
        rc, out, err = self.listing()
        self.assertEqual(0, rc)
        self.assertIn(f"{d}:iptc:By-line  p.jpg", _bare(out).splitlines())
        self.assertIn("type-level line for iptc", err)

    def test_listing_lines_load_once_given_reasons(self):
        self.put("t.png", self.png)
        d = _sha(self.png)
        self.manifest(f"{d}  t.png  # synthetic\n"
                      f"{d}:png-text:Author,Creation%20Time  t.png  # the credit line\n")
        self.assertEqual([], self.scan())
        self.assertEqual("", self.listing()[1])

    def test_no_value_reaches_any_output(self):
        self.keep(self.jpg, rel="p.jpg")
        self.put("x.png", _png((b"iTXt", b"XML:com.adobe.xmp\x00\x00\x00\x00\x00" + self.xmp)))
        self.put("t.png", self.png)
        for extra in ((), ("--json",)):
            rc, out, err = self.run_main(ls.TYPE_LEVEL_UNTIL, *extra)
            self.assertNotIn(self.SECRET, out + err)
            self.assertNotIn("41,24N", out + err)
        rc, out, err = self.listing()
        self.assertNotIn(self.SECRET, out + err)


class BinaryGitTracking(_TreeCase):
    """In a git work tree the gate covers what git tracks (the ruling's word);
    an untracked binary is counted, never silently skipped."""

    def git(self, *args):
        _subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid",
                         "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false",
                         *args], cwd=self.tmp, check=True, capture_output=True)

    def setUp(self):
        super().setUp()
        self.git("init", "-q")

    def test_untracked_binary_is_counted_not_gated(self):
        self.put(".DS_Store", b"\x00\x00\x00\x01Bud1")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual(1, tally.binaries_untracked)

    def test_tracked_binary_is_gated(self):
        self.put("img.bin", b"\x00tracked")
        self.git("add", "img.bin")
        self.assertEqual(["binary-unlisted"], self.rules())

    def test_entry_for_an_untracked_file_is_stale(self):
        data = self.put("img.bin", b"\x00untracked")
        self.manifest(f"{_sha(data)}  img.bin  # reviewed fixture\n")
        fs = self.scan()
        self.assertEqual(["binary-stale-entry"], [f.rule for f in fs])
        self.assertIn("not tracked", fs[0].excerpt)

    # --- the staged plane (the pre-commit hook) -----------------------------

    def staged(self, day=_CUTOFF):
        # In-process, so the date can be patched; `--staged` reads git from
        # the working directory, hence the chdir.
        out, err = io.StringIO(), io.StringIO()
        with _chdir(self.tmp), _on(day), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = ls.main(["--staged", "--root", ".", "--terms", str(self.terms)])
        return rc, out.getvalue() + err.getvalue()

    def test_staged_binary_blocks_and_its_name_is_now_read(self):
        # Before G3 the staged plane never saw a binary at all — not even the
        # leak in its name (git's diff prints no `+++` line for it).
        self.put("10.1.2.3.bin", b"\x00\x01")
        self.git("add", ".")
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("binary-unlisted", out)
        self.assertIn("ipv4", out)

    def test_staged_listed_binary_passes(self):
        data = self.put("ok.bin", b"\x00\x01ok")
        self.manifest(f"{_sha(data)}  ok.bin  # reviewed fixture\n")
        self.git("add", ".")
        rc, out = self.staged()
        self.assertEqual(0, rc, out)
        self.assertIn(f"1 binary file(s) by {ls.BINARY_MANIFEST}", out)

    def test_staged_check_reads_the_index_copy_not_the_working_tree(self):
        data = self.put("ok.bin", b"\x00\x01ok")
        self.manifest(f"{_sha(data)}  ok.bin  # reviewed fixture\n")
        self.put("ok.bin", b"\x00\x01changed after listing")
        self.git("add", "ok.bin", ls.BINARY_MANIFEST)
        self.put("ok.bin", data)  # working tree restored; the INDEX holds the change
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("binary-changed", out)

    def test_staged_removal_of_a_listed_binary_flags_the_stale_entry(self):
        data = self.put("old.bin", b"\x00\x01old")
        self.manifest(f"{_sha(data)}  old.bin  # reviewed fixture\n")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "seed")
        self.git("rm", "-q", "old.bin")
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("binary-stale-entry", out)

    def test_staged_pure_rename_has_its_new_name_read(self):
        self.put("a.md", "text\n")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "seed")
        self.git("mv", "a.md", "10.1.2.3.md")
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("ipv4", out)

    def test_staged_unlisted_binary_warns_before_the_cutoff_and_blocks_after(self):
        # The hook plane honours the same G3 grace, on the same date.
        self.put("img.bin", b"\x00\x01staged")
        self.git("add", ".")
        rc, out = self.staged(_BEFORE)
        self.assertEqual(0, rc, out)
        self.assertIn(f"blocks from {_CUTOFF}", out)
        rc, out = self.staged(_CUTOFF)
        self.assertEqual(1, rc, out)

    def test_staged_text_hidden_by_a_binary_attribute_is_read(self):
        self.put(".gitattributes", "*.cfg binary\n")
        self.put("app.cfg", "owner a.b@example.com\n")
        self.git("add", ".")
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("email", out)

    def test_staged_empty_new_file_has_its_name_read(self):
        # 160/800 SX5: no added line, so the diff names no path for it.
        self.put("10.1.2.3.md", "")
        self.git("add", ".")
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("ipv4", out)

    def test_staged_typechange_has_its_name_and_body_read(self):
        # 160/800 SX3 and SX5: a regular file that replaces a symlink is a
        # typechange to git, which `ACMR` filters showed to no plane.
        os.symlink("elsewhere", self.tmp / "10.1.2.3.md")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "seed")
        (self.tmp / "10.1.2.3.md").unlink()
        self.put("10.1.2.3.md", "owner a.b@example.com\n")
        self.git("add", ".")
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("ipv4", out)
        self.assertIn("email", out)

    def test_staged_text_hidden_by_a_diff_attribute_is_read_once(self):
        # The reader now re-reads such a file with `--text`; the gate already
        # scans the whole staged copy, so the same line is not reported twice.
        self.put(".gitattributes", "*.cfg -diff\n")
        self.put("app.cfg", "owner a.b@example.com\n")
        self.git("add", ".")
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertEqual(1, out.count("app.cfg:1"), out)

    def test_a_line_separator_before_a_hit_keeps_the_finding_at_its_line(self):
        # 160/830 RN1: unlike conflictscan, leakscan's structural rules are
        # not anchored to column 0, so a separator inside a line moves nothing
        # but the number, and the number is the file's.
        for sep in ("\x0c", "\x0b", "\x85", "\u2028", "\r"):
            with self.subTest(sep=repr(sep)):
                name = "s%d.md" % ord(sep)
                (self.tmp / name).write_bytes(
                    f"one\ntwo{sep}10.1.2.3\n".encode())
                self.git("add", name)
                rc, out = self.staged()
                self.assertEqual(1, rc, out)
                self.assertIn(f"{name}:2", out)
                self.git("rm", "-q", "--cached", name)

    def test_staged_manifest_an_unstaged_manifest_edit_does_not_excuse_a_staged_binary(self):
        data = self.put("ok.bin", b"\x00\x01ok")
        self.git("add", "ok.bin")
        self.manifest(f"{_sha(data)}  ok.bin  # reviewed fixture\n")     # never staged
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("binary-unlisted", out)
        self.assertIn("not staged", out)


    def test_staged_manifest_a_staged_manifest_excuses_it_whatever_the_working_copy_says(self):
        data = self.put("ok.bin", b"\x00\x01ok")
        self.manifest(f"{_sha(data)}  ok.bin  # reviewed fixture\n")
        self.git("add", ".")
        self.manifest("")                                  # working copy emptied after staging
        rc, out = self.staged()
        self.assertEqual(0, rc, out)
        self.assertIn("differs from its staged copy", out)


    def test_staged_manifest_a_staged_removal_of_the_manifest_leaves_no_entries(self):
        data = self.put("ok.bin", b"\x00\x01ok")
        self.manifest(f"{_sha(data)}  ok.bin  # reviewed fixture\n")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "seed")
        self.git("rm", "-q", "--cached", ls.BINARY_MANIFEST)
        self.put("ok.bin", b"\x00\x01ok changed")
        self.git("add", "ok.bin")
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("binary-unlisted", out)


    def test_staged_glob_a_staged_binary_under_a_glob_is_gated(self):
        self.put(".leakscanignore", "vendor/  # third-party files, not ours\n")
        self.put("vendor/f.woff", b"\x00\x01staged font")
        self.git("add", ".")
        rc, out = self.staged()
        self.assertEqual(1, rc, out)
        self.assertIn("binary-unlisted", out)


    def test_staged_glob_text_under_the_glob_is_still_skipped(self):
        self.put(".leakscanignore", "vendor/  # third-party files, not ours\n")
        self.put("vendor/notes.txt", "contact a.b@example.com\n")   # leakscan:allow: fixture
        self.git("add", ".")
        rc, out = self.staged()
        self.assertEqual(0, rc, out)


    def test_staged_glob_a_listed_binary_under_a_glob_passes(self):
        data = self.put("vendor/f.woff", b"\x00\x01staged font")
        self.put(".leakscanignore", "vendor/  # third-party files, not ours\n")
        self.manifest(f"{_sha(data)}  vendor/f.woff  # vendored font, looked at\n")
        self.git("add", ".")
        rc, out = self.staged()
        self.assertEqual(0, rc, out)


class BinaryEntriesListing(_TreeCase):
    """`--binary-entries` — the one-act re-baseline: it prints the lines, a
    person writes the reason, and the scan refuses the file until they do."""

    def listing(self):
        import contextlib, io
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = ls.main(["--root", str(self.tmp), "--binary-entries"])
        return rc, out.getvalue(), err.getvalue()

    # The listing's who/when depends on the session id; outside a session it
    # prints by=CHOOSE, which refuses before the reason rule this test pins.
    @unittest.mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "abcd1234"})
    def test_lines_print_without_a_reason_and_need_one_to_load(self):
        a = self.put("a.bin", b"\x00a")
        b = self.put("b.png", _png((b"eXIf", b"MM")))
        rc, out, err = self.listing()
        self.assertEqual(0, rc)
        self.assertEqual(sorted(_bare(out).splitlines()),
                         sorted([f"{_sha(a)}  a.bin", f"{_sha(b)}  b.png",
                                 f"{_sha(b)}:exif:unknown  b.png"]))
        self.assertNotIn("#", _bare(out))
        self.assertIn("exif:unknown", err)
        self.manifest(out)
        with self.assertRaises(ls.BinaryManifestError):
            self.scan()
        # One comment over every line is one blanket reason: refused, because
        # the exif line's need must be its own (Mike, 2026-10-18).
        self.manifest("# synthetic fixtures, reviewed\n" + out)
        with self.assertRaises(ls.BinaryManifestError) as cm:
            self.scan()
        self.assertIn("needs its own reason", str(cm.exception))
        self.manifest("".join(
            line + ("  # test fixture needs its exif block\n" if ":" in line
                    else "  # synthetic fixture, reviewed\n")
            for line in _bare(out).splitlines()))
        self.assertEqual([], self.rules())

    def test_only_unaccepted_files_are_listed_and_a_change_is_named(self):
        a = self.put("a.bin", b"\x00a")
        self.manifest(f"{_sha(a)}  a.bin  # reviewed\n")
        self.assertEqual("", self.listing()[1])
        self.put("a.bin", b"\x00a2")
        _rc, out, err = self.listing()
        self.assertIn("a.bin", out)
        self.assertIn("replaces line 1", err)

    def test_refuses_json(self):
        self.assertEqual(2, ls.main(["--root", str(self.tmp), "--binary-entries", "--json"]))


class BinaryGrace(_TreeCase):
    """The G3 adoption grace (Mike's answer on 020/150, 2026-10-18): before
    `BINARY_GRACE_UNTIL` the four gate rules warn, naming the date and the
    remedy, and do not fail the exit code; on and after it they block. Every
    other rule is untouched by it."""

    BLOB = b"\x00\x01 grace fixture"

    def run_main(self, day, *extra):
        out, err = io.StringIO(), io.StringIO()
        with _on(day), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = ls.main(["--root", str(self.tmp), str(self.tmp),
                          "--terms", str(self.terms), *extra])
        return rc, out.getvalue(), err.getvalue()

    def test_the_cutoff_is_one_iso_date_and_grace_is_strictly_before_it(self):
        self.assertIsInstance(_CUTOFF, _dt.date)
        self.assertTrue(ls.in_binary_grace(_BEFORE))
        self.assertFalse(ls.in_binary_grace(_CUTOFF))
        self.assertFalse(ls.in_binary_grace(_CUTOFF + _dt.timedelta(days=400)))

    def test_before_the_cutoff_an_unlisted_binary_warns_and_exits_0(self):
        self.put("img.bin", self.BLOB)
        rc, out, _err = self.run_main(_BEFORE)
        self.assertEqual(0, rc, out)
        warn = [l for l in out.splitlines() if "binary-unlisted" in l]
        self.assertEqual(1, len(warn), out)
        self.assertIn(_CUTOFF.isoformat(), warn[0])
        self.assertIn("--binary-entries", warn[0])
        self.assertIn("WARNING ONLY", out)
        self.assertIn(f"1 G3 finding(s) warned, not blocking, before {_CUTOFF}", out)
        self.assertIn(f"block from {_CUTOFF}", out)

    def test_on_the_cutoff_the_same_tree_blocks(self):
        self.put("img.bin", self.BLOB)
        rc, out, _err = self.run_main(_CUTOFF)
        self.assertEqual(1, rc, out)
        self.assertNotIn("WARNING ONLY", out)
        self.assertIn("binary-unlisted", out)
        self.assertIn(f"0 G3 finding(s) warned, not blocking, before {_CUTOFF}", out)

    def test_every_gate_rule_is_graced_and_names_its_remedy(self):
        self.put("changed.bin", self.BLOB + b"!")
        self.put("meta.png", _png((b"eXIf", b"MM\x00\x2a")))
        self.manifest(f"{_sha(self.BLOB)}  changed.bin  # reviewed fixture\n"
                      f"{_sha(self.BLOB)}  gone.bin  # was a fixture\n")
        rc, out, _err = self.run_main(_BEFORE)
        self.assertEqual(0, rc, out)
        for rule, remedy in (("binary-changed", "--binary-entries"),
                             ("binary-metadata", "strip the set"),
                             ("binary-unlisted", "--binary-entries"),
                             ("binary-stale-entry", "delete or re-path")):
            lines = [l for l in out.splitlines() if f"] {rule} →" in l]
            self.assertTrue(lines, f"{rule} missing:\n{out}")
            for l in lines:
                self.assertIn(f"blocks from {_CUTOFF}", l)
                self.assertIn(remedy, l)
        self.assertEqual(1, self.run_main(_CUTOFF)[0])

    def test_non_binary_rules_are_untouched_by_the_grace(self):
        self.put("notes.md", "write to a.b@example.com\n")
        rc, out, _err = self.run_main(_BEFORE)
        self.assertEqual(1, rc, out)
        self.assertIn("email", out)

    def test_a_text_metadata_hit_still_blocks_during_the_grace(self):
        # The hit is an ordinary rule's (email), read out of the image: it is
        # what the scan already did, so the grace does not reach it.
        data = _png((b"tEXt", b"Author\x00a.b@example.com"))
        self.put("i.png", data)
        rc, out, _err = self.run_main(_BEFORE)
        self.assertEqual(1, rc, out)
        blocking = out.split("commit blocked.")[1]
        self.assertIn("email", blocking)
        self.assertNotIn("binary-unlisted →", blocking)

    def test_json_keeps_graced_findings_out_of_the_blocking_list(self):
        self.put("img.bin", self.BLOB)
        rc, out, _err = self.run_main(_BEFORE, "--json")
        self.assertEqual(0, rc)
        doc = json.loads(out)
        self.assertTrue(doc["clean"])
        self.assertEqual([], doc["findings"])
        self.assertEqual({"until": _CUTOFF.isoformat(), "active": True},
                         {k: doc["binary_grace"][k] for k in ("until", "active")})
        self.assertEqual(["leakscan:binary-unlisted"],
                         [w["id"] for w in doc["binary_grace"]["warnings"]])
        rc, out, _err = self.run_main(_CUTOFF, "--json")
        self.assertEqual(1, rc)
        doc = json.loads(out)
        self.assertFalse(doc["binary_grace"]["active"])
        self.assertEqual(["binary-unlisted"], [f["rule"] for f in doc["findings"]])

    def test_no_command_line_route_moves_the_cutoff(self):
        # Nothing to pass, so nothing a child's floor overrides could pass.
        for argv in (["--grace-until", "2099-01-01"], ["--grace"], ["--today", "2026-01-01"]):
            with self.subTest(argv=argv), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as cm:
                    ls.main(["--root", str(self.tmp), *argv])
                self.assertEqual(2, cm.exception.code)


class BinaryNamedSets(_TreeCase):
    """Per-set acceptance: an entry names every metadata set it keeps, one or
    several to a line under the need for exactly those sets (020/440); a set
    present and not named blocks,
    naming the set. All images are synthetic, built from bytes here."""

    ICC = _zlib.compress(b"synthetic colour profile bytes")

    def png_icc(self, *extra):
        return _png((b"iCCP", b"test profile\x00\x00" + self.ICC), *extra)

    def keep(self, rel, data, *sets, file_reason="synthetic image, reviewed"):
        self.put(rel, data)
        d = _sha(data)
        self.manifest(f"{d}  {rel}  # {file_reason}\n"
                      + "".join(f"{d}:{s}  {rel}  # needs {s} for this test\n"
                                for s in sets))

    def test_inspect_media_names_each_set(self):
        import io as _io
        cases = {
            "icc": [self.png_icc(),
                    _jpeg((0xE2, b"ICC_PROFILE\x00\x01\x01" + self.ICC)),
                    _webp((b"VP8X", bytes(10)), (b"ICCP", self.ICC))],
            "exif": [_png((b"eXIf", b"MM\x00\x2a"))],
            "iptc": [_jpeg((0xED, b"Photoshop 3.0\x008BIM")),
                     _png((b"tEXt", b"Raw profile type iptc\x00\n  4\n1c02"))],
            "xmp": [_png((b"iTXt", b"XML:com.adobe.xmp\x00\x00\x00\x00\x00<x/>"))],
            "png-text": [_png((b"tEXt", b"Title\x00a diagram"))],
            "jpeg-comment": [_jpeg((0xFE, b"a comment"))],
            "unknown": [_jpeg((0xE1, b"NotExif\x00")), _png()[:-12]],
        }
        for want, images in cases.items():
            for data in images:
                with self.subTest(set=want, head=data[:4]):
                    _f, _t, found = ls.inspect_media(_io.BytesIO(data))
                    self.assertEqual([want], list(ls.metadata_sets(found)))
        self.assertEqual(set(ls.METADATA_SETS), set(cases))

    def test_naming_only_icc_passes_an_icc_only_image(self):
        self.keep("c.png", self.png_icc(), "icc")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual(1, tally.binaries_by_manifest)

    def test_naming_only_icc_blocks_an_image_that_also_carries_exif(self):
        data = self.png_icc((b"eXIf", b"MM\x00\x2a"))
        self.keep("c.png", data, "icc")
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertTrue(fs[0].excerpt.startswith("exif:"), fs[0].excerpt)
        self.assertNotIn("icc", fs[0].excerpt)

    def test_an_unkept_icc_profile_blocks_too(self):
        self.keep("c.png", self.png_icc())
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertTrue(fs[0].excerpt.startswith("icc:"))

    def test_each_missing_set_is_its_own_finding(self):
        data = _jpeg((0xE1, b"Exif\x00\x00MM"), (0xED, b"Photoshop 3.0\x008BIM"),
                     (0xFE, b"plain"))
        self.keep("p.jpg", data, "jpeg-comment")
        self.assertEqual(["exif", "iptc"],
                         sorted(f.excerpt.split(":")[0] for f in self.scan()))

    def test_a_set_the_file_lacks_is_a_stale_line(self):
        # Chosen: stale, so blocking (warning during the grace). The digest
        # binds the bytes, so the line was wrong when written; and a line per
        # set "just in case" is the blanket acceptance the answer forbids.
        data = self.png_icc()
        self.keep("c.png", data, "icc", "exif")
        fs = self.scan()
        self.assertEqual(["binary-stale-entry"], [f.rule for f in fs])
        self.assertEqual((ls.BINARY_MANIFEST, 3), (fs[0].path, fs[0].line))
        self.assertIn("keeps exif, which these bytes do not carry", fs[0].excerpt)

    def test_one_reason_may_keep_several_named_sets(self):
        data = self.png_icc((b"eXIf", b"MM\x00\x2a"))
        d = _sha(data)
        self.put("m.png", data)
        # Both sets named under one reason: the image passes.
        self.manifest(f"{d}  m.png  # product photo, reviewed\n"
                      f"{d}:exif,icc  m.png  # print shop needs the camera "
                      "profile and colour profile\n")
        self.assertEqual([], self.rules())
        # Name only one: the other still blocks, by name.
        self.manifest(f"{d}  m.png  # product photo, reviewed\n"
                      f"{d}:icc  m.png  # print colour\n")
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertIn("exif", fs[0].excerpt)

    def test_kept_text_sets_are_still_scanned(self):
        self.keep("t.png", _png((b"tEXt", b"Author\x00a.b@example.com")), "png-text")
        self.assertEqual(["email"], self.rules())

    def _refused(self, text, needle):
        self.manifest(text)
        with self.assertRaises(ls.BinaryManifestError) as cm:
            ls.load_binary_manifest(self.tmp)
        self.assertIn(needle, str(cm.exception))

    def test_set_line_grammar_is_strict(self):
        d = _sha(b"x")
        e = _sha(b"y")
        self._refused(f"{d}:icc  a.png  # colour accuracy\n", "no file line")
        self._refused(f"{d}  a.png  # ok\n{d}:icc,icc  a.png  # twice\n",
                      "list each metadata set once")
        self._refused(f"{d}  a.png  # ok\n{d}:icc,  a.png  # trailing comma\n",
                      "list each metadata set once")
        self._refused(f"{d}  a.png  # ok\n{d}:icc,colour  a.png  # colour\n",
                      "unknown metadata set colour")
        self._refused(f"{d}  a.png  # ok\n{d}:icc  a.png  # colour\n"
                      f"{d}:exif,icc  a.png  # again\n", "icc in 'a.png' already kept at line 2")
        self._refused(f"{d}  a.png  # ok\n{e}:icc  a.png  # colour\n",
                      "different digest")
        self._refused(f"{d}  a.png  # ok\n{d}:icc  a.png  # colour\n"
                      f"{d}:icc  a.png  # again\n", "already kept at line 2")
        self._refused(f"{d}:binary-metadata  a.png  # the old scope\n",
                      "unknown metadata set binary-metadata")
        self._refused(f"{d}  a.png  # ok\n{d}:icc  a.png\n",
                      "keeping icc in 'a.png' has no stated reason")

    def test_the_files_own_reason_cannot_stand_for_its_metadata(self):
        d = _sha(b"x")
        self._refused(f"# logo, reviewed\n{d}  a.png\n{d}:icc  a.png\n",
                      "needs its own reason")
        self._refused(f"# logo, reviewed\n{d}  a.png\n{d}:icc,exif  a.png\n",
                      "repeats the file line 2's")
        # Mike, 2026-10-19 (020/440): one specific reason may cover several
        # named sets, on one line or shared by two lines.
        self.manifest(f"{d}  a.png  # ok\n{d}:icc  a.png  # print colour\n"
                      f"{d}:exif  a.png  # print colour\n")
        self.assertEqual({"icc", "exif"},
                         set(ls.load_binary_manifest(self.tmp)["a.png"].sets))
        # The same need for the same set in two files is not a blanket.
        self.manifest(f"{d}  a.png  # a\n{d}:icc  a.png  # brand colours\n"
                      f"{d}  b.png  # b\n{d}:icc  b.png  # brand colours\n")
        self.assertEqual({"a.png", "b.png"}, set(ls.load_binary_manifest(self.tmp)))

    def test_binary_entries_prints_reasonless_per_set_lines(self):
        data = self.png_icc((b"eXIf", b"MM\x00\x2a"))
        self.put("c.png", data)
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(0, ls.main(["--root", str(self.tmp), "--binary-entries"]))
        d = _sha(data)
        self.assertEqual([f"{d}  c.png", f"{d}:exif:unknown  c.png", f"{d}:icc  c.png"],
                         _bare(out.getvalue()).splitlines())
        self.assertIn("strip every set or field you have no need for", err.getvalue())

    def test_binary_entries_lists_only_the_sets_still_missing(self):
        data = self.png_icc((b"eXIf", b"MM\x00\x2a"))
        self.keep("c.png", data, "icc")
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            ls.main(["--root", str(self.tmp), "--binary-entries"])
        self.assertEqual([f"{_sha(data)}:exif:unknown  c.png"],
                         _bare(out.getvalue()).splitlines())



# ===========================================================================
# 115/090 — rules that are OFF report without blocking.
#
# CONTRACT: Mike's answer (2026-10-16, "Report-only for off rules") lifted the
# EI6 ruling for rules that are off and nothing else: NOTHING THAT BLOCKS
# TODAY STOPS BLOCKING. `BlockingSetPinned` enumerates the rules that blocked
# when the answer was built and asserts each still blocks. A rule leaving this
# list, or one of them starting to report, is a narrowing of the personal-data
# boundary and is the principal's decision (SECRETS.md § The boundary's
# posture), never an edit to make this suite green. Adding a rule is welcome.
# Every fixture is synthetic.
# ===========================================================================
BLOCKING_AT_115_090 = (
    ("private-key-header", "-----BEGIN RSA PRIVATE KEY-----"),
    ("aws-access-key-id", "key AKIAABCDEFGHIJKLMNOP here"),
    ("jwt", "tok eyJhbGciOiJI.eyJzdWIiOiIx.abcdefghij"),
    ("email", "mail jane.doe@example.org now"),
    ("pii-key-context", "dob = 1984-02-29"),
    ("payment-card", "card 4111111111111111 on file"),
    ("iban", "iban GB82WEST12345698765432 x"),
    ("mac-address", "mac aa:bb:cc:dd:ee:ff end"),
    ("ipv4", "gateway 172.16.31.7 is the igw"),
    ("ipv6", "uplink fd00:1234:5678::abcd up"),
    ("nz-bank-account", "acct 12-3456-1234567-00 ok"),
    ("nz-phone", "call 021 123 4567"),
    ("nz-address", "at 12 Cuba Street"),
    ("coordinates", "loc -41.2865, 174.7762 pin"),
    ("nz-ird", "ird 123-456-789 x"),
)
TERM = ("zzzterm", re.compile(r"\bzzzterm\b", re.IGNORECASE))


class BinaryProvenance(_TreeCase):
    """160/980 GM5 (Mike's answer, 2026-11-08): each `.leakscanbinaries` line
    records WHO allowed it and WHEN, per his 2026-10-03 words, not a reason
    alone. A line written before the form existed still loads and WARNS."""

    BLOB = b"\x00provenance fixture"
    PROV = "by=agent session=0123abcd-4567 on=2026-11-09"

    def write(self, text):
        self.put("a.bin", self.BLOB)
        self.manifest(text)
        return ls.load_binary_manifest(self.tmp)

    def test_a_trailing_note_records_who_and_when_apart_from_the_reason(self):
        e = self.write(f"{_sha(self.BLOB)}  a.bin  # {self.PROV} our own diagram\n")["a.bin"]
        self.assertEqual(ls.Provenance("agent", "0123abcd-4567", "2026-11-09"), e.prov)
        self.assertEqual("our own diagram", e.reason)

    def test_the_stanza_may_carry_either_or_both(self):
        d = _sha(self.BLOB)
        e = self.write(f"# our own diagram, looked at\n{d}  a.bin  # {self.PROV}\n")["a.bin"]
        self.assertEqual("our own diagram, looked at", e.reason)
        self.assertEqual("agent", e.prov.by)
        e = self.write(f"# {self.PROV}\n{d}  a.bin  # our own diagram\n")["a.bin"]
        self.assertEqual("our own diagram", e.reason)
        self.assertEqual("0123abcd-4567", e.prov.session)

    def test_who_and_when_alone_are_not_a_reason(self):
        d = _sha(self.BLOB)
        for text in (f"{d}  a.bin  # {self.PROV}\n", f"# {self.PROV}\n{d}  a.bin\n"):
            with self.subTest(text), self.assertRaises(ls.BinaryManifestError) as cm:
                self.write(text)
            self.assertIn("no stated reason", str(cm.exception))

    def test_a_principal_kind_and_a_human_session_parse(self):
        d = _sha(self.BLOB)
        for kind in ("principal-ruled", "principal-answer", "agent"):
            e = self.write(f"{d}  a.bin  # by={kind} session=human on=2026-11-09 fine\n")
            self.assertEqual((kind, "human"), (e["a.bin"].prov.by, e["a.bin"].prov.session))

    def test_a_who_and_when_that_does_not_read_is_a_config_error_not_a_pass(self):
        d = _sha(self.BLOB)
        for why, note in (("by=agent on=2026-11-09", "incomplete who/when"),
                          ("by=robot session=human on=2026-11-09", "not a kind of grant"),
                          ("by=agent session=x on=2026-11-09", "not a session id"),
                          ("by=agent session=human on=2026-13-45", "not a YYYY-MM-DD date"),
                          ("by=CHOOSE session=human on=2026-11-09", "not a kind of grant")):
            with self.subTest(why), self.assertRaises(ls.BinaryManifestError) as cm:
                self.write(f"{d}  a.bin  # {why} the reason\n")
            self.assertIn(note, str(cm.exception))

    def test_the_blanket_check_compares_reasons_not_who_and_when(self):
        # One stanza over a file line and its set line is one blanket reason
        # even though both lines now also carry a who/when.
        data = _png((b"iCCP", b"p\x00\x00" + _zlib.compress(b"x")))
        self.put("c.png", data)
        d = _sha(data)
        self.manifest(f"# one reason for all\n{d}  c.png  # {self.PROV}\n"
                      f"{d}:icc  c.png  # {self.PROV}\n")
        with self.assertRaises(ls.BinaryManifestError) as cm:
            ls.load_binary_manifest(self.tmp)
        self.assertIn("needs its own reason", str(cm.exception))

    # -- the old, reason-only line: a clear warning, never a silent pass ----

    def test_a_reason_only_line_still_loads_and_warns_by_line(self):
        data = _png((b"iCCP", b"p\x00\x00" + _zlib.compress(b"x")))
        self.put("c.png", data)
        d = _sha(data)
        self.manifest(f"{d}  c.png  # our own logo\n{d}:icc  c.png  # brand colours\n")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))     # does not block
        self.assertEqual([1, 2], [w.line for w in tally.provenance_warnings])
        self.assertEqual(ls.PROVENANCE_RULE, tally.provenance_warnings[0].rule)
        self.assertIn("2 manifest line(s) with no who/when warned, not blocking",
                      tally.summary())

    def test_a_line_that_records_who_and_when_does_not_warn(self):
        self.put("a.bin", self.BLOB)
        self.manifest(f"{_sha(self.BLOB)}  a.bin  # {self.PROV} reviewed\n")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual([], tally.provenance_warnings)

    def test_the_warning_prints_in_the_run_and_in_json_and_never_moves_the_exit(self):
        self.put("a.bin", self.BLOB)
        self.manifest(f"{_sha(self.BLOB)}  a.bin  # reviewed fixture\n")
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            rc = ls.main(["--root", str(self.tmp), str(self.tmp), "--terms", str(self.terms)])
        self.assertEqual(0, rc, out.getvalue())
        self.assertIn("record a reason but not who allowed them or when", out.getvalue())
        self.assertIn(f"{ls.BINARY_MANIFEST}:1", out.getvalue())
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            rc = ls.main(["--root", str(self.tmp), str(self.tmp), "--terms", str(self.terms),
                          "--json"])
        self.assertEqual(0, rc)
        j = json.loads(out.getvalue())["binary_provenance"]
        self.assertEqual(ls.PROVENANCE_FORM, j["form"])
        self.assertEqual([1], [w["line"] for w in j["warnings"]])

    def test_a_long_list_prints_a_screenful_and_counts_the_rest(self):
        n = ls.PROVENANCE_LIST_CAP + 5
        lines = []
        for i in range(n):
            body = b"\x00body %d" % i
            self.put(f"f{i}.bin", body)
            lines.append(f"{_sha(body)}  f{i}.bin  # fixture {i}\n")
        self.manifest("".join(lines))
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        text = "\n".join(ls.render_provenance(tally.provenance_warnings))
        self.assertEqual(ls.PROVENANCE_LIST_CAP, text.count("[warn]"))
        self.assertIn("…and 5 more, counted but not listed", text)

    # -- the printed lines carry it ---------------------------------------

    def test_the_listing_stub_is_agent_with_the_session_in_a_claude_session(self):
        with unittest.mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "abcd1234-ef"}):
            stub = ls.provenance_stub(_dt.date(2026, 11, 9))
        self.assertEqual("by=agent session=abcd1234-ef on=2026-11-09", stub)

    def test_the_listing_stub_leaves_the_kind_to_a_person(self):
        env = {k: v for k, v in os.environ.items() if k != "CLAUDE_CODE_SESSION_ID"}
        with unittest.mock.patch.dict(os.environ, env, clear=True):
            stub = ls.provenance_stub(_dt.date(2026, 11, 9))
        self.assertEqual("by=CHOOSE session=human on=2026-11-09", stub)
        # ...and the loader refuses it until they choose, and it is no reason.
        self.put("a.bin", self.BLOB)
        self.manifest(f"{_sha(self.BLOB)}  a.bin  # {stub}\n")
        with self.assertRaises(ls.BinaryManifestError) as cm:
            ls.load_binary_manifest(self.tmp)
        self.assertIn("not a kind of grant", str(cm.exception))

    def test_a_printed_line_with_a_reason_added_loads_clean(self):
        self.put("a.bin", self.BLOB)
        out = io.StringIO()
        with unittest.mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "abcd1234-ef"}), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            ls.main(["--root", str(self.tmp), "--binary-entries"])
        line = out.getvalue().strip()
        self.assertIn("# by=agent session=abcd1234-ef on=", line)
        self.manifest(line + " our own fixture, looked at\n")
        tally = ls.Tally()
        self.assertEqual([], self.scan(tally=tally))
        self.assertEqual([], tally.provenance_warnings)


class BinaryManifestPaths(_TreeCase):
    """160/980 GM6: an entry that can match nothing is a config error at load,
    not a line the inventory carries unremarked."""

    def test_absolute_and_climbing_paths_are_refused_at_load(self):
        d = "0123456789abcdef"
        for path in ("/etc/x.bin", "../x.bin", "a/../../x.bin", "a/../x.bin"):
            with self.subTest(path):
                self.manifest(f"{d}  {path}  # reason\n")
                with self.assertRaises(ls.BinaryManifestError) as cm:
                    ls.load_binary_manifest(self.tmp)
                self.assertIn("not a path inside the repo", str(cm.exception))

    def test_a_dot_slash_path_still_loads(self):
        self.manifest("0123456789abcdef  ./a/x.bin  # reason\n")
        self.assertEqual(["a/x.bin"], list(ls.load_binary_manifest(self.tmp)))

    def test_the_run_exits_two_on_one(self):
        self.manifest("0123456789abcdef  /etc/x.bin  # reason\n")
        rc = ls.main(["--root", str(self.tmp), str(self.tmp), "--terms", str(self.terms)])
        self.assertEqual(2, rc)


class RawXmpProfile(_TreeCase):
    """160/980 GM4 (Mike's answer, 2026-11-08): the raw `xmp` profile in a PNG
    is decoded and scanned like every other XMP form, and one the gate cannot
    read is reported UNREADABLE, never as clean."""

    def raw(self, payload_hex, n=0):
        return _png((b"tEXt", b"Raw profile type xmp\x00" + (f"\nxmp\n  {n}\n" + payload_hex).encode()))

    def test_a_raw_profile_xmp_packet_is_text_scanned_kept_or_not(self):
        pkt = _xmp(body="<dc:creator>a.b@example.com</dc:creator>")
        data = self.raw(pkt.hex(), len(pkt))
        self.put("r.png", data)
        self.manifest(f"{_sha(data)}  r.png  # synthetic image, reviewed\n"
                      f"{_sha(data)}:xmp:dc:creator  r.png  # the credit line\n")
        fs = self.scan()
        self.assertEqual(["email"], [f.rule for f in fs])
        self.assertIn("hex-encoded binary profile", fs[0].where)

    def test_the_same_address_is_found_in_every_xmp_form(self):
        pkt = _xmp(body="<dc:creator>a.b@example.com</dc:creator>")
        forms = {"raw.png": self.raw(pkt.hex(), len(pkt)),
                 "x.webp": _webp((b"VP8 ", b"\x00" * 10), (b"XMP ", pkt)),
                 "x.jpg": _jpeg((0xE1, ls._XMP_NS + pkt)),
                 "i.png": _png((b"iTXt", b"XML:com.adobe.xmp\x00\x00\x00\x00\x00" + pkt))}
        for rel, data in forms.items():
            with self.subTest(rel):
                self.put(rel, data)
                fs = ls.scan_paths([self.tmp / rel], self.tmp, [], frozenset())
                self.assertIn("email", [f.rule for f in fs])

    def test_an_undecodable_raw_profile_is_reported_unreadable_and_blocks(self):
        data = self.raw("zz not hex at all")
        self.put("r.png", data)
        self.manifest(f"{_sha(data)}  r.png  # synthetic image, reviewed\n")
        fs = self.scan()
        self.assertEqual(["binary-metadata"], [f.rule for f in fs])
        self.assertIn("UNREADABLE", fs[0].excerpt)
        self.assertIn("xmp:unknown", fs[0].excerpt)
        # Keeping it is a deliberate, named line, and it stays reported.
        self.manifest(f"{_sha(data)}  r.png  # synthetic image, reviewed\n"
                      f"{_sha(data)}:xmp:unknown  r.png  # the profile is a vendor blob\n")
        self.assertEqual([], self.scan())

    def test_an_undecodable_exif_or_iptc_raw_profile_is_unreadable_too(self):
        for kind in ("exif", "iptc"):
            with self.subTest(kind):
                data = _png((b"tEXt", f"Raw profile type {kind}\x00\n{kind}\n  4\nzz".encode()))
                self.put(f"{kind}.png", data)
                self.manifest("")
                fs = [f for f in self.scan() if f.path == f"{kind}.png"]
                self.assertTrue(any("UNREADABLE" in f.excerpt for f in fs), fs)


class _CliCase(unittest.TestCase):
    """A temp tree and an in-process `main`, with a term list kept OUTSIDE the
    tree so the list cannot hit itself."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        cfg = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, cfg, ignore_errors=True)
        self.terms = cfg / "terms.txt"
        self.terms.write_text("zzzterm\n")

    def run_cli(self, text, *argv):
        (self.tmp / "f.txt").write_text(text + "\n")
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = ls.main(["--root", str(self.tmp), str(self.tmp),
                          "--terms", str(self.terms), *argv])
        return rc, out.getvalue()

    def run_json(self, text, *argv):
        rc, out = self.run_cli(text, "--json", *argv)
        return rc, json.loads(out)


class BlockingSetPinned(_CliCase):
    """The blocking set cannot shrink (115/090)."""

    def test_every_rule_that_blocked_is_still_a_blocking_rule(self):
        names = {p.name for p in ls.STRUCTURAL}
        for rule, _text in BLOCKING_AT_115_090:
            self.assertIn(rule, names, f"{rule} left the structural rule set")
            self.assertNotIn(rule, ls.WITHDRAWN_NAMES)
            self.assertTrue(ls.blocks(rule), rule)
        self.assertTrue(ls.blocks("local-term"))
        # A withdrawn rule is a NEW, report-only rule; it never takes the
        # place of one that blocked.
        self.assertFalse(names & ls.WITHDRAWN_NAMES)
        self.assertEqual(set(ls.BINARY_RULES) & ls.WITHDRAWN_NAMES, set())

    def test_every_pinned_rule_blocks_its_fixture(self):
        for rule, text in BLOCKING_AT_115_090:
            with self.subTest(rule=rule):
                fs = scan(text)
                self.assertIn(rule, blocking(fs))
                rc, out = self.run_json(text)
                self.assertEqual(1, rc)
                self.assertIn(rule, {f["rule"] for f in out["findings"]})
                self.assertEqual(0, out["counts"]["advisory"])

    def test_disabling_every_other_rule_leaves_each_one_blocking(self):
        every = [r for r, _t in BLOCKING_AT_115_090]
        for rule, text in BLOCKING_AT_115_090:
            with self.subTest(rule=rule):
                others = ",".join(r for r in every if r != rule)
                rc, out = self.run_json(text, "--disable", others)
                self.assertEqual(1, rc)
                self.assertIn(rule, {f["rule"] for f in out["findings"]})

    def test_the_term_list_blocks_with_every_structural_rule_disabled(self):
        every = ",".join(r for r, _t in BLOCKING_AT_115_090)
        rc, out = self.run_json("zzzterm at 172.16.31.7", "--disable", every)
        self.assertEqual(1, rc)
        self.assertEqual(["local-term"], [f["rule"] for f in out["findings"]])

    def test_a_binary_gate_finding_is_built_blocking(self):
        (self.tmp / "b.bin").write_bytes(b"\x00\x01binary")
        fs = ls.scan_paths([self.tmp], self.tmp, [])
        self.assertTrue(fs)
        self.assertTrue(all(f.blocks for f in fs if f.rule in ls.BINARY_RULES))

    def test_a_finding_that_does_not_say_blocks(self):
        self.assertTrue(ls.Finding("p", 1, "email", "structural", "high", "x").blocks)


class CoverageLine(_CliCase):
    """115/130: the run says how many files it read and how many lines (or
    binaries) a rule evaluated, on the blocked path as on the clean one; the
    exit codes are the ones the same runs already had."""

    def test_a_clean_run_counts_the_file_and_its_lines(self):
        rc, out = self.run_cli("one\ntwo")
        self.assertEqual(0, rc)
        self.assertIn("  coverage: 1 file(s) opened \u00b7 2 line(s)/binary "
                      "file(s) checked", out)
        self.assertNotIn("scanned nothing", out)

    def test_the_blocked_path_prints_it_and_still_exits_1(self):
        rc, out = self.run_cli("gateway 172.16.31.7 here")
        self.assertEqual(1, rc)
        self.assertIn("ipv4", out)
        self.assertIn("  coverage: 1 file(s) opened \u00b7 1 line(s)/binary "
                      "file(s) checked", out)

    def test_a_run_over_an_empty_tree_says_scanned_nothing_and_exits_0(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), \
                contextlib.redirect_stderr(io.StringIO()):
            rc = ls.main(["--root", str(self.tmp), str(self.tmp),
                          "--terms", str(self.terms)])
        self.assertEqual(0, rc)
        self.assertIn("coverage: 0 file(s) opened", out.getvalue())
        self.assertIn("scanned nothing", out.getvalue())

    def test_a_binary_gated_is_not_scanned_nothing(self):
        (self.tmp / "b.bin").write_bytes(b"\x00\x01binary")
        out = io.StringIO()
        with contextlib.redirect_stdout(out), \
                contextlib.redirect_stderr(io.StringIO()):
            ls.main(["--root", str(self.tmp), str(self.tmp),
                     "--terms", str(self.terms)])
        self.assertIn("coverage: 1 file(s) opened \u00b7 1 line(s)/binary "
                      "file(s) checked", out.getvalue())
        self.assertNotIn("scanned nothing", out.getvalue())

    def test_the_staged_plane_counts_the_added_lines(self):
        subprocess.run(["git", "-C", str(self.tmp), "init", "-q"], check=True)
        (self.tmp / "a.md").write_text("one\ntwo\nthree\n")
        subprocess.run(["git", "-C", str(self.tmp), "add", "--", "a.md"],
                       check=True)
        out = io.StringIO()
        old = os.getcwd()
        os.chdir(self.tmp)
        try:
            with contextlib.redirect_stdout(out), \
                    contextlib.redirect_stderr(io.StringIO()):
                rc = ls.main(["--staged", "--root", str(self.tmp),
                              "--terms", str(self.terms)])
        finally:
            os.chdir(old)
        self.assertEqual(0, rc)
        self.assertIn("coverage: 1 file(s) opened \u00b7 3 line(s)/binary "
                      "file(s) checked", out.getvalue())

    def test_json_carries_the_same_coverage(self):
        rc, out = self.run_json("one\ntwo")
        self.assertEqual({"files_opened": 1,
                          "lines_and_binaries_checked": 2,
                          "scanned_nothing": False,
                          "lines_read": 2, "binaries_checked": 0},
                         out["coverage"])


class DisabledClassReports(_CliCase):
    """A class a repo turns off with `--disable` reports without blocking."""

    def test_a_disabled_class_alone_exits_clean_and_is_listed(self):
        rc, out = self.run_cli("gateway 172.16.31.7 here", "--disable", "ipv4")
        self.assertEqual(0, rc)
        self.assertIn("✓ leakscan clean", out)
        self.assertIn("  leakscan advisory: 1 finding(s) — reported, not blocking.", out)
        self.assertIn("🟡 REPORT-ONLY FINDINGS", out)
        self.assertRegex(out, r"f\.txt:1  \[advisory/structural\] ipv4 → .*\[leakscan:ipv4\]")

    def test_json_keeps_blocking_and_report_only_apart(self):
        rc, out = self.run_json("172.16.31.7 and a.b@example.org", "--disable", "ipv4")
        self.assertEqual(1, rc)
        self.assertEqual(["email"], [f["rule"] for f in out["findings"]])
        self.assertEqual(["ipv4"], [f["rule"] for f in out["advisory"]["findings"]])
        self.assertEqual({"blocking": 1, "advisory": 1}, out["counts"])
        self.assertFalse(out["clean"])
        self.assertTrue(out["blocked"])
        self.assertEqual("advisory", out["advisory"]["findings"][0]["response"])

    def test_clean_keeps_its_meaning_on_a_report_only_run(self):
        rc, out = self.run_json("gateway 172.16.31.7 here", "--disable", "ipv4")
        self.assertEqual(0, rc)
        self.assertTrue(out["clean"])
        self.assertFalse(out["blocked"])
        self.assertEqual([], out["findings"])

    def test_the_count_line_prints_its_zero(self):
        rc, out = self.run_cli("nothing here")
        self.assertEqual(0, rc)
        self.assertIn("  leakscan advisory: 0 finding(s) — reported, not blocking.", out)
        self.assertNotIn("REPORT-ONLY", out)

    def test_a_blocking_run_still_counts_report_only_findings(self):
        rc, out = self.run_cli("172.16.31.7 and a.b@example.org", "--disable", "ipv4")
        self.assertEqual(1, rc)
        self.assertIn("✗ leakscan: 1 finding(s) — commit blocked.", out)
        self.assertIn("  leakscan advisory: 1 finding(s) — reported, not blocking.", out)

    def test_a_marker_exempts_a_report_only_hit_and_is_counted(self):
        tally = ls.Tally(disabled_rules=("ipv4",))
        fs = ls.scan_text("t", "172.16.31.7  # leakscan:allow:ipv4: fixture", [],
                          frozenset({"ipv4"}), tally)
        self.assertEqual([], fs)
        self.assertEqual({"ipv4": 1}, tally.by_marker)

    def test_path_names_report_too(self):
        (self.tmp / "host-172.16.31.7.txt").write_text("x\n")
        fs = ls.scan_paths([self.tmp], self.tmp, [], frozenset({"ipv4"}))
        self.assertEqual([("ipv4", "advisory", 0)],
                         [(f.rule, f.response, f.line) for f in fs])

    def test_report_only_findings_past_the_cap_never_move_the_exit_code(self):
        from unittest import mock
        text = "\n".join(f"10.0.0.{i}" for i in range(1, 6))
        with mock.patch.object(ls, "MAX_MATERIALIZED_FINDINGS", 2):
            rc, out = self.run_json(text, "--disable", "ipv4")
        self.assertEqual(0, rc)
        self.assertEqual(0, out["findings_over_cap"])
        self.assertEqual(3, out["advisory"]["over_cap"])
        self.assertEqual({"blocking": 0, "advisory": 5}, out["counts"])

    def test_floor_reads_the_count(self):
        import floor
        _rc, out = self.run_cli("10.0.0.1\n10.0.0.2", "--disable", "ipv4")
        self.assertEqual(2, floor._read_advisory_count(out, "leakscan"))


class WithdrawnRuleReports(_CliCase):
    """A withdrawn rule (the G1 diagnosis key) reports without blocking."""

    def test_the_diagnosis_key_reports(self):
        for text in ("diagnosis: Foobaritis", "Diagnoses = 'Foo-bar'",
                     "patientDiagnosis: Foobaritis"):
            with self.subTest(text=text):
                fs = scan(text)
                self.assertEqual((set(), {"diagnosis-key"}),
                                 (blocking(fs), reporting(fs)))

    def test_placeholders_are_suppressed_as_for_the_key_context_rule(self):
        self.assertEqual([], scan("diagnosis: <redacted>"))
        self.assertEqual([], scan("diagnosis: example"))

    def test_prose_without_a_key_shape_is_not_a_hit(self):
        self.assertEqual([], scan("the diagnosis was a stale cache"))

    def test_it_exits_clean_and_is_counted(self):
        rc, out = self.run_cli("diagnosis: Foobaritis")
        self.assertEqual(0, rc)
        self.assertIn("  leakscan advisory: 1 finding(s) — reported, not blocking.", out)
        self.assertIn("diagnosis-key", out)

    def test_disable_cannot_name_a_withdrawn_rule(self):
        rc, _out = self.run_cli("x", "--disable", "diagnosis-key")
        self.assertEqual(2, rc)

    def test_a_scoped_marker_exempts_it(self):
        tally = ls.Tally()
        self.assertEqual([], ls.scan_text(
            "t", "diagnosis: Foobaritis  # leakscan:allow:diagnosis-key: fixture",
            [], frozenset(), tally))
        self.assertEqual({"diagnosis-key": 1}, tally.by_marker)


if __name__ == "__main__":
    unittest.main()
