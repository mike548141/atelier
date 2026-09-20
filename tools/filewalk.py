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
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, Iterator


def walk_files(base: Path, skip_dir_names: Iterable[str]) -> Iterator[Path]:
    """Every regular file under `base`, streamed one at a time via
    `os.walk`, pruning `skip_dir_names` from `dirnames` in place so the walk
    never DESCENDS into them at any depth.

    `skip_dir_names` is a per-guard PARAMETER, not a shared constant — see
    the module docstring: ten callers pass an identical ten-name set and one
    (`licenscan`) passes a twelve-name set that additionally prunes `dist`
    and `build`. Passing it in, rather than hard-coding one set here, is
    what keeps that real behavioural difference intact."""
    skip = skip_dir_names if isinstance(skip_dir_names, (set, frozenset)) else set(skip_dir_names)
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
        dirnames[:] = [
            d for d in dirnames
            if d not in skip
            and not Path(dirpath, d, ".git").is_file()
        ]
        for name in filenames:
            p = Path(dirpath) / name
            if p.is_file():  # excludes broken symlinks, matching the old rglob filter
                yield p
