#!/usr/bin/env python3
"""leakscan — the mechanical net that catches the SHAPE of personal/estate data
before it is committed.

The doctrine (`docs/build/REPO-STANDARD.md` § Personal data) says a repo holds
personal data only for a purpose, with every exception recorded; a public repo
holds only the closed list its principal has granted. A rule enforced by intent
alone fails the first tired session. This is the machine behind it: a denylist
scan run as a pre-commit hook and in CI, so a leak fails the commit instead of
reaching the remote. It reads shapes and listed terms, not purpose: a person
described in paraphrase passes, and an allow-marker on a line records that
someone judged the line; it is not a grant of an exception.

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
blocking until a reasoned line keeps that set. Each manifest line also records
WHO allowed it and WHEN (`by=… session=… on=…`; a line without them warns).
Until `BINARY_GRACE_UNTIL` (2026-11-18, firm for every child) these G3 findings
warn and do not block — the one, dated exception to "no advisory form" for a
rule that blocks. See the G3 block below and the leakscan section of
`tools/README.md`.

Rules that are OFF report without blocking (115/090, Mike's answer
2026-10-16: "Report-only for off rules"). A rule a repo turns off with
`--disable`, and a rule withdrawn from the blocking set for noise
(`WITHDRAWN`), still run: each hit is listed in a report-only block, counted on
a `leakscan advisory: N finding(s)` line printed on every run, and never moves
the exit code. Nothing that blocks today stops blocking; `test_leakscan.
BlockingSetPinned` holds that. Design: `leakscan.off-rules.design.md`.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean, or report-only findings only (G3 grace warnings, before the
     cut-off, do not change this either)
  1  blocking findings (blocks the commit)
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
import unicodedata
import xml.parsers.expat as _expat
import zlib
from dataclasses import dataclass, asdict, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import filewalk  # noqa: E402
import allowmarker  # noqa: E402
import anchoredrx  # noqa: E402
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
    severity: str  # "high" | "medium" — confidence only, never the response
    regex: "re.Pattern[str]"
    # 110/130 lever 4, 160/720 GT2: the rule's pre-filter, declared BESIDE the
    # rule so that widening the regex and re-reading the gate are one diff
    # hunk. A gate is a cheap test on the line that is NECESSARY for the rule
    # to match; None means the rule always runs its full regex (fail open). See
    # "per-rule pre-filters" below for what a gate may and may not be.
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

# Cheap pieces the rules' gates (declared on each rule below) share. Each is
# derived from a rule's own pattern text and is a NECESSARY condition for it.
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
# diagnosis-key: its key alternatives all contain these letters, any case.
_DIAGNOS_RX = re.compile(r"(?i)diagnos")

# Structural patterns. Ordered high→medium. Tuned to catch real estate/PII shapes
# while keeping false positives survivable (fail-safe favours over-flagging: a
# false positive costs a `leakscan:allow`, a false negative costs a leak).
STRUCTURAL: list[Pattern] = [
    _p("private-key-header", "high",
       r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----",
       # gate: `-----BEGIN [..] PRIVATE KEY-----` ends in this literal.
       gate=lambda ln: "PRIVATE KEY-----" in ln),
    _p("aws-access-key-id", "high", r"\bAKIA[0-9A-Z]{16}\b",
       gate=lambda ln: "AKIA" in ln),
    _p("jwt", "high", r"\beyJ[A-Za-z0-9_-]{6,}\.eyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}",
       # gate: `eyJ…\.eyJ…` - the second segment's lead-in.
       gate=lambda ln: ".eyJ" in ln),
    _p("email", "high",
       r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
       gate=lambda ln: "@" in ln,
       anchored=dict(run=r"[A-Za-z0-9._%+-]+", literal="@", start=r"\b")),
    # G1 — the key-context layer. High: the label has already done the
    # filtering, so a surviving hit is about as confident as this tool gets.
    _p("pii-key-context", "high", PII_KEY_RX,
       gate=lambda ln: _PII_TAIL_RX.search(ln) is not None),
    # G4 — financial identifiers. Card and IBAN are SELF-VALIDATING (Luhn and
    # ISO 7064 mod-97 respectively, both applied in VALIDATORS below), which is
    # what keeps a long digit run from being a false-positive engine. The
    # grouped alternative exists so the space- and hyphen-separated spellings
    # of a card are caught without letting a single-space separator stitch an
    # arbitrary numeric table row into a sixteen-digit "card".
    _p("payment-card", "high",
       r"(?<![\d-])(?:\d{13,19}|\d{4}(?:[ -]\d{4}){2,3}(?:[ -]\d{1,3})?)(?![\d-])",
       # gate: 13-19 digits or `\d{4}` groups: either way four digits in a row.
       gate=lambda ln: _DIGITS4_RX.search(ln) is not None),
    _p("iban", "high", r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b",
       # gate: `[A-Z]{2}\d{2}[A-Z0-9]{11,30}` is at least 15 characters long.
       gate=lambda ln: len(ln) >= 15),
    _p("mac-address", "high",
       r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b",
       # gate: `(?:xx[:-]){5}xx` - five separators.
       gate=lambda ln: ln.count(":") + ln.count("-") >= 5),
    _p("ipv4", "medium", r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
       gate=lambda ln: ln.count(".") >= 3),
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
       r")(?![0-9A-Za-z:])",
       # gate: every alternative carries at least two colons (`h::h`, `h:h::`, `::h:h`).
       gate=lambda ln: ln.count(":") >= 2),
    # G4 — the NZ bank account in its hyphenated field form (bank-branch-
    # account-suffix). The COMPACT all-digit form stays key-context-only per
    # the ruling: bare eight-to-sixteen digit runs are the don't-add list.
    _p("nz-bank-account", "medium", r"\b\d{2}-\d{4}-\d{7}-\d{2,3}\b",
       gate=lambda ln: ln.count("-") >= 3),
    # G7 — the bracketed area-code form (landline or mobile prefix in
    # parentheses), the one common NZ spelling the rule missed.
    _p("nz-phone", "medium",
       r"(?<!\d)(?:"
       r"(?:\+64[\s-]?|0)(?:2\d|[3-9])"
       r"|\((?:\+64[\s-]?)?0?(?:2\d|[3-9])\)"
       r")[\s-]?\d{3}[\s-]?\d{3,4}(?!\d)",
       gate=lambda ln: _PHONE_TAIL_RX.search(ln) is not None),
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
       r")\b",
       gate=lambda ln: _ADDRESS_SUFFIX_RX.search(ln) is not None),
    _p("coordinates", "medium",
       r"[-+]?\d{1,2}\.\d{4,}\s*,\s*[-+]?\d{1,3}\.\d{4,}",
       gate=lambda ln: "," in ln and ln.count(".") >= 2),
    _p("nz-ird", "medium", r"\b\d{2,3}-\d{3}-\d{3}\b",
       gate=lambda ln: ln.count("-") >= 2),
]

# --- rules that are OFF report without blocking (115/090) ---------------
#
# Mike's answer, 2026-10-16, re-briefed on the EI6 ruling it narrows: "Report-
# only for off rules". A rule that is off today comes back as REPORT-ONLY: it
# runs, its hits are listed and counted on every run, and none of them moves
# the exit code. Nothing that blocks today stops blocking. Two kinds of off:
#
#   * WITHDRAWN below: a rule taken out of the blocking set for noise and kept
#     out. It has no blocking form at all, so `--disable` has nothing to switch.
#   * DISABLED: a STRUCTURAL rule a repo turns off with `--disable` (the floor
#     config's `flags`). It still runs; its hits report instead of blocking.
#
# A rule NARROWED for noise (ipv6's D2 shape, nz-address's D4 suffix guard) is
# not off: it blocks on its narrower shape, and the shapes it excludes are
# not reported. The design note is `leakscan.off-rules.design.md`.
#
# The diagnosis/diagnoses key was the withdrawn member of the G1 vocabulary
# (see the note above PII_KEY_RX): a genuine health key that is also how
# root-cause paragraphs open. Here it reads exactly as `pii-key-context` would
# read it, placeholder suppression included.
WITHDRAWN: list[Pattern] = [
    _p("diagnosis-key", "medium",
       r"(?i)" + _KEY_LEAD + r"(?P<key>diagnos[ie]s)"
       r"\b\s*[:=]\s*[\"']?(?P<value>[^\s\"'`,;:]{2,})",
       # gate: the key-context tail, and the key's own letters.
       gate=lambda ln: (_DIAGNOS_RX.search(ln) is not None
                        and _PII_TAIL_RX.search(ln) is not None)),
]
WITHDRAWN_NAMES = frozenset(p.name for p in WITHDRAWN)
# Every rule the engine runs, in report order: STRUCTURAL first, unchanged.
ALL_RULES: tuple[Pattern, ...] = (*STRUCTURAL, *WITHDRAWN)

# A finding's response. Defaulted to block on `Finding`, so a new rule that
# forgets to say fails SAFE, into the gate (secretscan's shape).
RESPONSE_BLOCK = "block"
RESPONSE_ADVISORY = "advisory"

# The line `render_human` prints on EVERY run, zero included, so a reader and
# `tools/floor.py`'s board read the count off one run (the advisory-count
# contract, `floor.advisory_count_rx`).
ADVISORY_COUNT_PREFIX = "leakscan advisory:"

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
    # 020/380 — see MAX_MATERIALIZED_FINDINGS above. `findings_over_cap`
    # counts BLOCKING findings past the cap and feeds the exit code; since
    # 115/090 a reporting finding past the cap is counted apart, in
    # `advisory_over_cap`, so it can never move the exit code (secretscan's
    # blocking/advisory split).
    findings_over_cap: int = 0
    advisory_over_cap: int = 0
    # G3: tracked binaries whose body the scan could not read and a reasoned,
    # hash-bound `.leakscanbinaries` entry accepted; and binaries the
    # full-tree walk met that git does not track, which the gate does not
    # cover (an untracked file reaches no remote). Both are counted so a
    # clean run says what it did not read.
    binaries_by_manifest: int = 0
    binaries_untracked: int = 0
    # 160/480 AM10: allow-markers whose scope names a rule that does not
    # exist, which are silently inert (the finding they were written for still
    # reports). Counted so a typo is visible on a clean run too.
    unknown_scope_markers: int = 0
    # The G3 adoption grace (see `BINARY_GRACE_UNTIL`): gate findings printed
    # as warnings, not counted in the exit code. Always 0 from the cut-off on.
    binary_grace_warnings: int = 0
    # 020/450: type-level entries still accepted, as warnings, before
    # `TYPE_LEVEL_UNTIL`. Always 0 from that date on.
    # They are kept OUT of the findings, so no caller of `scan_paths` can take
    # one for a block; the CLI prints them.
    type_level_warnings: list = field(default_factory=list, compare=False)
    # 160/980 GM5: manifest lines that record no who/when, as warnings that
    # never block. Kept out of the findings for the same reason.
    provenance_warnings: list = field(default_factory=list, compare=False)
    _materialized: int = field(default=0, repr=False, compare=False)

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def take_finding_slot(self, blocking: bool = True) -> bool:
        """True if a finding may still be fully materialized (built and
        held); False once the run-wide cap is reached, in which case it is
        counted instead — in `findings_over_cap` if it blocks, in
        `advisory_over_cap` if it only reports."""
        if self._materialized < MAX_MATERIALIZED_FINDINGS:
            self._materialized += 1
            return True
        if blocking:
            self.findings_over_cap += 1
        else:
            self.advisory_over_cap += 1
        return False

    def note_marker(self, rule: str) -> None:
        self.by_marker[rule] = self.by_marker.get(rule, 0) + 1

    def note_unknown_scope(self) -> None:
        self.unknown_scope_markers += 1

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
                 f"{len(self.type_level_warnings)} type-level metadata entr(y/ies) "
                 f"warned, not blocking, before {TYPE_LEVEL_UNTIL.isoformat()}",
                 f"{len(self.provenance_warnings)} manifest line(s) with no who/when "
                 "warned, not blocking",
                 report.cap_part(self.findings_over_cap, MAX_MATERIALIZED_FINDINGS),
                 f"{self.unknown_scope_markers} marker(s) naming no rule"]
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
    # 115/090: "block" | "advisory". Defaulted to block so a finding built
    # anywhere without saying fails SAFE, into the gate. Only a rule that is
    # off (withdrawn, or disabled by the repo) builds an advisory one.
    response: str = RESPONSE_BLOCK

    @property
    def blocks(self) -> bool:
        return self.response == RESPONSE_BLOCK


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


_HEX_RUN_MIN = 16   # a hex run this long is a digest or id, not prose


def _phone_inside_hex_digest(m: "re.Match[str]") -> bool:
    r"""Roadmap 320/470 (option 1, a digest-context guard). The phone rule's
    `(?<!\d)`/`(?!\d)` lookarounds accept a hex LETTER beside the digits, so a
    nine-digit run between two hex letters inside a SHA digest read as a phone. A
    separator-free digit match is not a phone when the unbroken run of hex
    characters around it is 16+ long. A spaced, dashed or bracketed phone is
    never skipped — a digest holds no separator, so prose keeps full reach."""
    text = m.group(0)
    if not text.isdigit():
        return False
    s, line = m.start(), m.string
    lo = s
    while lo > 0 and line[lo - 1] in _HEX_CHARS:
        lo -= 1
    hi = m.end()
    while hi < len(line) and line[hi] in _HEX_CHARS:
        hi += 1
    return hi - lo >= _HEX_RUN_MIN


_HEX_CHARS = frozenset("0123456789abcdefABCDEF")


# Per-rule post-match validators: the regex says "this is the right SHAPE", the
# validator says "and it is not one of the shapes we ruled out". Keeping them
# beside the patterns means a rule's exclusions are readable in one place
# rather than accreting as special cases inside the scan loop. A rule with no
# entry here keeps every match.
VALIDATORS: dict[str, "object"] = {
    "ipv4": lambda m: not _ipv4_is_safe(m.group(0)),
    "payment-card": lambda m: _luhn_ok(m.group(0)),
    "iban": lambda m: _iban_ok(m.group(0)),
    "nz-phone": lambda m: not _phone_inside_hex_digest(m),
    "pii-key-context": lambda m: not _is_placeholder(m.group("value")),
    "diagnosis-key": lambda m: not _is_placeholder(m.group("value")),
}


def _nfc(text: str) -> str:
    """Unicode NFC (LK2, 2026-11-09). A macron can be one code point (U+0101)
    or a base letter plus a combining mark (U+0061 U+0304); the two print
    identically and a plain regex matches only the spelling it was compiled
    from. Plain and `forms:` terms are compiled from NFC, and the line is also
    searched in NFC (`_term_hit`), so a term typed one way catches text typed
    the other. ASCII, the overwhelming case, is returned untouched."""
    return text if text.isascii() else unicodedata.normalize("NFC", text)


def derived_form_regex(term: str) -> "re.Pattern[str]":
    """G6 — the OPT-IN derived-form matcher behind a `forms:` term.

    A name leaks as a slug, a localpart or an identifier far more often than as
    the canonical spaced literal: the sweep probed a listed name's slug,
    camel-case, snake-case and double-spaced forms and every one passed clean.
    This joins the term's words with `[\\s._/+-]*`, so one term covers
    `jane-q-public`, `jane_q_public`, `jane.q.public`, `janeQPublic`,
    `janeqpublic`, any whitespace run between the words, and (LK3, 2026-11-09)
    a name spread across path components (`jane/q/public.md`, the shape the
    path plane reads) or tagged into an email local part (`jane+q+public`).

    OPT-IN, and it stays opt-in: the zero-separator form means a short or
    common-word term can start matching inside ordinary compounds, and only the
    operator holding the real list can judge that. Word boundaries still bound
    both ends. LIMIT, stated because it is not obvious: scanning is line-based,
    so a name split ACROSS lines is still not matched by anything.

    Also carries the plural/plural-possessive suffix (PLURAL_SUFFIX, ruled
    2026-09-18) so `jane-q-publics` and `jane-q-publics'` hit alongside the
    bare derived form."""
    parts = [re.escape(p) for p in term.split() if p]
    return re.compile(r"\b" + r"[\s._/+-]*".join(parts) + PLURAL_SUFFIX, re.IGNORECASE)


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
            body = _nfc(line[len("forms:"):].strip())
            terms.append((body, derived_form_regex(body)))
        else:
            line = _nfc(line)
            terms.append((line, re.compile(r"\b" + re.escape(line) + PLURAL_SUFFIX, re.IGNORECASE)))
    return terms, None


BY_NAME: dict[str, Pattern] = {p.name: p for p in ALL_RULES}

# What a marker's scope may name (AM10): a structural rule, or `local-term`.
_MARKER_RULE_NAMES = frozenset(BY_NAME) | {"local-term"}


# --- per-rule pre-filters (roadmap 110/130, lever 4) ---------------------
#
# Each gate is a CHEAP test on the line that is NECESSARY for its rule to match:
# if the gate says no, the rule's regex provably has no match on that line, so
# skipping `finditer` changes nothing — same findings, same order, same counts.
# That is the only property a gate may have. A gate that could reject a line the
# rule would match is a silent false negative in a boundary scanner, the worst
# failure this tool has, so every gate below states WHY it is necessary and is
# derived from the rule's own pattern text, never from a guess about the data.
# A rule that declares no gate has no provable cheap necessary condition and
# always runs its full regex (fail open). The gate is declared on the rule
# (`Pattern.gate`), beside the regex it conditions. `test_leakscan.
# GatesAreNecessary` pins each gate against its rule on matching and near-miss
# lines, and every top-level alternative of every gated rule.
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
# The gate table, DERIVED from the rules (160/720 GT2/GT3): each rule's gate is
# declared on the rule itself, above, and this dict is the single runtime home
# the scan loop and `_shadow_spans` both read. `_active_rules` builds from it
# when it first needs a disabled-set, behind its memo, so patching `GATES` and
# clearing `_ACTIVE_CACHE` switches gating off everywhere at once.
GATES: dict[str, "object"] = {p.name: p.gate for p in ALL_RULES
                              if p.gate is not None}
_ACTIVE_CACHE: dict[frozenset[str], tuple] = {}


def blocks(rule: str, disabled: frozenset[str] = frozenset()) -> bool:
    """Does a hit of `rule` block, with `disabled` turned off? (115/090.)
    A withdrawn rule never blocks; a disabled one reports instead; every
    other rule blocks exactly as it did before off rules began reporting."""
    return rule not in disabled and rule not in WITHDRAWN_NAMES


def _active_rules(disabled: frozenset[str]) -> tuple:
    """Every rule in `ALL_RULES`, each with its gate from `GATES` and whether
    its hits block (115/090: a    disabled rule runs and reports rather than being skipped), memoised per
    disabled-set so the per-line loop does not re-test every name."""
    if not isinstance(disabled, frozenset):   # a plain set worked before
        disabled = frozenset(disabled)
    got = _ACTIVE_CACHE.get(disabled)
    if got is None:
        got = _ACTIVE_CACHE[disabled] = tuple(
            (p, GATES.get(p.name), blocks(p.name, disabled))
            for p in ALL_RULES)
    return got


def _shadow_spans(line: str, disabled: frozenset[str]) -> dict[str, list[tuple[int, int]]]:
    """D5 — per shadowed rule, the spans another rule has already claimed.

    115/090: every rule runs now, but a shadow may never cost a BLOCKING
    finding. A blocking shadowed rule is shadowed only by blocking shadowers,
    exactly as before (a disabled shadower casts no shadow, so `--disable
    mac-address` still leaves ipv6 blocking a MAC). A reporting shadowed rule
    is shadowed by every shadower: one span, one finding."""
    out: dict[str, list[tuple[int, int]]] = {}
    for shadowed, shadowers in SHADOWED_BY.items():
        shadowed_blocks = blocks(shadowed, disabled)
        # 110/130: a shadow only ever suppresses a match of the SHADOWED rule,
        # and a shadower casts a span only where its own regex matches — so if
        # the shadowed rule's gate fails there is nothing to suppress, and if a
        # shadower's gate fails it has no span. Gates are necessary conditions
        # (see GATES), so no span that could have mattered is lost.
        gate = GATES.get(shadowed)
        if gate is not None and not gate(line):
            continue
        spans = [m.span()
                 for name in shadowers
                 if not shadowed_blocks or blocks(name, disabled)
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
    if tally is None or tally.take_finding_slot(finding.blocks):
        findings.append(finding)


def _term_hit(rx: "re.Pattern[str]", line: str, nfc_line: str) -> bool:
    """A term matches the line as written, or (LK2) as NFC-normalised. The
    union only ever adds a hit, so a `regex:` term that matched before still
    matches and one written for the decomposed spelling still can."""
    return rx.search(line) is not None or (
        nfc_line is not line and rx.search(nfc_line) is not None)


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
        if (allow_scope and tally is not None
                and allowmarker.names_no_rule(allow_scope, _MARKER_RULE_NAMES)):
            tally.note_unknown_scope()
        shadows = _shadow_spans(line, disabled)
        for pat, gate, blocking in rules:
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
                _record(findings, tally, Finding(
                    path, lineno, pat.name, "structural", pat.severity,
                    redact(span),
                    response=RESPONSE_BLOCK if blocking else RESPONSE_ADVISORY))
        # D1: the term list runs on EVERY line — the unscoped marker never
        # reaches it. The ONE exemption is a scope naming `local-term`
        # explicitly (ruled 2026-08-09): deliberate, reasoned, counted.
        nfc_line = _nfc(line)
        for term, rx in local_terms:
            if _term_hit(rx, line, nfc_line):
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
    exempted by a glob never reaches it. That is now true by construction
    (LK6, 2026-11-09): the path is scanned with `honour_markers=False`, so a
    filename that itself spells a marker and a reason cannot exempt its own
    findings. (The docstring said so before; the code did not do it.)"""
    return [Finding(rel, 0, f.rule, f.kind, f.severity, f.excerpt,
                    response=f.response)
            for f in scan_text(rel, rel, local_terms, disabled, tally,
                               honour_markers=False)]


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
# for a rule that blocks (E6a; rules that are off report, 115/090), with ONE
# dated exception, the adoption grace below. This is the build
# of that ruling:
#
#   * THE MARKER is an entry in `.leakscanbinaries` at the scan root —
#     `<sha256 hex, ≥16 chars>  <path>` accepts the file, and
#     `<same digest>:<set>  <path>` keeps ONE named metadata set — each line
#     reasoned with the SAME grammar as `.leakscanignore`
#     (`allowmarker.read_reasoned_parts`: a trailing `# reason` or a comment
#     stanza), and recording WHO allowed it and WHEN beside the reason
#     (`by=<principal-ruled|principal-answer|agent> session=<id|human>
#     on=<YYYY-MM-DD>`, the exception register's vocabulary, ADR 2026-10-03-0641:
#     Mike, 2026-10-03, wanted every exception "recorded so that its clear
#     that the exception exists, why it is necessary, who created it (e.g.
#     session transcript ID, did I rule or did you do it automatically etc),
#     when the exception was granted"; he chose that for this manifest on
#     2026-11-08, 160/980 GM5). A line written before that, with a reason and
#     no who/when, still loads and WARNS, naming itself; nothing here dates
#     the warning into a block, which is the principal's to rule. A binary
#     cannot hold an inline marker, and a `.leakscanignore` glob is the wrong
#     hatch: it is path-wide, rule-wide and blind to content, so a REPLACED
#     image would pass under the old acceptance. For that reason the gate runs
#     BEFORE the ignore file for a binary (Mike's answer, 2026-11-08, 160/980
#     GM9): a glob never skips G3. The digest is what makes "one-time" true — a
#     changed binary no longer matches its entry and blocks again, and the
#     human who re-lists it is looking at the new bytes.
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
#     blocks as `binary-metadata`, naming the set. These sets are DATA TYPES
#     (Exif, XMP, …), not the fields he meant ("GPS versus the camera model",
#     his next sentence, 020/440); the field-level keep is `020/450`, built
#     below for Exif, GPS, IPTC, XMP and PNG text. ICC profiles and JPEG
#     comments have no fields to name.
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
#   * FIELDS (020/450): the Exif, IPTC, XMP and PNG text sets are read field by
#     field, so a line keeps `exif:Model,LensModel` and not the `gps:` tags
#     beside them, `iptc:By-line,Credit`, `xmp:dc:creator` or
#     `png-text:Author`. See `EXIF_TAGS`, `IPTC_DATASETS`, `xmp_fields` and
#     `png_text_field`. A type-level line (`exif`, `iptc`, `xmp`, `png-text`)
#     is accepted with a warning until `TYPE_LEVEL_UNTIL`. ICC profiles and JPEG
#     comments have no fields to name and stay whole-set.
#
# What it cannot see, stated so nobody infers cover that is not there: the
# pixels themselves (no OCR — the entry's reason is the human attesting to
# them); metadata in any other format (GIF, TIFF, HEIC/AVIF, PDF, Office
# documents, fonts, archives — for these the file line accepts the whole
# file, metadata included); JPEG segments after the first start-of-scan, and
# JPEG APPn segments other than APP1, APP2 (ICC) and APP13; the CONTENT of an
# ICC profile (named by presence, never read); the VALUES of Exif and IPTC
# fields (named, never read; XMP and PNG text values are run through the text
# rules, which match shapes and do not understand them); bytes appended after
# a format's end marker.
#
# Two guards here are weaker than a reader may assume (160/980 GM14): the
# blanket refusal (a set line's reason may not repeat the file line's) is
# textual equality, so a one-character difference loads and specificity stays
# the human's; and the JPEG walker's cost is linear in the length of a run of
# degenerate markers (a million RST markers took 0.5 s), bounded by the file's
# size and not budgeted.
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
_ENTRY_RX = re.compile(r"^(?P<digest>[0-9A-Fa-f]{%d,64})(?::(?P<scope>[A-Za-z0-9_,:.%%-]+))?"
                       r"[ \t]+\*?(?P<path>\S.*)$" % MIN_DIGEST_HEX)

# THE ADOPTION GRACE — the one exception to E6a, and dated.
#
# E6a: leakscan has no advisory form for a rule that blocks; every finding of
# one blocks (rules that are off report, and never blocked, 115/090). On
# 020/150, 2026-10-18, Mike chose, through the decision device, the option
# labelled "Grace period (Recommended)". The option's own text was the queue
# run's, not his words: "unlisted files print a warning naming a cut-off date
# (~30 days), then start blocking. No child goes red today; each lists its
# files when convenient." His choice of that option is the authority for this
# exception, and it is the ONLY one: it covers the four G3 gate rules
# (`BINARY_RULES`) and nothing else. Every other leakscan rule, including a
# hit in an image's TEXT metadata, blocks as before.
#
# The exact date was the queue-run orchestrator's pick on that "~30 days"
# (31 days after the answer was given). Mike made it FIRM on 2026-11-08
# (160/980 GM7; his answer, "Firm; queue fixes now"): 2026-11-18 stands for
# every child, each child that would fail gets an item on its own board to
# strip or list before then, and a child not worked by the date goes red until
# it is. In GUARDS' terms it is a mandate: a child may list or strip earlier
# or argue an exemption through its parent, and none can move the date. Before
# it, a G3 finding prints as a warning naming the date and the remedy and does
# not fail the exit code; ON and after it, the finding blocks exactly as built. It is
# unreachable after the date by construction: the cut-off lives in this one
# constant and is compared with the UTC clock, and there is no flag, env var
# or config key that moves it. A child's floor overrides cannot reach it
# (floor.py refuses an abbreviated mode flag, and `--disable` refuses a
# binary rule as unknown). The grace is not an advisory FORM in floor.py's
# registry either: leakscan's `advisory` stays None, so it still "cannot be
# softened". Delete this block, `in_binary_grace` and its callers once the
# date has passed.
BINARY_GRACE_UNTIL = datetime.date(2026, 11, 18)

# THE TYPE-LEVEL CUT-OFF (020/450) — a second, later and narrower date.
#
# `020/450` reads the FIELDS inside a metadata set (Exif and GPS tags, IPTC
# datasets, XMP properties, PNG text keywords), so an entry can keep
# `exif:Model,LensModel` and not the GPS block beside them. Entries written
# before that, which keep a whole set (`exif`, `iptc`, `xmp`, `png-text`), are
# still accepted: until this date they WARN, naming the fields the file carries
# and asking for field-level entries. From it they stop keeping the sets whose
# fields are read, and the set blocks as `binary-metadata`. Sets with no fields
# to name (`icc`, `jpeg-comment`, `unknown`) keep their type-level entries
# unchanged. Like the grace it is one constant compared with the UTC
# clock, with no flag, env var or config key to move it; it is later than the
# grace's end on purpose, so a child that listed its binaries by type before
# 2026-11-18 has a month to migrate. Delete the warning path once it passes.
TYPE_LEVEL_UNTIL = datetime.date(2026, 12, 18)
TYPE_LEVEL_RULE = "binary-type-level"


def in_type_level_grace(today: datetime.date | None = None) -> bool:
    """True strictly before `TYPE_LEVEL_UNTIL` (UTC). Tests patch
    `_utc_today`."""
    return (today or _utc_today()) < TYPE_LEVEL_UNTIL


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
class Provenance:
    """WHO allowed a manifest line and WHEN (160/980 GM5): the exception
    register's `granted_by`, `session` and `granted`, written
    `by=<kind> session=<id|human> on=<YYYY-MM-DD>` in the line's comment."""
    by: str
    session: str
    on: str


@dataclass(frozen=True)
class KeptSet:
    """One `<digest>:<set>  <path>` line: a metadata set kept, and why."""
    name: str
    reason: str
    lineno: int
    prov: "Provenance | None" = field(default=None, compare=False)


@dataclass(frozen=True)
class BinaryEntry:
    path: str
    digest: str               # lower-case hex prefix of the file's SHA-256
    reason: str
    lineno: int
    sets: dict = field(default_factory=dict, compare=False)   # name -> KeptSet
    prov: "Provenance | None" = field(default=None, compare=False)

    def matches(self, sha256_hex: str) -> bool:
        return sha256_hex.startswith(self.digest)


# WHO and WHEN, in the exception register's vocabulary (ADR 2026-10-03-0641):
# `principal-ruled` (his own words), `principal-answer` (a pick from a session's
# options), or `agent` (a session's judgement). The session is the transcript
# id (`$CLAUDE_CODE_SESSION_ID`) or `human`. This is the minimum that honours
# his 2026-10-03 words for this manifest; the held register (110/100) would
# carry the same three fields as `file` entries, so a line migrates as it is.
PROVENANCE_KINDS = ("principal-ruled", "principal-answer", "agent")
_PROVENANCE_RX = re.compile(
    r"\bby=(?P<by>\S+)\s+session=(?P<session>\S+)\s+on=(?P<on>\S+)")
_SESSION_RX = re.compile(r"^(?:human|[A-Za-z0-9][A-Za-z0-9._-]{3,63})$")
PROVENANCE_FORM = "by=<principal-ruled|principal-answer|agent> session=<id|human> on=<YYYY-MM-DD>"
PROVENANCE_RULE = "binary-no-provenance"


def split_provenance(text: str) -> tuple["Provenance | None", str, str | None]:
    """`(provenance, rest, problem)` for the comment text of a manifest line.
    `rest` is the text with the provenance removed, which is what counts as
    the reason: who and when are not a reason. No `by=` token is no
    provenance and no problem (the line is old, and warns); a `by=` that does
    not read as the whole form is a problem, never a quiet pass."""
    if not re.search(r"\bby=", text):
        return None, text, None
    m = _PROVENANCE_RX.search(text)
    if not m:
        return None, text, f"incomplete who/when — write {PROVENANCE_FORM}"
    if m.group("by") not in PROVENANCE_KINDS:
        return None, text, (f"by={m.group('by')} is not a kind of grant (use "
                            f"{', '.join(PROVENANCE_KINDS)})")
    if not _SESSION_RX.match(m.group("session")):
        return None, text, (f"session={m.group('session')} is not a session id "
                            "(4–64 letters, digits, '.', '_' or '-') or 'human'")
    try:
        datetime.date.fromisoformat(m.group("on"))
    except ValueError:
        return None, text, f"on={m.group('on')} is not a YYYY-MM-DD date"
    rest = (text[:m.start()] + " " + text[m.end():]).strip(" \t;,-—")
    return Provenance(m.group("by"), m.group("session"), m.group("on")), \
        re.sub(r"\s+", " ", rest), None


def _same_digest(a: str, b: str) -> bool:
    return a.startswith(b) or b.startswith(a)


# A type-level key and the field sets it keeps when it is the whole type: the
# Exif set holds the GPS IFD, so a whole-`exif` entry has always kept GPS too.
_KEY_COVERS = {"exif": ("exif", "gps"), "iptc": ("iptc",), "xmp": ("xmp",),
               "png-text": ("png-text",)}


def _keys_overlap(a: str, b: str) -> bool:
    """Do two kept keys keep any of the same thing? `exif` overlaps every
    `exif:` and `gps:` field; a field overlaps only itself."""
    if a == b:
        return True
    for whole, field_sets in _KEY_COVERS.items():
        for x, y in ((a, b), (b, a)):
            if x == whole and ":" in y and y.split(":", 1)[0] in field_sets:
                return True
    return False


def parse_scope(scope: str) -> tuple[list[str], str | None]:
    """A set line's scope, `icc,xmp` or `exif:Model,LensModel,gps:GPSLatitude`,
    as `(keys, problem)`. A key is a whole set (`icc`) or one field
    (`exif:Model`); a bare name after a `set:Field` is another field of the
    same set (an XMP field is always written in full, `xmp:dc:creator`, as its
    own prefix could be a set's name). No wildcard, and no group name alone:
    `gps` would keep every GPS tag under a reason that names none of them
    (020/450: "it should be specific"), so the fields are listed."""
    keys: list[str] = []
    cur: str | None = None
    for tok in scope.split(","):
        if not tok:
            return [], f"list each metadata set once, separated by commas — '{scope}'"
        head, sep, rest = tok.partition(":")
        if sep and head in FIELD_SETS:
            cur, name = head, rest
        elif sep and cur == "iptc" and _IPTC_NUM_RX.match(tok):
            name = tok                      # iptc:2:080, then 2:090 continues it
        elif sep and cur == "xmp":
            return [], (f"write each xmp field in full, xmp:{tok} — a bare "
                        f"'{head}:' could be another set's field")
        elif sep:
            return [], (f"'{head}' has no fields to name — fields are read for "
                        f"{', '.join(FIELD_SETS)}")
        elif tok in METADATA_SETS:
            keys.append(tok)
            cur = None
            continue
        elif cur == "xmp":
            return [], f"write each xmp field in full, xmp:<prefix>:{tok}"
        elif cur is not None:
            name = tok
        elif tok in FIELD_SETS:
            return [], (f"'{tok}' alone would keep every field in it — name them, "
                        f"'{tok}:<Field>[,<Field>...]'")
        else:
            return [], (f"unknown metadata set {tok} (the sets are "
                        f"{', '.join(METADATA_SETS)}; fields are written "
                        "set:Field, such as exif:Model)")
        if not field_valid(cur, name):
            return [], (f"unknown {cur} field {name} (names are "
                        f"{_FIELD_HELP[cur]})")
        keys.append(f"{cur}:{name}")
    if len(set(keys)) != len(keys):
        return [], f"list each metadata set once, separated by commas — '{scope}'"
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if _keys_overlap(a, b):
                return [], (f"{a} already keeps {b} — name the whole set or its "
                            "fields, not both")
    return keys, None


def _line_reason(trailing: str, stanza: str | None
                 ) -> tuple["Provenance | None", str | None, str | None]:
    """`(provenance, reason, problem)` for one manifest line's two comment
    places. Who and when may sit in either; they are never the reason, so a
    note holding only them leaves the reason to the stanza above, and a
    stanza holding only them is no reason at all. A bare `#` stanza still
    counts as a reasoned block, as it always has for `.leakscanignore`."""
    prov, t_rest, bad = split_provenance(trailing)
    s_prov, s_rest = None, stanza
    if bad is None and stanza is not None:
        s_prov, s_rest, bad = split_provenance(stanza)
    if bad:
        return None, None, bad
    if t_rest:
        reason: str | None = t_rest
    elif stanza is not None and (s_rest or stanza == ""):
        reason = s_rest
    else:
        reason = None
    return prov or s_prov, reason, None


def _escapes_root(path: str) -> bool:
    """A path no repo-relative file can have: absolute, or climbing out with
    `..` (160/980 GM6). Such a line could match nothing, and the stale-entry
    check only sees paths under a scanned tree, so it would sit in the
    inventory unremarked."""
    return Path(path).is_absolute() or path.startswith("/") \
        or ".." in Path(path).parts


def load_binary_manifest(root: Path, source: Path | None = None
                         ) -> dict[str, BinaryEntry]:
    """Entries from `<root>/.leakscanbinaries`, keyed by repo-relative path.
    Every problem is collected and raised together as `BinaryManifestError`:
    an unreasoned line, a malformed line, an unknown or comma-joined set, a
    path or a set listed twice (or one that is absolute or climbs out with
    `..`), a set line with no file line for its path or with a different
    digest, a who/when that does not read. An absent file is no entries.
    `source` reads another copy of the manifest, for the staged plane's index
    copy (GM12)."""
    files: dict[str, tuple[str, str, int, Provenance | None]] = {}
    set_lines: list[tuple[int, str, str, tuple, str, Provenance | None]] = []
    problems: list[str] = []
    for n, body, trailing, stanza in allowmarker.read_reasoned_parts(
            source or root / BINARY_MANIFEST):
        prov, reason, bad = _line_reason(trailing, stanza)
        if bad:
            problems.append(f"line {n}: {bad}")
            continue
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
        names: list[str] = []
        if scope:
            names, bad = parse_scope(scope)
            if bad:
                problems.append(f"line {n}: {bad}")
                continue
        path = m.group("path").strip()
        path = path[2:] if path.startswith("./") else path
        if _escapes_root(path):
            problems.append(f"line {n}: '{path}' is not a path inside the repo "
                            "(absolute, or climbing out with '..'): it can match "
                            "no file")
            continue
        if reason is None:
            what = f"keeping {scope} in '{path}'" if scope else f"'{path}'"
            problems.append(f"line {n}: {what} has no stated reason")
            continue
        digest = m.group("digest").lower()
        if scope:
            set_lines.append((n, path, digest, tuple(names), reason, prov))
        elif path in files:
            problems.append(f"line {n}: '{path}' already listed at line "
                            f"{files[path][2]}")
        else:
            files[path] = (digest, reason, n, prov)
    kept: dict[str, dict[str, KeptSet]] = {}
    for n, path, digest, group, reason, prov in set_lines:
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
        again = [x for x in group if any(_keys_overlap(x, k) for k in sets)]
        if again:
            first = next(k for k in sets if _keys_overlap(again[0], k))
            problems.append(f"line {n}: {', '.join(again)} in '{path}' already kept "
                            f"at line {sets[first].lineno}")
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
            sets[name] = KeptSet(name, reason, n, prov)
    if problems:
        raise BinaryManifestError(
            f"{BINARY_MANIFEST}: {len(problems)} problem(s) — {'; '.join(problems)}. "
            "Every accepted binary, and every metadata set it keeps, states its "
            "reason where a reviewer reads it (method/GUARDS.md): a comment above "
            "the stanza, or a trailing '# reason' on the line.")
    return {path: BinaryEntry(path, d, reason, n, kept.get(path, {}), prov)
            for path, (d, reason, n, prov) in files.items()}


def provenance_gaps(manifest: dict[str, BinaryEntry]) -> list[Finding]:
    """One warning per manifest LINE that records no who/when (160/980 GM5):
    a line written before the form existed. Never a block, and never silent —
    a reason alone is not what the principal asked for (2026-10-03), but an
    old line must not break a child that was told, on 2026-10-18, it would not
    go red today. Sorted by line; a set line naming several sets is one."""
    gaps: dict[int, Finding] = {}
    for e in manifest.values():
        if e.prov is None:
            gaps[e.lineno] = Finding(BINARY_MANIFEST, e.lineno, PROVENANCE_RULE,
                                     "binary", "high", f"{e.path}: file line")
        for k in e.sets.values():
            if k.prov is None and k.lineno not in gaps:
                gaps[k.lineno] = Finding(BINARY_MANIFEST, k.lineno, PROVENANCE_RULE,
                                         "binary", "high",
                                         f"{e.path}: keeps {k.name}")
    return [gaps[n] for n in sorted(gaps)]


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


# --- G3 field level (020/450): Exif and GPS tags read by name ---------------
#
# Mike, 2026-10-19, on 020/440: "I did mean fields as in GPS versus the camera
# model. Things like exif, iptc, xmp are data types, nto fields." An Exif block
# is a TIFF structure: a header, then image file directories (IFDs) of
# `tag, type, count, value` entries. This reads the TAG NUMBERS only (never a
# value), names each from the Exif / TIFF / GPS specifications, and reports
# `exif:<TagName>` or `gps:<TagName>`. A tag the table does not name is
# reported by its number (`exif:0x9999`) so an entry can still keep it
# explicitly. What cannot be walked at all (a short header, an offset outside
# the block, a loop, too many entries) is `exif:unknown`: it blocks unless
# named, exactly as `unknown` does at the type level.
#
# The values are not read: the entry keeps a field, and the human who writes
# its reason has looked at the value in the file. The pointers that only lead
# to another IFD (Exif, GPS, Interop) are followed and not reported.
EXIF_TAGS = {
    0x00FE: "NewSubfileType", 0x0100: "ImageWidth", 0x0101: "ImageLength",
    0x0102: "BitsPerSample", 0x0103: "Compression",
    0x0106: "PhotometricInterpretation", 0x010E: "ImageDescription",
    0x010F: "Make", 0x0110: "Model", 0x0111: "StripOffsets",
    0x0112: "Orientation", 0x0115: "SamplesPerPixel", 0x0116: "RowsPerStrip",
    0x0117: "StripByteCounts", 0x011A: "XResolution", 0x011B: "YResolution",
    0x011C: "PlanarConfiguration", 0x0128: "ResolutionUnit",
    0x012D: "TransferFunction", 0x0131: "Software", 0x0132: "DateTime",
    0x013B: "Artist", 0x013E: "WhitePoint", 0x013F: "PrimaryChromaticities",
    0x0201: "JPEGInterchangeFormat", 0x0202: "JPEGInterchangeFormatLength",
    0x0211: "YCbCrCoefficients", 0x0212: "YCbCrSubSampling",
    0x0213: "YCbCrPositioning", 0x0214: "ReferenceBlackWhite",
    0x8298: "Copyright",
    0x829A: "ExposureTime", 0x829D: "FNumber", 0x8822: "ExposureProgram",
    0x8824: "SpectralSensitivity", 0x8827: "ISOSpeedRatings",
    0x8828: "OECF", 0x8830: "SensitivityType",
    0x8831: "StandardOutputSensitivity", 0x8832: "RecommendedExposureIndex",
    0x8833: "ISOSpeed", 0x9000: "ExifVersion", 0x9003: "DateTimeOriginal",
    0x9004: "DateTimeDigitized", 0x9010: "OffsetTime",
    0x9011: "OffsetTimeOriginal", 0x9012: "OffsetTimeDigitized",
    0x9101: "ComponentsConfiguration", 0x9102: "CompressedBitsPerPixel",
    0x9201: "ShutterSpeedValue", 0x9202: "ApertureValue",
    0x9203: "BrightnessValue", 0x9204: "ExposureBiasValue",
    0x9205: "MaxApertureValue", 0x9206: "SubjectDistance",
    0x9207: "MeteringMode", 0x9208: "LightSource", 0x9209: "Flash",
    0x920A: "FocalLength", 0x9214: "SubjectArea", 0x927C: "MakerNote",
    0x9286: "UserComment", 0x9290: "SubSecTime",
    0x9291: "SubSecTimeOriginal", 0x9292: "SubSecTimeDigitized",
    0xA000: "FlashpixVersion", 0xA001: "ColorSpace",
    0xA002: "PixelXDimension", 0xA003: "PixelYDimension",
    0xA004: "RelatedSoundFile", 0xA20B: "FlashEnergy",
    0xA20C: "SpatialFrequencyResponse", 0xA20E: "FocalPlaneXResolution",
    0xA20F: "FocalPlaneYResolution", 0xA210: "FocalPlaneResolutionUnit",
    0xA214: "SubjectLocation", 0xA215: "ExposureIndex",
    0xA217: "SensingMethod", 0xA300: "FileSource", 0xA301: "SceneType",
    0xA302: "CFAPattern", 0xA401: "CustomRendered", 0xA402: "ExposureMode",
    0xA403: "WhiteBalance", 0xA404: "DigitalZoomRatio",
    0xA405: "FocalLengthIn35mmFilm", 0xA406: "SceneCaptureType",
    0xA407: "GainControl", 0xA408: "Contrast", 0xA409: "Saturation",
    0xA40A: "Sharpness", 0xA40B: "DeviceSettingDescription",
    0xA40C: "SubjectDistanceRange", 0xA420: "ImageUniqueID",
    0xA430: "CameraOwnerName", 0xA431: "BodySerialNumber",
    0xA432: "LensSpecification", 0xA433: "LensMake", 0xA434: "LensModel",
    0xA435: "LensSerialNumber", 0xA460: "CompositeImage", 0xA500: "Gamma",
    # Interoperability IFD
    0x0001: "InteroperabilityIndex", 0x0002: "InteroperabilityVersion",
}
GPS_TAGS = {
    0x00: "GPSVersionID", 0x01: "GPSLatitudeRef", 0x02: "GPSLatitude",
    0x03: "GPSLongitudeRef", 0x04: "GPSLongitude", 0x05: "GPSAltitudeRef",
    0x06: "GPSAltitude", 0x07: "GPSTimeStamp", 0x08: "GPSSatellites",
    0x09: "GPSStatus", 0x0A: "GPSMeasureMode", 0x0B: "GPSDOP",
    0x0C: "GPSSpeedRef", 0x0D: "GPSSpeed", 0x0E: "GPSTrackRef",
    0x0F: "GPSTrack", 0x10: "GPSImgDirectionRef", 0x11: "GPSImgDirection",
    0x12: "GPSMapDatum", 0x13: "GPSDestLatitudeRef",
    0x14: "GPSDestLatitude", 0x15: "GPSDestLongitudeRef",
    0x16: "GPSDestLongitude", 0x17: "GPSDestBearingRef",
    0x18: "GPSDestBearing", 0x19: "GPSDestDistanceRef",
    0x1A: "GPSDestDistance", 0x1B: "GPSProcessingMethod",
    0x1C: "GPSAreaInformation", 0x1D: "GPSDateStamp",
    0x1E: "GPSDifferential", 0x1F: "GPSHPositioningError",
}
# Field names by field set: the vocabulary an entry may use after `exif:` or
# `gps:`. `unknown` is the parse-failure field and lives in `exif` only.
FIELD_NAMES = {
    "exif": frozenset(EXIF_TAGS.values()) | {"unknown"},
    "gps": frozenset(GPS_TAGS.values()),
}
# Every set whose fields are read; `field_valid` knows each one's vocabulary.
FIELD_SETS = ("exif", "gps", "iptc", "xmp", "png-text")
_EXIF_POINTERS = {0x8769: "exif", 0x8825: "gps", 0xA005: "exif"}
_EXIF_MAX_IFDS = 16          # IFDs walked in one block (a real one has 3-5)
_EXIF_MAX_ENTRIES = 1024     # entries read from ONE IFD (the count is a u16)
_HEX_TAG_RX = re.compile(r"^0x[0-9A-F]{4}$")


def exif_fields(blob: bytes) -> list[str]:
    """The field keys (`exif:Model`, `gps:GPSLatitude`, `exif:0x9999`) an Exif
    block carries, sorted; `exif:unknown` is added when any part of the block
    could not be walked. Reads tag numbers only, every offset and count
    bounded by the block's own length, so a hostile block costs a bounded
    number of reads and never an unbounded one."""
    keys: set[str] = set()
    if blob.startswith(b"Exif\x00\x00"):
        blob = blob[6:]
    if len(blob) < 8 or blob[:2] not in (b"II", b"MM"):
        return ["exif:unknown"]
    e = "<" if blob[:2] == b"II" else ">"
    if struct.unpack(e + "H", blob[2:4])[0] != 42:
        return ["exif:unknown"]
    todo = [(struct.unpack(e + "I", blob[4:8])[0], "exif", True)]
    seen: set[int] = set()
    ok = True
    while todo:
        off, kind, chain = todo.pop()
        if off in seen:             # a shared or looping pointer: walked once
            continue
        if len(seen) >= _EXIF_MAX_IFDS:
            ok = False
            continue
        seen.add(off)
        if off + 2 > len(blob):
            ok = False
            continue
        n = struct.unpack(e + "H", blob[off:off + 2])[0]
        if n > _EXIF_MAX_ENTRIES or off + 2 + 12 * n + 4 > len(blob):
            ok = False
            n = min(n, _EXIF_MAX_ENTRIES, (len(blob) - off - 2) // 12)
        for i in range(n):
            at = off + 2 + 12 * i
            tag = struct.unpack(e + "H", blob[at:at + 2])[0]
            if tag in _EXIF_POINTERS and kind != "gps":
                ptr = struct.unpack(e + "I", blob[at + 8:at + 12])[0]
                todo.append((ptr, _EXIF_POINTERS[tag], False))
                continue
            table, prefix = (GPS_TAGS, "gps") if kind == "gps" else (EXIF_TAGS, "exif")
            keys.add(f"{prefix}:" + table.get(tag, f"0x{tag:04X}"))
        if chain and off + 2 + 12 * n + 4 <= len(blob):
            nxt = struct.unpack(e + "I", blob[off + 2 + 12 * n:off + 6 + 12 * n])[0]
            if nxt:
                todo.append((nxt, "exif", True))
    if not ok:
        keys.add("exif:unknown")
    return sorted(keys)


# --- G3 field level (020/450 part 2): IPTC, XMP and PNG text, by name -------
#
# The same rule as Exif: Mike's "things like exif, iptc, xmp are data types,
# nto fields". Names only, never values, in every output.
#
#   iptc:<dataset>   the IPTC IIM dataset names of the Photoshop 8BIM resource
#                    0x0404 (`iptc:By-line`, `iptc:City`). A dataset the table
#                    does not name is `iptc:<record>:<number>`
#                    (`iptc:2:999`); another Photoshop resource in the same
#                    APP13 is `iptc:8BIM-0x03ED`.
#   xmp:<prefix:property>   the top-level properties of the packet's
#                    rdf:Description elements (`xmp:dc:creator`,
#                    `xmp:exif:GPSLatitude`), attributes and child elements
#                    alike; a property's value, nested structure included, is
#                    one field. Well-known namespaces are spelled with their
#                    usual prefix whatever the packet declares.
#   png-text:<keyword>   the keyword of a tEXt / zTXt / iTXt chunk; a byte
#                    outside [A-Za-z0-9_.-] is %XX (`Creation%20Time`).
#
# `<set>:unknown` is what could not be walked (a block that fails to parse, a
# DOCTYPE or entity in a packet, a structure outside the RDF skeleton, too many
# fields, an overlong keyword). It blocks until named, as `exif:unknown` does.
_FIELDS_PER_SET_CAP = 1024    # distinct fields kept per set; past it, unknown
_IPTC_MAX_DATASETS = 4096
_IPTC_MAX_RESOURCES = 1024
IPTC_DATASETS = {
    (1, 0): "ModelVersion", (1, 5): "Destination", (1, 20): "FileFormat",
    (1, 22): "FileFormatVersion", (1, 30): "ServiceIdentifier",
    (1, 40): "EnvelopeNumber", (1, 50): "ProductID",
    (1, 60): "EnvelopePriority", (1, 70): "DateSent", (1, 80): "TimeSent",
    (1, 90): "CodedCharacterSet", (1, 100): "UniqueObjectName",
    (1, 120): "ARMIdentifier", (1, 122): "ARMVersion",
    (2, 0): "RecordVersion", (2, 3): "ObjectTypeReference",
    (2, 4): "ObjectAttributeReference", (2, 5): "ObjectName",
    (2, 7): "EditStatus", (2, 8): "EditorialUpdate", (2, 10): "Urgency",
    (2, 12): "SubjectReference", (2, 15): "Category",
    (2, 20): "SupplementalCategories", (2, 22): "FixtureIdentifier",
    (2, 25): "Keywords", (2, 26): "ContentLocationCode",
    (2, 27): "ContentLocationName", (2, 30): "ReleaseDate",
    (2, 35): "ReleaseTime", (2, 37): "ExpirationDate",
    (2, 38): "ExpirationTime", (2, 40): "SpecialInstructions",
    (2, 42): "ActionAdvised", (2, 45): "ReferenceService",
    (2, 47): "ReferenceDate", (2, 50): "ReferenceNumber",
    (2, 55): "DateCreated", (2, 60): "TimeCreated",
    (2, 62): "DigitalCreationDate", (2, 63): "DigitalCreationTime",
    (2, 65): "OriginatingProgram", (2, 70): "ProgramVersion",
    (2, 75): "ObjectCycle", (2, 80): "By-line", (2, 85): "By-lineTitle",
    (2, 90): "City", (2, 92): "Sub-location", (2, 95): "Province-State",
    (2, 100): "Country-PrimaryLocationCode",
    (2, 101): "Country-PrimaryLocationName",
    (2, 103): "OriginalTransmissionReference", (2, 105): "Headline",
    (2, 110): "Credit", (2, 115): "Source", (2, 116): "CopyrightNotice",
    (2, 118): "Contact", (2, 120): "Caption-Abstract",
    (2, 122): "Writer-Editor", (2, 125): "RasterizedCaption",
    (2, 130): "ImageType", (2, 131): "ImageOrientation",
    (2, 135): "LanguageIdentifier", (2, 150): "AudioType",
    (2, 151): "AudioSamplingRate", (2, 152): "AudioSamplingResolution",
    (2, 153): "AudioDuration", (2, 154): "AudioOutcue", (2, 184): "JobID",
    (2, 185): "MasterDocumentID", (2, 186): "ShortDocumentID",
    (2, 187): "UniqueDocumentID", (2, 188): "OwnerID",
    (2, 200): "ObjectPreviewFileFormat", (2, 201): "ObjectPreviewFileVersion",
    (2, 202): "ObjectPreviewData", (2, 221): "Prefs",
    (2, 225): "ClassifyState", (2, 228): "SimilarityIndex",
    (2, 230): "DocumentNotes", (2, 231): "DocumentHistory",
    (2, 232): "ExifCameraInfo", (2, 255): "CatalogSets",
}
_IPTC_NAMES = frozenset(IPTC_DATASETS.values())
_IPTC_NUM_RX = re.compile(r"^[0-9]:[0-9]{3}$")
_IPTC_RES_RX = re.compile(r"^8BIM-0x[0-9A-F]{4}$")


def _iptc_iim(data: bytes, keys: set) -> bool:
    """IIM datasets in `data` (tag marker 0x1C, record, dataset, length,
    value) added to `keys` by name; False if they cannot be walked. Lengths
    are read, values never."""
    pos, n = 0, len(data)
    count = 0
    while pos < n:
        if data[pos] == 0 and not any(data[pos:]):   # trailing padding
            return True
        if data[pos] != 0x1C or pos + 5 > n:
            return False
        rec, ds = data[pos + 1], data[pos + 2]
        ln = struct.unpack(">H", data[pos + 3:pos + 5])[0]
        pos += 5
        if ln & 0x8000:                  # extended: the length is `ln` bytes long
            ll = ln & 0x7FFF
            if ll > 4 or pos + ll > n:
                return False
            ln = int.from_bytes(data[pos:pos + ll], "big")
            pos += ll
        if rec == 0 or rec > 9 or pos + ln > n:
            return False
        pos += ln
        count += 1
        if count > _IPTC_MAX_DATASETS:
            return False
        keys.add("iptc:" + IPTC_DATASETS.get((rec, ds), f"{rec}:{ds:03d}"))
    return True


def iptc_fields(blob: bytes) -> list[str]:
    """The field keys (`iptc:By-line`, `iptc:2:999`, `iptc:8BIM-0x03ED`) an
    APP13 / ImageMagick IPTC profile carries, sorted; `iptc:unknown` is added
    when any part cannot be walked. `blob` is a Photoshop 3.0 header and 8BIM
    resources, bare 8BIM resources, or bare IIM datasets."""
    keys: set[str] = set()
    ok = True
    if blob.startswith(b"Photoshop 3.0\x00"):
        pos = 14
    elif blob.startswith(b"8BIM"):
        pos = 0
    elif blob[:1] == b"\x1c":
        ok = _iptc_iim(blob, keys)
        pos = len(blob)
    else:
        return ["iptc:unknown"]
    seen = 0
    while ok and pos < len(blob):
        if blob[pos:pos + 4] != b"8BIM" or pos + 7 > len(blob):
            ok = False
            break
        rid = struct.unpack(">H", blob[pos + 4:pos + 6])[0]
        name_len = 1 + blob[pos + 6]
        at = pos + 6 + name_len + (name_len & 1)
        if at + 4 > len(blob):
            ok = False
            break
        size = struct.unpack(">I", blob[at:at + 4])[0]
        at += 4
        if at + size > len(blob):
            ok = False
            break
        if rid == 0x0404:
            ok = _iptc_iim(blob[at:at + size], keys)
        else:
            keys.add(f"iptc:8BIM-0x{rid:04X}")
        pos = at + size + (size & 1)
        seen += 1
        if seen > _IPTC_MAX_RESOURCES:
            ok = False
    if not ok:
        keys.add("iptc:unknown")
    return sorted(keys)


_RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
_XML_NS = "http://www.w3.org/XML/1998/namespace"
_XMPMETA_NS = "adobe:ns:meta/"
_XMP_PREFIXES = {
    "http://purl.org/dc/elements/1.1/": "dc",
    "http://ns.adobe.com/xap/1.0/": "xmp",
    "http://ns.adobe.com/xap/1.0/rights/": "xmpRights",
    "http://ns.adobe.com/xap/1.0/mm/": "xmpMM",
    "http://ns.adobe.com/xap/1.0/bj/": "xmpBJ",
    "http://ns.adobe.com/xap/1.0/t/pg/": "xmpTPg",
    "http://ns.adobe.com/xmp/note/": "xmpNote",
    "http://ns.adobe.com/photoshop/1.0/": "photoshop",
    "http://ns.adobe.com/exif/1.0/": "exif",
    "http://ns.adobe.com/exif/1.0/aux/": "aux",
    "http://ns.adobe.com/tiff/1.0/": "tiff",
    "http://ns.adobe.com/pdf/1.3/": "pdf",
    "http://ns.adobe.com/camera-raw-settings/1.0/": "crs",
    "http://ns.adobe.com/lightroom/1.0/": "lr",
    "http://iptc.org/std/Iptc4xmpCore/1.0/xmlns/": "Iptc4xmpCore",
    "http://iptc.org/std/Iptc4xmpExt/2008-02-29/": "Iptc4xmpExt",
    "http://ns.microsoft.com/photo/1.0/": "MicrosoftPhoto",
    _RDF_NS: "rdf",
}
_NCNAME = r"[A-Za-z_][A-Za-z0-9_.-]{0,63}"
_XMP_FIELD_RX = re.compile(rf"^{_NCNAME}:{_NCNAME}$")
_XMP_MAX_PROPERTIES = 1024


class _XmpUnwalkable(Exception):
    pass


def xmp_fields(data: bytes) -> list[str]:
    """The field keys (`xmp:dc:creator`) an XMP packet carries, sorted, or
    `["xmp:unknown"]` when it cannot be read with confidence. Parsed by expat
    from the standard library as a stream of start tags, never a tree: a
    DOCTYPE, an entity declaration, an element outside the
    xmpmeta / RDF / Description skeleton, an unqualified or unprefixable name,
    or more than 1,024 properties is `unknown`. Element text is never kept."""
    keys: set[str] = set()
    roles: list[str] = []
    declared: dict[str, str] = {}
    seen_rdf = False

    def fail(*_a):
        raise _XmpUnwalkable

    def key_of(qname: str) -> str:
        uri, _, local = qname.rpartition(" ")
        prefix = _XMP_PREFIXES.get(uri) or declared.get(uri)
        if not uri or not prefix:
            fail()
        k = f"{prefix}:{local}"
        if not _XMP_FIELD_RX.match(k):
            fail()
        return k

    def start(qname, attrs):
        nonlocal seen_rdf
        uri, _, local = qname.rpartition(" ")
        parent = roles[-1] if roles else None
        if parent is None:
            if (uri, local) == (_XMPMETA_NS, "xmpmeta"):
                role = "meta"
            elif (uri, local) == (_RDF_NS, "RDF"):
                role = "rdf"
                seen_rdf = True
            else:
                fail()
        elif parent == "meta":
            if (uri, local) != (_RDF_NS, "RDF"):
                fail()
            role = "rdf"
            seen_rdf = True
        elif parent == "rdf":
            if (uri, local) != (_RDF_NS, "Description"):
                fail()
            role = "desc"
            for a in attrs:
                auri, _, alocal = a.rpartition(" ")
                if auri in (_RDF_NS, _XML_NS):
                    continue                   # rdf:about, xml:lang: not properties
                keys.add("xmp:" + key_of(a))
        elif parent == "desc":
            role = "prop"
            keys.add("xmp:" + key_of(qname))
        else:                                  # inside a property's value
            role = "inner"
        if len(keys) > _XMP_MAX_PROPERTIES:
            fail()
        roles.append(role)

    p = _expat.ParserCreate("utf-8", " ")
    p.SetParamEntityParsing(_expat.XML_PARAM_ENTITY_PARSING_NEVER)
    p.StartDoctypeDeclHandler = fail
    p.EntityDeclHandler = fail
    p.StartNamespaceDeclHandler = lambda pre, uri: declared.setdefault(uri, pre) if pre else None
    p.StartElementHandler = start
    p.EndElementHandler = lambda _n: roles.pop()
    try:
        p.Parse(data, True)
    except (_XmpUnwalkable, _expat.ExpatError):
        return ["xmp:unknown"]
    if not seen_rdf:
        return ["xmp:unknown"]
    return sorted(keys)


_PNG_KEYWORD_OK = frozenset(b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                            b"0123456789_.-")
_PNG_KEYWORD_RX = re.compile(r"^(?:[A-Za-z0-9_.-]|%[0-9A-F]{2}){1,237}$")


def png_text_field(keyword: bytes) -> str:
    """The field key for a PNG text chunk keyword: percent-encoded outside
    `[A-Za-z0-9_.-]`, so it is one token in the manifest; a keyword outside
    the PNG limit (1 to 79 bytes) is `png-text:unknown`, and a keyword that is
    itself `unknown` is written `%75nknown` so the two cannot be confused."""
    if not 1 <= len(keyword) <= 79:
        return "png-text:unknown"
    if keyword == b"unknown":
        return "png-text:%75nknown"
    return "png-text:" + "".join(chr(b) if b in _PNG_KEYWORD_OK else f"%{b:02X}"
                                 for b in keyword)


def field_valid(field_set: str, name: str) -> bool:
    """Is `name` something an entry may use after `<field_set>:`? Exif and
    GPS: a named tag, `unknown` (exif only), or a tag number spelled `0x` and
    four upper-case hex digits. IPTC: a dataset name, `<record>:<number>`,
    `8BIM-0x....` or `unknown`. XMP: `<prefix>:<Property>` or `unknown`.
    PNG text: a percent-encoded keyword or `unknown`."""
    if field_set in ("exif", "gps"):
        return (name in FIELD_NAMES.get(field_set, ())
                or bool(_HEX_TAG_RX.match(name)))
    if name == "unknown":
        return field_set in ("iptc", "xmp", "png-text")
    if field_set == "iptc":
        return (name in _IPTC_NAMES or bool(_IPTC_NUM_RX.match(name))
                or bool(_IPTC_RES_RX.match(name)))
    if field_set == "xmp":
        return bool(_XMP_FIELD_RX.match(name))
    if field_set == "png-text":
        return bool(_PNG_KEYWORD_RX.match(name))
    return False


_FIELD_HELP = {
    "exif": "the Exif / GPS tag names, such as exif:Model or gps:GPSLatitude, or "
            "a tag number as 0x9999",
    "iptc": "the IPTC dataset names, such as iptc:By-line or iptc:City, or "
            "<record>:<number> as 2:999",
    "xmp": "<prefix>:<Property>, each written in full, such as xmp:dc:creator",
    "png-text": "the chunk keyword, spaces and punctuation as %XX, such as "
                "png-text:Creation%20Time",
}
_FIELD_HELP["gps"] = _FIELD_HELP["exif"]


# The walkers append `(set, label)` to `found` for every metadata segment they
# meet, and `(label, text)` to `texts` for every one they can read as text. A
# set whose fields are read (Exif, IPTC, XMP, PNG text: 020/450) also appends
# `(set, label, keys)` to `fields`, `keys` being the field keys that segment
# carries; every `found` entry of such a set has one.
_XMP_KEYWORD = "XML:com.adobe.xmp"
_RAW_PROFILE_SETS = {"exif": "exif", "app1": "exif", "iptc": "iptc",
                     "8bim": "iptc", "xmp": "xmp", "icc": "icc", "icm": "icc"}


def _note_exif(label: str, blob: bytes | None, found: list, fields: list) -> None:
    """One Exif segment: the set, and its fields (`exif:unknown` when the
    block is absent from the read: past the cap or undecodable)."""
    found.append(("exif", label))
    fields.append(("exif", label,
                   exif_fields(blob) if blob is not None else ["exif:unknown"]))


def _note_iptc(label: str, blob: bytes | None, found: list, fields: list) -> None:
    """One IPTC segment: the set, and its fields (`iptc:unknown` when the
    block is absent from the read or cannot be walked)."""
    found.append(("iptc", label))
    fields.append(("iptc", label,
                   iptc_fields(blob) if blob is not None else ["iptc:unknown"]))


def _note_xmp(label: str, blob: bytes | None, found: list, fields: list) -> None:
    """One XMP packet: the set, and its properties (`xmp:unknown` when the
    packet is absent from the read or does not parse)."""
    found.append(("xmp", label))
    fields.append(("xmp", label,
                   xmp_fields(blob) if blob is not None else ["xmp:unknown"]))


def _png_metadata(fh, size: int, texts: list, found: list, fields: list) -> None:
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
            _note_exif("PNG eXIf", fh.read(n) if n <= META_SEGMENT_CAP else None,
                       found, fields)
        elif ctype == "iCCP":
            found.append(("icc", "PNG iCCP"))
        elif ctype in ("tEXt", "zTXt", "iTXt"):
            if n > META_SEGMENT_CAP:
                found.append(("unknown", f"PNG {ctype} past the "
                                         f"{META_SEGMENT_CAP}-byte cap"))
            else:
                _png_text_chunk(ctype, fh.read(n), texts, found, fields)
        pos += 12 + n


def _png_text_decode(ctype: str, rest: bytes) -> str | None:
    """The text of a tEXt / zTXt / iTXt chunk body (after its keyword), or
    None when it is truncated, undecodable or inflates past the cap."""
    if ctype == "tEXt":
        return rest.decode("latin-1")
    if ctype == "zTXt":
        raw = _inflate(rest[1:])
        return None if raw is None else raw.decode("latin-1")
    # iTXt: flag, method, language\0, translated keyword\0, text
    if len(rest) < 2:
        return None
    compressed = rest[0] == 1
    _lang, _, rest2 = rest[2:].partition(b"\x00")
    _tkw, _, body = rest2.partition(b"\x00")
    if compressed:
        body = _inflate(body)
        if body is None:
            return None
    return body.decode("utf-8", errors="replace")


def _raw_profile_bytes(value: str) -> bytes | None:
    """The binary profile inside ImageMagick's text form: a blank line, the
    profile name, the byte count, then the bytes as hex. None if it does not
    decode."""
    lines = value.split("\n")
    try:
        return bytes.fromhex("".join("".join(lines[3:]).split()))
    except ValueError:
        return None


def _png_text_chunk(ctype: str, data: bytes, texts: list, found: list,
                    fields: list) -> None:
    keyword, _, rest = data.partition(b"\x00")
    kw = keyword.decode("latin-1")
    label = f"PNG {ctype} '{kw}'"
    if kw.lower().startswith("raw profile type"):
        # ImageMagick carries Exif/IPTC/8BIM here as a hex dump of the binary
        # profile: text-shaped, but nothing a text rule can read.
        kind = kw.lower()[len("raw profile type"):].strip()
        what = f"{label} (hex-encoded binary profile)"
        kept = _RAW_PROFILE_SETS.get(kind, "unknown")
        if kept in ("exif", "iptc", "xmp"):
            raw = _png_text_decode(ctype, rest)
            blob = _raw_profile_bytes(raw) if raw is not None else None
            if blob is None:
                # Never clean (160/980 GM4): a profile the gate cannot decode
                # is reported as UNREADABLE, and blocks as `<set>:unknown`.
                what = f"{label} (hex-encoded binary profile, UNREADABLE: does not decode)"
            {"exif": _note_exif, "iptc": _note_iptc, "xmp": _note_xmp}[kept](
                what, blob, found, fields)
            if kept == "xmp" and blob is not None:
                # The packet is text: scan it like every other XMP form, kept
                # or not. This was the one XMP shape the text rules never saw.
                texts.append((what, blob.decode("utf-8", errors="replace")))
        else:
            found.append((kept, what))
        return
    set_name = "xmp" if kw == _XMP_KEYWORD else "png-text"
    value = _png_text_decode(ctype, rest)
    if value is None:
        found.append(("unknown", f"{label} (undecodable, truncated or past the cap)"))
        return
    if set_name == "xmp":
        _note_xmp(label, value.encode("utf-8"), found, fields)
    else:
        found.append((set_name, label))
        fields.append((set_name, label, [png_text_field(keyword)]))
    texts.append((label, f"{kw}: {value}"))


_XMP_NS = b"http://ns.adobe.com/xap/1.0/\x00"
_XMP_EXT_NS = b"http://ns.adobe.com/xmp/extension/\x00"
_ICC_TAG = b"ICC_PROFILE\x00"


def _jpeg_metadata(fh, size: int, texts: list, found: list, fields: list) -> None:
    # Extended XMP arrives in numbered pieces that are only well-formed once
    # joined, so the pieces are gathered per GUID and read once at the end.
    # `ext["total"]` bounds what is held: past the cap the pieces are dropped
    # and the packet reads as unknown.
    ext: dict = {"pieces": {}, "total": 0, "bad": False}
    try:
        _jpeg_walk(fh, size, texts, found, fields, ext)
    finally:
        if ext["bad"]:
            fields.append(("xmp", "JPEG extended XMP", ["xmp:unknown"]))
        for pieces in ext["pieces"].values():
            fields.append(("xmp", "JPEG extended XMP",
                           xmp_fields(b"".join(b for _o, b in sorted(pieces)))))


def _jpeg_walk(fh, size: int, texts: list, found: list, fields: list,
               ext: dict) -> None:
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
                _note_iptc("JPEG APP13 (IPTC/Photoshop)", seg, found, fields)
            elif marker == 0xE2:
                if seg.startswith(_ICC_TAG):
                    found.append(("icc", "JPEG APP2 ICC_PROFILE"))
                # other APP2 payloads (FlashPix, MPF) are outside the walk
            elif seg.startswith(b"Exif\x00"):
                _note_exif("JPEG APP1 Exif", seg, found, fields)
            elif seg.startswith(_XMP_NS):
                _note_xmp("JPEG XMP", seg[len(_XMP_NS):], found, fields)
                texts.append(("JPEG XMP", seg[len(_XMP_NS):].decode("utf-8", errors="replace")))
            elif seg.startswith(_XMP_EXT_NS):
                # 32-byte GUID + 4-byte full length + 4-byte offset, then XML
                body = seg[len(_XMP_EXT_NS) + 40:]
                found.append(("xmp", "JPEG extended XMP"))
                head = len(_XMP_EXT_NS)
                ext["total"] += len(seg)
                if len(seg) < head + 40 or ext["total"] > META_SEGMENT_CAP:
                    ext["bad"] = True           # short header, or past the cap
                    ext["pieces"].clear()
                elif not ext["bad"]:
                    off = struct.unpack(">I", seg[head + 36:head + 40])[0]
                    ext["pieces"].setdefault(seg[head:head + 32], []).append((off, body))
                texts.append(("JPEG extended XMP", body.decode("utf-8", errors="replace")))
            else:
                found.append(("unknown", "JPEG APP1 (unrecognised)"))
        pos += 2 + n


def _webp_metadata(fh, size: int, texts: list, found: list, fields: list) -> None:
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
            _note_exif("WebP EXIF", fh.read(n) if n <= META_SEGMENT_CAP else None,
                       found, fields)
        elif fourcc == "ICCP":
            found.append(("icc", "WebP ICCP"))
        elif fourcc == "XMP ":
            if n > META_SEGMENT_CAP:
                found.append(("unknown", f"WebP XMP past the {META_SEGMENT_CAP}-byte cap"))
            else:
                raw = fh.read(n)
                _note_xmp("WebP XMP", raw, found, fields)
                texts.append(("WebP XMP", raw.decode("utf-8", errors="replace")))
        pos += 8 + n + (n & 1)


def inspect_media(fh) -> tuple[str | None, list[tuple[str, str]], list[tuple[str, str]]]:
    """`inspect_media_fields` without the field detail: `(format, texts, found)`."""
    fmt, texts, found, _fields = inspect_media_fields(fh)
    return fmt, texts, found


def inspect_media_fields(fh) -> tuple[str | None, list, list, list]:
    """`(format, text segments, metadata found, fields)` for a PNG, JPEG or WebP
    file object; `(None, [], [])` for anything else. Text segments are
    `(label, decoded text)` to be scanned; metadata found is `(set, label)`
    for every segment, text or opaque, with `set` a key of `METADATA_SETS`.
    Every read is bounded (`META_SEGMENT_CAP`, or the format's own 64 KiB
    segment limit for JPEG), so peak memory is independent of the file's
    size. `fields` is `(set, label, keys)` per segment of a set whose fields are
    read (Exif and GPS so far, 020/450), `keys` like `exif:Model`."""
    fh.seek(0, os.SEEK_END)
    size = fh.tell()
    fh.seek(0)
    head = fh.read(12)
    texts: list[tuple[str, str]] = []
    found: list[tuple[str, str]] = []
    fields: list[tuple[str, str, list[str]]] = []
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        fmt, walker = "png", _png_metadata
    elif head.startswith(b"\xff\xd8"):
        fmt, walker = "jpeg", _jpeg_metadata
    elif head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        fmt, walker = "webp", _webp_metadata
    else:
        return None, texts, found, fields
    try:
        walker(fh, size, texts, found, fields)
    except struct.error:
        found.append(("unknown", f"{fmt.upper()} structure cannot be walked"))
    return fmt, texts, found, fields


def metadata_fields(fields: list) -> dict[str, list[str]]:
    """`fields` grouped by set: set -> sorted field keys across its segments.
    A set with more than `_FIELDS_PER_SET_CAP` distinct fields keeps the first
    ones in sorted order and gains `<set>:unknown`, so a file of thousands of
    chunks costs a bounded report, not an unbounded one."""
    out: dict[str, set[str]] = {}
    for name, _label, keys in fields:
        out.setdefault(name, set()).update(keys)
    done: dict[str, list[str]] = {}
    for name, keys in out.items():
        ordered = sorted(keys)
        if len(ordered) > _FIELDS_PER_SET_CAP:
            ordered = sorted(set(ordered[:_FIELDS_PER_SET_CAP]) | {f"{name}:unknown"})
        done[name] = ordered
    return done


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
            _fmt, texts, found, fields = inspect_media_fields(fh)
    except OSError as e:
        gate("binary-unlisted", f"unreadable ({e.__class__.__name__})")
        return findings
    for label, text in texts:
        for f in scan_text(rel, text, local_terms, disabled, tally, honour_markers=False):
            f.where = f"metadata {label}"
            findings.append(f)
    accepted = entry is not None and entry.matches(digest)
    present = metadata_sets(found)
    keys_by_set = metadata_fields(fields)
    for name, labels in present.items():
        keys = keys_by_set.get(name)
        whole = accepted and name in entry.sets
        if keys is None:                       # a set whose fields are not read
            if not whole:
                gate("binary-metadata", f"{name}: {'; '.join(labels)} — no line keeps it")
            continue
        if whole:                              # a type-level line (020/450)
            if in_type_level_grace():
                if tally is not None:
                    tally.type_level_warnings.append(Finding(
                        rel, 0, TYPE_LEVEL_RULE, "binary", "high",
                        f"{name} is kept as a whole type; it carries "
                        f"{', '.join(keys) or 'no fields'}", "binary"))
            else:
                gate("binary-metadata",
                     f"{name}: a type-level line no longer keeps it since "
                     f"{TYPE_LEVEL_UNTIL.isoformat()} — name its fields: "
                     f"{', '.join(keys) or 'it carries none'}")
            continue
        unkept = [k for k in keys if not (accepted and k in entry.sets)]
        if unkept:
            gate("binary-metadata",
                 f"{name}: {', '.join(unkept)} ({'; '.join(labels)}) — no line "
                 f"keeps {'it' if len(unkept) == 1 else 'them'}")
    if entry is None:
        twin = (by_digest or {}).get(digest[:MIN_DIGEST_HEX])
        hint = f" — same bytes as the entry for {twin}" if twin else ""
        gate("binary-unlisted", f"sha256 {digest[:PRINTED_DIGEST_HEX]}{hint}")
    elif not accepted:
        gate("binary-changed", f"listed {entry.digest[:PRINTED_DIGEST_HEX]}, "
                               f"now {digest[:PRINTED_DIGEST_HEX]} (line {entry.lineno})")
    else:
        every_field = {k for ks in keys_by_set.values() for k in ks}
        for name, kept in entry.sets.items():
            if name not in (every_field if ":" in name else present):
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
    return filewalk.walk_files(base, SKIP_DIR_NAMES,
                               read_tracked_under_skip=True)


def iter_files(paths: list[Path], root: Path, globs: list[str],
               tally: Tally | None = None):
    """Every file the ignore globs leave, as `(path, repo-relative path)`; the
    ones they skip are counted on `tally`."""
    for p, rel, ignored in iter_files_marked(paths, root, globs):
        if ignored:
            if tally is not None:
                tally.files_by_glob += 1
            continue
        yield p, rel


def iter_files_marked(paths: list[Path], root: Path, globs: list[str]):
    """As `iter_files` but ALSO the files the ignore globs skip, as
    `(path, repo-relative path, ignored)`. G3 runs before the ignore file for a
    binary (160/980 GM9), so the caller must see the ignored ones to gate
    them, and decide itself what a skip counts as."""
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
            yield p, rel, _ignored(rel, globs)


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
    except OSError as e:
        # A file that VANISHES mid-walk (a race with another process) is not
        # this scanner's failure to report. One that exists but cannot be read
        # is: re-raised, and `guarded_main` turns it into exit 2 - a broken
        # scan is not a pass (RT1, 160/730).
        if not report.is_vanished(e):
            raise
    return findings


def scan_paths(paths: list[Path], root: Path,
               local_terms: list[tuple[str, "re.Pattern[str]"]],
               disabled: frozenset[str] = frozenset(),
               tally: Tally | None = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    manifest = load_binary_manifest(root)
    if tally is not None:
        tally.provenance_warnings.extend(provenance_gaps(manifest))
    tracked = tracked_files(root)
    by_digest = _digest_index(manifest)
    findings: list[Finding] = []
    gated: set[str] = set()
    for p, rel, ignored in iter_files_marked(paths, root, globs):
        if ignored:
            # G3 runs BEFORE the ignore file for a binary (160/980 GM9): a
            # glob is path-wide and blind to content, so it cannot be the
            # hatch for a binary. A tracked binary under a glob is gated like
            # any other; everything else the glob skips stays skipped.
            if not _looks_binary_file(p) or (tracked is not None
                                             and rel not in tracked):
                if tally is not None:
                    tally.files_by_glob += 1
                continue
            gated.add(rel)
            findings.extend(check_binary(p, rel, manifest.get(rel), local_terms,
                                         disabled, tally, by_digest))
            continue
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
        if entry.path in gated or not _under_any(root / entry.path, paths):
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


def provenance_stub(today: datetime.date | None = None) -> str:
    """The who/when a printed line carries (160/980 GM5), so recording it costs
    the person nothing: the session id and today's UTC date, and `by=agent`
    when a Claude session prints it. Run by a person there is no session, and
    the kind of grant is theirs to state, so it prints `by=CHOOSE`, which the
    loader refuses until they write principal-ruled, principal-answer or
    agent. It is never a reason: a line holding only this is still unreasoned."""
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    on = (today or _utc_today()).isoformat()
    if sid and _SESSION_RX.match(sid):
        return f"by=agent session={sid} on={on}"
    return f"by=CHOOSE session=human on={on}"


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
    stub = provenance_stub()
    lines: list[str] = []
    notes: list[str] = []
    for p, rel, _ignored_by_glob in iter_files_marked(paths, root, globs):
        # An ignored binary is gated too (GM9), so its lines are listed.
        if not _looks_binary_file(p) or (tracked is not None and rel not in tracked):
            continue
        with open(p, "rb") as fh:
            digest = _sha256_file(fh)
            _fmt, _texts, found, fields = inspect_media_fields(fh)
        entry = manifest.get(rel)
        accepted = entry is not None and entry.matches(digest)
        present = metadata_sets(found)
        keys_by_set = metadata_fields(fields)
        # One line per thing still to keep: a set (no fields read), or a field.
        # A type-level line on a set whose fields are read is migrated: it is
        # replaced by the field lines, so every field is listed again.
        missing: list[str] = []
        migrating: list[str] = []
        for name in present:
            keys = keys_by_set.get(name)
            whole = accepted and name in entry.sets
            if keys is None:
                if not whole:
                    missing.append(name)
            elif whole:
                migrating.append(name)
                missing.extend(keys)
            else:
                missing.extend(k for k in keys if not (accepted and k in entry.sets))
        if accepted and not missing:
            continue
        if "#" in rel or "\n" in rel or rel != rel.strip() or rel.startswith("*"):
            notes.append(f"{rel!r}: this path cannot be written as an entry "
                         "(it holds '#', a newline, edge whitespace or a leading "
                         "'*') — rename the file")
            continue
        d = digest[:PRINTED_DIGEST_HEX]
        if not accepted:
            lines.append(f"{d}  {rel}  # {stub}")
            if entry is not None:
                notes.append(f"{rel}: changed since listed — replaces line "
                             f"{entry.lineno} and the set lines under it")
        lines.extend(f"{d}:{s}  {rel}  # {stub}" for s in missing)
        if missing:
            shown = [s for s in present if s in missing]
            notes.append(f"{rel}: carries metadata set(s) "
                         + ", ".join(f"{s} ({'; '.join(present[s])})" for s in shown)
                         + (", and fields " + ", ".join(k for k in missing if ":" in k)
                            if any(":" in k for k in missing) else "")
                         + " — strip every set or field you have no need for (that "
                         "changes the bytes: re-run this), and keep one only with "
                         "its own need as the reason; fields that share one need "
                         "may share a line, written "
                         f"{d}:exif:Model,LensModel  {rel}")
        for name in migrating:
            notes.append(f"{rel}: the type-level line for {name} (line "
                         f"{entry.sets[name].lineno}) is replaced by the field "
                         "lines above; it is accepted with a warning until "
                         f"{TYPE_LEVEL_UNTIL.isoformat()}")
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


def _staged_manifest(root: Path, dest: Path) -> dict[str, BinaryEntry]:
    """The manifest as the commit will hold it (160/980 GM12): the INDEX copy,
    and none when the index holds none, whatever the working tree says. Like
    the ignore file the hook read the working tree before; unlike it, this
    file holds the entries that excuse a binary, so the hook and CI must judge
    the same bytes. A working copy that differs from the staged one is said so
    on stderr, because the verdict is then not the one the person is looking
    at."""
    r = subprocess.run(["git", "ls-files", "--stage", "--", BINARY_MANIFEST],
                       capture_output=True, check=True)
    working = root / BINARY_MANIFEST
    if not r.stdout.strip():
        if working.exists():
            print(f"leakscan: {BINARY_MANIFEST} is not staged, so this commit holds "
                  "no manifest and the hook reads none (`git add` it)",
                  file=sys.stderr)
        return {}
    _staged_blob(BINARY_MANIFEST, dest)
    if working.exists() and working.read_bytes() != dest.read_bytes():
        print(f"leakscan: {BINARY_MANIFEST} differs from its staged copy; the hook "
              "reads the staged one, which is what the commit holds",
              file=sys.stderr)
    return load_binary_manifest(root, dest)


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


def render_type_level(warns: list[Finding]) -> list[str]:
    """020/450: type-level entries still accepted, each naming the fields the
    file carries and the date they stop being accepted."""
    if not warns:
        return []
    cut = TYPE_LEVEL_UNTIL.isoformat()
    lines = [f"⚠ leakscan: {len(warns)} G3 type-level metadata entr"
             f"{'y' if len(warns) == 1 else 'ies'} — WARNING ONLY until {cut}, "
             f"refused from {cut}:"]
    for f in sorted(warns, key=lambda x: (x.path, x.excerpt)):
        lines.append(report.with_id(
            f"  {_where(f)}  [warn until {cut}] {f.rule} → {f.excerpt}"
            f" — refused from {cut}; remedy: name the fields instead "
            "(`leakscan --binary-entries` prints the lines)",
            "leakscan", f.rule))
    lines.append(f"  Before {cut}: replace each type-level line in {BINARY_MANIFEST} "
                 "with a line naming the fields kept (`<digest>:exif:Model,LensModel`) "
                 "under the need for those fields, strip the rest, and commit.")
    lines.append("")
    return lines


PROVENANCE_LIST_CAP = 20


def render_provenance(warns: list[Finding]) -> list[str]:
    """160/980 GM5: manifest lines that record a reason and no who/when. A
    warning, with no date on it: whether and when it blocks is the principal's
    to rule. Lists the first `PROVENANCE_LIST_CAP` lines and counts the rest,
    so a child with a hundred old lines gets one screen, not a wall."""
    if not warns:
        return []
    n = len(warns)
    lines = [f"⚠ leakscan: {n} {BINARY_MANIFEST} line(s) record a reason but not who "
             "allowed them or when — WARNING ONLY:"]
    for f in warns[:PROVENANCE_LIST_CAP]:
        lines.append(report.with_id(
            f"  {BINARY_MANIFEST}:{f.line}  [warn] {f.rule} → {f.excerpt}",
            "leakscan", f.rule))
    if n > PROVENANCE_LIST_CAP:
        lines.append(f"  …and {n - PROVENANCE_LIST_CAP} more, counted but not listed.")
    lines.append(f"  Add `{PROVENANCE_FORM}` to each line's comment (the exception "
                 "register's who, session and date; 'agent' for a session's own "
                 "judgement). `leakscan --binary-entries` prints it on new lines.")
    lines.append("")
    return lines


def advisory_count_line(n: int) -> str:
    """The one line that always says how many findings this run reported
    without blocking (115/090). ALWAYS printed, zero included, for the reason
    `secretscan.advisory_count_line` gives: a line printed only when non-zero
    makes "no line" mean both "nothing found" and "the wording drifted", and
    `tools/floor.py` reads this line for its board. The wording lives in
    `report.advisory_count_line` (RT6, 160/730)."""
    return report.advisory_count_line("leakscan", n)


def render_advisory(advisory: list[Finding], over_cap: int = 0) -> list[str]:
    """The report-only block (115/090). It shares no wording with the blocking
    block (not the ✗, not "commit blocked", not the remediation paragraph), so
    a reader can tell at a glance which list stopped the commit."""
    if not advisory and not over_cap:
        return []
    lines = ["",
             "🟡 REPORT-ONLY FINDINGS — none of these blocked anything.",
             "   Rules that are off: one this repo turns off with --disable, or "
             "one withdrawn",
             "   from the blocking set for noise. They still run, so what they "
             "see is shown",
             "   rather than dropped."]
    for f in sorted(advisory, key=lambda x: (x.path, x.line, x.rule)):
        lines.append(report.with_id(
            f"     {_where(f)}  [advisory/{f.kind}] {f.rule} → {f.excerpt}",
            "leakscan", f.rule))
    if over_cap:
        lines.append(report.over_cap_line(over_cap, MAX_MATERIALIZED_FINDINGS,
                                          noun="report-only finding(s)",
                                          indent="   "))
    lines.append("   Real personal data here: remove it. No rotation undoes a "
                 "leak of it, and")
    lines.append("   report-only describes this rule's noise, never the "
                 "value's safety. Otherwise")
    lines.append(f"   leave it, or exempt the line with '# {ALLOW_MARKER}:<rule>: "
                 "<reason>'.")
    return lines


def render_human(findings: list[Finding], warning: str | None,
                 scanned_local: bool, tally: Tally | None = None,
                 grace: list[Finding] | None = None,
                 typewarn: list[Finding] | None = None,
                 provwarn: list[Finding] | None = None) -> str:
    # 115/090: `findings` may carry report-only findings from rules that are
    # off; they are listed in their own block and never counted as blocking.
    advisory = [f for f in findings if not f.blocks]
    findings = [f for f in findings if f.blocks]
    advisory_over = tally.advisory_over_cap if tally is not None else 0
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
    lines.extend(render_type_level(typewarn or []))
    lines.extend(render_provenance(provwarn or []))
    if not findings and not over_cap:
        cover = "structural + local" if scanned_local else "structural only"
        lines.append(f"✓ leakscan clean ({cover})."
                     + (f" The G3 warning(s) above block from "
                        f"{BINARY_GRACE_UNTIL.isoformat()}." if grace else "")
                     + (f" The type-level warning(s) above are refused from "
                        f"{TYPE_LEVEL_UNTIL.isoformat()}." if typewarn else ""))
        if tally is not None:
            lines.append(tally.summary())
        lines.append(advisory_count_line(len(advisory) + advisory_over))
        lines.extend(render_advisory(advisory, advisory_over))
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
    lines.append(advisory_count_line(len(advisory) + advisory_over))
    lines.append("\n  A true positive: remove the data (and rotate if it's a secret).")
    lines.append(f"  A false positive: append '# {ALLOW_MARKER}: <reason>' to the line")
    lines.append(f"  (or '# {ALLOW_MARKER}:<rule>: <reason>' to exempt just one rule —")
    lines.append("  the narrowest allowance that covers the case), or add a path glob")
    lines.append("  to .leakscanignore. A marker with no reason exempts nothing.")
    if any(f.kind == "binary" for f in findings):
        lines.append(f"  A binary (G3): look at it, then list it in {BINARY_MANIFEST} with a")
        lines.append("  reason — `leakscan --binary-entries` prints the lines, hash-bound, so a")
        lines.append("  changed file blocks again. Metadata: strip every set and field you do not")
        lines.append("  need; keep one only on its own '<digest>:<set>' or '<digest>:<set>:<Field>'")
        lines.append("  line, reasoned with that need.")
        lines.append("  A stale entry: delete or re-path it.")
    lines.extend(render_advisory(advisory, advisory_over))
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="leakscan",
        description="Scan for the shape of personal/estate data before it is committed.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo, or --staged). "
                         "With --staged, repo-root-relative paths in git's own "
                         "spelling and case ('.' is the whole diff); one git "
                         "does not know is refused (exit 2)")
    ap.add_argument("--staged", action="store_true",
                    help="scan only lines added in the git staging area (pre-commit hook)")
    ap.add_argument("--terms", help="path to the local literal-term list")
    ap.add_argument("--require-terms", action="store_true",
                    help="fail (exit 2) if no local term list is found, instead of "
                         "degrading to structural-only. For hooks/CI on a machine "
                         "that is EXPECTED to have full cover — review B5: to "
                         "automation, a degraded exit-0 pass is indistinguishable "
                         "from a full one.")
    ap.add_argument("--root", default=".",
                    help="repo root for relative paths/.leakscanignore "
                         "(with --staged it must be the repo you run in)")
    ap.add_argument("--disable", default="",
                    help="comma-separated structural rules that report instead "
                         "of blocking (e.g. ipv4,ipv6,mac-address for a networking "
                         "repo where those shapes are unavoidable noise). Their "
                         "hits are still listed and counted, never in the exit "
                         "code. Local terms always run and always block.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--binary-entries", action="store_true",
                    help=f"print the {BINARY_MANIFEST} lines still needed and exit 0: "
                         "a file line for every tracked binary no entry accepts yet "
                         "(new, or changed since listed), and a '<digest>:<set>' line "
                         "for every metadata set it carries that no line keeps. Lines "
                         "carry no reason: review each file and write one per file and "
                         "per set kept, or the scan refuses it. Each ends with a "
                         "'by= session= on=' who/when note. Never writes the file.")
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
              "and on each set line the need for keeping that set; keep the "
              "'by= session= on=' note on each line, and replace by=CHOOSE with "
              f"{', '.join(PROVENANCE_KINDS)}. Strip a set you do not need rather "
              "than keep it.",
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
    withdrawn = disabled & WITHDRAWN_NAMES
    if withdrawn:
        return report.broken(
            "leakscan", f"--disable {', '.join(sorted(withdrawn))}: a withdrawn "
            "rule already reports without blocking, and --disable never silences "
            "a report. Exempt a line with an allow-marker, or a path with "
            ".leakscanignore.")
    unknown = disabled - {p.name for p in STRUCTURAL}
    if unknown:
        return report.broken(
            "leakscan", f"unknown rule(s) in --disable: {', '.join(sorted(unknown))}")
    # A scope reduction taken at invocation is itself an allowance, and rule (b)
    # says a reduction nobody can see is a reduction nobody reviewed — so
    # `--disable` now reports itself in the output instead of narrowing the scan
    # silently from a flag nobody reading the result will ever see. Since
    # 115/090 it narrows nothing at all: a disabled rule still runs, and its
    # hits report without blocking.
    tally = Tally(disabled_rules=tuple(sorted(disabled)))

    if args.staged:
        rc = report.refuse_other_repo("leakscan", root)
        if rc is not None:
            return rc
        try:
            staged = staged_added_lines()
            changed, binary, removed = staged_changes()
        except report.STAGED_DIFF_FAILURES as e:
            return report.git_diff_failed("leakscan", e)
        # Positional paths, in --staged mode, restrict the scan to staged files
        # under those paths — e.g. scan only the shareable `tiki/` subtree of
        # an otherwise-private repo. `report.resolve_staged_scope` judges the
        # positionals ONCE (roadmap 115/360, 160/950): it refuses an absolute
        # path (which matches no repo-relative git path), one that leaves the
        # repo, and one git does not know (a typo, the wrong case), and
        # otherwise lets git say what each names. G3's extra path lists
        # (binaries, empty new files, pure renames, removals) are cut by the
        # same answer, so one scope means one thing on every list.
        rc, allowed = report.resolve_staged_scope("leakscan", args.paths, "tiki/")
        if rc is not None:
            return rc
        staged = report.restrict_to_scope(staged, allowed)
        in_changed = report.restrict_to_scope(dict.fromkeys(changed), allowed)
        in_removed = report.restrict_to_scope(dict.fromkeys(removed), allowed)
        report.note_empty_scope("leakscan", len(changed), len(in_changed),
                                args.paths)
        # .leakscanignore applies in staged mode too, so an exemption means the
        # same thing whether you scan the tree or a commit.
        globs = load_ignore_globs(root)
        findings = []
        # Every changed path once, in a stable order: the text diff's files
        # first (their existing order), then the paths only git's name list
        # carries — binaries, empty new files, pure renames.
        ordered = list(staged) + [p for p in in_changed if p not in staged]
        with tempfile.TemporaryDirectory(prefix="leakscan-") as td:
            blob = Path(td) / "blob"
            # The manifest this commit will hold, not the working tree's
            # (160/980 GM12): a commit whose manifest edit is unstaged must
            # be judged on what it commits, as on CI.
            try:
                manifest = _staged_manifest(root, Path(td) / "manifest")
            except subprocess.CalledProcessError as e:
                return report.broken("leakscan",
                                     f"git cat-file failed for {BINARY_MANIFEST}: {e}")
            tally.provenance_warnings.extend(provenance_gaps(manifest))
            by_digest = _digest_index(manifest)
            for path in ordered:
                ignored = _ignored(path, globs)
                if ignored and path not in binary:
                    tally.files_by_glob += 1
                    continue
                if not ignored:
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
                if ignored and not _looks_binary_file(blob):
                    # G3 runs before the ignore file for a BINARY (GM9); a file
                    # git calls binary that is really text is only text, and
                    # the glob still skips it.
                    tally.files_by_glob += 1
                    continue
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
            if entry is not None:
                _record(findings, tally, _stale(entry, "removed or renamed by this commit"))
    else:
        # A RELATIVE target resolves against --root, never the caller's cwd:
        # mixing the two reads one repo's file under another repo's rules,
        # and neither half of the output says so (roadmap 010/110).
        targets = report.resolve_targets(root, args.paths or [str(root)])
        # A typo'd path scanning nothing must never read as a clean pass —
        # the linkscan L1 silent-success class, closed here too
        # (2026-07-11 review N2).
        rc = report.refuse_escaping_targets("leakscan", root, args.paths)
        if rc is not None:
            return rc
        rc = report.refuse_missing_paths("leakscan", targets)
        if rc is not None:
            return rc
        findings = scan_paths(targets, root, local_terms, disabled, tally)

    # THE G3 GRACE (see `BINARY_GRACE_UNTIL`): before the cut-off the four
    # gate rules warn instead of blocking. Only those rules — a text-metadata
    # hit is an ordinary rule's finding and still blocks. Findings past the
    # materialisation cap were counted, never built, so they cannot be sorted
    # by rule and stay blocking: fail closed.
    typewarn = tally.type_level_warnings
    provwarn = tally.provenance_warnings
    grace: list[Finding] = []
    if in_binary_grace():
        grace = [f for f in findings if f.rule in BINARY_RULES]
        findings = [f for f in findings if f.rule not in BINARY_RULES]
        tally.binary_grace_warnings = len(grace)
    # 115/090: findings from rules that are off report without blocking. They
    # are kept out of `blocking`, which alone feeds the exit code.
    blocking = [f for f in findings if f.blocks]
    advisory = [f for f in findings if not f.blocks]
    blocking_total = len(blocking) + tally.findings_over_cap
    advisory_total = len(advisory) + tally.advisory_over_cap

    if args.json:
        print(json.dumps({
            # `clean` and `findings` keep their meaning: BLOCKING findings
            # only, which before 115/090 was every finding. Report-only ones
            # are under `advisory`, so a consumer that gated on `clean` gates
            # on exactly what it did.
            "clean": not blocking_total,
            "blocked": bool(blocking_total),
            "counts": {"blocking": blocking_total, "advisory": advisory_total},
            "scanned_local_terms": scanned_local,
            "warning": warning,
            "findings": report.finding_dicts("leakscan", blocking,
                                             lambda f: f.rule),
            "findings_over_cap": tally.findings_over_cap,
            "advisory": {
                "findings": report.finding_dicts("leakscan", advisory,
                                                 lambda f: f.rule),
                "over_cap": tally.advisory_over_cap,
            },
            "binary_grace": {
                "until": BINARY_GRACE_UNTIL.isoformat(),
                "active": in_binary_grace(),
                "warnings": report.finding_dicts("leakscan", grace,
                                                 lambda f: f.rule),
            },
            "binary_provenance": {
                "form": PROVENANCE_FORM,
                "warnings": report.finding_dicts("leakscan", provwarn,
                                                 lambda f: f.rule),
            },
            "binary_type_level": {
                "until": TYPE_LEVEL_UNTIL.isoformat(),
                "active": in_type_level_grace(),
                "warnings": report.finding_dicts("leakscan", typewarn,
                                                 lambda f: f.rule),
            },
            "suppressed": {
                "by_allow_marker": tally.marker_total,
                "by_allow_marker_rule": tally.by_marker,
                "markers_naming_no_rule": tally.unknown_scope_markers,
                "files_by_ignore_glob": tally.files_by_glob,
                "disabled_rules": list(tally.disabled_rules),
                "binaries_by_manifest": tally.binaries_by_manifest,
                "binaries_untracked_not_gated": tally.binaries_untracked,
            },
        }, indent=2))
    else:
        print(render_human(findings, warning, scanned_local, tally, grace, typewarn,
                           provwarn))

    return report.exit_code(blocking_total)


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
    # G3 fields (020/450): one IFD0 entry, tag 0x0110, reads as `exif:Model`.
    tiff = (b"MM\x00*" + struct.pack(">IH", 8, 1)
            + struct.pack(">HHII", 0x0110, 2, 1, 0) + struct.pack(">I", 0))
    if exif_fields(tiff) != ["exif:Model"]:
        print("FAIL: Exif tag 0x0110 not read as the field exif:Model")
        ok = False
    # G3 fields, part 2 (020/450): an IPTC By-line, an XMP property and a PNG
    # keyword are each read by name; a packet that is not XMP is unknown.
    if iptc_fields(b"\x1c\x02\x50\x00\x01x") != ["iptc:By-line"]:
        print("FAIL: IPTC dataset 2:080 not read as the field iptc:By-line")
        ok = False
    packet = (b'<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="'
              + _RDF_NS.encode() + b'"><rdf:Description xmlns:dc="http://purl.org/dc/elements/1.1/">'
              b"<dc:title>t</dc:title></rdf:Description></rdf:RDF></x:xmpmeta>")
    if xmp_fields(packet) != ["xmp:dc:title"] or xmp_fields(b"<a/>") != ["xmp:unknown"]:
        print("FAIL: XMP properties not read by name")
        ok = False
    if png_text_field(b"Creation Time") != "png-text:Creation%20Time":
        print("FAIL: PNG text keyword not written as a field")
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
