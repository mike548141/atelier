#!/usr/bin/env python3
"""archivecut — cut a repo's frozen pre-split archives into the store form.

WHY (board `010/220`, the principal's pick 2026-11-20: "Split, fall back to
move")
---------------------------------------------------------------------------
The board moved to one file per item on 2026-08-15 and the session log to an
index plus detail files before that, but two archives were frozen in the old
one-file form and left in `docs/`: `ROADMAP-DONE.md` (finished board work from
before the split) and, in some children, `SESSIONS-ARCHIVE.md` (older session
index entries rotated out). They are the last records outside their stores.
This tool puts them in, by one of two routes, and says which ran:

  (a) CUT. Board: every top-level `- [x]` entry becomes its own item file in
      one archive section, `docs/roadmap/990-done-before-the-split/`, whose
      `README.md` carries the archive's preamble, its headings and every line
      that was not an entry, verbatim and in order, each entry replaced by a
      link to its item file. Sessions: every entry becomes a detail file in
      `docs/sessions/` with a one-line index entry in `docs/SESSIONS.md`
      (`method/RECORD.md`'s index/detail split); an entry that already IS an
      index line (it links its own detail file) goes back to the index as it
      stands.
  (b) MOVE. Where the cut cannot prove itself lossless, the file moves whole
      (`git mv`, so `git log --follow` keeps its history): the board archive
      to `docs/roadmap/990-done-before-the-split/frozen/`, with a README that
      points at it, and the session archive to `docs/sessions/`, with an index
      line that points at it.

LOSSLESSNESS IS THE GATE, AND IT IS PROVEN, NOT EYED
----------------------------------------------------
`010/030` records what the first child's split taught: verify as a multiset
over every non-heading source line, never by eye. The cut proves three things
before it writes anything, and falls back to (b) if any fails:

  1. MULTISET. Every non-heading source line appears in the outputs exactly as
     often as in the source, and the headings appear in the same order.
  2. BYTES. Reading the outputs in order, each link line replaced by the file
     it links, gives back the source byte for byte.
  3. PATHS. Links in the moved text are re-pointed for their new depth (a page
     two directories down cannot keep `reviews/x.md`), and every re-pointed
     link must map back to its original text exactly, so (2) holds from the
     files as committed too: `--verify` re-runs it from disk against the last
     committed copy of the source.

Anything that would make the reading ambiguous fails the proof rather than
being guessed at: a source line already shaped like the tool's link line or
marker, an entry the board cannot read as `[x]`, a reference-style link whose
definition would land in a different file from its use, or a link that will
not map back.

LINKS ACROSS THE TREE
---------------------
Every Markdown link to the archive, in every tracked `.md` file, records
included, is re-pointed to its new home. That changes a path and never a word.
Both sides of `](` are handled: where the link text is itself a path naming the
archive, it is rewritten to the new path too, because `pathscan` reads both
halves of a link. Inline links and reference definitions both count.

USAGE
-----
    archivecut.py --plan   [--root R]   say which route each archive would take,
                                        with the proof; write nothing (default)
    archivecut.py --cut    [--root R]   do it: write, `git rm` / `git mv`
    archivecut.py --verify [--root R]   rebuild each cut archive from the files
                                        on disk; compare with its last
                                        committed copy

Exit 0 on success; 1 when `--verify` finds a mismatch or `--cut` cannot run;
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

BOARD_SRC = "docs/ROADMAP-DONE.md"
BOARD_DIR = "docs/roadmap"
ARCHIVE_SECTION = "990-done-before-the-split"
SECTION_DIR = f"{BOARD_DIR}/{ARCHIVE_SECTION}"
SECTION_README = f"{SECTION_DIR}/README.md"
# Route (b)'s home sits one level below the section, because `board.py` reads
# every `*.md` directly in a section as an item, and a whole archive has no
# state line; neither of its planes recurses, so a subdirectory is outside both.
FROZEN_BOARD = f"{SECTION_DIR}/frozen/ROADMAP-DONE.md"

SESSIONS_SRC = "docs/SESSIONS-ARCHIVE.md"
SESSIONS_INDEX = "docs/SESSIONS.md"
SESSIONS_DIR = "docs/sessions"
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
# The session index's stand-in for an entry or preamble cut to a detail file.
SESSION_REF_RE = re.compile(
    r"^- \[.*\]\(sessions/(\d{4}-\d{2}-\d{2}-archived-(\d{3})-[a-z0-9-]+\.md)\)"
    r" — archived (?:entry|preamble), verbatim in its file$")
# An entry that is already an index line: it opens by linking its detail file.
POINTER_RE = re.compile(r"^[-*] \[[^\]]*\]\(sessions/", re.S)
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


def _repoint_tree(root: Path, plan: Plan, src: str, new_home: str,
                  skip: set[str], anchors: set[str]) -> None:
    """Re-point every tracked Markdown link to `src` at `new_home`, in place in
    `plan.tree_writes`. An anchor the new home carries is kept; one it does
    not is dropped (it named nothing there either)."""
    for path in tracked_md(root):
        if path in skip or path == src or ".claude/worktrees/" in path:
            continue
        text = plan.writes.get(path)
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
            plan.tree_writes[path] = new_text
            plan.link_files += 1
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


def board_moves(names: list[str]) -> dict[str, Move]:
    reps = frozenset([SECTION_README] + [f"{SECTION_DIR}/{n}" for n in names])
    out = {SECTION_README: Move(BOARD_SRC, "docs", SECTION_README,
                                SECTION_README, reps, REF_RE)}
    for n in names:
        f = f"{SECTION_DIR}/{n}"
        out[f] = Move(BOARD_SRC, "docs", f, SECTION_README, reps)
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
    plan = Plan("board", BOARD_SRC)
    try:
        text = _read(root, BOARD_SRC)
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
    sha = last_commit(root, BOARD_SRC)
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
    _repoint_tree(root, plan, BOARD_SRC, home, set(plan.writes), anchors)
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
    readme = board_readme_header(BOARD_SRC, sha) + "".join(body)

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
    moves = board_moves(names)
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
        text = _read(root, BOARD_SRC) or ""
    except UnicodeDecodeError:
        plan.writes[SECTION_README] = board_moved_readme(BOARD_SRC, sha)
        return
    reps = frozenset([FROZEN_BOARD])
    mv = Move(BOARD_SRC, "docs", FROZEN_BOARD, FROZEN_BOARD, reps)
    moved, edits = relocate(text, mv)
    back, _ = unrelocate(moved, mv)
    _check(plan.proof, back == text,
           f"route (b): {len(edits)} link paths re-pointed in the moved file, "
           "each maps back to its original")
    plan.writes[FROZEN_BOARD] = moved
    plan.writes[SECTION_README] = board_moved_readme(BOARD_SRC, sha)


# ---- the session archive --------------------------------------------------

def plan_sessions(root: Path) -> Plan:
    plan = Plan("sessions", SESSIONS_SRC)
    try:
        text = _read(root, SESSIONS_SRC)
    except UnicodeDecodeError:
        text, plan.route = None, "move"
        plan.reasons.append("not UTF-8")
    if text is None and plan.route == "absent":
        return plan
    index = _read(root, SESSIONS_INDEX)
    if index is None:
        plan.route = "blocked"
        plan.reasons.append(f"{SESSIONS_INDEX} does not exist")
        return plan
    if BEGIN in index:
        plan.route = "blocked"
        plan.reasons.append(f"{SESSIONS_INDEX} already holds a cut block")
        return plan
    if text is not None:
        ok = _cut_sessions(root, plan, text, index)
        plan.route = "cut" if ok else "move"
    if plan.route == "move":
        _move_sessions(root, plan, index)
    # The index itself is re-pointed too: its own header may name the archive.
    _repoint_tree(root, plan, SESSIONS_SRC, SESSIONS_INDEX,
                  set(plan.writes) - {SESSIONS_INDEX}, set())
    return plan


def _insert_block(index: str, block: str) -> str:
    """The index with `block` before its first column-0 entry."""
    lines = split_lines(index)
    for i, line in enumerate(lines):
        if SESSION_ENTRY_RE.match(line):
            return "".join(lines[:i]) + block + "".join(lines[i:])
    sep = "" if not index or index.endswith("\n") else "\n"
    return index + sep + block


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


def _index_label(text: str) -> str:
    t = text.replace("\n", " ")
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*`]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) > 72:
        t = t[:71].rstrip() + "…"
    return board._escape_link_text(t)


def _cut_sessions(root: Path, plan: Plan, text: str, index: str) -> bool:
    proof = plan.proof
    blocks = segment(text, SESSION_ENTRY_RE)
    entries = [b for k, b in blocks if k == "entry"]
    ok = _check(proof, bool(entries), f"{len(entries)} session entries found")
    existing = {p.name for p in (root / SESSIONS_DIR).glob("*.md")} \
        if (root / SESSIONS_DIR).is_dir() else set()
    # The preamble: every text block before the first entry.
    pre_lines: list[str] = []
    while blocks and blocks[0][0] == "text":
        pre_lines.extend(blocks.pop(0)[1])
    first_date = None
    for _, lines in [("x", pre_lines)] + [b for b in blocks if b[0] == "entry"]:
        m = DATE_RE.search("".join(lines))
        if m:
            first_date = m.group(1)
            break
    files: dict[str, str] = {}
    block_lines: list[str] = []
    collisions = 0
    undated = 0
    pointers = details = 0
    pre_name = None
    if pre_lines:
        h1 = next((x[2:].strip() for x in pre_lines if x.startswith("# ")),
                  "session log archive")
        pre_name = f"{first_date or '0000-00-00'}-archived-000-{board.slug(h1)}.md"
        files[pre_name] = "".join(pre_lines)
        block_lines.append(
            f"- [{first_date} · {_index_label(h1)}](sessions/{pre_name})"
            " — archived preamble, verbatim in its file\n")
        undated += first_date is None
    n = 0
    for kind, lines in blocks:
        if kind == "text":
            for line in lines:
                s = line.rstrip("\n")
                if SESSION_REF_RE.match(s) or s in (BEGIN, END):
                    collisions += 1
            block_lines.extend(lines)
            continue
        etext = "".join(lines)
        if SESSION_REF_RE.match(lines[0].rstrip("\n")):
            collisions += 1
        if POINTER_RE.match(etext):
            pointers += 1
            block_lines.extend(lines)
            continue
        details += 1
        n += 1
        m = DATE_RE.search(etext)
        if not m:
            undated += 1
        date = m.group(1) if m else "0000-00-00"
        title = _title(etext)
        name = f"{date}-archived-{n:03d}-{board.slug(title)}.md"
        files[name] = etext
        nl = "\n" if lines[-1].endswith("\n") else ""
        block_lines.append(
            f"- [{date} · {_index_label(title)}](sessions/{name})"
            f" — archived entry, verbatim in its file{nl}")
    plan.items = details
    ok &= _check(proof, n < 1000, f"{details} entries cut to detail files, "
                 f"{pointers} already index lines kept as they stand")
    ok &= _check(proof, undated == 0,
                 f"every cut entry carries a date for its file name ({undated} do not)")
    ok &= _check(proof, collisions == 0,
                 "no source line is shaped like the cut's index line or block "
                 f"marker ({collisions} found)")
    clash = sorted(set(files) & existing)
    ok &= _check(proof, not clash,
                 f"no detail file name is already taken ({len(clash)} are)")
    block = "".join(block_lines)
    if block and not block.endswith("\n"):
        block += "\n"
    rebuilt = sessions_reconstruct(block, files)
    ok &= _check(proof, rebuilt is not None
                 and rebuilt.encode("utf-8") == text.encode("utf-8"),
                 "the outputs, read in order, rebuild the source byte for byte")
    src_lines = split_lines(text)
    out_lines = [x for x in split_lines(block) if not SESSION_REF_RE.match(x.rstrip("\n"))]
    for t in files.values():
        out_lines.extend(split_lines(t))
    key = lambda ls: Counter(x.rstrip("\n") for x in ls if not is_heading(x))  # noqa: E731
    ok &= _check(proof, key(src_lines) == key(out_lines),
                 f"multiset of {sum(1 for x in src_lines if not is_heading(x))} "
                 "non-heading source lines matches the outputs")
    crossing = ref_labels_crossing([block] + list(files.values()))
    ok &= _check(proof, not crossing,
                 "no reference-style link is cut away from its definition"
                 + (f" ({', '.join(crossing)})" if crossing else ""))
    self_target = f"{SESSIONS_DIR}/{pre_name}" if pre_name else SESSIONS_INDEX
    reps = frozenset([self_target])
    moves = {f"{SESSIONS_DIR}/{k}": Move(SESSIONS_SRC, "docs", f"{SESSIONS_DIR}/{k}",
                                         self_target, reps) for k in files}
    bmove = Move(SESSIONS_SRC, "docs", SESSIONS_INDEX, self_target, reps,
                 SESSION_REF_RE)
    moved = {p: relocate(files[p.rsplit("/", 1)[1]], mv)[0] for p, mv in moves.items()}
    mblock, bedits = relocate(block, bmove)
    n_links = len(bedits) + sum(len(relocate(files[p.rsplit("/", 1)[1]], mv)[1])
                                for p, mv in moves.items())
    back_files = {p.rsplit("/", 1)[1]: unrelocate(t, moves[p])[0] for p, t in moved.items()}
    back_block = unrelocate(mblock, bmove)[0]
    rebuilt2 = sessions_reconstruct(back_block, back_files)
    ok &= _check(proof, rebuilt2 is not None
                 and rebuilt2.encode("utf-8") == text.encode("utf-8"),
                 f"{n_links} link paths re-pointed for the new depth, and the "
                 "committed files rebuild the source byte for byte")
    if self_target == SESSIONS_INDEX:
        ok &= _check(proof, n_links == 0 or SESSIONS_SRC.split("/")[-1] not in text,
                     "the archive's links to itself have a home to map back from")
    if ok:
        plan.writes = dict(moved)
        plan.writes[SESSIONS_INDEX] = _insert_block(index, BEGIN + "\n" + mblock + END + "\n")
    return ok


def _move_sessions(root: Path, plan: Plan, index: str) -> None:
    plan.writes = {}
    plan.move_to = FROZEN_SESSIONS
    line = ("- [the older entries, moved whole](sessions/SESSIONS-ARCHIVE.md)"
            " — the session archive could not be cut with a proof, so it was"
            " moved here by `tools/archivecut.py`\n")
    plan.writes[SESSIONS_INDEX] = _insert_block(index, line)
    try:
        text = _read(root, SESSIONS_SRC) or ""
    except UnicodeDecodeError:
        return
    mv = Move(SESSIONS_SRC, "docs", FROZEN_SESSIONS, FROZEN_SESSIONS,
              frozenset([FROZEN_SESSIONS]))
    moved, edits = relocate(text, mv)
    back, _ = unrelocate(moved, mv)
    _check(plan.proof, back == text,
           f"route (b): {len(edits)} link paths re-pointed in the moved file, "
           "each maps back to its original")
    plan.writes[FROZEN_SESSIONS] = moved


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


def verify(root: Path) -> list[str]:
    """Lines of a verdict; a line starting FAIL means a mismatch."""
    out: list[str] = []
    # board
    src = committed_source(root, BOARD_SRC)
    if (root / BOARD_SRC).exists():
        out.append(f"--    {BOARD_SRC}: still in place, not cut")
    elif src is None:
        out.append(f"--    {BOARD_SRC}: never committed here")
    elif (root / FROZEN_BOARD).is_file():
        mv = Move(BOARD_SRC, "docs", FROZEN_BOARD, FROZEN_BOARD,
                  frozenset([FROZEN_BOARD]))
        back = unrelocate(_read(root, FROZEN_BOARD) or "", mv)[0]
        out.append(("PASS" if back == src else "FAIL")
                   + f"  {BOARD_SRC}: route (b), the moved file maps back to "
                   "its last committed copy")
    else:
        readme = _read(root, SECTION_README)
        if readme is None:
            out.append(f"FAIL  {BOARD_SRC}: gone, and {SECTION_README} is missing")
        else:
            names = [p.name for p in (root / SECTION_DIR).glob("*.md")
                     if p.name != "README.md"]
            moves = board_moves(names)
            items = {n: unrelocate(_read(root, f"{SECTION_DIR}/{n}") or "",
                                   moves[f"{SECTION_DIR}/{n}"])[0] for n in names}
            body = unrelocate(readme, moves[SECTION_README])[0]
            rebuilt = board_reconstruct(body, items)
            used = {m.group(1) for line in split_lines(readme)
                    if (m := REF_RE.match(line.rstrip("\n")))}
            ok = rebuilt == src
            out.append(("PASS" if ok else "FAIL")
                       + f"  {BOARD_SRC}: {len(names)} item files and the section "
                       "README rebuild its last committed copy byte for byte")
            spare = sorted(set(n[:-3] for n in names) - used)
            if spare:
                out.append(f"FAIL  {SECTION_DIR}: {len(spare)} item files the "
                           "README does not link")
    # sessions
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
        index = _read(root, SESSIONS_INDEX) or ""
        got = _extract_block(index)
        if got is None:
            out.append(f"FAIL  {SESSIONS_SRC}: gone, and {SESSIONS_INDEX} holds "
                       "no cut block")
        else:
            block = got[0]
            names = [m.group(1) for line in split_lines(block)
                     if (m := SESSION_REF_RE.match(line.rstrip("\n")))]
            pre = next((n for n in names if "-archived-000-" in n), None)
            self_target = f"{SESSIONS_DIR}/{pre}" if pre else SESSIONS_INDEX
            reps = frozenset([self_target])
            files = {}
            for n in names:
                p = f"{SESSIONS_DIR}/{n}"
                files[n] = unrelocate(_read(root, p) or "",
                                      Move(SESSIONS_SRC, "docs", p, self_target, reps))[0]
            back = unrelocate(block, Move(SESSIONS_SRC, "docs", SESSIONS_INDEX,
                                          self_target, reps, SESSION_REF_RE))[0]
            ok = sessions_reconstruct(back, files) == src
            out.append(("PASS" if ok else "FAIL")
                       + f"  {SESSIONS_SRC}: {len(names)} detail files and the "
                       "index block rebuild its last committed copy byte for byte")
    return out


# --------------------------------------------------------------------------
# apply and report
# --------------------------------------------------------------------------

def apply(root: Path, plan: Plan) -> None:
    if plan.route == "cut":
        r = _git(root, "rm", "-q", "--", plan.src)
        if r.returncode != 0:
            (root / plan.src).unlink()
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
    lines = [f"{plan.kind}: {plan.src} — route: "
             + {"cut": "(a) cut into the store",
                "move": "(b) moved whole (the cut could not prove itself)",
                "absent": "nothing to do (no such file)",
                "blocked": "blocked"}[plan.route]]
    for r in plan.reasons:
        lines.append(f"  reason: {r}")
    for p in plan.proof:
        lines.append(f"  {p}")
    if plan.route == "cut":
        what = "item files" if plan.kind == "board" else "detail files"
        lines.append(f"  {plan.items} {what}"
                     + (f" under {plan.headings} `## ` headings" if plan.kind == "board" else ""))
    if plan.route == "move":
        lines.append(f"  moves to {plan.move_to}")
    if plan.route in ("cut", "move"):
        lines.append(f"  links re-pointed elsewhere in the tree: {plan.link_edits}"
                     f" in {plan.link_files} files")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Cut a repo's frozen pre-split archives (ROADMAP-DONE.md, "
                    "SESSIONS-ARCHIVE.md) into the store form, with a proof; "
                    "move them whole where the proof fails.")
    act = ap.add_mutually_exclusive_group()
    act.add_argument("--plan", action="store_true",
                     help="say which route each archive would take, with the "
                          "proof; write nothing (the default)")
    act.add_argument("--cut", action="store_true",
                     help="carry the plan out: write the outputs, `git rm` or "
                          "`git mv` the source, re-point links")
    act.add_argument("--verify", action="store_true",
                     help="rebuild each cut archive from the files on disk and "
                          "compare it with its last committed copy")
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
    if any(p.route == "blocked" for p in plans):
        print("archivecut: blocked; nothing written", file=sys.stderr)
        return 1
    # Board first; the session plan re-reads the tree so its link edits land
    # on top of the board's.
    apply(root, plans[0])
    second = plan_sessions(root)
    apply(root, second)
    return 0


if __name__ == "__main__":
    sys.exit(main())
