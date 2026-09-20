#!/usr/bin/env python3
"""secretscan — the mechanical gate that keeps plaintext credentials out of a
git commit.

leakscan guards the *public boundary* (personal/estate data must not enter a
repo that can go public). secretscan guards a different boundary that exists in
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
import codecs
import fnmatch
import json
import math
import os
import re
import subprocess
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

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

ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER) + r"(?::(?P<rule>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>[\w\"\'“‘])")


def parse_allow(line: str) -> str | None:
    """The scope of the line's allow-marker, or None if it carries none.

    `""` means every rule; a rule name means just that one. A marker with no
    reason returns None — it is a mention, not an exemption."""
    m = ALLOW_RX.search(line)
    if not m:
        return None
    return m.group("rule") or ""


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
                 f"{self.blocking_over_cap + self.advisory_over_cap} beyond the "
                 f"{MAX_MATERIALIZED_FINDINGS}-finding cap (counted, not listed)"]
        line = "  suppressed: " + " · ".join(parts)
        if self.by_marker:
            detail = ", ".join(f"{r}×{n}" for r, n in sorted(self.by_marker.items()))
            line += f"\n    allow-marker breakdown: {detail}"
        if self.disabled_rules:
            line += f"\n    disabled: {', '.join(self.disabled_rules)}"
        return line


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


def _p(name: str, severity: str, rx: str, flags: int = 0) -> Pattern:
    return Pattern(name, severity, re.compile(rx, flags))


# NAMED credential formats — unambiguous by construction, so they flag on shape
# alone. Ordered by how self-evidently they are a secret.
NAMED: list[Pattern] = [
    _p("private-key-header", "high",
       r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"),
    _p("pgp-private-key", "high", r"-----BEGIN PGP PRIVATE KEY BLOCK-----"),  # secretscan:allow: this is the detection pattern, not a key
    _p("aws-access-key-id", "high", r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    _p("github-token", "high",
       r"\bgh[posru]_[A-Za-z0-9]{36,}\b|\bgithub_pat_[0-9A-Za-z_]{22,}\b"),
    _p("slack-token", "high", r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b"),
    _p("slack-webhook", "high",
       r"https://hooks\.slack\.com/services/[A-Za-z0-9/]+"),
    _p("google-api-key", "high", r"\bAIza[0-9A-Za-z_-]{35}\b"),
    _p("gcp-oauth-secret", "medium", r"\bGOCSPX-[0-9A-Za-z_-]{20,}\b"),
    _p("stripe-key", "high", r"\b[rsp]k_(?:live|test)_[0-9A-Za-z]{20,}\b"),
    _p("anthropic-key", "high", r"\bsk-ant-[A-Za-z0-9-]{20,}\b"),
    _p("openai-key", "high", r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    _p("npm-token", "high", r"\bnpm_[A-Za-z0-9]{36}\b"),
    _p("twilio-key", "high", r"\bSK[0-9a-fA-F]{32}\b"),
    _p("sendgrid-key", "high", r"\bSG\.[A-Za-z0-9_-]{16,}\.[A-Za-z0-9_-]{16,}\b"),
    _p("jwt", "high",
       r"\beyJ[A-Za-z0-9_-]{6,}\.eyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}"),
    _p("basic-auth-url", "high",
       r"\b[a-zA-Z][a-zA-Z0-9+.-]*://[^/\s:@]+:[^/\s:@]{4,}@"),
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
URL_RX = re.compile(r"\b[A-Za-z][A-Za-z0-9+.-]*://[^\s<>\"']+")


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
               tally: Tally | None = None) -> list[Finding]:
    """The scanning engine. `numbered_lines` pairs each line of text with its
    REAL line number in the file — which need not be sequential or start at 1.
    That is the shape `--staged` mode needs (320/290): only a diff's added
    lines are scanned, but a finding must still point at the line it actually
    sits on, not at its position in a blob of concatenated fragments.
    `scan_text` below is the sequential-numbering convenience wrapper every
    whole-file caller uses."""
    findings: list[Finding] = []
    # Line -> allowance scope, collected as we go. The subtraction happens
    # AFTER dedupe (rule b, find first and subtract second): suppressing at
    # match time would also count entropy hits that dedupe was about to drop,
    # inflating the very number this exists to make trustworthy.
    allow_by_line: dict[int, str] = {}
    for lineno, line in numbered_lines:
        scope = parse_allow(line)
        if scope is not None:
            allow_by_line[lineno] = scope

        for pat in NAMED:
            if pat.name in disabled:
                continue
            for m in pat.regex.finditer(line):
                _record(findings, tally, Finding(path, lineno, pat.name, "named",
                                                 pat.severity, redact(m.group(0), "named")))

        if "assigned" not in disabled:
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
        public_key_line = bool(PUBLIC_KEY_RX.search(line))
        fingerprints = () if public_key_line else _fingerprint_spans(line)
        url_spans = () if public_key_line else _url_spans(line)
        for m in HIGH_ENTROPY_RX.finditer(line):
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
                      | {"assigned", "high-entropy", LOW_VARIETY_RULE})


class IgnoreFileError(ValueError):
    """An ignore file granted an exemption with no reason stated anywhere."""

    def __init__(self, filename: str, entries: list[tuple[int, str]]):
        self.filename = filename
        self.entries = entries
        detail = "; ".join(f"line {n}: '{g}'" for n, g in entries)
        super().__init__(
            f"{filename}: {len(entries)} glob(s) with no stated reason — "
            f"{detail}. Every exemption states its reason where a reviewer "
            f"reads it (method/GUARDS.md): put a comment above the stanza, or "
            f"a trailing '# reason' on the line.")


def load_ignore_globs(root: Path) -> list[str]:
    """Globs from `.secretscanignore`, each of which MUST carry a stated reason.

    GUARDS.md rule (c): an ignore glob is the widest allowance this scanner
    grants — a whole path, every rule, indefinitely — so it is the last place
    an unexplained exemption should be possible. A glob is reasoned if it
    carries a trailing `# reason` (publishscan's form) OR sits under a comment
    block in its own stanza, which is how this estate's ignore files already
    document themselves and is the better documentation of the two. A blank
    line ends a stanza, so a bare glob under no comment at all is refused.

    An unreasoned glob is a CONFIG ERROR, not a warning: a scan that silently
    honours an exemption nobody explained is the failure the rule exists to
    stop. Callers surface it as exit 2 — a broken scan is not a pass."""
    f = root / ".secretscanignore"
    if not f.exists():
        return []
    globs: list[str] = []
    unreasoned: list[tuple[int, str]] = []
    stanza_reason = False
    for n, raw in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw.strip()
        if not line:
            stanza_reason = False
            continue
        if line.startswith("#"):
            stanza_reason = True
            continue
        glob, _, trailing = line.partition("#")
        glob = glob.strip()
        if not glob:
            continue
        if not trailing.strip() and not stanza_reason:
            unreasoned.append((n, glob))
        globs.append(glob)
    if unreasoned:
        raise IgnoreFileError(".secretscanignore", unreasoned)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


def _walk_files(base: Path):
    """Every regular file under `base`, streamed one at a time — the 020/370
    fix for the OTHER half of `iter_files`' old defect. The previous
    implementation was `base.rglob("*")` funnelled through a list
    comprehension: `rglob` returns a generator, but wrapping it in `[... ]`
    forced Python to walk the ENTIRE subtree and hold every `Path` it found
    before scanning a single byte — measured at ~1 KiB of held memory per
    file just for that list (60,000 files: +54 MB over a 10,000-file
    baseline), on top of it doing so twice as long as the whole enumeration
    ran before scanning could even start on a large tree.

    `os.walk` is used instead of `rglob` specifically because it exposes
    `dirnames` for in-place pruning: filtering `SKIP_DIR_NAMES` out of
    `dirnames` stops `os.walk` from ever DESCENDING into `.git`,
    `node_modules`, etc. at any depth, rather than descending into them and
    discarding what it found — the same skip semantics as the old
    `not (SKIP_DIR_NAMES & set(p.parts))` filter (any path component, not
    just the immediate parent), just applied before the walk pays for it
    instead of after."""
    for dirpath, dirnames, filenames in os.walk(base):
        # 020/160 (E9): a git worktree LINKED into this tree has a `.git`
        # FILE (`gitdir: <path>`), not a directory, so SKIP_DIR_NAMES' name
        # match never fires and the walk descends into a full second
        # checkout of the same repo — double-counting every finding and
        # putting root-relative ignore globs out of reach inside the copy.
        # Checked by file-ness alone, not by parsing the `gitdir:` line: a
        # bare file named exactly `.git` is never anything else (only a
        # worktree or submodule link creates one), and pruning here is the
        # same name/type check SKIP_DIR_NAMES already makes, not a content
        # decision.
        dirnames[:] = [
            d for d in dirnames
            if d not in SKIP_DIR_NAMES
            and not Path(dirpath, d, ".git").is_file()
        ]
        for name in filenames:
            p = Path(dirpath) / name
            if p.is_file():  # excludes broken symlinks, matching the old rglob filter
                yield p


def iter_files(paths: list[Path], root: Path, globs: list[str],
               tally: Tally | None = None):
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
            if _ignored(rel, globs):
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
            while True:
                nl = pending.find("\n")
                if nl == -1:
                    break
                yield lineno, pending[:nl], True
                pending = pending[nl + 1:]
                lineno += 1
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
        for lineno, text, is_final in _iter_numbered_lines(path):
            unit = scan_lines(rel, [(lineno, text)], disabled, tally)
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


def scan_paths(paths: list[Path], root: Path,
               disabled: frozenset[str] = frozenset(),
               tally: Tally | None = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p, rel in iter_files(paths, root, globs, tally):
        findings.extend(_scan_file(p, rel, disabled, tally))
    return findings


# A unified-diff hunk header: `@@ -oldStart[,oldCount] +newStart[,newCount] @@`.
# Only the NEW side matters here — it is the file the commit is about to
# produce, and every added/context line after this header advances from it.
_HUNK_HEADER_RX = re.compile(r"^@@ -\d+(?:,\d+)? \+(?P<new_start>\d+)(?:,\d+)? @@")


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
    out = subprocess.run(
        ["git", "-c", "core.quotePath=false", "diff", "--cached",
         "--unified=0", "--no-color", "--diff-filter=ACMR"],
        capture_output=True, text=True, check=True).stdout
    files: dict[str, list[tuple[int, str]]] = {}
    current: str | None = None
    new_lineno = 0
    for line in out.splitlines():
        if line.startswith("+++ "):
            path = line[len("+++ "):]
            if path.startswith("b/"):
                path = path[2:]
            # The only terminator git emits on this header is the whitespace
            # tab described above — strip it, and nothing else.
            current = path.rstrip("\t")
            files.setdefault(current, [])
            continue
        if line.startswith("@@"):
            m = _HUNK_HEADER_RX.match(line)
            if m:
                new_lineno = int(m.group("new_start"))
            continue
        if current is None:
            continue
        if line.startswith("+") and not line.startswith("+++"):
            files[current].append((new_lineno, line[1:]))
            new_lineno += 1
        elif line.startswith(" "):
            # --unified=0 asks git for none of these, but a caller-side change
            # to that flag must not silently start mis-numbering again.
            new_lineno += 1
        # a '-' (removed) line, and `\ No newline at end of file`, do not
        # advance the new-file counter — neither lands in the new file.
    return {path: lines for path, lines in files.items() if lines}


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
    lines = ["",
             "🟡 ADVISORY FINDINGS — none of these blocked anything.",
             "   Coverage the blocking net does not reach: an unbroken 32+ "
             "character run with no",
             "   credential-named key beside it. Most are hashes, digests and "
             "ids; a hex-encoded",
             "   credential outside an assignment looks exactly the same, which "
             "is why these are",
             "   shown rather than dropped."]
    for f in sorted(advisory, key=lambda x: (x.path, x.line)):
        lines.append(f"     {f.path}:{f.line}  [advisory/{f.kind}] {f.rule} → {f.excerpt}")
    lines.append("   A real secret here: remove it and ROTATE it — advisory "
                 "describes this scan's")
    lines.append("   confidence, never the value's safety. Otherwise leave it: "
                 "the finding costs a")
    lines.append(f"   line, and '# {ALLOW_MARKER}:{LOW_VARIETY_RULE}: <reason>' "
                 "is there for a line")
    lines.append("   that is genuinely noise worth silencing.")
    if over_cap:
        lines.append(f"   …and {over_cap} more advisory finding(s), counted but not "
                     f"listed (past the {MAX_MATERIALIZED_FINDINGS}-finding memory cap).")
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
        lines.append("✓ secretscan clean — no credentials in the scanned lines.")
        if tally is not None:
            lines.append(tally.summary())
        lines.append(advisory_count_line(len(advisory) + advisory_over))
        if advisory:
            lines.extend(_render_advisory(advisory, advisory_over))
        return "\n".join(lines)
    lines.append(f"✗ secretscan: {len(blocking) + blocking_over} finding(s) — commit blocked.\n")
    for f in sorted(blocking, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.severity}/{f.kind}] {f.rule} → {f.excerpt}")
    if blocking_over:
        lines.append(f"  …and {blocking_over} more blocking finding(s), counted but not "
                     f"listed (past the {MAX_MATERIALIZED_FINDINGS}-finding memory cap).")
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
                    help="files/dirs to scan (default: whole repo, or --staged)")
    ap.add_argument("--staged", action="store_true",
                    help="scan only lines added in the git staging area (pre-commit hook)")
    ap.add_argument("--root", default=".",
                    help="repo root for relative paths/.secretscanignore")
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
        print(f"secretscan: unknown rule(s) in --disable: {', '.join(sorted(unknown))}",
              file=sys.stderr)
        return 2
    # A scope reduction taken at invocation is an allowance too, and rule (b)
    # says one nobody can see is one nobody reviewed — so `--disable` reports
    # itself in the output rather than narrowing the scan invisibly.
    tally = Tally(disabled_rules=tuple(sorted(disabled)))

    if args.staged:
        try:
            staged = staged_added_lines()
        except subprocess.CalledProcessError as e:
            print(f"secretscan: git diff failed: {e}", file=sys.stderr)
            return 2
        # An ABSOLUTE path here scans NOTHING and exits 0 — the silent-success
        # class (linkscan L1) this tool already closes for a missing path, found
        # again on 2026-07-25 while building tools/floor.py. git lists staged
        # paths repo-relative, so `/Users/…/repo/x.py` matches no prefix, the
        # filter empties the set, and a boundary scan that covered nothing looks
        # exactly like one that found nothing wrong. Refuse it.
        absolute = [p for p in args.paths if Path(p).is_absolute()]
        if absolute:
            print(f"secretscan: --staged needs repo-relative path(s), got absolute: "
                  f"{', '.join(absolute)}\n"
                  "  git lists staged paths relative to the repo root, so an "
                  "absolute path matches nothing\n"
                  "  and the scan would pass while covering nothing. Pass e.g. "
                  "'src/' instead.", file=sys.stderr)
            return 2
        prefixes = tuple(p.rstrip("/") + "/" for p in args.paths)
        if prefixes:
            staged = {path: lines for path, lines in staged.items()
                      if path.startswith(prefixes) or path in args.paths}
        globs = load_ignore_globs(root)
        findings = []
        for path, lines in staged.items():
            if _ignored(path, globs):
                tally.files_by_glob += 1
                continue
            findings.extend(scan_lines(path, lines, disabled, tally))
    else:
        # A RELATIVE target resolves against --root, never the caller's cwd:
        # mixing the two reads one repo's file under another repo's rules,
        # and neither half of the output says so (roadmap 010/110).
        targets = [(root / p) if not Path(p).is_absolute() else Path(p)
                   for p in (args.paths or [str(root)])]
        missing = [str(p) for p in targets if not p.exists()]
        if missing:
            # A typo'd path scanning nothing must never read as a clean pass —
            # the linkscan L1 silent-success class, closed here too
            # (2026-07-11 review N2).
            print(f"secretscan: path does not exist: {', '.join(missing)}",
                  file=sys.stderr)
            return 2
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
            "findings": [asdict(f) for f in findings],
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

    return 1 if blocking_total else 0


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
    try:
        return _main(argv)
    except IgnoreFileError as e:
        print(f"secretscan: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
