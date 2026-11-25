"""The single-sourced file walk shared by every scanner (`115/080`, part 1).

`_walk_files` existed as **eleven** separate, near-identical copies —
`secretscan`, `leakscan`, `conflictscan`, `linkscan`, `sizescan`, `datescan`,
`wrapscan`, `spellscan`, `pathscan`, `licenscan`, `stampscan` — all written in
one sitting on 2026-09-20 (`020/380`, converting the guard layer's file
enumeration from `base.rglob("*")` funnelled through a list comprehension —
which forced the WHOLE subtree to be walked and every `Path` held before a
single file was scanned — to a streamed `os.walk`). `os.walk` is used rather
than `rglob` specifically because it exposes `dirnames` for in-place pruning:
filtering skip-names out of `dirnames` stops the walk from ever DESCENDING
into `.git`, `node_modules`, etc. at any depth, rather than descending into
them and discarding what it found — the same skip semantics as the pre-020/380
`not (SKIP_DIR_NAMES & set(p.parts))` filter (any path component, not just
the immediate parent), just applied before the walk pays for it instead of
after.

Diffed byte-for-byte across all eleven copies (2026-09-21): the walk body
itself was already identical in ten of them and differed from the eleventh
(`licenscan`) in exactly one respect — WHICH directory names get skipped.
Ten scanners skip a common ten-name set (`.git`, `node_modules`,
`__pycache__`, `.venv`, `venv`, `.mypy_cache`, `.ruff_cache`, `.pytest_cache`,
`.idea`, `.vscode`); `licenscan` skips a twelve-name set that additionally
prunes `dist` and `build`, because a licence check has no reason to inspect
built/vendored output the way, say, a link check might. That is a genuine
per-guard difference, not drift — so it stays a parameter here rather than
being flattened into one shared constant that would silently change
`licenscan`'s output. Every other difference the eleven copies carried
(docstring prose, incident citations, variable naming — `SKIP_DIR_NAMES` vs
`sizescan`'s `NON_CONTENT_DIR_NAMES`) was cosmetic and is retired by this
single source; the calling scanner still owns and names its own skip-set.

The `020/160` (E9) linked-worktree fix — pruning a `.git` FILE (a worktree's
`gitdir:` link) the same way a `.git` DIRECTORY is pruned, so the walk never
descends into a second, nested checkout of the same repo — was present,
identically, in all eleven copies already; it is preserved here unchanged.

Explicitly NOT in this module: the allow-marker grammar and ignore-file
loaders (part 2 of `115/080`), the exit/reporting contract and finding
identifiers (part 3), and the window/overlap streaming-line readers and the
finding-materialisation cap that the same `020/380` commit also introduced
alongside this walk. Those readers are a DIFFERENT mechanism from the walk —
some guards need windowed re-scanning with overlap (an arbitrary-position
credential match could straddle a window cut), one guard's reader also
carries markdown fenced-code-block state (`linkscan`), several guards use a
truncation-only reader with no overlap at all (their matches are anchored at
line start), and one guard reads the whole file up to a byte cap with no
line-splitting at all (`licenscan`). Folding those into "the walk" was
examined and rejected for this part — see the `115/080` part 1 hand-back for
the full breakdown; consolidating them safely is a separate decision, not
this module's job.

110 (guards walk untracked trees): `walk_files` now asks git first. Inside a
git work tree it STREAMS `git ls-files -z --cached --others
--exclude-standard` (tracked files plus untracked files that are not
ignored: everything that could be committed) instead of `os.walk`-ing the
whole disk. A gitignored file can never be committed, so not reading it loses
no protection, and one real repo went from 15.8 GB walked to its 132 MB
tracked. The per-guard `skip_dir_names` and the linked-worktree skip are
applied to the paths git yields, so each guard's own exclusions still hold.
Where git cannot answer (root outside a work tree, root itself ignored, git
missing) the original `os.walk` runs; `LAST_MODE` records which path ran, and
a git that is missing (as opposed to simply absent from this tree) says so on
stderr, once per process. A git that fails partway raises.

Nested repositories: `ls-files` reports a nested clone (or a tracked
submodule) as one directory entry, not its files. Those entries are walked
with the old `os.walk` so a nested plain clone's content is still read
exactly as before (FW9), and a directory whose `.git` is a FILE (linked
worktree, initialised submodule) is still pruned (020/160).

Tracked files under a skip-named directory (160/600, GW1). The skip names
exist to stop the walk paying for litter. In git mode that reason is gone: git
never lists litter, so the only thing a skip name can still remove is a file
that could be committed - and, for a tracked file, already was. A caller that
is a boundary guard (a secret, a leak or a conflict marker in a committed
editor-settings or vendored file must not pass the whole-tree plane) passes
`read_tracked_under_skip=True`, and then the skip names apply to untracked
entries and nested walks only; a tracked file is always yielded. The default is
False, so every other guard keeps its own skip contract unchanged (a prose or
licence check has no business reading vendored output). Decided per guard, as
the cold pass counselled; the three that pass True are `secretscan`,
`leakscan` and `conflictscan`.

What the walk guarantees, and what it does not (GW4, GW5, GW8, GW10):
  * A yielded path never has a symlinked parent directory. Git can index
    `d/f.txt` while the worktree has `d` replaced by a link out of the root;
    reading it would read a file outside the tree. (A leaf that is a symlink to
    a file is still yielded, as before.)
  * Every git call runs with `core.fsmonitor=false`. A repository's own
    `.git/config` can name a command for `fsmonitor`, and git would run it for
    `ls-files`; scanning a tree must not execute anything the tree names. Other
    tree-configured commands (hooks) are not run by the calls made here. A
    guard pointed at a tree the operator does not trust still trusts git itself
    to parse that tree's index and config.
  * No git call has a timeout. A git that hangs hangs the guard: it stops, it
    does not pass. Recorded rather than bounded, because any bound short enough
    to matter would fall back to the whole-disk walk this module exists to avoid.
  * The walk answers "which paths", not "which content". At the hook a
    staged-then-deleted file is committed unread and a file whose worktree copy
    differs from its staged copy is read in the worktree version. The three
    boundary guards avoid this with `--staged`; the others do not.
  * Fallbacks speak. `os.walk:not-in-git-tree` (git says there is no
    repository, nothing above the directory looks like one) is the ordinary
    case and stays silent. Where git itself failed - it cannot be run, or
    refuses a tree that carries a `.git` entry (dubious ownership, a corrupt
    HEAD) - the walk says so once on stderr and `LAST_MODE` is
    `os.walk:git-failed`, because the wide fallback reads the ignored files
    again and the result would otherwise change with the machine (GW2).

Pruned files are counted, not silently dropped (320/900). In the `os.walk`
fallback a skip-named directory (`.vscode`, `.idea`, `node_modules`...) is
never descended into, so whatever it holds is never read - and before this,
nothing said so: a scan over a plain (non-git) tree with a secret only under
`.vscode/` read exactly as green as a scan over a tree with no `.vscode/` at
all. A caller passes a `PruneCount` as `walk_files(..., pruned=)` and the
fallback adds to it the regular files under each directory it prunes by skip
name. They are counted, never opened: the count lists directory entries and
reads no content, but it does list them, so it costs a directory walk of the
pruned subtree. That is why it is opt-in per caller rather than always on.
Not counted:
  * `.git` directories, at any depth - repository metadata, not content, and
    never yielded in git mode either; counting a nested clone's object store
    would make every tree holding one warn.
  * directories pruned as a linked worktree / initialised submodule (a `.git`
    FILE, 020/160): they are another checkout, not a skip-named directory.
  * the git-mode walk. It prunes nothing the way `os.walk` does (its skip
    names act on the paths git lists), so the count is not measured there and
    the `PruneCount` records that a git walk ran (`git_walks`); a caller then
    says "not counted", never a zero it did not measure. Git mode's yielded
    set is unchanged by this.
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable, Iterator

# Which enumeration the most recent `walk_files` call used: "git",
# "os.walk:not-in-git-tree", "os.walk:root-ignored", "os.walk:git-unavailable"
# or "os.walk:git-failed".
LAST_MODE: str | None = None

_WARNED: set[str] = set()


class PruneCount:
    """What the `os.walk` fallback stepped over without reading (320/900).

    `files`: regular files under a directory pruned by skip name, summed over
    every `walk_files` call given this object (a scanner walks several roots
    into one tally). `dirs`: the skip-named directories pruned. `git_walks`:
    how many of those calls took the git path, where nothing is counted - so a
    renderer can tell a measured zero from an unmeasured one."""

    __slots__ = ("files", "dirs", "git_walks")

    def __init__(self) -> None:
        self.files = 0
        self.dirs = 0
        self.git_walks = 0

    # Value semantics, so a tally holding one compares and copies (asdict) by
    # its counts, as its plain int fields do.
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PruneCount):
            return NotImplemented
        return ((self.files, self.dirs, self.git_walks)
                == (other.files, other.dirs, other.git_walks))

    __hash__ = None  # mutable

    def __repr__(self) -> str:
        return (f"PruneCount(files={self.files}, dirs={self.dirs}, "
                f"git_walks={self.git_walks})")

    @property
    def measured(self) -> bool:
        """False when a walk ran through git and the fallback counted
        nothing: the zero would then not be a measured one. A run that mixes
        both and did prune something reports what the fallback counted, a
        floor."""
        return self.git_walks == 0 or self.files > 0 or self.dirs > 0

    def as_json(self) -> "int | None":
        """The `--json` value: the count, or None when it was not measured."""
        return self.files if self.measured else None


def _count_pruned(top: str) -> int:
    """Regular files under `top`, by directory listing alone (no file is
    opened). Does not follow directory symlinks (as `os.walk` does not) and
    does not descend into `.git` directories. A leaf symlink to a file counts,
    as the walk would have yielded it. An unreadable directory counts as
    what could be listed: the count is a floor, never an inflation."""
    n = 0
    stack = [top]
    while stack:
        d = stack.pop()
        try:
            with os.scandir(d) as it:
                for e in it:
                    try:
                        if e.is_dir(follow_symlinks=False):
                            if e.name != ".git":
                                stack.append(e.path)
                        elif e.is_file():
                            n += 1
                    except OSError:
                        continue
        except OSError:
            continue
    return n
_GIT_ENV_DROP = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_PREFIX")


def _git_env() -> dict:
    # Hooks export GIT_DIR / GIT_INDEX_FILE; the answer must depend on the
    # directory being walked, not on whatever invoked the guard.
    return {k: v for k, v in os.environ.items() if k not in _GIT_ENV_DROP}


# GW5: never let a tree's own `.git/config` name a command for git to run on
# our behalf (`core.fsmonitor` is run by `ls-files`). Prepended to every call.
_GIT_SAFE = ("-c", "core.fsmonitor=false")


def _git(base: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *_GIT_SAFE, "-C", str(base), *args],
                          capture_output=True, env=_git_env(), check=False)


def _warn_once(key: str, text: str) -> None:
    if key not in _WARNED:
        _WARNED.add(key)
        print(text, file=sys.stderr)


def _has_git_entry(base: Path) -> bool:
    """True if `base` or any ancestor has a `.git` entry (directory or file):
    the tree looks like a repository, so a git that will not answer for it has
    FAILED rather than reported "no repository"."""
    try:
        here = base.resolve()
    except OSError:
        here = base.absolute()
    return any((d / ".git").exists() for d in (here, *here.parents))


def _git_unusable(base: Path) -> str:
    """"" when `base` can be enumerated through git, else the reason code."""
    try:
        r = _git(base, "rev-parse", "--is-inside-work-tree")
    except OSError as exc:
        _warn_once("unavailable",
                   f"filewalk: git unavailable ({exc}); walking the whole "
                   "directory tree, untracked and ignored files included")
        return "git-unavailable"
    if r.returncode != 0 or r.stdout.strip() != b"true":
        if r.returncode != 0 and _has_git_entry(base):
            # GW2: a repository that git will not enumerate (dubious
            # ownership, a corrupt HEAD) is not "no repository".
            detail = (r.stderr.decode(errors="replace").strip().splitlines()
                      or ["no detail"])[0][:200]
            _warn_once("failed",
                       f"filewalk: git could not enumerate {base} ({detail}); "
                       "walking the whole directory tree, untracked and "
                       "ignored files included")
            return "git-failed"
        return "not-in-git-tree"
    # A root that is itself gitignored lists nothing under --others; the
    # caller asked for it explicitly, so read it with the plain walk.
    if _git(base, "check-ignore", "-q", ".").returncode == 0:
        return "root-ignored"
    return ""


def _stream_nul(proc: subprocess.Popen) -> Iterator[bytes]:
    """NUL-separated records from `proc.stdout`, read incrementally."""
    buf = b""
    while True:
        chunk = proc.stdout.read1(1 << 16)
        if not chunk:
            break
        buf += chunk
        *recs, buf = buf.split(b"\0")
        yield from recs
    if buf:
        yield buf


def _git_walk(base: Path, skip: "frozenset | set",
              tracked_ignores_skip: bool = False) -> Iterator[Path]:
    err = tempfile.TemporaryFile()
    # `-t` tags every record: `H ` for a tracked path, `? ` for an untracked
    # one (GW1 needs to tell them apart).
    proc = subprocess.Popen(
        ["git", *_GIT_SAFE, "-C", str(base), "ls-files", "-z", "-t",
         "--cached", "--others", "--exclude-standard"],
        stdout=subprocess.PIPE, stderr=err, env=_git_env())
    ok_dirs: dict[tuple[str, bool], bool] = {("", True): True, ("", False): True}

    def dir_ok(rel_dir: str, honour_skip: bool = True) -> bool:
        """False if a component is in `skip` (only when `honour_skip`), the
        directory is a symlink (GW4), or it is a linked worktree /
        initialised submodule (a `.git` FILE)."""
        key = (rel_dir, honour_skip)
        hit = ok_dirs.get(key)
        if hit is None:
            parent, _, leaf = rel_dir.rpartition("/")
            hit = ((not honour_skip or leaf not in skip)
                   and dir_ok(parent, honour_skip)
                   and not (base / rel_dir).is_symlink()
                   and not (base / rel_dir / ".git").is_file())
            ok_dirs[key] = hit
        return hit

    finished = False
    try:
        last = None
        for raw in _stream_nul(proc):
            if raw == last:  # unmerged paths are listed once per stage
                continue
            last = raw
            tracked = raw[:1] != b"?"
            rel = os.fsdecode(raw[2:])
            is_dir_entry = rel.endswith("/")
            rel = rel.rstrip("/")
            honour = not (tracked and tracked_ignores_skip)
            if not dir_ok(rel.rpartition("/")[0], honour):
                continue
            p = base / rel
            if is_dir_entry or (not p.is_symlink() and p.is_dir()):
                # nested clone / submodule: git does not list its files.
                if rel.rpartition("/")[2] not in skip and not (p / ".git").is_file():
                    yield from _os_walk(p, skip)
                continue
            if p.is_file():  # drops files deleted from the tree but still cached
                yield p
        finished = True
    finally:
        if not finished:
            proc.kill()
        proc.stdout.close()
        rc = proc.wait()
        err.seek(0)
        msg = err.read().decode(errors="replace").strip()
        err.close()
        if finished and rc != 0:
            raise RuntimeError(f"filewalk: `git ls-files` failed (exit {rc}): {msg}")


def walk_files(base: Path, skip_dir_names: Iterable[str],
               read_tracked_under_skip: bool = False,
               pruned: "PruneCount | None" = None) -> Iterator[Path]:
    """Every regular file under `base`, streamed one at a time.

    Inside a git work tree: tracked plus untracked-not-ignored files via a
    streamed `git ls-files` (see the module docstring). Otherwise `os.walk`
    (`_os_walk`). `LAST_MODE` records the path taken.

    `skip_dir_names` is a per-guard PARAMETER, not a shared constant — see
    the module docstring: ten callers pass an identical ten-name set and one
    (`licenscan`) passes a twelve-name set that additionally prunes `dist`
    and `build`.

    `read_tracked_under_skip` (GW1, 160/600): in git mode, yield a TRACKED
    file even when it sits under a skip-named directory; the skip names then
    apply to untracked entries and nested walks only. For the boundary
    guards. Ignored in the `os.walk` fallback, which has no notion of
    tracked.

    `pruned` (320/900): a `PruneCount` the `os.walk` fallback adds to, one
    count per regular file under a directory it prunes by skip name (see the
    module docstring for what is and is not counted). In git mode it is only
    marked as a git walk. Omitted, nothing is counted and nothing extra is
    listed."""
    global LAST_MODE
    skip = skip_dir_names if isinstance(skip_dir_names, (set, frozenset)) else set(skip_dir_names)
    why = _git_unusable(Path(base))
    if why:
        LAST_MODE = "os.walk:" + why
        yield from _os_walk(base, skip, pruned)
        return
    LAST_MODE = "git"
    if pruned is not None:
        pruned.git_walks += 1
    yield from _git_walk(Path(base), skip, read_tracked_under_skip)


def _os_walk(base: Path, skip: "frozenset | set",
             pruned: "PruneCount | None" = None) -> Iterator[Path]:
    """The original walk: `os.walk`, pruning `skip` from `dirnames` in place
    so it never DESCENDS into them at any depth. With `pruned`, each
    skip-named directory pruned (other than `.git`) has its regular files
    counted onto it, unread (320/900)."""
    for dirpath, dirnames, filenames in os.walk(base):
        # 020/160 (E9): a git worktree LINKED into this tree has a `.git`
        # FILE (`gitdir: <path>`), not a directory, so a name-only skip set
        # never fires and the walk descends into a full second checkout of
        # the same repo — double-counting every finding and putting
        # root-relative ignore globs out of reach inside the copy. Checked
        # by file-ness alone, not by parsing the `gitdir:` line: a bare file
        # named exactly `.git` is never anything else (only a worktree or
        # submodule link creates one), and pruning here is the same
        # name/type check the skip-set already makes, not a content
        # decision.
        if pruned is not None:
            for d in dirnames:
                full = os.path.join(dirpath, d)
                # A symlinked directory is never descended into whatever its
                # name, so pruning it hides nothing the walk would have read.
                if d in skip and d != ".git" and not os.path.islink(full):
                    pruned.dirs += 1
                    pruned.files += _count_pruned(full)
        dirnames[:] = [
            d for d in dirnames
            if d not in skip
            and not Path(dirpath, d, ".git").is_file()
        ]
        for name in filenames:
            p = Path(dirpath) / name
            if p.is_file():  # excludes broken symlinks, matching the old rglob filter
                yield p
