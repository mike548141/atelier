#!/usr/bin/env python3
"""plainscan — plain-language gate for prose the principal has to read.

WHY THIS FILE EXISTS (the failure it closes, 2026-08-09)
--------------------------------------------------------
`COMMUNICATION.md` is the one doctrine in the house with no mechanical floor.
It says so itself, honestly, in its own enforcement clause: "write-time
discipline is the *only* control". Every other rule this estate cares about —
personal data, secrets, dates, links, wrap width, NZ spelling — has a scanner
standing behind it. Plain language had a principle and nothing else.

Measured across 6,704 assistant replies of 200+ characters, spanning 1,094
session transcripts in 18 repos (2026-07 to 2026-08):

  bracketed aside over 25 chars     67.2% of replies   (doctrine since 2026-07-15)
  uncommon acronym, unexpanded      55.5% of replies
  sentence over 35 words            36.8% of replies
  bare reference ID (F1, C5, SL2)   17.4% of replies

and, the sharpest number of the four: of every reference ID's **first use in a
session**, 86% arrived with no gloss at all — 1,457 bare against 236 glossed.
The rate did not improve after the rules were written down. Reference-ID
density rose between July and August (4.04 to 7.23 per thousand words) while
the rule against it sat in doctrine, unbroken and unenforced.

That is the whole argument for this file. A principle the author must remember
at write time is a principle that decays; the estate learned this once already
with vendored policy (`floor.py`'s opening) and closed it with a registry. This
closes the same shape one surface over.

WHAT IT CHECKS, AND WHAT EACH RULE IS GROUNDED IN
--------------------------------------------------
Grounding matters more here than usual, because a threshold fitted to the
current measurement is not a standard — it is a photograph of the defect with
a number written under it. Each rule below names its ground, and where the
ground is a house call rather than a published standard, it says so plainly.

  P1  undefined-reference   A short ID (F1, C5, SL2, EP3) used before anything
                            in the document says what it refers to.
                            GROUND: published. digital.govt.nz plain-language
                            guidance — "Use the expanded form or meaning of
                            abbreviations and acronyms the first time you use
                            them." No threshold to fit: either the first use
                            carries a gloss or it does not.

  P2  unexpanded-acronym    An uncommon acronym on first use with no expansion
                            and no glossary entry.
                            GROUND: published, same clause as P1. The house
                            adds one honest escape the standard does not need:
                            a term defined in the repo's GLOSSARY.md counts as
                            expanded, because the reader has one canonical
                            place to look (thin anchor, fat pointer).

  P3  long-sentence         A sentence over the word limit.
                            GROUND: HOUSE CALL, not a published number. Two
                            authoritative plain-language sources were checked
                            for a numeric cap (digital.govt.nz, digital.gov)
                            and neither states one — they say "one idea per
                            sentence" and stop. The default here is therefore
                            declared, not derived, and is the one number in
                            this file the principal should rule on. It is set
                            deliberately ABOVE the common 20-25 word editorial
                            advice: this gate exists to stop the sentences that
                            cost a reread, not to impose a style.

  P4  buried-aside          A parenthetical over the character limit sitting
                            mid-sentence, forcing the reader to hold the
                            sentence open while parsing the interruption.
                            GROUND: house doctrine, already decided and dated —
                            COMMUNICATION.md § Accessibility of the language,
                            2026-07-15: "Brackets are for short, droppable
                            glosses only; content that matters never lives in
                            them." The character limit distinguishes a gloss
                            from content; it is a house call like P3's.

ONE ENGINE, TWO PLANES — the same shape floor.py already uses
--------------------------------------------------------------
`scan_text()` is the whole rule engine and it takes a string. Two callers:

  repo   this CLI, in the floor registry, gating committed prose in docs/**
         on every hook and every CI run in the estate — MINUS the session
         records, excluded by ruling (2026-08-10, see RECORDS_GLOBS below).
  reply  a Stop hook reading `last_assistant_message`, gating the replies the
         principal actually reads — the surface where all four defects were
         measured, and the surface no floor has ever reached.

The second plane is the point. Committed doctrine is not where the trust was
lost; it was lost in chat, one unreadable reply at a time, across every repo.

WARN-FIRST, LIKE EVERY FIRST-OF-KIND SCANNER HERE
--------------------------------------------------
This lands advisory. wrapscan and spellscan did the same and for the same
reason: a brand-new prose rule meeting a corpus written before it existed will
find hundreds of true positives, and a gate that reds every commit on day one
teaches people to pass --no-verify, which is worse than no gate. The registry
entry carries `warn_only` until the principal rules on the two house numbers
and the backlog is worked down.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# --- the two house numbers (P3, P4) --------------------------------------
# Declared, not derived. See the P3 note above: no plain-language authority
# checked publishes a sentence cap, so this is the house's own call and the
# principal's to set. Changing these is a doctrine change, not a tuning knob.
SENTENCE_LIMIT = 35      # words; a sentence longer than this is a finding
ASIDE_LIMIT = 40         # chars inside the brackets, mid-sentence only

# Reference-ID shape: one to three capitals then one to three digits, as a
# whole token. Catches F1, C5, SL2, EP3, B14, ADR? no — "ADR 0005" has a space
# and a four-digit number, and is a named document class, not a bare pointer.
RE_REFID = re.compile(r'(?<![\w/#.-])([A-Z]{1,3}\d{1,3})(?![\w.-])')
RE_ACRONYM = re.compile(r'(?<![\w])([A-Z]{2,6})(?![\w])')

# Acronyms that are not jargon to any reader this doctrine has. Deliberately
# short: the test is not "is it well known" but "would this reader stop". When
# in doubt a term belongs in GLOSSARY.md, which is the designed escape.
COMMON_ACRONYMS = frozenset("""
OK API CLI URL URI ID IDS UI UX CI CD PR PRS OS IO HTTP HTTPS JSON YAML XML
HTML CSS SQL SSH TLS SSL DNS IP TCP UDP VPN RAM CPU GPU USB PDF CSV PNG JPG
SVG GIT NZ NZD UTC ISO PC MAC AWS GCP LLM AI ML MB GB KB TB TODO FIXME NOTE
README ADR OK NA AM PM EOF ASCII UTF UUID SHA MD HEAD DIFF ADD
""".split())

# Structural markdown words that the acronym regex sees as acronyms because
# they are shouted, not because they are jargon. This list is the FALLBACK
# half of the emphasis test; `_is_shouted_prose` below is the general half.
SHOUTED_PROSE = frozenset("""
PASS FAIL MAJOR MEDIUM LOW HIGH DONE OPEN CLOSED BLOCKED WARN ERROR INFO DEBUG
YES NO NOT AND OR IF THE TO IS IT AS AT BY IN ON OF SO DO BE WE US ME MY UP GO
ALL ONE TWO NEW OLD NEVER ALWAYS ONLY MUST STOP WHY WHAT HOW WHO WHEN ABOVE
BELOW EACH BOTH THIS THAT THEN ELSE ANY EVERY SAME OWN VERY REAL FULL HALF
""".split())

# A word this house shouts for emphasis is not jargon, and the general test is
# cheaper than maintaining a list: an all-caps token that ALSO appears in the
# same text in ordinary casing is emphasis. "ABOVE" beside "above" is emphasis;
# "MNDP" with no lowercase twin is an acronym. The system dictionary sharpens
# this where it exists, and its absence degrades to the list above rather than
# passing silently — a missing wordlist must not widen what counts as plain.
_DICT_CACHE: frozenset[str] | None = None


def _system_words() -> frozenset[str]:
    global _DICT_CACHE
    if _DICT_CACHE is None:
        words: set[str] = set()
        for p in ("/usr/share/dict/words", "/usr/dict/words"):
            f = Path(p)
            if f.is_file():
                try:
                    words = {w.strip().upper() for w in
                             f.read_text(errors="replace").splitlines() if w.strip()}
                except OSError:
                    words = set()
                break
        _DICT_CACHE = frozenset(words)
    return _DICT_CACHE


def _is_shouted_prose(acr: str, text: str) -> bool:
    if acr in SHOUTED_PROSE:
        return True
    if re.search(rf'(?<![\w]){re.escape(acr.capitalize())}(?![\w])', text):
        return True
    if re.search(rf'(?<![\w]){re.escape(acr.lower())}(?![\w])', text):
        return True
    return acr in _system_words() and len(acr) >= 4


@dataclass
class Finding:
    rule: str
    line: int
    excerpt: str
    detail: str
    path: str = ""

    def as_dict(self) -> dict:
        return {"rule": self.rule, "path": self.path, "line": self.line,
                "detail": self.detail, "excerpt": self.excerpt}


@dataclass
class Tally:
    findings: list[Finding] = field(default_factory=list)
    allowed: int = 0

    def by_rule(self) -> dict[str, int]:
        out: dict[str, int] = {}
        for f in self.findings:
            out[f.rule] = out.get(f.rule, 0) + 1
        return out


# --- markdown stripping ---------------------------------------------------
# Every rule below reads PROSE. Code, links, and tables are not prose, and a
# scanner that cannot tell the difference is the fail-loud half of a scanner
# nobody trusts. Positions are preserved (same-length replacement) so line
# numbers survive the strip.

RE_FENCE = re.compile(r'^\s*(```|~~~)')
RE_INLINE_CODE = re.compile(r'`[^`\n]*`')
RE_MD_LINK = re.compile(r'\[([^\]\n]*)\]\([^)\n]*\)')
RE_BARE_URL = re.compile(r'https?://\S+')
RE_HTML_COMMENT = re.compile(r'<!--.*?-->', re.S)


def _blank(m: re.Match) -> str:
    return " " * len(m.group(0))


def _keep_link_text(m: re.Match) -> str:
    """Keep a link's visible text, blank its target — the reader reads one."""
    text = m.group(1)
    return text + " " * (len(m.group(0)) - len(text))


def prose_lines(text: str) -> list[tuple[int, str]]:
    """Yield (1-based line number, prose-only text) for each prose line.

    Dropped entirely: fenced code, indented code, tables, headings, HTML
    comments (scanner directives live there), and blockquote markers are
    stripped but their content kept — a quote of the principal is prose the
    reader still reads.
    """
    text = RE_HTML_COMMENT.sub(_blank, text)
    out: list[tuple[int, str]] = []
    in_fence = False
    for i, raw in enumerate(text.splitlines(), start=1):
        if RE_FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if raw.startswith("    ") or raw.startswith("\t"):
            continue                                   # indented code block
        line = raw
        stripped = line.lstrip()
        if stripped.startswith("|") or re.match(r'^\s*\|?[-: |]+\|[-: |]*$', line):
            continue                                   # table row / separator
        if stripped.startswith("#"):
            continue                                   # heading: not a sentence
        line = re.sub(r'^\s*>+\s?', lambda m: " " * len(m.group(0)), line)
        line = RE_INLINE_CODE.sub(_blank, line)
        line = RE_MD_LINK.sub(_keep_link_text, line)
        line = RE_BARE_URL.sub(_blank, line)
        if line.strip():
            out.append((i, line))
    return out


def paragraphs(lines: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Join wrapped prose lines into (start line, paragraph) pairs.

    Sentence rules need the whole sentence, and a wrapped markdown paragraph
    splits sentences across lines. A list item starts a new paragraph; a bare
    continuation line does not.
    """
    out: list[tuple[int, str]] = []
    buf: list[str] = []
    start = 0
    prev_no = -10
    for no, line in lines:
        starts_item = bool(re.match(r'^\s*([-*+]|\d+\.)\s', line))
        if buf and (starts_item or no != prev_no + 1):
            out.append((start, " ".join(buf)))
            buf = []
        if not buf:
            start = no
        buf.append(line.strip())
        prev_no = no
    if buf:
        out.append((start, " ".join(buf)))
    return out


RE_SENT_SPLIT = re.compile(r'(?<=[.!?:])\s+(?=[A-Z"“\'—*])|\s+·\s+')


def sentences(par: str) -> list[str]:
    """Split a paragraph into sentences.

    Deliberately generous about what ends one. A colon before a capital, and a
    mid-dot separator, both end a readable unit here even though a grammarian
    would disagree — the rule is about how far the reader must carry the
    sentence in their head, not about grammar.
    """
    par = re.sub(r'^\s*([-*+]|\d+\.)\s+', '', par)
    return [s.strip() for s in RE_SENT_SPLIT.split(par) if s.strip()]


def word_count(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’‑-]*", s))


# --- the rules ------------------------------------------------------------

# What counts as a gloss immediately after the code. Note what is ABSENT: a
# bare "is". "F1 is the missing stamp" defines it, but "F1 is open" and "F1 is
# still blocked" do not, and no cheap pattern separates the two — the tests
# caught the scanner reading a status as a definition. Dropping "is" costs the
# occasional false positive on a real inline definition; the remedy for that is
# the house's own preferred form anyway, an em-dash: "F1 — the missing stamp".
RE_GLOSS_AFTER = re.compile(r'^\s*(?:[—–:(\-]|\bmeans\b|\bcovers\b|\brefers\b|=)')


def _refid_defined_in(text: str, rid: str) -> bool:
    """Does the document define this ID anywhere the reader can find it?

    Two accepted forms, both real in this estate: a table row that opens with
    the ID (`| F1 | ... |`), and a bold or list definition (`**F1** — ...`).
    A definition ANYWHERE in the document counts, not only before first use —
    a findings table below the summary is a legitimate layout, and a reader
    who scrolls finds it.
    """
    pats = [
        rf'^\s*\|\s*\**{re.escape(rid)}\**\s*[‑-]?\s*\w*\s*\|',   # table row
        rf'^\s*[-*+]\s+\**{re.escape(rid)}\**\s*[—–:\-]',          # list def
        rf'\*\*{re.escape(rid)}\**\s*[—–:]',                        # bold def
        rf'^\s*#{{1,6}}\s.*\b{re.escape(rid)}\b',                        # heading
    ]
    return any(re.search(p, text, re.M) for p in pats)


def _acronym_expanded(text: str, acr: str) -> bool:
    """`Some Long Name (ACR)` or `ACR (some long name)` anywhere in the text."""
    if re.search(rf'\(\s*{re.escape(acr)}s?\s*\)', text):
        return True
    if re.search(rf'\b{re.escape(acr)}\b\s*\([^)]{{4,}}\)', text):
        return True
    return False


def _load_glossary(root: Path) -> set[str]:
    """Terms already defined canonically in the repo, in any casing.

    An acronym with a glossary entry is expanded as far as the reader is
    concerned: there is one place to look and it is named in the doctrine.
    """
    terms: set[str] = set()
    for rel in ("docs/method/GLOSSARY.md", "docs/GLOSSARY.md", "GLOSSARY.md"):
        p = root / rel
        if not p.is_file():
            continue
        try:
            body = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in re.finditer(r'\*\*([^*]+)\*\*', body):
            for tok in re.findall(r'[A-Za-z][A-Za-z0-9-]*', m.group(1)):
                terms.add(tok.upper())
    return terms


def scan_text(text: str, *, path: str = "", glossary: set[str] | None = None,
              sentence_limit: int = SENTENCE_LIMIT,
              aside_limit: int = ASIDE_LIMIT,
              rules: set[str] | None = None) -> list[Finding]:
    """The whole rule engine. Both planes call exactly this."""
    glossary = glossary or set()
    active = rules or {"P1", "P2", "P3", "P4"}
    found: list[Finding] = []
    lines = prose_lines(text)
    pars = paragraphs(lines)

    seen_ids: set[str] = set()
    seen_acr: set[str] = set()

    for start, par in pars:
        # P1 / P2 — first use, per document
        if "P1" in active:
            for m in RE_REFID.finditer(par):
                rid = m.group(1)
                if rid in seen_ids:
                    continue
                seen_ids.add(rid)
                tail = par[m.end():m.end() + 160]
                if RE_GLOSS_AFTER.match(tail) or _refid_defined_in(text, rid):
                    continue
                found.append(Finding(
                    "P1", start, _excerpt(par, m.start()),
                    f"reference '{rid}' used with nothing saying what it refers to"))
        if "P2" in active:
            for m in RE_ACRONYM.finditer(par):
                acr = m.group(1)
                if acr in seen_acr or acr in COMMON_ACRONYMS:
                    continue
                if acr.upper() in glossary or _is_shouted_prose(acr, text):
                    continue
                seen_acr.add(acr)
                if _acronym_expanded(text, acr):
                    continue
                found.append(Finding(
                    "P2", start, _excerpt(par, m.start()),
                    f"acronym '{acr}' never expanded and not in the glossary"))

        for sent in sentences(par):
            if "P3" in active:
                n = word_count(sent)
                if n > sentence_limit:
                    found.append(Finding(
                        "P3", start, sent[:160],
                        f"sentence runs {n} words (limit {sentence_limit})"))
            if "P4" in active:
                for m in re.finditer(r'\(([^()]+)\)', sent):
                    inner = m.group(1)
                    if len(inner) <= aside_limit:
                        continue
                    tail = sent[m.end():].strip()
                    # sentence-FINAL asides are fine: the reader has already
                    # landed the sentence before the bracket opens.
                    if tail in ("", ".", ",", ";", ":", "!", "?"):
                        continue
                    found.append(Finding(
                        "P4", start, _excerpt(sent, m.start()),
                        f"{len(inner)}-char aside buried mid-sentence "
                        f"(limit {aside_limit})"))
    for f in found:
        f.path = path
    return found


def _excerpt(s: str, at: int, span: int = 70) -> str:
    lo = max(0, at - span // 3)
    return ("…" if lo else "") + s[lo:lo + span].strip() + ("…" if lo + span < len(s) else "")


# --- repo plane -----------------------------------------------------------

# THE RECORDS EXCLUSION (ruled 2026-08-10). Session records are append-only
# history written for the next session's agent; the prose the principal reads
# in a repo is the doctrine, the ruling asks, and the review briefs. The
# principal opened by proposing removal of the repo plane altogether on that
# audience argument, and the accepted counter-recommendation was this scoping
# instead: keep the floor under human-read docs, stop warning about archives
# nobody may rewrite — the backlog item already called rewriting records
# dishonest, so a warning there has no possible fix and is pure noise.
# The exclusion binds only when a directory is EXPANDED (the floor passes
# `docs`); a records file named explicitly as a path argument is scanned,
# because an explicit selection is a question deserving an answer.
RECORDS_GLOBS = ["docs/SESSIONS.md", "docs/sessions", "docs/ROADMAP-DONE.md"]


def load_ignore_globs(root: Path) -> list[str]:
    p = root / ".plainscanignore"
    if not p.is_file():
        return []
    globs = []
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            globs.append(line)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or rel.startswith(g.rstrip("/") + "/")
               for g in globs)


def iter_markdown(paths: list[Path], root: Path, globs: list[str],
                  include_records: bool = False):
    for p in paths:
        expanded = p.is_dir()
        cands = sorted(p.rglob("*.md")) if expanded else ([p] if p.suffix == ".md" else [])
        for f in cands:
            try:
                rel = str(f.resolve().relative_to(root.resolve()))
            except ValueError:
                rel = str(f)
            if _ignored(rel, globs) or ".git/" in rel:
                continue
            if expanded and not include_records and _ignored(rel, RECORDS_GLOBS):
                continue
            yield f, rel


def scan_paths(paths: list[Path], root: Path, *,
               include_records: bool = False, **kw) -> Tally:
    globs = load_ignore_globs(root)
    glossary = _load_glossary(root)
    tally = Tally()
    for f, rel in iter_markdown(paths, root, globs,
                                include_records=include_records):
        try:
            body = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        tally.findings.extend(scan_text(body, path=rel, glossary=glossary, **kw))
    return tally


RULE_NAMES = {
    "P1": "undefined reference",
    "P2": "unexpanded acronym",
    "P3": "long sentence",
    "P4": "buried aside",
}


def render_human(tally: Tally, limit: int = 6) -> str:
    """Human output, deliberately SHORT by default.

    The first run of this scanner on atelier printed 7,379 findings into the
    pre-commit output. A gate that floods the commit path gets scrolled past,
    and then every check above it gets scrolled past too — which is precisely
    the "written down, therefore assumed working" failure this scanner exists
    to catch, reproduced by the scanner itself on its first outing.

    So the default is a tally plus the worst few files, and `--limit` is how
    you ask for the list. The count is never hidden; only the recitation is.
    """
    if not tally.findings:
        return "plainscan: clean — prose is readable on first pass."
    out = []
    counts = tally.by_rule()
    head = "  ".join(f"{k} {RULE_NAMES[k]} ×{v}" for k, v in sorted(counts.items()))
    out.append(f"plainscan: {len(tally.findings)} finding(s) — {head}")

    by_path: dict[str, int] = {}
    for f in tally.findings:
        if f.path:
            by_path[f.path] = by_path.get(f.path, 0) + 1
    if by_path:
        worst = sorted(by_path.items(), key=lambda kv: -kv[1])[:3]
        out.append("  heaviest: " + " · ".join(f"{p} ×{n}" for p, n in worst))

    for f in tally.findings[:limit]:
        loc = f"{f.path}:{f.line}" if f.path else f"line {f.line}"
        out.append(f"  [{f.rule}] {loc} — {f.detail}")
        out.append(f"        {f.excerpt}")
    if len(tally.findings) > limit:
        out.append(f"  … {len(tally.findings) - limit} more — "
                   f"`plainscan --limit 0` for all, `--json` for the set.")
    return "\n".join(out)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="plainscan",
        description="Check prose for the four plain-language defects measured "
                    "across this estate's transcripts (COMMUNICATION.md).")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: <root>/docs if present)")
    ap.add_argument("--root", default=".", help="repo root for ignores and rel paths")
    ap.add_argument("--warn", action="store_true",
                    help="report findings but always exit 0 (warn-first rollout)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--sentence-limit", type=int, default=SENTENCE_LIMIT,
                    help=f"words per sentence (default {SENTENCE_LIMIT}; house call)")
    ap.add_argument("--aside-limit", type=int, default=ASIDE_LIMIT,
                    help=f"chars in a mid-sentence bracket (default {ASIDE_LIMIT})")
    ap.add_argument("--rules", default="P1,P2,P3,P4",
                    help="comma-separated subset of P1,P2,P3,P4")
    ap.add_argument("--include-records", action="store_true",
                    help="also scan the session records (docs/SESSIONS.md, "
                         "docs/sessions/, docs/ROADMAP-DONE.md), excluded by "
                         "default since the 2026-08-10 ruling — they are "
                         "append-only history for the next session, not prose "
                         "the principal reads. A records file named explicitly "
                         "as a path argument is always scanned.")
    ap.add_argument("--limit", type=int, default=6, metavar="N",
                    help="findings to print in full (default 6; 0 = all). The "
                         "tally is always printed — this caps the recitation, "
                         "so the floor's other checks stay readable.")
    ap.add_argument("--selftest", action="store_true", help="run built-in checks")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root)
    if not root.is_dir():
        print(f"plainscan: root does not exist: {args.root}", file=sys.stderr)
        return 2
    if args.paths:
        targets = [Path(p) for p in args.paths]
        missing = [str(p) for p in targets if not p.exists()]
        if missing:
            print(f"plainscan: path does not exist: {', '.join(missing)}", file=sys.stderr)
            return 2
    else:
        targets = [root / "docs"] if (root / "docs").is_dir() else [root]

    rules = {r.strip().upper() for r in args.rules.split(",") if r.strip()}
    bad = rules - set(RULE_NAMES)
    if bad:
        print(f"plainscan: unknown rule(s): {', '.join(sorted(bad))}", file=sys.stderr)
        return 2

    tally = scan_paths(targets, root, include_records=args.include_records,
                       sentence_limit=args.sentence_limit,
                       aside_limit=args.aside_limit, rules=rules)

    if args.json:
        print(json.dumps({
            "scanner": "plainscan",
            "findings": [f.as_dict() for f in tally.findings],
            "counts": tally.by_rule(),
            "warn": args.warn,
        }, indent=2))
    else:
        print(render_human(tally, limit=len(tally.findings) if args.limit == 0
                           else args.limit))
        if tally.findings and args.warn:
            print("\n  (--warn: advisory only — not blocking this build.)")

    if args.warn:
        return 0
    return 1 if tally.findings else 0


# --- selftest -------------------------------------------------------------

def _selftest() -> int:
    ok = True

    def check(name: str, cond: bool):
        nonlocal ok
        if not cond:
            print(f"FAIL: {name}")
            ok = False

    # P1: bare vs glossed vs table-defined
    bare = "The ruling closes F1 and we move on to the next batch of work."
    check("P1 flags a bare reference",
          any(f.rule == "P1" for f in scan_text(bare)))
    glossed = "The ruling closes F1 — the missing UTC stamp — and we move on."
    check("P1 accepts an inline gloss",
          not any(f.rule == "P1" for f in scan_text(glossed)))
    tabled = "The ruling closes F1 and we move on.\n\n| F1 | the missing stamp |\n"
    check("P1 accepts a table definition",
          not any(f.rule == "P1" for f in scan_text(tabled)))

    # P2: acronyms
    check("P2 flags an unexpanded acronym",
          any(f.rule == "P2" for f in scan_text("We rely on MNDP for discovery here.")))
    check("P2 accepts an expansion",
          not any(f.rule == "P2" for f in
                  scan_text("MikroTik Neighbor Discovery Protocol (MNDP) finds them.")))
    check("P2 accepts a glossary term",
          not any(f.rule == "P2" for f in
                  scan_text("We rely on MNDP here.", glossary={"MNDP"})))
    check("P2 ignores common acronyms",
          not any(f.rule == "P2" for f in scan_text("The CLI writes JSON to the API.")))

    # P3: sentence length
    long_s = "word " * 40 + "end."
    check("P3 flags a 41-word sentence", any(f.rule == "P3" for f in scan_text(long_s)))
    check("P3 passes a short sentence",
          not any(f.rule == "P3" for f in scan_text("This sentence is short.")))
    check("P3 honours a raised limit",
          not any(f.rule == "P3" for f in scan_text(long_s, sentence_limit=60)))

    # P4: asides
    buried = ("The scanner runs on the hook (which reads only the staged diff, "
              "so the commit path stays fast) and blocks the commit.")
    check("P4 flags a buried aside", any(f.rule == "P4" for f in scan_text(buried)))
    final = ("The scanner runs on the hook and blocks the commit "
             "(it reads only the staged diff, so the commit path stays fast).")
    check("P4 accepts a sentence-final aside",
          not any(f.rule == "P4" for f in scan_text(final)))
    check("P4 accepts a short gloss",
          not any(f.rule == "P4" for f in
                  scan_text("The hook (staged only) blocks the commit here.")))

    # structural: code and tables are not prose
    fenced = "```\nF1 MNDP " + "word " * 50 + "\n```\n"
    check("code fences are not prose", not scan_text(fenced))
    check("headings are not sentences",
          not any(f.rule == "P3" for f in scan_text("# " + "word " * 50)))
    inline = "Run `plainscan --rules P1` to check.\n"
    check("inline code is not prose", not scan_text(inline))

    # exit codes, against a real tree — the plane the hook actually runs
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "docs").mkdir()
        (root / "docs" / "bad.md").write_text(
            "The ruling closes F1 and we move on to the next item.\n",
            encoding="utf-8")
        check("findings exit 1 without --warn", _main(["--root", td]) == 1)
        check("findings exit 0 with --warn", _main(["--root", td, "--warn"]) == 0)
        (root / "docs" / "bad.md").write_text("All clear here.\n", encoding="utf-8")
        check("a clean tree exits 0", _main(["--root", td]) == 0)
        check("a missing root exits 2", _main(["--root", td + "/nope"]) == 2)

    # the records exclusion (ruled 2026-08-10)
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "docs" / "sessions").mkdir(parents=True)
        bad = "The ruling closes F1 and we move on to the next item.\n"
        for rel in ("docs/SESSIONS.md", "docs/sessions/one.md",
                    "docs/ROADMAP-DONE.md"):
            (root / rel).write_text(bad, encoding="utf-8")
        check("records are excluded by default", _main(["--root", td]) == 0)
        check("--include-records selects them",
              _main(["--root", td, "--include-records"]) == 1)
        check("an explicit records path is still scanned",
              _main(["--root", td, str(root / "docs" / "SESSIONS.md")]) == 1)

    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    try:
        return _main(argv)
    except KeyboardInterrupt:
        return 130
    except OSError as e:
        print(f"plainscan: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
