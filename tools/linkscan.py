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

  * REFERENCE-STYLE links, checked at their DEFINITION (`[label]: dest`) rather
    than at their usages. CommonMark's whole reference family — full
    `[text][ref]`, collapsed `[ref][]`, shortcut `[ref]` and image `![alt][ref]`
    — routes through one definition line, so validating definitions covers every
    usage form at once. It also dodges the hazard of the obvious alternative: a
    shortcut-form matcher fires on ordinary prose (`[square brackets]`,
    `arr[0]`, a citation `[1]`). Until 2026-08-23 the whole family was invisible
    — not unresolved, never *extracted* — and a file whose only broken links
    were reference-style reported "every internal link resolves" at exit 0
    (roadmap `020/320`). The residue a definition-only check leaves is the
    **undefined label**: `[text][nope]` with no `[nope]:` line renders as
    literal text rather than a link, and nothing here notices. Named as a limit
    rather than chased, because chasing it needs the usage matcher this design
    exists to avoid. Footnote definitions (`[^1]: …`) are not link definitions
    and are skipped.

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
import codecs
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

# A link reference definition: up to three spaces of indent, `[label]:`, the
# destination, and an OPTIONAL quoted or parenthesised title — then end of line.
#
# THE END ANCHOR IS THE WHOLE GUARD, and it is why this cannot be loosened
# casually. CommonMark says a definition's title must be quoted or in parens, so
# anchoring at `$` is what keeps ordinary prose out: `[note]: this is prose`
# leaves `is prose` unmatched and correctly fails to be a definition, while
# `[note]: word` — one bare token, indistinguishable from a real definition —
# is one. That is the same trade the rest of this tool takes: a shape that
# cannot be told apart from a link IS treated as a link, and the allow-marker
# is the hatch.
#
# A label starting with `^` is a FOOTNOTE definition (`[^1]: text`), not a link
# definition — GitHub's extension, and its body is prose. Excluded at the label
# so a one-word footnote cannot be read as a path.
_LINK_DEF = re.compile(
    r"^ {0,3}\[(?!\^)([^\]]+)\]:\s*"
    r"(<[^>]*>|\S+)"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^()]*\)))?\s*$")

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


class _FenceState:
    """Fence-tracking state, factored out of the old `_content_lines` loop
    body (020/380) so the text-based reader (`_content_lines`, what direct
    string tests and the `heading_slugs`/`iter_links` string API use) and the
    streaming file-based reader (`_iter_file_content_lines`, what real files
    on disk use so a huge one is never held whole) share ONE fence-transition
    rule and can never drift apart. CommonMark-faithful where it bites: a
    fence closes only on a run of the *same* character at least as long as
    the opener (so a ``` inside a ```` block stays code), and a closing fence
    carries no info string (so a ```python line inside an open ``` block is
    content, not a close).

    A fence DELIMITER line is always a handful of characters — three-or-more
    backticks/tildes and nothing else of consequence — so it always resolves
    fully within a single read window, even for a file whose scanning is
    windowed for memory safety. That is what lets the streaming reader only
    call `is_content` on the FIRST window of a physical line (see
    `_iter_file_content_lines`): a line that needed more than one window was
    never a fence delimiter to begin with, so no transition is missed."""

    def __init__(self):
        self.in_fence = False
        self.fence_char = ""
        self.fence_len = 0

    def is_content(self, line: str) -> bool:
        stripped = line.lstrip()
        m = _FENCE.match(stripped)
        if self.in_fence:
            if m and m.group(1)[0] == self.fence_char and len(m.group(1)) >= self.fence_len \
                    and stripped.rstrip() == m.group(1):
                self.in_fence = False
            return False
        if m:
            self.in_fence = True
            self.fence_char = m.group(1)[0]
            self.fence_len = len(m.group(1))
            return False
        return True


def _content_lines(text: str):
    """Yield (lineno, line) for lines outside fenced code blocks, from an
    in-memory string — the shape direct-string tests and the `heading_slugs`/
    `iter_links` string API use. Real files scanned from disk go through
    `_iter_file_content_lines` instead (020/380), which produces the same
    shape without ever holding the whole file at once."""
    state = _FenceState()
    for lineno, line in enumerate(text.splitlines(), start=1):
        if state.is_content(line):
            yield lineno, line


# Streaming-read tuning (020/380, reusing 020/370's WINDOWING shape — see
# `tools/secretscan.py`'s identical mechanism). Every constant is a FIXED
# size, independent of the file or tree being scanned: peak memory for
# reading ANY one file is bounded by `LINE_WINDOW_BYTES + LINE_WINDOW_OVERLAP`,
# never by the file's own size. Duplicated here rather than imported so this
# tool stays self-contained and copyable alone (this module's own stated
# design principle, and secretscan's).
#
# The WINDOW SIZE itself is grounded in THIS tool's own shapes, not copied
# from secretscan's number: secretscan's 4 MiB accounts for a large NAMED
# credential token (a JWT can run to a few KiB, generously multiplied).
# linkscan has no equivalent long-token shape — a link destination, an
# anchor, and a heading are all, by construction, well under a few hundred
# bytes; nothing this tool matches (`_LINK`, `_LINK_DEF`, `_ATX`) is
# open-ended the way a credential is. 256 KiB is already 1000x more
# generous than any real line this format produces. It also keeps the
# per-window footprint small enough that an adversarial file with MANY
# overlong lines does not compound allocator overhead across windows —
# measured while building this fix: a 4 MiB window showed ~76 MB of growth
# between an 8 MiB and a 32 MiB single-line file (repeated large
# allocations retaining fragmented heap, not a single unbounded hold); a
# 256 KiB window showed ~1 MB of growth over the same comparison.
READ_CHUNK_BYTES = 1 * 1024 * 1024        # raw bytes read from disk at a time
LINE_WINDOW_BYTES = 256 * 1024            # a physical line longer than this
                                          # is scanned in WINDOWS instead
LINE_WINDOW_OVERLAP = 4 * 1024            # carried from one window into the
                                          # next so a match straddling the
                                          # cut is still whole in one of them


def _iter_file_content_lines(path: Path):
    """Yield (lineno, line) for lines outside fenced code blocks, reading
    `path` in fixed-size chunks so peak memory is bounded by a constant
    regardless of the file's total size or its longest line (020/380;
    mirrors secretscan's 020/370 fix). Replaces the old whole-file
    `read_text()` -> `text.splitlines()`, which held the file's content and
    its full line list at once — unbounded for a large enough single file.

    STATED RESIDUAL: a physical line longer than `LINE_WINDOW_BYTES` is
    scanned in overlapping windows, and a link/anchor destination whose
    syntax straddles one exact window cut could be missed — the same trade
    secretscan's reader makes. Nothing is dropped SILENTLY: every window is
    still scanned as content (or as fenced, per `_FenceState`); the residual
    is an exotic match at one byte offset inside an implausibly long single
    line, not silence over ordinary content.

    Fence transitions are evaluated only on a physical line's FIRST window —
    see `_FenceState`'s docstring for why that misses nothing."""
    state = _FenceState()
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    lineno = 1
    pending = ""
    first_window_of_line = True
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(READ_CHUNK_BYTES)
            if not chunk:
                break
            pending += decoder.decode(chunk)
            while True:
                nl = pending.find("\n")
                if nl == -1:
                    break
                line = pending[:nl]
                pending = pending[nl + 1:]
                is_content = (state.is_content(line) if first_window_of_line
                             else not state.in_fence)
                if is_content:
                    yield lineno, line
                lineno += 1
                first_window_of_line = True
            if len(pending) >= LINE_WINDOW_BYTES:
                is_content = (state.is_content(pending) if first_window_of_line
                             else not state.in_fence)
                if is_content:
                    yield lineno, pending
                pending = pending[-LINE_WINDOW_OVERLAP:]
                first_window_of_line = False
        pending += decoder.decode(b"", final=True)
        if pending:
            is_content = (state.is_content(pending) if first_window_of_line
                         else not state.in_fence)
            if is_content:
                yield lineno, pending


def _heading_slugs_from_lines(lines) -> set[str]:
    """Shared engine behind `heading_slugs` (in-memory text) and
    `heading_slugs_from_path` (streaming, real files — 020/380). `lines` is
    any iterable of (lineno, line) already filtered to exclude fenced code —
    the shape both `_content_lines` and `_iter_file_content_lines` produce —
    so the two entry points can never drift apart. Every anchor GitHub would
    mint for these headings — ATX (`#`) and setext (a paragraph line
    underlined with `===`/`---`) — including the `-1`, `-2` disambiguation
    suffixes for repeated headings."""
    slugs: set[str] = set()
    counts: dict[str, int] = {}

    def add(heading: str) -> None:
        base = slugify(heading)
        n = counts.get(base, 0)
        counts[base] = n + 1
        slugs.add(base if n == 0 else f"{base}-{n}")

    prev_text: str | None = None   # candidate setext heading text
    prev_lineno = -2
    for lineno, line in lines:
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


def heading_slugs(text: str) -> set[str]:
    """`_heading_slugs_from_lines` over an in-memory string. Kept for direct
    string tests and small callers; real files on disk use
    `heading_slugs_from_path` so a large one is never held whole."""
    return _heading_slugs_from_lines(_content_lines(text))


def heading_slugs_from_path(path: Path) -> set[str]:
    """Streaming sibling of `heading_slugs`, for real files on disk — peak
    memory bounded by `_iter_file_content_lines` regardless of the file's
    size (020/380)."""
    return _heading_slugs_from_lines(_iter_file_content_lines(path))


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


def _iter_links_from_lines(lines, allow_by_line: dict[int, str] | None = None):
    """Shared engine behind `iter_links` (in-memory text) and
    `iter_links_from_path` (streaming, real files — 020/380). `lines` is any
    iterable of (lineno, line) already filtered to exclude fenced code.

    A definition line yields its destination and nothing else: the same line
    cannot also hold an inline link, and checking it here means every usage
    form of that label is covered by one finding, reported where the fix
    belongs."""
    for lineno, line in lines:
        scope = parse_allow(line)
        if scope is not None and allow_by_line is not None:
            allow_by_line[lineno] = scope
        stripped = _strip_inline_code(line)
        definition = _LINK_DEF.match(stripped)
        if definition:
            dest = definition.group(2).strip()
            if dest.startswith("<") and dest.endswith(">"):
                dest = dest[1:-1].strip()
            yield lineno, dest
            continue
        for m in _LINK.finditer(stripped):
            dest = m.group(1).strip()
            if dest.startswith("<") and dest.endswith(">"):
                dest = dest[1:-1].strip()
            yield lineno, dest


def iter_links(text: str, allow_by_line: dict[int, str] | None = None):
    """Yield (lineno, raw_destination) for every link destination in a Markdown
    file — inline `](dest)` and reference definitions `[label]: dest` alike —
    skipping fenced and inline code. Allow-markered lines are still yielded: the
    finding is formed first and subtracted afterwards (`method/GUARDS.md`,
    rule b), so the exemption can be counted. Scopes are recorded into
    `allow_by_line` for the caller to apply.

    Operates on an in-memory string — kept for direct string tests and small
    callers. Real files on disk use `iter_links_from_path` (020/380) so a
    large one is never held whole."""
    yield from _iter_links_from_lines(_content_lines(text), allow_by_line)


def iter_links_from_path(path: Path, allow_by_line: dict[int, str] | None = None):
    """Streaming sibling of `iter_links`, for real files on disk — peak
    memory bounded by `_iter_file_content_lines` regardless of the file's
    size (020/380)."""
    yield from _iter_links_from_lines(_iter_file_content_lines(path), allow_by_line)


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


def _build_basename_index(root: Path) -> dict[str, list[Path]]:
    """Every file/dir basename anywhere under `root` (excluding any path with
    a dot-prefixed component — `.git`, `.github` and friends are not link
    targets, matching the old filter exactly) mapped to the path(s) that
    carry it.

    Built ONCE per scan and reused for every broken link's suggestion
    (020/380). The old code called `root.rglob(name)` — a fresh whole-tree
    walk — for EVERY unresolved link, which made a tree with many broken
    links quadratic in tree size (measured: 3,000 files with one broken link
    each took ~18s; the same shape at 20,000 files did not finish in three
    minutes). Dot-directories are pruned from the walk itself rather than
    filtered from the result, since a match inside one would be discarded
    below anyway — free, not just equivalent."""
    index: dict[str, list[Path]] = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for d in dirnames:
            index.setdefault(d, []).append(Path(dirpath) / d)
        for name in filenames:
            if name.startswith("."):
                continue
            index.setdefault(name, []).append(Path(dirpath) / name)
    return index


class _BasenameIndex:
    """Lazy holder for `_build_basename_index`'s result — built on the FIRST
    suggestion a scan actually needs, never for a clean tree, and reused for
    every suggestion after that within the same `scan_paths` call."""

    def __init__(self, root: Path):
        self._root = root
        self._index: dict[str, list[Path]] | None = None

    def matches(self, name: str) -> list[Path]:
        if self._index is None:
            self._index = _build_basename_index(self._root)
        return self._index.get(name, [])


def _suggest(md_file: Path, root: Path, path: str,
            basename_index: "_BasenameIndex | None" = None) -> str:
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

    `basename_index` (020/380) makes tier 2 a lookup into a tree-wide index
    built once, rather than a fresh `root.rglob(name)` walk per call — see
    `_build_basename_index`. `None` is accepted for direct callers/tests that
    want the tier-2 walk done on the spot instead."""
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
    if basename_index is not None:
        matches = basename_index.matches(name)
    else:
        matches = []
        for cand in root.rglob(name):
            if any(part.startswith(".") for part in cand.relative_to(root).parts):
                continue     # .git, .github and friends are not link targets
            matches.append(cand)
    if len(matches) != 1:
        return ""            # 0: no candidate. 2+: ambiguous — say nothing.
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


def _case_mismatch(target: Path, root: Path,
                   listdir_cache: dict[Path, list[str]] | None = None) -> str | None:
    """On a case-insensitive filesystem (macOS APFS) `exists()` says yes to a
    wrongly-cased link that a case-sensitive host (GitHub) 404s. Walk the
    on-disk names and return the true casing of the first mismatched component,
    or None if the link's casing is exact. Unicode-normalisation-only
    differences (APFS stores NFD; links are usually NFC) are NOT mismatches.

    `listdir_cache` (020/380) makes repeat calls into the SAME directory
    (the common case — many links across a tree resolve into the same
    handful of directories) an O(1) lookup after the first `os.listdir`,
    instead of re-reading it from scratch every time. Without it, N links
    into one M-entry directory cost O(N*M) directory reads — measured: 3,000
    markdown files linking into one shared directory took ~18s; the tally
    scales quadratically with file count from there. `None` is accepted for
    direct callers/tests that want the uncached behaviour."""
    try:
        rel = target.resolve().relative_to(root.resolve())
    except (OSError, ValueError):
        return None
    cur = root.resolve()
    nfc = unicodedata.normalize
    for part in rel.parts:
        try:
            if listdir_cache is not None:
                names = listdir_cache.get(cur)
                if names is None:
                    names = os.listdir(cur)
                    listdir_cache[cur] = names
            else:
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


def check_file(md_file: Path, root: Path,
               slug_cache: dict[Path, set[str]],
               listdir_cache: dict[Path, list[str]],
               basename_index: "_BasenameIndex | None",
               tally: "Tally | None" = None) -> list[Finding]:
    """Scans `md_file` from disk via the streaming readers (020/380) —
    peak memory for this file is bounded regardless of its size, never a
    whole-file `read_text()` held alongside its own line list. `own_slugs`
    is computed lazily, and only via a SECOND bounded pass over the same
    file (`heading_slugs_from_path`), so the common case (no same-file
    anchor in the file) never pays for it at all."""
    rel = _rel(md_file, root)
    own_slugs: set[str] | None = None
    findings: list[Finding] = []
    allow_by_line: dict[int, str] = {}
    for lineno, dest in iter_links_from_path(md_file, allow_by_line):
        if not dest or is_external(dest):
            continue
        path, anchor = split_target(dest)

        if path == "":
            # Same-file anchor. `#` alone (top-of-page) always resolves.
            if not anchor or _LINE_ANCHOR.match(anchor):
                continue
            if own_slugs is None:
                own_slugs = heading_slugs_from_path(md_file)
            f = _check_anchor(rel, lineno, dest, anchor, own_slugs, "in this file")
            if f:
                findings.append(f)
            continue

        target = resolve(md_file, root, path)
        if not target.exists():
            findings.append(Finding(rel, lineno, "missing-file", dest,
                                    f"{_rel(target, root)} does not exist",
                                    _suggest(md_file, root, path, basename_index)))
            continue
        if not _within_root(target, root):
            findings.append(Finding(rel, lineno, "outside-root", dest,
                                    "resolves outside the repo root — a reader "
                                    "on GitHub gets a 404",
                                    _suggest(md_file, root, path, basename_index)))
            continue
        wrong = _case_mismatch(target, root, listdir_cache)
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
                slug_cache[key] = heading_slugs_from_path(target)
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


def _walk_files(base: Path):
    """Every regular file under `base`, streamed one at a time (020/380,
    mirrors secretscan's 020/370 `_walk_files`) — the old `base.rglob("*")`
    funnelled through a list comprehension forced the WHOLE subtree to be
    walked and every `Path` held before scanning a single file. Pruning
    `SKIP_DIR_NAMES` from `dirnames` stops `os.walk` descending into them at
    any depth — the same skip semantics as the old
    `not (SKIP_DIR_NAMES & set(p.parts))` filter, applied before the walk
    pays for it instead of after."""
    for dirpath, dirnames, filenames in os.walk(base):
        # 020/160 (E9): a git worktree LINKED into this tree has a `.git`
        # FILE (`gitdir: <path>`), not a directory, so SKIP_DIR_NAMES' name
        # match never fires and the walk descends into a full second
        # checkout of the same repo, double-counting every finding.
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
            if p.is_file():
                yield p


def iter_markdown(paths: list[Path], root: Path, globs: list[str],
                  tally: "Tally | None" = None):
    for base in paths:
        candidates = [base] if base.is_file() else _walk_files(base)
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
    listdir_cache: dict[Path, list[str]] = {}
    basename_index = _BasenameIndex(root)
    findings: list[Finding] = []
    for md in iter_markdown(paths, root, globs, tally):
        findings.extend(check_file(md, root, slug_cache, listdir_cache,
                                   basename_index, tally))
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
    # A RELATIVE target resolves against --root, never the caller's cwd:
    # mixing the two reads one repo's file under another repo's rules,
    # and neither half of the output says so (roadmap 010/110).
    targets = [(root / p) if not Path(p).is_absolute() else Path(p)
               for p in (args.paths or [str(root)])]
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
        # Reference style, checked at the definition. The usages above the
        # definitions are deliberately present and deliberately NOT what is
        # matched — one finding per definition, not per usage.
        "a [full][r-ok], a [collapsed][], a shortcut, an ![image][r-bad]\n"
        "[r-ok]: target.md\n"                           # resolves
        "[collapsed]: target.md \"titled\"\n"          # resolves, with a title
        "[r-ext]: https://example.com/y\n"             # external, skipped
        "[r-bad]: ghost.md\n"                           # BREAK 5
        "[^1]: a footnote, not a link definition\n"    # skipped: footnote
        "[prose]: this is not a definition at all\n"   # skipped: unquoted tail
    )
    findings = scan_paths([tmp], tmp)
    kinds = sorted((f.kind, f.target) for f in findings)
    expected = sorted([
        ("missing-file", "missing.md"),
        ("missing-anchor", "target.md#ghost"),
        ("missing-anchor", "#no-such"),
        ("missing-anchor", "#A-Section"),
        ("missing-file", "ghost.md"),
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
