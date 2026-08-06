"""Stdlib-only tests for secretscan (no pytest needed): `python3 -m unittest`.

Every credential-looking literal here is fictional/example-shaped — the point of
the test is the *shape*, not any real value.
"""

import contextlib
import io
import os
import shutil
import tempfile
import pathlib
import unittest
from pathlib import Path

import secretscan as ss


def scan(text, disabled=frozenset()):
    return ss.scan_text("t", text, disabled)


def rules(text, disabled=frozenset()):
    return {f.rule for f in scan(text, disabled)}


# ===========================================================================
# THE CANARY SUITE — credential SHAPES that must ALWAYS flag.
#
# CONTRACT: a canary going quiet is a DETECTION REGRESSION, never a fixture to
# update casually. If a gate change makes one of these pass clean, the gate
# change is wrong until a principal rules otherwise — do not edit the canary to
# match the new behaviour, and do not delete one to make a suite green.
#
# Why it exists (SF3, ruled 2026-07-28): the acceptance test for the 2026-07-28
# gate change was "re-scan the estate's corpus". That is a sound regression
# floor and an INSUFFICIENT acceptance test — a suppression validated against
# one estate's true secrets (all mixed-class, as it happened) cannot see the
# credential shapes that estate does not hold. SF1 is the live demonstration: a
# new kebab-slug exemption silently un-flagged diceware-style passphrases, and
# the corpus re-scan could not have noticed because no repo held one. This set
# would have caught it — the passphrase canaries below are red at that commit.
#
# The five families are the ruled ones: env-var assignment, hex, base64,
# passphrase, connection string. Adding a family is welcome. Removing one, or
# weakening one, is a decision, not a refactor.
# ===========================================================================
CANARIES = (
    # --- env-var assignment: the single most common shape a real credential
    # takes in compose/.env files. `_` is a word character, which is how every
    # prefixed env var was once exempt (2026-07-28, 15 live assignments).
    ("env-var, prefixed", "REDIS_PASSWORD: Qw82Lmfhtxz47"),
    ("env-var, exported", "export DB_TOKEN=Zx91Kdms4hq82Tvb"),
    ("env-var, camelCase key", "redisPassword: Gk8xQvie2mNfR7pL"),

    # --- hex: single-case hex reads as a git SHA to every variety-based gate,
    # so both leading forms are pinned. Letter-leading was the proven gap
    # (E6c/SF2); digit-leading flagged only by accident of the identifier rule
    # requiring a letter start, which is not a guarantee worth trusting.
    ("hex, digit-leading", "password = 0f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c"),
    ("hex, letter-leading", "api_key = deadbeefcafef00d0123456789abcdef"),
    ("hex, uppercase", "SECRET_KEY=ABCDEF0123456789ABCDEF0123456789"),

    # --- base64 / base64url key material, assigned and context-free.
    ("base64url, assigned", "client_secret: aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5bC7"),
    ("base64, padded blob", "auth_token = QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVow=="),
    ("base64, context-free blob", "blob aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5bC7"),

    # --- passphrase: the SF1 shape. BOTH spellings, because the kebab
    # exemption and its snake twin each swallow one of them.
    ("passphrase, hyphenated", "password=correct-horse-battery-staple"),
    ("passphrase, underscored", "password=correct_horse_battery_staple"),

    # --- connection string: the credential is embedded in a URL, so no key
    # name announces it.
    ("connection string, postgres",
     "DATABASE_URL=postgres://svc:s3cr3tpwd@db.internal:5432/app"),
    ("connection string, amqp", "broker = amqp://worker:Hq83zLmt4x@rabbit:5672/"),

    # --- vendor formats: unambiguous by construction, and the cheapest thing
    # in the tool to break with a regex tidy-up.
    ("vendor, AWS key id", "aws_access_key_id = AKIAIOSFODNN7EXAMPLE"),
    ("vendor, GitHub token", "token: ghp_012345678901234567890123456789abcdef"),
    ("vendor, private-key header", "-----BEGIN OPENSSH PRIVATE KEY-----"),
)


class CanarySuite(unittest.TestCase):
    """Standing detection canaries — see the CONTRACT comment above CANARIES.

    Run beside the corpus re-scan on every gate change. The corpus proves you
    did not break this estate; the canaries prove you did not break detection.
    """

    def test_every_canary_flags(self):
        for name, line in CANARIES:
            with self.subTest(canary=name):
                found = scan(line)
                self.assertTrue(
                    found,
                    f"CANARY WENT QUIET: {name!r} no longer flags. This is a "
                    f"detection regression in the gate, not a stale fixture — "
                    f"fix the gate, do not edit this canary.")

    def test_canary_set_is_not_silently_shrunk(self):
        """Deleting a canary is the easy way to make this suite green again.

        The count is pinned so that doing it has to be deliberate: raise the
        number when you ADD a family, and treat any need to lower it as a
        decision for a principal, with the reason written down.
        """
        self.assertGreaterEqual(len(CANARIES), 16)
        self.assertEqual(len(set(CANARIES)), len(CANARIES), "duplicate canary")


class Named(unittest.TestCase):
    def test_private_key_header(self):
        self.assertIn("private-key-header",
                      rules("-----BEGIN OPENSSH PRIVATE KEY-----"))

    def test_pgp_private_key(self):
        self.assertIn("pgp-private-key",
                      rules("-----BEGIN PGP PRIVATE KEY BLOCK-----"))

    def test_aws_access_key_id(self):
        self.assertIn("aws-access-key-id", rules("id AKIAIOSFODNN7EXAMPLE here"))

    def test_aws_temporary_key(self):
        self.assertIn("aws-access-key-id", rules("ASIAIOSFODNN7EXAMPLE"))

    def test_github_token(self):
        tok = "ghp_012345678901234567890123456789abcdef"
        self.assertIn("github-token", rules(f"gh {tok}"))

    def test_github_pat(self):
        self.assertIn("github-token",
                      rules("github_pat_11ABCDE0123456789_abcdefghij"))

    def test_slack_token(self):
        self.assertIn("slack-token", rules("xoxb-1234567890-abcdefghijklmno"))

    def test_slack_webhook(self):
        self.assertIn("slack-webhook",
                      rules("post to https://hooks.slack.com/services/T00/B00/xyz"))

    def test_google_api_key(self):
        self.assertIn("google-api-key",
                      rules("AIzaSyD-abcdefghijklmnopqrstuvwxyz01234"))

    def test_stripe_key(self):
        self.assertIn("stripe-key", rules("sk_live_0123456789abcdefghijklmn"))

    def test_anthropic_key(self):
        self.assertIn("anthropic-key", rules("sk-ant-api03-abcdefghijklmnopqrst"))

    def test_jwt(self):
        tok = "eyJhbGciOi.eyJzdWIiOi.SflKxwRJSM"
        self.assertIn("jwt", rules(f"auth {tok}"))

    def test_basic_auth_url(self):
        self.assertIn("basic-auth-url",
                      rules("db at postgres://user:s3cr3tpw@host/db"))


class Assigned(unittest.TestCase):
    def test_high_entropy_password(self):
        self.assertIn("assigned-secret",
                      rules('password = "Gk8xQvie2mNfR7pLzW3dTaHb"'))

    def test_api_key_assignment(self):
        self.assertIn("assigned-secret",
                      rules("api_key: 7f3Kd9Lm2Qp8Rt5Vx1Zc4Nb6Wg0Hs"))

    def test_client_secret_hyphen(self):
        self.assertIn("assigned-secret",
                      rules("client-secret=aB3dE5fG7hJ9kL1mN3pQ5rS7"))

    def test_placeholder_not_flagged(self):
        self.assertNotIn("assigned-secret", rules("password = changeme"))
        self.assertNotIn("assigned-secret", rules("token = your-token-here"))

    def test_env_indirection_not_flagged(self):
        self.assertNotIn("assigned-secret", rules("api_key = ${API_KEY}"))
        self.assertNotIn("assigned-secret", rules("secret = $SECRET"))

    def test_tiki_secret_reference_not_flagged(self):
        # the CORRECT pattern — a reference to the secret store, not the secret
        self.assertEqual(set(), rules('psk = "!secret wg_home"'))

    def test_path_value_not_flagged(self):
        self.assertNotIn("assigned-secret",
                         rules("private_key = /etc/ssl/server.key"))

    def test_generic_key_word_not_flagged(self):
        # bare `key`/`id` are too generic to be the secret-name half
        self.assertNotIn("assigned-secret",
                         rules("primary_key = Gk8xQvie2mNfR7pLzW3dTaHb"))

    def test_variable_reference_not_flagged(self):
        # `password=admin_password` passes a variable, not a literal
        self.assertNotIn("assigned-secret",
                         rules("host=h, password=admin_password, port=80"))

    def test_attribute_access_not_flagged(self):
        self.assertNotIn("assigned-secret",
                         rules("auth=(self.conn.username, self.conn.password)"))

    def test_function_call_value_not_flagged(self):
        self.assertNotIn("assigned-secret",
                         rules("password = inv.effective(device).factory_password"))

    def test_mixed_class_identifier_still_flagged(self):
        # an alphanumeric value with the key-material signature is NOT a code ref
        self.assertIn("assigned-secret",
                      rules("password = Gk8xQvie2mNfR7pLzW3dTaHb"))


class BlindSpots2026_07_28(unittest.TestCase):
    """Four ways a REAL credential slipped past this gate, found together on
    2026-07-28 when a live NetBox config scanned clean while the commented-out
    secret-store reference above it was reported high-severity. Each test below
    failed before that day's fix. They are grouped rather than scattered because
    they share one root cause: a suppression rule matching on a FRAGMENT (a word
    boundary, an opening marker, a stray bracket) instead of a whole shape."""

    # A — `_` is a word character, so `\b` never matched between the prefix and
    # the keyword. Every prefixed env var was exempt: 15 live assignments went
    # unflagged across the estate.
    def test_prefixed_env_var_flagged(self):
        self.assertIn("assigned-secret", rules("REDIS_PASSWORD: Qw82Lmfhtxz47"))

    def test_camel_case_key_flagged(self):
        self.assertIn("assigned-secret", rules("redisPassword: Gk8xQvie2mNfR7pL"))

    def test_bypass_still_not_a_password_key(self):
        # the camelCase hump must stay case-SENSITIVE, or `BYPASS` matches `PASS`
        # and re-introduces the false positives the word boundary existed to stop
        self.assertNotIn("assigned-secret", rules("if bypass: SomeValue123abc"))

    # B — the extension requirement meant the secret-store form we WANT people to
    # use was reported as a high-severity secret.
    def test_extensionless_secret_mount_not_flagged(self):
        self.assertNotIn("assigned-secret",
                         rules("SECRET_KEY: /run/secrets/netbox_key"))

    def test_base64_blob_containing_slash_still_flagged(self):
        # a path-shaped exemption must not become a way to smuggle key material
        self.assertIn("assigned-secret",
                      rules("password: /aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5bC7/x"))

    # C — an OPENING templating marker anywhere in a value wrote it off as a
    # template. A random key containing the two characters `$(` was exempt.
    # The value below is SYNTHETIC — same shape as the live key that exposed
    # this (symbol-rich, `$(` and unbalanced parens, no closing brace), never
    # the value itself. Quoting a real credential to prove a scanner catches
    # real credentials would leak it into a public repo.
    def test_real_key_containing_unclosed_template_marker_flagged(self):
        self.assertIn("assigned-secret",
                      rules("SECRET_KEY: k(z)4tPwqBn$(_x7M2v9c(HdRuLjjbse31"
                            "y5TgKmpa%2QW#n!8ZX@+U6Fh1B"))

    def test_closed_template_still_not_flagged(self):
        self.assertNotIn("assigned-secret", rules("password: ${DB_PASSWORD}"))
        self.assertNotIn("assigned-secret", rules("password: $(vault read pw)"))

    # D — same fragment bug in the code-reference test: a stray `(` or `)`
    # anywhere meant "function call".
    def test_stray_bracket_in_key_material_flagged(self):
        self.assertIn("assigned-secret", rules("password: Gk8(Qvie2mNfR7pLzW3d"))

    def test_genuine_call_still_not_flagged(self):
        self.assertNotIn("assigned-secret", rules("password: get_secret()"))

    # The three false positives the fix itself introduced, caught by re-scanning
    # the estate before landing. Each is a shape the old stray-bracket test had
    # been quietly absorbing.
    def test_js_function_expression_not_flagged(self):
        # vendored minified JS: `password:function(a){return a.nodeName…}`
        self.assertNotIn("assigned-secret",
                         rules("password:function(a){return a.nodeName}"))
        self.assertNotIn("assigned-secret",
                         rules("const token = Buffer.from(JSON.stringify({"))

    def test_kebab_case_enum_not_flagged(self):
        self.assertNotIn("assigned-secret",
                         rules('_home(require_message_auth="yes-access-request")'))

    def test_prose_after_key_word_not_flagged(self):
        self.assertNotIn("assigned-secret",
                         rules("# without password= (live-proven 2026-07-04); and"))


class LowVarietyIsNotInnocence(unittest.TestCase):
    """E6c — in credential-key context, low character variety is NOT evidence
    of innocence (ruled 2026-07-28, generalising the SF1+SF2 carve-outs).

    Every suppression in the assigned path reads low variety as innocence: the
    identifier rule, the slug rule, the mixed-class hoist, the entropy floor.
    That is sound with no context and unsound once a key name has said
    "credential" — the key name has already done the filtering.

    THE SIX-SHAPE PROBE, reconstructed. Mike ruled on a live probe of six
    credential-shaped assignments: four passed CLEAN before this change — both
    passphrase spellings and both letter-leading hex values — while only the
    digit-leading hex and the mixed-class password flagged. All six flag now.
    Re-run against `secretscan.py` before this change and the four marked below
    are red legs.
    """

    # --- probe 1/6: flagged before, by accident of the identifier rule
    # requiring a letter/underscore start. Pinned so the accident becomes a
    # guarantee.
    def test_probe_digit_leading_hex(self):
        self.assertIn("assigned-secret",
                      rules("password = 0f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c"))

    # --- probe 2/6 and 3/6: RED LEGS. Letter-leading hex was the proven gap —
    # roughly 6 in 16 random hex keys start with a letter.
    def test_probe_letter_leading_hex(self):
        self.assertIn("assigned-secret",
                      rules("api_key = deadbeefcafef00d0123456789abcdef"))

    def test_probe_letter_leading_hex_env_var(self):
        self.assertIn("assigned-secret",
                      rules("DB_PASSWORD=abcdef0123456789abcdef0123456789"))

    # --- probe 4/6 and 5/6: RED LEGS. The SF1 shape. The kebab exemption
    # un-flagged the hyphenated spelling; the identifier rule had long exempted
    # the snake twin. Both are diceware shapes real people really use.
    def test_probe_hyphenated_passphrase(self):
        self.assertIn("assigned-secret",
                      rules("password=correct-horse-battery-staple"))

    def test_probe_underscored_passphrase(self):
        self.assertIn("assigned-secret",
                      rules("password=correct_horse_battery_staple"))

    # --- probe 6/6: the control — flagged before and still flags.
    def test_probe_mixed_class_password(self):
        self.assertIn("assigned-secret",
                      rules("password = Gk8xQvie2mNfR7pLzW3dTaHb"))

    # --- the generalisation: shapes the ruling did not have to enumerate but
    # which are the same error. E6c is a rule, not two carve-outs.
    def test_uppercase_hex_value(self):
        self.assertIn("assigned-secret",
                      rules("SECRET_KEY=ABCDEF0123456789ABCDEF0123456789"))

    def test_base32_seed_value(self):
        # a TOTP seed: uppercase + digits, no lowercase → identifier-shaped to
        # every variety gate
        self.assertIn("assigned-secret",
                      rules("totp_secret: JBSWY3DPEHPK3PXPJBSWY3DPEHPK3PXP"))

    def test_all_lowercase_key_material(self):
        self.assertIn("assigned-secret",
                      rules("auth_token = qwertzuiopasdfghjklyxcvbnmqwertz"))

    def test_five_word_passphrase(self):
        self.assertIn("assigned-secret",
                      rules("passphrase: staple-battery-horse-correct-blue"))

    # --- the blocking set only WIDENS: everything the suppressions exist for
    # still passes. The discriminator is whole shape (length, part count), not
    # character variety.
    def test_code_reference_still_not_flagged(self):
        self.assertNotIn("assigned-secret",
                         rules("host=h, password=admin_password, port=80"))
        self.assertNotIn("assigned-secret",
                         rules("password = inv.effective(device).factory_password"))
        self.assertNotIn("assigned-secret", rules("password: get_secret()"))

    def test_three_part_slug_still_not_flagged(self):
        # `yes-access-request` and `require_message_auth` are names. Four parts
        # is the line, and it is the ruled one.
        self.assertNotIn("assigned-secret",
                         rules('_home(require_message_auth="yes-access-request")'))

    def test_placeholder_wins_over_the_carve_out(self):
        # placeholder/indirection/path are statements about what a value is
        # FOR, not about its variety, so they stay above E6c.
        self.assertNotIn("assigned-secret",
                         rules("password = changeme-changeme-changeme-changeme"))
        self.assertNotIn("assigned-secret",
                         rules("password = example-value-goes-here"))
        self.assertNotIn("assigned-secret", rules("password: ${DB_PASSWORD}"))
        self.assertNotIn("assigned-secret",
                         rules("SECRET_KEY: /run/secrets/netbox_key"))

    def test_context_free_blocking_set_is_unchanged(self):
        # E6c is scoped to credential-key context; nothing it did makes a bare
        # git SHA in prose BLOCK, because nothing named it a credential.
        #
        # CONTRACT CHANGED DELIBERATELY, 2026-08-06 (E6b). This test read
        # `assertEqual(set(), ...)` — no finding of any kind — which was the
        # right assertion while `block` was the only response a finding could
        # carry. E6b gives the context-free path a second response, and the git
        # SHA is precisely what it reports: E6c's own comment said "in the
        # context-free net (where they do live) nothing changes", and E6b is the
        # ruled change. So the claim is narrowed to the one E6c actually made —
        # the CRY-WOLF case stays out of the gate — and the advisory half is
        # asserted a few lines down rather than left unpinned.
        for line in ("commit 9f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f90",
                     "sha256 deadbeefcafef00d0123456789abcdef"):
            self.assertEqual([], [f.rule for f in scan(line) if f.blocks], line)
        # The passphrase shape stays SILENT context-free — not advisory either.
        # Four-part kebab slugs are everywhere in prose and filenames, so
        # widening to them would be the cry-wolf tax the tier exists to avoid,
        # and E6b widened the alphanumeric-run shape only.
        self.assertEqual(set(), rules("slug: correct-horse-battery-staple"))


class HighEntropy(unittest.TestCase):
    def test_mixed_class_blob_flagged(self):
        self.assertIn("high-entropy",
                      rules("blob aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5bC7"))

    def test_git_sha_not_flagged(self):
        # single-case hex → excluded by the mixed-class requirement
        self.assertNotIn("high-entropy",
                         rules("9f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f90"))

    def test_allcaps_constant_not_flagged(self):
        self.assertNotIn("high-entropy",
                         rules("CONST ABCDEFGHIJKLMNOPQRSTUVWXYZ012345"))

    def test_short_token_not_flagged(self):
        self.assertNotIn("high-entropy", rules("id aB3dE5fG"))

    def test_url_path_not_flagged(self):
        # `/` is not in the token class, so a URL path can't form one long span
        self.assertNotIn("high-entropy",
                         rules('url = "https://github.com/someUser42/repo/blob/main/CHANGELOG.md"'))

    def test_ssh_public_key_not_flagged(self):
        self.assertNotIn("high-entropy",
                         rules("sshkey: ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE4y7EHsSkv3kR1TE1iLzJfjUMR"))

    def test_public_key_field_not_flagged(self):
        self.assertNotIn("high-entropy",
                         rules("public_key: ANS5EE79aBcDeFgHiJkLmNoPqRsTuVwXyZ012345678="))


class AdvisoryTier(unittest.TestCase):
    """E6b — a second response, and the coverage it buys.

    The item's own test, which the roadmap asked to be tested rather than
    assumed: *does an advisory tier weaken the gate?* The answer has two halves
    and both are pinned below — the blocking set is byte-for-byte unchanged
    (`BlockingSetNeverShrinks`), and the tier only ever ADDS findings that did
    not exist before.
    """

    # Shapes that were SILENT before the tier and are now reported. Each is a
    # single-case run at key-material length: exactly what `HIGH_ENTROPY_RX`'s
    # mixed-class requirement excluded, which the E6 intent cold pass (EI4)
    # named as the real narrowing site.
    WIDENED = (
        ("lowercase hex, 40 (git SHA / sha1)",
         "commit 9f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f90"),
        ("lowercase hex, 64 (sha256 digest / hex-encoded key)",
         "digest 4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5"),
        ("uppercase hex", "CONST DEADBEEFCAFEF00D0123456789ABCDEF0123456789ABCDEF01"),
        ("uppercase alnum (base32 seed, no key name)",
         "seed JBSWY3DPEHPK3PXPJBSWY3DPEHPK3PXP"),
        ("lowercase alnum", "blob qwertzuiopasdfghjklyxcvbnmqwertz"),
        ("all-caps constant at length",
         "CONST ABCDEFGHIJKLMNOPQRSTUVWXYZ012345"),
    )

    def test_widened_shapes_are_reported(self):
        for name, line in self.WIDENED:
            with self.subTest(shape=name):
                found = scan(line)
                self.assertTrue(found, f"{name}: reported nothing at all")
                self.assertEqual([ss.LOW_VARIETY_RULE], [f.rule for f in found])

    def test_widened_shapes_never_block(self):
        for name, line in self.WIDENED:
            with self.subTest(shape=name):
                self.assertEqual([], [f.rule for f in scan(line) if f.blocks])

    def test_findings_default_to_blocking(self):
        """A rule that forgets to state its response must fail INTO the gate."""
        f = ss.Finding("t", 1, "r", "named", "high", "x")
        self.assertEqual(ss.RESPONSE_BLOCK, f.response)
        self.assertTrue(f.blocks)

    def test_advisory_only_run_exits_zero(self):
        findings = scan("commit 9f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f90")
        self.assertTrue(findings)
        self.assertFalse(any(f.blocks for f in findings))

    def test_short_run_still_silent(self):
        # The length bar is E6c's ruled 32, not a number fitted to this tree.
        self.assertEqual(set(), rules("commit 9f3a1c2b4d5e6f7a"))

    def test_placeholder_is_not_even_advisory(self):
        self.assertEqual(set(), rules("x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))
        self.assertEqual(set(), rules("v exampleexampleexampleexampleexample"))

    def test_public_key_line_is_not_even_advisory(self):
        self.assertEqual(
            set(),
            rules("sshkey: ssh-ed25519 aaaac3nzac1lzdi1nte5aaaaie4y7ehsskv3kr1te1"))

    def test_allow_marker_reaches_the_advisory_rule_by_name(self):
        # Rule (a) of GUARDS.md: the narrowest allowance that covers the case.
        line = ("commit 9f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f90"
                f"  # secretscan:allow:{ss.LOW_VARIETY_RULE}: a commit id")
        self.assertEqual([], scan(line))

    def test_disable_reaches_the_advisory_rule(self):
        self.assertIn(ss.LOW_VARIETY_RULE, ss.ALL_RULES)
        self.assertEqual(
            set(), rules("commit 9f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f90",
                         frozenset({ss.LOW_VARIETY_RULE})))

    def test_disabling_advisory_leaves_the_blocking_net_alone(self):
        self.assertIn("high-entropy",
                      rules("blob aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5bC7",
                            frozenset({ss.LOW_VARIETY_RULE})))

    def test_a_blocking_hit_wins_dedupe_over_an_advisory_hit(self):
        # The same 32-char hex run is BOTH an assigned-secret (blocking, E6c)
        # and a low-variety context-free run (advisory). Reported once, as the
        # blocking finding — a line that blocks must never also appear in the
        # advisory list, where a reader could take it for the whole story.
        fs = scan("api_key = deadbeefcafef00d0123456789abcdef")
        self.assertEqual(["assigned-secret"], [f.rule for f in fs])
        self.assertTrue(all(f.blocks for f in fs))


class AdvisoryRender(unittest.TestCase):
    """The reader must never mistake an advisory finding for a blocking one.

    That is a claim about OUTPUT, so it is tested on output. EI1's warning was
    that an advisory finding nobody reads is cover rather than coverage; a block
    that reads like the blocking block is the same failure by another route.
    """

    def _advisory(self):
        return scan("commit 9f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f90")

    def test_clean_run_with_advisory_still_says_clean(self):
        out = ss.render_human(self._advisory(), ss.Tally())
        self.assertIn("✓ secretscan clean", out)
        self.assertNotIn("commit blocked", out)

    def test_advisory_block_states_it_does_not_block(self):
        out = ss.render_human(self._advisory(), ss.Tally())
        self.assertIn("none of these blocked anything", out)
        self.assertIn("🟡", out)
        self.assertIn(ss.LOW_VARIETY_RULE, out)

    def test_advisory_never_wears_the_blocking_markers(self):
        out = ss.render_human(self._advisory(), ss.Tally())
        for blocking_marker in ("✗", "commit blocked"):
            self.assertNotIn(blocking_marker, out)

    def test_both_kinds_together_stay_separable(self):
        findings = scan("aws AKIAIOSFODNN7EXAMPLE") + self._advisory()
        out = ss.render_human(findings, ss.Tally())
        self.assertIn("✗ secretscan: 1 finding(s) — commit blocked.", out)
        self.assertIn(f"{ss.ADVISORY_COUNT_PREFIX} 1 finding(s)", out)
        # The blocking count must not absorb the advisory one.
        self.assertNotIn("2 finding(s) — commit blocked", out)

    def test_count_line_is_machine_readable_for_the_board(self):
        out = ss.render_human(self._advisory(), ss.Tally())
        self.assertIn(f"{ss.ADVISORY_COUNT_PREFIX} 1 finding(s)", out)

    def test_zero_advisory_still_prints_the_count(self):
        """The known-zero rule, and the board's drift guard.

        A count line printed only when non-zero makes "no line" ambiguous
        between nothing-found and wording-drifted — and floor.py's board reads
        this line. Printing the zero is what turns a vanished count into a
        visible defect instead of a quiet green."""
        out = ss.render_human([], ss.Tally())
        self.assertIn(f"{ss.ADVISORY_COUNT_PREFIX} 0 finding(s)", out)
        self.assertNotIn("🟡", out)     # no detail block with nothing to detail


class BlockingSetNeverShrinks(unittest.TestCase):
    """The E6b invariant, pinned as an invariant rather than argued in prose.

    CONTRACT: every input here exited NON-ZERO before the advisory tier existed
    and must exit non-zero after it, with the same rule firing. A line moving
    from this set into the advisory set is a gate weakening — it is a decision
    for a principal, never a test edit.

    E3 is the ONE ruled subtraction (2026-08-04, Mike) and it is scoped to a
    whole shape that is public material by definition; `Fingerprints` below
    pins both of its directions.
    """

    def test_every_canary_still_blocks(self):
        # The canary suite proves detection; this proves the RESPONSE those
        # canaries earn did not quietly soften underneath them.
        for name, line in CANARIES:
            with self.subTest(canary=name):
                self.assertTrue(
                    any(f.blocks for f in scan(line)),
                    f"{name!r} still reports, but no longer BLOCKS — the "
                    f"advisory tier has absorbed a blocking finding.")

    def test_mixed_class_entropy_blob_still_blocks(self):
        fs = scan("blob aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5bC7")
        self.assertEqual(["high-entropy"], [f.rule for f in fs])
        self.assertTrue(all(f.blocks for f in fs))

    def test_assigned_low_variety_still_blocks_not_advises(self):
        # E6c's carve-outs live in ASSIGNED context and are blocking findings.
        # The advisory tier must not have captured them on its way past.
        for line in ("api_key = deadbeefcafef00d0123456789abcdef",
                     "password=correct-horse-battery-staple",
                     "SECRET_KEY=ABCDEF0123456789ABCDEF0123456789"):
            with self.subTest(line=line):
                fs = scan(line)
                self.assertEqual(["assigned-secret"], [f.rule for f in fs])
                self.assertTrue(all(f.blocks for f in fs))


class Fingerprints(unittest.TestCase):
    """E3 — public-key fingerprints are public material and are suppressed.

    RULED 2026-08-04 (Mike): suppress the shape, whole-shape never fragment,
    with canaries BOTH directions so the suppression cannot quietly widen. The
    second direction is the one that matters: a value that merely resembles a
    fingerprint, or wears its prefix, is a credential until its whole shape says
    otherwise.

    Every value below is synthetic. A fingerprint is not itself sensitive, but
    quoting a real one would tie this public repo to a real key, and the shape
    is the entire point of the test.
    """

    # Synthetic 43-char base64 bodies — the length ssh-keygen prints for a
    # SHA-256 digest (32 bytes, unpadded base64).
    FP256 = "aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5bC7dE9f"
    FPMD5 = "16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48"

    def test_fixture_body_is_the_real_fingerprint_length(self):
        """If this drifts, every suppression test below proves nothing."""
        self.assertEqual(43, len(self.FP256))

    # --- direction 1: the shape is suppressed, and would otherwise have blocked
    def test_sha256_fingerprint_alone_is_suppressed(self):
        self.assertEqual([], scan(f"SHA256:{self.FP256}"))

    def test_sha256_fingerprint_in_a_keygen_line_is_suppressed(self):
        self.assertEqual([], scan(f"2048 SHA256:{self.FP256} user@host (RSA)"))

    def test_the_body_alone_would_have_blocked(self):
        # Proves the suppression is doing real work rather than describing a
        # line that was already clean.
        self.assertIn("high-entropy", rules(f"blob {self.FP256}"))

    def test_md5_hex_fingerprint_is_recognised_both_spellings(self):
        self.assertEqual([], scan(f"MD5:{self.FPMD5}"))
        self.assertEqual([], scan(f"fingerprint {self.FPMD5}"))
        self.assertTrue(ss.FINGERPRINT_RX.search(f"MD5:{self.FPMD5}"))
        self.assertTrue(ss.FINGERPRINT_RX.search(self.FPMD5))

    def test_suppression_is_counted_never_silent(self):
        # GUARDS.md rule (b): find first, subtract second, and report the
        # subtraction. A carve-out nobody can see growing is the failure mode.
        tally = ss.Tally()
        ss.scan_text("t", f"host key SHA256:{self.FP256}\n", frozenset(), tally)
        self.assertEqual(1, tally.fingerprints)
        self.assertIn("1 public-key fingerprint(s)", tally.summary())

    def test_zero_count_is_still_printed(self):
        self.assertIn("0 public-key fingerprint(s)", ss.Tally().summary())

    # --- direction 2: a NEAR-fingerprint that is a credential must still flag.
    # This is the half that stops the carve-out widening in silence.
    def test_wrong_body_length_still_blocks(self):
        for body in (self.FP256 + "ZZZZ", self.FP256[:-6]):
            with self.subTest(length=len(body)):
                fs = scan(f"SHA256:{body}")
                self.assertTrue(any(f.blocks for f in fs),
                                "a SHA256: prefix is not a fingerprint on its own")

    def test_prefix_without_the_separator_still_blocks(self):
        self.assertTrue(any(f.blocks for f in scan(f"SHA256{self.FP256}")))

    def test_a_credential_under_a_key_name_still_blocks(self):
        # The carve-out lives on the context-free entropy path only. A value a
        # key name has already called a credential is never reached by it.
        self.assertIn("assigned-secret",
                      rules("api_key = Gk8xQvie2mNfR7pLzW3dTaHbXy4Wz9Qm"))

    def test_a_vendor_token_beside_a_fingerprint_still_blocks(self):
        fs = scan(f"SHA256:{self.FP256} AKIAIOSFODNN7EXAMPLE")
        self.assertEqual(["aws-access-key-id"], [f.rule for f in fs])

    def test_short_hex_pair_run_is_not_a_fingerprint(self):
        # Fifteen pairs, not sixteen — a MAC address or a truncated dump is
        # not a digest, and the whole-shape rule is what says so.
        short = ":".join(["ab"] * 15)
        self.assertIsNone(ss.FINGERPRINT_RX.search(short))

    def test_private_key_header_is_untouched_by_the_public_carve_out(self):
        self.assertIn("private-key-header",
                      rules("-----BEGIN OPENSSH PRIVATE KEY-----"))


class Dedupe(unittest.TestCase):
    def test_named_suppresses_entropy_on_same_line(self):
        # a github token is high-entropy AND named — report once, as named
        fs = scan("token ghp_012345678901234567890123456789abcdef")
        kinds = {f.kind for f in fs}
        self.assertIn("named", kinds)
        self.assertNotIn("entropy", kinds)


class Disable(unittest.TestCase):
    def test_disable_high_entropy_keeps_named(self):
        text = "AKIAIOSFODNN7EXAMPLE and aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3z"
        got = rules(text, frozenset({"high-entropy"}))
        self.assertIn("aws-access-key-id", got)
        self.assertNotIn("high-entropy", got)

    def test_disable_assigned(self):
        self.assertEqual(
            set(), rules('password = "Gk8xQvie2mNfR7pLzW3dTaHb"',
                         frozenset({"assigned", "high-entropy"})))

    def test_disable_named_rule(self):
        self.assertNotIn("aws-access-key-id",
                         rules("AKIAIOSFODNN7EXAMPLE",
                               frozenset({"aws-access-key-id"})))


class Allow(unittest.TestCase):
    def test_inline_allow_marker_exempts_line(self):
        self.assertEqual(
            [], scan("aws AKIAIOSFODNN7EXAMPLE  # secretscan:allow: doc example"))

    # Rule (c) — reasoned. Tightened 2026-08-05: a marker with no reason is a
    # mention, not an exemption.
    def test_bare_marker_without_reason_does_not_exempt(self):
        found = scan("aws AKIAIOSFODNN7EXAMPLE  # secretscan:allow")
        self.assertEqual(["aws-access-key-id"], [f.rule for f in found])

    def test_marker_with_empty_reason_does_not_exempt(self):
        self.assertTrue(scan("aws AKIAIOSFODNN7EXAMPLE  # secretscan:allow:"))

    def test_dual_marker_needs_its_own_reason(self):
        # The exact loose form found live on 2026-08-05: only the SECOND
        # marker carried a reason, and the first was silently honoured anyway.
        self.assertTrue(
            scan("aws AKIAIOSFODNN7EXAMPLE  # secretscan:allow / leakscan:allow: fixture"))
        self.assertEqual([], scan(
            "aws AKIAIOSFODNN7EXAMPLE  # secretscan:allow: fixture / leakscan:allow: fixture"))

    # Rule (a) — narrow.
    def test_scoped_marker_exempts_only_its_own_rule(self):
        found = scan("aws AKIAIOSFODNN7EXAMPLE and ghp_012345678901234567890123456789abcdef"
                     "  # secretscan:allow:aws-access-key-id: documented example")
        self.assertNotIn("aws-access-key-id", {f.rule for f in found})
        self.assertIn("github-token", {f.rule for f in found})

    def test_scoped_marker_naming_no_real_rule_exempts_nothing(self):
        self.assertTrue(scan("aws AKIAIOSFODNN7EXAMPLE  # secretscan:allow:not-a-rule: typo"))


class Suppression(unittest.TestCase):
    """Rule (b) — a suppressed finding is counted, never silently dropped."""

    def test_marker_suppressions_are_counted_per_rule(self):
        tally = ss.Tally()
        ss.scan_text("t", "aws AKIAIOSFODNN7EXAMPLE  # secretscan:allow: fixture\n",
                     frozenset(), tally)
        self.assertEqual({"aws-access-key-id": 1}, tally.by_marker)

    def test_suppression_count_is_taken_after_dedupe(self):
        # A named hit and an entropy hit fire on the same token; dedupe drops
        # the entropy one. Counting before dedupe would report 2 suppressions
        # where the scan only ever had 1 finding to suppress.
        tally = ss.Tally()
        ss.scan_text("t", "github: ghp_012345678901234567890123456789abcdef"
                          "  # secretscan:allow: fixture\n", frozenset(), tally)
        self.assertEqual(1, tally.marker_total)

    def test_clean_tally_reports_known_zeros(self):
        summary = ss.Tally().summary()
        self.assertIn("0 by allow-marker", summary)
        self.assertIn("0 file(s) by .secretscanignore", summary)
        self.assertIn("0 rule(s) disabled", summary)

    def test_render_reports_suppression_on_a_clean_run(self):
        tally = ss.Tally()
        tally.note_marker("github-token")
        out = ss.render_human([], tally)
        self.assertIn("clean", out)
        self.assertIn("1 by allow-marker", out)


class Redact(unittest.TestCase):
    def test_named_keeps_prefix_not_full_value(self):
        out = ss.redact("AKIAIOSFODNN7EXAMPLE", "named")
        self.assertTrue(out.startswith("AKIA"))
        self.assertNotIn("EXAMPLE", out)

    def test_entropy_hides_value(self):
        out = ss.redact("Gk8xQvie2mNfR7pLzW3dTaHb", "entropy")
        self.assertNotIn("Gk8x", out)
        self.assertIn("entropy", out)


class Helpers(unittest.TestCase):
    def test_shannon_zero_for_uniform(self):
        self.assertEqual(0.0, ss.shannon("aaaa"))

    def test_shannon_higher_for_random(self):
        self.assertGreater(ss.shannon("aB3dE5fG7hJ9"), ss.shannon("aaaabbbb"))

    def test_indirection_detection(self):
        self.assertTrue(ss._is_indirection("!secret foo"))
        self.assertTrue(ss._is_indirection("${VAR}"))
        self.assertFalse(ss._is_indirection("Gk8xQvie2mNf"))

    def test_placeholder_detection(self):
        self.assertTrue(ss._is_placeholder("changeme"))
        self.assertTrue(ss._is_placeholder("xxxxxxxx"))
        self.assertFalse(ss._is_placeholder("Gk8xQvie2mNfR7pL"))


class Ignore(unittest.TestCase):
    def test_exact_glob(self):
        self.assertTrue(ss._ignored("tools/test_secretscan.py",
                                    ["tools/test_secretscan.py"]))

    def test_subtree_glob(self):
        self.assertTrue(ss._ignored("secrets/prod.yaml", ["secrets/"]))

    def test_non_match(self):
        self.assertFalse(ss._ignored("src/real.py", ["secrets/"]))


class WholeTree(unittest.TestCase):
    """Whole-tree walk guards from the 2026-07-11 child-CI-floor review
    (findings N1–N3): no masked content dirs, no phantom-success on a bad
    path, and the ignore hatch working however the caller invokes it."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _main(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            return ss.main(argv)

    def test_content_dir_named_build_is_walked(self):
        # Regression (N1): `build`/`dist` are NOT hardcode-skipped — a content
        # dir sharing the name (atelier's own docs/build/) must be scanned; a
        # real build-output dir uses .secretscanignore instead.
        self._write("docs/build/note.md", "key = AKIAJ7Q2XR4TP9WNB5KD\n")
        fs = ss.scan_paths([self.tmp], self.tmp)
        self.assertEqual(["aws-access-key-id"], [f.rule for f in fs])

    def test_nonexistent_path_is_an_error_not_a_pass(self):
        # Regression (N2), the linkscan L1 class: a typo'd path scanning
        # nothing must never exit 0.
        self.assertEqual(2, self._main(["--root", str(self.tmp),
                                        str(self.tmp / "gone")]))

    def test_ignore_hatch_lives_when_cwd_is_not_root(self):
        # Regression (N3): floor.yml runs `--root repo repo` from the
        # workspace, not the repo — the scanned repo's own .secretscanignore
        # globs are root-relative by contract and must still match. Sanity
        # first: without the hatch the planted key flags.
        self._write("repo/docs/fixture.md", "key = AKIAJ7Q2XR4TP9WNB5KD\n")
        old = os.getcwd()
        os.chdir(self.tmp)
        try:
            self.assertEqual(1, self._main(["--root", "repo", "repo"]))
            self._write("repo/.secretscanignore", "# a reasoned fixture exemption\ndocs/fixture.md\n")
            self.assertEqual(0, self._main(["--root", "repo", "repo"]))
        finally:
            os.chdir(old)


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ss._selftest())


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
            [sys.executable, str(pathlib.Path(__file__).resolve().parent / "secretscan.py"), *args],
            capture_output=True, text=True)

    def test_absolute_staged_path_is_refused(self):
        r = self._run("--staged", "--root", "/tmp", "/tmp/anything")
        self.assertEqual(r.returncode, 2, "must be an environment error, not a pass")
        self.assertIn("absolute", r.stderr.lower())

    def test_error_names_the_working_form(self):
        """A refusal that doesn't say what to do instead just gets --no-verify'd."""
        r = self._run("--staged", "--root", "/tmp", "/tmp/anything")
        self.assertIn("src/", r.stderr)


if __name__ == "__main__":
    unittest.main()
