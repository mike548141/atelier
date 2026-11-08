#!/usr/bin/env python3
"""secretscan — the mechanical gate that keeps plaintext credentials out of a
git commit.

leakscan catches the *shape of personal/estate data* (a repo holds such data
only for a recorded purpose). secretscan guards a different boundary that exists in
*every* repo, private ones included: a committed credential is burned the moment
it lands in history, regardless of who can see the repo — history is forever and
a private repo can be shared, forked or leaked later. So this runs everywhere,
and pairs with the SECRETS doctrine's other half: detect → rotate immediately →
the burn cost is minutes, not a breach.

Unlike leakscan there is no machine-local vocabulary: a secret is not a
person-specific name, it is a *shape*. Two detector classes:

  * NAMED credentials (high confidence) — formats that are unambiguously a
    secret by construction: private-key headers, AWS/GitHub/Slack/Google/Stripe/
    Anthropic tokens, JWTs. These always flag; no entropy gate needed.

  * ASSIGNED secrets (context + entropy) — a key that *names* a credential
    (`password`, `api_key`, `token`, `client_secret`…) assigned a value that is
    long, high-entropy, and not an obvious placeholder or indirection. This is
    the workhorse for home-grown secrets that match no vendor format. Context
    (the key name) plus entropy is far more precise than raw entropy scanning,
    which drowns in git hashes and base64 blobs. In this context — and ONLY
    here, because the key name has already done the filtering — low character
    variety is not evidence of innocence (E6c, ruled 2026-07-28): a 32+ char
    single-case hex value and a four-word passphrase are credentials, not names.

TWO RESPONSES, NOT ONE — the advisory tier (E6b, ruled 2026-07-28, built after
its consumer was named 2026-08-04). Every finding carries a `response`:

  * BLOCK — the named formats, the assigned-secret workhorse, and the
    context-free entropy net exactly as they have always fired. **The blocking
    set never shrinks.** Every input that exited non-zero before this tier
    existed still exits non-zero, with the same finding.
  * ADVISORY — reported in full, distinctly, and the exit code stays 0.

Why the tier had to exist before coverage could widen: while `block` was the
only response, widening detection bought coverage at the price of crying wolf,
and that price is what drove the narrowing `SECRETS.md` § *The boundary's
posture* records. The real narrowing site is `HIGH_ENTROPY_RX`'s mixed-class
requirement (E6 intent cold pass, EI4): single-case runs — git SHAs, checksums
*and* lowercase-hex secrets — are excluded from the context-free net entirely,
so a hex-encoded credential outside a secret-named assignment was invisible.
`low-variety-entropy` is that gap, opened as advisory rather than left shut: the
same whole-shape reasoning E6c already ruled (an unbroken 32+ alphanumeric run
is key material, not a name), applied to the path where SHAs actually live, and
costing a printed line rather than a blocked commit.

A second advisory rule, `exempt-private-key` (115/380), reads what a whole-file
`.secretscanignore` glob would otherwise hide: a file exempted on the promise that
its fixtures are fictional is still checked for REAL private-key material (a PEM
private-key block, or a base64 run, that decodes to a private key's DER outline).
Every other rule stays skipped for that file; the one check is advisory, so the
exit code is unmoved. See `scan_exempt_lines`.

An advisory finding nobody reads is cover, not coverage (EI1) — so the tier ships
with its consumers rather than ahead of them: the pre-commit hook prints them at
the commit that would introduce them, every CI push re-prints ALL of them
tree-wide, and `tools/floor.py`'s board carries a `🟡 N advisory finding(s)`
count read from THIS run's output, never from a stored number. No state file, so
there is nothing to go stale and nothing to quietly vanish.

Deliberately does NOT flag the safe indirection patterns — `!secret foo` (tiki),
`${VAR}`, `$(cmd)`, `<placeholder>` — because those are the *correct* way to
reference a secret without embedding it. Flagging them would train people to
disable the scanner.

The report never prints a secret value: findings carry path:line + a redacted
fingerprint (length + entropy), enough to locate, not enough to re-leak.

Some overlap with leakscan is intentional (both catch private-key headers, AWS
key ids, JWTs) — the tools have different *purposes* and are each self-contained
so a peer can copy either one alone. The small plumbing duplication (staged
diff, ignore globs, file iteration) is the price of that zero-coupling; if a
third scanner ever lands, factor a shared base then, not speculatively now.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean, or advisory findings only (they are REPORTED, never a gate)
  1  blocking findings (blocks the commit)
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import codecs
import fnmatch
import itertools
import json
import math
import re
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import filewalk  # noqa: E402
import allowmarker  # noqa: E402
import anchoredrx  # noqa: E402
import report  # noqa: E402

# A line carrying this marker is intentionally exempt (e.g. a documented example
# credential, or a known-public test key). Keep the reason on the same line.
#
# GOVERNED BY `method/GUARDS.md` — narrow, noisy, reasoned, declared. Same contract as
# leakscan next door:
#
#   * NARROW. `secretscan:allow: <reason>` exempts every rule on the line;
#     `secretscan:allow:<rule>: <reason>` exempts only that one, named as the
#     finding names it (`aws-access-key-id`, `assigned-secret`, `high-entropy`,
#     …). A scoped name matching no rule exempts NOTHING — a typo fails closed.
#   * REASONED. Colon plus a non-empty reason, or it is a mention rather than
#     an exemption. Tightened 2026-08-05; a bare marker used to exempt.
#   * NOISY. Every suppression is counted and reported (`Tally`).
ALLOW_MARKER = "secretscan:allow"

ALLOW_RX = allowmarker.marker_rx(ALLOW_MARKER, scope="one", group="rule")


def parse_allow(line: str) -> str | None:
    """The scope of the line's allow-marker, or None if it carries none.

    `""` means every rule; a rule name means just that one. A marker with no
    reason returns None — it is a mention, not an exemption."""
    return allowmarker.scope_of(ALLOW_RX, line, "rule")


# 020/370 — a fixed ceiling on how many `Finding` objects one run MATERIALIZES
# (builds and holds in memory), independent of how many the input actually
# contains. Grounded in a memory BUDGET, not fitted to any one incident's
# number (`ground-numeric-limits`): each held `Finding` costs on the order of
# 1 KiB once its path/excerpt strings and object overhead are counted
# (measured ~700 B/finding on a 400,000-finding synthetic run while building
# this fix). Budgeting roughly 50 MiB for the findings buffer — independent of
# input size — gives this round cap. It comfortably exceeds every real
# finding count on record, including 020/370's own reported incident
# (~43,000): the point of a fixed ceiling is that it does not need raising to
# fit the last incident, only to fit a memory budget.
MAX_MATERIALIZED_FINDINGS = 50_000


@dataclass
class Tally:
    """What the scan removed AFTER finding it — rule (b) of `method/GUARDS.md`.

    A guard that subtracts silently prints the same clean tick for "nothing
    matched" and "everything matched and was exempted"."""
    by_marker: dict[str, int] = field(default_factory=dict)
    files_by_glob: int = 0
    disabled_rules: tuple[str, ...] = ()
    # E3 (ruled 2026-08-04): the public-key-fingerprint carve-out is a
    # suppression like any other, so it is COUNTED rather than applied in
    # silence. Without this the shape would be the one allowance in the tool
    # that a reader cannot see growing — the exact state rule (b) exists to
    # stop.
    fingerprints: int = 0
    # The `PUBLIC_KEY_RX` line carve-out, brought into the same model
    # 2026-08-09. It predated rule (b) and was the LAST silent subtraction here:
    # a line naming public key material had its whole entropy pass skipped, so
    # spans it wrote off appeared in no tally and a clean tick meant either
    # "nothing matched" or "a growing pile of public-key lines matched and were
    # all written off". Counted per entropy SPAN, not per line, for the same
    # reason as `fingerprints`: the unit reported is the would-be finding, which
    # is what rule (b) says gets produced before the allowance is applied.
    public_key_spans: int = 0
    # The URL carve-out (320/290, 2026-09-18, tightened same day): a token in a
    # published URL's SCHEME+HOST+PATH is not treated as an entropy candidate —
    # see `URL_RX`. A query string or fragment is NOT covered — that is where a
    # signed-URL credential actually lives, so it stays live. Counted per span
    # for the same reason as the two above: the widest allowances get the most
    # visible count.
    url_tokens: int = 0

    # 020/370 — the machine-thrash defect. A run over pathological/adversarial
    # content can generate an unbounded NUMBER of findings (measured: ~700
    # bytes held per materialized `Finding`, so hundreds of thousands of them
    # is hundreds of MB — see the board item's before/after table). This is a
    # SAFETY NET, not the expected path: `take_finding_slot` lets the first
    # `MAX_MATERIALIZED_FINDINGS` findings be built and held in full (path,
    # excerpt, everything a reader needs); every one after that is still
    # COUNTED here — never silently dropped — but not built as an object, so
    # the findings list itself stays bounded by a fixed constant regardless of
    # how many the input actually contains. Split blocking/advisory so a
    # capped run's exit code and the advisory count both stay ACCURATE (they
    # read these counters, never `len(findings)`).
    blocking_over_cap: int = 0
    advisory_over_cap: int = 0
    _materialized: int = field(default=0, repr=False, compare=False)

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def take_finding_slot(self, response: str) -> bool:
        """True if a finding with this `response` may still be fully
        materialized (built and held); False once the run-wide cap is
        reached, in which case the caller must count it via
        `blocking_over_cap`/`advisory_over_cap` instead of building a
        `Finding` for it. `response` is `RESPONSE_BLOCK`/`RESPONSE_ADVISORY`
        (referenced by value, not name, to avoid a forward reference — those
        constants are defined later in this module, after `Tally`, and this
        method only runs at call time, long after the whole module has
        loaded)."""
        if self._materialized < MAX_MATERIALIZED_FINDINGS:
            self._materialized += 1
            return True
        if response == "block":
            self.blocking_over_cap += 1
        else:
            self.advisory_over_cap += 1
        return False

    def note_marker(self, rule: str) -> None:
        self.by_marker[rule] = self.by_marker.get(rule, 0) + 1

    def note_fingerprint(self) -> None:
        self.fingerprints += 1

    def note_public_key_span(self) -> None:
        self.public_key_spans += 1

    def note_url_token(self) -> None:
        self.url_tokens += 1

    def summary(self) -> str:
        """One stable line, known zeros printed, so two runs compare.

        Field ORDER and wording are part of the contract, not cosmetics: the
        line exists to be read against another run of it, and a field that
        moves, renames or vanishes at zero breaks that comparison. New
        mechanisms append."""
        parts = [f"{self.marker_total} by allow-marker",
                 f"{self.files_by_glob} file(s) by .secretscanignore",
                 f"{len(self.disabled_rules)} rule(s) disabled",
                 f"{self.fingerprints} public-key fingerprint(s)",
                 f"{self.public_key_spans} by public-key line",
                 f"{self.url_tokens} by published-url token",
                 report.cap_part(self.blocking_over_cap + self.advisory_over_cap,
                                 MAX_MATERIALIZED_FINDINGS)]
        return report.suppressed_line(parts, breakdown=self.by_marker,
                                      disabled=self.disabled_rules)


# Paths never worth scanning. Hardcode-skip ONLY names that are never
# human-authored content — VCS, dependency, and tool-cache dirs. `build`/`dist`
# are DELIBERATELY absent (2026-07-11 child-CI-floor review, N1 — the same
# masking linkscan fixed at d0870a4): a content dir can legitimately share the
# name (atelier's own docs/build/ doctrine layer), and skipping it by name made
# a whole-tree scan blind to a planted key there. Masking a layer is the worst
# failure a publish-safety scanner has; a repo with a real build-output dir
# names it in `.secretscanignore` (one line). Repo-specific globs come from
# .secretscanignore at the scan root.
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

# The key-name half of the ASSIGNED-secret heuristic: a word that means "this is
# a credential". Bounded so `password`, `api_key`, `client-secret`, `authToken`
# all hit but plain `key`/`id` (too generic, huge FP) do not.
# The leading boundary is NOT a plain `\b`. `_` is a word character, so `\b`
# never matches between `REDIS` and `PASSWORD` — which silently exempted every
# prefixed environment variable (`REDIS_PASSWORD`, `POSTGRES_PASSWORD`,
# `DB_TOKEN`), the single most common shape a real credential takes in compose
# and `.env` files. Found 2026-07-28 with 15 live assignments unflagged across
# the estate. So: a word boundary, OR an underscore prefix, OR a camelCase hump
# (`redisPassword`). The hump is matched case-SENSITIVELY via `(?-i:…)` — under
# the pattern's global `(?i)` a case-insensitive lookbehind would also fire
# inside `BYPASS` and re-introduce the false positives `\b` was there to stop.
_LEAD = r"(?:\b|_|(?-i:(?<=[a-z0-9])(?=[A-Z])))"
SECRET_KEY_RX = re.compile(
    r"(?i)" + _LEAD + r"("
    r"pass(?:word|wd|phrase)?"
    r"|secret(?:[_-]?key)?"
    r"|token"
    r"|api[_-]?key|apikey"
    r"|access[_-]?key"
    r"|auth(?:[_-]?token)?"
    r"|client[_-]?secret"
    r"|private[_-]?key"
    r"|credentials?"
    r"|bearer"
    r")\b\s*[:=]\s*[\"']?([^\s\"'`,;:]{6,})")
# The value class excludes ':' so a doc line like `secret: foo: !secret x` stops
# at the field name (a code ref, rejected) rather than swallowing the colon; real
# secrets don't carry ':' (auth/connection strings are the basic-auth-url rule).

# Values that are indirections or placeholders, never a real secret. Checked
# case-insensitively; a substring match is enough for the word-shaped markers.
PLACEHOLDER_SUBSTRINGS = (
    "example", "changeme", "change-me", "change_me", "placeholder", "redacted",
    "your-", "your_", "yourtoken", "yourkey", "my-secret", "dummy", "sample",
    "xxxxxx", "todo", "fixme", "notreal", "fake", "test-token", "test_token",
    "******", "……", "...",
)

# Templating markers are NOT substring-matched. They used to be — `${`, `$(`,
# `%(`, `<`, `>`, `{{`, `}}` sat in the tuple above — and an OPENING marker
# occurring anywhere in a value was enough to write it off as a template. A
# randomly generated 60-char key that happened to contain the two characters
# `$(` was therefore exempted by coincidence, which is exactly how a real
# NetBox SECRET_KEY (entropy 5.29) went unflagged (found 2026-07-28). Requiring
# the marker to be CLOSED keeps genuine templates suppressed and makes chance
# collisions harmless: a real secret would have to contain the opener *and* a
# matching closer, with no intervening delimiter, to slip through.
TEMPLATE_RX = re.compile(
    r"\$\{[^{}]*\}"        # ${VAR}
    r"|\$\([^()]*\)"       # $(command)
    r"|%\([^()]*\)"        # %(python)s
    r"|\{\{[^{}]*\}\}"     # {{ template }}
    r"|<[^<>]{1,64}>"      # <placeholder>
)
PLACEHOLDER_EXACT = frozenset({
    "none", "null", "nil", "undefined", "true", "false", "password", "secret",
    "token", "changeit", "admin", "root", "test", "", "-", "n/a", "na",
})

# The safe secret-indirection patterns. A value starting like this is a
# *reference* to a secret store, not the secret — the pattern we WANT people to
# use. Never flag it.
INDIRECTION_RX = re.compile(r"""^(?:
      !\s*secret\b        # tiki / RouterOS / YAML  !secret foo
    | \$\{                # ${VAR} / ${{ ci }}
    | \$\(                # $(command)
    | \$[A-Za-z_]         # $VAR
    | %\(                 # %(python)s
    | <[^>]+>             # <placeholder>
    | \{\{                # {{ template }}
    | @@                  # sops / templating sentinel
    | env:                # env:FOO
    | vault:              # vault:path
    | sops:               # sops:...
)""", re.VERBOSE)


@dataclass(frozen=True)
class Pattern:
    name: str
    severity: str  # "high" | "medium" — advisory; any hit still blocks
    regex: "re.Pattern[str]"
    # 110/130 lever 4, 160/720 GT2: the rule's pre-filter, declared BESIDE the
    # rule so that widening the regex and re-reading the gate are one diff
    # hunk. A gate is a cheap test on the line that is NECESSARY for the rule
    # to match; None means the rule always runs its full regex (fail open).
    gate: "object" = None


def _p(name: str, severity: str, rx: str, flags: int = 0,
       gate: "object" = None, anchored: "dict | None" = None) -> Pattern:
    """`anchored` (160/720 GT1) swaps the compiled regex for its linear-time
    stand-in (`anchoredrx.AnchoredRx`): same matches, but a run of the leading
    class is tried once, not once per word boundary."""
    compiled = re.compile(rx, flags)
    if anchored is not None:
        compiled = anchoredrx.AnchoredRx(compiled, **anchored)
    return Pattern(name, severity, compiled, gate)


# NAMED credential formats — unambiguous by construction, so they flag on shape
# alone. Ordered by how self-evidently they are a secret.
NAMED: list[Pattern] = [
    _p("private-key-header", "high",
       r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----",
       gate=lambda ln: "PRIVATE KEY-----" in ln),
    _p("pgp-private-key", "high", r"-----BEGIN PGP PRIVATE KEY BLOCK-----",  # secretscan:allow: this is the detection pattern, not a key
       gate=lambda ln: "-----BEGIN PGP PRIVATE KEY BLOCK-----" in ln),  # secretscan:allow: this is the detection pattern, not a key
    _p("aws-access-key-id", "high", r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b",
       gate=lambda ln: "AKIA" in ln or "ASIA" in ln),
    _p("github-token", "high",
       r"\bgh[posru]_[A-Za-z0-9]{36,}\b|\bgithub_pat_[0-9A-Za-z_]{22,}\b",
       gate=lambda ln: "_" in ln and ("gh" in ln or "github_pat_" in ln)),
    _p("slack-token", "high", r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b",
       gate=lambda ln: "xox" in ln),
    _p("slack-webhook", "high",
       r"https://hooks\.slack\.com/services/[A-Za-z0-9/]+",
       gate=lambda ln: "https://hooks.slack.com/services/" in ln),
    _p("google-api-key", "high", r"\bAIza[0-9A-Za-z_-]{35}\b",
       gate=lambda ln: "AIza" in ln),
    _p("gcp-oauth-secret", "medium", r"\bGOCSPX-[0-9A-Za-z_-]{20,}\b",
       gate=lambda ln: "GOCSPX-" in ln),
    _p("stripe-key", "high", r"\b[rsp]k_(?:live|test)_[0-9A-Za-z]{20,}\b",
       gate=lambda ln: "k_live_" in ln or "k_test_" in ln),
    _p("anthropic-key", "high", r"\bsk-ant-[A-Za-z0-9-]{20,}\b",
       gate=lambda ln: "sk-ant-" in ln),
    _p("openai-key", "high", r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b",
       gate=lambda ln: "sk-" in ln),
    _p("npm-token", "high", r"\bnpm_[A-Za-z0-9]{36}\b",
       gate=lambda ln: "npm_" in ln),
    _p("twilio-key", "high", r"\bSK[0-9a-fA-F]{32}\b",
       gate=lambda ln: "SK" in ln),
    _p("sendgrid-key", "high", r"\bSG\.[A-Za-z0-9_-]{16,}\.[A-Za-z0-9_-]{16,}\b",
       gate=lambda ln: "SG." in ln),
    _p("jwt", "high",
       r"\beyJ[A-Za-z0-9_-]{6,}\.eyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}",
       gate=lambda ln: ".eyJ" in ln),
    _p("basic-auth-url", "high",
       r"\b[a-zA-Z][a-zA-Z0-9+.-]*://[^/\s:@]+:[^/\s:@]{4,}@",
       gate=lambda ln: "://" in ln and "@" in ln,
       anchored=dict(run=r"[a-zA-Z0-9+.-]+", literal="://", start=r"\b[a-zA-Z]")),
]

# The context-free high-entropy net. Requires mixed character classes (lower +
# upper + digit) which excludes the two biggest false-positive families —
# single-case hex hashes (git SHAs, sha256 checksums) and ALL-CAPS constants.
# `/` is deliberately NOT in the class: it is the URL/path separator, and
# including it turned every long URL path into a false hit. A standard-base64
# secret (which uses `/`) is caught by assignment context or a vendor format
# instead; base64url tokens (the modern default) use `-_` and still match.
#
# The LOOKBEHIND excludes `=` from the token class but NOT from itself
# (320/290, 2026-09-18) — found while tightening the URL carve-out to leave a
# query string live: `sig=<value>` (or any `key=value` under a key
# SECRET_KEY_RX doesn't recognise) could never start a match, because the
# lookbehind treated a preceding `=` as "still inside the previous token" the
# same way it treats a preceding letter/digit. That made every unnamed
# `key=value` assignment invisible to this net EVERYWHERE, not just in a URL
# query — the exact shape a signed-URL credential takes. The LOOKAHEAD still
# excludes `=` (unchanged): that half stops a match ending mid-way through a
# base64 blob's own `==` padding, which is a different case (the padding is
# consumed by `={0,2}` and read as trailing, never leading). This is a
# monotonic widening — it can only ADD matches a preceding `=` used to hide,
# never remove one that fired before — so the blocking set does not shrink.
HIGH_ENTROPY_RX = re.compile(r"(?<![A-Za-z0-9+_-])[A-Za-z0-9+_-]{32,}={0,2}(?![A-Za-z0-9+=_-])")
# The shortest line HIGH_ENTROPY_RX can match in — the `{32,}` above, restated
# so scan_lines can skip the regex on shorter lines (110/130). A test pins it
# to the pattern, so the two cannot drift apart.
HIGH_ENTROPY_MIN_LEN = 32
HIGH_ENTROPY_MIN = 4.0        # bits/char; random base64 sits ~5.0, prose ~3-4
ASSIGNED_ENTROPY_MIN = 3.0    # assigned values get context, so a lower bar

# A line naming PUBLIC key material — a public key or certificate is meant to be
# shared, so its high-entropy body is not a secret. Suppress the entropy net on
# these lines. Private-key indicators are deliberately absent: a `private_key:`
# line must still flag.
#
# COUNTED since 2026-08-09 (`Tally.public_key_spans`), which is the only thing
# that changed: the suppression is the same regex over the same per-line scope,
# but the entropy spans it writes off are now reported instead of vanishing.
# It is the WIDEST suppression in the tool — one keyword anywhere on a line
# exempts every entropy span on it — which is exactly why the count matters:
# `public_key` sitting in a comment beside a real credential is the growth path,
# and a reader can now see the number climb.
PUBLIC_KEY_RX = re.compile(
    r"(?i)\b(?:ssh-(?:ed25519|rsa|dss)|ecdsa-sha2[\w-]*|public[_-]?key|pubkey"
    r"|sshkey|authorized_keys)\b"
    r"|-----BEGIN (?:PUBLIC KEY|CERTIFICATE|[A-Z ]*PUBLIC)")

# 320/790 — the BODY of a PEM public certificate or public key. `PUBLIC_KEY_RX`
# is per line, so it exempts the `-----BEGIN CERTIFICATE-----` line and nothing
# under it: each base64 body line is 64 mixed-class characters with no keyword
# beside it, and tripped the entropy net one finding per line (a fresh 14-line
# P-256 certificate gave 8). A comment cannot go inside a PEM block, so a child
# had only a whole-file `.secretscanignore` — which blinds EVERY rule to the
# file, a private key pasted in later included.
#
# So the block is recognised as a unit and its body lines are handed to the SAME
# carve-out, counted in the same `Tally.public_key_spans` field (no new field,
# so the summary line's field set is unchanged). Nothing else is widened: it is
# the entropy pass only; named and assigned rules still run on every body line.
#
# Every condition is a way to FAIL CLOSED, because this is a blind spot and a
# private key is what it must never cover:
#   * the label is exactly `CERTIFICATE` or `PUBLIC KEY` (a `PRIVATE KEY`
#     header, whatever its prefix, is not a label here and opens nothing);
#   * the block must CLOSE with the matching END line — an unterminated BEGIN
#     suppresses nothing, rather than suppressing to end of file;
#   * it must close within `PEM_MAX_BODY_LINES`, which also bounds the buffer;
#   * every line between is pure base64 (`A-Za-z0-9+/=`) of at most
#     `PEM_MAX_LINE` characters (RFC 7468 §3), consecutive in the file. One
#     stray line (a `password=…`, a private-key header, a blank, a gap in the
#     line numbers of a staged diff) voids the WHOLE block, not just that line;
#   * the decoded body must be one DER SEQUENCE whose length accounts for every
#     byte and whose FIRST element is itself a SEQUENCE — the shape an X.509
#     certificate (tbsCertificate) and a SubjectPublicKeyInfo
#     (AlgorithmIdentifier) share, and which PKCS#8, PKCS#1 and SEC1 private
#     keys (first element an INTEGER) do not have. So a private key mislabelled
#     or glued under a certificate header is not exempt. (Stdlib only: tags and
#     lengths, no certificate parsing; a heuristic on shape, not a validation.)
#
# PEM_MAX_BODY_LINES is grounded in certificate size, not in the one certificate
# that prompted this: openssl emits 64 base64 characters (48 DER bytes) per line,
# so a bound in DER bytes converts directly. Ordinary web certificates are
# 1-3 KiB (20-60 lines); a post-quantum certificate carrying an SLH-DSA-256f
# signature is about 50 KB (about 1,050 lines), the largest signature in the
# standardised sets. 2048 lines is 96 KiB of DER, about twice that, with the
# buffer for it held at 2048 x 76 characters, about 150 KiB, per open block.
PEM_PUBLIC_LABELS = ("CERTIFICATE", "PUBLIC KEY")
PEM_MAX_BODY_LINES = 2048
PEM_MAX_LINE = 76
_PEM_BEGIN_RX = re.compile(
    "-----BEGIN (" + "|".join(PEM_PUBLIC_LABELS) + ")-----")
_PEM_BODY_RX = re.compile(r"[A-Za-z0-9+/]+={0,2}")


def _is_pem_body_line(stripped: str) -> bool:
    return len(stripped) <= PEM_MAX_LINE and bool(_PEM_BODY_RX.fullmatch(stripped))


def _der_element(raw: bytes, at: int):
    """The (tag, content start, content end) of the DER element at `at`, or None
    if its header is truncated, its length is not a definite one of one to four
    octets, or its content runs past the end of `raw`."""
    if len(raw) < at + 2:
        return None
    tag, first = raw[at], raw[at + 1]
    if first < 0x80:
        start, length = at + 2, first
    elif 0x81 <= first <= 0x84:
        start = at + 2 + (first - 0x80)
        if len(raw) < start:
            return None
        length = int.from_bytes(raw[at + 2:start], "big")
    else:
        return None
    if start + length > len(raw):
        return None
    return tag, start, start + length


def _is_der_sequence(raw: bytes) -> bool:
    """True if `raw` is exactly one DER SEQUENCE (tag 0x30, a length that
    accounts for every byte) whose FIRST element is itself a SEQUENCE that fits
    inside it. That is the shape a certificate (tbsCertificate) and a
    SubjectPublicKeyInfo (AlgorithmIdentifier) share, and no private-key DER
    form has it: PKCS#8, PKCS#1 and SEC1 all open with an INTEGER version. The
    outer-SEQUENCE test alone let a private key's body pass as a certificate."""
    outer = _der_element(raw, 0)
    if outer is None or outer[0] != 0x30 or outer[2] != len(raw):
        return False
    inner = _der_element(raw, outer[1])
    return inner is not None and inner[0] == 0x30 and inner[2] <= outer[2]


def _pem_body_is_der(lines: list[str]) -> bool:
    try:
        raw = base64.b64decode("".join(lines), validate=True)
    except (binascii.Error, ValueError):
        return False
    return _is_der_sequence(raw)


def pem_exempt_stream(items):
    """Pass `items` — `(lineno, text, extra)` triples in file order — through,
    appending a fourth element: True for a body line of a closed, valid
    public-certificate / public-key PEM block (see the 320/790 comment), else
    False.

    A block's body can only be judged at its END line, so its lines are held
    (at most `PEM_MAX_BODY_LINES`) and released together; every other line passes
    through at once. Order is preserved. A line that voids an open block is
    released with the block as non-exempt and then re-read as an ordinary line,
    so a certificate that follows an unterminated one still gets its own span
    (a chain: each certificate stands alone)."""
    label = None
    held: list = []
    last = 0
    for item in items:
        lineno, text = item[0], item[1]
        while True:
            if label is None:
                if "-----BEGIN" in text:
                    m = _PEM_BEGIN_RX.fullmatch(text.strip())
                    if m:
                        label, held, last = m.group(1), [], lineno
                yield (*item, False)
                break
            stripped = text.strip()
            if lineno == last + 1:
                if stripped == f"-----END {label}-----":
                    ok = bool(held) and _pem_body_is_der(
                        [h[1].strip() for h in held])
                    for h in held:
                        yield (*h, ok)
                    yield (*item, False)
                    label, held = None, []
                    break
                if len(held) < PEM_MAX_BODY_LINES and _is_pem_body_line(stripped):
                    held.append(item)
                    last = lineno
                    break
            for h in held:      # voided: release as ordinary lines, re-read this one
                yield (*h, False)
            label, held = None, []
    for h in held:               # EOF inside an open block: never closed
        yield (*h, False)


def pem_body_lines(numbered_lines) -> frozenset[int]:
    """Line numbers of the exempt PEM body lines among `numbered_lines`
    (`(lineno, text)` pairs). A block must be seen whole, with consecutive line
    numbers, to count."""
    return frozenset(n for n, _t, _x, ok in
                     pem_exempt_stream((n, t, None) for n, t in numbered_lines) if ok)


_NO_PEM_LINES: frozenset[int] = frozenset()

# E3 (ruled 2026-08-04, Mike): a PUBLIC-KEY FINGERPRINT is public material by
# definition — it is the value you publish so someone can verify a key they were
# given, and it is one-way, so possessing it grants nothing. It was blocking:
# `ssh-keygen -l` prints `SHA256:<43 base64url-ish chars>`, which is 32+ chars of
# mixed classes at entropy ~5.9 and therefore a high-entropy hit on any line that
# does not also happen to name `ssh-ed25519`. Two of eight findings in one child
# were this shape, and widening a security scanner's blind spot is atelier's call
# rather than the child's — which is why it was correctly left unfixed there.
#
# WHOLE SHAPE, NEVER FRAGMENT — the standing lesson of 2026-07-28, where four
# real credentials walked past suppressions that matched on a fragment (a word
# boundary, an opening brace, a stray bracket). So this does NOT suppress "a line
# mentioning SHA256", and does NOT suppress "a value that looks base64". It
# matches the ENTIRE fingerprint token — the algorithm prefix, the separator, and
# a body of exactly the digest's length in that encoding — and suppresses only an
# entropy span lying inside such a token. A `SHA256:` prefix in front of a body
# of the WRONG length is not a fingerprint and still flags: that is a credential
# wearing a fingerprint's hat, and it is the direction the canaries pin.
#
# Both ruled spellings:
#   SHA256:<43 base64 chars>            ssh-keygen -l, OpenSSH ≥ 6.8 default
#   [MD5:]aa:bb:…:pp   (16 hex pairs)   the legacy hex form, still emitted by
#                                       ssh-keygen -E md5 and by many appliances
# The MD5 form produces no finding to suppress TODAY — `:` is not in
# `HIGH_ENTROPY_RX`'s character class, so the colon-joined pairs never form a
# span. It is recognised anyway, and canaried, so that a future widening of the
# context-free net cannot start flagging it without someone deciding to.
FINGERPRINT_RX = re.compile(
    r"(?i)"
    r"\bSHA256:[A-Za-z0-9+/]{43}=?(?![A-Za-z0-9+/=])"
    r"|\bMD5:(?:[0-9a-f]{2}:){15}[0-9a-f]{2}\b"
    r"|(?<![0-9a-f:])(?:[0-9a-f]{2}:){15}[0-9a-f]{2}(?![0-9a-f:])")


# A published URL is not a credential (320/290, filed via a private child's
# `secretscan:allow`-per-line workaround, 2026-09-10). A documentation link's
# path commonly hyphenates several words into one segment (a mixed-case
# "how to configure X" page slug), which is exactly `HIGH_ENTROPY_RX`'s shape
# — 32+ mixed-class characters with no separator — so a rigorously-sourced
# document blocked on its own citations.
#
# Recognised whole-run: a scheme (`scheme://`) followed by a run that is
# actually host/path-SHAPED — containing a `.` (a hostname) or a `/` (a path)
# after the scheme. That shape requirement is deliberate, not decorative: a
# bare `http://` glued onto a real credential with no dot and no slash
# (`http://Gk8xQvie2mNfR7pLzW3dTaHb`) does NOT match, and the value is still
# scored as an entropy candidate — so gluing a scheme prefix alone buys no
# suppression.
#
# SCOPED TO SCHEME+HOST+PATH ONLY (tightened 2026-09-18, on a coordinator's
# ruling before merge). The exclusion originally covered the whole matched
# run including any query string or fragment — and a signed-URL query value
# is EXACTLY where credentials live in practice (`?sig=`, `?token=`,
# `#access_token=` from an OAuth implicit-grant redirect). A convincing host
# and path in front of an unnamed query/fragment secret
# (`https://api.example.com/download?sig=<realsecret>`) made that credential
# invisible to the context-free net, which is not an acceptable residual for
# a scanner whose whole job is finding exactly that shape. Fixed at the root
# rather than documented as a residual: everything from the FIRST `?` or `#`
# in the matched run is excluded from the URL span and stays a live entropy
# candidate, scored exactly as if no URL were present — the assigned-secret
# rule also still runs over it unconditionally, unaffected either way.
#
# RESIDUAL RISK, stated rather than closed: this is a cheap shape check on the
# host+path portion only, not proof of a real URL. A value glued behind a
# CONVINCING host and PATH with no query/fragment at all
# (`https://example.com/<realsecret>`) still reads as URL-shaped and that
# credential is hidden from this net — the same way any suppression in this
# file is bypassed by faking the shape it trusts. What keeps that survivable:
# a credential named by a credential key anywhere on the line (`token:`,
# `api_key=`, …) is still caught by the assigned-secret rule regardless of
# URL shape, so the one thing this carve-out cannot see through is an UNNAMED
# credential sitting in a URL's PATH specifically (not its query or fragment,
# both now live). Narrowing further (e.g. requiring a real TLD, or excluding
# only the path's non-final segments) is available if that narrower residual
# is ever measured live; it is not narrowed pre-emptively because a floor
# fitted to a hypothetical is not a floor (`ground-numeric-limits`).
URL_RX = anchoredrx.AnchoredRx(
    re.compile(r"\b[A-Za-z][A-Za-z0-9+.-]*://[^\s<>\"']+"),
    run=r"[A-Za-z0-9+.-]+", literal="://", start=r"\b[A-Za-z]")


def _url_spans(line: str) -> list[tuple[int, int]]:
    """Character ranges on this line occupied by a host/path-shaped URL's
    SCHEME+HOST+PATH portion only — never its query string or fragment, which
    stay live entropy candidates (see the module comment above `URL_RX`)."""
    spans = []
    for m in URL_RX.finditer(line):
        whole = m.group(0)
        scheme_end = whole.index("://") + 3
        cut = len(whole)
        for sep in "?#":
            idx = whole.find(sep, scheme_end)
            if idx != -1:
                cut = min(cut, idx)
        host_and_path = whole[scheme_end:cut]
        if "." not in host_and_path and "/" not in host_and_path:
            continue  # not host/path-shaped — not treated as a URL at all
        spans.append((m.start(), m.start() + cut))
    return spans


def _inside_url(span: tuple[int, int], urls: list[tuple[int, int]]) -> bool:
    return any(start <= span[0] and span[1] <= end for start, end in urls)


def _fingerprint_spans(line: str) -> list[tuple[int, int]]:
    """Character ranges on this line occupied by a whole public-key fingerprint."""
    return [m.span() for m in FINGERPRINT_RX.finditer(line)]


def _inside_fingerprint(span: tuple[int, int],
                        fingerprints: list[tuple[int, int]]) -> bool:
    return any(start <= span[0] and span[1] <= end
               for start, end in fingerprints)

# A value that is a code reference — a bare/dotted identifier or a function call
# — is a variable, not a literal secret. `password=admin_password`,
# `self.conn.password`, `get_secret()` are the dominant false positives in real
# source. Identifier-shaped values are rejected UNLESS they carry the mixed
# upper+lower+digit signature of real key material (so `Gk8xQvie2mNfR7pL` stays).
IDENTIFIER_RX = re.compile(r"[A-Za-z_][A-Za-z0-9_.]*$")

# An absolute, multi-segment, path-shaped value — `/run/secrets/netbox_key`.
# Deliberately excludes the base64 padding/alphabet extras (`+`, `=`) so a
# standard-base64 secret cannot masquerade as a path on shape alone.
ABS_PATH_RX = re.compile(r"/(?:[A-Za-z0-9._@-]+/)+[A-Za-z0-9._@-]+")

# A code expression used as a value: `get_secret()`, `os.getenv("KEY")`,
# `inv.effective(device).factory_password`, `function(a){return`. Defined by its
# CHARACTER SET — code is built from identifiers, dots, calls, subscripts and
# braces. `{}` and `$` are in the set because JS puts them in ordinary
# expressions (`encodeShortlist({`, jQuery's `$`); omitting them flagged
# vendored minified JS as credentials. Random key material still fails the set:
# it carries `% # ! @ +`, which no identifier expression contains.
# `-` is admitted because prose fragments land here too — a comment reading
# `# without password= (live-proven 2026-07-04)` yields the value `(live-proven`.
# It stays safe because a value must ALSO contain a bracket to be called code,
# and the base64url alphabet (`A-Za-z0-9-_`) has no brackets at all.
CODE_EXPR_RX = re.compile(r"[A-Za-z0-9_.\-()\[\]{}$'\"]+")

# kebab-case is the same class of thing as snake_case: a slug or enum value
# (`yes-access-request`), not key material. IDENTIFIER_RX covers the snake form,
# but `-` is not an identifier character so the hyphenated twin needs saying.
# Deliberately letters-only — admitting digits would swallow lowercase hex
# secrets. That was recorded here as a gap left open; it is now closed for the
# path that matters, one level up: in assigned-secret context the E6c carve-outs
# below run FIRST, so neither this rule nor IDENTIFIER_RX can suppress a
# credential-shaped value under a credential-named key.
SLUG_RX = re.compile(r"[a-z]+(?:[-_][a-z]+)+")

# ---------------------------------------------------------------------------
# E6c — in credential-key context, low character variety is NOT evidence of
# innocence (ruled 2026-07-28, generalising the SF1+SF2 carve-outs).
#
# Every suppression above reads low character variety as innocence: the
# identifier rule, the slug rule, the mixed-class hoist, the entropy floor. That
# is sound where there is no context — a bare single-case hex run really is
# usually a git SHA. It is NOT sound once a key name has already said
# "credential": the key name has done the filtering, so variety carries no
# further information about innocence, and reading it as innocence is how these
# slipped past (live-probed 2026-07-28: of six credential-shaped assignments,
# four passed clean — both passphrase spellings and both letter-leading hex
# values — while only the digit-leading hex and the mixed-class password
# flagged).
#
# The rule is implemented as WHOLE-SHAPE carve-outs rather than by switching the
# suppressions off wholesale, because the suppressions still have a real job in
# this context: `password=admin_password` and `password=get_secret()` are code
# references, not credentials, and re-flagging them would be the cry-wolf the
# 2026-07-28 fragment fixes were about. What separates the two is not character
# variety but whole shape — LENGTH and PART COUNT. Both thresholds below come
# from the ruling and from HIGH_ENTROPY_RX's existing 32; neither is fitted to a
# measurement.
#
# These are the ruled shapes generalised, not an exhaustive enumeration. A new
# low-variety credential shape belongs here, not in a new suppression exception.

# An unbroken alphanumeric run at key-material length. Covers the ruled shape
# (32+ lowercase hex, letter-leading AND digit-leading) and its siblings the
# ruling did not have to enumerate: uppercase hex, base32 TOTP seeds, long
# single-case alnum keys. Names simply do not run 32 characters unbroken; keys
# do. Cry-wolf case is the git SHA, which the ruling weighed: SHAs rarely sit
# assigned to a credential-named key, and in the context-free net (where they do
# live) nothing changes.
LOW_VARIETY_KEY_RX = re.compile(r"[A-Za-z0-9]{32,}")

# Four or more separator-joined lowercase words — the diceware/passphrase shape
# real people really use. Both spellings, because the kebab exemption (SLUG_RX)
# and its snake twin (IDENTIFIER_RX) each swallow one of them. Four parts, not
# two or three: `admin_password`, `require_message_auth` and
# `yes-access-request` are names, and stay suppressed.
PASSPHRASE_RX = re.compile(r"[a-z]+(?:[-_][a-z]+){3,}")


def _low_variety_credential_shape(value: str) -> bool:
    """E6c: a whole shape that is credential material whose ONLY innocence
    signal is low character variety. True here means the variety-reading gates
    below do not get a say."""
    return (LOW_VARIETY_KEY_RX.fullmatch(value) is not None
            or PASSPHRASE_RX.fullmatch(value) is not None)


# ---------------------------------------------------------------------------
# E6b — the advisory tier (ruled 2026-07-28; consumer ruled 2026-08-04).
#
# A finding's RESPONSE is separate from what the scan believes about it — the
# split `method/GUARDS.md` names, and the one CodeQL ships (@precision describes,
# @problem.severity decides). Here it takes its simplest useful form: two
# responses, and only one of them touches the exit code.
RESPONSE_BLOCK = "block"
RESPONSE_ADVISORY = "advisory"

# The context-free rule the tier exists to make affordable. Its detection is
# E6c's ruled whole shape — an unbroken 32+ alphanumeric run is key material,
# because names do not run 32 characters unbroken — applied on the path E6c
# deliberately left alone ("in the context-free net, where SHAs live, nothing
# changes"). E6b is what changes it: the run is now SEEN and REPORTED there,
# and the mixed-class requirement decides only whether it BLOCKS.
#
# No new threshold is introduced, and that is deliberate — a floor fitted to
# whatever the tree currently measures proves nothing. The length comes from
# `LOW_VARIETY_KEY_RX`, already ruled; the mixed-class split comes from
# `HIGH_ENTROPY_RX`, already there. What is new is only the response.
LOW_VARIETY_RULE = "low-variety-entropy"

# 115/380 — the one check that still runs on a file a `.secretscanignore` glob
# skips. Advisory, like the rule above; see `scan_exempt_lines`.
EXEMPT_PRIVATE_KEY_RULE = "exempt-private-key"

# The line `render_human` prints so a reader — and `tools/floor.py`'s board —
# can both read the count off one run. floor.py matches this prefix rather than
# importing anything: the scanners are self-contained by design (one is
# copyable alone), so the coupling is a documented output contract, pinned from
# both sides by `test_floor.py::AdvisoryCountContract`.
ADVISORY_COUNT_PREFIX = "secretscan advisory:"


@dataclass
class Finding:
    path: str
    line: int
    rule: str
    kind: str          # "named" | "assigned" | "entropy"
    severity: str
    excerpt: str       # redacted — locates the hit, never re-leaks it
    # "block" | "advisory". Defaulted to block so a new rule that forgets to
    # say fails SAFE — into the gate, never out of it.
    response: str = RESPONSE_BLOCK

    @property
    def blocks(self) -> bool:
        return self.response == RESPONSE_BLOCK


def shannon(s: str) -> float:
    if not s:
        return 0.0
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())


def redact(value: str, kind: str) -> str:
    """A fingerprint precise enough to locate, useless to re-leak. For a named
    token we keep the recognisable prefix (e.g. `AKIA…`, already public-shaped);
    for entropy/assigned hits we surface only length + entropy."""
    if kind == "named":
        head = value[:4]
        return f"{head}… ({len(value)} chars)"
    return f"<{len(value)} chars, entropy {shannon(value):.1f}>"


def _has_mixed_classes(s: str) -> bool:
    return (any(c.islower() for c in s)
            and any(c.isupper() for c in s)
            and any(c.isdigit() for c in s))


def _is_placeholder(value: str) -> bool:
    low = value.lower()
    if low in PLACEHOLDER_EXACT:
        return True
    if any(sub in low for sub in PLACEHOLDER_SUBSTRINGS):
        return True
    if TEMPLATE_RX.search(value):
        return True
    # a run of one repeated character (xxxx, ****, ----) is never a real secret
    if len(set(value)) <= 1:
        return True
    return False


def _is_indirection(value: str) -> bool:
    return INDIRECTION_RX.match(value) is not None


def _looks_like_path(value: str) -> bool:
    # `private_key = /etc/ssl/server.key` names a file, not a secret.
    if " " not in value and not value.startswith("http") and "/" in value:
        if re.search(r"\.[A-Za-z0-9]{1,6}$", value) is not None:
            return True
        # An EXTENSIONLESS mount path is the secret-store form we actively want
        # people to use (`/run/secrets/netbox_key`, a K8s projected volume). The
        # extension requirement above meant those flagged as high-severity
        # secrets — so following Docker's recommended pattern is what turned a
        # repo red, while the plaintext value on the next line stayed green
        # (found 2026-07-28). Recognise absolute, multi-segment, path-shaped
        # values; guard with the SAME mixed-class + entropy signature the
        # high-entropy net uses, so a standard-base64 blob that merely contains
        # `/` still flags rather than passing as a path.
        if ABS_PATH_RX.fullmatch(value):
            return not any(_has_mixed_classes(seg) and shannon(seg) >= HIGH_ENTROPY_MIN
                           for seg in value.strip("/").split("/"))
    return False


def _looks_like_code_ref(value: str) -> bool:
    """A variable reference, attribute access or call — not a literal secret."""
    # The mixed upper+lower+digit signature of key material wins over every code
    # shape below — `Gk8xQvie2mNf` is a secret even though it is identifier-
    # shaped. Hoisted to the top so it guards the call/expression branch too.
    if _has_mixed_classes(value):
        return False
    # Testing for a stray `(` or `)` ANYWHERE was the same unclosed-marker bug as
    # TEMPLATE_RX above: the real NetBox SECRET_KEY carries `(` and `)` among its
    # random symbols and was written off as a function call (found 2026-07-28).
    # Require the whole value to be code-SHAPED instead — and to actually contain
    # a call/attribute/subscript, so a bare word still falls through to the
    # identifier branch and its own reasoning.
    if CODE_EXPR_RX.fullmatch(value) and re.search(r"[.()\[\]{}]", value):
        return True
    if SLUG_RX.fullmatch(value):
        return True
    # a bare or dotted identifier that lacks the mixed-class signature of key
    # material (admin_password, self.conn.password) — but NOT a mixed-class token
    # that merely happens to be alphanumeric (Gk8xQvie2mNf, a real secret shape)
    if IDENTIFIER_RX.match(value):
        return True
    return False


def _assigned_is_secret(value: str) -> bool:
    if len(value) < 6:
        return False
    if _is_placeholder(value) or _is_indirection(value) or _looks_like_path(value):
        return False
    # E6c, decided BEFORE every gate that reads character variety as innocence —
    # the code-ref/slug/identifier suppressions below AND the entropy floor,
    # which is itself a variety measure. Placeholder/indirection/path stay above
    # it deliberately: those are statements about what the value *is for*, not
    # about its variety, so `${DB_PASSWORD}` and `/run/secrets/x` keep passing.
    if _low_variety_credential_shape(value):
        return True
    if _looks_like_code_ref(value):
        return False
    # A value with whitespace-free high entropy, or mixed classes at length, is
    # credential-shaped. Short dictionary words assigned to `password=` are
    # weak/example creds, not the leak class this gate is for.
    if shannon(value) >= ASSIGNED_ENTROPY_MIN and (len(value) >= 12 or _has_mixed_classes(value)):
        return True
    return False


# --- per-rule pre-filters (roadmap 110/130, lever 4) ---------------------
#
# Each gate is a CHEAP test on the line that is NECESSARY for its rule to match:
# if the gate says no, the rule's regex provably has no match on that line, so
# skipping `finditer` changes nothing — same findings, same order, same counts.
# That is the only property a gate may have. A gate that could reject a line the
# rule would match is a silent false negative in a credential scanner, the
# worst failure this tool has, so every gate below is a literal (or fixed
# shape) the rule's own pattern text contains, never a guess about the data.
# A rule with no entry has no provable cheap necessary condition and always
# runs its full regex (fail open). Every literal here is case-sensitive because
# the pattern it comes from is — none of the NAMED rules carries `(?i)`.
# `test_secretscan.GatesAreNecessary` pins each gate against its rule.
#
# The `assigned` gate is deliberately vocabulary-free: SECRET_KEY_RX's fixed
# tail is `\b\s*[:=]\s*["']?<6+ value chars>`; this is the part from the
# `[:=]` on, necessary whatever key names are added later because it names no
# key. (Starting at `[:=]` means the regex engine only wakes at a colon or an
# equals sign, not at every word.)
_ASSIGNED_TAIL_RX = re.compile(r"""[:=]\s*["']?[^\s"'`,;:]{6}""")

# The gate table, DERIVED from the rules (160/720 GT2): each rule's gate is
# declared on the rule itself, above. This dict is the one runtime home
# `_active_named` reads, behind its memo, so patching `NAMED_GATES` and
# clearing `_ACTIVE_CACHE` switches gating off everywhere at once.
NAMED_GATES: dict[str, "object"] = {p.name: p.gate for p in NAMED
                                    if p.gate is not None}
_ACTIVE_CACHE: dict[frozenset[str], tuple] = {}


def _active_named(disabled: frozenset[str]) -> tuple:
    """`NAMED` with each rule's gate, minus the disabled rules, memoised per
    disabled-set."""
    if not isinstance(disabled, frozenset):   # a plain set worked before
        disabled = frozenset(disabled)
    got = _ACTIVE_CACHE.get(disabled)
    if got is None:
        got = _ACTIVE_CACHE[disabled] = tuple(
            (p, NAMED_GATES.get(p.name)) for p in NAMED
            if p.name not in disabled)
    return got


def _record(findings: list[Finding], tally: Tally | None, finding: Finding) -> None:
    """Append `finding` unless the run-wide materialization cap (020/370,
    `MAX_MATERIALIZED_FINDINGS`) has been reached — in which case
    `tally.take_finding_slot` has already counted it and there is nothing
    left for the caller to hold. The single choke point every finding in
    `scan_lines` passes through, so the cap cannot be forgotten at a new call
    site."""
    if tally is None or tally.take_finding_slot(finding.response):
        findings.append(finding)


def scan_lines(path: str, numbered_lines: list[tuple[int, str]],
               disabled: frozenset[str] = frozenset(),
               tally: Tally | None = None,
               pem_lines: frozenset[int] | None = None) -> list[Finding]:
    """The scanning engine. `numbered_lines` pairs each line of text with its
    REAL line number in the file — which need not be sequential or start at 1.
    That is the shape `--staged` mode needs (320/290): only a diff's added
    lines are scanned, but a finding must still point at the line it actually
    sits on, not at its position in a blob of concatenated fragments.
    `scan_text` below is the sequential-numbering convenience wrapper every
    whole-file caller uses.

    `pem_lines` (320/790) is the set of line numbers that are the body of a
    public certificate / public key PEM block, whose entropy spans take the
    public-key carve-out below. None means "work it out from `numbered_lines`":
    a block counts only if every line of it, BEGIN to END, is present with
    consecutive numbers. A caller that sees only part of a file (a staged diff's
    added lines, one line at a time) passes the set it derived from the whole
    file instead."""
    findings: list[Finding] = []
    if pem_lines is None:
        pem_lines = pem_body_lines(numbered_lines)
    # Line -> allowance scope, collected as we go. The subtraction happens
    # AFTER dedupe (rule b, find first and subtract second): suppressing at
    # match time would also count entropy hits that dedupe was about to drop,
    # inflating the very number this exists to make trustworthy.
    allow_by_line: dict[int, str] = {}
    named = _active_named(disabled)
    for lineno, line in numbered_lines:
        # The marker regex opens with the literal marker text, so a line
        # without it cannot carry a marker (110/130, lever 4).
        scope = parse_allow(line) if ALLOW_MARKER in line else None
        if scope is not None:
            allow_by_line[lineno] = scope

        for pat, gate in named:
            if gate is not None and not gate(line):
                continue
            for m in pat.regex.finditer(line):
                _record(findings, tally, Finding(path, lineno, pat.name, "named",
                                                 pat.severity, redact(m.group(0), "named")))

        if "assigned" not in disabled and _ASSIGNED_TAIL_RX.search(line):
            for m in SECRET_KEY_RX.finditer(line):
                value = m.group(2)
                if _assigned_is_secret(value):
                    _record(findings, tally, Finding(path, lineno, "assigned-secret",
                                                     "assigned", "high",
                                                     redact(value, "assigned")))

        # The public-key line carve-out is applied INSIDE the entropy pass
        # rather than around it (2026-08-09), so the spans it writes off can be
        # counted — rule (b) of `method/GUARDS.md`: find first, subtract second,
        # report the subtraction. Skipping the pass wholesale suppressed exactly
        # the same spans, but silently, and this was the last silent subtraction
        # in the tool. The suppression itself is unchanged: same regex, same
        # per-line scope, same precedence ahead of the fingerprint carve-out, so
        # a line that is both counts once, as a public-key line.
        #
        # 110/130 (lever 4): the three line-level lookups below — public-key
        # keyword, fingerprint spans, URL spans — are pure functions of the
        # line that are read ONLY inside the loop over entropy matches. So the
        # (rare) entropy match is found first, and they are computed only if
        # there is one; with none, the loop body would never have run. A match
        # needs 32 characters, so a shorter line cannot have one. The matches
        # stay a lazy iterator (peek one, chain the rest) — a list would hold
        # every match of an overlong line at once, which 020/370 forbids.
        entropy = (HIGH_ENTROPY_RX.finditer(line) if len(line) >= HIGH_ENTROPY_MIN_LEN
                   else iter(()))
        first = next(entropy, None)
        # GT4 (160/720): wrapped, not `continue`d past. A later step added
        # to this loop body would otherwise be skipped on every line with
        # no entropy match - nearly all of them - and nothing would say so.
        if first is not None:
            public_key_line = lineno in pem_lines or bool(PUBLIC_KEY_RX.search(line))
            fingerprints = () if public_key_line else _fingerprint_spans(line)
            url_spans = () if public_key_line else _url_spans(line)
            for m in itertools.chain((first,), entropy):
                span = m.group(0)
                if public_key_line:
                    if tally is not None:
                        tally.note_public_key_span()
                    continue
                # E3, checked BEFORE the rule split so the carve-out costs one
                # decision rather than two, and is counted once either way.
                if _inside_fingerprint(m.span(), fingerprints):
                    if tally is not None:
                        tally.note_fingerprint()
                    continue
                # 320/290 — a token inside a published URL's scheme+host+path is
                # not an entropy candidate at all, neither blocking nor advisory.
                # Its query string and fragment are NOT covered by this span (see
                # `URL_RX`/`_url_spans`), so a token there still reaches the
                # checks below exactly as if no URL were present.
                if _inside_url(m.span(), url_spans):
                    if tally is not None:
                        tally.note_url_token()
                    continue
                if _is_placeholder(span):
                    continue
                if _has_mixed_classes(span):
                    # The blocking net, byte for byte as it has always been.
                    if ("high-entropy" not in disabled
                            and shannon(span) >= HIGH_ENTROPY_MIN):
                        _record(findings, tally, Finding(path, lineno, "high-entropy",
                                                         "entropy", "medium",
                                                         redact(span, "entropy"),
                                                         RESPONSE_BLOCK))
                elif (LOW_VARIETY_RULE not in disabled
                        and LOW_VARIETY_KEY_RX.fullmatch(span)):
                    # E6b — the coverage that did not exist before the tier.
                    _record(findings, tally, Finding(path, lineno, LOW_VARIETY_RULE,
                                                     "entropy", "medium",
                                                     redact(span, "entropy"),
                                                     RESPONSE_ADVISORY))
    # A named/assigned hit and a bare entropy hit often fire on the same token;
    # keep the more specific one so the report isn't doubled.
    if not findings:
        return []
    kept: list[Finding] = []
    for f in _dedupe_same_span(findings):
        scope = allow_by_line.get(f.line)
        if scope is not None and scope in ("", f.rule):
            if tally is not None:
                tally.note_marker(f.rule)
            continue
        kept.append(f)
    return kept


def scan_text(path: str, text: str,
              disabled: frozenset[str] = frozenset(),
              tally: Tally | None = None) -> list[Finding]:
    """Scan a whole text blob, numbering lines sequentially from 1 — the
    whole-file/whole-tree shape. Every non-staged caller (and every existing
    test) uses this; `scan_lines` is the shared engine underneath it."""
    return scan_lines(path, list(enumerate(text.splitlines(), start=1)),
                      disabled, tally)


def _dedupe_same_span(findings: list[Finding]) -> list[Finding]:
    by_line: dict[int, list[Finding]] = {}
    for f in findings:
        by_line.setdefault(f.line, []).append(f)
    kept: list[Finding] = []
    for line_findings in by_line.values():
        has_specific = any(f.kind in ("named", "assigned") for f in line_findings)
        for f in line_findings:
            if f.kind == "entropy" and has_specific:
                continue
            kept.append(f)
    return kept


def _looks_binary(data: bytes) -> bool:
    return b"\x00" in data[:8192]


ALL_RULES = frozenset({p.name for p in NAMED}
                      | {"assigned", "high-entropy", LOW_VARIETY_RULE,
                         EXEMPT_PRIVATE_KEY_RULE})


IgnoreFileError = allowmarker.IgnoreFileError


def load_ignore_globs(root: Path) -> list[str]:
    """Globs from `.secretscanignore`, each of which MUST carry a stated reason.
    Single-sourced (115/080 part 2) in `tools/allowmarker.py`; this
    scanner supplies only its own ignore-file name."""
    return allowmarker.load_ignore_globs(root, ".secretscanignore")


def _ignored(rel: str, globs: list[str]) -> bool:
    return allowmarker.ignored(rel, globs)


def _walk_files(base: Path):
    """Every regular file under `base`, streamed one at a time. Single-sourced
    (115/080 part 1) in `tools/filewalk.py`, which every one of the eleven
    scanners that used to define this independently now imports instead —
    see that module's docstring for the mechanism, the 020/370/020/380
    history, and the 020/160 (E9) linked-worktree skip. `SKIP_DIR_NAMES` is
    this scanner's own per-guard parameter, passed in rather than shared."""
    return filewalk.walk_files(base, SKIP_DIR_NAMES,
                               read_tracked_under_skip=True)


def _classify_files(paths: list[Path], root: Path, globs: list[str]):
    """Yield `(path, root-relative path, ignored)` for every file under `paths`.
    `ignored` is True when a `.secretscanignore` glob names it. The one place
    that decision is made, so the skip and the exempt-file check (115/380) can
    never disagree about which files are exempt."""
    for base in paths:
        candidates = [base] if base.is_file() else _walk_files(base)
        for p in candidates:
            # Resolve BOTH sides so rel is root-relative no matter the caller's
            # CWD (2026-07-11 review N3): floor.yml runs `--root repo repo` from
            # the workspace, where the unresolved relative_to raised and the
            # fallback quietly produced CWD-relative paths — so the scanned
            # repo's own .secretscanignore globs never matched.
            try:
                rel = str(p.resolve().relative_to(root.resolve()))
            except ValueError:
                rel = str(p)
            yield p, rel, _ignored(rel, globs)


def iter_files(paths: list[Path], root: Path, globs: list[str],
               tally: Tally | None = None):
    for p, rel, ignored in _classify_files(paths, root, globs):
        if ignored:
            if tally is not None:
                tally.files_by_glob += 1
            continue
        yield p, rel


# Streaming-read tuning (020/370, the machine-thrash defect). Every constant
# here is a FIXED size, chosen once and independent of the file or tree being
# scanned — that independence is the entire fix. `LINE_WINDOW_OVERLAP` is
# grounded in the patterns this file matches, not fitted to any incident's
# measurement: every NAMED format has a realistic token length under a few
# hundred characters, and even an unusually large JWT (the one genuinely
# open-ended NAMED shape) runs to at most a few KiB in practice — 64 KiB is
# generous by two further orders of magnitude on top of that.
READ_CHUNK_BYTES = 1 * 1024 * 1024        # raw bytes read from disk at a time
LINE_WINDOW_BYTES = 4 * 1024 * 1024       # a physical line (no '\n' in sight)
                                          # longer than this is scanned in
                                          # WINDOWS rather than buffered whole
LINE_WINDOW_OVERLAP = 64 * 1024           # carried from one window into the
                                          # next so a match straddling the cut
                                          # is still whole in one of the two


def _iter_numbered_lines(path: Path):
    """Yield `(lineno, text, is_final_window)` for every physical line in
    `path`, reading and decoding it in fixed-size chunks so peak memory for
    ONE file is bounded by `LINE_WINDOW_BYTES + LINE_WINDOW_OVERLAP` —
    independent of the file's total size or its longest line. Yields nothing
    for a file that looks binary (checked on the first chunk only, so a huge
    binary file is never read past `READ_CHUNK_BYTES`).

    This replaces the old `read_bytes()` → whole `str` → `splitlines()` list,
    which held the file THREE TIMES OVER at once — the dominant driver behind
    020/370's ~9 GB incident (measured while building this fix: a clean
    32 MB/400,000-line synthetic file alone peaked the old code at 134 MB,
    ~7.5x the file's size, from exactly that shape).

    `is_final_window` is False for every window of an overlong line except
    its last (or its only one, for an ordinary line) — `_scan_file` uses it
    to dedupe a match that straddles a window boundary and would otherwise
    be reported twice, once from each window's copy of the overlap."""
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    lineno = 1
    pending = ""
    with open(path, "rb") as fh:
        first_chunk = True
        while True:
            chunk = fh.read(READ_CHUNK_BYTES)
            if first_chunk:
                first_chunk = False
                if _looks_binary(chunk):
                    return
            if not chunk:
                break
            pending += decoder.decode(chunk)
            # Walk an offset forward and cut `pending` once per chunk. The
            # old `pending = pending[nl + 1:]` per line re-copied the whole
            # remainder for every line: quadratic in lines-per-chunk
            # (110/140; linkscan's reader had the same shape, 110/120).
            start = 0
            while True:
                nl = pending.find("\n", start)
                if nl == -1:
                    break
                yield lineno, pending[start:nl], True
                start = nl + 1
                lineno += 1
            if start:
                pending = pending[start:]
            if len(pending) >= LINE_WINDOW_BYTES:
                # No newline for a very long stretch — scan what has
                # accumulated as a window instead of growing `pending`
                # without bound, then keep only the OVERLAP tail so a match
                # straddling this cut is still whole in the next window.
                yield lineno, pending, False
                pending = pending[-LINE_WINDOW_OVERLAP:]
        pending += decoder.decode(b"", final=True)
        if pending:
            yield lineno, pending, True  # EOF: whatever remains is the last line


def _scan_file(path: Path, rel: str, disabled: frozenset[str],
               tally: Tally | None) -> list[Finding]:
    """Scan one file with memory bounded by a fixed constant regardless of
    the file's size (020/370) — see `_iter_numbered_lines`. Ordinary lines
    are scanned one at a time via the same `scan_lines` engine as before (its
    own dedupe/allow-marker logic is already scoped per line number, so
    calling it once per line rather than once for a whole file produces
    IDENTICAL findings — verified against the pre-fix behaviour by the
    existing test suite, not just asserted here).

    An overlong line's windows need one extra step this function owns: two
    consecutive windows of the SAME physical line share `LINE_WINDOW_OVERLAP`
    characters of real content, so a token sitting in that shared region
    would otherwise be found — and reported — twice. `seen_in_window` dedupes
    by (rule, excerpt) across a run of windows belonging to one line; it is
    reset the moment a window's `is_final_window` says that line is done."""
    findings: list[Finding] = []
    seen_in_window: set[tuple[str, str]] = set()
    in_overlong = False
    try:
        for lineno, text, is_final, pem in pem_exempt_stream(
                _iter_numbered_lines(path)):
            unit = scan_lines(rel, [(lineno, text)], disabled, tally,
                              frozenset((lineno,)) if pem else _NO_PEM_LINES)
            if in_overlong:
                for f in unit:
                    key = (f.rule, f.excerpt)
                    if key not in seen_in_window:
                        seen_in_window.add(key)
                        findings.append(f)
            else:
                findings.extend(unit)
            if is_final:
                in_overlong = False
                seen_in_window = set()
            else:
                in_overlong = True
    except OSError:
        # A file that vanishes/becomes unreadable mid-walk (race with another
        # process) is not this scanner's failure to report — matches the old
        # behaviour, which never guarded `read_bytes()` here either.
        pass
    return findings


# ---------------------------------------------------------------------------
# 115/380 — what an EXEMPT file is still read for.
#
# A glob in `.secretscanignore` skips a file for every rule. The scanners' own
# test files are skipped on the stated ground that their fixtures are fictional,
# and nothing held them to it: on 2026-11-06 a worker put four working private
# keys into `tools/test_secretscan.py`, every check passed, and only a human
# read caught it. So an exempt file keeps ONE narrow check, for exactly what
# "fictional" is meant to exclude: real private-key material. Every other rule
# stays skipped, so a stated-reason glob works as it always did.
#
# ADVISORY for now (`RESPONSE_ADVISORY`): reported and counted in the same
# `secretscan advisory:` line, exit code unmoved, because it changes what a
# guard reads inside its own exemptions and children float at `main`. A later
# item may flip it to blocking once the estate reads clean.
#
# Two shapes, both judged on the DECODED BYTES, never on the text, so a
# fictional header, a certificate and a public key cannot trip it:
#   (a) a PEM block with any `... PRIVATE KEY` label whose body is pure base64
#       and decodes to a private-key DER outline (or, for `OPENSSH PRIVATE KEY`,
#       to `openssh-key-v1\0`; for `ENCRYPTED PRIVATE KEY`, to the encrypted
#       PKCS#8 outline);
#   (b) a bare base64 run of at least `EXEMPT_RUN_MIN_DECODED` bytes that
#       decodes to the outline: a SEQUENCE opening with INTEGER 0 or 1, then
#       PKCS#8 (SEQUENCE{OID..}, OCTET STRING), PKCS#1/DSA (five or more
#       INTEGERs) or SEC1 (OCTET STRING, optional [0]/[1]), the children
#       filling the SEQUENCE exactly. That is what a private key has and a
#       certificate (first child a SEQUENCE) and a public key do not.
#
# FRAGMENTS ARE JOINED. A Python test writes a key as adjacent quoted strings,
# one per line, so no single line holds a run long enough to judge. A quoted
# fragment line is joined to the lines directly after it until a line that is
# not a fragment, or one that ends with `,` or `)`, or a padded `=` end. The
# join costs a small state machine and is worth it: it is exactly the shape the
# 2026-11-06 keys were committed in, and the alternative is a rule that passes
# on the realistic case and fails on a wrapped one. A joined run is judged from
# its first character, so a key that does not begin at a fragment is missed;
# that is the known gap, with base64url (`-_`) runs and a bare run under
# `EXEMPT_RUN_MIN_DECODED` bytes (the PEM form of a short key is still caught
# by (a)). The floor is a cost bound, not a detection threshold: the outline
# test is what keeps a false positive out.
#
# BOUNDED. The file is streamed through `_iter_numbered_lines` (020/370), a
# joined run is capped at `EXEMPT_RUN_MAX_CHARS` (the PEM bound, ~150 KiB), and
# a hit is held as a redacted `Finding` through `_record`, so the findings cap
# applies. The key is never printed: an excerpt carries a length and a form.
EXEMPT_RUN_MIN_DECODED = 100
EXEMPT_RUN_MIN_CHARS = (EXEMPT_RUN_MIN_DECODED * 4 + 2) // 3
EXEMPT_FRAG_MIN = 16
# A fragment or a tail suffix longer than this is not a wrapped literal, and the
# whitespace-tolerant patterns that read them must not be fed an arbitrary
# length (a long blank run before a stray character is quadratic to reject).
EXEMPT_LINE_MAX = 4096
EXEMPT_RUN_MAX_CHARS = PEM_MAX_BODY_LINES * PEM_MAX_LINE
OPENSSH_MAGIC = b"openssh-key-v1\x00"

_PEM_PRIV_BEGIN_RX = re.compile(r"-----BEGIN ((?:[A-Z0-9]+ )*PRIVATE KEY)-----")
_PEM_PRIV_ONELINE_RX = re.compile(
    r"-----BEGIN ((?:[A-Z0-9]+ )*PRIVATE KEY)-----(.*?)-----END \1-----")
_ESCAPES_RX = re.compile(r"\\[nrt]|[\s\"'+\\]")
# A whole line that is one (optionally quoted) base64 fragment: `"MIIE..."`,
# `    "MIIE...\n"  # why`, `MIIE...` (a raw PEM body line). Group 2 is the
# fragment, 4 is the trailer that says whether the literal goes on.
_FRAG_RX = re.compile(
    r"""^\s*(?:[A-Za-z]{0,2}["'])?([A-Za-z0-9+/]+={0,2})((?:\\[nrt])*)"""
    r"""["']?\s*([+,)\\]*)\s*(?:\#.*)?$""")
# What may follow the last fragment of a line that has other text before it
# (`KEY = ("MIIE...`): a closing quote, line-continuation punctuation, a comment.
# Matched against the text AFTER the run, never searched for across the line: a
# search that fails after a long run retries from every position inside it,
# which is quadratic on an overlong line (found by the 6 MB test below).
_TAIL_AFTER_RX = re.compile(
    r"""((?:\\[nrt])*)["']?\s*([+,)\\]*)\s*(?:\#.*)?$""")
_LONG_FRAG_RX = re.compile(r"[A-Za-z0-9+/]{%d,}={0,2}" % EXEMPT_FRAG_MIN)
_RUN_RX = re.compile(r"[A-Za-z0-9+/]{%d,}={0,2}" % EXEMPT_RUN_MIN_CHARS)


def _der_children(raw: bytes, start: int, end: int):
    """The elements that exactly fill `raw[start:end]`, or None."""
    out, at = [], start
    while at < end:
        el = _der_element(raw, at)
        if el is None or el[2] > end:
            return None
        out.append(el)
        at = el[2]
    return out


def private_key_outline(raw: bytes) -> str | None:
    """The form (`PKCS#8`, `PKCS#1`, `SEC1`) if `raw` opens with a private
    key's DER outline, else None. A SEQUENCE whose first child is INTEGER 0 or
    1, then children that fill it exactly in one of the three private-key
    shapes. A certificate or a SubjectPublicKeyInfo opens with a SEQUENCE and
    matches none. Tags and lengths only; a shape check, not a key parse."""
    outer = _der_element(raw, 0)
    if outer is None or outer[0] != 0x30:
        return None
    kids = _der_children(raw, outer[1], outer[2])
    if not kids or len(kids) < 2:
        return None
    ver = kids[0]
    if ver[0] != 0x02 or ver[2] - ver[1] != 1 or raw[ver[1]] not in (0, 1):
        return None
    rest = kids[1:]
    tag = rest[0][0]
    if tag == 0x30 and len(rest) >= 2 and rest[1][0] == 0x04 \
            and all(k[0] in (0xA0, 0x81) for k in rest[2:]):
        first = _der_element(raw, rest[0][1])      # AlgorithmIdentifier: OID first
        return "PKCS#8" if first is not None and first[0] == 0x06 else None
    if tag == 0x04 and all(k[0] in (0xA0, 0xA1) for k in rest[1:]):
        return "SEC1"
    ints = [k for k in rest if k[0] == 0x02]
    if tag == 0x02 and len(ints) >= 5 \
            and all(k[0] == 0x02 for k in rest[:len(ints)]) \
            and all(k[0] == 0x30 for k in rest[len(ints):]):
        return "PKCS#1"
    return None


def _is_encrypted_pkcs8(raw: bytes) -> bool:
    """EncryptedPrivateKeyInfo: SEQUENCE { SEQUENCE, OCTET STRING }. Judged
    only under an `ENCRYPTED PRIVATE KEY` label — bare, the same outline is a
    DigestInfo, which is not a key."""
    outer = _der_element(raw, 0)
    if outer is None or outer[0] != 0x30:
        return False
    kids = _der_children(raw, outer[1], outer[2])
    return bool(kids) and [k[0] for k in kids] == [0x30, 0x04]


def _b64_decode_loose(s: str) -> bytes | None:
    """Decode base64 that may carry junk after the real end: padding is
    rebuilt from the length, a dangling single character is dropped."""
    s = s.rstrip("=")
    if len(s) % 4 == 1:
        s = s[:-1]
    s += "=" * (-len(s) % 4)
    try:
        return base64.b64decode(s, validate=True)
    except (binascii.Error, ValueError):
        return None


def _pem_private_hit(label: str, body: str) -> str | None:
    raw = _b64_decode_loose(body)
    if not raw:
        return None
    if label.startswith("OPENSSH "):
        ok = raw.startswith(OPENSSH_MAGIC)
    elif label.startswith("ENCRYPTED "):
        ok = _is_encrypted_pkcs8(raw)
    else:
        ok = private_key_outline(raw) is not None
    return f"<PEM {label} block, {len(raw)} bytes decoded>" if ok else None


def _bare_run_hit(run: str) -> str | None:
    if len(run) < EXEMPT_RUN_MIN_CHARS:
        return None
    raw = _b64_decode_loose(run[:EXEMPT_RUN_MAX_CHARS])
    if raw is None or len(raw) < EXEMPT_RUN_MIN_DECODED:
        return None
    form = private_key_outline(raw)
    return f"<base64 run, {len(raw)} bytes decoded, {form} outline>" if form else None


def _drop_escape_lead(text: str, start: int, run: str) -> str:
    """`"\\nMIIE..."` puts the `n` of a source-level `\\n` escape on the front
    of the run; it is not base64."""
    if start > 0 and text[start - 1] == "\\" and run[:1] in ("n", "r", "t"):
        return run[1:]
    return run


def exempt_key_hits(items):
    """Yield `(lineno, excerpt)` for each real private key in `items`, a stream
    of `(lineno, text, ...)` in file order. See the 115/380 comment above."""
    acc: list[str] = []          # the open joined run
    acc_len = acc_line = acc_last = 0
    pem_label = None             # the open PEM block
    pem_body: list[str] = []
    pem_line = pem_last = 0
    covered = (0, 0)             # lines of a PEM block already reported by (a)

    def flush():
        nonlocal acc, acc_len
        run, line = "".join(acc), acc_line
        acc, acc_len = [], 0
        if covered[0] < line <= covered[1]:
            return None          # (a) already reported this key
        hit = _bare_run_hit(run)
        return (line, hit) if hit else None

    for item in items:
        lineno, text = item[0], item[1]
        # Cost: a short line with nothing open and no PEM marker cannot start
        # anything, and is the common case in a file of code.
        if (len(text) < EXEMPT_FRAG_MIN and not acc and pem_label is None
                and "-----" not in text):
            continue
        if acc and lineno != acc_last + 1:
            got = flush()
            if got:
                yield got

        one = _PEM_PRIV_ONELINE_RX.search(text) if "PRIVATE KEY-----" in text else None
        if one:
            hit = _pem_private_hit(one.group(1), _ESCAPES_RX.sub("", one.group(2)))
            if acc:
                got = flush()
                if got:
                    yield got
            if hit:
                yield lineno, hit
                continue

        frag = _FRAG_RX.match(text) if len(text) <= EXEMPT_LINE_MAX else None

        if pem_label is not None:
            if lineno == pem_last + 1 and f"-----END {pem_label}-----" in text:
                hit = (_pem_private_hit(pem_label, "".join(pem_body))
                       if pem_body else None)
                if hit:
                    covered = (pem_line, lineno)
                    yield pem_line, hit
                pem_label, pem_body = None, []
            elif (lineno == pem_last + 1 and frag
                    and len(pem_body) < PEM_MAX_BODY_LINES):
                pem_body.append(frag.group(1))
                pem_last = lineno
            else:
                pem_label, pem_body = None, []      # voided: not a clean block

        if frag and (acc or len(frag.group(1)) >= EXEMPT_FRAG_MIN):
            if not acc:
                acc_line = lineno
            acc.append(frag.group(1))
            acc_len += len(frag.group(1))
            acc_last = lineno
            # Padding ends a base64 value, but inside an open PEM block the
            # run is judged at the END line, after (a) has had its say.
            ends = ((frag.group(1).endswith("=") and pem_label is None)
                    or "," in frag.group(3) or ")" in frag.group(3))
            if ends or acc_len > EXEMPT_RUN_MAX_CHARS:
                got = flush()
                if got:
                    yield got
            continue

        if acc:
            got = flush()
            if got:
                yield got

        if pem_label is None and "PRIVATE KEY-----" in text:
            m = _PEM_PRIV_BEGIN_RX.search(text)
            if m and not one:
                pem_label, pem_body, pem_line, pem_last = m.group(1), [], lineno, lineno

        if len(text) < EXEMPT_FRAG_MIN:
            continue
        tail_start = -1
        last = None
        for last in _LONG_FRAG_RX.finditer(text):
            pass
        after = (_TAIL_AFTER_RX.match(text, last.end())
                 if last is not None and len(text) - last.end() <= EXEMPT_LINE_MAX
                 else None)
        if after:
            run = _drop_escape_lead(text, last.start(), last.group(0))
            tail_start = last.start()
            if "," in after.group(2) or ")" in after.group(2) or run.endswith("="):
                hit = _bare_run_hit(run)
                if hit and not (covered[0] < lineno <= covered[1]):
                    yield lineno, hit
            else:
                acc, acc_len, acc_line, acc_last = [run], len(run), lineno, lineno
        if len(text) >= EXEMPT_RUN_MIN_CHARS:
            for m in _RUN_RX.finditer(text):
                if m.start() == tail_start:
                    continue      # the tail run was handled (or is open) above
                hit = _bare_run_hit(_drop_escape_lead(text, m.start(), m.group(0)))
                if hit and not (covered[0] < lineno <= covered[1]):
                    yield lineno, hit
    if acc:
        got = flush()
        if got:
            yield got


def _exempt_findings(rel: str, items, tally: Tally | None) -> list[Finding]:
    findings: list[Finding] = []
    seen: set[tuple[int, str]] = set()      # an overlong line's windows overlap
    for lineno, excerpt in exempt_key_hits(items):
        if (lineno, excerpt) in seen:
            continue
        seen.add((lineno, excerpt))
        _record(findings, tally, Finding(rel, lineno, EXEMPT_PRIVATE_KEY_RULE,
                                         "exempt", "high", excerpt,
                                         RESPONSE_ADVISORY))
    return findings


def _scan_exempt_file(path: Path, rel: str, disabled: frozenset[str],
                      tally: Tally | None) -> list[Finding]:
    """The one check an exempt (`.secretscanignore`) file still gets. Streams
    the file; reads nothing if the rule is disabled."""
    if EXEMPT_PRIVATE_KEY_RULE in disabled:
        return []
    try:
        return _exempt_findings(rel, _iter_numbered_lines(path), tally)
    except OSError:
        return []       # vanished mid-walk, as `_scan_file` treats it


def scan_exempt_lines(rel: str, numbered_lines: list[tuple[int, str]],
                      disabled: frozenset[str] = frozenset(),
                      tally: Tally | None = None) -> list[Finding]:
    """The same check over a staged diff's ADDED lines of an exempt file. No
    blob is read: a key is seen only if its lines were added together, and the
    CI run, which reads the whole file, re-prints anything this misses."""
    if EXEMPT_PRIVATE_KEY_RULE in disabled:
        return []
    return _exempt_findings(rel, ((n, t) for n, t in numbered_lines), tally)


def scan_paths(paths: list[Path], root: Path,
               disabled: frozenset[str] = frozenset(),
               tally: Tally | None = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p, rel, ignored in _classify_files(paths, root, globs):
        if ignored:
            # Skipped by every rule EXCEPT the one narrow check (115/380).
            if tally is not None:
                tally.files_by_glob += 1
            findings.extend(_scan_exempt_file(p, rel, disabled, tally))
            continue
        findings.extend(_scan_file(p, rel, disabled, tally))
    return findings


def staged_added_lines() -> dict[str, list[tuple[int, str]]]:
    """Path → [(real file line number, added-line text), ...] for the staged
    diff. Scans only what a commit would introduce (the pre-commit hot path),
    not the whole tree.

    Fixes two defects found TOGETHER in one commit and filed as one report
    (320/290), each masking the other: a spaced filename reported a truncated
    path, and the finding's line number pointed 765 lines from the real one.
    Reproduced directly against real git output before either fix, not
    inferred from the diff format spec:

      * git appends a literal trailing TAB to the `+++ b/<path>` header when
        the path contains whitespace — there is no timestamp field here (that
        is POSIX `diff -u`'s convention, not git's), so the tab is the ONLY
        thing that can trail the path and stripping it is safe. `-c
        core.quotePath=false` is passed too, so a non-ASCII path is not C-quoted
        into something this parser would then have to un-escape.
      * the OLD code numbered every added line sequentially from 1 — as if the
        whole diff were one hunk starting at the top of the file — so a file
        touched in more than one place reported EVERY finding at the wrong
        line, independent of the path at all (reproduced with a two-hunk diff
        on an ordinary, space-free filename). Each `@@ -a,b +c,d @@` hunk
        header now resets the real new-file line counter, and every added or
        context line advances it by one; a removed (`-`) line does not, since
        it never lands in the file the commit produces.

    R is in the filter deliberately (review B4): git detects renames by
    default, and a renamed-AND-edited file's added lines are exactly as
    leak-capable as a modified file's — ACM alone silently skipped them."""
    # The diff is read by `report.staged_added` (115/280): the file header is
    # taken from git's structure, the real line number from each hunk's
    # counts, and the quoting of a tab/newline/quote/backslash name undone
    # (115/260). An added line that merely LOOKS like a header (`++ b/x`
    # prints as `+++ b/x`) used to move attribution here, and was itself
    # dropped as not-an-added-line, hiding what followed it.
    files: dict[str, list[tuple[int, str]]] = {}
    for path, lineno, text in report.staged_added():
        files.setdefault(path, []).append((lineno, text))
    return files


def staged_pem_lines(path: str, added: list[tuple[int, str]]) -> frozenset[int]:
    """Which of a staged file's ADDED lines are the body of a public PEM block
    (320/790). A diff that adds only body lines to a certificate already in the
    file shows no BEGIN line, so the block is found in the INDEX copy of the
    file — what the commit will hold — and a line is exempt only if that whole
    block, BEGIN to END, is valid there. A line whose block is not seen is
    simply scanned. The blob is read only if some added line could be a body
    line long enough to trip the entropy net, so the hook's hot path is
    unchanged for every other file. Raises `STAGED_DIFF_FAILURES` if git cannot
    produce the blob; the caller exits 2 rather than treat that as clean."""
    wanted = {n for n, t in added
              if len(t.strip()) >= HIGH_ENTROPY_MIN_LEN and _is_pem_body_line(t.strip())}
    if not wanted:
        return _NO_PEM_LINES
    with report.staged_blob(path) as stream:
        items = ((n, raw.decode("utf-8", "replace").rstrip("\n"), None)
                 for n, raw in enumerate(stream, start=1))
        return frozenset(n for n, _t, _x, ok in pem_exempt_stream(items)
                         if ok and n in wanted)


def advisory_count_line(n: int) -> str:
    """The one line that always says how many advisory findings this run made.

    ALWAYS printed, zero included — the same reasoning as `Tally.summary`, and
    the reason the board can be trusted. A line printed only when non-zero makes
    "no line" mean two different things: nothing found, or the wording drifted
    and the reader (or `tools/floor.py`) is now parsing a message that no longer
    exists. Printing the zero collapses that ambiguity, so a count that
    disappears is a defect somebody can see rather than a quiet green."""
    return f"  {ADVISORY_COUNT_PREFIX} {n} finding(s) — reported, not blocking."


def _render_advisory(advisory: list[Finding], over_cap: int = 0) -> list[str]:
    """The advisory detail block. Deliberately shares NO wording with the
    blocking block — not the ✗, not "commit blocked", not the remediation
    paragraph. A reader skimming two adjacent lists must be able to tell which
    one stopped the commit without reading either carefully, so the icon, the
    verb and the framing all differ, and the block states its own exit-code
    consequence rather than leaving it to be inferred."""
    lines = ["", "🟡 ADVISORY FINDINGS — none of these blocked anything."]
    rules = {f.rule for f in advisory}
    if rules - {EXEMPT_PRIVATE_KEY_RULE}:
        lines += ["   Coverage the blocking net does not reach: an unbroken 32+ "
                  "character run with no",
                  "   credential-named key beside it. Most are hashes, digests and "
                  "ids; a hex-encoded",
                  "   credential outside an assignment looks exactly the same, which "
                  "is why these are",
                  "   shown rather than dropped."]
    if EXEMPT_PRIVATE_KEY_RULE in rules:
        # 115/380: what a `.secretscanignore` exemption is still read for.
        lines += [f"   {EXEMPT_PRIVATE_KEY_RULE}: a file exempted by .secretscanignore "
                  "on the promise that its",
                  "   fixtures are fictional holds text that decodes as a real private "
                  "key. Build a test",
                  "   key at run time instead of committing one."]
    for f in sorted(advisory, key=lambda x: (x.path, x.line)):
        lines.append(report.with_id(
            f"     {f.path}:{f.line}  [advisory/{f.kind}] {f.rule} → {f.excerpt}",
            "secretscan", f.rule))
    lines.append("   A real secret here: remove it and ROTATE it — advisory "
                 "describes this scan's")
    if rules - {EXEMPT_PRIVATE_KEY_RULE}:
        lines.append("   confidence, never the value's safety. Otherwise leave it: "
                     "the finding costs a")
        lines.append(f"   line, and '# {ALLOW_MARKER}:{LOW_VARIETY_RULE}: <reason>' "
                     "is there for a line")
        lines.append("   that is genuinely noise worth silencing.")
    else:
        lines.append("   confidence, never the value's safety.")
    if over_cap:
        lines.append(report.over_cap_line(over_cap, MAX_MATERIALIZED_FINDINGS,
                                          noun="advisory finding(s)", indent="   "))
    return lines


def render_human(findings: list[Finding], tally: Tally | None = None) -> str:
    blocking = [f for f in findings if f.blocks]
    advisory = [f for f in findings if not f.blocks]
    # 020/370 — a capped run's TRUE totals live on the tally, never on
    # `len(findings)`: everything past `MAX_MATERIALIZED_FINDINGS` was
    # counted there instead of being built as a `Finding` at all (see
    # `Tally.take_finding_slot`), so reading the list length alone would
    # silently under-report both the exit-code-relevant blocking count and
    # the advisory count on exactly the runs this cap exists for.
    blocking_over = tally.blocking_over_cap if tally is not None else 0
    advisory_over = tally.advisory_over_cap if tally is not None else 0
    lines: list[str] = []
    if not blocking and not blocking_over:
        lines.append(report.clean_head("secretscan",
                                       "no credentials in the scanned lines."))
        if tally is not None:
            lines.append(tally.summary())
        lines.append(advisory_count_line(len(advisory) + advisory_over))
        if advisory:
            lines.extend(_render_advisory(advisory, advisory_over))
        return "\n".join(lines)
    lines.append(report.findings_head("secretscan", len(blocking) + blocking_over,
                                      tail=" — commit blocked.\n"))
    for f in sorted(blocking, key=lambda x: (x.path, x.line)):
        lines.append(report.with_id(
            f"  {f.path}:{f.line}  [{f.severity}/{f.kind}] {f.rule} → {f.excerpt}",
            "secretscan", f.rule))
    if blocking_over:
        lines.append(report.over_cap_line(blocking_over, MAX_MATERIALIZED_FINDINGS,
                                          noun="blocking finding(s)"))
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append(advisory_count_line(len(advisory) + advisory_over))
    lines.append("\n  A true positive: remove the secret, move it to the secret store")
    lines.append("  (e.g. a `!secret`/env reference), and ROTATE it — commit history is forever.")
    lines.append(f"  A false positive: append '# {ALLOW_MARKER}: <reason>' to the line")
    lines.append(f"  (or '# {ALLOW_MARKER}:<rule>: <reason>' to exempt just one rule —")
    lines.append("  the narrowest allowance that covers the case), or add a path glob")
    lines.append("  to .secretscanignore. A marker with no reason exempts nothing.")
    if advisory:
        lines.extend(_render_advisory(advisory, advisory_over))
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="secretscan",
        description="Scan for plaintext credentials before they reach git history.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo, or --staged). "
                         "With --staged, repo-root-relative paths in git's own "
                         "spelling and case ('.' is the whole diff); one git "
                         "does not know is refused (exit 2)")
    ap.add_argument("--staged", action="store_true",
                    help="scan only lines added in the git staging area (pre-commit hook)")
    ap.add_argument("--root", default=".",
                    help="repo root for relative paths/.secretscanignore "
                         "(with --staged it must be the repo you run in)")
    ap.add_argument("--disable", default="",
                    help="comma-separated rules to skip (named rule, 'assigned', "
                         f"'high-entropy', or '{LOW_VARIETY_RULE}'). Use to quiet "
                         "a noisy generic rule while keeping the high-confidence "
                         "vendor formats.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()

    disabled = frozenset(r.strip() for r in args.disable.split(",") if r.strip())
    unknown = disabled - ALL_RULES
    if unknown:
        return report.broken(
            "secretscan", f"unknown rule(s) in --disable: {', '.join(sorted(unknown))}")
    # A scope reduction taken at invocation is an allowance too, and rule (b)
    # says one nobody can see is one nobody reviewed — so `--disable` reports
    # itself in the output rather than narrowing the scan invisibly.
    tally = Tally(disabled_rules=tuple(sorted(disabled)))

    if args.staged:
        rc = report.refuse_other_repo("secretscan", root)
        if rc is not None:
            return rc
        try:
            staged = staged_added_lines()
        except report.STAGED_DIFF_FAILURES as e:
            return report.git_diff_failed("secretscan", e)
        # An ABSOLUTE path here scans NOTHING and exits 0 — the silent-success
        # class (linkscan L1) this tool already closes for a missing path, found
        # again on 2026-07-25 while building tools/floor.py. git lists staged
        # paths repo-relative, so `/Users/…/repo/x.py` matches no prefix, the
        # filter empties the set, and a boundary scan that covered nothing looks
        # exactly like one that found nothing wrong. Refuse it.
        # `report.scope_staged` also normalises the spelling (`.`, `./x`),
        # refuses one that escapes the repo, and lets git resolve what each
        # positional names, refusing one git does not know (115/360, 160/950).
        rc, staged = report.scope_staged("secretscan", staged, args.paths, "src/")
        if rc is not None:
            return rc
        globs = load_ignore_globs(root)
        findings = []
        for path, lines in staged.items():
            if _ignored(path, globs):
                tally.files_by_glob += 1
                findings.extend(scan_exempt_lines(path, lines, disabled, tally))
                continue
            try:
                pem = staged_pem_lines(path, lines)
            except report.STAGED_DIFF_FAILURES as e:
                return report.git_diff_failed("secretscan", e)
            findings.extend(scan_lines(path, lines, disabled, tally, pem))
    else:
        # A RELATIVE target resolves against --root, never the caller's cwd:
        # mixing the two reads one repo's file under another repo's rules,
        # and neither half of the output says so (roadmap 010/110).
        targets = report.resolve_targets(root, args.paths or [str(root)])
        # A typo'd path scanning nothing must never read as a clean pass —
        # the linkscan L1 silent-success class, closed here too
        # (2026-07-11 review N2).
        rc = report.refuse_missing_paths("secretscan", targets)
        if rc is not None:
            return rc
        findings = scan_paths(targets, root, disabled, tally)

    blocking = [f for f in findings if f.blocks]
    # 020/370 — a capped run's TRUE counts include what the cap counted but
    # never materialized (`Tally.take_finding_slot`); reading `len(findings)`
    # alone would silently under-report exactly the runs this cap exists for.
    blocking_total = len(blocking) + tally.blocking_over_cap
    advisory_total = (len(findings) - len(blocking)) + tally.advisory_over_cap
    if args.json:
        print(json.dumps({
            # `clean` keeps its original meaning — nothing found at all — and
            # `blocked` is the field that tracks the exit code. Two fields
            # rather than one redefined field, so a consumer written against
            # the old shape cannot silently start reading a green tick off a
            # run that has advisory findings in it.
            "clean": not findings and not blocking_total and not advisory_total,
            "blocked": bool(blocking_total),
            "counts": {"blocking": blocking_total,
                       "advisory": advisory_total},
            "findings": report.finding_dicts("secretscan", findings,
                                             lambda f: f.rule),
            "suppressed": {
                "by_allow_marker": tally.marker_total,
                "by_allow_marker_rule": tally.by_marker,
                "files_by_ignore_glob": tally.files_by_glob,
                "disabled_rules": list(tally.disabled_rules),
                "public_key_fingerprints": tally.fingerprints,
                "by_public_key_line": tally.public_key_spans,
                "by_published_url_token": tally.url_tokens,
                "beyond_finding_cap": {
                    "cap": MAX_MATERIALIZED_FINDINGS,
                    "blocking": tally.blocking_over_cap,
                    "advisory": tally.advisory_over_cap,
                },
            },
        }, indent=2))
    else:
        print(render_human(findings, tally))

    return report.exit_code(blocking_total)


def _selftest() -> int:
    """Smoke test so `secretscan --selftest` proves the engine on any box, even
    where the unittest file isn't shipped. Fixtures are fictional/example
    credentials — the shapes are the point."""
    should_flag = [
        "aws_key = AKIAIOSFODNN7EXAMPLE",                       # secretscan:allow: selftest fixture / leakscan:allow: selftest fixture
        "-----BEGIN OPENSSH PRIVATE KEY-----",                  # secretscan:allow: selftest fixture / leakscan:allow: selftest fixture
        "github: ghp_012345678901234567890123456789abcdef",    # secretscan:allow: selftest fixture
        'password = "Gk8xQvie2mNfR7pLzW3dTaHb"',                # secretscan:allow: selftest fixture
        "slack xoxb-1234567890-abcdefghijklmno",                # secretscan:allow: selftest fixture
        # E6c — low variety is not innocence under a credential-named key.
        # Both were clean before 2026-07-28; the git SHA below is the control.
        "api_key = deadbeefcafef00d0123456789abcdef",           # secretscan:allow: selftest fixture
        "password=correct-horse-battery-staple",                # secretscan:allow: selftest fixture
        # 320/290 — a credential in a URL query string is still caught by the
        # assigned-secret rule, which is unaffected by the URL carve-out below.
        "GET https://api.example.com/v1/data?token=aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3z",  # secretscan:allow: selftest fixture
    ]
    should_pass = [
        "password = changeme",                     # placeholder
        "api_key = ${API_KEY}",                    # env indirection
        'psk = "!secret wg_home"',                 # tiki secret reference
        "private_key = /etc/ssl/server.key",       # a path, not a secret
        "version = 1.2.3",                         # not a secret
        "token = abc  # secretscan:allow: doc example",
        # E3 — a public-key fingerprint is public material by definition. This
        # value is a synthetic 43-char base64 body, not any real key's digest.
        "host key SHA256:aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5bC7dE9f",  # secretscan:allow: selftest fixture
        # 320/290 — a published URL's hyphenated path segment is not an
        # entropy candidate, however high it scores.
        "doc: https://docs.example.org/guides/how-to-Configure-OAuth2-Bearer-Tokens-For-Api",
    ]
    # E6b — REPORTED and not blocking. A git SHA is the honest exemplar: it is
    # what the widened context-free net mostly finds, and a hex-encoded
    # credential is indistinguishable from it, which is the whole argument.
    should_advise = [
        "commit 9f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f90",  # git SHA (single-case hex)
        "checksum deadbeefcafef00d0123456789abcdef01234567",
    ]
    ok = True
    for text in should_flag:
        fs = scan_text("t", text)
        if not any(f.blocks for f in fs):
            print(f"FAIL (expected a BLOCKING finding): {text!r}")
            ok = False
    for text in should_pass:
        fs = scan_text("t", text)
        if fs:
            print(f"FAIL (expected clean): {text!r} → {[f.rule for f in fs]}")
            ok = False
    for text in should_advise:
        fs = scan_text("t", text)
        if not fs or any(f.blocks for f in fs):
            print(f"FAIL (expected an ADVISORY-only finding): {text!r} → "
                  f"{[(f.rule, f.response) for f in fs]}")
            ok = False
    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1



def main(argv: list[str] | None = None) -> int:
    """Exit 2 on an ignore file that grants an exemption with no reason.

    A broken scan is not a pass (the house exit-code contract), and an
    unexplained exemption makes the scan's own scope untrustworthy."""
    return report.guarded_main("secretscan", _main, argv, (IgnoreFileError,))

if __name__ == "__main__":
    sys.exit(main())
