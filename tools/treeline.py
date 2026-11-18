#!/usr/bin/env python3
"""treeline -- the second, indented line a check prints naming the tree it read.

    python3 tools/treeline.py [DIR]     print DIR's line (default: this checkout)

Why (board 450/010 row 9, first built in an estate child repo): a session's
shell cwd drifted out of its worktree through one compound command holding a
`cd`. Its edits used absolute paths and were safe; its verification ran against
a tree without the change, and every check came back green and meaningless. It
surfaced only because a passing run reported fewer assertions than the agent
had just written. Nobody interrogates a green run, so the identity of the tree
has to sit in the output everyone already reads. The coverage line says how much
a check looked at (GUARDS.md); this says where.

The shape, two spaces in like the `coverage:` line it sits beside:

    tree /work/demo · main@1a2b3c4 · worktree · tools in-tree

  <branch>@<sha>         or `detached@<sha>` (an empty branch name reads as an
                         ordinary run), or `no commits yet`
  worktree               a linked worktree, where parallel sessions work
  REBASE IN PROGRESS     the commonest way to be detached by accident
  not a git checkout     said out loud: an absent identity reads as a clean one
  ⚠ not the git root: X  the tree read is not where git says the tree starts
  tools in-tree | tools <dir> · <branch>@<sha>
                         which checkout's scanners ran; a child runs atelier's,
                         and a worktree can run the primary's

THE ROOT IS THE ONE THE CHECK READ, never `os.getcwd()` behind the caller's
back. A caller passes the resolved root it actually scanned; a helper that
re-derived it from the cwd would print the right answer in every ordinary run
and the wrong one in exactly the drifted case it exists to catch.

It never raises and never gates: a lookup that fails degrades to a plainer line.
`ATELIER_NO_TREE_LINE=1` suppresses it (`line()` then returns None). Stdlib
only. Node instruments have no twin yet: none of them is a check with a verdict
a wrong tree would falsify; the first that is gets one in the same shape.

Tests: tools/test_treeline.py.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ENV_OFF = "ATELIER_NO_TREE_LINE"
GIT_TIMEOUT_S = 2      # a wedged index must not hold a verdict hostage


def _git(root, *args):
    """Stripped stdout of a read-only git call in `root`, or None."""
    try:
        r = subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                           text=True, timeout=GIT_TIMEOUT_S)
    except (OSError, subprocess.SubprocessError, ValueError):
        return None
    return r.stdout.strip() if r.returncode == 0 else None


def _real(p) -> str:
    try:
        return os.path.realpath(str(p))
    except (OSError, ValueError):
        return str(p)


def _head(root) -> str:
    branch = (_git(root, "rev-parse", "--abbrev-ref", "HEAD") or "").split("\n")[0]
    sha = (_git(root, "rev-parse", "--short", "HEAD") or "").split("\n")[0]
    if not branch and not sha:
        return "no commits yet"
    if branch in ("", "HEAD"):
        return f"detached@{sha}" if sha else "detached"
    return f"{branch}@{sha}" if sha else branch


def identity(root) -> list[str]:
    """The git parts of the line for `root`. Never raises."""
    paths = _git(root, "rev-parse", "--show-toplevel", "--absolute-git-dir",
                 "--git-common-dir")
    if not paths:
        return ["not a git checkout"]
    rows = paths.split("\n") + ["", "", ""]
    top, git_dir, common = rows[0], rows[1], rows[2]
    if common and not os.path.isabs(common):      # relative to the -C dir
        common = os.path.join(str(root), common)
    parts = [_head(root)]
    if git_dir and common and _real(git_dir) != _real(common):
        parts.append("worktree")
    if git_dir and any(os.path.exists(os.path.join(git_dir, m))
                       for m in ("rebase-merge", "rebase-apply")):
        parts.append("REBASE IN PROGRESS")
    if top and _real(top) != _real(root):
        parts.append(f"⚠ not the git root: {top}")
    return parts


def line(root, tools=None) -> str | None:
    """The tree line for the tree a check read, or None when switched off.

    `root` is the resolved root the check scanned. `tools`, when given, is the
    directory whose scanners ran: named in-tree when it sits inside `root`,
    else by path and its own branch@sha."""
    if os.environ.get(ENV_OFF):
        return None
    root = Path(root)
    parts = [f"tree {root}", *identity(root)]
    if tools is not None:
        t = _real(tools)
        r = _real(root)
        if t == r or t.startswith(r.rstrip(os.sep) + os.sep):
            parts.append("tools in-tree")
        else:
            tool_id = identity(Path(tools))
            parts.append(f"tools {tools}")
            if tool_id and tool_id[0] != "not a git checkout":
                parts.append(tool_id[0])
    return "  " + " · ".join(parts)


def main(argv: list[str]) -> int:
    root = Path(argv[0]).resolve() if argv else Path(__file__).resolve().parent.parent
    text = line(root)
    if text:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
