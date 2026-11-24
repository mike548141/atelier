#!/usr/bin/env python3
"""deadhook -- are this clone's commit hooks on, and is a dead hook there to mislead?

Board 450/010 row 8; first built in an estate child repo, homed here. Two jobs:

  tools/deadhook.py            the CHECK. Exits 1 while a floor hook
                               (pre-commit, pre-merge-commit, commit-msg) that is
                               not a `*.sample` sits in the clone's default hooks
                               directory while `core.hooksPath` points git
                               somewhere else, so git never runs it.
  tools/deadhook.py --status   "are hooks on?". Says which hooks directory git
                               runs, whether its pre-commit is there and
                               executable, whether the hook will find atelier's
                               scanners, and whether a dead hook is present.
                               Read-only; exits 1 if commits here would not be
                               scanned.

Why the status mode is separate: a check that runs inside the hook can never
report that the hook is off. If nothing arms the hook, nothing here runs. So
"are my commits being scanned?" needs a command a person, a session at open, or
a health sweep runs by hand.

Why a dead hook is a fault and not clutter: with `core.hooksPath` set, git never
runs `.git/hooks/pre-commit`, but a reader looking for "the hook" finds it
first. In the repo this was first built in, a stale copy listed three scanners
and disabled a rule the live hook enforced, and it led a subagent to a
confident, wrong audit. The legacy install (`cp tools/pre-commit.sample
.git/hooks/pre-commit`) leaves exactly this behind once a clone moves to a
tracked `.githooks/`. Git's own `*.sample` files are inert and expected, so they
are ignored. A non-floor hook left behind (a `post-checkout`, say) is named by
`--status` and fails nothing: it is dead too, but no reader mistakes it for the
commit gate.

Worktrees: hooks live in the common git directory every worktree shares
(`git rev-parse --git-common-dir`; in a worktree `.git` is a file), and repo
config is shared too, so a `core.hooksPath` set to an ABSOLUTE path points
every tree at one copy of the hook. A worktree that edits `.githooks/pre-commit`
is then not running its own edit. `--status` says when the armed hook is another
tree's copy and compares this tree's copy with it byte for byte. A differing
copy is a warning, not a failure: commits are still scanned (by the armed copy),
and the difference can as well be this branch behind a hook edit on main as
this branch editing the hook.

Exit codes (tools/README.md, the shared contract): 0 clean, 1 a dead floor hook
(check) or commits not scanned (`--status`), 2 not inside a git work tree.
`--warn` turns 1 into 0 for warn-only wiring. `-C DIR` runs against another
clone. Not wired into the floor: see tools/README.md § deadhook.

Tests: tools/test_deadhook.py.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

FLOOR_HOOKS = ("pre-commit", "pre-merge-commit", "commit-msg")
CWD = Path.cwd()


def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(CWD), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def repo_root() -> Path | None:
    top = git("rev-parse", "--show-toplevel")
    return Path(top) if top else None


def default_hooks_dir() -> Path:
    """`<common git dir>/hooks`: where git looks when `core.hooksPath` is unset."""
    common = Path(git("rev-parse", "--git-common-dir") or ".git")
    if not common.is_absolute():
        common = CWD / common
    return common / "hooks"


def hooks_path() -> str:
    # --type=path expands a leading `~`, as git itself does when it runs the hook.
    return git("config", "--type=path", "core.hooksPath")


def armed_dir(root: Path) -> Path:
    """The directory git runs hooks from. A relative `core.hooksPath` is relative
    to the work tree git runs the hook in; `/` keeps an absolute one absolute."""
    hp = hooks_path()
    return root / hp if hp else default_hooks_dir()


def same_dir(a: Path, b: Path) -> bool:
    try:
        return a.resolve() == b.resolve()
    except OSError:
        return False


def dead_hooks(root: Path) -> list[Path]:
    """Every hook file in the default directory while git runs another one."""
    if not hooks_path():
        return []
    default = default_hooks_dir()
    if same_dir(default, armed_dir(root)) or not default.is_dir():
        return []
    return sorted(p for p in default.iterdir()
                  if p.is_file() and not p.name.endswith(".sample"))


def check(root: Path) -> int:
    dead = [d for d in dead_hooks(root) if d.name in FLOOR_HOOKS]
    if not dead:
        print("✓ deadhook clean — no dead floor hook beside the live ones")
        return 0
    live = armed_dir(root)
    for d in dead:
        print(f"✗ deadhook: a DEAD {d.name} hook exists at {d}\n"
              f"  git runs {live / d.name} instead, so this file never runs, but it is "
              f"where a reader looks first and it does not say what the live hook checks.\n"
              f"  Remove it:  rm {d}", file=sys.stderr)
    return 1


def work_trees() -> list[Path]:
    """Every work tree of this repo, primary first, as real paths."""
    out = git("worktree", "list", "--porcelain")
    return [Path(line[len("worktree "):]).resolve()
            for line in out.splitlines() if line.startswith("worktree ")]


def owner_tree(hook: Path, trees: list[Path]) -> Path | None:
    """The work tree the armed hook lives in, or None if it is outside all of them.

    Only the directory is resolved (macOS `/tmp` is `/private/tmp`), never the
    hook file itself, so a symlinked hook is still judged by where it is armed.
    Longest match wins, so a tree nested inside another is not mistaken for it.
    """
    real = hook.parent.resolve() / hook.name
    inside = [t for t in trees if t == real or t in real.parents]
    return max(inside, key=lambda t: len(t.parts), default=None)


def show(path: Path, root: Path) -> str:
    """A path relative to this tree when it is under it, else as it is."""
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def worktree_lines(root: Path, hook: Path) -> tuple[list[str], bool]:
    """What to say when the armed hook might not be this tree's own copy.
    Returns (lines, warned); silent when the armed hook IS this tree's."""
    trees = work_trees()
    owner = owner_tree(hook, trees)
    if owner == root.resolve():
        return [], False
    if owner is None:
        rel = Path(".githooks") / "pre-commit"
        lines = [f"ℹ️  the armed hook ({hook}) is outside every work tree of this "
                 f"repo, not this tree's copy: commits here run that file."]
    else:
        rel = hook.parent.resolve().relative_to(owner) / hook.name
        whose = "the PRIMARY checkout's" if trees and owner == trees[0] else "another work tree's"
        lines = [f"ℹ️  the armed hook is {whose} copy ({hook}), not this tree's: one "
                 f"core.hooksPath is shared by every work tree, so commits here run that copy."]
    mine = root / rel
    if not mine.is_file():
        return lines + [f"⚠️ this tree has no {rel} to compare with the armed hook"], True
    if mine.read_bytes() == hook.read_bytes():
        return lines + [f"✅ this tree's {rel} is byte-identical to the armed hook"], False
    return lines + [
        f"⚠️ this tree's {rel} DIFFERS from the armed hook: an edit to it here is NOT "
        f"what runs when you commit here.\n"
        f"   See the difference:  diff {hook} {mine}\n"
        f"   (a relative `core.hooksPath = .githooks` would give each tree its own copy)"], True


def tools_dir(root: Path) -> tuple[str, str]:
    """(dir, where it came from), resolved as atelier's pre-commit hook does:
    ATELIER_TOOLS, then `git config hooks.atelierTools`, then in-repo tools/."""
    env = os.environ.get("ATELIER_TOOLS")
    if env:
        return env, "ATELIER_TOOLS"
    cfg = git("config", "--get", "hooks.atelierTools")
    if cfg:
        return cfg, "hooks.atelierTools"
    return str(root / "tools"), "in-repo tools/"


def status(root: Path) -> int:
    ok, warned = True, False
    hp = hooks_path()
    live = armed_dir(root)
    hook = live / "pre-commit"
    where = f"core.hooksPath = {hp}" if hp else f"core.hooksPath unset (git runs {live})"
    if hook.is_file() and os.access(hook, os.X_OK):
        print(f"✅ {where}  ({show(hook, root)} is executable)")
        if hp:
            lines, warned = worktree_lines(root, hook)
            for line in lines:
                print(line)
    else:
        ok = False
        print(f"❌ {where}, and no executable pre-commit there: commits here are NOT scanned.\n"
              f"   Fix: git config core.hooksPath .githooks   (or /atelier:repo hook)")
    if not hp and (root / ".githooks" / "pre-commit").is_file():
        print("ℹ️  this tree carries a tracked .githooks/ that git is not running; "
              "`git config core.hooksPath .githooks` arms it")
    for name in FLOOR_HOOKS[1:]:
        if not (live / name).is_file():
            warned = True
            print(f"⚠️ no {name} hook in {live}: the checks of that plane do not run here")
    tools, source = tools_dir(root)
    if (Path(tools) / "floor.py").is_file():
        print(f"✅ scanners at {tools}  (from {source}; floor.py found)")
    else:
        ok = False
        print(f"❌ scanners at {tools}  (from {source}): no floor.py, so the hook would "
              f"BLOCK every commit, failing closed.\n"
              f"   Fix: git config hooks.atelierTools <path to atelier>/tools")
    dead = dead_hooks(root)
    for d in dead:
        if d.name in FLOOR_HOOKS:
            ok = False
            print(f"❌ dead {d.name} hook at {d}: git never runs it; remove it")
        else:
            print(f"ℹ️  {d.name} at {d} never runs either (core.hooksPath points elsewhere)")
    if not any(d.name in FLOOR_HOOKS for d in dead):
        print("✅ no dead floor hook beside the live ones")
    if not ok:
        print("NOT all set — see ❌ above")
    elif warned:
        print("all set: commits here are scanned (but see ⚠️ above)")
    else:
        print("all set: commits here are scanned")
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    global CWD
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--status", action="store_true",
                    help="say whether this clone's hooks are on (read-only)")
    ap.add_argument("--warn", action="store_true",
                    help="report, but exit 0 where it would exit 1")
    ap.add_argument("-C", dest="dir", default=None, help="run against the clone at DIR")
    a = ap.parse_args(argv)
    if a.dir:
        CWD = Path(a.dir).resolve()
    root = repo_root()
    if root is None:
        print(f"deadhook: not inside a git work tree: {CWD}", file=sys.stderr)
        return 2
    rc = status(root) if a.status else check(root)
    return 0 if a.warn and rc == 1 else rc


if __name__ == "__main__":
    sys.exit(main())
