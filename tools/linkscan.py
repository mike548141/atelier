#!/usr/bin/env python3
"""linkscan — the mechanical check that atelier's internal links resolve.

atelier's whole architecture is "thin anchor, fat pointer" (PROPAGATION.md): a
child inlines a safety floor and *points up* to the canonical doctrine; a doc
states a bearing and *points* to the case-law. That design is only as sound as
its pointers. A relative link that 404s — a renamed file, a moved doc, a typo'd
anchor — is a silent hole in the doctrine graph: the reader is told "see X" and X
isn't there. Intent doesn't catch that; a machine does. This is the machine.

Scope, deliberately narrow (a broad flaky tool is worse than a sharp honest one):

  * INTERNAL links only. `[text](path)` and `![alt](path)` whose destination is a
    relative or root-relative path. External schemes (http, https, mailto, tel,
    ftp…) and protocol-relative `//host` are SKIPPED — verifying them means the
    network, which is flaky, slow, and a different tool's job.

  * FILE existence — the destination path must resolve to a real file or dir,
    relative to the linking file (or the repo root for a leading `/` — GitHub
    resolves those against the repository root too). The on-disk name must match
    the link's case exactly (a case-insensitive local filesystem hides a
    mismatch that a case-sensitive host 404s), and the target must live inside
    the scan root (GitHub cannot serve anything above the repository root).

  * ANCHOR existence — for a `#fragment` into a Markdown file (or same-file), the
    fragment must match a heading anchor **exactly** — GitHub fragment matching
    is exact, so `#A-Section` does not reach `#a-section`. Both ATX (`#`) and
    setext (underline `===`/`---`) headings mint anchors. `#L42`-style line
    anchors are line references, not headings, and are skipped. Anchors into
    non-Markdown targets aren't validated (nothing to validate against).

Links inside fenced (``` ```) or inline (`` `…` ``) code are ignored — they are
examples, not live pointers. Wiki-style `[[name]]` memory links are NOT Markdown
links (no `](`) and are out of scope by design.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean
  1  broken link(s) found
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can run
it with the system python3 and no install — and CI needs nothing but Python.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field, asdict
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

# A line carrying this marker is intentionally exempt (e.g. a deliberately
# dangling pointer in a doc, or a template placeholder). Keep the reason on the
# same line so the exemption is self-documenting and greppable.
ALLOW_MARKER = "linkscan:allow"

ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER) + r"(?::(?P<rule>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>[\w\"\'“‘])")


def parse_allow(line: str) -> str | None:
    """The scope of the line's allow-marker, or None if it carries none.

    `""` means every rule on the line; a rule name means just that one. A
    marker with no reason returns None — it is a mention, not an exemption
    (`method/GUARDS.md`, rule c)."""
    m = ALLOW_RX.search(line)
    if not m:
        return None
    return m.group("rule") or ""


@dataclass
class Tally:
    """What the scan removed AFTER finding it — rule (b) of `method/GUARDS.md`.

    A guard that subtracts silently prints the same clean tick for "nothing
    matched" and "everything matched and was exempted"."""
    by_marker: dict[str, int] = field(default_factory=dict)
    files_by_glob: int = 0

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def note_marker(self, rule: str) -> None:
        self.by_marker[rule] = self.by_marker.get(rule, 0) + 1

    def summary(self) -> str:
        """One stable line, known zeros printed, so two runs compare."""
        line = ("  suppressed: "
                f"{self.marker_total} by allow-marker · "
                f"{self.files_by_glob} file(s) by .linkscanignore")
        if self.by_marker:
            detail = ", ".join(f"{r}×{n}" for r, n in sorted(self.by_marker.items()))
            line += f"\n    allow-marker breakdown: {detail}"
        return line


# Only these extensions are parsed for links and headings; everything else is a
# link *target* (checked for existence) but never a *source*.
MARKDOWN_SUFFIXES = {".md", ".markdown"}

# Paths never worth walking. Hardcode-skip ONLY names that are never
# human-authored prose — VCS, dependency, and tool-cache dirs. Ambiguous names
# a content dir can legitimately share (`build`, `dist`) are DELIBERATELY absent:
# atelier's own `docs/build/` is a first-class doctrine layer, and skipping it by
# name silently masked 14 files from every whole-tree scan — a false negative,
# linkscan's cardinal sin. The tool cannot tell "build output" from "content
# named build" by name alone, so it must not guess; a repo with a real
# build-output dir names it in `.linkscanignore` (one line). Over-scanning a
# generated dir is cheap; masking a doctrine layer is not.
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

# A URI scheme (http:, mailto:, tel:…) or a protocol-relative //host prefix:
# not our link to check.
_SCHEME = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.\-]*:|//)")

# `#L12` or `#L12-L20`: a GitHub line reference into source, not a heading.
_LINE_ANCHOR = re.compile(r"^L\d+(?:-L\d+)?$")

# An inline Markdown link/image destination: `](dest)` or `](dest "title")`,
# where dest is either <bracketed> (may hold spaces) or a bare run of non-space
# chars allowing one level of balanced parens (`a(1).md` is a legal filename).
_LINK = re.compile(
    r"!?\]\(\s*(<[^>]*>|(?:[^()\s]|\([^()\s]*\))+)(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)")

# An ATX heading line: leading #'s then the text (trailing #'s stripped).
_ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")

# A fence delimiter: 3+ backticks or tildes at (possibly indented) line start.
_FENCE = re.compile(r"^(`{3,}|~{3,})")

# A setext underline (`===` / `---`), and a line that cannot be the heading
# *text* above one (list/quote/table/heading/rule shapes — conservative: a
# skipped setext heading costs at worst one allow-marker on an exotic link).
_SETEXT_UNDERLINE = re.compile(r"^ {0,3}(=+|-+)\s*$")
_NOT_SETEXT_TEXT = re.compile(r"^\s*(?:[#>|]|[-*+]\s|\d+[.)]\s)")


@dataclass
class Finding:
    path: str          # the linking Markdown file (repo-relative)
    line: int
    kind: str          # "missing-file" | "missing-anchor" | "outside-root"
    target: str        # the raw link destination, as written
    detail: str        # human hint at what's missing
    suggest: str = ""  # a computed replacement path, or "" when none is certain


def slugify(heading: str) -> str:
    """GitHub's heading-anchor slug: strip inline formatting, lowercase, drop
    punctuation (keeping word chars, spaces, hyphens), spaces→hyphens. Good
    enough for the ATX headings atelier writes; deliberately not a full CommonMark
    renderer (an exotic heading that mis-slugs costs one `linkscan:allow`)."""
    text = heading.strip()
    # Unwrap the commonest inline formatting so `` `foo` `` / `**foo**` /
    # `[foo](x)` slug to their visible text, matching GitHub. Underscores are
    # emphasis only when they flank a word (`_emph_`); a literal `snake_case`
    # keeps its underscores — GitHub's slugs keep them too (`\w` covers `_`).
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"(?<!\w)_+([^_]+?)_+(?!\w)", r"\1", text)
    text = re.sub(r"[*~]", "", text)
    text = text.lower()
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    text = text.replace(" ", "-")
    return text


def _content_lines(text: str):
    """Yield (lineno, line) for lines outside fenced code blocks. One tracker
    for both link extraction and heading collection, so the two can never
    drift. CommonMark-faithful where it bites: a fence closes only on a run of
    the *same* character at least as long as the opener (so a ``` inside a
    ```` block stays code), and a closing fence carries no info string (so a
    ```python line inside an open ``` block is content, not a close)."""
    in_fence = False
    fence_char = ""
    fence_len = 0
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        m = _FENCE.match(stripped)
        if in_fence:
            if m and m.group(1)[0] == fence_char and len(m.group(1)) >= fence_len \
                    and stripped.rstrip() == m.group(1):
                in_fence = False
            continue
        if m:
            in_fence = True
            fence_char = m.group(1)[0]
            fence_len = len(m.group(1))
            continue
        yield lineno, line


def heading_slugs(text: str) -> set[str]:
    """Every anchor GitHub would mint for this Markdown file's headings —
    ATX (`#`) and setext (a paragraph line underlined with `===`/`---`) —
    including the `-1`, `-2` disambiguation suffixes for repeated headings.
    Headings inside fenced code blocks are not headings."""
    slugs: set[str] = set()
    counts: dict[str, int] = {}

    def add(heading: str) -> None:
        base = slugify(heading)
        n = counts.get(base, 0)
        counts[base] = n + 1
        slugs.add(base if n == 0 else f"{base}-{n}")

    prev_text: str | None = None   # candidate setext heading text
    prev_lineno = -2
    for lineno, line in _content_lines(text):
        m = _ATX.match(line)
        if m:
            add(m.group(2))
            prev_text = None
            continue
        if _SETEXT_UNDERLINE.match(line) and prev_text is not None \
                and prev_lineno == lineno - 1:
            add(prev_text)
            prev_text = None
            continue
        stripped = line.strip()
        if stripped and not _SETEXT_UNDERLINE.match(line) \
                and not _NOT_SETEXT_TEXT.match(line):
            prev_text, prev_lineno = stripped, lineno
        else:
            prev_text = None
    return slugs


def _strip_inline_code(line: str) -> str:
    """Blank out inline `code spans` so a link-shaped example inside them isn't
    read as a live link. Backtick runs must match in length (CommonMark)."""
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        if line[i] == "`":
            j = i
            while j < n and line[j] == "`":
                j += 1
            ticks = line[i:j]
            close = line.find(ticks, j)
            if close != -1 and line[close:close + len(ticks)] == ticks \
                    and (close + len(ticks) >= n or line[close + len(ticks)] != "`"):
                out.append(" " * (close + len(ticks) - i))
                i = close + len(ticks)
                continue
        out.append(line[i])
        i += 1
    return "".join(out)


def iter_links(text: str, allow_by_line: dict[int, str] | None = None):
    """Yield (lineno, raw_destination) for every inline link/image destination
    in a Markdown file, skipping fenced and inline code. Allow-markered lines
    are still yielded: the finding is formed first and subtracted afterwards
    (`method/GUARDS.md`, rule b), so the exemption can be counted. Scopes are
    recorded into `allow_by_line` for the caller to apply."""
    for lineno, line in _content_lines(text):
        scope = parse_allow(line)
        if scope is not None and allow_by_line is not None:
            allow_by_line[lineno] = scope
        for m in _LINK.finditer(_strip_inline_code(line)):
            dest = m.group(1).strip()
            if dest.startswith("<") and dest.endswith(">"):
                dest = dest[1:-1].strip()
            yield lineno, dest


def is_external(dest: str) -> bool:
    return bool(_SCHEME.match(dest))


def split_target(dest: str) -> tuple[str, str]:
    """(path, anchor) for a link destination. A leading `#` means same-file."""
    path, _, anchor = dest.partition("#")
    return unquote(path), anchor


def resolve(md_file: Path, root: Path, path: str) -> Path:
    """Resolve a link's path part to a filesystem path: root-relative for a
    leading `/` (GitHub resolves those against the repository root), else
    relative to the linking file's directory."""
    if path.startswith("/"):
        return (root / path.lstrip("/"))
    return (md_file.parent / path)


def _suggest(md_file: Path, root: Path, path: str) -> str:
    """A replacement path for a link that didn't resolve, or "" if none is
    certain. Suggestions are advisory text only — they never change a verdict
    or an exit code, and nothing rewrites a file.

    Two tiers, both requiring a *unique* answer, because a confident wrong
    suggestion costs more than none at all:

    1. The path resolves from the **repository root**. This is the commonest
       break by a wide margin: a root-relative path written inside a file two
       levels down (`tools/x.py` in `docs/method/`) resolves to
       `docs/method/tools/x.py` and 404s, when the writer meant the repo root.
       The correct target is fully computable, so compute it.
    2. Exactly **one** file anywhere under the root carries that basename —
       the moved-or-renamed case. Two or more matches means guessing which,
       so it stays silent.
    """
    if not path or path.startswith("/"):
        return ""            # already root-relative: tier 1 IS the written form
    # Tier 1 — did they mean it relative to the repo root?
    from_root = root / path
    if from_root.exists():
        rel = os.path.relpath(from_root.resolve(), start=md_file.parent.resolve())
        return rel if rel != path else ""
    # Tier 2 — a unique basename match elsewhere in the tree.
    name = PurePosixPath(path).name
    if not name or name in (".", ".."):
        return ""
    matches: list[Path] = []
    for cand in root.rglob(name):
        if any(part.startswith(".") for part in cand.relative_to(root).parts):
            continue         # .git, .github and friends are not link targets
        matches.append(cand)
        if len(matches) > 1:
            return ""        # ambiguous — say nothing rather than pick
    if len(matches) != 1:
        return ""
    rel = os.path.relpath(matches[0].resolve(), start=md_file.parent.resolve())
    return rel if rel != path else ""


def _within_root(target: Path, root: Path) -> bool:
    """A link that resolves *above* the scan root exists on this disk but not
    on GitHub — nothing above the repository root is servable."""
    try:
        target.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    except OSError:
        return True    # can't tell — don't invent a break
    return True


def _case_mismatch(target: Path, root: Path) -> str | None:
    """On a case-insensitive filesystem (macOS APFS) `exists()` says yes to a
    wrongly-cased link that a case-sensitive host (GitHub) 404s. Walk the
    on-disk names and return the true casing of the first mismatched component,
    or None if the link's casing is exact. Unicode-normalisation-only
    differences (APFS stores NFD; links are usually NFC) are NOT mismatches."""
    try:
        rel = target.resolve().relative_to(root.resolve())
    except (OSError, ValueError):
        return None
    cur = root.resolve()
    nfc = unicodedata.normalize
    for part in rel.parts:
        try:
            names = os.listdir(cur)
        except OSError:
            return None
        if part in names or nfc("NFD", part) in names or nfc("NFC", part) in names:
            cur = cur / part
            continue
        want = nfc("NFC", part).casefold()
        for name in names:
            if nfc("NFC", name).casefold() == want:
                return name
        return None    # exists() said yes but we can't identify why — don't flag
    return None


def _check_anchor(rel: str, lineno: int, dest: str, anchor: str,
                  slugs: set[str], where: str):
    """GitHub fragment matching is exact, so the anchor must equal a minted
    slug verbatim. If a lenient (re-slugged) match exists, the heading is there
    but the anchor as written won't reach it — say so, with the fix."""
    frag = unquote(anchor)
    if frag in slugs:
        return None
    lenient = slugify(frag)
    if lenient in slugs:
        return Finding(rel, lineno, "missing-anchor", dest,
                       f"heading exists but anchors match exactly — write '#{lenient}'")
    return Finding(rel, lineno, "missing-anchor", dest,
                   f"no heading '#{anchor}' {where}")


def check_file(md_file: Path, root: Path, text: str,
               slug_cache: dict[Path, set[str]],
               tally: "Tally | None" = None) -> list[Finding]:
    rel = _rel(md_file, root)
    own_slugs: set[str] | None = None
    findings: list[Finding] = []
    allow_by_line: dict[int, str] = {}
    for lineno, dest in iter_links(text, allow_by_line):
        if not dest or is_external(dest):
            continue
        path, anchor = split_target(dest)

        if path == "":
            # Same-file anchor. `#` alone (top-of-page) always resolves.
            if not anchor or _LINE_ANCHOR.match(anchor):
                continue
            if own_slugs is None:
                own_slugs = heading_slugs(text)
            f = _check_anchor(rel, lineno, dest, anchor, own_slugs, "in this file")
            if f:
                findings.append(f)
            continue

        target = resolve(md_file, root, path)
        if not target.exists():
            findings.append(Finding(rel, lineno, "missing-file", dest,
                                    f"{_rel(target, root)} does not exist",
                                    _suggest(md_file, root, path)))
            continue
        if not _within_root(target, root):
            findings.append(Finding(rel, lineno, "outside-root", dest,
                                    "resolves outside the repo root — a reader "
                                    "on GitHub gets a 404",
                                    _suggest(md_file, root, path)))
            continue
        wrong = _case_mismatch(target, root)
        if wrong is not None:
            findings.append(Finding(rel, lineno, "missing-file", dest,
                                    f"case mismatch — on-disk name is '{wrong}' "
                                    "(a case-sensitive host 404s)"))
            continue

        # Path resolves. Validate a Markdown anchor if one was given.
        if anchor and not _LINE_ANCHOR.match(anchor) \
                and target.is_file() and target.suffix.lower() in MARKDOWN_SUFFIXES:
            key = target.resolve()
            if key not in slug_cache:
                slug_cache[key] = heading_slugs(
                    target.read_text(encoding="utf-8", errors="replace"))
            f = _check_anchor(rel, lineno, dest, anchor, slug_cache[key],
                              f"in {_rel(target, root)}")
            if f:
                findings.append(f)
    # SUBTRACT SECOND (rule b): every finding is fully formed above, so an
    # exemption is counted here rather than vanishing at extraction time.
    kept: list[Finding] = []
    for f in findings:
        scope = allow_by_line.get(f.line)
        if scope is not None and scope in ("", f.kind):
            if tally is not None:
                tally.note_marker(f.kind)
            continue
        kept.append(f)
    return kept


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


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
    """Globs from `.linkscanignore`, each of which MUST carry a stated reason.

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
    f = root / ".linkscanignore"
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
        raise IgnoreFileError(".linkscanignore", unreasoned)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


def iter_markdown(paths: list[Path], root: Path, globs: list[str],
                  tally: "Tally | None" = None):
    for base in paths:
        if base.is_file():
            candidates = [base]
        else:
            candidates = [p for p in base.rglob("*")
                          if p.is_file() and not (SKIP_DIR_NAMES & set(p.parts))]
        for p in candidates:
            if p.suffix.lower() not in MARKDOWN_SUFFIXES:
                continue
            if _ignored(_rel(p, root), globs):
                if tally is not None:
                    tally.files_by_glob += 1
                continue
            yield p


def scan_paths(paths: list[Path], root: Path,
               tally: "Tally | None" = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    slug_cache: dict[Path, set[str]] = {}
    findings: list[Finding] = []
    for md in iter_markdown(paths, root, globs, tally):
        text = md.read_text(encoding="utf-8", errors="replace")
        findings.extend(check_file(md, root, text, slug_cache, tally))
    return findings


def render_human(findings: list[Finding], tally: "Tally | None" = None) -> str:
    if not findings:
        out = "✓ linkscan clean — every internal link resolves."
        return out + ("\n" + tally.summary() if tally is not None else "")
    lines = [f"✗ linkscan: {len(findings)} broken internal link(s).\n"]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.target} → {f.detail}")
        if f.suggest:
            lines.append(f"      ↳ did you mean: {f.suggest}")
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append("\n  A real break: fix the path/anchor (or the moved/renamed target).")
    lines.append(f"  A deliberate dangling pointer: append '<!-- {ALLOW_MARKER}: <reason> -->'")
    lines.append(f"  to the line (or '{ALLOW_MARKER}:<kind>: <reason>' for just one of")
    lines.append("  missing-file/missing-anchor/outside-root), or add a path glob to")
    lines.append("  .linkscanignore. A marker with no reason exempts nothing.")
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="linkscan",
        description="Check that internal Markdown links (paths + anchors) resolve.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo)")
    ap.add_argument("--root", default=".",
                    help="repo root for root-relative (/…) links and .linkscanignore")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"linkscan: root does not exist: {args.root}", file=sys.stderr)
        return 2
    targets = [Path(p) for p in (args.paths or [str(root)])]
    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        # A typo'd path scanning nothing must never read as a clean pass.
        print(f"linkscan: path does not exist: {', '.join(missing)}",
              file=sys.stderr)
        return 2
    tally = Tally()
    try:
        findings = scan_paths(targets, root, tally)
    except OSError as e:
        print(f"linkscan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "findings": [asdict(f) for f in findings],
            "suppressed": {
                "by_allow_marker": tally.marker_total,
                "by_allow_marker_rule": tally.by_marker,
                "files_by_ignore_glob": tally.files_by_glob,
            },
        }, indent=2))
    else:
        print(render_human(findings, tally))

    return 1 if findings else 0


def _selftest() -> int:
    """Minimal smoke test so `linkscan --selftest` proves the engine on any box,
    even where the unittest file isn't shipped. Builds a tiny doc tree in a temp
    dir and asserts the four core behaviours."""
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="linkscan-self-"))
    (tmp / "target.md").write_text("# Real Heading\n\nbody\n")
    (tmp / "index.md").write_text(
        "# Top\n\n"
        "## A Section\n"
        "[ok file](target.md)\n"                       # resolves
        "[ok anchor](target.md#real-heading)\n"        # slug matches
        "[ok same](#a-section)\n"                       # same-file anchor
        "[ok external](https://example.com/x)\n"       # skipped
        "[ok line](target.md#L5)\n"                     # line ref, skipped
        "`[not a link](nope.md)`\n"                     # inline code, skipped
        "[bad file](missing.md)\n"                      # BREAK 1
        "[bad anchor](target.md#ghost)\n"              # BREAK 2
        "[bad same](#no-such)\n"                         # BREAK 3
        "[bad case](#A-Section)\n"                       # BREAK 4 — exact match only
        "```\n[fenced](also-missing.md)\n```\n"        # fenced, skipped
    )
    findings = scan_paths([tmp], tmp)
    kinds = sorted((f.kind, f.target) for f in findings)
    expected = sorted([
        ("missing-file", "missing.md"),
        ("missing-anchor", "target.md#ghost"),
        ("missing-anchor", "#no-such"),
        ("missing-anchor", "#A-Section"),
    ])
    ok = kinds == expected
    if not ok:
        print(f"FAIL: got {kinds}, expected {expected}")
    # slug edge cases
    for heading, want in [("Hello World", "hello-world"),
                          ("`code` & punct!", "code--punct"),
                          ("A—B", "ab"),
                          ("snake_case stays", "snake_case-stays")]:
        got = slugify(heading)
        if got != want:
            print(f"FAIL slug: {heading!r} → {got!r}, expected {want!r}")
            ok = False
    print("selftest OK" if ok else "selftest FAILED")
    import shutil
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1



def main(argv: list[str] | None = None) -> int:
    """Exit 2 on an ignore file that grants an exemption with no reason.

    A broken scan is not a pass (the house exit-code contract), and an
    unexplained exemption makes the scan's own scope untrustworthy."""
    try:
        return _main(argv)
    except IgnoreFileError as e:
        print(f"linkscan: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
