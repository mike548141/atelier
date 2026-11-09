#!/usr/bin/env python3
"""sweepscan — where sibling worktrees exist, a commit names its files.

WHY (board `320/060`, the fourth slice of `320/810`; the principal, 2026-11-09:
"all six, warnings at first and then move to blocking action"). A session
staged into a shared index in the window between another session's reading of
that index and its commit, so a commit carried paths its author never chose.
The filer's own floor printed the correct count on screen: a correct number
among a hundred lines stopped nothing. Printing more was shown to be the wrong
fix, so this check names the act.

THE SIGNAL. Git hands the hook the index the commit is about to write, and the
name of that file says which form of commit is running (measured on git 2.x):

    git add x; git commit        GIT_INDEX_FILE ends `.git/index`
    git commit -a, -i            GIT_INDEX_FILE ends `index.lock`
    git commit -- paths, --only  GIT_INDEX_FILE ends `next-index-<pid>.lock`

So only `next-index-` is a commit that names its files, and it is the only
form whose carried set is exactly what the commit named. The check is free: no
output is parsed, no message needed.

THE MARKER. "The whole index is meant" is `ATELIER_WHOLE_INDEX=1` in the
commit's environment. An environment variable and not a message trailer, for a
measured reason: git runs `pre-commit` BEFORE it writes the message (at that
moment the message file still holds the previous commit's text), so no trailer
can reach this plane. Any non-empty value counts: the marker has no reason to
carry, because nothing records it. A session that exports it for good has
turned the check off for itself, and this scanner cannot tell.

WHAT IS IN SCOPE. A repo with more than one live worktree (`git worktree list`;
bare and prunable entries do not count, so a removed worktree stops charging).
A merge, cherry-pick, revert or rebase is replaying commits already written, so
it is exempt; `pre-merge-commit` hands over to this same hook.

WHAT IT DOES NOT DO. It does not make an index safe: a commit that names files
it did not write still carries them (`CONCURRENCY.md`'s precondition stays
true). It cannot stop a deliberate foreign path-scope, only the accidental
sweep. `git worktree list` is a proxy for concurrency: a stale worktree still
charges the tax, and two sessions in one checkout with no worktree slip through.

NO DATE, AND WHY: THE MEASUREMENT (`320/060`). A commit's form is not in git
history, so the measure is the session transcripts' `git commit` command lines,
counts only: 88% of 2,510 in atelier and 97% of 3,530 in one child took the
whole index, 46% and 79% this month. A check that fires on most commits is
noise, not a gate, so this one is warn-only with no blocking date, on purpose,
and that is a finding for the principal, not a default.

Exit codes: 0 reported or clean (it has no blocking form) · 2 the scan itself is
broken (a broken scan is not a pass).

Stdlib-only, like every sibling.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report  # noqa: E402

NAME = "sweepscan"
MARKER_ENV = "ATELIER_WHOLE_INDEX"
NAMED_INDEX_PREFIX = "next-index-"
REPLAY_REFS = ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "REBASE_HEAD")


class ConfigError(RuntimeError):
    """Something the scan needs is unusable; fail closed."""


def _git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args],
                          capture_output=True, text=True, check=False)


def live_worktrees(root: Path) -> int:
    """How many worktrees could a commit race with. Bare and prunable entries
    do not count."""
    out = _git(root, "worktree", "list", "--porcelain")
    if out.returncode != 0:
        raise ConfigError(f"git worktree list failed: {out.stderr.strip()}")
    live = 0
    for block in out.stdout.strip().split("\n\n"):
        lines = block.splitlines()
        if not lines or not lines[0].startswith("worktree "):
            continue
        if any(ln == "bare" or ln.split(" ", 1)[0] == "prunable" for ln in lines):
            continue
        live += 1
    return live


def replaying(root: Path) -> bool:
    return any(_git(root, "rev-parse", "-q", "--verify", ref).returncode == 0
               for ref in REPLAY_REFS)


def staged_count(root: Path) -> int:
    out = _git(root, "diff", "--cached", "--name-only", "-z")
    if out.returncode != 0:
        raise ConfigError(f"git diff --cached failed: {out.stderr.strip()}")
    return len([p for p in out.stdout.split("\0") if p])


def judge(root: Path, env: dict[str, str]) -> tuple[bool, str]:
    """(is a finding, why). The env is passed in so tests need no real commit."""
    index_file = env.get("GIT_INDEX_FILE", "")
    if not index_file:
        return False, "no commit in progress"
    if Path(index_file).name.startswith(NAMED_INDEX_PREFIX):
        return False, "the commit names its files"
    live = live_worktrees(root)
    if live <= 1:
        return False, "one worktree"
    if env.get(MARKER_ENV):
        return False, f"{MARKER_ENV} is set: the whole index is declared"
    if replaying(root):
        return False, "replaying commits already written"
    return True, f"{live} worktrees"


def _main(argv: list[str] | None) -> int:
    ap = argparse.ArgumentParser(
        prog=NAME,
        description="Where sibling worktrees exist, a commit names its files "
                    "or declares the whole index.")
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the tool against its own fixtures, then exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return report.quiet_selftest(NAME, _selftest)
    root = Path(args.root).resolve()
    rc = report.refuse_missing_root(NAME, root, args.root)
    if rc is not None:
        return rc

    found, why = judge(root, dict(os.environ))
    staged = staged_count(root) if found else 0
    if args.json:
        print(json.dumps({"clean": True, "finding": found, "reason": why,
                          "staged_paths": staged}, indent=2))
    elif found:
        print(f"⚠ {NAME}: this commit takes the whole index ({staged} staged path(s), "
              f"{why}). Name your files, `git commit -- <paths>`, or set "
              f"{MARKER_ENV}=1 if the whole index is meant. Warn-only, no "
              "blocking date (board 320/060).")
    else:
        print(report.clean_head(NAME, f"{why}."))
    if not args.json:
        print(report.advisory_count_line(NAME, 1 if found else 0))
    return 0


def main(argv: list[str] | None = None) -> int:
    return report.guarded_main(NAME, _main, argv, (ConfigError,))


def _selftest() -> int:
    """Minimal smoke test over a real throwaway repo with a sibling worktree."""
    import tempfile

    fails: list[str] = []

    def check(name: str, got, want) -> None:
        if got != want:
            fails.append(f"{name}: got {got!r}, want {want!r}")

    with tempfile.TemporaryDirectory(prefix="sweepscan-selftest-") as tmp:
        repo = Path(tmp) / "r"
        repo.mkdir()
        for args in (["init", "-q"], ["config", "user.name", "t"],
                     ["config", "user.email", "t@example.invalid"],  # leakscan:allow: RFC-2606 fixture identity
                     ["config", "commit.gpgsign", "false"]):
            _git(repo, *args)
        (repo / "a").write_text("1\n", encoding="utf-8")
        _git(repo, "add", "a")
        _git(repo, "commit", "-q", "-m", "init")
        check("one worktree", judge(repo, {"GIT_INDEX_FILE": ".git/index"})[0], False)
        _git(repo, "worktree", "add", "-q", str(Path(tmp) / "w2"))
        check("two worktrees, plain commit",
              judge(repo, {"GIT_INDEX_FILE": ".git/index"})[0], True)
        check("-a is not a named commit",
              judge(repo, {"GIT_INDEX_FILE": "/r/.git/index.lock"})[0], True)
        check("path-scoped commit",
              judge(repo, {"GIT_INDEX_FILE": "/r/.git/next-index-99.lock"})[0], False)
        check("marker clears it",
              judge(repo, {"GIT_INDEX_FILE": ".git/index", MARKER_ENV: "1"})[0], False)
        check("no commit in progress", judge(repo, {})[0], False)
    for f in fails:
        print(f"{NAME} selftest FAIL: {f}", file=sys.stderr)
    print(f"{NAME} selftest: {'FAILED' if fails else 'ok'} ({len(fails)} failure(s))")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
