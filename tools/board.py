#!/usr/bin/env python3
"""board — the roadmap is one file per item; ROADMAP.md is its generated index.

WHY THE BOARD SPLIT (ADR 2026-08-15, Mike's ruling)
----------------------------------------------------
One 4,000-line ROADMAP.md was simultaneously the unit of contention (every
session edits it, and a wholesale revert destroyed a sibling session's in-flight
work), the unit of reading (~67k tokens at every session open), and the unit of
truth for a hundred-plus independent items whose "done" was asserted in prose
and drifted from the tree five recorded times. Splitting the store to one file
per item under `docs/roadmap/` fixes all three at the grain where they occur:
two sessions on different items now touch different files; the session-start
read is a short index; and an item's own `git log` is its provenance — which
commit flipped its state, and what work that commit carried.

THE LAYOUT THIS TOOL OWNS
--------------------------
    docs/roadmap/README.md              board preamble (checkbox legend etc.)
    docs/roadmap/<NN>-<section>/README.md   section narrative, verbatim
    docs/roadmap/<NN>-<section>/<NN>-<slug>.md  ONE item: its checkbox line
                                          first, continuations beneath
    docs/ROADMAP.md                     GENERATED index — never hand-edited

Item files keep the board's existing checkbox grammar VERBATIM — `- [ ]` open,
`- [~] (claimed …)`, `- [x]` done, `- ⏳` a queued-review pointer — because
every scanner that reads items (`harvestscan`, `pointerscan`, `sizescan`)
already speaks that grammar, and a second state vocabulary (frontmatter) would
be one fact in two homes. State lives in the item file's first line and nowhere
else; the index derives from it.

WHY THE INDEX IS COMMITTED AND CHECKED, NOT HAND-KEPT
------------------------------------------------------
A committed derived file can drift from its source — the estate's most-recorded
defect class. So this tool is wired into the floor as a CHECK: a commit whose
index does not match its item files fails, with the remedy printed (run
`rebuild`) — on CI unconditionally; at the hook, `--staged` (below) reads the
git INDEX rather than the worktree, the same plane harvestscan's HV4 reads for
the identical reason: the hook's question is what this commit is about to make
true, which is neither HEAD nor an unstaged edit lying dirty in the same
checkout. That closes the two live slips BS1 named (2026-08-15) — an index
rebuilt but never staged, and a rebuild that read a sibling's dirty item line
off the worktree and baked it into the committed index — because both are
content the INDEX never had. `rebuild --from-index` (below) is the matching
write-side fix: it regenerates from the same plane, so a claimer at a dirty
primary checkout (CONCURRENCY.md § Claiming work) never absorbs a sibling's
unstaged line into the file it is about to stage. CI keeps the plain
(worktree) form — a CI checkout has no unstaged state to confuse it with, so
the worktree already IS the committed tree there, and `--staged` would answer
a question CI cannot ask (BS1 → `010/020`, FUNDED 2026-08-17, landed
2026-09-20). Two sessions closing different items both regenerate; if their
index hunks collide, the resolution is deterministic — regenerate again after
the merge. The index renders done items as `✅`, never `[x]`, so `sizescan`'s
cold-content gate (a `[x]` on the hot path) can never fire on a generated line.

The index opens with a GENERATED marker line. Scanners that lint *item* grammar
(`pointerscan`) skip any file carrying it — the index's one-line renderings are
projections, not the items themselves.

CHILD REPOS. A repo with no `docs/roadmap/` directory is not using the split
board; the check reports not-in-scope and exits 0. That is the same graceful
posture every scoped scanner takes, and it is not fail-open: the check's
subject (a generated index) does not exist where the store does not.

WHAT THE GENERATOR MAY NOT ASSUME (learned from the first child, 2026-08-17).
This tool writes text that is READ somewhere it was never written for, so
every string it emits into a committed file must be true in a repo that is
not this one. Two ways that failed at once when `faves` adopted the board:
the banner named `tools/board.py`, which exists only where the tool lives —
children CALL the floor's tools and never vendor them (ADR 0008) — and the
section links repeated their own path as the link TEXT, which `pathscan`
resolves, so a clean child produced one false finding per section on every
commit. Hence `rebuild_cmd()`: repo-relative where the tool is inside the
tree, the hook's `$ATELIER_TOOLS` spelling where it is not, and NEVER an
absolute path, which would put a machine-local fact into a public file.

STATED RESIDUAL — RETIRED 2026-09-20 (010/020, BS1's fund). The gap above used
to be permanent: `--check` compared the WORKTREE's item files against the
WORKTREE's index unconditionally, so a commit that staged an item edit
without the rebuilt index — or one that staged a rebuild which had quietly
absorbed a sibling's dirty item line — passed the hook every time, on nothing
stronger than "worktree happened to agree with itself", and only failed later
on CI. `--staged` closes it by reading the INDEX instead, on both sides of
the comparison: the built-index side reads item files via `git show :path`,
and the against side reads the committed `docs/ROADMAP.md` the same way,
so the question answered is "does what's about to be committed already
agree with itself" — never "does the working directory agree with itself",
which is the question that let both slips through. `rebuild --from-index`
is the write-side twin, for regenerating cleanly at a dirty primary checkout.
What is NOT claimed: this does not protect a commit that stages BOTH a stale
item edit and a stale index together in one deliberate act — that is not a
plane confusion, it is just a wrong commit, and no check on which plane to
read defends against staging the wrong content on purpose.

Exit codes:  0 clean/not-in-scope · 1 stale index or invalid item file ·
2 environment error (bad root, or `--staged`/`--from-index` outside a git
repo — the INDEX plane has no meaning without one). `--selftest` proves the
core WORKTREE-plane logic offline; the INDEX plane needs a real git repo,
so it is proved by `test_board.py`'s git-backed test class instead.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

# `harvestscan` already named and solved this exact problem (HV4): which
# version of a tracked file a check should read — the WORKTREE (what's on
# disk, right for a hand-run or CI, where the checkout already IS the
# committed tree) or the INDEX (what's staged, right for the hook, because
# the hook's question is what THIS COMMIT is about to make true, and a
# sibling's dirty edit sitting in the same worktree is neither committed nor
# about to be). Reusing its vocabulary and its `git show :path` mechanism
# here answers the same question the same way instead of inventing a second
# one (BS1, 010/020's fund: "the same way harvestscan closed HV4").
sys.path.insert(0, str(Path(__file__).resolve().parent))
import harvestscan  # noqa: E402

WORKTREE = harvestscan.WORKTREE
INDEX = harvestscan.INDEX

BOARD_DIR = "docs/roadmap"
INDEX_REL = "docs/ROADMAP.md"

# The marker is matched as a PREFIX, and the legacy spelling is still accepted
# so no repo needs a flag day: an index generated before 2026-08-17 keeps its
# skip in pointerscan until its next rebuild, which the check demands anyway.
GENERATED_MARK = "<!-- GENERATED by board.py"
GENERATED_MARKS = (GENERATED_MARK, "<!-- GENERATED by tools/board.py")

# Where this tool sits inside the tree it rebuilds, when it sits there at all.
# Used to answer "is the repo-relative rebuild command true for a reader of the
# index I am writing?" — see rebuild_cmd, which must not answer that from the
# executing file's own path.
SELF_REL = "tools/board.py"

# The banner names NO path. It used to say `python3 tools/board.py rebuild`,
# which is true only in the repo the tool lives in — children call the floor's
# tools and never vendor them (ADR 0008), so in every child the one instruction
# printed at the top of the one file readers are told never to hand-edit named
# a file that was not there. The HOW moved to the preamble, which is built
# against a known root and can therefore be true from where the reader stands.
GENERATED_LINE = (
    "<!-- GENERATED by board.py — do not hand-edit; edit docs/roadmap/ -->"
)

# The board's item grammar — the SAME shape harvestscan/pointerscan read, but
# anchored to column 0: an item file's state line is top-level by definition,
# and an indented match is a sub-bullet of the item, not a second item.
STATE_RE = re.compile(r"^-\s+(\[[ x~]\]|⏳)\s*(.*)$")

# Eye-flags lifted from the state line into the index, in the order shown.
FLAGS = ("🎯", "🔥", "🛑", "⏳", "🔎", "🤔")

# A claim fragment, surfaced in the index so "who has this" is one glance.
CLAIM_RE = re.compile(r"\(claimed [^)]*\)")

TITLE_RE = re.compile(r"\*\*(.+?)\*\*")
LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
TITLE_MAX = 70

# Allow-markers on the source state line travel to the generated line: the
# projection reproduces the exempted text (a verbatim title can carry a
# non-ISO date), so it inherits the exemption — found live on day one, when
# the index re-flagged a date its item file had already scoped-allowed.
ALLOW_COMMENT_RE = re.compile(r"<!--[^>]*\ballow\b[^>]*-->")


def slug(text: str, limit: int = 46) -> str:
    """Filesystem-safe kebab slug, the session-file convention."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return text[:limit].rstrip("-") or "item"


def item_state(text: str) -> tuple[str, str] | None:
    """(marker, rest-of-line) from an item file's first item line, else None.

    Leading HTML comments and blank lines are tolerated — an item file may open
    with an allow-marker — but prose before the state line is a defect the
    check reports: state must be findable without reading the body.
    """
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("<!--"):
            continue
        m = STATE_RE.match(line)
        return (m.group(1), m.group(2)) if m else None
    return None


def index_title(rest: str) -> str:
    """The index line's link text: the item's bold title, links flattened.

    The fallback strips the claim first. `TITLE_RE` wants a CLOSED `**…**` span
    on the state line, and many real item files wrap the bold title across
    lines — so the state line carries an opening `**` and no closing one, the
    fallback takes the head of `rest`, and `rest` begins with the claim. The
    result rendered the claim twice on one line, once from `index_line` and
    once swallowed into the title (reported by a child, 2026-08-17)."""
    m = TITLE_RE.search(rest)
    raw = m.group(1) if m else CLAIM_RE.sub("", rest)
    raw = LINK_RE.sub(r"\1", raw)
    raw = raw.replace("*", "").replace("`", "").strip(" —-:")
    for f in FLAGS:
        raw = raw.replace(f, "")
    raw = " ".join(raw.split())
    if len(raw) > TITLE_MAX:
        raw = raw[:TITLE_MAX].rsplit(" ", 1)[0] + "…"
    return raw or "(untitled)"


def index_line(marker: str, rest: str, rel_link: str) -> str:
    """One generated index line for an item. `[x]` renders ✅ by design."""
    glyph = {"[ ]": "- [ ]", "[~]": "- [~]", "[x]": "- ✅", "⏳": "- ⏳"}[marker]
    flags = "".join(f for f in FLAGS if f in rest and f != marker)
    title = index_title(rest)

    # Flags and the claim fragment go BEFORE the link, and the reason is
    # mechanical, not taste. wrapscan exempts a line whose overflow is one
    # unbreakable token — which every item line is, because it ends in a
    # store path. Appending ` 🎯` put a space *after* that path, so the
    # overflow gained a legal wrap point and the exemption stopped applying:
    # in the first child, 13 of the index's 14 wrapscan findings were exactly
    # its 13 flagged lines, and nothing else. Leading them costs nothing, and
    # a reader gains a flag column that aligns instead of tracking flags to
    # ragged line ends. Allow-comments stay last — a trailing marker is how
    # every scanner reads them, and a line carrying one exempts itself anyway.
    line = glyph
    if flags:
        line += f" {flags}"
    if marker == "[~]":
        m = CLAIM_RE.search(rest)
        if m:
            line += f" {m.group(0)}"
    line += f" [{title}]({rel_link})"
    for c in ALLOW_COMMENT_RE.findall(rest):
        line += f" {c}"
    return line


def section_title(readme_text: str, fallback: str) -> str:
    for line in readme_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _is_this_tool(path: Path) -> bool:
    """Is `path` a copy of THIS tool, judged from its content?

    A name and a location are conventions; the generated marker is a fact this
    tool must carry to do its job, and it is pinned as a format constant (see
    GENERATED_MARKS) so a copy parked at an older revision still answers yes.
    Anything unreadable answers no — the caller's fallback is the spelling that
    is true everywhere, so failing that way costs a longer command and never a
    wrong one.
    """
    try:
        return GENERATED_MARK in path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False


def rebuild_cmd(root: Path) -> str:
    """The rebuild instruction, true from where the reader stands.

    In atelier the tool lives inside the tree it rebuilds, so the repo-relative
    path is both true and copy-pasteable. In a child it does not live there —
    and an absolute path must never be written into a committed file, because
    it is a machine-local fact in a tree that may be public. So a child gets
    the hook's own resolution, which is true everywhere and names nobody's
    home directory.

    THE CHILD SPELLING IS THE HOOK'S FULL ORDER, NOT ITS FIRST CHOICE. This
    shipped as `"$ATELIER_TOOLS"` and was wrong within the hour: `.githooks/
    pre-commit` resolves `${ATELIER_TOOLS:-$(git config hooks.atelierTools)}`,
    and on the machine that found it `ATELIER_TOOLS` is unset while the git
    config carries the path — so the emitted command expanded to
    `python3 /board.py` and the remedy printed at the moment a check fails was
    unusable. Naming half a fallback chain is the same defect one layer in:
    the first version named a file only atelier has, this one named a variable
    only some machines set. Emit the whole order or none of it.

    ASK THE TREE, NOT THE TOOL (2026-08-23). Deciding this from the *executing
    file's* location answers a different question than the one that matters,
    and the two answers diverge in exactly one geometry: a WORKTREE of atelier,
    driven by atelier's canonical tools path — which is the invocation this
    estate's own cross-tree guidance prescribes. There the tool sits outside
    the root, the child spelling is emitted, and every rebuilt index differs
    from the one on `main` by its banner: `check` calls a current index stale,
    and the remedy it prints — the only instruction offered at the moment a
    check fails — is the child form, which in atelier expands to
    `python3 /board.py rebuild` because atelier sets neither half of the chain.
    Running the remedy then writes the wrong banner into atelier's own index.
    The question is whether the repo-relative path is true FOR A READER of the
    index being written, so it is answered from the tree being written: if that
    tree carries this tool where the repo-relative spelling would name it, the
    spelling is true there whichever copy happens to be executing. Identity is
    confirmed from the file's content, not from its path — a child that vendors
    an unrelated `tools/board.py` must still get the portable spelling, and
    matching on the generated marker (a format constant, stable across
    revisions by design) keeps that true without making the answer depend on
    which revision the other tree is parked at.

    STAYS THE BARE WORD (roadmap 010/090). `main()` now prefers `--rebuild`,
    but this function's OUTPUT is embedded verbatim in a committed file
    (`build_index`'s preamble) across every repo on the fleet. Switching it
    to `--rebuild` changes that committed text for no behavioural gain — the
    bare word still runs — and would leave every existing checkout's
    `ROADMAP.md` stale against its own tool the moment this file's version
    bumped, which is exactly the drift class this whole tool exists to
    prevent. The flag form is the documented, preferred spelling everywhere
    a human reads it (CLAUDE.md, tools/README.md, `--help`); this one
    generated string keeps the spelling that costs nothing to leave alone.
    """
    root = root.resolve()
    here = Path(__file__).resolve()
    try:
        rel = here.relative_to(root)
    except ValueError:
        rel = Path(SELF_REL)
        if not _is_this_tool(root / rel):
            return ('python3 "${ATELIER_TOOLS:-$(git config hooks.atelierTools)}"'
                    "/board.py rebuild")
    return f"python3 {rel.as_posix()} rebuild"


_LEADING_NUMBER = re.compile(r"^(\d+)-")


def number_collisions(names: list[str], where: str, kind: str) -> list[str]:
    """Problems for every leading number used more than once in `names`.

    THE ONE SURVIVING COUNTER. The board's coordination-free naming argument
    (`CONCURRENCY.md` § Integration hygiene) retired next-N counters for records
    precisely because two sessions allocating from stale views collide in
    silence — but a section or item number is still a next-N counter, read off
    the directory. Two new files are not a shared line, so git sees no conflict,
    `rebuild` produces a perfectly well-formed index containing both, and the
    pair sorts adjacently and reads as intentional.

    Nothing asserted the numbers were unique, so nothing could report that they
    were not: the generator's clean verdict was honest and carried no
    information about this class at all. This is the assertion. It fires on
    `check` and on `rebuild` alike, because a rebuild that papers over the
    collision is how the last one survived a week.
    """
    seen: dict[str, list[str]] = {}
    for name in names:
        m = _LEADING_NUMBER.match(name)
        if m:
            seen.setdefault(m.group(1), []).append(name)
    out: list[str] = []
    for number, hits in sorted(seen.items()):
        if len(hits) > 1:
            out.append(
                f"{where}: {kind} number {number} is used {len(hits)} times — "
                + ", ".join(sorted(hits))
                + ". Renumber one: fewest inbound references moves "
                "(`PRINCIPLES.md` §10's tie-break).")
    return out


# A section, in the shape `build_index` consumes: its name, its README text
# (`None` if it has none — distinct from `""`, an empty-but-present file), and
# its items as (filename, file text) pairs, sorted. Both planes below produce
# exactly this shape so `build_index` never has to know which one it got.
_Section = tuple[str, "str | None", list[tuple[str, str]]]


def _worktree_sections(board: Path) -> tuple[bool, list[_Section]]:
    """(README present, sections) read off the DISK, exactly as before this
    item — the default plane, unchanged: a hand-run or CI form, where the
    checkout already IS the committed tree, so reading the filesystem directly
    answers the same question `git show HEAD:path` would, at a fraction of the
    process-spawning cost."""
    readme_present = (board / "README.md").is_file()
    sections: list[_Section] = []
    for sec in sorted(p for p in board.iterdir() if p.is_dir()):
        readme = sec / "README.md"
        rtext = readme.read_text(encoding="utf-8") if readme.is_file() else None
        items: list[tuple[str, str]] = []
        for f in sorted(sec.glob("*.md")):
            if f.name == "README.md":
                continue
            items.append((f.name, f.read_text(encoding="utf-8")))
        sections.append((sec.name, rtext, items))
    return readme_present, sections


def _index_sections(root: Path) -> tuple[bool, list[_Section]]:
    """Same shape as `_worktree_sections`, read off the git INDEX instead —
    the hook's plane (HV4). `git ls-files`, called with no revision, already
    lists the INDEX (the staged tree), not the worktree — a sibling's dirty,
    unstaged edit to a DIFFERENT item file changes nothing this call sees,
    because that file's path is unchanged; only its staged BLOB would need to
    change to show up here, and an unstaged edit never touches the blob.
    `git show :path` reads that same staged blob's content.
    """
    r = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--", f"{BOARD_DIR}/"],
        capture_output=True, text=True, check=False)
    paths = [line for line in r.stdout.splitlines() if line] \
        if r.returncode == 0 else []

    prefix = f"{BOARD_DIR}/"
    by_section: dict[str, list[str]] = {}
    top_readme = False
    for p in paths:
        rest = p[len(prefix):]
        parts = rest.split("/")
        if len(parts) == 1:
            if parts[0] == "README.md":
                top_readme = True
            continue
        if len(parts) == 2:
            sec_name, fname = parts
            by_section.setdefault(sec_name, [])
            if fname != "README.md":
                by_section[sec_name].append(fname)
        # A store deeper than section/file is not this layout's shape — the
        # worktree walk (`sec.glob("*.md")`) does not recurse either, so a
        # stray nested path is silently outside both planes' scope alike.

    sections: list[_Section] = []
    for sec_name in sorted(by_section.keys()):
        rtext = harvestscan.git_show(root, "", f"{prefix}{sec_name}/README.md")
        items = [(fname, harvestscan.git_show(root, "", f"{prefix}{sec_name}/{fname}") or "")
                 for fname in sorted(by_section[sec_name])]
        sections.append((sec_name, rtext, items))
    return top_readme, sections


def build_index(
    board: Path,
    source: str = WORKTREE,
    _read: tuple[bool, list[_Section]] | None = None,
) -> tuple[str, list[str]]:
    """(index text, problems). Deterministic: sorted dirs, sorted files.

    `source` selects the PLANE — WORKTREE (default, the disk as it stands) or
    INDEX (the git index — what is staged, HV4's plane). Everything below the
    read is plane-agnostic: the two `_*_sections` helpers above are the only
    place that knows which one it is looking at. `_read` lets a caller that
    already paid for the read (`run_check`'s scope check) hand its result in
    rather than paying for a second `git ls-files`/`git show` pass per item —
    internal only, no test or caller outside this module should pass it.
    """
    problems: list[str] = []
    parts: list[str] = [GENERATED_LINE, ""]
    root = board.parent.parent
    cmd = rebuild_cmd(root)
    if _read is not None:
        readme_present, sections = _read
    elif source == INDEX:
        readme_present, sections = _index_sections(root)
    else:
        readme_present, sections = _worktree_sections(board)

    # The preamble is LINKED, never inlined: its relative links are written
    # for its own home (docs/roadmap/), and inlining the text at the index's
    # depth would break every one of them — one text cannot be correct at two
    # depths. The index carries only what it generates.
    parts.append("# ROADMAP — board index")
    parts.append("")
    if readme_present:
        # Wrapped by hand at the house width: it is the index's one line of
        # real prose, and the only finding left once the flags moved.
        parts.append("Board doctrine and the checkbox legend:")
        parts.append("[roadmap/README.md](roadmap/README.md). One item per "
                     "file; edit the item,")
        parts.append(f"then `{cmd}`.")
        parts.append("")
    else:
        problems.append(f"{BOARD_DIR}/README.md missing — the board preamble "
                        "(checkbox legend) has no home")

    problems.extend(number_collisions(
        [name for name, _, _ in sections], BOARD_DIR, "section"))

    for sec_name, rtext, items in sections:
        problems.extend(number_collisions(
            [name for name, _ in items], f"{BOARD_DIR}/{sec_name}", "item"))
        parts.append(f"## {section_title(rtext or '', sec_name)}")
        parts.append("")
        if rtext is not None:
            # Link TEXT, not just the target: the old text repeated the path,
            # and pathscan resolves both halves of a link, so every section
            # produced one finding per commit in any repo that scans the index
            # (49 in the first child to adopt). A generated file that always
            # fires a warn-only check is a check nobody reads.
            parts.append(f"*[Narrative](roadmap/{sec_name}/README.md)*")
            parts.append("")
        wrote = False
        for fname, text in items:
            state = item_state(text)
            if state is None:
                problems.append(
                    f"{BOARD_DIR}/{sec_name}/{fname}: no state line — an item "
                    "file opens with its checkbox line (`- [ ] …`), before any "
                    "prose")
                continue
            marker, rest = state
            parts.append(index_line(marker, rest,
                                    f"roadmap/{sec_name}/{fname}"))
            wrote = True
        if wrote:
            parts.append("")
    text = "\n".join(parts).rstrip() + "\n"
    return text, problems


def _is_git_repo(root: Path) -> bool:
    r = subprocess.run(["git", "-C", str(root), "rev-parse",
                        "--is-inside-work-tree"],
                       capture_output=True, text=True, check=False)
    return r.returncode == 0 and r.stdout.strip() == "true"


def run_check(root: Path, fix: bool, source: str = WORKTREE) -> int:
    """`source=INDEX` is the hook's plane (`--staged` / `--from-index`): the
    scope check, the built `want`, and (when not fixing) the `have` it is
    compared against are ALL read from the git index rather than the disk —
    reading the index for one side and the disk for the other would just move
    the plane confusion this item exists to close, not close it."""
    if source == INDEX and not _is_git_repo(root):
        print(f"✗ board: --staged/--from-index needs a git repository at "
              f"{root} — it reads the git index, which does not exist "
              "without one", file=sys.stderr)
        return 2
    board = root / BOARD_DIR
    read: tuple[bool, list[_Section]] | None = None
    if source == INDEX:
        read = _index_sections(root)
        if not read[0] and not read[1]:
            print(f"✓ board not in scope — no {BOARD_DIR}/ directory tracked "
                  "in the index (this repo does not use the split board, or "
                  "not on this plane yet).")
            return 0
    elif not board.is_dir():
        print(f"✓ board not in scope — no {BOARD_DIR}/ directory "
              "(this repo does not use the split board).")
        return 0
    want, problems = build_index(board, source=source, _read=read)
    for p in problems:
        print(f"✗ board: {p}")
    index = root / INDEX_REL
    if fix:
        # The WRITE always lands on disk — `rebuild`'s job either way is to
        # fix the WORKTREE file so it can be staged; only the READ that
        # decides what to write differs by plane.
        have = index.read_text(encoding="utf-8") if index.is_file() else ""
        if have != want:
            index.write_text(want, encoding="utf-8")
            print(f"✓ board: {INDEX_REL} rebuilt "
                  f"({len(want.splitlines())} lines).")
        else:
            print(f"✓ board: {INDEX_REL} already current.")
        return 1 if problems else 0
    # `--check` (not fixing): the comparison target is plane-dependent too.
    # On the INDEX plane the question is "does what's STAGED already agree
    # with itself" — so `have` must be the staged blob (`git show :path`),
    # never the disk file, which may carry further unstaged edits the hook's
    # commit will never see. Reading disk here for the INDEX plane is exactly
    # the bug this item exists to close (BS1's slip (a)): it would let a
    # rebuilt-but-unstaged index read back as "current" because the disk copy
    # agrees with itself, while the staged blob the commit will actually ship
    # is still the stale one.
    if source == INDEX:
        have = harvestscan.git_show(root, "", INDEX_REL) or ""
    else:
        have = index.read_text(encoding="utf-8") if index.is_file() else ""
    if have != want:
        remedy = rebuild_cmd(root)
        if source == INDEX:
            # The safe remedy at THIS plane is the matching source flag: a
            # plain `rebuild` would read the worktree, which is exactly the
            # plane that may be dirty with a sibling's unrelated edit
            # (BS1's slip (b)) — the failure this check just caught the
            # hook-side symptom of.
            remedy += " --from-index"
        plane = "the staged " if source == INDEX else ""
        print(f"✗ board: {INDEX_REL} is stale against {plane}{BOARD_DIR}/ — "
              f"run: {remedy}   (then stage the index; "
              "after a merge conflict on the index, rebuilding IS the "
              "resolution)")
        return 1
    if not problems:
        plane = "the staged " if source == INDEX else ""
        print(f"✓ board index current — {INDEX_REL} matches {plane}"
              f"{BOARD_DIR}/.")
    return 1 if problems else 0


# ---------------------------------------------------------------------------
def selftest() -> int:
    import shutil
    import tempfile

    failures: list[str] = []

    def check(name: str, cond: bool) -> None:
        if not cond:
            failures.append(name)

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        sec = root / BOARD_DIR / "10-track-a"
        sec.mkdir(parents=True)
        (root / BOARD_DIR / "README.md").write_text(
            "# board\n\nlegend here\n", encoding="utf-8")
        (sec / "README.md").write_text("# Track A — live exposure\nwhy\n",
                                       encoding="utf-8")
        (sec / "10-fix-the-gate.md").write_text(
            "- [ ] 🎯 **Fix the gate** — the gate fails open\n      detail\n",
            encoding="utf-8")
        (sec / "20-done-thing.md").write_text(
            "- [x] **Shipped thing** — landed\n", encoding="utf-8")
        (sec / "30-claimed.md").write_text(
            "- [~] **Mid-flight** … (claimed 2026-08-15-0610, wt: b) more\n",
            encoding="utf-8")
        (sec / "40-pointer.md").write_text(
            "- ⏳ Rule-4 review queued — delta abc..def\n", encoding="utf-8")
        (sec / "50-marked.md").write_text(
            "- [ ] **Verbatim (15/7/26) title** "
            "<!-- datescan:allow: verbatim --> — body\n", encoding="utf-8")

        # not-in-scope: a bare tree passes without a board directory
        with tempfile.TemporaryDirectory() as bare:
            check("bare tree exits 0", run_check(Path(bare), fix=False) == 0)

        # a missing index is stale; rebuild writes it; then check passes
        check("missing index is stale", run_check(root, fix=False) == 1)
        check("rebuild exits 0", run_check(root, fix=True) == 0)
        check("rebuilt index passes", run_check(root, fix=False) == 0)

        text = (root / INDEX_REL).read_text(encoding="utf-8")
        check("generated marker first",
              text.splitlines()[0].startswith(GENERATED_MARK))
        check("banner names no path", "tools/board.py" not in
              text.splitlines()[0] and "$ATELIER_TOOLS" not in
              text.splitlines()[0])
        check("narrative link text is not path-shaped",
              "*[Narrative](roadmap/" in text
              and "*Narrative: [" not in text)
        # The selftest root is a tempdir, so this file is OUTSIDE it — which
        # is exactly a child's geometry, and the reason the child spelling is
        # the one the offline test proves.
        check("child root gets the portable rebuild command",
              'python3 "${ATELIER_TOOLS:-$(git config hooks.atelierTools)}"'
              "/board.py rebuild" in text)
        # Half a fallback chain expands to nothing on a machine that uses the
        # other half — the defect this replaced.
        check("child command names the whole resolution order",
              '"$ATELIER_TOOLS"' not in text)
        # THE THIRD GEOMETRY, which is neither atelier's checkout nor a
        # child's: a WORKTREE of atelier, where the executing copy is outside
        # the tree and the tree carries its own copy anyway. Judged from the
        # executing file alone this reads as a child, and every rebuild driven
        # from atelier's canonical tools path then differed from `main` by its
        # banner — a current index called stale, with an unusable remedy
        # printed beneath it (2026-08-23).
        with tempfile.TemporaryDirectory() as sibling:
            sib = Path(sibling)
            (sib / "tools").mkdir()
            (sib / "tools" / "board.py").write_text(
                f'MARK = "{GENERATED_MARK}"\n', encoding="utf-8")
            check("a sibling checkout carrying this tool gets the repo path",
                  rebuild_cmd(sib) == f"python3 {SELF_REL} rebuild")
            # Identity is read from content, so a name collision in a child
            # that vendors something else entirely still gets the form that
            # is true everywhere.
            (sib / "tools" / "board.py").write_text(
                "# an unrelated tool that happens to share the name\n",
                encoding="utf-8")
            check("an unrelated tools/board.py still gets the portable form",
                  rebuild_cmd(sib).startswith(
                      'python3 "${ATELIER_TOOLS'))
        check("no home directory in the index", str(Path.home()) not in text)
        check("open item rendered", "[Fix the gate]" in text)
        check("flag lifted", "🎯" in text)
        # The wrapscan exemption depends on the line ENDING in its path, so
        # the flag leading the link is load-bearing, not cosmetic.
        check("flag precedes the link", "- [ ] 🎯 [Fix the gate](" in text)
        check("no item line ends in a flag",
              not any(line.rstrip().endswith(FLAGS)
                      for line in text.splitlines()
                      if line.startswith("- ")))
        check("done renders ✅ never [x]",
              "- ✅ [Shipped thing]" in text and "- [x]" not in text)
        check("claim fragment surfaced",
              "(claimed 2026-08-15-0610, wt: b)" in text)
        check("pointer glyph kept", "- ⏳ [" in text)
        check("allow-marker travels to the generated line",
              "<!-- datescan:allow: verbatim -->" in text)
        check("section heading from README", "## Track A — live exposure" in text)
        check("preamble linked, never inlined",
              "(roadmap/README.md)" in text and "legend here" not in text)

        # editing an item makes the committed index stale again
        (sec / "10-fix-the-gate.md").write_text(
            "- [x] 🎯 **Fix the gate** — the gate fails open (done)\n",
            encoding="utf-8")
        check("state flip detected", run_check(root, fix=False) == 1)
        run_check(root, fix=True)

        # an item file with no state line is a reported defect
        (sec / "50-broken.md").write_text("just prose\n", encoding="utf-8")
        check("stateless item file fails", run_check(root, fix=True) == 1)
        (sec / "50-broken.md").unlink()
        run_check(root, fix=True)

        # A DUPLICATE NUMBER, at both grains. git sees no conflict — two new
        # files are not a shared line — so the generator has to be the one that
        # notices, and it must notice on `rebuild` too: papering over the
        # collision with a well-formed index is exactly how the 2026-08-17 one
        # survived unseen. A live item-level pair was found on this board while
        # this check was being written.
        dup = root / BOARD_DIR / "10-track-a-again"
        dup.mkdir()
        (dup / "README.md").write_text("# Track A again\n", encoding="utf-8")
        check("duplicate section number fails rebuild",
              run_check(root, fix=True) == 1)
        _, probs = build_index(root / BOARD_DIR)
        # Both names, not just a count: the message has to be actionable at
        # the moment it fires, and "10 is used twice" names nothing to fix.
        check("the section collision names both directories",
              any("section number 10" in p and p.count("10-track-a") == 2
                  for p in probs))
        shutil.rmtree(dup)

        (sec / "10-also-ten.md").write_text(
            "- [ ] **Also ten** — the sibling grain\n", encoding="utf-8")
        check("duplicate item number fails rebuild",
              run_check(root, fix=True) == 1)
        _, probs = build_index(root / BOARD_DIR)
        check("the item collision names its section",
              any("item number 10" in p and "10-track-a" in p for p in probs))
        (sec / "10-also-ten.md").unlink()
        check("clean numbering passes again", run_check(root, fix=True) == 0)

        # determinism: rebuild twice, byte-identical
        a = (root / INDEX_REL).read_text(encoding="utf-8")
        run_check(root, fix=True)
        b = (root / INDEX_REL).read_text(encoding="utf-8")
        check("rebuild is deterministic", a == b)

        # THE FLOOR'S OWN ARGV must run, not abort the process. This is the
        # CURRENT shape floor.py renders (`--check`/`--rebuild` ahead of
        # `--root`, `{scope}` trailing) — a flag has no position to fight
        # `paths` for, so this shape was never the one that aborted.
        check("floor argv runs (--check)",
              main(["--check", "--root", str(root), str(root)]) == 0)
        check("floor argv reaches the action (--rebuild)",
              main(["--rebuild", "--root", str(root), str(root)]) == 0)

        # THE LEGACY ARGV — every invocation on record before this fix, and
        # what floor.py itself rendered until this change: a bare leading
        # `check`/`rebuild` word. This is the shape that aborted with exit 2
        # once `{scope}` followed `--root` (roadmap 010/090), and it must go
        # on working verbatim — docs, hooks and every child still spell it
        # this way, and a flag day is not being demanded of them.
        check("legacy floor argv runs (bare check)",
              main(["check", "--root", str(root), str(root)]) == 0)
        check("legacy floor argv reaches the action (bare rebuild)",
              main(["rebuild", "--root", str(root), str(root)]) == 0)

        try:
            rc = main(["check", "--root", str(root), "--bogus"])
        except SystemExit as e:
            rc = e.code
        check("an unknown option is still an error (legacy word)", rc == 2)
        try:
            rc = main(["--check", "--root", str(root), "--bogus"])
        except SystemExit as e:
            rc = e.code
        check("an unknown option is still an error (flag)", rc == 2)

        # The default (neither spelling) stays `check`, and a caller may not
        # say both `check` and `rebuild` at once, in any spelling mix.
        check("no action defaults to check",
              main(["--root", str(root)]) == run_check(root, fix=False))
        try:
            rc = main(["--check", "--rebuild", "--root", str(root)])
        except SystemExit as e:
            rc = e.code
        check("--check and --rebuild are mutually exclusive", rc == 2)
        try:
            rc = main(["check", "--rebuild", "--root", str(root)])
        except SystemExit as e:
            rc = e.code
        check("a legacy word cannot combine with the opposite flag", rc == 2)

    if failures:
        print("board selftest FAIL: " + "; ".join(failures))
        return 1
    print("board selftest OK")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="--check (default) or --rebuild the generated roadmap "
                    "index; the bare `check`/`rebuild` words still work "
                    "(roadmap 010/090)")
    ap.add_argument("--check", action="store_true",
                    help="verify the index against docs/roadmap/ (default)")
    ap.add_argument("--rebuild", action="store_true",
                    help="regenerate the index from docs/roadmap/")
    # Two spellings, one switch: `--staged` for `--check` (harvestscan's own
    # name for this exact plane, HV4) and `--from-index` for `--rebuild`
    # (named for what it SELECTS, the house convention — `--from-archive`,
    # `--from-github` — not an imperative). Both flip the same `source`; a
    # caller may use either with either action, because the underlying
    # question ("read the git INDEX instead of the worktree") is identical
    # either way, and refusing the "wrong" spelling for the "wrong" action
    # would be ceremony with no defect behind it.
    ap.add_argument("--staged", dest="from_index", action="store_true",
                    help="read the git INDEX, not the worktree, when "
                         "checking — the hook's plane (harvestscan's HV4 "
                         "shape); CI and hand-runs keep the worktree "
                         "default, where the checkout already IS the "
                         "committed tree")
    ap.add_argument("--from-index", dest="from_index", action="store_true",
                    help="for --rebuild: regenerate from the git INDEX "
                         "rather than the (possibly dirty) worktree, so a "
                         "claimer at a dirty primary checkout never bakes a "
                         "sibling's unstaged item edit into the index this "
                         "commit is about to stage")
    ap.add_argument("--root", default=".")
    ap.add_argument("paths", nargs="*",
                    help="accepted for floor argv compatibility; the board "
                         "location is fixed at docs/roadmap/")
    ap.add_argument("--selftest", action="store_true")

    # `action` USED TO BE a positional-with-`choices` ahead of `paths` — the
    # ONLY bare positional action word anywhere in the floor's registry, every
    # neighbour (`sizescan` included) leads with a flag or with nothing. That
    # shape means a bare invocation omitting the literal word binds the FIRST
    # remaining positional to `action`, which then fails its choices check —
    # exactly what floor.py renders when it drops the leading `check` token,
    # and `board` is enforced with no advisory form, so every repo the floor
    # invoked it in went red on an argv it had itself rendered (roadmap
    # 010/090, reproduced at HEAD 2026-08-17). `parse_known_args` papered over
    # the acute break without touching the signature, which left the shape
    # itself as the standing risk: the next registry edit made by
    # pattern-matching every OTHER scanner reintroduces the abort.
    #
    # The fix is in the signature: `--check`/`--rebuild` flags, matching
    # `sizescan`'s house precedent, with `paths` the ONLY positional left —
    # nothing can ever bind to it ahead of schedule, because nothing else
    # competes for a position. floor.py's registry now renders `--check`, not
    # `check` (see tools/floor.py's `board` entry).
    #
    # BACKWARD COMPATIBILITY: every invocation on record before this change —
    # child repos, docs, hooks — spells this `board.py rebuild` / `board.py
    # check`, a bare LEADING word. Breaking that on a flag-day is worse than
    # the defect it fixes, so the legacy word is still accepted: stripped off
    # `argv[0]` before argparse ever sees it, so it cannot collide with
    # `paths` for a positional slot — there is no positional slot left to
    # collide with.
    if argv is None:
        argv = sys.argv[1:]
    else:
        argv = list(argv)
    legacy_action: str | None = None
    if argv and argv[0] in ("check", "rebuild"):
        legacy_action = argv.pop(0)

    # Unknown OPTIONS stay an error; unknown positionals are the scope this
    # tool has always ignored, because the board location is fixed at
    # docs/roadmap/ — `paths` absorbs them regardless of where they fall in
    # argv, which a lone `nargs="*"` positional can do that a positional pair
    # never could.
    args, extra = ap.parse_known_args(argv)
    unknown_opts = [a for a in extra if a.startswith("-")]
    if unknown_opts:
        ap.error("unrecognized arguments: " + " ".join(unknown_opts))
    if args.selftest:
        return selftest()

    want_check = args.check or legacy_action == "check"
    want_rebuild = args.rebuild or legacy_action == "rebuild"
    if want_check and want_rebuild:
        ap.error("--check and --rebuild (or their legacy words) are "
                 "mutually exclusive")

    root = Path(args.root)
    if not root.is_dir():
        print(f"✗ board: root {args.root} does not exist", file=sys.stderr)
        return 2
    source = INDEX if args.from_index else WORKTREE
    return run_check(root, fix=want_rebuild, source=source)


if __name__ == "__main__":
    sys.exit(main())
