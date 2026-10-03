#!/usr/bin/env python3
"""leakscan — the mechanical boundary that keeps personal/estate data out of a
shareable repo.

The doctrine (atelier apex + AUTONOMY floor) says personal, health, family,
financial and estate-topology detail must never enter a repo that can go public.
A rule enforced by intent alone fails the first tired session. This is the
machine that enforces it: a denylist scan run as a pre-commit hook and in CI, so
a leak fails the commit instead of reaching the remote.

Three layers, split so the scanner itself leaks nothing:

  * STRUCTURAL patterns (in this file, shareable) match the *shape* of sensitive
    data — an email, an IPv4, a MAC, a private-key header — naming no real
    value. They need no secrets, so they ALWAYS run: partial cover even with no
    local list (graceful degradation).

  * KEY CONTEXT (`pii-key-context`) reads the *label* rather than the value: a
    non-placeholder value assigned to an explicit personal-data key name (date
    of birth, bank account, passport, NHI, medication, plate) is a finding even
    though the value alone matches no shape. Personal data has no entropy
    signature — unlike a credential, a date of birth is indistinguishable from
    any other date — so label context is the only available analogue of
    secretscan's context-free net. Added 2026-08-04 (ruled), sweep gap G1.

  * LITERAL terms (machine-local, never in a repo) are the actual names,
    addresses, medications, device IDs and deal figures unique to one person's
    estate. That list would itself be the leak if committed, so it lives at
    $ATELIER_LEAKSCAN_TERMS or ~/.claude/leakscan-terms.txt — outside every repo.
    Absent ⇒ the scan says so LOUDLY and runs structural-only, never silently
    weaker (legibility). A plain or `forms:` term also matches its plural and
    plural-possessive — `Term`, `Terms`, `Terms'` all hit, always on, fails
    closed (ruled 2026-09-18, roadmap 320/240: a possessive was evading a
    listed term while the scan reported clean). `regex:` terms are verbatim
    and untouched.

All three run over file CONTENT *and* over each file's repo-relative PATH — a
file whose *name* carries an address or a person's name leaks exactly as much as
one whose body does, and until 2026-08-04 the name was never read (gap G2). Path
findings report at line 0.

A tracked BINARY's body cannot be read, so since G3 (ruled 2026-08-04) it
blocks until a reasoned, hash-bound `.leakscanbinaries` entry accepts its exact
bytes; PNG/JPEG/WebP metadata is walked, text metadata scanned and opaque
metadata (Exif, IPTC) blocking on its own scope. See the G3 block below and
the leakscan section of `tools/README.md`.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean
  1  findings (blocks the commit)
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can run
it with the system python3 and no install.
"""

from __future__ import annotations

import argparse
import codecs
import fnmatch
import hashlib
import json
import os
import re
import struct
import subprocess
import sys
import tempfile
import zlib
from dataclasses import dataclass, asdict, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import filewalk  # noqa: E402
import allowmarker  # noqa: E402

# A line carrying this marker is intentionally exempt (e.g. an illustrative
# example in doctrine). Keep the reason on the same line so the exemption is
# self-documenting and greppable.
#
# GOVERNED BY `method/GUARDS.md` — narrow, noisy, reasoned, declared:
#
#   * NARROW. Two forms. `leakscan:allow: <reason>` exempts every STRUCTURAL
#     rule on the line; `leakscan:allow:<rule>: <reason>` exempts only that one
#     (`leakscan:allow:ipv4: rendered example`), so a marker written for a
#     false-positive email no longer silently exempts a MAC address sitting on
#     the same line. A scoped name that matches no rule exempts NOTHING — a
#     typo fails closed and the finding still reports.
#   * REASONED. The marker only counts with a colon and a non-empty reason, so
#     prose that merely mentions the marker text does not exempt anything. A
#     bare `leakscan:allow` with no reason is a MENTION, not an exemption —
#     tightened 2026-08-05; it used to exempt the whole line.
#   * NOISY. Every suppression is counted and reported (see `Tally`). The scan
#     finds first and subtracts second, so a clean run states what it removed
#     rather than looking identical to a run that found nothing.
#
# D1 (Mike ruled 2026-08-04): an allow-marker exempts STRUCTURAL rules only.
# The machine-local term list always runs — it is the highest-confidence layer,
# and switching it off because a human judged the line safe for an unrelated
# structural reason is exactly backwards. A term-list misfire is fixed in the
# term list, which is the operator's own config.
#
# THE ONE DELIBERATE HATCH (Mike ruled 2026-08-09): a marker whose scope NAMES
# `local-term` explicitly — `leakscan:allow:local-term: <reason>` — exempts
# term hits on that line. This is not a D1 reversal; it is its complement. D1
# closed the ACCIDENTAL route (a marker written for a structural false positive
# silently taking the term layer with it); this opens only the deliberate one,
# where naming the highest-confidence layer in the scope IS the human judging
# exactly that layer, on the record, with a reason. The forcing case: atelier
# publishes its author's own git identity as ADR 0005's named worked example,
# and the term list cannot express "this name is public in THIS repo". Scopes
# compose with commas (`leakscan:allow:email,local-term: <reason>`) because
# such a line usually needs the structural email rule exempted too — one
# marker, each covered rule named.
ALLOW_MARKER = "leakscan:allow"

# `<marker>[:<rule>[,<rule>…]]: <non-empty reason>`. The optional rule group
# cannot swallow a plain reason: `leakscan:allow: a reason` fails the inner `:`
# after `a` and backtracks to the unscoped form, so both spellings parse
# correctly.
ALLOW_RX = allowmarker.marker_rx(ALLOW_MARKER, scope="list", group="rule")


def parse_allow(line: str) -> frozenset[str] | None:
    """The scope of the line's allow-marker, or None if it carries none.

    Returns an empty frozenset for the unscoped form (every STRUCTURAL rule —
    never the term list, D1) or the named rules for the scoped form. A marker
    without a reason returns None — it is a mention, not an exemption."""
    return allowmarker.scopes_of(ALLOW_RX, line, "rule")

# Documentation-reserved / non-routable ranges that are safe to appear in
# shareable docs (RFC 5737 TEST-NET + the loopback net). Real private
# addresses are NOT here — those are estate topology and must be flagged.
#
# PREFIXES are network prefixes and end in a dot, so the match is genuinely
# "inside this network" and cannot run past an octet boundary. D6 (ruled
# 2026-08-04): the unspecified address used to sit in this tuple, where the
# startswith test exempted anything merely BEGINNING with those characters —
# an octet of two or three digits in the last position was exempt for free.
# Fixed-value addresses belong in the exact set below, matched exactly.
SAFE_IP_PREFIXES = ("192.0.2.", "198.51.100.", "203.0.113.", "127.")


def _netmask_literals() -> frozenset[str]:
    """Every contiguous IPv4 netmask, 0.0.0.0 through 255.255.255.255.

    Computed rather than listed: the set is exactly 33 values, none of which is
    assignable to a host, so naming them by construction is both complete and
    impossible to get subtly wrong. This is D3's "common netmask literals" —
    networking prose that quotes a mask was a guaranteed allow-marker generator.
    """
    out = set()
    for bits in range(33):
        v = (0xFFFFFFFF << (32 - bits)) & 0xFFFFFFFF
        out.add(".".join(str((v >> s) & 0xFF) for s in (24, 16, 8, 0)))
    return frozenset(out)


# D3 (ruled 2026-08-04): widen the safe set past the doc ranges. These are
# addresses that carry NO estate topology — a netmask, the unspecified and
# broadcast addresses, and the well-known public resolvers every network doc
# names. Flagging them produced findings whose only possible resolution was an
# allow-marker, which is the false-positive class GUARDS.md says to fix at the
# rule. Note what is deliberately absent: RFC 1918 space, CGNAT and link-local
# are real topology and still flag.
SAFE_IP_EXACT = _netmask_literals() | frozenset({
    "8.8.8.8", "8.8.4.4",            # Google Public DNS
    "1.1.1.1", "1.0.0.1",            # Cloudflare
    "9.9.9.9", "149.112.112.112",    # Quad9
    "208.67.222.222", "208.67.220.220",  # OpenDNS
})

DEFAULT_LOCAL_TERMS = "~/.claude/leakscan-terms.txt"

# Paths never worth scanning. Hardcode-skip ONLY names that are never
# human-authored content — VCS, dependency, and tool-cache dirs. `build`/`dist`
# are DELIBERATELY absent (2026-07-11 child-CI-floor review, N1 — the same
# masking linkscan fixed at d0870a4): a content dir can legitimately share the
# name (atelier's own docs/build/ doctrine layer), and skipping it by name made
# a whole-tree scan blind to a planted leak there. Masking a layer is the worst
# failure a publish-safety scanner has; a repo with a real build-output dir
# names it in `.leakscanignore` (one line). Repo-specific globs come from
# .leakscanignore at the scan root.
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}


@dataclass(frozen=True)
class Pattern:
    name: str
    severity: str  # "high" | "medium" — advisory only; any hit still blocks
    regex: "re.Pattern[str]"


def _p(name: str, severity: str, rx: str, flags: int = 0) -> Pattern:
    return Pattern(name, severity, re.compile(rx, flags))


# --- the personal-data key vocabulary (G1) -------------------------------
#
# The mirror of secretscan's credential-key rule, for the other half of the
# boundary. Every alternative below is a key name that ANNOUNCES its value as
# personal data, so the value needs no shape of its own — which is the whole
# point: a date of birth is shaped like every other date, a passport number
# like every other SKU, and the sweep's don't-add list rules out detecting
# those context-free (letters-plus-digits is the shape of ticket refs; a bare
# date rule fires on every record in the estate).
#
# The vocabulary is deliberately COMPOUND where a bare word would be ambiguous:
# `bank_account` and `account_number`, never bare `account`; `number_plate` and
# `rego`, never bare `plate` (which lives inside `template`); `home_address`,
# never bare `address` (an IP or a memory address is not personal data); an IRD
# key must name itself a number, because the bare three letters are also how a
# sentence labels a clause about the tax department, and the digits themselves
# are the `nz-ird` rule's job.
#
# ONE KEY WAS TRIED AND WITHDRAWN, measured against this repo: the
# diagnosis/diagnoses pair. It is a genuine health key and it is also how every
# root-cause paragraph in the estate opens — three live false positives in
# records on the first tree-wide run. Health cover comes from the medication,
# prescription, allergy and blood-type keys instead. Left here as a note
# because the next person to widen this vocabulary will reach for it again.
_KEY_LEAD = r"(?:\b|_|(?-i:(?<=[a-z0-9])(?=[A-Z])))"
PII_KEY_RX = (
    r"(?i)" + _KEY_LEAD + r"(?P<key>"
    r"d\.?o\.?b|dates?[_ -]?of[_ -]?birth|birth[_ -]?dates?|birthdays?"
    r"|bank[_ -]?accounts?|accounts?[_ -]?(?:number|no)|acct[_ -]?(?:number|no)"
    r"|iban|bsb|sort[_ -]?code|routing[_ -]?number"
    r"|cards?[_ -]?number|credit[_ -]?card|cardholder|cvv|cvc"
    r"|passports?(?:[_ -]?(?:number|no))?"
    r"|drivers?'?[_ -]?licen[cs]e|licen[cs]e[_ -]?(?:number|no|plate)"
    r"|number[_ -]?plate|vehicle[_ -]?plate|rego"
    r"|nhi(?:[_ -]?number)?|nhs[_ -]?number|medicare|ssn|social[_ -]?security"
    r"|tax[_ -]?(?:file[_ -]?)?(?:number|id)|tfn|ird[_ -]?(?:number|no)"
    r"|medications?|prescriptions?|blood[_ -]?type|allerg(?:y|ies)"
    r"|patients?(?:[_ -]?name)?|next[_ -]?of[_ -]?kin|emergency[_ -]?contact"
    r"|maiden[_ -]?name|mothers?'?[_ -]?maiden"
    r"|(?:home|street|postal|residential|physical)[_ -]?address"
    r")\b\s*[:=]\s*[\"']?(?P<value>[^\s\"'`,;:]{2,})")

# Structural patterns. Ordered high→medium. Tuned to catch real estate/PII shapes
# while keeping false positives survivable (fail-safe favours over-flagging: a
# false positive costs a `leakscan:allow`, a false negative costs a leak).
STRUCTURAL: list[Pattern] = [
    _p("private-key-header", "high",
       r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"),
    _p("aws-access-key-id", "high", r"\bAKIA[0-9A-Z]{16}\b"),
    _p("jwt", "high", r"\beyJ[A-Za-z0-9_-]{6,}\.eyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}"),
    _p("email", "high",
       r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    # G1 — the key-context layer. High: the label has already done the
    # filtering, so a surviving hit is about as confident as this tool gets.
    _p("pii-key-context", "high", PII_KEY_RX),
    # G4 — financial identifiers. Card and IBAN are SELF-VALIDATING (Luhn and
    # ISO 7064 mod-97 respectively, both applied in VALIDATORS below), which is
    # what keeps a long digit run from being a false-positive engine. The
    # grouped alternative exists so the space- and hyphen-separated spellings
    # of a card are caught without letting a single-space separator stitch an
    # arbitrary numeric table row into a sixteen-digit "card".
    _p("payment-card", "high",
       r"(?<![\d-])(?:\d{13,19}|\d{4}(?:[ -]\d{4}){2,3}(?:[ -]\d{1,3})?)(?![\d-])"),
    _p("iban", "high", r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b"),
    _p("mac-address", "high",
       r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b"),
    _p("ipv4", "medium", r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    # D2 (ruled 2026-08-04, and E4 with it): require `::` OR four-plus groups.
    # The old rule took any THREE colon-separated hex-ish groups, which is also
    # the shape of `HH:MM:SS`, a port map, a ratio and a hex colour triplet —
    # a false-positive class the sweep confirmed is far wider than the two
    # clock times originally recorded. The compressed form additionally
    # requires TWO hex groups in total, so a Python slice (`a[::2]`) and a bare
    # loopback/unspecified address are not addresses this rule reports.
    _p("ipv6", "medium",
       r"(?<![0-9A-Za-z:])(?:"
       r"[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4}){1,6}::"
       r"(?:[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4}){0,5})?"
       r"|[0-9A-Fa-f]{1,4}::[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4}){0,5}"
       r"|::[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4}){1,5}"
       r"|[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4}){3,7}"
       r")(?![0-9A-Za-z:])"),
    # G4 — the NZ bank account in its hyphenated field form (bank-branch-
    # account-suffix). The COMPACT all-digit form stays key-context-only per
    # the ruling: bare eight-to-sixteen digit runs are the don't-add list.
    _p("nz-bank-account", "medium", r"\b\d{2}-\d{4}-\d{7}-\d{2,3}\b"),
    # G7 — the bracketed area-code form (landline or mobile prefix in
    # parentheses), the one common NZ spelling the rule missed.
    _p("nz-phone", "medium",
       r"(?<!\d)(?:"
       r"(?:\+64[\s-]?|0)(?:2\d|[3-9])"
       r"|\((?:\+64[\s-]?)?0?(?:2\d|[3-9])\)"
       r")[\s-]?\d{3}[\s-]?\d{3,4}(?!\d)"),
    # D4 (ruled 2026-08-04): the abbreviated and bare-word suffixes now need at
    # least one capitalised word in front of them. Without it, a low number
    # beside an abbreviation or an ordinary English word — a figure reference,
    # a count of somethings — read as an address. The distinctive full-word
    # suffixes keep the permissive form, so a number and a bare Terrace or
    # Crescent still flags with no street name in front of it.
    _p("nz-address", "medium",
       r"\b\d{1,4}[A-Za-z]?\s+(?:"
       r"(?:[A-Z][a-z]+\s+){0,2}"
       r"(?:Street|Road|Avenue|Lane|Drive|Terrace|Crescent)"
       r"|(?:[A-Z][a-z]+\s+){1,2}"
       r"(?:St|Rd|Ave|Ln|Dr|Pl|Tce|Cres|Place|Way|Close|Grove|Hill|Green)"
       r")\b"),
    _p("coordinates", "medium",
       r"[-+]?\d{1,2}\.\d{4,}\s*,\s*[-+]?\d{1,3}\.\d{4,}"),
    _p("nz-ird", "medium", r"\b\d{2,3}-\d{3}-\d{3}\b"),
]

# D5 (ruled 2026-08-04): one span, one finding. A MAC address is six colon-
# separated hex pairs, which is also a valid four-plus-group IPv6 shape, so the
# same twelve characters reported twice — cosmetic, but a duplicated finding
# teaches a reader to skim the list, which is how a real second finding gets
# missed. The shadowing rule wins; the shadowed one skips any span it overlaps.
#
# Shadow spans are computed from the REGEX ALONE, before allow-markers are
# consulted: if a MAC is exempted on the line, the ipv6 rule must not step in
# and re-report the exact characters the exemption was written for. A DISABLED
# shadower casts no shadow, so `--disable mac-address` leaves no blind spot.
SHADOWED_BY: dict[str, tuple[str, ...]] = {
    "ipv6": ("mac-address",),
}


# 020/380 — a fixed ceiling on how many `Finding` objects one run MATERIALIZES
# (builds and holds in memory), independent of how many the input actually
# contains. The same defect `020/370` fixed in `secretscan` (an unbounded
# `findings` list held every hit for the whole run) applies here byte for
# byte: this scanner's STRUCTURAL patterns run `finditer` per line per rule,
# so a pathological/adversarial tree can generate an unbounded NUMBER of
# findings independent of tree size. Reusing secretscan's own derivation
# rather than re-deriving one: each held `Finding` costs on the order of
# 1 KiB (path + excerpt strings + object overhead), so a ~50 MiB findings
# budget — independent of input size — gives the same round cap. Findings
# past the cap are COUNTED (`Tally.findings_over_cap`), never dropped
# silently.
MAX_MATERIALIZED_FINDINGS = 50_000


@dataclass
class Tally:
    """What the scan removed AFTER finding it — rule (b) of `method/GUARDS.md`.

    Without this, a guard that subtracts silently prints the same clean tick
    for "nothing matched" and "forty things matched and every one of them was
    exempted", which are opposite states of the world. The second is where an
    allowance has quietly grown past what anyone approved."""
    by_marker: dict[str, int] = field(default_factory=dict)   # rule name -> hits
    files_by_glob: int = 0
    disabled_rules: tuple[str, ...] = ()
    # 020/380 — see MAX_MATERIALIZED_FINDINGS above. Every finding is BLOCKING
    # here (leakscan has no advisory tier), so one counter is enough — unlike
    # secretscan's blocking/advisory split.
    findings_over_cap: int = 0
    # G3: tracked binaries whose body the scan could not read and a reasoned,
    # hash-bound `.leakscanbinaries` entry accepted; and binaries the
    # full-tree walk met that git does not track, which the gate does not
    # cover (an untracked file reaches no remote). Both are counted so a
    # clean run says what it did not read.
    binaries_by_manifest: int = 0
    binaries_untracked: int = 0
    _materialized: int = field(default=0, repr=False, compare=False)

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def take_finding_slot(self) -> bool:
        """True if a finding may still be fully materialized (built and
        held); False once the run-wide cap is reached, in which case the
        caller counts it via `findings_over_cap` instead of building a
        `Finding` for it."""
        if self._materialized < MAX_MATERIALIZED_FINDINGS:
            self._materialized += 1
            return True
        self.findings_over_cap += 1
        return False

    def note_marker(self, rule: str) -> None:
        self.by_marker[rule] = self.by_marker.get(rule, 0) + 1

    def summary(self) -> str:
        """One stable line, zeros printed. The field set never varies between
        runs so two runs can be read side by side (a missing field would read
        as a zero rather than as 'this run did not measure it')."""
        parts = [f"{self.marker_total} by allow-marker",
                 f"{self.files_by_glob} file(s) by .leakscanignore",
                 f"{len(self.disabled_rules)} rule(s) disabled",
                 f"{self.binaries_by_manifest} binary file(s) by {BINARY_MANIFEST}",
                 f"{self.binaries_untracked} untracked binary file(s) not gated",
                 f"{self.findings_over_cap} beyond the "
                 f"{MAX_MATERIALIZED_FINDINGS}-finding cap (counted, not listed)"]
        line = "  suppressed: " + " · ".join(parts)
        if self.by_marker:
            detail = ", ".join(f"{r}×{n}" for r, n in sorted(self.by_marker.items()))
            line += f"\n    allow-marker breakdown: {detail}"
        if self.disabled_rules:
            line += f"\n    disabled: {', '.join(self.disabled_rules)}"
        return line


@dataclass
class Finding:
    path: str
    line: int
    rule: str          # pattern name or "local-term"
    kind: str          # "structural" | "local"
    severity: str
    excerpt: str       # the matched span, redacted to keep the report shareable
    # G3: where inside the file a finding sits when it is not a text line —
    # "binary" for a gate finding about the file as a whole, or
    # "metadata <segment>" for a hit in an image's text metadata (then `line`
    # counts within that segment). Empty for ordinary text and path findings.
    where: str = ""


def redact(match: str) -> str:
    """Keep enough to locate the hit, not enough to re-leak it in the report."""
    if len(match) <= 6:
        return match[0] + "*" * (len(match) - 1)
    return f"{match[:3]}…{match[-2:]} ({len(match)} chars)"


def _ipv4_is_safe(text: str) -> bool:
    """D6: exact values match EXACTLY; only network prefixes match by prefix."""
    return text in SAFE_IP_EXACT or any(text.startswith(p) for p in SAFE_IP_PREFIXES)


# --- placeholder suppression (G1's other half) ---------------------------
#
# The key-context rule fires on a LABEL, so without this it would fire on every
# piece of documentation that shows the label — a template, an example config,
# a fill-in-the-blank form. secretscan learned the same lesson on the
# credential half; leakscan had no suppression of any kind before 2026-08-04.
# The list is intentionally the PII-flavoured one, not a copy of secretscan's:
# the shapes that stand in for a person's data are format specs and fill-mes,
# not `${VAR}` env indirection (though that is covered too).
PLACEHOLDER_SUBSTRINGS = (
    "example", "placeholder", "redacted", "changeme", "change-me", "change_me",
    "sample", "dummy", "fake", "notreal", "fictional", "your-", "your_",
    "yourname", "todo", "fixme", "xxxx", "****", "……", "...", "n/a",
)
PLACEHOLDER_EXACT = frozenset({
    "", "-", "?", "…", "0", "none", "null", "nil", "undefined", "unknown",
    "true", "false", "na", "n/a", "tbc", "tbd", "redacted", "anonymous",
})
# Templating markers must be CLOSED to count — the open-marker bug secretscan
# hit on 2026-07-28, where a real value containing a stray `$(` was written off
# as a template. Same trap, so the same shape of fix.
TEMPLATE_RX = re.compile(
    r"\$\{[^{}]*\}|\$\([^()]*\)|%\([^()]*\)|\{\{[^{}]*\}\}|<[^<>]{1,64}>")
# A FORMAT SPEC is a placeholder that looks like data: `yyyy-mm-dd`,
# `dd/mm/yyyy`, `nnn-nnn-nnn`. Letters drawn only from the format alphabet,
# with no digits at all — real data of these classes always carries digits.
_FORMAT_ALPHABET = set("ymdhnsx#-/. ")


def _is_format_spec(value: str) -> bool:
    low = value.lower()
    return (any(c.isalpha() for c in low)
            and not any(c.isdigit() for c in low)
            and set(low) <= _FORMAT_ALPHABET)


def _is_placeholder(value: str) -> bool:
    low = value.lower().strip("\"'")
    if low in PLACEHOLDER_EXACT:
        return True
    if any(sub in low for sub in PLACEHOLDER_SUBSTRINGS):
        return True
    if TEMPLATE_RX.search(value) or _is_format_spec(value):
        return True
    # `!secret foo`, `$VAR`, `env:FOO` — a REFERENCE to data held elsewhere is
    # the pattern we want people to use, never the data itself.
    if re.match(r"^(?:!\s*secret\b|\$[A-Za-z_{(]|env:|vault:|sops:|@@)", value):
        return True
    # a run of one repeated character (xxxx, ----, 0000) is never real data
    if len(set(value)) <= 1:
        return True
    return False


def _luhn_ok(text: str) -> bool:
    """The card-number check digit (ISO/IEC 7812), plus a brand-prefix guard.

    Luhn alone lets one random digit run in ten through; requiring the issuer
    identifier to start 2–6 (the assigned major-industry range for payment
    cards) drops that again without excluding any real card. Together they are
    what makes a bare digit run safe to flag at all — the sweep's don't-add
    list rules out bare-digit rules that self-validate against nothing."""
    digits = [int(c) for c in text if c.isdigit()]
    if not 13 <= len(digits) <= 19 or digits[0] not in (2, 3, 4, 5, 6):
        return False
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def _iban_ok(text: str) -> bool:
    """ISO 13616 / 7064 mod-97 check: rotate the first four characters to the
    end, map letters to two-digit numbers, and require a remainder of 1."""
    if not 15 <= len(text) <= 34:
        return False
    rotated = text[4:] + text[:4]
    try:
        numeric = "".join(str(int(c, 36)) for c in rotated)
    except ValueError:
        return False
    return int(numeric) % 97 == 1


# Per-rule post-match validators: the regex says "this is the right SHAPE", the
# validator says "and it is not one of the shapes we ruled out". Keeping them
# beside the patterns means a rule's exclusions are readable in one place
# rather than accreting as special cases inside the scan loop. A rule with no
# entry here keeps every match.
VALIDATORS: dict[str, "object"] = {
    "ipv4": lambda m: not _ipv4_is_safe(m.group(0)),
    "payment-card": lambda m: _luhn_ok(m.group(0)),
    "iban": lambda m: _iban_ok(m.group(0)),
    "pii-key-context": lambda m: not _is_placeholder(m.group("value")),
}


def derived_form_regex(term: str) -> "re.Pattern[str]":
    """G6 — the OPT-IN derived-form matcher behind a `forms:` term.

    A name leaks as a slug, a localpart or an identifier far more often than as
    the canonical spaced literal: the sweep probed a listed name's slug,
    camel-case, snake-case and double-spaced forms and every one passed clean.
    This joins the term's words with `[\\s._-]*`, so one term covers
    `jane-q-public`, `jane_q_public`, `jane.q.public`, `janeQPublic`,
    `janeqpublic` and any whitespace run between the words.

    OPT-IN, and it stays opt-in: the zero-separator form means a short or
    common-word term can start matching inside ordinary compounds, and only the
    operator holding the real list can judge that. Word boundaries still bound
    both ends. LIMIT, stated because it is not obvious: scanning is line-based,
    so a name split ACROSS lines is still not matched by anything.

    Also carries the plural/plural-possessive suffix (PLURAL_SUFFIX, ruled
    2026-09-18) so `jane-q-publics` and `jane-q-publics'` hit alongside the
    bare derived form."""
    parts = [re.escape(p) for p in term.split() if p]
    return re.compile(r"\b" + r"[\s._-]*".join(parts) + PLURAL_SUFFIX, re.IGNORECASE)


# Mike ruled 2026-09-18 (roadmap 320/240): a listed term must ALSO catch its
# plural and plural-possessive inflections, always on, fails closed. `\bTerm\b`
# already matches `Term's` — the `\b` sits at the boundary before the
# apostrophe regardless of what follows it, so the singular possessive needed
# no change (verified in tools/test_leakscan.py). What it never matched was
# the bare plural `Terms` or the plural possessive `Terms'`, because neither
# has an `s` at all in the listed spelling. Appending an OPTIONAL trailing `s`
# before the closing `\b` closes both at once: the same boundary-before-
# non-word-char reasoning that already covered `Term's` now covers `Terms'`
# for free once the `s` is there to place a boundary after.
#
# SIMPLE ON PURPOSE, per the ruling: this is one optional literal `s`, not
# English pluralisation. A term already ending in `s` (`Widgets`) gets an
# optional DOUBLED `s` (`Widgetss`) rather than the real plural (`Widgetses`)
# — that miss is accepted rather than special-cased; state it, don't fix it.
# `regex:` terms are operator-authored verbatim and are NEVER touched by this.
PLURAL_SUFFIX = r"(?:s)?\b"


def load_local_terms(path: Path | None) -> tuple[list[tuple[str, "re.Pattern[str]"]], str | None]:
    """Return (compiled terms, warning). Each line is a case-insensitive
    whole-word literal, unless prefixed `regex:` for a raw pattern or `forms:`
    for a literal plus its derived separator/case variants (G6). `#` comments
    and blank lines are ignored.

    Every literal (plain or `forms:`) also matches its plural and plural-
    possessive inflection — `Term`, `Terms`, `Terms'` all hit; only `regex:` is
    exempt, verbatim (ruled 2026-09-18, see PLURAL_SUFFIX)."""
    if path is None:
        return [], (
            "no local term list found — scanned STRUCTURAL patterns only. "
            f"Set $ATELIER_LEAKSCAN_TERMS or create {DEFAULT_LOCAL_TERMS} for full cover.")
    terms: list[tuple[str, "re.Pattern[str]"]] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("regex:"):
            body = line[len("regex:"):].strip()
            terms.append((body, re.compile(body, re.IGNORECASE)))
        elif line.startswith("forms:"):
            body = line[len("forms:"):].strip()
            terms.append((body, derived_form_regex(body)))
        else:
            terms.append((line, re.compile(r"\b" + re.escape(line) + PLURAL_SUFFIX, re.IGNORECASE)))
    return terms, None


BY_NAME: dict[str, Pattern] = {p.name: p for p in STRUCTURAL}


def _shadow_spans(line: str, disabled: frozenset[str]) -> dict[str, list[tuple[int, int]]]:
    """D5 — per shadowed rule, the spans another rule has already claimed."""
    out: dict[str, list[tuple[int, int]]] = {}
    for shadowed, shadowers in SHADOWED_BY.items():
        if shadowed in disabled:
            continue
        spans = [m.span()
                 for name in shadowers if name not in disabled
                 for m in BY_NAME[name].regex.finditer(line)]
        if spans:
            out[shadowed] = spans
    return out


def _record(findings: list[Finding], tally: Tally | None, finding: Finding) -> None:
    """Append `finding` unless the run-wide materialization cap (020/380,
    `MAX_MATERIALIZED_FINDINGS`) has been reached — in which case
    `tally.take_finding_slot` has already counted it and there is nothing
    left for the caller to hold. The single choke point every finding in
    `scan_lines` passes through, so the cap cannot be forgotten at a new
    call site — the same shape as `secretscan._record` (020/370)."""
    if tally is None or tally.take_finding_slot():
        findings.append(finding)


def scan_lines(path: str, numbered_lines: list[tuple[int, str]],
              local_terms: list[tuple[str, "re.Pattern[str]"]],
              disabled: frozenset[str] = frozenset(),
              tally: Tally | None = None,
              honour_markers: bool = True) -> list[Finding]:
    """The scanning engine. `numbered_lines` pairs each line of text with its
    real line number — the shape `_scan_file` needs to call this once per
    physical line while streaming a file, and `scan_text` below is the
    whole-blob convenience wrapper every existing caller (staged mode, the
    path-name scan, the test suite) uses.

    `honour_markers=False` (G3, image metadata) reads an allow-marker as
    plain text: a marker inside a binary's metadata sits where no reviewer
    reads it, which `method/GUARDS.md` § *Who, why, when* forbids."""
    findings: list[Finding] = []
    for lineno, line in numbered_lines:
        allow_scope = parse_allow(line) if honour_markers else None
        shadows = _shadow_spans(line, disabled)
        for pat in STRUCTURAL:
            if pat.name in disabled:
                continue
            validator = VALIDATORS.get(pat.name)
            claimed = shadows.get(pat.name, ())
            for m in pat.regex.finditer(line):
                span = m.group(0)
                # The shape matched; now the rule's own exclusions (safe IP
                # ranges, a failed checksum, a placeholder value) get a say.
                if validator is not None and not validator(m):
                    continue
                if any(s < m.end() and m.start() < e for s, e in claimed):
                    continue
                # FIND FIRST, SUBTRACT SECOND (rule b). The hit is fully
                # formed before the allowance is consulted, so the exemption
                # can be counted rather than vanishing at the top of the loop.
                if allow_scope is not None and (not allow_scope
                                               or pat.name in allow_scope):
                    if tally is not None:
                        tally.note_marker(pat.name)
                    continue
                _record(findings, tally, Finding(path, lineno, pat.name, "structural",
                                                 pat.severity, redact(span)))
        # D1: the term list runs on EVERY line — the unscoped marker never
        # reaches it. The ONE exemption is a scope naming `local-term`
        # explicitly (ruled 2026-08-09): deliberate, reasoned, counted.
        for term, rx in local_terms:
            if rx.search(line):
                if allow_scope is not None and "local-term" in allow_scope:
                    if tally is not None:
                        tally.note_marker("local-term")
                    continue
                _record(findings, tally, Finding(path, lineno, "local-term", "local",
                                                 "high", f"term:{term[:2]}…"))
    return findings


def scan_text(path: str, text: str,
              local_terms: list[tuple[str, "re.Pattern[str]"]],
              disabled: frozenset[str] = frozenset(),
              tally: Tally | None = None,
              honour_markers: bool = True) -> list[Finding]:
    """Scan a whole text blob, numbering lines sequentially from 1 — the
    staged-diff and path-name callers' shape (both already hold their input
    in memory: a diff's added lines, or a single path string)."""
    return scan_lines(path, list(enumerate(text.splitlines(), start=1)),
                      local_terms, disabled, tally, honour_markers)


def scan_path_name(rel: str,
                   local_terms: list[tuple[str, "re.Pattern[str]"]],
                   disabled: frozenset[str] = frozenset(),
                   tally: Tally | None = None) -> list[Finding]:
    """G2 — run the same rule set over the repo-relative PATH, reporting at
    line 0.

    A file whose NAME carries an address, a person or a phone number leaks
    exactly as much as one whose body does, and the name was never read before
    2026-08-04. Measured cost when the sweep proposed it: zero findings over
    this repo's 390 tracked paths.

    A path cannot carry an inline allow-marker, so the only hatch here is
    `.leakscanignore` — which callers apply before this runs, so a path already
    exempted by a glob never reaches it."""
    return [Finding(rel, 0, f.rule, f.kind, f.severity, f.excerpt)
            for f in scan_text(rel, rel, local_terms, disabled, tally)]


def _looks_binary(data: bytes) -> bool:
    return b"\x00" in data[:8192]


IgnoreFileError = allowmarker.IgnoreFileError


def load_ignore_globs(root: Path) -> list[str]:
    """Globs from `.leakscanignore`, each of which MUST carry a stated reason.
    Single-sourced (115/080 part 2) in `tools/allowmarker.py`; this
    scanner supplies only its own ignore-file name."""
    return allowmarker.load_ignore_globs(root, ".leakscanignore")


def _ignored(rel: str, globs: list[str]) -> bool:
    return allowmarker.ignored(rel, globs)


# ─── G3 — binary media (Mike ruled BLOCKING 2026-08-04, funded 2026-08-09) ───
#
# Until G3 a tracked binary's body was skipped in silence: only its NAME was
# read (G2), so a screenshot of a bank statement, or a photo whose Exif names
# its owner and where it was taken, passed as "clean". The ruling: a tracked
# binary that is unscannable, or that carries metadata, BLOCKS; a legitimate
# one carries a one-time REASONED marker; leakscan keeps no advisory form
# (E6a). This is the build of that ruling:
#
#   * THE MARKER is an entry in `.leakscanbinaries` at the scan root —
#     `<sha256 hex, ≥16 chars>[:binary-metadata]  <path>`, reasoned with the
#     SAME grammar as `.leakscanignore` (`allowmarker.read_reasoned_lines`: a
#     trailing `# reason` or a comment stanza). A binary cannot hold an inline
#     marker, and a `.leakscanignore` glob is the wrong hatch: it is
#     path-wide, rule-wide and blind to content, so a REPLACED image would
#     pass under the old acceptance. The digest is what makes "one-time"
#     true — a changed binary no longer matches its entry and blocks again,
#     and the human who re-lists it is looking at the new bytes.
#   * THE DIGEST is a hex PREFIX of SHA-256, at least 16 characters (64
#     bits). Full 64 also parses. The printed form is 16 because secretscan's
#     context-free entropy net reports every 32+ character run as an advisory
#     finding; a manifest of full digests would buy one advisory per binary on
#     every scan for no gain: the threat is an unnoticed change, not a forged
#     64-bit second preimage by someone who can edit the manifest anyway.
#   * METADATA is walked, not guessed, for the three web image formats
#     (PNG, JPEG, WebP), stdlib only, every read bounded. TEXT metadata (PNG
#     tEXt/zTXt/iTXt, JPEG XMP and comments, WebP XMP) is decoded and run
#     through the ordinary rule set and term list — a `Software` tag scans
#     clean, an author's name or email does not — with allow-markers NOT
#     honoured inside it. OPAQUE metadata (Exif, IPTC, ImageMagick's
#     hex-encoded raw profiles, an unrecognised APP1, a segment past the
#     size cap, a structure that cannot be walked) cannot be read as text, so
#     its PRESENCE blocks as `binary-metadata`; an entry clears that only by
#     naming the scope (`<digest>:binary-metadata`), so accepting the pixels
#     never silently accepts the GPS block too (GUARDS rule-scoped allowance).
#
# What it cannot see, stated so nobody infers cover that is not there: the
# pixels themselves (no OCR — the entry's reason is the human attesting to
# them); metadata in any other format (GIF, TIFF, HEIC/AVIF, PDF, Office
# documents, fonts, archives — for these the entry accepts the whole file,
# metadata included); JPEG segments after the first start-of-scan; ICC
# profiles; bytes appended after a format's end marker.
#
# THE GATE COVERS TRACKED BINARIES (the ruling's word). A full-tree scan of a
# git work tree gates the files `git ls-files` lists and counts the rest
# (`.DS_Store`, build output) as "not gated"; a scan of a directory that is
# not a git work tree gates every binary, failing closed. The staged plane
# gates every binary the commit adds, modifies or renames.
BINARY_MANIFEST = ".leakscanbinaries"
SCOPE_METADATA = "binary-metadata"
BINARY_RULES = ("binary-unlisted", "binary-changed", SCOPE_METADATA,
                "binary-stale-entry")
MIN_DIGEST_HEX = 16
PRINTED_DIGEST_HEX = 16
META_SEGMENT_CAP = 1 * 1024 * 1024   # bytes of ONE metadata segment read or
                                     # inflated; past it the segment is opaque
_ENTRY_RX = re.compile(r"^(?P<digest>[0-9A-Fa-f]{%d,64})(?::(?P<scope>[A-Za-z0-9_,-]+))?"
                       r"[ \t]+\*?(?P<path>\S.*)$" % MIN_DIGEST_HEX)


class BinaryManifestError(ValueError):
    """`.leakscanbinaries` is malformed, or grants an acceptance with no
    reason. A config error (exit 2), never a warning: a broken scan is not a
    pass."""


@dataclass(frozen=True)
class BinaryEntry:
    path: str
    digest: str               # lower-case hex prefix of the file's SHA-256
    scopes: frozenset[str]
    reason: str
    lineno: int

    def matches(self, sha256_hex: str) -> bool:
        return sha256_hex.startswith(self.digest)


def load_binary_manifest(root: Path) -> dict[str, BinaryEntry]:
    """Entries from `<root>/.leakscanbinaries`, keyed by repo-relative path.
    Every problem is collected and raised together as `BinaryManifestError`:
    an unreasoned entry, a malformed line, an unknown scope, a path listed
    twice. An absent file is no entries."""
    entries: dict[str, BinaryEntry] = {}
    problems: list[str] = []
    for n, body, reason in allowmarker.read_reasoned_lines(root / BINARY_MANIFEST):
        m = _ENTRY_RX.match(body)
        if not m:
            problems.append(f"line {n}: not '<sha256 hex, ≥{MIN_DIGEST_HEX} chars>"
                            f"[:{SCOPE_METADATA}]  <path>'")
            continue
        scopes = frozenset(m.group("scope").split(",")) if m.group("scope") else frozenset()
        unknown = scopes - {SCOPE_METADATA}
        if unknown:
            problems.append(f"line {n}: unknown scope {', '.join(sorted(unknown))} "
                            f"(the only scope is '{SCOPE_METADATA}')")
            continue
        path = m.group("path").strip()
        path = path[2:] if path.startswith("./") else path
        if reason is None:
            problems.append(f"line {n}: '{path}' has no stated reason")
            continue
        if path in entries:
            problems.append(f"line {n}: '{path}' already listed at line "
                            f"{entries[path].lineno}")
            continue
        entries[path] = BinaryEntry(path, m.group("digest").lower(), scopes, reason, n)
    if problems:
        raise BinaryManifestError(
            f"{BINARY_MANIFEST}: {len(problems)} problem(s) — {'; '.join(problems)}. "
            "Every accepted binary states its reason where a reviewer reads it "
            "(method/GUARDS.md): a comment above the stanza, or a trailing "
            "'# reason' on the line.")
    return entries


def _looks_binary_file(path: Path) -> bool:
    try:
        with open(path, "rb") as fh:
            return _looks_binary(fh.read(8192))
    except OSError:
        return False


def _sha256_file(fh) -> str:
    fh.seek(0)
    h = hashlib.sha256()
    for chunk in iter(lambda: fh.read(READ_CHUNK_BYTES), b""):
        h.update(chunk)
    return h.hexdigest()


def _inflate(data: bytes) -> bytes | None:
    """zlib-inflate at most `META_SEGMENT_CAP` bytes; None if the stream is
    corrupt or inflates past the cap (a decompression bomb reads as opaque,
    never as a long wait)."""
    d = zlib.decompressobj()
    try:
        out = d.decompress(data, META_SEGMENT_CAP)
    except zlib.error:
        return None
    return None if d.unconsumed_tail else out


def _png_metadata(fh, size: int, texts: list, opaque: list) -> None:
    pos = 8
    while True:
        fh.seek(pos)
        hdr = fh.read(8)
        if len(hdr) < 8:
            opaque.append("PNG ends without IEND")
            return
        n = struct.unpack(">I", hdr[:4])[0]
        ctype = hdr[4:8].decode("latin-1")
        if pos + 12 + n > size:
            opaque.append(f"PNG chunk {ctype} overruns the file")
            return
        if ctype == "IEND":
            return
        if ctype == "eXIf":
            opaque.append("PNG eXIf (Exif)")
        elif ctype in ("tEXt", "zTXt", "iTXt"):
            if n > META_SEGMENT_CAP:
                opaque.append(f"PNG {ctype} past the {META_SEGMENT_CAP}-byte cap")
            else:
                _png_text_chunk(ctype, fh.read(n), texts, opaque)
        pos += 12 + n


def _png_text_chunk(ctype: str, data: bytes, texts: list, opaque: list) -> None:
    keyword, _, rest = data.partition(b"\x00")
    kw = keyword.decode("latin-1")
    if kw.lower().startswith("raw profile type"):
        # ImageMagick carries Exif/IPTC/8BIM here as a hex dump of the binary
        # profile: text-shaped, but nothing a text rule can read.
        opaque.append(f"PNG {ctype} '{kw}' (hex-encoded binary profile)")
        return
    if ctype == "tEXt":
        value = rest.decode("latin-1")
    elif ctype == "zTXt":
        raw = _inflate(rest[1:])
        if raw is None:
            opaque.append(f"PNG zTXt '{kw}' (undecodable or past the cap)")
            return
        value = raw.decode("latin-1")
    else:  # iTXt: flag, method, language\0, translated keyword\0, text
        if len(rest) < 2:
            opaque.append(f"PNG iTXt '{kw}' (truncated)")
            return
        compressed = rest[0] == 1
        _lang, _, rest2 = rest[2:].partition(b"\x00")
        _tkw, _, body = rest2.partition(b"\x00")
        if compressed:
            body = _inflate(body)
            if body is None:
                opaque.append(f"PNG iTXt '{kw}' (undecodable or past the cap)")
                return
        value = body.decode("utf-8", errors="replace")
    texts.append((f"PNG {ctype} '{kw}'", f"{kw}: {value}"))


_XMP_NS = b"http://ns.adobe.com/xap/1.0/\x00"
_XMP_EXT_NS = b"http://ns.adobe.com/xmp/extension/\x00"


def _jpeg_metadata(fh, size: int, texts: list, opaque: list) -> None:
    pos = 2
    while True:
        fh.seek(pos)
        b = fh.read(2)
        if len(b) < 2:
            opaque.append("JPEG ends before image data")
            return
        if b[0] != 0xFF:
            opaque.append("JPEG structure cannot be walked")
            return
        marker = b[1]
        if marker == 0xFF:          # fill byte
            pos += 1
            continue
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        if marker in (0xDA, 0xD9):  # start of scan / end of image
            return
        ln = fh.read(2)
        n = struct.unpack(">H", ln)[0] if len(ln) == 2 else 0
        if n < 2 or pos + 2 + n > size:
            opaque.append("JPEG segment overruns the file")
            return
        if marker in (0xE1, 0xED, 0xFE):
            seg = fh.read(n - 2)    # ≤ 65533 bytes by the format's own limit
            if marker == 0xFE:
                texts.append(("JPEG comment", seg.decode("utf-8", errors="replace")))
            elif marker == 0xED:
                opaque.append("JPEG APP13 (IPTC/Photoshop)")
            elif seg.startswith(b"Exif\x00"):
                opaque.append("JPEG APP1 Exif")
            elif seg.startswith(_XMP_NS):
                texts.append(("JPEG XMP", seg[len(_XMP_NS):].decode("utf-8", errors="replace")))
            elif seg.startswith(_XMP_EXT_NS):
                # 32-byte GUID + 4-byte full length + 4-byte offset, then XML
                body = seg[len(_XMP_EXT_NS) + 40:]
                texts.append(("JPEG extended XMP", body.decode("utf-8", errors="replace")))
            else:
                opaque.append("JPEG APP1 (unrecognised)")
        pos += 2 + n


def _webp_metadata(fh, size: int, texts: list, opaque: list) -> None:
    fh.seek(4)
    riff_end = min(size, 8 + struct.unpack("<I", fh.read(4))[0])
    pos = 12
    while pos + 8 <= riff_end:
        fh.seek(pos)
        hdr = fh.read(8)
        fourcc = hdr[:4].decode("latin-1")
        n = struct.unpack("<I", hdr[4:8])[0]
        if pos + 8 + n > riff_end:
            opaque.append(f"WebP chunk {fourcc.strip()} overruns the file")
            return
        if fourcc == "EXIF":
            opaque.append("WebP EXIF")
        elif fourcc == "XMP ":
            if n > META_SEGMENT_CAP:
                opaque.append(f"WebP XMP past the {META_SEGMENT_CAP}-byte cap")
            else:
                texts.append(("WebP XMP", fh.read(n).decode("utf-8", errors="replace")))
        pos += 8 + n + (n & 1)


def inspect_media(fh) -> tuple[str | None, list[tuple[str, str]], list[str]]:
    """`(format, text segments, opaque segments)` for a PNG, JPEG or WebP
    file object; `(None, [], [])` for anything else. Text segments are
    `(label, decoded text)` to be scanned; opaque segments are labels whose
    presence blocks. Every read is bounded (`META_SEGMENT_CAP`, or the
    format's own 64 KiB segment limit for JPEG), so peak memory is
    independent of the file's size."""
    fh.seek(0, os.SEEK_END)
    size = fh.tell()
    fh.seek(0)
    head = fh.read(12)
    texts: list[tuple[str, str]] = []
    opaque: list[str] = []
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        fmt, walker = "png", _png_metadata
    elif head.startswith(b"\xff\xd8"):
        fmt, walker = "jpeg", _jpeg_metadata
    elif head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        fmt, walker = "webp", _webp_metadata
    else:
        return None, texts, opaque
    try:
        walker(fh, size, texts, opaque)
    except struct.error:
        opaque.append(f"{fmt.upper()} structure cannot be walked")
    return fmt, texts, opaque


def check_binary(path: Path, rel: str, entry: BinaryEntry | None,
                 local_terms: list[tuple[str, "re.Pattern[str]"]],
                 disabled: frozenset[str], tally: Tally | None,
                 by_digest: dict[str, str] | None = None) -> list[Finding]:
    """The G3 gate for ONE tracked binary: its text metadata scanned, its
    opaque metadata and its unread body each blocking unless `entry` — a
    reasoned `.leakscanbinaries` line whose digest matches these exact bytes
    — accepts them. `by_digest` (digest prefix → listed path) lets an
    unlisted file say "same bytes as the entry for <old path>", the rename
    case. An unreadable file blocks rather than passing."""
    findings: list[Finding] = []

    def gate(rule: str, excerpt: str) -> None:
        _record(findings, tally, Finding(rel, 0, rule, "binary", "high", excerpt, "binary"))

    try:
        with open(path, "rb") as fh:
            digest = _sha256_file(fh)
            _fmt, texts, opaque = inspect_media(fh)
    except OSError as e:
        gate("binary-unlisted", f"unreadable ({e.__class__.__name__})")
        return findings
    for label, text in texts:
        for f in scan_text(rel, text, local_terms, disabled, tally, honour_markers=False):
            f.where = f"metadata {label}"
            findings.append(f)
    accepted = entry is not None and entry.matches(digest)
    if opaque and not (accepted and SCOPE_METADATA in entry.scopes):
        gate(SCOPE_METADATA, "; ".join(opaque))
    if entry is None:
        twin = (by_digest or {}).get(digest[:MIN_DIGEST_HEX])
        hint = f" — same bytes as the entry for {twin}" if twin else ""
        gate("binary-unlisted", f"sha256 {digest[:PRINTED_DIGEST_HEX]}{hint}")
    elif not accepted:
        gate("binary-changed", f"listed {entry.digest[:PRINTED_DIGEST_HEX]}, "
                               f"now {digest[:PRINTED_DIGEST_HEX]} (line {entry.lineno})")
    elif tally is not None:
        tally.binaries_by_manifest += 1
    return findings


def _digest_index(manifest: dict[str, BinaryEntry]) -> dict[str, str]:
    return {e.digest[:MIN_DIGEST_HEX]: e.path for e in manifest.values()}


def _stale(entry: BinaryEntry, why: str) -> Finding:
    """An entry that accepts nothing — its file is gone, untracked, or read
    as text. Blocking, because the manifest is the repo's standing inventory
    of what the scan does not read (GUARDS rule b), and an inventory naming
    files that are not there is one nobody can trust. The fix is one deleted
    or re-pathed line, normally in the same commit that moved the file."""
    return Finding(BINARY_MANIFEST, entry.lineno, "binary-stale-entry", "binary",
                   "high", f"{entry.path}: {why}")


def tracked_files(root: Path) -> set[str] | None:
    """Root-relative paths git tracks under `root`, or None when `root` is
    not inside a git work tree — in which case every binary is gated (fail
    closed)."""
    try:
        r = subprocess.run(["git", "-C", str(root), "ls-files", "-z"],
                           capture_output=True, check=False)
    except OSError:
        return None
    if r.returncode != 0:
        return None
    return {p for p in r.stdout.decode("utf-8", errors="surrogateescape").split("\0") if p}


def _walk_files(base: Path):
    """Every regular file under `base`, streamed one at a time. Single-sourced
    (115/080 part 1) in `tools/filewalk.py` — see that module's docstring
    for the mechanism and the 020/160 (E9) linked-worktree skip (measured in
    `faves` 2026-08-15: 101 leakscan findings, all already covered by
    `.leakscanignore`, blocked a commit — the incident that motivated that
    fix). `SKIP_DIR_NAMES` is this scanner's own per-guard parameter, passed
    in rather than shared."""
    return filewalk.walk_files(base, SKIP_DIR_NAMES)


def iter_files(paths: list[Path], root: Path, globs: list[str],
               tally: Tally | None = None):
    for base in paths:
        candidates = [base] if base.is_file() else _walk_files(base)
        for p in candidates:
            # Resolve BOTH sides so rel is root-relative no matter the caller's
            # CWD (2026-07-11 review N3): floor.yml runs `--root repo repo` from
            # the workspace, where the unresolved relative_to raised and the
            # fallback quietly produced CWD-relative paths — so the scanned
            # repo's own .leakscanignore globs never matched.
            try:
                rel = str(p.resolve().relative_to(root.resolve()))
            except ValueError:
                rel = str(p)
            if _ignored(rel, globs):
                if tally is not None:
                    tally.files_by_glob += 1
                continue
            yield p, rel


# Streaming-read tuning (020/380, reusing secretscan's 020/370 constants
# verbatim rather than re-deriving them — every FIXED size here is chosen
# once and independent of the file or tree being scanned, which is the
# entire fix). See `secretscan.py`'s module comment above its own copy of
# these for the full derivation.
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
    for a file that looks binary (checked on the first chunk only).

    This replaces the old `read_bytes()` → whole `str` → `splitlines()`
    list, which held the file THREE TIMES OVER at once (measured, see
    020/380's board item and 020/370's own precedent in secretscan).

    `is_final_window` is False for every window of an overlong line except
    its last — `_scan_file` uses it to dedupe a match that straddles a
    window boundary and would otherwise be reported twice."""
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
                yield lineno, pending, False
                pending = pending[-LINE_WINDOW_OVERLAP:]
        pending += decoder.decode(b"", final=True)
        if pending:
            yield lineno, pending, True  # EOF: whatever remains is the last line


def _scan_file(path: Path, rel: str,
               local_terms: list[tuple[str, "re.Pattern[str]"]],
               disabled: frozenset[str], tally: Tally | None) -> list[Finding]:
    """Scan one file with memory bounded by a fixed constant regardless of
    the file's size (020/380) — see `_iter_numbered_lines`. Ordinary lines
    go through `scan_lines` one at a time, identically to the pre-fix
    whole-file call (each physical line was already scoped independently by
    line number). An overlong line's windows share `LINE_WINDOW_OVERLAP`
    characters of real content between consecutive windows, so a token
    sitting in that shared region would otherwise be found — and reported —
    twice; `seen_in_window` dedupes by (rule, excerpt) across one line's
    windows, reset the moment `is_final_window` says that line is done —
    identical shape to `secretscan._scan_file` (020/370)."""
    findings: list[Finding] = []
    seen_in_window: set[tuple[str, str]] = set()
    in_overlong = False
    try:
        for lineno, text, is_final in _iter_numbered_lines(path):
            unit = scan_lines(rel, [(lineno, text)], local_terms, disabled, tally)
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
               local_terms: list[tuple[str, "re.Pattern[str]"]],
               disabled: frozenset[str] = frozenset(),
               tally: Tally | None = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    manifest = load_binary_manifest(root)
    tracked = tracked_files(root)
    by_digest = _digest_index(manifest)
    findings: list[Finding] = []
    gated: set[str] = set()
    for p, rel in iter_files(paths, root, globs, tally):
        # G2: the path is scanned whatever the contents turn out to be — a
        # binary's NAME is readable even when its body is not.
        findings.extend(scan_path_name(rel, local_terms, disabled, tally))
        if not _looks_binary_file(p):
            findings.extend(_scan_file(p, rel, local_terms, disabled, tally))
        elif tracked is not None and rel not in tracked:
            if tally is not None:
                tally.binaries_untracked += 1
        else:
            gated.add(rel)
            findings.extend(check_binary(p, rel, manifest.get(rel), local_terms,
                                         disabled, tally, by_digest))
    # An entry this walk could have reached but did not gate accepts nothing.
    for entry in manifest.values():
        if entry.path in gated or _ignored(entry.path, globs) \
                or not _under_any(root / entry.path, paths):
            continue
        _record(findings, tally, _stale(entry, _stale_reason(root / entry.path,
                                                             entry.path, tracked)))
    return findings


def _under_any(target: Path, bases: list[Path]) -> bool:
    t = target.resolve()
    for base in bases:
        b = base.resolve()
        if t == b:
            return True
        try:
            t.relative_to(b)
        except ValueError:
            continue
        if b.is_dir():
            return True
    return False


def _stale_reason(p: Path, rel: str, tracked: set[str] | None) -> str:
    if not p.is_file():
        return "no such file"
    if tracked is not None and rel not in tracked:
        return "not tracked by git"
    if not _looks_binary_file(p):
        return "read as text, so it is scanned and the entry accepts nothing"
    return "in a directory the scan never walks"


def binary_entries(paths: list[Path], root: Path) -> tuple[list[str], list[str]]:
    """`--binary-entries`: a `.leakscanbinaries` line for every gated binary
    no entry accepts yet (new, or changed since it was listed), plus notes
    for the human. Lines carry NO reason on purpose — the loader refuses an
    entry without one, so the re-baseline cannot complete until a person has
    written why each file may stand. Never writes the file."""
    globs = load_ignore_globs(root)
    manifest = load_binary_manifest(root)
    tracked = tracked_files(root)
    lines: list[str] = []
    notes: list[str] = []
    for p, rel in iter_files(paths, root, globs):
        if not _looks_binary_file(p) or (tracked is not None and rel not in tracked):
            continue
        with open(p, "rb") as fh:
            digest = _sha256_file(fh)
            _fmt, _texts, opaque = inspect_media(fh)
        entry = manifest.get(rel)
        if entry is not None and entry.matches(digest):
            continue
        if "#" in rel or "\n" in rel or rel != rel.strip() or rel.startswith("*"):
            notes.append(f"{rel!r}: this path cannot be written as an entry "
                         "(it holds '#', a newline, edge whitespace or a leading "
                         "'*') — rename the file")
            continue
        lines.append(f"{digest[:PRINTED_DIGEST_HEX]}  {rel}")
        if entry is not None:
            notes.append(f"{rel}: changed since listed — replaces line {entry.lineno}")
        if opaque:
            notes.append(f"{rel}: carries opaque metadata ({'; '.join(opaque)}) — "
                         f"strip it, or append ':{SCOPE_METADATA}' to the digest "
                         "once you have checked what it holds")
    return lines, notes


def staged_added_lines() -> dict[str, str]:
    """Map path → the added-line text of the staged diff. Scans only what a
    commit would introduce (the pre-commit hot path), not the whole tree.
    R is in the filter deliberately (review B4): git detects renames by
    default, and a renamed-AND-edited file's added lines are exactly as
    leak-capable as a modified file's — ACM alone silently skipped them."""
    out = subprocess.run(
        ["git", "diff", "--cached", "--unified=0", "--no-color",
         "--diff-filter=ACMR"],
        capture_output=True, text=True, check=True).stdout
    files: dict[str, list[str]] = {}
    current: str | None = None
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            current = line[len("+++ b/"):]
            files.setdefault(current, [])
        elif line.startswith("+") and not line.startswith("+++") and current:
            files[current].append(line[1:])
    return {path: "\n".join(lines) for path, lines in files.items() if lines}


def staged_changes() -> tuple[list[str], set[str], list[str]]:
    """G3 on the hot path: `(every path the commit adds, modifies or renames
    to; the subset git reads as binary; every path the commit removes —
    deletions and rename sources)`.

    The added-lines diff above never names a binary (git prints "Binary files
    … differ" and no `+++` line), so before G3 a staged binary's NAME was not
    scanned either — and neither was an empty new file's, or a pure rename's.
    Every changed path now gets the path-name scan. `--no-textconv` keeps a
    repo's textconv driver from turning an image into text lines here, so
    git's binary verdict is about the bytes."""
    def paths(*extra: str) -> list[bytes]:
        return subprocess.run(["git", "diff", "--cached", "-z", *extra],
                              capture_output=True, check=True).stdout.split(b"\0")

    def dec(b: bytes) -> str:
        return b.decode("utf-8", errors="surrogateescape")

    changed: list[str] = []
    removed: list[str] = []
    toks = paths("--name-status", "--diff-filter=ACMRD")
    i = 0
    while i < len(toks):
        status = dec(toks[i])
        if not status:
            i += 1
            continue
        if status[0] in "RC":
            src, dst = dec(toks[i + 1]), dec(toks[i + 2])
            changed.append(dst)
            if status[0] == "R":
                removed.append(src)
            i += 3
        else:
            (removed if status[0] == "D" else changed).append(dec(toks[i + 1]))
            i += 2
    binary: set[str] = set()
    toks = paths("--numstat", "--no-textconv", "--diff-filter=ACMR")
    i = 0
    while i < len(toks):
        if not toks[i]:
            i += 1
            continue
        added, deleted, rest = toks[i].split(b"\t", 2)
        if rest:
            path, i = dec(rest), i + 1
        else:  # rename/copy: the source and destination follow as tokens
            path, i = dec(toks[i + 2]), i + 3
        if added == b"-" and deleted == b"-":
            binary.add(path)
    return changed, binary, removed


def _staged_blob(path: str, dest: Path) -> None:
    """Write the INDEX copy of `path` (what the commit will hold, not the
    working tree's) to `dest`, streamed by git rather than held in memory."""
    with open(dest, "wb") as fh:
        subprocess.run(["git", "cat-file", "blob", f":0:{path}"], stdout=fh, check=True)


class TermsPathError(RuntimeError):
    """An explicitly set terms path that does not resolve.

    Falling through to the default list would silently narrow cover on
    exactly the plane EP3 hardened against silent degradation — a mistyped
    dedicated-list path must be an error, not a quieter scan (AP4, the
    principal's ruling 2026-08-23)."""


def resolve_terms_path(cli: str | None) -> Path | None:
    # The CLI flag and the env var are EXPLICIT settings: if one is given and
    # does not resolve, that is an error, never a fall-through. Only the
    # default location may be quietly absent.
    for candidate, source in ((cli, "--terms"),
                              (os.environ.get("ATELIER_LEAKSCAN_TERMS"),
                               "$ATELIER_LEAKSCAN_TERMS")):
        if candidate:
            p = Path(candidate).expanduser()
            if not p.exists():
                raise TermsPathError(
                    f"{source} points at {candidate}, which does not exist — "
                    "refusing to fall back to a narrower default list")
            return p
    p = Path(DEFAULT_LOCAL_TERMS).expanduser()
    return p if p.exists() else None


def render_human(findings: list[Finding], warning: str | None,
                 scanned_local: bool, tally: Tally | None = None) -> str:
    # 020/380 — a capped run's TRUE total lives on the tally, never on
    # `len(findings)`: everything past `MAX_MATERIALIZED_FINDINGS` was
    # counted there instead of being built as a `Finding` at all (see
    # `Tally.take_finding_slot`), so reading the list length alone would
    # silently under-report the exit-code-relevant count on exactly the
    # runs this cap exists for.
    over_cap = tally.findings_over_cap if tally is not None else 0
    lines: list[str] = []
    if warning:
        lines.append(f"⚠ {warning}")
    if not findings and not over_cap:
        cover = "structural + local" if scanned_local else "structural only"
        lines.append(f"✓ leakscan clean ({cover}).")
        if tally is not None:
            lines.append(tally.summary())
        return "\n".join(lines)
    lines.append(f"✗ leakscan: {len(findings) + over_cap} finding(s) — commit blocked.\n")
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        # Line 0 means the hit is in the PATH itself (G2) — say so, because
        # ':0' would otherwise read as a line number nobody can open.
        if f.where:
            where = f"{f.path} ({f.where}" + (f", line {f.line})" if f.line else ")")
        elif f.line:
            where = f"{f.path}:{f.line}"
        else:
            where = f"{f.path} (in the path name)"
        lines.append(f"  {where}  [{f.severity}/{f.kind}] {f.rule} → {f.excerpt}")
    if over_cap:
        lines.append(f"  …and {over_cap} more finding(s), counted but not listed "
                     f"(past the {MAX_MATERIALIZED_FINDINGS}-finding memory cap).")
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append("\n  A true positive: remove the data (and rotate if it's a secret).")
    lines.append(f"  A false positive: append '# {ALLOW_MARKER}: <reason>' to the line")
    lines.append(f"  (or '# {ALLOW_MARKER}:<rule>: <reason>' to exempt just one rule —")
    lines.append("  the narrowest allowance that covers the case), or add a path glob")
    lines.append("  to .leakscanignore. A marker with no reason exempts nothing.")
    if any(f.kind == "binary" for f in findings):
        lines.append(f"  A binary (G3): look at it, then list it in {BINARY_MANIFEST} with a")
        lines.append("  reason — `leakscan --binary-entries` prints the lines, hash-bound, so a")
        lines.append("  changed file blocks again. Opaque metadata: strip it, or scope the entry")
        lines.append(f"  ':{SCOPE_METADATA}' once checked. A stale entry: delete or re-path it.")
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="leakscan",
        description="Scan for personal/estate data before it reaches a shareable repo.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo, or --staged)")
    ap.add_argument("--staged", action="store_true",
                    help="scan only lines added in the git staging area (pre-commit hook)")
    ap.add_argument("--terms", help="path to the local literal-term list")
    ap.add_argument("--require-terms", action="store_true",
                    help="fail (exit 2) if no local term list is found, instead of "
                         "degrading to structural-only. For hooks/CI on a machine "
                         "that is EXPECTED to have full cover — review B5: to "
                         "automation, a degraded exit-0 pass is indistinguishable "
                         "from a full one.")
    ap.add_argument("--root", default=".", help="repo root for relative paths/.leakscanignore")
    ap.add_argument("--disable", default="",
                    help="comma-separated structural rules to skip (e.g. "
                         "ipv4,ipv6,mac-address for a networking repo where those "
                         "shapes are unavoidable noise). Local terms always run.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--binary-entries", action="store_true",
                    help=f"print a {BINARY_MANIFEST} line for every tracked binary no "
                         "entry accepts yet (new, or changed since listed) and exit 0. "
                         "Lines carry no reason: review each file and write one, or "
                         "the scan refuses the entry. Never writes the file.")
    ap.add_argument("--selftest", action="store_true", help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if args.binary_entries:
        if args.staged or args.json:
            print("leakscan: --binary-entries lists the whole tree as plain lines; it "
                  "takes neither --staged nor --json", file=sys.stderr)
            return 2
        targets = [(root / p) if not Path(p).is_absolute() else Path(p)
                   for p in (args.paths or [str(root)])]
        missing = [str(p) for p in targets if not p.exists()]
        if missing:
            print(f"leakscan: path does not exist: {', '.join(missing)}", file=sys.stderr)
            return 2
        lines, notes = binary_entries(targets, root)
        for line in lines:
            print(line)
        for note in notes:
            print(f"leakscan: {note}", file=sys.stderr)
        print(f"leakscan: {len(lines)} entr{'y' if len(lines) == 1 else 'ies'} to review. "
              f"Append to {BINARY_MANIFEST} with a reason — a '# reason' comment above "
              "the stanza or on the line — saying what each file is and that you looked.",
              file=sys.stderr)
        return 0
    try:
        terms_path = resolve_terms_path(args.terms)
    except TermsPathError as e:
        print(f"leakscan: {e}", file=sys.stderr)
        return 2
    if args.require_terms and terms_path is None:
        print("leakscan: --require-terms set but no local term list found "
              f"(--terms, $ATELIER_LEAKSCAN_TERMS, or {DEFAULT_LOCAL_TERMS}). "
              "A structural-only scan is partial cover — refusing to report it "
              "as a pass.", file=sys.stderr)
        return 2
    local_terms, warning = load_local_terms(terms_path)
    scanned_local = terms_path is not None

    disabled = frozenset(r.strip() for r in args.disable.split(",") if r.strip())
    unknown = disabled - {p.name for p in STRUCTURAL}
    if unknown:
        print(f"leakscan: unknown rule(s) in --disable: {', '.join(sorted(unknown))}",
              file=sys.stderr)
        return 2
    # A scope reduction taken at invocation is itself an allowance, and rule (b)
    # says a reduction nobody can see is a reduction nobody reviewed — so
    # `--disable` now reports itself in the output instead of narrowing the scan
    # silently from a flag nobody reading the result will ever see.
    tally = Tally(disabled_rules=tuple(sorted(disabled)))

    if args.staged:
        try:
            staged = staged_added_lines()
            changed, binary, removed = staged_changes()
        except subprocess.CalledProcessError as e:
            print(f"leakscan: git diff failed: {e}", file=sys.stderr)
            return 2
        # Positional paths, in --staged mode, restrict the scan to staged files
        # under those prefixes — e.g. scan only the shareable `tiki/` subtree of
        # an otherwise-private repo.
        # An ABSOLUTE path here scans NOTHING and exits 0 — the silent-success
        # class (linkscan L1) already closed for a missing path, found again on
        # 2026-07-25 while building tools/floor.py. git lists staged paths
        # repo-relative, so an absolute one matches no prefix, the filter empties
        # the set, and a boundary scan covering nothing looks exactly like one
        # that found nothing wrong. Refuse it — this is the subtree-scoping
        # entry point for private repos with a shareable subtree, so a silent
        # miss here is precisely the case that matters.
        absolute = [p for p in args.paths if Path(p).is_absolute()]
        if absolute:
            print(f"leakscan: --staged needs repo-relative path(s), got absolute: "
                  f"{', '.join(absolute)}\n"
                  "  git lists staged paths relative to the repo root, so an "
                  "absolute path matches nothing\n"
                  "  and the scan would pass while covering nothing. Pass e.g. "
                  "'tiki/' instead.", file=sys.stderr)
            return 2
        prefixes = tuple(p.rstrip("/") + "/" for p in args.paths)

        def in_scope(path: str) -> bool:
            return not prefixes or path.startswith(prefixes) or path in args.paths

        staged = {path: text for path, text in staged.items() if in_scope(path)}
        # .leakscanignore applies in staged mode too, so an exemption means the
        # same thing whether you scan the tree or a commit.
        globs = load_ignore_globs(root)
        manifest = load_binary_manifest(root)
        by_digest = _digest_index(manifest)
        findings = []
        # Every changed path once, in a stable order: the text diff's files
        # first (their existing order), then the paths only git's name list
        # carries — binaries, empty new files, pure renames.
        ordered = list(staged) + [p for p in changed if p not in staged and in_scope(p)]
        with tempfile.TemporaryDirectory(prefix="leakscan-") as td:
            blob = Path(td) / "blob"
            for path in ordered:
                if _ignored(path, globs):
                    tally.files_by_glob += 1
                    continue
                # G2 on the hot path too: a leak in a NEW file's name reaches
                # the remote by the same commit as one in its body.
                findings.extend(scan_path_name(path, local_terms, disabled, tally))
                if path in staged:
                    findings.extend(scan_text(path, staged[path], local_terms, disabled, tally))
                if path not in binary:
                    continue
                try:
                    _staged_blob(path, blob)
                except subprocess.CalledProcessError as e:
                    print(f"leakscan: git cat-file failed for {path}: {e}", file=sys.stderr)
                    return 2
                if _looks_binary_file(blob):
                    findings.extend(check_binary(blob, path, manifest.get(path),
                                                 local_terms, disabled, tally, by_digest))
                else:
                    # git calls it binary (a `binary`/`-diff` attribute) but the
                    # bytes are text: the diff showed no lines, so read the
                    # whole staged copy rather than let the attribute hide it.
                    findings.extend(_scan_file(blob, path, local_terms, disabled, tally))
        for path in removed:
            entry = manifest.get(path)
            if entry is not None and in_scope(path) and not _ignored(path, globs):
                _record(findings, tally, _stale(entry, "removed or renamed by this commit"))
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
            print(f"leakscan: path does not exist: {', '.join(missing)}",
                  file=sys.stderr)
            return 2
        findings = scan_paths(targets, root, local_terms, disabled, tally)

    if args.json:
        print(json.dumps({
            "clean": not findings and not tally.findings_over_cap,
            "scanned_local_terms": scanned_local,
            "warning": warning,
            "findings": [asdict(f) for f in findings],
            "findings_over_cap": tally.findings_over_cap,
            "suppressed": {
                "by_allow_marker": tally.marker_total,
                "by_allow_marker_rule": tally.by_marker,
                "files_by_ignore_glob": tally.files_by_glob,
                "disabled_rules": list(tally.disabled_rules),
                "binaries_by_manifest": tally.binaries_by_manifest,
                "binaries_untracked_not_gated": tally.binaries_untracked,
            },
        }, indent=2))
    else:
        print(render_human(findings, warning, scanned_local, tally))

    return 1 if (findings or tally.findings_over_cap) else 0


def _selftest() -> int:
    """Minimal smoke test so `leakscan --selftest` proves the engine on any box,
    even where the unittest file isn't shipped."""
    cases = [  # fictional fixtures; the shapes here are the point of the test
        ("contact me at jane.doe@example.com", "email", True),      # leakscan:allow: selftest fixture
        ("gateway 172.16.31.7 is the igw", "ipv4", True),           # leakscan:allow: selftest fixture
        ("example host 192.0.2.10 in docs", None, False),      # TEST-NET is safe
        ("mac aa:bb:cc:dd:ee:ff", "mac-address", True),            # leakscan:allow: selftest fixture
        ("version 1.2.3 released", None, False),              # semver, not an IP
        ("secret@host.com  # leakscan:allow: doc example", None, False),
        ("uplink fd00:1234:5678::abcd", "ipv6", True),              # leakscan:allow: selftest fixture
        ("ran 03:04:05 to 03:04:09", None, False),            # D2: clock times
        ("netmask 255.255.255.0 applies", None, False),       # D3: not topology
        ("dob = 1984-02-29", "pii-key-context", True),              # leakscan:allow: selftest fixture
        ("passport_number: <redacted>", None, False),         # G1 placeholder
        ("card 4111111111111111 on file", "payment-card", True),    # leakscan:allow: selftest fixture
    ]
    ok = True
    for text, expect_rule, expect_hit in cases:
        fs = scan_text("t", text, [])
        hit = bool(fs)
        if hit != expect_hit:
            print(f"FAIL: {text!r} expected hit={expect_hit} got {hit}")
            ok = False
        elif expect_rule and not any(f.rule == expect_rule for f in fs):
            print(f"FAIL: {text!r} expected rule {expect_rule}, got {[f.rule for f in fs]}")
            ok = False
    # G3: the metadata walker on two synthetic PNGs — opaque Exif is seen,
    # and text metadata is read as text (a fictional address, so it hits).
    import io

    def png(ctype: bytes, data: bytes) -> io.BytesIO:
        def chunk(t: bytes, d: bytes) -> bytes:
            return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d))
        return io.BytesIO(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", bytes(13))
                          + chunk(ctype, data) + chunk(b"IEND", b""))
    _f, _t, opaque = inspect_media(png(b"eXIf", b"MM\x00\x2a"))
    if not opaque:
        print("FAIL: PNG eXIf chunk not reported as opaque metadata")
        ok = False
    _f, texts, _o = inspect_media(png(b"tEXt", b"Author\x00jane.doe@example.com"))  # leakscan:allow: selftest fixture
    if not any(f.rule == "email" for _l, t in texts for f in scan_text("t", t, [])):
        print("FAIL: PNG tEXt metadata not scanned as text")
        ok = False
    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1



def main(argv: list[str] | None = None) -> int:
    """Exit 2 on an ignore file or a binary manifest that grants an exemption
    with no reason, or a manifest that does not parse.

    A broken scan is not a pass (the house exit-code contract), and an
    unexplained exemption makes the scan's own scope untrustworthy."""
    try:
        return _main(argv)
    except (IgnoreFileError, BinaryManifestError) as e:
        print(f"leakscan: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
