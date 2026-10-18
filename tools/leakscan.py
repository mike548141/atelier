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
bytes; PNG/JPEG/WebP metadata is walked, text metadata scanned, and every
named metadata set it carries (Exif, IPTC, XMP, ICC, text chunks, comments)
blocking until a reasoned line keeps that set. Until `BINARY_GRACE_UNTIL`
(2026-11-18) these G3 findings warn and do not block — the one, dated
exception to "no advisory form". See the G3 block below and the leakscan
section of `tools/README.md`.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean (G3 grace warnings, before the cut-off, do not change this)
  1  findings (blocks the commit)
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can run
it with the system python3 and no install.
"""

from __future__ import annotations

import argparse
import codecs
import datetime
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
import report  # noqa: E402

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
    # The G3 adoption grace (see `BINARY_GRACE_UNTIL`): gate findings printed
    # as warnings, not counted in the exit code. Always 0 from the cut-off on.
    binary_grace_warnings: int = 0
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
                 f"{self.binary_grace_warnings} G3 finding(s) warned, not blocking, "
                 f"before {BINARY_GRACE_UNTIL.isoformat()}",
                 report.cap_part(self.findings_over_cap, MAX_MATERIALIZED_FINDINGS)]
        return report.suppressed_line(parts, breakdown=self.by_marker,
                                      disabled=self.disabled_rules)


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


# --- per-rule pre-filters (roadmap 110/130, lever 4) ---------------------
#
# Each gate is a CHEAP test on the line that is NECESSARY for its rule to match:
# if the gate says no, the rule's regex provably has no match on that line, so
# skipping `finditer` changes nothing — same findings, same order, same counts.
# That is the only property a gate may have. A gate that could reject a line the
# rule would match is a silent false negative in a boundary scanner, the worst
# failure this tool has, so every gate below states WHY it is necessary and is
# derived from the rule's own pattern text, never from a guess about the data.
# A rule with no entry here has no provable cheap necessary condition and
# always runs its full regex (fail open). `test_leakscan.GatesAreNecessary`
# pins each gate against its rule on matching and near-miss lines.
#
# NOT BUILT, and why: lever 3 of 110/130, one combined alternation pass over
# every rule. Rules here overlap on the same span (a MAC is also a valid IPv6;
# an email and a JWT can share characters) and each reports its own finding,
# in rule order, with its own validator. One alternation takes the leftmost
# match per position and reports a single rule, so it cannot reproduce that
# output byte for byte. Gates are the form of the idea that is exact.
#
# Counting gates (`count(x) >= n`) rest on one fact: a match whose pattern
# needs n separator characters contains at least n of them, and `str.count` /
# `in` are single C passes that allocate nothing.
_DIGITS4_RX = re.compile(r"\d{4}")                     # payment-card
_PHONE_TAIL_RX = re.compile(r"\d{3}[\s-]?\d{3}")       # nz-phone
# nz-address: every alternative ends in one of these suffix words.
_ADDRESS_SUFFIX_RX = re.compile(
    r"Street|Road|Avenue|Lane|Drive|Terrace|Crescent"
    r"|St|Rd|Ave|Ln|Dr|Pl|Tce|Cres|Place|Way|Close|Grove|Hill|Green")
# pii-key-context: the pattern's fixed tail is
# `\b\s*[:=]\s*["']?<2+ value chars>`. This is the part from the `[:=]` on —
# necessary whatever key vocabulary is added to PII_KEY_RX later, because it
# names no key. (The `[:=]` first means the regex engine only wakes at a colon
# or equals sign, not at every word.)
_PII_TAIL_RX = re.compile(r"""[:=]\s*["']?[^\s"'`,;:]{2}""")

GATES: dict[str, "object"] = {
    # `-----BEGIN [..] PRIVATE KEY-----` ends in this literal.
    "private-key-header": lambda ln: "PRIVATE KEY-----" in ln,
    "aws-access-key-id": lambda ln: "AKIA" in ln,
    # `eyJ…\.eyJ…` — the second segment's lead-in.
    "jwt": lambda ln: ".eyJ" in ln,
    "email": lambda ln: "@" in ln,
    "pii-key-context": lambda ln: _PII_TAIL_RX.search(ln) is not None,
    # 13-19 digits or `\d{4}` groups: either way four digits in a row.
    "payment-card": lambda ln: _DIGITS4_RX.search(ln) is not None,
    # `[A-Z]{2}\d{2}[A-Z0-9]{11,30}` is at least 15 characters long.
    "iban": lambda ln: len(ln) >= 15,
    # `(?:xx[:-]){5}xx` — five separators.
    "mac-address": lambda ln: ln.count(":") + ln.count("-") >= 5,
    "ipv4": lambda ln: ln.count(".") >= 3,
    # every alternative carries at least two colons (`h::h`, `h:h::`, `::h:h`).
    "ipv6": lambda ln: ln.count(":") >= 2,
    "nz-bank-account": lambda ln: ln.count("-") >= 3,
    "nz-phone": lambda ln: _PHONE_TAIL_RX.search(ln) is not None,
    "nz-address": lambda ln: _ADDRESS_SUFFIX_RX.search(ln) is not None,
    "coordinates": lambda ln: "," in ln and ln.count(".") >= 2,
    "nz-ird": lambda ln: ln.count("-") >= 2,
}
# One entry per rule, in STRUCTURAL's order: (pattern, gate-or-None).
_GATED: tuple[tuple[Pattern, "object"], ...] = tuple(
    (p, GATES.get(p.name)) for p in STRUCTURAL)
_ACTIVE_CACHE: dict[frozenset[str], tuple] = {}


def _active_rules(disabled: frozenset[str]) -> tuple:
    """`_GATED` minus the disabled rules, memoised per disabled-set so the
    per-line loop does not re-test every name against it."""
    if not isinstance(disabled, frozenset):   # a plain set worked before
        disabled = frozenset(disabled)
    got = _ACTIVE_CACHE.get(disabled)
    if got is None:
        got = _ACTIVE_CACHE[disabled] = tuple(
            (p, g) for p, g in _GATED if p.name not in disabled)
    return got


def _shadow_spans(line: str, disabled: frozenset[str]) -> dict[str, list[tuple[int, int]]]:
    """D5 — per shadowed rule, the spans another rule has already claimed."""
    out: dict[str, list[tuple[int, int]]] = {}
    for shadowed, shadowers in SHADOWED_BY.items():
        if shadowed in disabled:
            continue
        # 110/130: a shadow only ever suppresses a match of the SHADOWED rule,
        # and a shadower casts a span only where its own regex matches — so if
        # the shadowed rule's gate fails there is nothing to suppress, and if a
        # shadower's gate fails it has no span. Gates are necessary conditions
        # (see GATES), so no span that could have mattered is lost.
        gate = GATES.get(shadowed)
        if gate is not None and not gate(line):
            continue
        spans = [m.span()
                 for name in shadowers if name not in disabled
                 if GATES.get(name) is None or GATES[name](line)
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
    physical line while streaming a file, and the staged plane, whose added
    lines are not consecutive lines of the file (115/300). `scan_text` below
    is the whole-blob convenience wrapper the path-name scan, the image
    metadata reader and the test suite use.

    `honour_markers=False` (G3, image metadata) reads an allow-marker as
    plain text: a marker inside a binary's metadata sits where no reviewer
    reads it, which `method/GUARDS.md` § *Who, why, when* forbids."""
    findings: list[Finding] = []
    rules = _active_rules(disabled)
    for lineno, line in numbered_lines:
        # The marker regex opens with the literal marker text, so a line
        # without it cannot carry a marker (110/130, lever 4).
        allow_scope = (parse_allow(line)
                       if honour_markers and ALLOW_MARKER in line else None)
        shadows = _shadow_spans(line, disabled)
        for pat, gate in rules:
            if gate is not None and not gate(line):
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
    path-name caller's shape (it holds a single path string in memory). The
    staged plane does not use this: its lines carry real file line numbers
    and go to `scan_lines` (115/300)."""
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
# (E6a), with ONE dated exception, the adoption grace below. This is the build
# of that ruling:
#
#   * THE MARKER is an entry in `.leakscanbinaries` at the scan root —
#     `<sha256 hex, ≥16 chars>  <path>` accepts the file, and
#     `<same digest>:<set>  <path>` keeps ONE named metadata set — each line
#     reasoned with the SAME grammar as `.leakscanignore`
#     (`allowmarker.read_reasoned_lines`: a trailing `# reason` or a comment
#     stanza). A binary cannot hold an inline marker, and a `.leakscanignore`
#     glob is the wrong hatch: it is path-wide, rule-wide and blind to
#     content, so a REPLACED image would pass under the old acceptance. The
#     digest is what makes "one-time" true — a changed binary no longer
#     matches its entry and blocks again, and the human who re-lists it is
#     looking at the new bytes.
#   * THE DIGEST is a hex PREFIX of SHA-256, at least 16 characters (64
#     bits). Full 64 also parses. The printed form is 16 because secretscan's
#     context-free entropy net reports every 32+ character run as an advisory
#     finding; a manifest of full digests would buy one advisory per binary on
#     every scan for no gain: the threat is an unnoticed change, not a forged
#     64-bit second preimage by someone who can edit the manifest anyway.
#   * METADATA is walked, not guessed, for the three web image formats
#     (PNG, JPEG, WebP), stdlib only, every read bounded, and sorted into the
#     NAMED SETS of `METADATA_SETS` — the sets the walker can tell apart.
#     Mike, 2026-10-18, on 020/150: "that reason for the image metadata must
#     be specific to the sets of metadata it wants to keep. It should only
#     keep the metadata it has a need for". And, 2026-10-19, on 020/440: "I
#     am fine with one reason applying to multiple fields of metadata, but it
#     should be specific e.g. fields A, B, and C allowed because of X". So a
#     set line names each set it keeps explicitly — one (`:icc`) or several
#     (`:icc,xmp`) — under one reason, the need for exactly those sets; there
#     is no wildcard, and every set present in the file that no line names
#     blocks as `binary-metadata`, naming the set.
#     Accepting the pixels never accepts a GPS block, and keeping a colour
#     profile never keeps the Exif beside it. TEXT sets (PNG text chunks, XMP,
#     JPEG comments) are ALSO decoded and run through the ordinary rule set
#     and term list whether or not a line keeps them — naming a set states a
#     need, it does not stop the scan — with allow-markers NOT honoured inside
#     them. A set line for a set these bytes do not carry is stale (below):
#     the digest binds the bytes, so it was wrong when it was written, and a
#     line per set "just in case" is the blanket acceptance the answer
#     forbids.
#
# What it cannot see, stated so nobody infers cover that is not there: the
# pixels themselves (no OCR — the entry's reason is the human attesting to
# them); metadata in any other format (GIF, TIFF, HEIC/AVIF, PDF, Office
# documents, fonts, archives — for these the file line accepts the whole
# file, metadata included); JPEG segments after the first start-of-scan, and
# JPEG APPn segments other than APP1, APP2 (ICC) and APP13; the CONTENT of an
# ICC profile, Exif or IPTC block (named by presence, never read); bytes
# appended after a format's end marker.
#
# THE GATE COVERS TRACKED BINARIES (the ruling's word). A full-tree scan of a
# git work tree gates the files `git ls-files` lists and counts the rest
# (`.DS_Store`, build output) as "not gated"; a scan of a directory that is
# not a git work tree gates every binary, failing closed. The staged plane
# gates every binary the commit adds, modifies or renames.
BINARY_MANIFEST = ".leakscanbinaries"
BINARY_RULES = ("binary-unlisted", "binary-changed", "binary-metadata",
                "binary-stale-entry")
# The named metadata sets, in report order. The keys are the manifest's
# spelling; each is a set the walkers below can tell apart in the bytes.
METADATA_SETS = {
    "exif": "Exif (camera, time, place): PNG eXIf, JPEG APP1 Exif, WebP EXIF, "
            "ImageMagick raw exif profile",
    "iptc": "IPTC / Photoshop resources: JPEG APP13, ImageMagick raw iptc/8bim "
            "profile",
    "xmp": "XMP packet: JPEG APP1 (and extended), WebP XMP, PNG "
           "XML:com.adobe.xmp, ImageMagick raw xmp profile",
    "icc": "ICC colour profile: PNG iCCP, JPEG APP2 ICC_PROFILE, WebP ICCP",
    "png-text": "PNG tEXt/zTXt/iTXt text chunks (other than XMP)",
    "jpeg-comment": "JPEG COM comment segments",
    "unknown": "metadata or structure the walker cannot identify or read: an "
               "unrecognised APP1, a segment past the cap or undecodable, a "
               "structure that cannot be walked",
}
MIN_DIGEST_HEX = 16
PRINTED_DIGEST_HEX = 16
META_SEGMENT_CAP = 1 * 1024 * 1024   # bytes of ONE metadata segment read or
                                     # inflated; past it the segment is opaque
_ENTRY_RX = re.compile(r"^(?P<digest>[0-9A-Fa-f]{%d,64})(?::(?P<scope>[A-Za-z0-9_,-]+))?"
                       r"[ \t]+\*?(?P<path>\S.*)$" % MIN_DIGEST_HEX)

# THE ADOPTION GRACE — the one exception to E6a, and dated.
#
# E6a: leakscan has no advisory form; every finding blocks. Mike's answer on
# 020/150, 2026-10-18, chose to land G3 with a grace period: "unlisted files
# print a warning naming a cut-off date (~30 days), then start blocking. No
# child goes red today; each lists its files when convenient." That answer is
# the authority for this exception, and it is the ONLY one: it covers the
# four G3 gate rules (`BINARY_RULES`) and nothing else. Every other leakscan
# rule, including a hit in an image's TEXT metadata, blocks as before.
#
# The exact date is the queue-run orchestrator's choice on that "~30 days"
# answer (31 days after the answer was given), NOT a ruling. Before it, a G3 finding
# prints as a warning naming the date and the remedy and does not fail the
# exit code; ON and after it, the finding blocks exactly as built. It is
# unreachable after the date by construction: the cut-off lives in this one
# constant and is compared with the UTC clock, and there is no flag, env var
# or config key that moves it. A child's floor overrides cannot reach it
# (floor.py refuses an abbreviated mode flag, and `--disable` refuses a
# binary rule as unknown). The grace is not an advisory FORM in floor.py's
# registry either: leakscan's `advisory` stays None, so it still "cannot be
# softened". Delete this block, `in_binary_grace` and its callers once the
# date has passed.
BINARY_GRACE_UNTIL = datetime.date(2026, 11, 18)


def _utc_today() -> datetime.date:
    return datetime.datetime.now(datetime.timezone.utc).date()


def in_binary_grace(today: datetime.date | None = None) -> bool:
    """True strictly before `BINARY_GRACE_UNTIL` (UTC). Tests patch
    `_utc_today`; nothing a caller can pass at the command line reaches it."""
    return (today or _utc_today()) < BINARY_GRACE_UNTIL


def _grace_remedy(rule: str) -> str:
    if rule == "binary-stale-entry":
        return "delete or re-path the line"
    if rule == "binary-metadata":
        return ("strip the set, or run `leakscan --binary-entries` and write the "
                "need for keeping it")
    return "run `leakscan --binary-entries`, look at the file, write a reason"


class BinaryManifestError(ValueError):
    """`.leakscanbinaries` is malformed, or grants an acceptance with no
    reason. A config error (exit 2), never a warning: a broken scan is not a
    pass."""


@dataclass(frozen=True)
class KeptSet:
    """One `<digest>:<set>  <path>` line: a metadata set kept, and why."""
    name: str
    reason: str
    lineno: int


@dataclass(frozen=True)
class BinaryEntry:
    path: str
    digest: str               # lower-case hex prefix of the file's SHA-256
    reason: str
    lineno: int
    sets: dict = field(default_factory=dict, compare=False)   # name -> KeptSet

    def matches(self, sha256_hex: str) -> bool:
        return sha256_hex.startswith(self.digest)


def _same_digest(a: str, b: str) -> bool:
    return a.startswith(b) or b.startswith(a)


def load_binary_manifest(root: Path) -> dict[str, BinaryEntry]:
    """Entries from `<root>/.leakscanbinaries`, keyed by repo-relative path.
    Every problem is collected and raised together as `BinaryManifestError`:
    an unreasoned line, a malformed line, an unknown or comma-joined set, a
    path or a set listed twice, a set line with no file line for its path or
    with a different digest. An absent file is no entries."""
    files: dict[str, tuple[str, str, int]] = {}
    set_lines: list[tuple[int, str, str, str, str]] = []
    problems: list[str] = []
    for n, body, reason in allowmarker.read_reasoned_lines(root / BINARY_MANIFEST):
        m = _ENTRY_RX.match(body)
        if not m:
            problems.append(f"line {n}: not '<sha256 hex, ≥{MIN_DIGEST_HEX} chars>"
                            f"[:<metadata set>]  <path>'")
            continue
        scope = m.group("scope")
        # A set line names its sets explicitly: one, or several under one
        # reason (Mike, 2026-10-19, 020/440: "fields A, B, and C allowed
        # because of X"). Each must be a real set, named once; there is no
        # wildcard, so the reason is always about a stated list.
        names = scope.split(",") if scope else []
        if scope and (not all(names) or len(set(names)) != len(names)):
            problems.append(f"line {n}: list each metadata set once, separated "
                            f"by commas — '{scope}'")
            continue
        unknown = [x for x in names if x not in METADATA_SETS]
        if unknown:
            problems.append(f"line {n}: unknown metadata set {', '.join(unknown)} "
                            f"(the sets are {', '.join(METADATA_SETS)})")
            continue
        path = m.group("path").strip()
        path = path[2:] if path.startswith("./") else path
        if reason is None:
            what = f"keeping {scope} in '{path}'" if scope else f"'{path}'"
            problems.append(f"line {n}: {what} has no stated reason")
            continue
        digest = m.group("digest").lower()
        if scope:
            set_lines.append((n, path, digest, tuple(names), reason))
        elif path in files:
            problems.append(f"line {n}: '{path}' already listed at line "
                            f"{files[path][2]}")
        else:
            files[path] = (digest, reason, n)
    kept: dict[str, dict[str, KeptSet]] = {}
    for n, path, digest, group, reason in set_lines:
        label = ",".join(group)
        if path not in files:
            problems.append(f"line {n}: keeps {label} in '{path}', but no file line "
                            f"'<digest>  {path}' accepts the file")
            continue
        if not _same_digest(digest, files[path][0]):
            problems.append(f"line {n}: keeps {label} in '{path}' under a different "
                            f"digest from its file line {files[path][2]}")
            continue
        sets = kept.setdefault(path, {})
        again = [x for x in group if x in sets]
        if again:
            problems.append(f"line {n}: {', '.join(again)} in '{path}' already kept "
                            f"at line {sets[again[0]].lineno}")
            continue
        # The metadata's need may not be the file's own reason: one comment
        # stanza over a file line and its set lines gives every line the same
        # text, and that is the blanket form — the pixels' reason standing in
        # for the metadata's. Several sets under ONE reason is allowed (Mike,
        # 2026-10-19, 020/440), because the line names exactly which sets the
        # reason covers; so two set lines sharing a reason are not refused.
        if reason == files[path][1]:
            problems.append(f"line {n}: keeping {label} in '{path}' needs its own "
                            f"reason, the need for those sets — it repeats the "
                            f"file line {files[path][2]}'s (a comment over the file "
                            "and its sets is one blanket reason)")
            continue
        for name in group:
            sets[name] = KeptSet(name, reason, n)
    if problems:
        raise BinaryManifestError(
            f"{BINARY_MANIFEST}: {len(problems)} problem(s) — {'; '.join(problems)}. "
            "Every accepted binary, and every metadata set it keeps, states its "
            "reason where a reviewer reads it (method/GUARDS.md): a comment above "
            "the stanza, or a trailing '# reason' on the line.")
    return {path: BinaryEntry(path, d, reason, n, kept.get(path, {}))
            for path, (d, reason, n) in files.items()}


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


# The walkers append `(set, label)` to `found` for every metadata segment they
# meet, and `(label, text)` to `texts` for every one they can read as text.
_XMP_KEYWORD = "XML:com.adobe.xmp"
_RAW_PROFILE_SETS = {"exif": "exif", "app1": "exif", "iptc": "iptc",
                     "8bim": "iptc", "xmp": "xmp", "icc": "icc", "icm": "icc"}


def _png_metadata(fh, size: int, texts: list, found: list) -> None:
    pos = 8
    while True:
        fh.seek(pos)
        hdr = fh.read(8)
        if len(hdr) < 8:
            found.append(("unknown", "PNG ends without IEND"))
            return
        n = struct.unpack(">I", hdr[:4])[0]
        ctype = hdr[4:8].decode("latin-1")
        if pos + 12 + n > size:
            found.append(("unknown", f"PNG chunk {ctype} overruns the file"))
            return
        if ctype == "IEND":
            return
        if ctype == "eXIf":
            found.append(("exif", "PNG eXIf"))
        elif ctype == "iCCP":
            found.append(("icc", "PNG iCCP"))
        elif ctype in ("tEXt", "zTXt", "iTXt"):
            if n > META_SEGMENT_CAP:
                found.append(("unknown", f"PNG {ctype} past the "
                                         f"{META_SEGMENT_CAP}-byte cap"))
            else:
                _png_text_chunk(ctype, fh.read(n), texts, found)
        pos += 12 + n


def _png_text_chunk(ctype: str, data: bytes, texts: list, found: list) -> None:
    keyword, _, rest = data.partition(b"\x00")
    kw = keyword.decode("latin-1")
    label = f"PNG {ctype} '{kw}'"
    if kw.lower().startswith("raw profile type"):
        # ImageMagick carries Exif/IPTC/8BIM here as a hex dump of the binary
        # profile: text-shaped, but nothing a text rule can read.
        kind = kw.lower()[len("raw profile type"):].strip()
        found.append((_RAW_PROFILE_SETS.get(kind, "unknown"),
                      f"{label} (hex-encoded binary profile)"))
        return
    set_name = "xmp" if kw == _XMP_KEYWORD else "png-text"
    if ctype == "tEXt":
        value = rest.decode("latin-1")
    elif ctype == "zTXt":
        raw = _inflate(rest[1:])
        if raw is None:
            found.append(("unknown", f"{label} (undecodable or past the cap)"))
            return
        value = raw.decode("latin-1")
    else:  # iTXt: flag, method, language\0, translated keyword\0, text
        if len(rest) < 2:
            found.append(("unknown", f"{label} (truncated)"))
            return
        compressed = rest[0] == 1
        _lang, _, rest2 = rest[2:].partition(b"\x00")
        _tkw, _, body = rest2.partition(b"\x00")
        if compressed:
            body = _inflate(body)
            if body is None:
                found.append(("unknown", f"{label} (undecodable or past the cap)"))
                return
        value = body.decode("utf-8", errors="replace")
    found.append((set_name, label))
    texts.append((label, f"{kw}: {value}"))


_XMP_NS = b"http://ns.adobe.com/xap/1.0/\x00"
_XMP_EXT_NS = b"http://ns.adobe.com/xmp/extension/\x00"
_ICC_TAG = b"ICC_PROFILE\x00"


def _jpeg_metadata(fh, size: int, texts: list, found: list) -> None:
    pos = 2
    while True:
        fh.seek(pos)
        b = fh.read(2)
        if len(b) < 2:
            found.append(("unknown", "JPEG ends before image data"))
            return
        if b[0] != 0xFF:
            found.append(("unknown", "JPEG structure cannot be walked"))
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
            found.append(("unknown", "JPEG segment overruns the file"))
            return
        if marker in (0xE1, 0xE2, 0xED, 0xFE):
            seg = fh.read(n - 2)    # ≤ 65533 bytes by the format's own limit
            if marker == 0xFE:
                found.append(("jpeg-comment", "JPEG comment"))
                texts.append(("JPEG comment", seg.decode("utf-8", errors="replace")))
            elif marker == 0xED:
                found.append(("iptc", "JPEG APP13 (IPTC/Photoshop)"))
            elif marker == 0xE2:
                if seg.startswith(_ICC_TAG):
                    found.append(("icc", "JPEG APP2 ICC_PROFILE"))
                # other APP2 payloads (FlashPix, MPF) are outside the walk
            elif seg.startswith(b"Exif\x00"):
                found.append(("exif", "JPEG APP1 Exif"))
            elif seg.startswith(_XMP_NS):
                found.append(("xmp", "JPEG XMP"))
                texts.append(("JPEG XMP", seg[len(_XMP_NS):].decode("utf-8", errors="replace")))
            elif seg.startswith(_XMP_EXT_NS):
                # 32-byte GUID + 4-byte full length + 4-byte offset, then XML
                body = seg[len(_XMP_EXT_NS) + 40:]
                found.append(("xmp", "JPEG extended XMP"))
                texts.append(("JPEG extended XMP", body.decode("utf-8", errors="replace")))
            else:
                found.append(("unknown", "JPEG APP1 (unrecognised)"))
        pos += 2 + n


def _webp_metadata(fh, size: int, texts: list, found: list) -> None:
    fh.seek(4)
    riff_end = min(size, 8 + struct.unpack("<I", fh.read(4))[0])
    pos = 12
    while pos + 8 <= riff_end:
        fh.seek(pos)
        hdr = fh.read(8)
        fourcc = hdr[:4].decode("latin-1")
        n = struct.unpack("<I", hdr[4:8])[0]
        if pos + 8 + n > riff_end:
            found.append(("unknown", f"WebP chunk {fourcc.strip()} overruns the file"))
            return
        if fourcc == "EXIF":
            found.append(("exif", "WebP EXIF"))
        elif fourcc == "ICCP":
            found.append(("icc", "WebP ICCP"))
        elif fourcc == "XMP ":
            if n > META_SEGMENT_CAP:
                found.append(("unknown", f"WebP XMP past the {META_SEGMENT_CAP}-byte cap"))
            else:
                found.append(("xmp", "WebP XMP"))
                texts.append(("WebP XMP", fh.read(n).decode("utf-8", errors="replace")))
        pos += 8 + n + (n & 1)


def inspect_media(fh) -> tuple[str | None, list[tuple[str, str]], list[tuple[str, str]]]:
    """`(format, text segments, metadata found)` for a PNG, JPEG or WebP
    file object; `(None, [], [])` for anything else. Text segments are
    `(label, decoded text)` to be scanned; metadata found is `(set, label)`
    for every segment, text or opaque, with `set` a key of `METADATA_SETS`.
    Every read is bounded (`META_SEGMENT_CAP`, or the format's own 64 KiB
    segment limit for JPEG), so peak memory is independent of the file's
    size."""
    fh.seek(0, os.SEEK_END)
    size = fh.tell()
    fh.seek(0)
    head = fh.read(12)
    texts: list[tuple[str, str]] = []
    found: list[tuple[str, str]] = []
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        fmt, walker = "png", _png_metadata
    elif head.startswith(b"\xff\xd8"):
        fmt, walker = "jpeg", _jpeg_metadata
    elif head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        fmt, walker = "webp", _webp_metadata
    else:
        return None, texts, found
    try:
        walker(fh, size, texts, found)
    except struct.error:
        found.append(("unknown", f"{fmt.upper()} structure cannot be walked"))
    return fmt, texts, found


def metadata_sets(found: list[tuple[str, str]]) -> dict[str, list[str]]:
    """`found` grouped by set, in `METADATA_SETS` order: set -> labels."""
    by_set: dict[str, list[str]] = {}
    for name in METADATA_SETS:
        labels = [label for s, label in found if s == name]
        if labels:
            by_set[name] = labels
    return by_set


def check_binary(path: Path, rel: str, entry: BinaryEntry | None,
                 local_terms: list[tuple[str, "re.Pattern[str]"]],
                 disabled: frozenset[str], tally: Tally | None,
                 by_digest: dict[str, str] | None = None) -> list[Finding]:
    """The G3 gate for ONE tracked binary: its text metadata scanned, each
    metadata set it carries and its unread body each blocking unless `entry`
    — a reasoned `.leakscanbinaries` file line whose digest matches these
    exact bytes, plus one reasoned line per set kept — accepts them. A set
    line naming a set these bytes lack is stale. `by_digest` (digest prefix
    → listed path) lets an unlisted file say "same bytes as the entry for
    <old path>", the rename case. An unreadable file blocks rather than
    passing."""
    findings: list[Finding] = []

    def gate(rule: str, excerpt: str) -> None:
        _record(findings, tally, Finding(rel, 0, rule, "binary", "high", excerpt, "binary"))

    try:
        with open(path, "rb") as fh:
            digest = _sha256_file(fh)
            _fmt, texts, found = inspect_media(fh)
    except OSError as e:
        gate("binary-unlisted", f"unreadable ({e.__class__.__name__})")
        return findings
    for label, text in texts:
        for f in scan_text(rel, text, local_terms, disabled, tally, honour_markers=False):
            f.where = f"metadata {label}"
            findings.append(f)
    accepted = entry is not None and entry.matches(digest)
    present = metadata_sets(found)
    for name, labels in present.items():
        if not (accepted and name in entry.sets):
            gate("binary-metadata", f"{name}: {'; '.join(labels)} — no line keeps it")
    if entry is None:
        twin = (by_digest or {}).get(digest[:MIN_DIGEST_HEX])
        hint = f" — same bytes as the entry for {twin}" if twin else ""
        gate("binary-unlisted", f"sha256 {digest[:PRINTED_DIGEST_HEX]}{hint}")
    elif not accepted:
        gate("binary-changed", f"listed {entry.digest[:PRINTED_DIGEST_HEX]}, "
                               f"now {digest[:PRINTED_DIGEST_HEX]} (line {entry.lineno})")
    else:
        for name, kept in entry.sets.items():
            if name not in present:
                _record(findings, tally, _stale(
                    entry, f"keeps {name}, which these bytes do not carry",
                    kept.lineno))
        if tally is not None:
            tally.binaries_by_manifest += 1
    return findings


def _digest_index(manifest: dict[str, BinaryEntry]) -> dict[str, str]:
    return {e.digest[:MIN_DIGEST_HEX]: e.path for e in manifest.values()}


def _stale(entry: BinaryEntry, why: str, lineno: int | None = None) -> Finding:
    """An entry that accepts nothing — its file is gone, untracked, or read
    as text, or a set line keeps a set the file does not carry. Blocking,
    because the manifest is the repo's standing inventory of what the scan
    does not read (GUARDS rule b), and an inventory naming files or metadata
    that are not there is one nobody can trust. The fix is one deleted or
    re-pathed line, normally in the same commit that moved the file."""
    return Finding(BINARY_MANIFEST, lineno or entry.lineno, "binary-stale-entry",
                   "binary", "high", f"{entry.path}: {why}")


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
    """`--binary-entries`: the `.leakscanbinaries` lines a gated binary still
    needs — a file line when no entry accepts its bytes (new, or changed
    since it was listed), and one `<digest>:<set>` line per metadata set it
    carries that no line keeps — plus notes for the human. Lines carry NO
    reason on purpose: the loader refuses a line without one, so the
    re-baseline cannot complete until a person has written why each file
    may stand and, set by set, what each kept set is needed for. Never
    writes the file."""
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
            _fmt, _texts, found = inspect_media(fh)
        entry = manifest.get(rel)
        accepted = entry is not None and entry.matches(digest)
        present = metadata_sets(found)
        missing = [s for s in present if not (accepted and s in entry.sets)]
        if accepted and not missing:
            continue
        if "#" in rel or "\n" in rel or rel != rel.strip() or rel.startswith("*"):
            notes.append(f"{rel!r}: this path cannot be written as an entry "
                         "(it holds '#', a newline, edge whitespace or a leading "
                         "'*') — rename the file")
            continue
        d = digest[:PRINTED_DIGEST_HEX]
        if not accepted:
            lines.append(f"{d}  {rel}")
            if entry is not None:
                notes.append(f"{rel}: changed since listed — replaces line "
                             f"{entry.lineno} and the set lines under it")
        lines.extend(f"{d}:{s}  {rel}" for s in missing)
        if missing:
            notes.append(f"{rel}: carries metadata set(s) "
                         + ", ".join(f"{s} ({'; '.join(present[s])})" for s in missing)
                         + " — strip every set you have no need for (that changes "
                         "the bytes: re-run this), and keep a set's line only "
                         "with that set's own need as its reason")
    return lines, notes


def staged_added_lines() -> dict[str, list[tuple[int, str]]]:
    """Map path → [(real file line number, added-line text), ...] of the
    staged diff. Scans only what a commit would introduce (the pre-commit hot
    path), not the whole tree. The line number is the line's place in the file
    the commit produces, not its place among the file's added lines (115/300).
    R is in the filter deliberately (review B4): git detects renames by
    default, and a renamed-AND-edited file's added lines are exactly as
    leak-capable as a modified file's — ACM alone silently skipped them."""
    # `report.staged_added` reads the diff by its structure (115/280): the
    # path of a quoted name is undone there (115/260), and an added line that
    # merely looks like a header (`++ b/x` prints as `+++ b/x`) can neither
    # move attribution nor be dropped from the scan.
    files: dict[str, list[tuple[int, str]]] = {}
    for path, lineno, text in report.staged_added():
        files.setdefault(path, []).append((lineno, text))
    return files


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
    # `-z` output is never quoted, so `report.nul_paths` reads any name git
    # can hold (115/260). It drops empty tokens, which no field here needs.
    def toks(*extra: str) -> list[str]:
        return report.nul_paths(subprocess.run(
            ["git", "diff", "--cached", "-z", *extra],
            capture_output=True, check=True).stdout)

    changed: list[str] = []
    removed: list[str] = []
    t = toks("--name-status", "--diff-filter=ACMRD")
    i = 0
    while i < len(t):
        status = t[i]
        if status[0] in "RC":
            src, dst = t[i + 1], t[i + 2]
            changed.append(dst)
            if status[0] == "R":
                removed.append(src)
            i += 3
        else:
            (removed if status[0] == "D" else changed).append(t[i + 1])
            i += 2
    binary: set[str] = set()
    t = toks("--numstat", "--no-textconv", "--diff-filter=ACMR")
    i = 0
    while i < len(t):
        added, deleted, rest = t[i].split("\t", 2)
        if rest:
            path, i = rest, i + 1
        else:  # rename/copy: the source and destination follow as tokens
            path, i = t[i + 2], i + 3
        if added == "-" and deleted == "-":
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


def _where(f: Finding) -> str:
    # Line 0 means the hit is in the PATH itself (G2) — say so, because
    # ':0' would otherwise read as a line number nobody can open.
    if f.where:
        return f"{f.path} ({f.where}" + (f", line {f.line})" if f.line else ")")
    if f.line:
        return f"{f.path}:{f.line}"
    return f"{f.path} (in the path name)"


def render_grace(grace: list[Finding]) -> list[str]:
    """The G3 grace warnings: each names the cut-off date and its remedy."""
    if not grace:
        return []
    cut = BINARY_GRACE_UNTIL.isoformat()
    lines = [f"⚠ leakscan: {len(grace)} G3 binary finding(s) — WARNING ONLY until "
             f"{cut}, blocking from {cut} (G3 adoption grace):"]
    for f in sorted(grace, key=lambda x: (x.path, x.line, x.rule)):
        lines.append(report.with_id(
            f"  {_where(f)}  [warn until {cut}] {f.rule} → {f.excerpt}"
            f" — blocks from {cut}; remedy: {_grace_remedy(f.rule)}",
            "leakscan", f.rule))
    lines.append(f"  Before {cut}: run `leakscan --binary-entries`, write a "
                 "need-specific reason per file and per metadata set kept, strip "
                 f"the rest, and commit {BINARY_MANIFEST}.")
    lines.append("")
    return lines


def render_human(findings: list[Finding], warning: str | None,
                 scanned_local: bool, tally: Tally | None = None,
                 grace: list[Finding] | None = None) -> str:
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
    lines.extend(render_grace(grace or []))
    if not findings and not over_cap:
        cover = "structural + local" if scanned_local else "structural only"
        lines.append(f"✓ leakscan clean ({cover})."
                     + (f" The G3 warning(s) above block from "
                        f"{BINARY_GRACE_UNTIL.isoformat()}." if grace else ""))
        if tally is not None:
            lines.append(tally.summary())
        return "\n".join(lines)
    lines.append(report.findings_head("leakscan", len(findings) + over_cap,
                                      tail=" — commit blocked.\n"))
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(report.with_id(
            f"  {_where(f)}  [{f.severity}/{f.kind}] {f.rule} → {f.excerpt}",
            "leakscan", f.rule))
    if over_cap:
        lines.append(report.over_cap_line(over_cap, MAX_MATERIALIZED_FINDINGS))
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
        lines.append("  changed file blocks again. Metadata: strip every set you do not need;")
        lines.append("  keep one only on its own '<digest>:<set>' line, reasoned with that need.")
        lines.append("  A stale entry: delete or re-path it.")
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
                    help=f"print the {BINARY_MANIFEST} lines still needed and exit 0: "
                         "a file line for every tracked binary no entry accepts yet "
                         "(new, or changed since listed), and a '<digest>:<set>' line "
                         "for every metadata set it carries that no line keeps. Lines "
                         "carry no reason: review each file and write one per file and "
                         "per set kept, or the scan refuses it. Never writes the file.")
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
              "the stanza or on the line — saying what each file is and that you looked, "
              "and on each set line the need for keeping that set. Strip a set you do "
              "not need rather than keep it.",
              file=sys.stderr)
        return 0
    try:
        terms_path = resolve_terms_path(args.terms)
    except TermsPathError as e:
        return report.broken("leakscan", str(e))
    if args.require_terms and terms_path is None:
        return report.broken(
            "leakscan",
            "--require-terms set but no local term list found "
            f"(--terms, $ATELIER_LEAKSCAN_TERMS, or {DEFAULT_LOCAL_TERMS}). "
            "A structural-only scan is partial cover — refusing to report it "
            "as a pass.")
    local_terms, warning = load_local_terms(terms_path)
    scanned_local = terms_path is not None

    disabled = frozenset(r.strip() for r in args.disable.split(",") if r.strip())
    unknown = disabled - {p.name for p in STRUCTURAL}
    if unknown:
        return report.broken(
            "leakscan", f"unknown rule(s) in --disable: {', '.join(sorted(unknown))}")
    # A scope reduction taken at invocation is itself an allowance, and rule (b)
    # says a reduction nobody can see is a reduction nobody reviewed — so
    # `--disable` now reports itself in the output instead of narrowing the scan
    # silently from a flag nobody reading the result will ever see.
    tally = Tally(disabled_rules=tuple(sorted(disabled)))

    if args.staged:
        try:
            staged = staged_added_lines()
            changed, binary, removed = staged_changes()
        except report.STAGED_DIFF_FAILURES as e:
            return report.git_diff_failed("leakscan", e)
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
        # `report.scope_staged` also normalises the spelling (`.`, `./x`) and
        # refuses one that escapes the repo (roadmap 115/360). G3's extra path
        # lists (binaries, empty new files, pure renames, removals) go through
        # the same reader, so one scope means one thing on every list.
        rc, staged = report.scope_staged("leakscan", staged, args.paths, "tiki/")
        if rc is not None:
            return rc
        _rc, in_changed = report.scope_staged(
            "leakscan", dict.fromkeys(changed), args.paths, "tiki/")
        _rc, in_removed = report.scope_staged(
            "leakscan", dict.fromkeys(removed), args.paths, "tiki/")
        # .leakscanignore applies in staged mode too, so an exemption means the
        # same thing whether you scan the tree or a commit.
        globs = load_ignore_globs(root)
        manifest = load_binary_manifest(root)
        by_digest = _digest_index(manifest)
        findings = []
        # Every changed path once, in a stable order: the text diff's files
        # first (their existing order), then the paths only git's name list
        # carries — binaries, empty new files, pure renames.
        ordered = list(staged) + [p for p in in_changed if p not in staged]
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
                    findings.extend(scan_lines(path, staged[path], local_terms,
                                                 disabled, tally))
                if path not in binary:
                    continue
                try:
                    _staged_blob(path, blob)
                except subprocess.CalledProcessError as e:
                    return report.broken("leakscan",
                                         f"git cat-file failed for {path}: {e}")
                if _looks_binary_file(blob):
                    findings.extend(check_binary(blob, path, manifest.get(path),
                                                 local_terms, disabled, tally, by_digest))
                else:
                    # git calls it binary (a `binary`/`-diff` attribute) but the
                    # bytes are text: the diff showed no lines, so read the
                    # whole staged copy rather than let the attribute hide it.
                    findings.extend(_scan_file(blob, path, local_terms, disabled, tally))
        for path in in_removed:
            entry = manifest.get(path)
            if entry is not None and not _ignored(path, globs):
                _record(findings, tally, _stale(entry, "removed or renamed by this commit"))
    else:
        # A RELATIVE target resolves against --root, never the caller's cwd:
        # mixing the two reads one repo's file under another repo's rules,
        # and neither half of the output says so (roadmap 010/110).
        targets = report.resolve_targets(root, args.paths or [str(root)])
        # A typo'd path scanning nothing must never read as a clean pass —
        # the linkscan L1 silent-success class, closed here too
        # (2026-07-11 review N2).
        rc = report.refuse_missing_paths("leakscan", targets)
        if rc is not None:
            return rc
        findings = scan_paths(targets, root, local_terms, disabled, tally)

    # THE G3 GRACE (see `BINARY_GRACE_UNTIL`): before the cut-off the four
    # gate rules warn instead of blocking. Only those rules — a text-metadata
    # hit is an ordinary rule's finding and still blocks. Findings past the
    # materialisation cap were counted, never built, so they cannot be sorted
    # by rule and stay blocking: fail closed.
    grace: list[Finding] = []
    if in_binary_grace():
        grace = [f for f in findings if f.rule in BINARY_RULES]
        findings = [f for f in findings if f.rule not in BINARY_RULES]
        tally.binary_grace_warnings = len(grace)

    if args.json:
        print(json.dumps({
            "clean": not findings and not tally.findings_over_cap,
            "scanned_local_terms": scanned_local,
            "warning": warning,
            "findings": report.finding_dicts("leakscan", findings,
                                             lambda f: f.rule),
            "findings_over_cap": tally.findings_over_cap,
            "binary_grace": {
                "until": BINARY_GRACE_UNTIL.isoformat(),
                "active": in_binary_grace(),
                "warnings": report.finding_dicts("leakscan", grace,
                                                 lambda f: f.rule),
            },
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
        print(render_human(findings, warning, scanned_local, tally, grace))

    return report.exit_code(len(findings) + tally.findings_over_cap)


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
    _f, _t, found = inspect_media(png(b"eXIf", b"MM\x00\x2a"))
    if [s for s, _l in found] != ["exif"]:
        print("FAIL: PNG eXIf chunk not reported as the exif metadata set")
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
    return report.guarded_main("leakscan", _main, argv,
                               (IgnoreFileError, BinaryManifestError))

if __name__ == "__main__":
    sys.exit(main())
