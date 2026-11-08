"""The single-sourced allow-marker grammar and ignore-file loader shared by the
scanners (`115/080`, part 2; the GA1 finding).

Before this module each scanner carried its own copy of two mechanisms:

  * the reasoned allow-marker regex plus its `parse_allow` reader
    (`<scanner>:allow[:<scope>]: <reason>`), at fourteen regex sites across
    twelve files; and
  * the reason-required `.<scanner>ignore` loader, its `_ignored` glob test
    and its `IgnoreFileError`, eleven textually identical copies.

On 2026-08-09 a change to shared parsing, applied copy by copy, silently
voided nine live allow-markers across three child repos — and a voided marker
reads exactly like an absent one. Single-sourcing is the upstream fix.

WHAT THIS MODULE DELIBERATELY DOES NOT DO: unify behaviour. The scanners'
acceptance rules differ on purpose or by history, and every difference is a
PARAMETER here, never a default someone can drift into:

  * `scope`   — None (the marker takes no sub-scope), "one" (one optional
                `:<name>` scope) or "list" (comma-joined names; `leakscan`).
  * `group`   — the regex group name (`rule` or `kind`); cosmetic to callers
                but kept so each scanner's compiled pattern is byte-identical
                to what it carried before.
  * `sep`     — what may sit between the colon and the reason: `[ \\t]*`
                (same line only) or `\\s*` (may cross a newline).
  * `named_reason` — whether the reason's first character is a named group.

The reason's first character must be a word character or an opening quote;
that rule is not a parameter because every scanner already shared it, and a
marker inside its own HTML comment (`<!-- x:allow: -->`) must not mistake the
comment closer for a reason (DSR8).

Each scanner keeps its own `ALLOW_MARKER` constant, its own `parse_allow`
wrapper and its own result type (str / frozenset / bool); only the mechanism
is shared. `tools/test_allowmarker.py` pins every parameter combination.

WHAT IT FAILS CLOSED ON (160/480, the cold pass on this module; Mike
2026-11-09, "Strict, with a warning period"):

  * a MALFORMED scoped marker (`m:allow:ipv4:`, `m:allow:email, ipv4: why`) no
    longer backs off to the unscoped form and exempts the whole line. Before
    `MALFORMED_GRACE_UNTIL` it still does, with a stderr warning; from that date
    it exempts nothing (AM2, and LK1 which is the same finding);
  * a mention of the syntax inside an inline code span is not a marker (AM3);
  * a reader asks the pattern for its own scope group, so the group name is
    stated once (AM8).

The `\\s*` separator exists for the multi-line marker searches (`blockscan`'s
region text, `stampscan`'s block head); every other site reads one line.

THE UNIT OF REUSE is the `tools/` directory. The scanners import this module,
`filewalk` and `report`, so a single scanner file copied alone does not run.
"""

from __future__ import annotations

import datetime
import fnmatch
import re
import sys
from pathlib import Path

# First character of a reason: a word character or an opening quote.
REASON_START = r"[\w\"\'“‘]"

_SCOPE_ONE = r"[A-Za-z0-9_-]+"
_SCOPE_LIST = r"[A-Za-z0-9_-]+(?:,[A-Za-z0-9_-]+)*"

SEP_SAME_LINE = r"[ \t]*"
SEP_ANY_SPACE = r"\s*"


# THE MALFORMED-MARKER GRACE (160/480 AM2, answered by the principal
# 2026-11-09: "Strict, with a warning period").
#
# A scoped marker whose scope is broken (`leakscan:allow:ipv4:` with no reason,
# `leakscan:allow:email, ipv4: why` with a space in the scope, a trailing comma,
# a scope the scanner cannot take) used to back off to the UNSCOPED form and
# take the scope word for the reason, so it exempted EVERY rule on its line: the
# unsafe direction, on both boundary guards (LK1, the same finding as AM2).
# Before this date such a marker still exempts as it always did and WARNS, once
# per distinct marker per run, on stderr. ON and after it, it is a mention: it
# exempts nothing. The cut-off lives in this one constant, compared with the UTC
# clock; there is no flag, environment variable or config key that moves it
# (the same shape as leakscan's `BINARY_GRACE_UNTIL`). Delete the warning path
# and `in_malformed_grace` once the date has passed; the strict read stays.
MALFORMED_GRACE_UNTIL = datetime.date(2026, 12, 9)


def _utc_today() -> datetime.date:
    return datetime.datetime.now(datetime.timezone.utc).date()


def in_malformed_grace(today: datetime.date | None = None) -> bool:
    """True strictly before `MALFORMED_GRACE_UNTIL` (UTC). Tests patch
    `_utc_today`; nothing a caller can pass at the command line reaches it."""
    return (today or _utc_today()) < MALFORMED_GRACE_UNTIL


# pattern -> (marker, group name) for every scoped pattern `marker_rx` built;
# the malformed read needs the marker word and the group the reader asks for.
_SCOPED: "dict[re.Pattern[str], tuple[str, str]]" = {}
# The marker heads already warned about in this process (one warning each).
_WARNED: set[str] = set()


def marker_rx(marker: str, *, scope: str | None = None, group: str = "kind",
              sep: str = SEP_SAME_LINE, named_reason: bool = True) -> "re.Pattern[str]":
    """Compile the reasoned allow-marker pattern for `marker`
    (e.g. `"datescan:allow"`), word-boundary anchored, colon then a
    non-empty reason. A scoped pattern is remembered with its marker word and
    group name, so `scope_of` / `scopes_of` need no group argument (AM8) and
    can recognise a malformed scope (AM2)."""
    if scope is None:
        scope_part = ""
    elif scope == "one":
        scope_part = r"(?::(?P<" + group + r">" + _SCOPE_ONE + r"))?"
    elif scope == "list":
        scope_part = r"(?::(?P<" + group + r">" + _SCOPE_LIST + r"))?"
    else:
        raise ValueError(f"unknown scope mode: {scope!r}")
    reason = (r"(?P<reason>" + REASON_START + r")") if named_reason else REASON_START
    rx = re.compile(r"\b" + re.escape(marker) + scope_part + r":" + sep + reason)
    if scope is not None:
        _SCOPED[rx] = (marker, group)
    return rx


def blank_code_spans(text: str) -> str:
    """Blank inline `code spans`, keeping the length, so a mention of the
    marker syntax inside one is not read as a marker (AM3). Backtick runs must
    match in length (CommonMark). A line is the unit: an unmatched backtick
    run, or a span that would cross a newline, is left as it is. Identical to
    the helper `datescan`, `linkscan`, `spellscan` and `stampscan` carry for
    their own content, which blank code spans AFTER the marker was read."""
    if "`" not in text:
        return text
    return "".join(_blank_line(ln) for ln in text.splitlines(keepends=True))


def _blank_line(line: str) -> str:
    if "`" not in line:
        return line
    out: list[str] = []
    i = 0
    n = len(line)
    no_close: set[str] = set()      # tick runs known to have no later match
    while i < n:
        tick = line.find("`", i)
        if tick == -1:
            out.append(line[i:])
            break
        if tick > i:
            out.append(line[i:tick])
            i = tick
        j = i
        while j < n and line[j] == "`":
            j += 1
        ticks = line[i:j]
        if ticks not in no_close:
            close = line.find(ticks, j)
            if close == -1:
                no_close.add(ticks)
            elif line[close:close + len(ticks)] == ticks \
                    and (close + len(ticks) >= n or line[close + len(ticks)] != "`"):
                out.append(" " * (close + len(ticks) - i))
                i = close + len(ticks)
                continue
        out.append(line[i])
        i += 1
    return "".join(out)


def present(rx: "re.Pattern[str]", text: str) -> bool:
    """True if `text` carries a reasoned marker (the unscoped readers). A
    marker inside an inline code span is a mention, not a marker (AM3)."""
    return rx.search(blank_code_spans(text)) is not None


def _group_of(rx: "re.Pattern[str]", group: str | None) -> str:
    """The scope group's name. A pattern `marker_rx` built remembers its own,
    and that wins over any argument, so a reader cannot ask for a group the
    pattern does not have (AM8: the two defaults disagreed, and the mismatch
    raised mid-scan on the first marked file)."""
    reg = _SCOPED.get(rx)
    if reg is not None:
        return reg[1]
    names = [g for g in ("kind", "rule") if g in rx.groupindex]
    if group in rx.groupindex:
        return group
    if len(names) != 1:
        raise ValueError("pattern has no scope group; build it with scope=")
    return names[0]


# A glued run after the marker's first colon (no space, so the author did not
# mean it as a free-text reason) that reaches a second colon: the shape of a
# scope that failed to parse. Either it has no reason (`m:allow:ipv4:`), or the
# scope holds a space or a stray character (`m:allow:email, ipv4: why`), or a
# trailing comma (`m:allow:a,: why`). `<`, `>` and the backtick end the run, so
# an HTML comment closer or a following code span is not read as a scope.
def _malformed_rx(marker: str) -> "re.Pattern[str]":
    return re.compile(r"\b" + re.escape(marker) + r":(?=[A-Za-z0-9_-])[^:<>`\n]{1,80}?:")


def is_malformed(rx: "re.Pattern[str]", text: str, m: "re.Match[str]",
                 group: str | None = None) -> bool:
    """Did match `m` of scoped pattern `rx` read a BROKEN scoped marker as an
    unscoped one? True when the match took no scope but the text at its start
    is the glued scope-then-colon shape. A well-formed scoped marker has its
    scope in the group, and an honest unscoped one (`m:allow: why`) has a space
    after the first colon, so neither is malformed."""
    reg = _SCOPED.get(rx)
    if reg is None:
        return False
    if m.group(_group_of(rx, group)):
        return False
    mal = _malformed_rx(reg[0]).match(text, m.start())
    return mal is not None


def _warn_malformed(text: str, m: "re.Match[str]", rx: "re.Pattern[str]") -> None:
    reg = _SCOPED[rx]
    head = _malformed_rx(reg[0]).match(text, m.start())
    shown = head.group(0) if head else reg[0]
    if shown in _WARNED:
        return
    _WARNED.add(shown)
    print(f"allowmarker: warning: malformed allow-marker `{shown}` has no "
          f"valid scope or reason, so it reads as an unscoped marker and "
          f"exempts the WHOLE line. That stops on "
          f"{MALFORMED_GRACE_UNTIL.isoformat()}: from then it exempts nothing. "
          f"Spell it `{reg[0]}:<scope>: <reason>` (tools/README.md, 'Allow "
          f"markers and ignore files').", file=sys.stderr)


def malformed_seen() -> list[str]:
    """The malformed marker heads warned about so far in this process."""
    return sorted(_WARNED)


def _read(rx: "re.Pattern[str]", text: str, group: str | None):
    """The first marker match that counts, or None. Code spans are blanked
    first (AM3). A malformed match counts before `MALFORMED_GRACE_UNTIL`, with
    a warning, and is skipped after it (AM2): the strict read goes on to any
    well-formed marker later on the line."""
    group = _group_of(rx, group)
    reg = _SCOPED.get(rx)
    if reg is not None and reg[0] not in text:
        return None             # cheap exit: the marker word is not on the line
    text = blank_code_spans(text)
    for m in rx.finditer(text):
        if is_malformed(rx, text, m, group):
            if not in_malformed_grace():
                continue
            _warn_malformed(text, m, rx)
        return m, group
    return None


def scope_of(rx: "re.Pattern[str]", text: str, group: str | None = None) -> str | None:
    """The marker's scope, `""` for the unscoped form, None when there is no
    reasoned marker. Needs a `scope="one"` pattern from `marker_rx`; the group
    is the one the pattern was built with (a `group` argument is accepted for
    old callers and ignored)."""
    got = _read(rx, text, group)
    if got is None:
        return None
    m, group = got
    return m.group(group) or ""


def scopes_of(rx: "re.Pattern[str]", text: str, group: str | None = None) -> frozenset[str] | None:
    """As `scope_of` for a `scope="list"` pattern: the named scopes as a
    frozenset (empty for the unscoped form), None when there is no marker."""
    got = _read(rx, text, group)
    if got is None:
        return None
    m, group = got
    names = m.group(group)
    return frozenset(names.split(",")) if names else frozenset()


def names_no_rule(scope, known) -> bool:
    """True when a marker's scope names something outside `known` (AM10): a
    typo or a rule that does not exist, which is silently inert in the
    rule-matching scanners. `scope` is a str (`""` = unscoped, names nothing) or
    a frozenset of names; None (no marker) names nothing. Matching is
    case-insensitive on both sides, as the scanners that lower-case compare."""
    if scope is None or scope == "" or scope == frozenset():
        return False
    names = [scope] if isinstance(scope, str) else list(scope)
    low = {k.lower() for k in known}
    return any(n.lower() not in low for n in names)


def covers(scope: str | None, kind: str, kinds: frozenset[str]) -> bool:
    """Does a marker whose scope is `scope` exempt a finding of `kind`, in a
    scanner whose finding kinds are `kinds`? (`115/080`, the marker-scope half.)

    For the scanners that used to READ a scope and then ignore it, so that any
    reasoned marker exempted every kind of finding in its unit (`licenscan`,
    `sizescan`, `pointerscan`; the AM4 finding). The rule is additive, so a
    marker that exempted something before exempts exactly the same now:

      * `None` (no reasoned marker) exempts nothing;
      * `""` (the unscoped form) exempts every kind, as before;
      * a scope that NAMES one of `kinds` exempts that kind only — the new,
        narrower hatch, and the one a printed finding ID points at;
      * any other scope exempts every kind, as before. Not endorsed: it is the
        same widening as `115/230` item 1 (a malformed marker exempts more,
        not less), kept until that item is ruled, because refusing it would
        void any live marker written that way.

    The rule-matching scanners (`secretscan`, `datescan`, `linkscan`,
    `leakscan`, `spellscan`) do not use this: there an unknown scope already
    exempts nothing, and that stays theirs."""
    if scope is None:
        return False
    if scope in kinds:
        return scope == kind
    return True


def is_blanket(scope: str | None, kinds: frozenset[str]) -> bool:
    """True when a marker's scope exempts EVERY kind (`covers` for all of
    `kinds`): the unscoped form, or a scope naming none of them."""
    return scope is not None and scope not in kinds


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


def read_reasoned_parts(f: Path) -> list[tuple[int, str, str, str | None]]:
    """The grammar of `read_reasoned_lines` before its two reason places are
    merged: `(line number, entry, trailing, stanza)`. `trailing` is the text
    after the first `#` on the entry's own line (empty when none); `stanza` is
    the comment block directly above it, its lines joined by a space, or None
    when no comment block covers the entry (a blank line ends a stanza; a
    stanza of bare `#` lines is the empty string, still a block). A caller
    that records something beside the reason (G3's who and when) reads both
    places, so a trailing note never hides the stanza's reason.
    `read_reasoned_lines` is built on this, so the two cannot drift. An
    absent file reads as no entries."""
    if not f.exists():
        return []
    out: list[tuple[int, str, str, str | None]] = []
    stanza: list[str] = []
    for n, raw in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw.strip()
        if not line:
            stanza = []
            continue
        if line.startswith("#"):
            stanza.append(line.lstrip("#").strip())
            continue
        entry, _, trailing = line.partition("#")
        entry = entry.strip()
        if not entry:
            continue
        out.append((n, entry, trailing.strip(),
                    " ".join(s for s in stanza if s) if stanza else None))
    return out


def read_reasoned_lines(f: Path) -> list[tuple[int, str, str | None]]:
    """The reason grammar every reason-required config file shares, as
    `(line number, entry, reason)` triples — `reason` is None for an entry no
    reason covers. An absent file reads as no entries.

    An entry is reasoned if it carries a trailing `# reason` (publishscan's
    form) OR sits under a comment block in its own stanza; a blank line ends a
    stanza. The entry is the text before the first `#`, stripped, so an entry
    can never itself contain `#`. Callers decide what an unreasoned entry
    costs (both current callers refuse it as a config error): this reader
    only says which entries have a reason and what it is.

    Single-sourced so `.leakscanignore` and `.leakscanbinaries` (G3) cannot
    drift apart on what "reasoned" means."""
    out: list[tuple[int, str, str | None]] = []
    for n, entry, trailing, stanza in read_reasoned_parts(f):
        # A stanza of bare `#` lines still counts as a reason block — the
        # presence test the ignore loader always made — so the text may be
        # empty while the entry is reasoned; None is reserved for "no reason".
        if trailing:
            reason: str | None = trailing
        elif stanza is not None:
            reason = stanza
        else:
            reason = None
        out.append((n, entry, reason))
    return out


def load_ignore_globs(root: Path, filename: str) -> list[str]:
    """Globs from `<root>/<filename>`, each of which MUST carry a stated reason.

    GUARDS.md rule (c): an ignore glob is the widest allowance a scanner
    grants — a whole path, every rule, indefinitely — so it is the last place
    an unexplained exemption should be possible. A glob is reasoned if it
    carries a trailing `# reason` (publishscan's form) OR sits under a comment
    block in its own stanza. A blank line ends a stanza, so a bare glob under
    no comment at all is refused (`read_reasoned_lines` is the grammar).

    An unreasoned glob is a CONFIG ERROR, not a warning: raised as
    `IgnoreFileError`, which callers surface as exit 2 — a broken scan is not
    a pass. An absent file is not an error: no globs."""
    entries = read_reasoned_lines(root / filename)
    unreasoned = [(n, g) for n, g, reason in entries if reason is None]
    if unreasoned:
        raise IgnoreFileError(filename, unreasoned)
    return [g for _, g, _ in entries]


def ignored(rel: str, globs: list[str]) -> bool:
    """True if repo-relative `rel` matches any glob, or sits under a glob
    treated as a directory (`g/` or `g`).

    The match is `fnmatch`, NOT gitignore (AM6), whatever an ignore file's
    header says: `*` also crosses `/` (`docs/*.md` matches `docs/sub/a.md`),
    `**` means the same as `*` (and `**/x` misses a top-level `x`), a leading
    `/` never matches, and `!` is a literal character that negates nothing. A
    glob that can never match exempts nothing, silently, so write each one as a
    path from the repo root."""
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


# ---------------------------------------------------------------- census --
#
# `python3 tools/allowmarker.py --census [--root DIR]` lists every malformed
# scoped marker (the AM2 shape) in a tree, so a repo can find and fix its own
# before `MALFORMED_GRACE_UNTIL`. Read-only; exit 0 either way (it reports, the
# grace warning and the cut-off are what move a scan).

_SCOPED_MARKER_WORDS = ("leakscan", "secretscan", "spellscan", "linkscan",
                        "datescan", "pathscan", "licenscan", "sizescan",
                        "pointerscan", "reviewscan", "indexscan")
_CENSUS_RX = re.compile(r"\b(?:" + "|".join(_SCOPED_MARKER_WORDS) + r"):allow(?=:)")
# leakscan alone takes a comma-joined list; every other scoped scanner takes one.
_GOOD_TAIL_LIST_RX = re.compile(r":" + _SCOPE_LIST + r":" + SEP_SAME_LINE + REASON_START)
_GOOD_TAIL_ONE_RX = re.compile(r":" + _SCOPE_ONE + r":" + SEP_SAME_LINE + REASON_START)


def census_line(line: str) -> list[str]:
    """The malformed scoped-marker heads on `line` (code spans blanked first,
    as the readers do): glued scope-then-colon with no valid scoped reason."""
    line = blank_code_spans(line)
    out: list[str] = []
    for m in _CENSUS_RX.finditer(line):
        tail = line[m.end():]
        good = _GOOD_TAIL_LIST_RX if m.group(0).startswith("leakscan:") else _GOOD_TAIL_ONE_RX
        if good.match(tail):
            continue
        mal = re.compile(r":(?=[A-Za-z0-9_-])[^:<>`\n]{1,80}?:").match(tail)
        if mal:
            out.append(m.group(0) + mal.group(0))
    return out


def census(root: Path) -> list[tuple[str, int, str]]:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import filewalk
    found: list[tuple[str, int, str]] = []
    for f in filewalk.walk_files(root, {".git", "node_modules", "__pycache__"}):
        try:
            if f.stat().st_size > 3_000_000:
                continue
            raw = f.read_bytes()
        except OSError:
            continue
        if b"\0" in raw[:4096] or b":allow" not in raw:
            continue
        rel = f.relative_to(root).as_posix()
        for n, line in enumerate(raw.decode("utf-8", "replace").splitlines(), 1):
            if ":allow" in line:
                for head in census_line(line):
                    found.append((rel, n, head))
    return found


def main(argv: list[str] | None = None) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        prog="allowmarker",
        description="List malformed scoped allow-markers in a tree (read-only).")
    ap.add_argument("--census", action="store_true", required=True,
                    help="list malformed scoped markers")
    ap.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    rows = census(Path(args.root).resolve())
    for rel, n, head in rows:
        print(f"{rel}:{n}: {head}")
    if in_malformed_grace():
        print(f"allowmarker: {len(rows)} malformed scoped marker(s); each "
              f"exempts its whole line until {MALFORMED_GRACE_UNTIL.isoformat()} "
              "and nothing after")
    else:
        print(f"allowmarker: {len(rows)} malformed scoped marker(s); each "
              f"exempts nothing (the grace ended {MALFORMED_GRACE_UNTIL.isoformat()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
