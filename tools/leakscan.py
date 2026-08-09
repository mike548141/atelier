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
    weaker (legibility).

All three run over file CONTENT *and* over each file's repo-relative PATH — a
file whose *name* carries an address or a person's name leaks exactly as much as
one whose body does, and until 2026-08-04 the name was never read (gap G2). Path
findings report at line 0.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean
  1  findings (blocks the commit)
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can run
it with the system python3 and no install.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

# A line carrying this marker is intentionally exempt (e.g. an illustrative
# example in doctrine). Keep the reason on the same line so the exemption is
# self-documenting and greppable.
#
# GOVERNED BY `method/GUARDS.md` — narrow, noisy, reasoned:
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
ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER)
    + r"(?::(?P<rule>[A-Za-z0-9_-]+(?:,[A-Za-z0-9_-]+)*))?:[ \t]*(?P<reason>[\w\"\'“‘])")


def parse_allow(line: str) -> frozenset[str] | None:
    """The scope of the line's allow-marker, or None if it carries none.

    Returns an empty frozenset for the unscoped form (every STRUCTURAL rule —
    never the term list, D1) or the named rules for the scoped form. A marker
    without a reason returns None — it is a mention, not an exemption."""
    m = ALLOW_RX.search(line)
    if not m:
        return None
    rule = m.group("rule")
    return frozenset(rule.split(",")) if rule else frozenset()

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

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def note_marker(self, rule: str) -> None:
        self.by_marker[rule] = self.by_marker.get(rule, 0) + 1

    def summary(self) -> str:
        """One stable line, zeros printed. The field set never varies between
        runs so two runs can be read side by side (a missing field would read
        as a zero rather than as 'this run did not measure it')."""
        parts = [f"{self.marker_total} by allow-marker",
                 f"{self.files_by_glob} file(s) by .leakscanignore",
                 f"{len(self.disabled_rules)} rule(s) disabled"]
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
    so a name split ACROSS lines is still not matched by anything."""
    parts = [re.escape(p) for p in term.split() if p]
    return re.compile(r"\b" + r"[\s._-]*".join(parts) + r"\b", re.IGNORECASE)


def load_local_terms(path: Path | None) -> tuple[list[tuple[str, "re.Pattern[str]"]], str | None]:
    """Return (compiled terms, warning). Each line is a case-insensitive
    whole-word literal, unless prefixed `regex:` for a raw pattern or `forms:`
    for a literal plus its derived separator/case variants (G6). `#` comments
    and blank lines are ignored."""
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
            terms.append((line, re.compile(r"\b" + re.escape(line) + r"\b", re.IGNORECASE)))
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


def scan_text(path: str, text: str,
              local_terms: list[tuple[str, "re.Pattern[str]"]],
              disabled: frozenset[str] = frozenset(),
              tally: Tally | None = None) -> list[Finding]:
    findings: list[Finding] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        allow_scope = parse_allow(line)
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
                findings.append(Finding(path, lineno, pat.name, "structural",
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
                findings.append(Finding(path, lineno, "local-term", "local",
                                        "high", f"term:{term[:2]}…"))
    return findings


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
    """Globs from `.leakscanignore`, each of which MUST carry a stated reason.

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
    f = root / ".leakscanignore"
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
        raise IgnoreFileError(".leakscanignore", unreasoned)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


def iter_files(paths: list[Path], root: Path, globs: list[str],
               tally: Tally | None = None):
    for base in paths:
        if base.is_file():
            files = [base]
        else:
            files = [p for p in base.rglob("*")
                     if p.is_file() and not (SKIP_DIR_NAMES & set(p.parts))]
        for p in files:
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


def scan_paths(paths: list[Path], root: Path,
               local_terms: list[tuple[str, "re.Pattern[str]"]],
               disabled: frozenset[str] = frozenset(),
               tally: Tally | None = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p, rel in iter_files(paths, root, globs, tally):
        # G2: the path is scanned whatever the contents turn out to be — a
        # binary's NAME is readable even when its body is not.
        findings.extend(scan_path_name(rel, local_terms, disabled, tally))
        data = p.read_bytes()
        if _looks_binary(data):
            continue
        findings.extend(scan_text(rel, data.decode("utf-8", errors="replace"),
                                  local_terms, disabled, tally))
    return findings


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


def resolve_terms_path(cli: str | None) -> Path | None:
    for candidate in (cli, os.environ.get("ATELIER_LEAKSCAN_TERMS"), DEFAULT_LOCAL_TERMS):
        if candidate:
            p = Path(candidate).expanduser()
            if p.exists():
                return p
    return None


def render_human(findings: list[Finding], warning: str | None,
                 scanned_local: bool, tally: Tally | None = None) -> str:
    lines: list[str] = []
    if warning:
        lines.append(f"⚠ {warning}")
    if not findings:
        cover = "structural + local" if scanned_local else "structural only"
        lines.append(f"✓ leakscan clean ({cover}).")
        if tally is not None:
            lines.append(tally.summary())
        return "\n".join(lines)
    lines.append(f"✗ leakscan: {len(findings)} finding(s) — commit blocked.\n")
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        # Line 0 means the hit is in the PATH itself (G2) — say so, because
        # ':0' would otherwise read as a line number nobody can open.
        where = f"{f.path}:{f.line}" if f.line else f"{f.path} (in the path name)"
        lines.append(f"  {where}  [{f.severity}/{f.kind}] {f.rule} → {f.excerpt}")
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append("\n  A true positive: remove the data (and rotate if it's a secret).")
    lines.append(f"  A false positive: append '# {ALLOW_MARKER}: <reason>' to the line")
    lines.append(f"  (or '# {ALLOW_MARKER}:<rule>: <reason>' to exempt just one rule —")
    lines.append("  the narrowest allowance that covers the case), or add a path glob")
    lines.append("  to .leakscanignore. A marker with no reason exempts nothing.")
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
    ap.add_argument("--selftest", action="store_true", help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    terms_path = resolve_terms_path(args.terms)
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
        if prefixes:
            staged = {path: text for path, text in staged.items()
                      if path.startswith(prefixes) or path in args.paths}
        # .leakscanignore applies in staged mode too, so an exemption means the
        # same thing whether you scan the tree or a commit.
        globs = load_ignore_globs(root)
        findings = []
        for path, text in staged.items():
            if _ignored(path, globs):
                tally.files_by_glob += 1
                continue
            # G2 on the hot path too: a leak in a NEW file's name reaches the
            # remote by the same commit as one in its body.
            findings.extend(scan_path_name(path, local_terms, disabled, tally))
            findings.extend(scan_text(path, text, local_terms, disabled, tally))
    else:
        targets = [Path(p) for p in (args.paths or [str(root)])]
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
            "clean": not findings,
            "scanned_local_terms": scanned_local,
            "warning": warning,
            "findings": [asdict(f) for f in findings],
            "suppressed": {
                "by_allow_marker": tally.marker_total,
                "by_allow_marker_rule": tally.by_marker,
                "files_by_ignore_glob": tally.files_by_glob,
                "disabled_rules": list(tally.disabled_rules),
            },
        }, indent=2))
    else:
        print(render_human(findings, warning, scanned_local, tally))

    return 1 if findings else 0


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
    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1



def main(argv: list[str] | None = None) -> int:
    """Exit 2 on an ignore file that grants an exemption with no reason.

    A broken scan is not a pass (the house exit-code contract), and an
    unexplained exemption makes the scan's own scope untrustworthy."""
    try:
        return _main(argv)
    except IgnoreFileError as e:
        print(f"leakscan: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
