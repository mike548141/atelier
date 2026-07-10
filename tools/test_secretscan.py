"""Stdlib-only tests for secretscan (no pytest needed): `python3 -m unittest`.

Every credential-looking literal here is fictional/example-shaped — the point of
the test is the *shape*, not any real value.
"""

import unittest

import secretscan as ss


def scan(text, disabled=frozenset()):
    return ss.scan_text("t", text, disabled)


def rules(text, disabled=frozenset()):
    return {f.rule for f in scan(text, disabled)}


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


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ss._selftest())


if __name__ == "__main__":
    unittest.main()
