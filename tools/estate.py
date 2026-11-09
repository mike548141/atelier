#!/usr/bin/env python3
"""estate — where a repo's main checkout is, and where its neighbours live.

Not a check. The one answer to "a `../<sibling>` reference, from here: where
does it land?", shared by `pathscan`, `linkscan`, `pins` and `floorfleet`
(`320/180`, `320/660`). Importable alone; stdlib plus `filewalk` only.

TWO THINGS BROKE THE SIBLING CONVENTION, AND THEY ARE ONE ROOT CAUSE. Both
come from reading the path a checkout happens to sit at as if it named the
estate:

  * A linked worktree sits somewhere else on disk, so `../<sibling>` from one
    climbs into the worktrees folder. The same scanner over byte-identical
    files reported a clean main checkout and a red worktree (`320/180`), in
    the mode the concurrency doctrine prescribes for write-heavy work.
    `main_checkout` finds the main checkout through `git rev-parse
    --git-common-dir`, which names it from any worktree.
  * A repo moved into a group folder is no longer a direct sibling of the
    repos it names (`320/660`). One setting names the folder that holds them.

THE SETTING. `ATELIER_ESTATE_ROOT` in the environment, or else the git config
`hooks.atelierEstateRoot`: the folder that holds the repos and the group
folders. It is the same two-carrier shape, in the same order, as
`ATELIER_TOOLS` / `hooks.atelierTools`, and for the same reason: an environment
variable set in a shell does not reach a hook started by an editor, while a
`git config --global` line reaches every repo. Unset means "repos are direct
siblings", and nothing changes for anyone who has not set it. A value that is
not an absolute directory is reported once on stderr and ignored, so a typo
costs a warning and the old behaviour rather than a wrong answer.

WHAT A LANDING IS. `landings(root, target)` takes a path that leaves the repo
and returns where it could really be, which only ever adds places to look. It
is lexical plus one directory listing; a caller decides what existence means.
`pathscan` takes it as "resolves". `linkscan` takes it as "exists, and is
outside the repo root", which is what the same link already reports from a
main checkout.

COST. A scan with no `..` token that fails to resolve never runs git. A scan
with one runs it once per root, whatever the number of tokens.

STATED RESIDUAL. Existence only: with two repos of one name in two group
folders, a reference resolves if either carries the file. A host with no
parent checkout at all (a cloud session on a fresh clone) has nothing to land
on; this helper cannot help there and the reference stays a finding.
"""

import os
import subprocess
import sys
from pathlib import Path, PurePath

sys.path.insert(0, str(Path(__file__).resolve().parent))
import filewalk  # noqa: E402

ENV_VAR = "ATELIER_ESTATE_ROOT"
GIT_CONFIG_KEY = "hooks.atelierEstateRoot"


def _git(repo: Path, *args: str) -> "str | None":
    """One git read in `repo`, or None if git cannot answer. Uses the file
    walk's scrubbed environment: a hook exports GIT_DIR, and the answer must
    depend on the directory asked about, not on whatever invoked the tool."""
    try:
        out = subprocess.run(
            ["git", *filewalk._GIT_SAFE, "-C", str(repo), *args],
            capture_output=True, text=True, check=False,
            env=filewalk._git_env())
    except (OSError, ValueError):
        return None
    return out.stdout if out.returncode == 0 else None


def _checkout_of(base: Path, common_dir: str) -> "Path | None":
    """The checkout holding `common_dir`, as git printed it from `base`. Only a
    directory literally named `.git` sits inside a checkout: a submodule's
    common dir is `<super>/.git/modules/<name>` and a bare repo's is the repo
    itself, so neither has a main checkout at `.parent`. None for those."""
    common = Path(common_dir)
    if not common.is_absolute():
        common = base / common
    common = common.resolve()
    return common.parent if common.name == ".git" else None


def main_checkout(repo: Path) -> Path:
    """The main checkout behind `repo`, which IS `repo` unless it is a linked
    worktree. Falls back to `repo` whenever git cannot answer: a non-repo
    directory, or no git on PATH."""
    out = _git(repo, "rev-parse", "--git-common-dir")
    if out is None or not out.strip():
        return repo
    return _checkout_of(repo, out.strip()) or repo


_WARNED: set[str] = set()


def _validated(value: str, source: str) -> "Path | None":
    path = Path(value).expanduser()
    if path.is_absolute() and path.is_dir():
        return path
    if value not in _WARNED:
        _WARNED.add(value)
        print(f"estate: warning — {source} is {value!r}, not an absolute "
              "directory; ignoring it and treating repos as direct siblings",
              file=sys.stderr)
    return None


def root_setting(repo: "Path | None" = None) -> "Path | None":
    """The configured estate root, or None when the layout is the default one
    of direct siblings. The environment wins, then the git config as seen from
    `repo`. An empty value is unset."""
    value = os.environ.get(ENV_VAR)
    if value:
        return _validated(value, f"${ENV_VAR}")
    out = _git(repo if repo is not None else Path.cwd(),
               "config", "--get", GIT_CONFIG_KEY)
    if out and out.strip():
        return _validated(out.strip(), f"git config {GIT_CONFIG_KEY}")
    return None


def parent(repo: Path) -> Path:
    """The folder to look in for `repo`'s neighbours, from any worktree: the
    setting when there is one, else the folder holding the main checkout."""
    configured = root_setting(repo)
    return configured if configured is not None else main_checkout(repo).parent


def _lexical(path) -> str:
    return os.path.normpath(os.path.abspath(str(path)))


class _View:
    """One scan root's answers, worked out once."""

    def __init__(self, root: Path):
        root_text = _lexical(root)
        self.top = root_text
        self.main: "str | None" = None
        out = _git(root, "rev-parse", "--git-common-dir", "--show-prefix")
        if out is not None and out.strip():
            lines = out.split("\n")
            prefix_parts = PurePath(lines[1]).parts if len(lines) > 1 else ()
            # --show-prefix is lexical, and so is the climb: a scan root that
            # is a subfolder of its repo still measures from the repo's top.
            top = Path(root_text)
            for _ in prefix_parts:
                top = top.parent
            self.top = str(top)
            main = _checkout_of(Path(root_text), lines[0].strip())
            if main is not None and (os.path.realpath(main)
                                     != os.path.realpath(self.top)):
                self.main = str(main)
        self.estate_root = root_setting(root)
        self._folders: "list[Path] | None" = None

    def repo_parents(self) -> "list[Path]":
        """The estate root and each group folder under it: a directory that
        is not hidden, not a symlink, and is not itself a repo."""
        if self._folders is None:
            assert self.estate_root is not None
            folders = [self.estate_root]
            try:
                entries = sorted(self.estate_root.iterdir())
            except OSError:
                entries = []
            for entry in entries:
                try:
                    if (entry.name.startswith(".") or entry.is_symlink()
                            or not entry.is_dir()
                            or (entry / ".git").exists()):
                        continue
                except OSError:
                    continue
                folders.append(entry)
            self._folders = folders
        return self._folders

    def landings(self, target) -> "list[Path]":
        rel = os.path.relpath(_lexical(target), self.top)
        parts = PurePath(rel).parts
        if not parts or parts[0] != "..":
            return []
        out: list[Path] = []
        if self.main is not None:
            out.append(Path(os.path.normpath(os.path.join(self.main, rel))))
        ups = 0
        while ups < len(parts) and parts[ups] == "..":
            ups += 1
        # Only a single climb names a sibling. Two or more climbs were written
        # against a real depth, and the physical path answers those.
        if self.estate_root is not None and ups == 1 and len(parts) > 1:
            for folder in self.repo_parents():
                out.append(folder.joinpath(*parts[1:]))
        return out


_VIEWS: "dict[tuple[str, str | None], _View]" = {}


def landings(root: Path, target) -> "list[Path]":
    """Where `target`, a path that leaves the repo holding `root`, could really
    be: the same path read from the main checkout when `root` is in a linked
    worktree, and under each repo-holding folder when the setting names one.
    Empty when `target` stays inside the repo, or nothing is configured and
    `root` is not a worktree. The view is built once per root and setting."""
    key = (_lexical(root), os.environ.get(ENV_VAR))
    view = _VIEWS.get(key)
    if view is None:
        view = _VIEWS[key] = _View(root)
    return view.landings(target)


def forget() -> None:
    """Drop the per-root views, for a test that changes the layout under one."""
    _VIEWS.clear()
