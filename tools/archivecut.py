#!/usr/bin/env python3
"""archivecut — cut a repo's one-file records into their stores.

WHY (board `010/220`, the principal's pick 2026-11-20: "Split, fall back to
move"; and `010/270`, his pick 2026-11-20: "Retire SESSIONS.md")
---------------------------------------------------------------------------
The board moved to one file per item on 2026-08-15, but its finished work
from before the split stayed frozen in one file, `docs/ROADMAP-DONE.md` (or
`ROADMAP-DONE.md` at the repo root, where some children kept it; `docs/` wins
when both exist, and the other is left alone). The
session log kept a hand-appended index, `docs/SESSIONS.md`, beside its folder
of session files, and some children a frozen `SESSIONS-ARCHIVE.md` of older
index entries as well (either may sit at the repo root instead, where some
children kept them; as with the board, `docs/` wins when both exist and the
other is named and left alone). On the session log the principal said *"they should
not be in one big sessions file in the first place"*: the date-named
`docs/sessions/` folder is the index, and no file lists it. This tool puts
each one-file record into its store, and says which route ran:

  BOARD (a) CUT. Every top-level `- [x]` entry becomes its own item file in
      one archive section, `docs/roadmap/990-done-before-the-split/`, whose
      `README.md` carries the archive's preamble, its headings and every line
      that was not an entry, verbatim and in order, each entry replaced by a
      link to its item file.
  BOARD (b) MOVE. Where the cut cannot prove itself lossless, the file moves
      whole (`git mv`, so `git log --follow` keeps its history) to
      `docs/roadmap/990-done-before-the-split/frozen/`, with a README that
      points at it.
  SESSIONS: RETIRE. `SESSIONS-ARCHIVE.md` (oldest first) and `SESSIONS.md`
      leave, and only files are written. Each entry (a column-0 bullet with
      its continuation) goes word for word into the session file it links:
      the one it opens by linking, else the only one it links anywhere. It
      sits right after that file's first line where that is a `# ` heading,
      so the title stays first and the entry reads as the file's summary
      (else at the top), under the line "From the retired session log" and a
      comment giving its source and line numbers. An entry that links no
      session file gets a new file, `<date>-<HHMM>-<slug>.md` when it states
      its time straight after its date, `<date>-<NN>-<slug>.md` (its place
      among that day's entries) when it does not: the time is never guessed.
      Every line that is not an entry goes word for word into
      `docs/sessions/README.md`, inside fences, under comments giving its line
      numbers; a README the folder already had is kept, unchanged, above the
      tool's part. There is no fallback: where the proof fails, nothing is
      written. A session archive cut by the earlier route (an index block in
      `SESSIONS.md`) still verifies after the index is retired.

LOSSLESSNESS IS THE GATE, AND IT IS PROVEN, NOT EYED
----------------------------------------------------
`010/030` records what the first child's split taught: verify as a multiset
over every non-heading source line, never by eye. The board cut proves three
things before it writes anything, and falls back to (b) if any fails:

  1. MULTISET. Every non-heading source line appears in the outputs exactly as
     often as in the source, and the headings appear in the same order.
  2. BYTES. Reading the outputs in order, each link line replaced by the file
     it links, gives back the source byte for byte.
  3. PATHS. Links in the moved text are re-pointed for their new depth (a page
     two directories down cannot keep `reviews/x.md`), and every re-pointed
     link must map back to its original text exactly, so (2) holds from the
     files as committed too: `--verify` re-runs it from disk against the last
     committed copy of the source.

The tool re-points a path and never re-wraps prose, and a longer path can push
a line past `wrapscan`'s limit. Each such line, in a file `wrapscan` reads, is
listed in the plan ("WRAP") so the worker wraps it before the first commit. A
line already over, or in a file `.wrapscanignore` exempts, is not listed.

Anything that would make the reading ambiguous fails the proof rather than
being guessed at: a source line already shaped like the tool's link line or
marker, an entry the board cannot read as `[x]`, a reference-style link whose
definition would land in a different file from its use, or a link that will
not map back.

LINKS ACROSS THE TREE
---------------------
Every Markdown link to the archive (or to a retired session log, whose home
is the folder's README), in every tracked `.md` file, records included, is
re-pointed to its new home. That changes a path and never a word.
Both sides of `](` are handled: where the link text is itself a path naming the
archive, it is rewritten to the new path too, because `pathscan` reads both
halves of a link. Inline links and reference definitions both count.

THE SESSION LOG'S PROOF. Before anything is written: every non-blank line
of the log(s) is in the outputs as often as in the source (a multiset); no
source line is shaped like the tool's label or markers; every entry that
needs a new file has a date; every link in an entry still has a target once
the log is gone (a same-page anchor or a link to the log itself has none) and
maps back exactly from its re-pointed form; and, parsing the outputs exactly
as they will be written, the README and the session files rebuild each log
byte for byte while every session file that already existed is unchanged but
for the placed entries. `--verify` repeats the rebuild from disk against the
log's last committed copy.

USAGE
-----
    archivecut.py --plan   [--root R]   say what each would do, with the
                                        proof; write nothing (default)
    archivecut.py --cut    [--root R]   do it: write, `git rm` / `git mv`
    archivecut.py --verify [--root R]   rebuild each cut archive and retired
                                        log from the files on disk; compare
                                        with its last committed copy

Exit 0 on success; 1 when `--verify` finds a mismatch or `--cut` cannot run
(blocked, or a proof failed: then nothing is written);
2 on a usage error. Stdlib only.
"""
from __future__ import annotations

import argparse
import os
import posixpath
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import board  # noqa: E402
import linkscan  # noqa: E402
import wrapscan  # noqa: E402

# Where the pre-split board archive may sit, most usual first (010/280 item 3):
# a child that kept it at the repo root, not in `docs/`, read "nothing to do".
BOARD_SRCS = ("docs/ROADMAP-DONE.md", "ROADMAP-DONE.md")
BOARD_SRC = BOARD_SRCS[0]
BOARD_DIR = "docs/roadmap"
ARCHIVE_SECTION = board.ARCHIVE_SECTION
SECTION_DIR = f"{BOARD_DIR}/{ARCHIVE_SECTION}"
SECTION_README = f"{SECTION_DIR}/README.md"
# Route (b)'s home sits one level below the section, because `board.py` reads
# every `*.md` directly in a section as an item, and a whole archive has no
# state line; neither of its planes recurses, so a subdirectory is outside both.
FROZEN_BOARD = f"{SECTION_DIR}/frozen/ROADMAP-DONE.md"

SESSIONS_SRC = "docs/SESSIONS-ARCHIVE.md"
SESSIONS_INDEX = "docs/SESSIONS.md"
SESSIONS_DIR = "docs/sessions"
# Where the earlier route moved a session archive it could not cut; it no
# longer writes there, and --verify still reads one it finds.
FROZEN_SESSIONS = f"{SESSIONS_DIR}/SESSIONS-ARCHIVE.md"

MARKER = "<!-- archivecut:verbatim-below -->"
BEGIN = "<!-- archivecut:begin docs/SESSIONS-ARCHIVE.md -->"
END = "<!-- archivecut:end -->"

# A board entry: a column-0 done checkbox, the grammar the archive was written
# in. Its continuation is every following indented line, and a blank line only
# where the next non-blank line is indented again (a list item's later
# paragraph).
ENTRY_RE = re.compile(r"^- \[x\](?: |$)")
# A session entry: any column-0 bullet.
SESSION_ENTRY_RE = re.compile(r"^[-*] ")
# The board README's stand-in for a cut entry.
REF_RE = re.compile(r"^- ✅ \[(\d{4}-[a-z0-9-]+)\]\(\1\.md\)$")
# The stand-in the earlier session-archive route (before `010/270`) wrote into
# the index for an entry or preamble cut to a detail file; read by --verify.
SESSION_REF_RE = re.compile(
    r"^- \[.*\]\(sessions/(\d{4}-\d{2}-\d{2}-archived-(\d{3})-[a-z0-9-]+\.md)\)"
    r" — archived (?:entry|preamble), verbatim in its file$")
DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
REF_DEF_RE = re.compile(r"^ {0,3}\[(?!\^)([^\]]+)\]:\s*\S")
REF_USE_RE = re.compile(r"\[([^\]]+)\](?:\[([^\]]*)\])?(?![(:])")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


# --------------------------------------------------------------------------
# text primitives
# --------------------------------------------------------------------------

def split_lines(text: str) -> list[str]:
    """Lines with their endings, split on `\\n` alone. `str.splitlines` also
    breaks on form feeds and Unicode separators, which would make a byte-exact
    rebuild impossible for a file that carries one."""
    return re.findall(r"[^\n]*\n|[^\n]+$", text)


def is_heading(line: str) -> bool:
    return line.startswith("#")


def norm(path: str) -> str:
    return posixpath.normpath(path) if path else path


def rel(target: str, from_dir: str) -> str:
    return posixpath.relpath(target, from_dir or ".")


def segment(text: str, start_re: re.Pattern) -> list[tuple[str, list[str]]]:
    """The source as ordered blocks: ('entry', lines) or ('text', lines)."""
    lines = split_lines(text)
    blocks: list[tuple[str, list[str]]] = []
    buf: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        if not start_re.match(lines[i]):
            buf.append(lines[i])
            i += 1
            continue
        if buf:
            blocks.append(("text", buf))
            buf = []
        j = i + 1
        while j < n:
            line = lines[j]
            if line.strip() == "":
                k = j
                while k < n and lines[k].strip() == "":
                    k += 1
                if k < n and lines[k][:1] in (" ", "\t"):
                    j = k
                    continue
                break
            if line[:1] in (" ", "\t"):
                j += 1
                continue
            break
        blocks.append(("entry", lines[i:j]))
        i = j
    if buf:
        blocks.append(("text", buf))
    return blocks


# --------------------------------------------------------------------------
# links: find, rewrite, map back
# --------------------------------------------------------------------------

@dataclass
class Edit:
    line: int
    old: str
    new: str
    side: str  # "target" or "text"


def _link_text_span(stripped: str, close: int) -> tuple[int, int] | None:
    """(start, end) of the text inside `[...]` whose `]` sits at `close`."""
    depth = 0
    for i in range(close, -1, -1):
        c = stripped[i]
        if c == "]":
            depth += 1
        elif c == "[":
            depth -= 1
            if depth == 0:
                return i + 1, close
    return None


def rewrite_links(text: str, map_target, map_text=None,
                  skip: re.Pattern | None = None) -> tuple[str, list[Edit]]:
    """Rewrite link destinations (inline and reference definitions) outside
    fenced and inline code. `map_target(dest)` returns a new destination or
    None. `map_text(text, old_dest, new_dest)` may rewrite the link's text, and
    is asked only where the destination changed."""
    out: list[str] = []
    edits: list[Edit] = []
    fence = linkscan._FenceState()
    for lineno, line in enumerate(split_lines(text), 1):
        if not fence.is_content(line) or (skip and skip.match(line.rstrip("\n"))):
            out.append(line)
            continue
        stripped = linkscan._strip_inline_code(line)
        spans: list[tuple[int, int, str, str, str]] = []
        d = linkscan._LINK_DEF.match(stripped.rstrip("\n"))
        if d:
            s, e = d.span(2)
            dest = line[s:e]
            inner = dest[1:-1] if dest.startswith("<") and dest.endswith(">") else dest
            new = map_target(inner)
            if new is not None and new != inner:
                spans.append((s, e, dest, f"<{new}>" if inner != dest else new,
                              "target"))
        else:
            for m in linkscan._LINK.finditer(stripped):
                s, e = m.span(1)
                dest = line[s:e]
                inner = dest[1:-1] if dest.startswith("<") and dest.endswith(">") else dest
                new = map_target(inner)
                if new is None or new == inner:
                    continue
                spans.append((s, e, dest, f"<{new}>" if inner != dest else new,
                              "target"))
                if map_text is not None:
                    close = stripped.rfind("]", 0, m.start(1))
                    ts = _link_text_span(stripped, close) if close >= 0 else None
                    if ts:
                        old_text = line[ts[0]:ts[1]]
                        new_text = map_text(old_text, inner, new)
                        if new_text is not None and new_text != old_text:
                            spans.append((ts[0], ts[1], old_text, new_text,
                                          "text"))
        for s, e, old, new, side in sorted(spans, reverse=True):
            line = line[:s] + new + line[e:]
            edits.append(Edit(lineno, old, new, side))
        out.append(line)
    return "".join(out), edits


def split_dest(dest: str) -> tuple[str, str | None]:
    path, sep, anchor = dest.partition("#")
    return path, (anchor if sep else None)


def join_dest(path: str, anchor: str | None) -> str:
    return path + (f"#{anchor}" if anchor is not None else "")


def _keep_slash(orig: str, new: str) -> str:
    return new + "/" if orig.endswith("/") and not new.endswith("/") else new


@dataclass
class Move:
    """Where one moved text was and is: the source archive (`src`), the
    directory its links were written from (`old_dir`), the file it now is
    (`new_file`), the file a link to the archive itself now means
    (`self_target`), and every file that maps back to the archive."""
    src: str
    old_dir: str
    new_file: str
    self_target: str
    replacements: frozenset[str]
    # The cut's own link lines, written for their home already: never moved.
    skip: re.Pattern | None = None

    @property
    def new_dir(self) -> str:
        return posixpath.dirname(self.new_file)

    # A same-page anchor in a file that does not carry the archive's headings
    # is written as `./<self>#a`; the leading `./` is what tells it apart from
    # a link to the archive's own anchor on the way back.
    def _self_anchor_prefix(self) -> str:
        return "./" + rel(self.self_target, self.new_dir) + "#"

    def forward(self, dest: str) -> str | None:
        if SCHEME_RE.match(dest) or dest.startswith(("/", "//")):
            return None
        path, anchor = split_dest(dest)
        if not path:
            if anchor is None or self.new_file == self.self_target:
                return None
            return self._self_anchor_prefix() + anchor
        resolved = norm(posixpath.join(self.old_dir, path))
        if resolved == self.src:
            new = rel(self.self_target, self.new_dir)
        else:
            new = _keep_slash(path, rel(resolved, self.new_dir))
        return join_dest(new, anchor)

    def back(self, dest: str) -> str | None:
        if SCHEME_RE.match(dest) or dest.startswith(("/", "//")):
            return None
        if self.new_file != self.self_target and \
                dest.startswith(self._self_anchor_prefix()):
            return "#" + dest[len(self._self_anchor_prefix()):]
        path, anchor = split_dest(dest)
        if not path:
            return None
        resolved = norm(posixpath.join(self.new_dir, path))
        if resolved in self.replacements:
            old = rel(self.src, self.old_dir)
        else:
            old = _keep_slash(path, rel(resolved, self.old_dir))
        return join_dest(old, anchor)

    def text_forward(self, text: str, old: str, new: str) -> str | None:
        # Only a link to the archive itself has its text rewritten: every
        # other link's text is the record's own words.
        path = split_dest(old)[0]
        if not path or norm(posixpath.join(self.old_dir, path)) != self.src:
            return None
        return _text_map(text, self.src, self.self_target, self.old_dir,
                         self.new_dir, old, new)

    def text_back(self, text: str, old: str, new: str) -> str | None:
        if norm(posixpath.join(self.new_dir, split_dest(old)[0])) \
                not in self.replacements:
            return None
        return _text_map(text, self.self_target, self.src, self.new_dir,
                         self.old_dir, old, new, also=self.replacements)


def _text_map(text: str, frm: str, to: str, frm_dir: str, to_dir: str,
              old_dest: str, new_dest: str,
              also: frozenset[str] = frozenset()) -> str | None:
    """A link's text, rewritten where it is a path naming `frm` (or one of
    `also`): resolved from the linking file, from the repo root, or the same
    text as the old destination. Wrapping backticks are kept."""
    tick = text.startswith("`") and text.endswith("`") and len(text) >= 2
    inner = text[1:-1] if tick else text
    if not inner or " " in inner:
        return None
    names = {frm} | set(also)
    if inner == old_dest:
        new = new_dest
    elif norm(posixpath.join(frm_dir, inner)) in names:
        new = _keep_slash(inner, rel(to, to_dir))
    elif norm(inner) in names:
        new = to
    elif posixpath.basename(inner) == posixpath.basename(frm) and "/" not in inner:
        new = new_dest
    else:
        return None
    return f"`{new}`" if tick else new


def relocate(text: str, mv: Move) -> tuple[str, list[Edit]]:
    return rewrite_links(text, mv.forward, mv.text_forward, mv.skip)


def unrelocate(text: str, mv: Move) -> tuple[str, list[Edit]]:
    return rewrite_links(text, mv.back, mv.text_back, mv.skip)


def ref_labels_crossing(outputs: list[str]) -> list[str]:
    """Reference-style labels used in one output but defined only in another:
    after a cut the use would no longer render as a link."""
    defs_per: list[set[str]] = []
    for text in outputs:
        defs_per.append({m.group(1).strip().lower()
                         for line in split_lines(text)
                         if (m := REF_DEF_RE.match(line))})
    all_defs = set().union(*defs_per) if defs_per else set()
    bad: set[str] = set()
    for text, defs in zip(outputs, defs_per):
        for line in split_lines(text):
            if REF_DEF_RE.match(line):
                continue
            for m in REF_USE_RE.finditer(linkscan._strip_inline_code(line)):
                label = (m.group(2) or m.group(1)).strip().lower()
                if label in all_defs and label not in defs:
                    bad.add(label)
    return sorted(bad)


# --------------------------------------------------------------------------
# plans
# --------------------------------------------------------------------------

@dataclass
class Plan:
    kind: str                     # "board" | "sessions"
    src: str
    route: str = "absent"         # "cut" | "move" | "absent" | "blocked"
    reasons: list[str] = field(default_factory=list)
    proof: list[str] = field(default_factory=list)
    writes: dict[str, str] = field(default_factory=dict)
    move_to: str | None = None
    items: int = 0
    headings: int = 0
    link_files: int = 0
    link_edits: int = 0
    tree_writes: dict[str, str] = field(default_factory=dict)
    # Lines a re-pointed link pushed past the wrap limit: (path, line, width).
    long_lines: list[tuple[str, int, int]] = field(default_factory=list)


def _git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args],
                          capture_output=True, text=True, check=False)


def last_commit(root: Path, path: str) -> str:
    r = _git(root, "log", "-1", "--format=%h", "--", path)
    return r.stdout.strip() or "uncommitted"


def tracked_md(root: Path) -> list[str]:
    r = _git(root, "ls-files", "-z", "--", "*.md")
    if r.returncode != 0:
        return sorted(str(p.relative_to(root)).replace(os.sep, "/")
                      for p in root.rglob("*.md")
                      if ".git" not in p.parts and "worktrees" not in p.parts)
    return sorted(p for p in r.stdout.split("\0") if p)


def _read(root: Path, path: str) -> str | None:
    p = root / path
    if not p.is_file():
        return None
    return p.read_bytes().decode("utf-8")


def board_src(root: Path) -> str:
    """Where this repo keeps its pre-split board archive (010/280 item 3): the
    first of `BOARD_SRCS` that is a file on disk, else (for `--verify`, after a
    cut has removed it) the first the git history knows, else the usual home."""
    for cand in BOARD_SRCS:
        if (root / cand).is_file():
            return cand
    for cand in BOARD_SRCS:
        if committed_source(root, cand) is not None:
            return cand
    return BOARD_SRC


def _title(entry_text: str) -> str:
    state = board.item_state(entry_text)
    if state is not None:
        return board.index_title(state.rest)
    first = entry_text.split("\n", 1)[0]
    bold = board.TITLE_RE.search(first)
    if bold:
        return bold.group(1).strip()
    return re.sub(r"^[-*]\s+", "", first).strip()


def _check(proof: list[str], ok: bool, label: str) -> bool:
    proof.append(f"{'PASS' if ok else 'FAIL'}  {label}")
    return ok


def _note_long_lines(root: Path, plan: Plan, path: str, before: str,
                     after: str) -> None:
    """Record each line the re-pointing took past the house wrap limit
    (010/280 item 1). The tool changes a path and never re-wraps prose, so the
    worker has to: this names the lines, as `wrapscan` would read them, so the
    first commit is not the first they hear of it. A line already over before
    (or in a file `.wrapscanignore` exempts) is not reported: it was no news.
    The line count never changes, so line numbers match."""
    try:
        if wrapscan._ignored(path, wrapscan.load_ignore_globs(root)):
            return
    except wrapscan.IgnoreFileError:
        pass          # a broken ignore file is wrapscan's to report, not ours
    was = {f.line for f in wrapscan.scan_text(path, before)}
    seen = {(p, n) for p, n, _ in plan.long_lines}
    for f in wrapscan.scan_text(path, after):
        if f.line not in was and (path, f.line) not in seen:
            plan.long_lines.append((path, f.line, f.length))


def _repoint_tree(root: Path, plan: Plan, src: str, new_home: str,
                  skip: set[str], anchors: set[str]) -> None:
    """Re-point every tracked Markdown link to `src` at `new_home`, in place in
    `plan.tree_writes`. An anchor the new home carries is kept; one it does
    not is dropped (it named nothing there either)."""
    for path in tracked_md(root):
        if path in skip or path == src or ".claude/worktrees/" in path:
            continue
        text = plan.tree_writes.get(path, plan.writes.get(path))
        if text is None:
            try:
                text = _read(root, path)
            except UnicodeDecodeError:
                continue
        if text is None or posixpath.basename(src) not in text:
            continue
        fdir = posixpath.dirname(path)

        def target(dest: str, fdir=fdir) -> str | None:
            if SCHEME_RE.match(dest):
                return None
            p, anchor = split_dest(dest)
            if not p:
                return None
            resolved = norm(p.lstrip("/")) if p.startswith("/") \
                else norm(posixpath.join(fdir, p))
            if resolved != src:
                return None
            if anchor is not None and anchor not in anchors:
                anchor = None
            return join_dest(rel(new_home, fdir), anchor)

        def text_side(t: str, old: str, new: str, fdir=fdir) -> str | None:
            return _text_map(t, src, new_home, fdir, fdir, old,
                             split_dest(new)[0])

        new_text, edits = rewrite_links(text, target, text_side)
        if edits:
            plan.link_files += path not in plan.tree_writes
            _note_long_lines(root, plan, path, text, new_text)
            plan.tree_writes[path] = new_text
            plan.link_edits += len(edits)


# ---- the board archive ----------------------------------------------------

def _section_conflict(root: Path) -> str | None:
    bdir = root / BOARD_DIR
    if not bdir.is_dir():
        return f"{BOARD_DIR}/ does not exist: the board has not split here yet"
    for d in bdir.iterdir():
        if d.is_dir() and d.name.split("-", 1)[0] == ARCHIVE_SECTION.split("-", 1)[0] \
                and d.name != ARCHIVE_SECTION:
            return f"section number 990 is already used by {d.name}"
    if (root / SECTION_DIR).exists():
        return f"{SECTION_DIR}/ already exists"
    return None


def board_readme_header(src: str, sha: str) -> str:
    return (
        "# Done before the split\n"
        "\n"
        "The board's finished work from before it moved to one file per item,\n"
        f"cut from `{src}`\n"
        f"(last changed in `{sha}`) into one `[x]` item file per entry by\n"
        "`tools/archivecut.py`. Below the marker line this page is that file\n"
        "verbatim: its preamble, its headings and every line that was not an\n"
        "entry, in order, with each entry replaced by a link to the item file\n"
        "that holds it, and links re-pointed for the new depth.\n"
        "`python3 tools/archivecut.py --verify` rebuilds the original from these\n"
        "files and compares it with the last committed copy.\n"
        "\n"
        f"{MARKER}\n")


def board_moved_readme(src: str, sha: str) -> str:
    return (
        "# Done before the split\n"
        "\n"
        "The board's finished work from before it moved to one file per item.\n"
        f"`{src}`\n"
        f"(last changed in `{sha}`) could not be cut into item files with a\n"
        "proof that nothing was lost, so `tools/archivecut.py` moved it here\n"
        "whole: [`frozen/ROADMAP-DONE.md`](frozen/ROADMAP-DONE.md). Its words\n"
        "are unchanged; its links were re-pointed for the new depth.\n")


def board_moves(names: list[str], src: str = BOARD_SRC) -> dict[str, Move]:
    reps = frozenset([SECTION_README] + [f"{SECTION_DIR}/{n}" for n in names])
    old_dir = posixpath.dirname(src)
    out = {SECTION_README: Move(src, old_dir, SECTION_README,
                                SECTION_README, reps, REF_RE)}
    for n in names:
        f = f"{SECTION_DIR}/{n}"
        out[f] = Move(src, old_dir, f, SECTION_README, reps)
    return out


def board_reconstruct(readme: str, items: dict[str, str]) -> str | None:
    """The source, rebuilt from the README and item texts (as given)."""
    if readme.count(MARKER + "\n") != 1:
        return None
    body = readme.split(MARKER + "\n", 1)[1]
    out: list[str] = []
    for line in split_lines(body):
        m = REF_RE.match(line.rstrip("\n"))
        if m:
            name = m.group(1) + ".md"
            if name not in items:
                return None
            out.append(items[name])
        else:
            out.append(line)
    return "".join(out)


def plan_board(root: Path) -> Plan:
    src = board_src(root)
    plan = Plan("board", src)
    try:
        text = _read(root, src)
    except UnicodeDecodeError:
        text, plan.route = None, "move"
        plan.reasons.append("not UTF-8")
    if text is None and plan.route == "absent":
        return plan
    conflict = _section_conflict(root)
    if conflict:
        plan.route = "blocked"
        plan.reasons.append(conflict)
        return plan
    others = [c for c in BOARD_SRCS if c != src and (root / c).is_file()]
    if others:
        plan.reasons.append(f"{', '.join(others)} also exists and is left alone; "
                            f"cutting {src}")
    sha = last_commit(root, src)
    if text is not None:
        ok = _cut_board(plan, text, sha)
        plan.route = "cut" if ok else "move"
    if plan.route == "move":
        _move_board(root, plan, sha)
    anchors = set()
    if plan.route == "cut":
        anchors = linkscan.heading_slugs(plan.writes[SECTION_README])
        home = SECTION_README
    else:
        home = SECTION_README
    _repoint_tree(root, plan, src, home, set(plan.writes), anchors)
    return plan


def _cut_board(plan: Plan, text: str, sha: str) -> bool:
    proof = plan.proof
    blocks = segment(text, ENTRY_RE)
    entries = [b for k, b in blocks if k == "entry"]
    ok = _check(proof, bool(entries), f"{len(entries)} `[x]` entries found")
    width = max(4, len(str(10 * len(entries))))
    body: list[str] = []
    items: dict[str, str] = {}
    names: list[str] = []
    n = 0
    collisions = 0
    for kind, lines in blocks:
        if kind == "text":
            for line in lines:
                if REF_RE.match(line.rstrip("\n")) or line.rstrip("\n") == MARKER:
                    collisions += 1
            body.extend(lines)
            continue
        n += 1
        etext = "".join(lines)
        stem = f"{10 * n:0{width}d}-{board.slug(_title(etext))}"
        name = stem + ".md"
        names.append(name)
        items[name] = etext
        nl = "\n" if lines[-1].endswith("\n") else ""
        body.append(f"- ✅ [{stem}]({name}){nl}")
    ok &= _check(proof, collisions == 0,
                 f"no source line is shaped like the cut's link line or marker "
                 f"({collisions} found)")
    unread = [nm for nm, t in items.items()
              if (st := board.item_state(t)) is None or st.marker != "[x]"]
    ok &= _check(proof, not unread,
                 f"every item reads as `[x]` to board.py ({len(unread)} do not)")
    readme = board_readme_header(plan.src, sha) + "".join(body)

    # (2) bytes, before any link moves
    rebuilt = board_reconstruct(readme, items)
    ok &= _check(proof, rebuilt is not None
                 and rebuilt.encode("utf-8") == text.encode("utf-8"),
                 "the outputs, read in order, rebuild the source byte for byte")
    # (1) multiset over non-heading lines; headings in order
    src_lines = split_lines(text)
    out_lines = [ln for ln in split_lines("".join(body))
                 if not REF_RE.match(ln.rstrip("\n"))]
    for t in items.values():
        out_lines.extend(split_lines(t))
    key = lambda ls: Counter(x.rstrip("\n") for x in ls if not is_heading(x))  # noqa: E731
    ok &= _check(proof, key(src_lines) == key(out_lines),
                 f"multiset of {sum(1 for x in src_lines if not is_heading(x))} "
                 "non-heading source lines matches the outputs")
    src_heads = [x.rstrip("\n") for x in src_lines if is_heading(x)]
    out_heads = [x.rstrip("\n") for x in split_lines("".join(body)) if is_heading(x)]
    ok &= _check(proof, src_heads == out_heads,
                 f"{len(src_heads)} headings kept, in order")
    plan.headings = sum(1 for h in src_heads if h.startswith("## "))
    crossing = ref_labels_crossing([readme] + list(items.values()))
    ok &= _check(proof, not crossing,
                 "no reference-style link is cut away from its definition"
                 + (f" ({', '.join(crossing)})" if crossing else ""))

    # (3) links re-pointed for the new depth, and every one maps back
    moves = board_moves(names, plan.src)
    moved: dict[str, str] = {}
    n_links = 0
    raw = {SECTION_README: readme, **{f"{SECTION_DIR}/{k}": v for k, v in items.items()}}
    for path, t in raw.items():
        new, edits = relocate(t, moves[path])
        n_links += len(edits)
        moved[path] = new
    back = {p: unrelocate(t, moves[p])[0] for p, t in moved.items()}
    rebuilt2 = board_reconstruct(
        back[SECTION_README],
        {k: back[f"{SECTION_DIR}/{k}"] for k in items})
    ok &= _check(proof, rebuilt2 is not None
                 and rebuilt2.encode("utf-8") == text.encode("utf-8"),
                 f"{n_links} link paths re-pointed for the new depth, and the "
                 "committed files rebuild the source byte for byte")
    if ok:
        plan.writes = moved
        plan.items = len(items)
    return ok


def _move_board(root: Path, plan: Plan, sha: str) -> None:
    plan.writes = {}
    plan.move_to = FROZEN_BOARD
    try:
        text = _read(root, plan.src) or ""
    except UnicodeDecodeError:
        plan.writes[SECTION_README] = board_moved_readme(plan.src, sha)
        return
    reps = frozenset([FROZEN_BOARD])
    mv = Move(plan.src, posixpath.dirname(plan.src), FROZEN_BOARD,
              FROZEN_BOARD, reps)
    moved, edits = relocate(text, mv)
    back, _ = unrelocate(moved, mv)
    _check(plan.proof, back == text,
           f"route (b): {len(edits)} link paths re-pointed in the moved file, "
           "each maps back to its original")
    plan.writes[FROZEN_BOARD] = moved
    plan.writes[SECTION_README] = board_moved_readme(plan.src, sha)


# ---- the session log -------------------------------------------------------
#
# Retiring the one-file session log (`010/270`, the principal's pick
# 2026-11-20: "Retire SESSIONS.md"). The folder of session files is the index;
# no file in `docs/` keeps a list of them. Every entry of the index, and of a
# frozen `SESSIONS-ARCHIVE.md` where one is left, goes word for word into a
# session file: the file it opens by linking where that is a session file in
# the folder, a new file named for its date otherwise. Everything that is not
# an entry (the preamble, any heading or marker between entries) goes word for
# word into `docs/sessions/README.md`, inside fences so it reads as a record
# and no scanner acts on a marker in it. Marker comments carry each piece's
# line numbers, so the log can be rebuilt from the folder byte for byte.

LOG_SOURCES = (SESSIONS_SRC, SESSIONS_INDEX)   # oldest first
# Where each may sit, most usual first (010/280): a child that kept its log at
# the repo root, not in `docs/`, read "nothing to do", as the board did.
LOG_HOMES = (
    (SESSIONS_SRC, "SESSIONS-ARCHIVE.md"),
    (SESSIONS_INDEX, "SESSIONS.md"),
)
SESSIONS_README = f"{SESSIONS_DIR}/README.md"

# The label line is the tool's own prose, so it fits the house width (85; 010/280,
# the 2026-11-20 note): at 101 columns it made `wrapscan` refuse the first commit
# in about ten children. The wording that shipped first is still read (and a
# session file carrying it still verifies), but is never written again.
LOG_LABEL = ("**From the retired session log**, word for word; only link paths "
             "re-pointed:")
LEGACY_LOG_LABELS = (
    "**From the retired session log**, word for word; only its link "
    "paths were re-pointed for this folder:",
)
ENTRY_MARK = "<!-- archivecut:log-entry {src} {start}+{count} -->"
ENTRY_MARK_RE = re.compile(r"^<!-- archivecut:log-entry (\S+) (\d+)\+(\d+) -->$")
REGION_MARK = "<!-- archivecut:log-text {src} {start}+{count} -->"
REGION_MARK_RE = re.compile(r"^<!-- archivecut:log-text (\S+) (\d+)\+(\d+) -->$")
# The README's marker comment is the tool's own too, and it was 92 columns for
# the longer log name (`-ARCHIVE`) once a short sha was in: over `wrapscan`'s
# limit (010/280, the 2026-11-23 note). `nl=` is the old `final-newline=`, 10
# columns shorter and the same flag, so the line fits for either log name. The
# old spelling is still read, and a README carrying it still verifies
# (`_canonical_marks` rewrites it for the exact-text comparison), but only the
# short one is written.
RETIRED_MARK = ("<!-- archivecut:retired {src} lines={lines} "
                "nl={nl} last={sha} -->")
RETIRED_RE = re.compile(r"^<!-- archivecut:retired (\S+) lines=(\d+) "
                        r"(?:final-newline|nl)=(yes|no) last=(\S+) -->$")
LEGACY_RETIRED_RE = re.compile(r"^(<!-- archivecut:retired \S+ lines=\d+ )"
                               r"final-newline=((?:yes|no) last=\S+ -->)$")
# An entry that opens by linking: `- [text](dest)`, the text allowed to wrap.
OPENING_LINK_RE = re.compile(
    r"^[-*] \[(?:[^\[\]]|\[[^\[\]]*\])*\]\(<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\)")
# The time an entry states for itself, straight after its date:
# `2026-07-20 · ~1945 UTC`, `**2026-11-09 · 1242 UTC**`, `2026-07-18 · 13:50`.
STATED_TIME_RE = re.compile(
    r"(\d{4}-\d{2}-\d{2})\**\s*·\s*~?([01]\d|2[0-3]):?([0-5]\d)"
    r"(?=$|[\s*·\]),;])")
FENCE_RUN_RE = re.compile(r"^ {0,3}(`+)")

README_HEADER = """\
# Session records

One file per working session, named for the time the session started:
`YYYY-MM-DD-HHMM-slug.md`, the time in UTC (the house doctrine's RECORD.md,
§ *The session log*). The folder is the index. The names sort by start time,
so a session getting its bearings reads the newest few files, for example the
ones `ls docs/sessions/[0-9]* | tail -5` lists, and opens older ones only when
it needs them. Some older names carry a two-digit counter where the time
would be (`YYYY-MM-DD-NN-slug.md`). This README is the only file here that is
not a session record.

"""
# Everything from this line down is the tool's; above it is the folder's own
# README (the header above, or a README the repo already kept, unchanged).
INTRO_MARK = "<!-- archivecut:retired-log-below -->"
README_INTRO = """## The retired one-file session log

This repo once kept a one-file session log beside this folder as well. It
was retired by atelier's `archivecut.py`: each of its entries now sits, word
for word, near the top of the session file it linked, or in a new file named
for its date where it linked none, under the line "From the retired session
log". Below is the rest of that file, word for word: its preamble and
anything else that was not an entry, inside fences so that it is read as a
record and nothing acts on it. The comment lines carry its line numbers, so
`archivecut.py --verify` can rebuild the file from this folder byte for byte.
"""


class _NotPresent:
    pass


NOT_PRESENT = _NotPresent()


def _core(entries: list[tuple[str, int, int, str]],
          label: str = LOG_LABEL) -> str:
    out = [label + "\n", "\n"]
    for src, start, count, text in entries:
        out.append(ENTRY_MARK.format(src=src, start=start, count=count) + "\n")
        out.append(text if text.endswith("\n") else text + "\n")
    return "".join(out)


def insert_entries(original: str | None,
                   entries: list[tuple[str, int, int, str]],
                   label: str = LOG_LABEL) -> str:
    """A session file with retired-log entries placed in it: right after its
    first line where that is a `# ` heading (the title stays first and the
    entry reads as the file's summary), else at the top. `original` None
    means the file is new and holds the entries alone."""
    core = _core(entries, label)
    if original is None:
        return core
    lines = split_lines(original)
    if lines and lines[0].startswith("# ") and lines[0].endswith("\n"):
        return lines[0] + "\n" + core + "\n" + "".join(lines[1:])
    return core + "\n" + original


def strip_entries(text: str):
    """The inverse of `insert_entries`: (original or None, entries), or
    NOT_PRESENT when the file holds no placed entries, or None when it holds
    something shaped like them that does not read back exactly."""
    lines = split_lines(text)
    label = None
    for cand in (LOG_LABEL, *LEGACY_LOG_LABELS):
        if len(lines) > 2 and lines[0].startswith("# ") and lines[1] == "\n" \
                and lines[2] == cand + "\n":
            head, i, label = lines[0], 2, cand
            break
        if lines and lines[0] == cand + "\n":
            head, i, label = None, 0, cand
            break
    if label is None:
        return NOT_PRESENT
    if i + 1 >= len(lines) or lines[i + 1] != "\n":
        return None
    j = i + 2
    entries: list[tuple[str, int, int, str]] = []
    while j < len(lines):
        m = ENTRY_MARK_RE.match(lines[j].rstrip("\n"))
        if not m:
            break
        count = int(m.group(3))
        body = lines[j + 1:j + 1 + count]
        if len(body) != count or count < 1:
            return None
        entries.append((m.group(1), int(m.group(2)), count, "".join(body)))
        j += 1 + count
    if not entries:
        return None
    rest = "".join(lines[j:])
    if head is None:
        if rest == "":
            original = None
        elif rest.startswith("\n"):
            original = rest[1:]
        else:
            return None
    else:
        if not rest.startswith("\n"):
            return None
        original = head + rest[1:]
    if insert_entries(original, entries, label) != text:
        return None
    return original, entries


def without_entries(text: str) -> str:
    """A session file's text as it was before entries were placed in it."""
    got = strip_entries(text)
    if isinstance(got, tuple):
        return got[0] or ""
    return text


def _fence(body: str) -> str:
    run = 2
    for line in split_lines(body):
        m = FENCE_RUN_RE.match(line)
        if m:
            run = max(run, len(m.group(1)))
    return "`" * max(4, run + 1)


def readme_text(sections: list[dict], prefix: str | None = None) -> str:
    """The folder README: `prefix` (a README the repo already kept, as it
    stands) or the tool's header, then the retired logs' sections."""
    head = README_HEADER if prefix is None else prefix
    out = [head, INTRO_MARK + "\n\n", README_INTRO]
    for sec in sections:
        out.append(f"\n### `{sec['src']}`, retired\n\n")
        out.append(RETIRED_MARK.format(
            src=sec["src"], lines=sec["nlines"],
            nl="yes" if sec["final_nl"] else "no", sha=sec["sha"]) + "\n")
        for start, count, body in sec["regions"]:
            body = body if body.endswith("\n") else body + "\n"
            fence = _fence(body)
            out.append("\n" + REGION_MARK.format(src=sec["src"], start=start,
                                                 count=count) + "\n")
            out.append(fence + "\n" + body + fence + "\n")
    return "".join(out)


def readme_prefix(text: str) -> str | None:
    """A README's own text, above the tool's part; None when it has none."""
    k = text.find(INTRO_MARK + "\n")
    if k < 0 or (k > 0 and text[k - 1] != "\n"):
        return None
    return text[:k]


def _canonical_marks(text: str) -> str:
    """`text` with each old-spelling `archivecut:retired` comment written the
    way `readme_text` writes it now, so a README cut earlier compares equal."""
    return "".join(LEGACY_RETIRED_RE.sub(r"\1nl=\2", ln.rstrip("\n"))
                   + ("\n" if ln.endswith("\n") else "")
                   for ln in split_lines(text))


def parse_readme(text: str) -> list[dict] | None:
    """The retired logs' sections, read back from the README; None unless the
    README is exactly what `readme_text` writes for them."""
    lines = split_lines(text)
    sections: list[dict] = []
    cur = None
    i = 0
    while i < len(lines):
        s = lines[i].rstrip("\n")
        m = RETIRED_RE.match(s)
        if m:
            cur = {"src": m.group(1), "nlines": int(m.group(2)),
                   "final_nl": m.group(3) == "yes", "sha": m.group(4),
                   "regions": []}
            sections.append(cur)
            i += 1
            continue
        m = REGION_MARK_RE.match(s)
        if m:
            if cur is None or m.group(1) != cur["src"]:
                return None
            start, count = int(m.group(2)), int(m.group(3))
            if i + 2 + count >= len(lines):
                return None
            fence = lines[i + 1].rstrip("\n")
            if not re.fullmatch(r"`{3,}", fence) \
                    or lines[i + 2 + count].rstrip("\n") != fence:
                return None
            cur["regions"].append((start, count,
                                   "".join(lines[i + 2:i + 2 + count])))
            i += 3 + count
            continue
        i += 1
    prefix = readme_prefix(text)
    if prefix is None or readme_text(sections, prefix) != _canonical_marks(text):
        return None
    return sections


def log_src(root: Path, home: tuple[str, str]) -> str:
    """Where this repo keeps one of its session logs (010/280): the first home
    that is a file on disk, else (for `--verify`, after a retirement has
    removed it) the first the git history knows, else the usual one."""
    for cand in home:
        if (root / cand).is_file():
            return cand
    for cand in home:
        if committed_source(root, cand) is not None:
            return cand
    return home[0]


def _depth(d: str) -> int:
    return len([x for x in d.split("/") if x]) if d else 0


def _folder_in(base: str) -> str:
    """The session folder as a path from the directory `base` (a log's own)."""
    return posixpath.relpath(SESSIONS_DIR, base or ".")


def _entry_back(dest: str, base: str = "docs") -> str | None:
    """A placed entry's link, mapped back to how the log wrote it. `base` is
    the directory the log sat in (`docs`, or "" at the repo root)."""
    if SCHEME_RE.match(dest) or dest.startswith("/"):
        return None
    path, anchor = split_dest(dest)
    if not path:
        return None
    up = "../" * (_depth(SESSIONS_DIR) - _depth(base))
    if path.startswith(up):
        return join_dest(path[len(up):], anchor)
    if path.startswith("../"):
        return None            # `_entry_forward` never writes it
    return join_dest(_folder_in(base) + "/" + path, anchor)


def _entry_forward(dest: str, errors: list[str], base: str = "docs",
                   logs: tuple[str, ...] = LOG_SOURCES) -> str | None:
    """A log entry's link, re-pointed for the folder below it. A link into the
    folder loses its path to it (`sessions/` from `docs/`); any other gains
    `../` for each level it goes down. Both map back exactly (`_entry_back`),
    which a normalised path would not: the log may write `../docs/x.md` where
    `x.md` would do."""
    if SCHEME_RE.match(dest) or dest.startswith("/"):
        return None
    path, anchor = split_dest(dest)
    if not path:
        errors.append(f"a same-page anchor (`{dest}`) has no page once the log goes")
        return None
    if norm(posixpath.join(base, path)) in logs:
        errors.append(f"a link to the log itself (`{dest}`)")
        return None
    into = _folder_in(base) + "/"
    if path.startswith(into):
        rest = path[len(into):]
        if rest and "/" not in rest and rest not in (".", ".."):
            return join_dest(rest, anchor)
    return join_dest("../" * (_depth(SESSIONS_DIR) - _depth(base)) + path, anchor)


def _session_file(root: Path, dest: str, base: str = "docs") -> str | None:
    """The name of the session file a log link reaches, when it is a file
    directly in the folder (never the README)."""
    path = split_dest(dest)[0]
    if not path or SCHEME_RE.match(path) or path.startswith("/"):
        return None
    resolved = norm(posixpath.join(base, path))
    if posixpath.dirname(resolved) != SESSIONS_DIR:
        return None
    name = posixpath.basename(resolved)
    if name == "README.md" or not name.endswith(".md") \
            or not (root / resolved).is_file():
        return None
    return name


def _pointer_target(root: Path, etext: str, base: str = "docs") -> str | None:
    """The session file an entry belongs in: the one it opens by linking,
    else the only one it links anywhere (an index line may put its link on
    a later line). An entry linking two or more, none first, has no home."""
    m = OPENING_LINK_RE.match(etext)
    if m:
        name = _session_file(root, m.group(1), base)
        if name:
            return name
    found: list[str] = []

    def collect(dest: str) -> None:
        name = _session_file(root, dest, base)
        if name and name not in found:
            found.append(name)
        return None

    rewrite_links(etext, collect)
    return found[0] if len(found) == 1 else None


def entry_date_time(etext: str) -> tuple[str | None, str | None]:
    """The date an entry opens with (its first line's first ISO date, else
    the entry's) and the time it states straight after it, if any."""
    first = etext.split("\n", 1)[0]
    m = DATE_RE.search(first)
    if not m:
        m = DATE_RE.search(etext)
        return (m.group(1) if m else None), None
    t = STATED_TIME_RE.match(first, m.start())
    if t and t.group(1) == m.group(1):
        return m.group(1), t.group(2) + t.group(3)
    return m.group(1), None


def entry_slug(etext: str) -> str:
    first = etext.split("\n", 1)[0]
    t = re.sub(r"^[-*]\s+", "", first)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*\[\]`]", "", t)
    t = re.sub(r"^\s*\d{4}-\d{2}-\d{2}\s*(?:·\s*~?\d{2}:?\d{2}(?:\s*UTC)?\s*)?"
               r"(?:·\s*)?", "", t)
    return board.slug(t) if t.strip() else "session"


def rebuild_log(sec: dict, entries: list[tuple[int, int, str]]) -> str | None:
    """One retired log, rebuilt from its README section and its entries
    (link paths already mapped back). A line nothing covers was blank."""
    n = sec["nlines"]
    slots: list[str | None] = [None] * n
    for start, count, body in list(sec["regions"]) + entries:
        ls = split_lines(body)
        if len(ls) != count or start < 1 or start - 1 + count > n:
            return None
        for k, line in enumerate(ls):
            if slots[start - 1 + k] is not None:
                return None
            slots[start - 1 + k] = line
    out = [s if s is not None else "\n" for s in slots]
    if not sec["final_nl"] and out:
        if not out[-1].endswith("\n"):
            return None
        out[-1] = out[-1][:-1]
    return "".join(out)


def rebuild_logs(readme: str, files: dict[str, str]) -> dict[str, str | None] | None:
    """Every retired log the README names, rebuilt from the README and the
    session files' placed entries; None when the README does not read back."""
    sections = parse_readme(readme)
    if sections is None:
        return None
    by_src: dict[str, list[tuple[int, int, str]]] = {}
    bad = False
    for text in files.values():
        got = strip_entries(text)
        if got is None:
            bad = True
            continue
        if got is NOT_PRESENT:
            continue
        for src, start, count, body in got[1]:
            back, _ = rewrite_links(
                body, lambda d, b=posixpath.dirname(src): _entry_back(d, b))
            by_src.setdefault(src, []).append((start, count, back))
    out: dict[str, str | None] = {}
    known = {sec["src"] for sec in sections}
    for sec in sections:
        out[sec["src"]] = None if bad else rebuild_log(sec, by_src.get(sec["src"], []))
    for src in by_src:
        if src not in known:
            out[src] = None
    return out


def plan_sessions(root: Path) -> Plan:
    plan = Plan("sessions", " + ".join(log_src(root, h) for h in LOG_HOMES))
    present = []
    for home in LOG_HOMES:
        here = [c for c in home if (root / c).is_file()]
        if here:
            present.append(here[0])      # `docs/` first: it wins
            for other in here[1:]:
                plan.reasons.append(f"{other} also exists and is left alone; "
                                    f"retiring {here[0]}")
    if not present:
        return plan
    plan.src = " + ".join(present)
    texts: dict[str, str] = {}
    for s in present:
        try:
            texts[s] = _read(root, s) or ""
        except UnicodeDecodeError:
            plan.route = "blocked"
            plan.reasons.append(f"{s} is not UTF-8")
    if (root / SESSIONS_README).exists():
        try:
            prior = _read(root, SESSIONS_README) or ""
        except UnicodeDecodeError:
            prior = None
        if prior is None or INTRO_MARK in prior:
            plan.route = "blocked"
            plan.reasons.append(f"{SESSIONS_README} is not UTF-8 or already "
                                "holds a retired log")
    if plan.route == "blocked":
        return plan
    ok = _retire_log(root, plan, texts)
    plan.route = "cut" if ok else "failed"
    if ok:
        for s in present:
            _repoint_tree(root, plan, s, SESSIONS_README, set(present), set())
    return plan


def _retire_log(root: Path, plan: Plan, texts: dict[str, str]) -> bool:
    proof = plan.proof
    sdir = root / SESSIONS_DIR
    existing = {p.name for p in sdir.iterdir()} if sdir.is_dir() else set()
    taken = set(existing)
    created: set[str] = set()
    per_file: dict[str, list[tuple[str, int, int, str]]] = {}
    sections: list[dict] = []
    pieces: list[str] = []
    day_count: Counter = Counter()
    collisions = undated = placed = new = untimed = 0
    srcs = list(texts)           # oldest first, as `plan_sessions` read them
    logs = tuple(dict.fromkeys((*srcs, *LOG_SOURCES)))
    for src in srcs:
        base = posixpath.dirname(src)
        text = texts[src]
        lines = split_lines(text)
        for line in lines:
            s = line.rstrip("\n")
            if s in (LOG_LABEL, *LEGACY_LOG_LABELS) or ENTRY_MARK_RE.match(s) \
                    or REGION_MARK_RE.match(s) or RETIRED_RE.match(s):
                collisions += 1
        regions: list[tuple[int, int, str]] = []
        lineno = 1
        for kind, blines in segment(text, SESSION_ENTRY_RE):
            start = lineno
            lineno += len(blines)
            if kind == "text":
                a, b = 0, len(blines)
                while a < b and blines[a] == "\n":
                    a += 1
                while b > a and blines[b - 1] == "\n":
                    b -= 1
                if a < b:
                    regions.append((start + a, b - a, "".join(blines[a:b])))
                    pieces.append("".join(blines[a:b]))
                continue
            etext = "".join(blines)
            pieces.append(etext)
            date, hhmm = entry_date_time(etext)
            if date:
                day_count[date] += 1
            target = _pointer_target(root, etext, base)
            if target is None:
                if date is None:
                    undated += 1
                    continue
                slug_ = entry_slug(etext)
                stem = f"{date}-{hhmm}-{slug_}" if hhmm \
                    else f"{date}-{day_count[date]:02d}-{slug_}"
                name, k = stem + ".md", 2
                while name in taken:
                    name, k = f"{stem}-{k}.md", k + 1
                taken.add(name)
                created.add(name)
                target = name
                new += 1
                untimed += hhmm is None
            else:
                placed += 1
            per_file.setdefault(target, []).append((src, start, len(blines), etext))
        sections.append({"src": src, "nlines": len(lines),
                         "final_nl": text == "" or text.endswith("\n"),
                         "sha": last_commit(root, src), "regions": regions})
    entries = placed + new
    plan.items = entries
    ok = _check(proof, True,
                f"{entries} entries: {placed} placed in the session file they "
                f"link, {new} in new files ({untimed} of them state no time, so "
                "their names carry a day counter)")
    ok &= _check(proof, undated == 0,
                 f"every entry that links no session file carries a date for "
                 f"its new file's name ({undated} do not)")
    ok &= _check(proof, collisions == 0,
                 "no source line is shaped like the retirement's own label or "
                 f"markers ({collisions} found)")
    already = sorted(n for n in per_file if n not in created and
                     strip_entries(_read(root, f"{SESSIONS_DIR}/{n}") or "")
                     is not NOT_PRESENT)
    ok &= _check(proof, not already,
                 f"no session file already holds placed entries ({len(already)} do)")
    crossing = ref_labels_crossing(pieces)
    ok &= _check(proof, not crossing,
                 "no reference-style link is cut away from its definition"
                 + (f" ({', '.join(crossing)})" if crossing else ""))
    # (1) multiset: every non-blank source line is in the outputs as often
    src_key: Counter = Counter()
    for src, text in texts.items():
        src_key.update(x.rstrip("\n") for x in split_lines(text) if x.strip())
    out_key: Counter = Counter(x.rstrip("\n") for p in pieces
                               for x in split_lines(p) if x.strip())
    ok &= _check(proof, src_key == out_key,
                 f"multiset of {sum(src_key.values())} non-blank source lines "
                 "matches the outputs")
    # (2) links re-pointed one level down, each mapping back exactly
    errors: list[str] = []
    writes: dict[str, str] = {}
    n_links = 0
    unmapped = 0
    for name, ents in per_file.items():
        moved_ents = []
        for src, start, count, etext in ents:
            body = etext if etext.endswith("\n") else etext + "\n"
            base = posixpath.dirname(src)
            moved, edits = rewrite_links(
                body, lambda d: _entry_forward(d, errors, base, logs))
            n_links += len(edits)
            if rewrite_links(moved, lambda d: _entry_back(d, base))[0] != body:
                unmapped += 1
            moved_ents.append((src, start, count, moved))
        original = None if name in created \
            else _read(root, f"{SESSIONS_DIR}/{name}")
        writes[f"{SESSIONS_DIR}/{name}"] = insert_entries(original, moved_ents)
    ok &= _check(proof, not errors,
                 "every link in an entry still has a target once the log goes"
                 + (f" ({'; '.join(sorted(set(errors))[:3])})" if errors else ""))
    ok &= _check(proof, unmapped == 0,
                 f"{n_links} link paths re-pointed for the folder, each maps "
                 f"back to its original ({unmapped} entries do not)")
    prior = _read(root, SESSIONS_README) if (root / SESSIONS_README).is_file() \
        else None
    if prior is not None:
        prior = prior if prior.endswith("\n") else prior + "\n"
        prior += "\n"
        _check(proof, True, f"{SESSIONS_README} already exists: its own words "
               "are kept above the retired log's part (read them: they may "
               "still describe the index)")
    readme = readme_text(sections, prior)
    writes[SESSIONS_README] = readme
    # (3) from the outputs as they will be written: every log rebuilds byte for
    # byte, and every session file that existed is unchanged but for the entries
    files = {p.rsplit("/", 1)[1]: t for p, t in writes.items()
             if p != SESSIONS_README}
    rebuilt = rebuild_logs(readme, files) or {}
    for src, text in texts.items():
        ok &= _check(proof, rebuilt.get(src) is not None
                     and rebuilt[src].encode("utf-8") == text.encode("utf-8"),
                     f"{src}: the README and the session files, as written, "
                     "rebuild it byte for byte")
    changed = [n for n in files if n not in created and
               without_entries(files[n]) != _read(root, f"{SESSIONS_DIR}/{n}")]
    ok &= _check(proof, not changed,
                 f"{len(files) - len(created)} existing session files are "
                 f"unchanged but for the placed entries ({len(changed)} are not)")
    if ok:
        plan.writes = writes
    return ok


# --------------------------------------------------------------------------
# verify (from disk)
# --------------------------------------------------------------------------

def committed_source(root: Path, src: str) -> str | None:
    """The last committed copy of `src`: HEAD's if it still has it, else the
    parent of the commit that deleted (or moved) it."""
    r = _git(root, "cat-file", "-e", f"HEAD:{src}")
    if r.returncode == 0:
        return _git(root, "show", f"HEAD:{src}").stdout
    r = _git(root, "log", "-1", "--format=%H", "--diff-filter=DR", "--", src)
    sha = r.stdout.strip()
    if not sha:
        return None
    r = _git(root, "show", f"{sha}^:{src}")
    return r.stdout if r.returncode == 0 else None


def _verify_sessions(root: Path) -> list[str]:
    out: list[str] = []
    readme = _read(root, SESSIONS_README) if (root / SESSIONS_README).is_file() else None
    retired: set[str] = set()
    if readme is not None and not any(RETIRED_RE.match(x.rstrip("\n"))
                                      for x in split_lines(readme)):
        readme = None
    if readme is not None:
        sdir = root / SESSIONS_DIR
        files = {p.name: _read(root, f"{SESSIONS_DIR}/{p.name}") or ""
                 for p in sdir.glob("*.md") if p.name != "README.md"}
        rebuilt = rebuild_logs(readme, files)
        if rebuilt is None:
            out.append(f"FAIL  {SESSIONS_README}: its retired-log sections do "
                       "not read back")
            return out
        holding = sum(1 for t in files.values()
                      if isinstance(strip_entries(t), tuple))
        for src, text in rebuilt.items():
            retired.add(src)
            if (root / src).exists():
                out.append(f"FAIL  {src}: retired, yet still in place")
                continue
            committed = committed_source(root, src)
            ok = text is not None and committed is not None and text == committed
            out.append(("PASS" if ok else "FAIL")
                       + f"  {src}: the README and {holding} session files "
                       "rebuild its last committed copy byte for byte")
    # A session archive cut before `010/270`, into an index block (that route
    # only ever ran on `docs/`, so only a `docs/` archive is read for it).
    archive, index = LOG_HOMES
    if not retired.intersection(archive):
        asrc = log_src(root, archive)
        if asrc == SESSIONS_SRC:
            out.extend(_verify_archive_block(root))
        else:
            out.extend(_verify_unretired(root, asrc))
    if not retired.intersection(index):
        out.extend(_verify_unretired(root, log_src(root, index)))
    return out


def _verify_unretired(root: Path, src: str) -> list[str]:
    """A session log the README does not record as retired: still in place,
    never committed, or gone with nothing to show for it."""
    if (root / src).exists():
        return [f"--    {src}: still in place, not retired"]
    if committed_source(root, src) is None:
        return [f"--    {src}: never committed here"]
    return [f"FAIL  {src}: gone, and {SESSIONS_README} does not record its "
            "retirement"]


# The pre-`010/270` session-archive cut's index block, read back for --verify.

def _extract_block(index: str) -> tuple[str, str] | None:
    """(block body, index without the block), or None."""
    if index.count(BEGIN + "\n") != 1 or index.count(END + "\n") < 1:
        return None
    head, rest = index.split(BEGIN + "\n", 1)
    body, tail = rest.split(END + "\n", 1)
    return body, head + tail


def sessions_reconstruct(block: str, files: dict[str, str]) -> str | None:
    """The source, rebuilt from the index block and detail texts (as given)."""
    pre: list[str] = []
    out: list[str] = []
    for line in split_lines(block):
        m = SESSION_REF_RE.match(line.rstrip("\n"))
        if m:
            name = m.group(1)
            if name not in files:
                return None
            (pre if m.group(2) == "000" else out).append(files[name])
        else:
            out.append(line)
    return "".join(pre + out)


def _verify_archive_block(root: Path) -> list[str]:
    """The pre-`010/270` session-archive cut: an index block in
    `SESSIONS.md` and `-archived-` detail files. Once the index is retired,
    both are read as they stood just before the commit that retired it (that
    retirement re-pointed links in them and is proven on its own)."""
    out: list[str] = []
    src = committed_source(root, SESSIONS_SRC)
    if (root / SESSIONS_SRC).exists():
        out.append(f"--    {SESSIONS_SRC}: still in place, not cut")
    elif src is None:
        out.append(f"--    {SESSIONS_SRC}: never committed here")
    elif (root / FROZEN_SESSIONS).is_file():
        mv = Move(SESSIONS_SRC, "docs", FROZEN_SESSIONS, FROZEN_SESSIONS,
                  frozenset([FROZEN_SESSIONS]))
        back = unrelocate(_read(root, FROZEN_SESSIONS) or "", mv)[0]
        out.append(("PASS" if back == src else "FAIL")
                   + f"  {SESSIONS_SRC}: route (b), the moved file maps back")
    else:
        retire = None
        if (root / SESSIONS_INDEX).is_file():
            index = _read(root, SESSIONS_INDEX)
        else:
            retire = _git(root, "log", "-1", "--format=%H", "--diff-filter=DR",
                          "--", SESSIONS_INDEX).stdout.strip() or None
            index = _git(root, "show", f"{retire}^:{SESSIONS_INDEX}").stdout \
                if retire else None

        def detail(p: str) -> str:
            if retire is None:
                return _read(root, p) or ""
            return _git(root, "show", f"{retire}^:{p}").stdout

        got = _extract_block(index or "")
        if got is None:
            out.append(f"FAIL  {SESSIONS_SRC}: gone, and {SESSIONS_INDEX} holds "
                       "no cut block")
            return out
        block = got[0]
        names = [m.group(1) for line in split_lines(block)
                 if (m := SESSION_REF_RE.match(line.rstrip("\n")))]
        pre = next((n for n in names if "-archived-000-" in n), None)
        self_target = f"{SESSIONS_DIR}/{pre}" if pre else SESSIONS_INDEX
        reps = frozenset([self_target])
        files = {}
        for n in names:
            p = f"{SESSIONS_DIR}/{n}"
            files[n] = unrelocate(detail(p),
                                  Move(SESSIONS_SRC, "docs", p, self_target, reps))[0]
        back = unrelocate(block, Move(SESSIONS_SRC, "docs", SESSIONS_INDEX,
                                      self_target, reps, SESSION_REF_RE))[0]
        ok = sessions_reconstruct(back, files) == src
        out.append(("PASS" if ok else "FAIL")
                   + f"  {SESSIONS_SRC}: {len(names)} detail files and the "
                   "index block rebuild its last committed copy byte for byte")
    return out


def verify(root: Path) -> list[str]:
    """Lines of a verdict; a line starting FAIL means a mismatch."""
    out: list[str] = []
    # board
    bsrc = board_src(root)
    src = committed_source(root, bsrc)
    if (root / bsrc).exists():
        out.append(f"--    {bsrc}: still in place, not cut")
    elif src is None:
        out.append(f"--    {bsrc}: never committed here")
    elif (root / FROZEN_BOARD).is_file():
        mv = Move(bsrc, posixpath.dirname(bsrc), FROZEN_BOARD, FROZEN_BOARD,
                  frozenset([FROZEN_BOARD]))
        back = unrelocate(_read(root, FROZEN_BOARD) or "", mv)[0]
        out.append(("PASS" if back == src else "FAIL")
                   + f"  {bsrc}: route (b), the moved file maps back to "
                   "its last committed copy")
    else:
        readme = _read(root, SECTION_README)
        if readme is None:
            out.append(f"FAIL  {bsrc}: gone, and {SECTION_README} is missing")
        else:
            names = [p.name for p in (root / SECTION_DIR).glob("*.md")
                     if p.name != "README.md"]
            moves = board_moves(names, bsrc)
            items = {n: unrelocate(_read(root, f"{SECTION_DIR}/{n}") or "",
                                   moves[f"{SECTION_DIR}/{n}"])[0] for n in names}
            body = unrelocate(readme, moves[SECTION_README])[0]
            rebuilt = board_reconstruct(body, items)
            used = {m.group(1) for line in split_lines(readme)
                    if (m := REF_RE.match(line.rstrip("\n")))}
            ok = rebuilt == src
            out.append(("PASS" if ok else "FAIL")
                       + f"  {bsrc}: {len(names)} item files and the section "
                       "README rebuild its last committed copy byte for byte")
            spare = sorted(set(n[:-3] for n in names) - used)
            if spare:
                out.append(f"FAIL  {SECTION_DIR}: {len(spare)} item files the "
                           "README does not link")
    out.extend(_verify_sessions(root))
    return out


# --------------------------------------------------------------------------
# apply and report
# --------------------------------------------------------------------------

def apply(root: Path, plan: Plan) -> None:
    if plan.route == "cut":
        for src in plan.src.split(" + "):
            r = _git(root, "rm", "-q", "--", src)
            if r.returncode != 0 and (root / src).exists():
                (root / src).unlink()
    elif plan.route == "move":
        dest = root / plan.move_to
        dest.parent.mkdir(parents=True, exist_ok=True)
        r = _git(root, "mv", "--", plan.src, plan.move_to)
        if r.returncode != 0:
            os.replace(root / plan.src, dest)
    else:
        return
    for path, text in {**plan.writes, **plan.tree_writes}.items():
        p = root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))


def render(plan: Plan) -> str:
    cut = {"board": "(a) cut into the store",
           "sessions": "retired into the session folder"}[plan.kind]
    lines = [f"{plan.kind}: {plan.src} — route: "
             + {"cut": cut,
                "move": "(b) moved whole (the cut could not prove itself)",
                "absent": "nothing to do (no such file)",
                "blocked": "blocked",
                "failed": "not retired: the proof failed, nothing is written"
                }[plan.route]]
    for r in plan.reasons:
        lines.append(f"  reason: {r}")
    for p in plan.proof:
        lines.append(f"  {p}")
    if plan.route == "cut" and plan.kind == "board":
        lines.append(f"  {plan.items} item files under {plan.headings} `## ` headings")
    if plan.route == "move":
        lines.append(f"  moves to {plan.move_to}")
    if plan.route in ("cut", "move"):
        lines.append(f"  links re-pointed elsewhere in the tree: {plan.link_edits}"
                     f" in {plan.link_files} files")
    if plan.long_lines and plan.route in ("cut", "move"):
        lines.append(f"  WRAP  {len(plan.long_lines)} line(s) a re-pointed link "
                     f"pushed past {wrapscan.LINE_LIMIT} columns; wrap each "
                     "before committing (the tool never re-wraps prose):")
        for path, n, width in sorted(plan.long_lines):
            lines.append(f"    {path}:{n} ({width} columns)")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Cut a repo's frozen pre-split board archive "
                    "(ROADMAP-DONE.md) into the store form, and retire its "
                    "one-file session log (SESSIONS.md, SESSIONS-ARCHIVE.md) "
                    "into the docs/sessions/ folder, each with a proof. Each "
                    "is looked for in docs/ first, then at the repo root.")
    act = ap.add_mutually_exclusive_group()
    act.add_argument("--plan", action="store_true",
                     help="say what each would do, with the proof; write "
                          "nothing (the default)")
    act.add_argument("--cut", action="store_true",
                     help="carry the plan out: write the outputs, `git rm` or "
                          "`git mv` the sources, re-point links")
    act.add_argument("--verify", action="store_true",
                     help="rebuild each cut archive and retired log from the "
                          "files on disk and compare it with its last "
                          "committed copy")
    ap.add_argument("--root", default=".", help="the repo (default: cwd)")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    if args.verify:
        lines = verify(root)
        print("\n".join(lines))
        return 1 if any(x.startswith("FAIL") for x in lines) else 0
    plans = [plan_board(root), plan_sessions(root)]
    for p in plans:
        print(render(p))
    if not args.cut:
        return 0
    if any(p.route in ("blocked", "failed") for p in plans):
        print("archivecut: blocked or unproven; nothing written", file=sys.stderr)
        return 1
    # Board first; the session plan re-reads the tree so its link edits land
    # on top of the board's.
    apply(root, plans[0])
    second = plan_sessions(root)
    if second.route in ("blocked", "failed"):
        print(render(second))
        print("archivecut: the session log no longer proves after the board "
              "cut; the board cut stands, the log is untouched", file=sys.stderr)
        return 1
    apply(root, second)
    return 0


if __name__ == "__main__":
    sys.exit(main())
