#!/usr/bin/env python3
"""stashscan -- warn when the shared git stash stack holds an entry older than today.

    stashscan.py [--repo DIR] [--now ISO] [-v]   the check: exit 0 none older
                          than today, 1 residue found, 2 could not check
    stashscan.py --hook   Claude Code SessionStart hook: reads the hook JSON on
                          stdin, prints one JSON object when there is residue,
                          else nothing. Never blocks; always exits 0.
    stashscan.py --selftest   prove it fires, stays quiet, and never mutates

Why (board 450/010 row 7, first built in an estate child repo): `refs/stash`
lives in the COMMON git dir, so the primary checkout and every linked worktree,
and so every parallel session, share one stack. A bare `git stash pop` in any of
them pops `stash@{0}`, whoever made it. CONCURRENCY.md § Integration hygiene
says how an entry gets there (a `--autostash` whose re-apply conflicts; git
says "Your changes are safe in the stash" and the rebase exits 0) and the
recovery sweep's table asks for "none unexpected"; this is that row as a
mechanism. In the child two entries sat for three weeks from two sessions;
popped, one would have restored a weeks-old file over the current one.

"Older than today" is the machine's LOCAL calendar day: the stack is never
pushed and its only reader is whoever sits at this checkout, so the question is
about their day. `datetime.fromtimestamp` and `date.today` both honour `TZ`,
which is what makes the boundary testable. The age read is the stash commit's
committer date (`%ct`), when the work was set aside.

IT WARNS AND NEVER MUTATES. An entry is another session's uncommitted work, and
dropping it is not a delivering session's call. The only git commands run are
`rev-parse` and `stash list`. Not a floor check either: on CI a fresh clone's
stack is empty by construction (it could never fire), and on the commit hook a
peer's live stash would block or nag every commit for work that is not the
committer's. Its place is session open (the hook) and a sweep (the CLI).

Not seen: a rebase STOPPED by a conflict holds its autostash in
`.git/rebase-merge/autostash`, not `refs/stash`, until the rebase ends.

Wiring, user-level `~/.claude/settings.json`:

    "hooks": {"SessionStart": [{"matcher": "startup|resume", "hooks": [
        {"type": "command", "command": "python3 <atelier>/tools/stashscan.py --hook",
         "timeout": 10}]}]}

Tests: tools/test_stashscan.py.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

TAG = "stashscan"
GIT_TIMEOUT_S = 10
# NUL-separated: a stash subject is free text and has held every printable
# separator. `%gt` is not a valid placeholder, and the work's age is wanted
# anyway, not the reflog entry's.
STASH_FORMAT = "%gd%x00%ct%x00%H%x00%gs"


class CannotCheck(RuntimeError):
    """The stack could not be read: exit 2, never a silent pass."""


def _git(repo, *args) -> str:
    try:
        r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                           text=True, timeout=GIT_TIMEOUT_S)
    except FileNotFoundError as e:
        raise CannotCheck("git is not installed") from e
    except (OSError, subprocess.SubprocessError) as e:
        raise CannotCheck(f"git {' '.join(args)} could not run: {e}") from e
    if r.returncode != 0:
        tail = (r.stderr or "").strip().splitlines()
        raise CannotCheck(f"git {' '.join(args)}: "
                          f"{tail[-1] if tail else 'exit %d' % r.returncode}")
    return r.stdout


def stack_home(repo) -> str:
    """Where `refs/stash` lives: the common git dir, the same for every worktree."""
    out = _git(repo, "rev-parse", "--git-common-dir").strip()
    if not out:
        raise CannotCheck("git could not name the common git dir")
    p = Path(out)
    return str(p if p.is_absolute() else (Path(repo) / p).resolve())


def read_stack(repo) -> list[dict]:
    """Every entry, newest first, as git lists it. An empty stack is []."""
    entries = []
    for row in _git(repo, "stash", "list", f"--format={STASH_FORMAT}").splitlines():
        if not row.strip():
            continue
        parts = row.split("\0")
        if len(parts) < 4:
            raise CannotCheck(f"unparseable stash row from git: {row!r}")
        selector, ct, sha, subject = parts[0], parts[1], parts[2], "\0".join(parts[3:])
        try:
            when = datetime.fromtimestamp(int(ct))
        except (ValueError, OSError, OverflowError) as e:
            raise CannotCheck(f"stash {selector} has an unreadable date {ct!r}") from e
        entries.append({"selector": selector, "when": when, "sha": sha,
                        "subject": subject,
                        "autostash": "autostash" in subject.lower()})
    return entries


def resolve_today(raw: str | None) -> date:
    if raw is None:
        return date.today()
    try:
        parsed = datetime.fromisoformat(raw)
    except ValueError as e:
        raise CannotCheck(f"--now {raw!r} is not ISO 8601") from e
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone()        # compare local day with local day
    return parsed.date()


def stale(entries: list[dict], today: date) -> list[dict]:
    return [e for e in entries if e["when"].date() < today]


def describe(e: dict, today: date) -> str:
    delta = (e["when"].date() - today).days
    age = "today" if delta == 0 else (f"{-delta}d old" if delta < 0
                                      else f"dated {delta}d ahead")
    mark = "  <- autostash (nobody types these)" if e["autostash"] else ""
    return (f"  {e['selector']:<12} {e['when']:%Y-%m-%d %H:%M}  {age:<14} "
            f"{e['sha'][:8]}  {e['subject']}{mark}")


def _plural(n: int) -> str:
    return f"{n} entr{'y' if n == 1 else 'ies'}"


def check(repo, today: date, verbose: bool) -> int:
    try:
        home = stack_home(repo)
        entries = read_stack(repo)
    except CannotCheck as e:
        print(f"{TAG}: cannot check the stash stack: {e}", file=sys.stderr)
        return 2
    old = stale(entries, today)
    if not old:
        # The count is in the clean verdict: an empty stack and three same-day
        # entries are different facts, and "checked" must not read as "skipped".
        print(f"✓ {TAG}: {_plural(len(entries))} on the shared stash stack, none "
              f"older than {today:%Y-%m-%d} (local). Stack: {home}")
        if verbose:
            for e in entries:
                print(describe(e, today))
        _tree(repo)
        return 0
    print(f"⚠ {TAG}: {len(old)} of {_plural(len(entries))} on the shared stash "
          f"stack {'is' if len(old) == 1 else 'are'} older than "
          f"{today:%Y-%m-%d} (local). Stack: {home}")
    for e in entries:
        print(describe(e, today))
    print("  Every worktree of this repository shares this stack, so an entry\n"
          "  may be another session's uncommitted work: ask whose it is, never\n"
          "  clear it as yours. Look without touching: git stash show -p stash@{N}.\n"
          "  Never a bare `git stash pop` or `apply`: they reach stash@{0},\n"
          "  whoever made it.")
    _tree(repo)
    return 1


def _tree(repo) -> None:
    here = str(Path(__file__).resolve().parent)
    if here not in sys.path:        # `python3 -I` leaves the script dir off
        sys.path.insert(0, here)
    import treeline
    text = treeline.line(Path(repo).resolve())
    if text:
        print(text)


def hook_output(cwd) -> dict | None:
    """The SessionStart JSON for `cwd`, or None when there is nothing to say.

    Not a checkout: nothing (not this hook's business). A git failure inside a
    checkout: a 'no result' line to the model, never silence that reads as clean."""
    try:
        _git(cwd, "rev-parse", "--git-dir")
    except CannotCheck:
        return None
    try:
        home = stack_home(cwd)
        entries = read_stack(cwd)
    except CannotCheck as e:
        return {"hookSpecificOutput": {"hookEventName": "SessionStart",
                "additionalContext": f"{TAG}: no result: {e}. The shared stash "
                                     f"stack was NOT checked."}}
    today = date.today()
    old = stale(entries, today)
    if not old:
        return None
    rows = "; ".join(f"{e['selector']} {(today - e['when'].date()).days}d old"
                     f"{' autostash' if e['autostash'] else ''} '{e['subject'][:60]}'"
                     for e in old)
    head = (f"{len(old)} stash entr{'y' if len(old) == 1 else 'ies'} older than "
            f"today on the stack every worktree of this repo shares")
    ctx = (f"{TAG}: {head} ({home}): {rows}. An entry may be another session's "
           f"uncommitted work: do not pop, apply, drop or clear it, and never run a "
           f"bare `git stash pop`. Look with `git stash show -p stash@{{N}}` and "
           f"mention it to the principal once; atelier CONCURRENCY.md § Integration "
           f"hygiene.")
    return {"hookSpecificOutput": {"hookEventName": "SessionStart",
                                   "additionalContext": ctx},
            "systemMessage": f"⚠️ {TAG}: {head}."}


def run_hook() -> int:
    try:
        try:
            data = json.load(sys.stdin)
        except Exception:
            data = {}
        cwd = (data.get("cwd") if isinstance(data, dict) else None) or os.getcwd()
        out = hook_output(cwd)
        if out is not None:
            print(json.dumps(out, ensure_ascii=False))
    except BaseException:       # a hook error helps nobody; say nothing
        pass
    return 0


def _selftest() -> int:
    """Throwaway repos only; never this repo's stack."""
    import tempfile
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(GIT_CONFIG_NOSYSTEM="1", ATELIER_NO_TREE_LINE="1")
    ident = ["-c", "user.name=T", "-c", "user.email=t" + chr(64) + "example.invalid",
             "-c", "commit.gpgsign=false"]
    fails = []

    def git(repo, *args, when=None):
        e = dict(env)
        if when:
            e.update(GIT_AUTHOR_DATE=when, GIT_COMMITTER_DATE=when)
        subprocess.run(["git", *ident, "-C", str(repo), *args], check=True,
                       capture_output=True, env=e)

    def me(repo, *extra):
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "--repo", str(repo), "--now", "2026-09-21T09:00", *extra],
                           capture_output=True, text=True, env=env)
        return r.returncode, r.stdout + r.stderr

    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "r"
        repo.mkdir()
        git(repo, "init", "-q", "-b", "main")
        (repo / "f").write_text("base\n")
        git(repo, "add", "f")
        git(repo, "commit", "-qm", "base")
        rc, out = me(repo)
        if not (rc == 0 and "0 entries" in out):
            fails.append(f"empty stack not quiet: {rc} {out}")
        (repo / "f").write_text("set aside\n")
        git(repo, "stash", "push", "-q", "-m", "old work", when="2026-08-17T19:57:00")
        wt = Path(tmp) / "wt"
        git(repo, "worktree", "add", "-q", "-b", "wt", str(wt))
        before = subprocess.run(["git", "-C", str(repo), "stash", "list"],
                                capture_output=True, text=True, env=env).stdout
        rc, out = me(wt)
        if not (rc == 1 and "35d old" in out and "old work" in out):
            fails.append(f"old entry seen from a worktree did not fire: {rc} {out}")
        after = subprocess.run(["git", "-C", str(repo), "stash", "list"],
                               capture_output=True, text=True, env=env).stdout
        if before != after or not before:
            fails.append("a firing run changed the stack")
        rc, out = me(Path(tmp) / "absent")
        if rc != 2:
            fails.append(f"a missing dir did not exit 2: {rc}")
    if fails:
        for f in fails:
            print(f"✗ {TAG} selftest: {f}", file=sys.stderr)
        return 1
    print(f"selftest OK — {TAG}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Warn when the shared stash stack holds an entry older than today.",
        epilog="Read-only. Exit 0 none older than today; 1 residue found; "
               "2 could not check.")
    ap.add_argument("--repo", default=".",
                    help="the checkout whose stack to read (default: cwd); every "
                         "worktree of a repository reads the same stack")
    ap.add_argument("--now", help="freeze 'today' at this ISO 8601 local time")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="list every entry even when none is old")
    ap.add_argument("--hook", action="store_true",
                    help="run as a Claude Code SessionStart hook")
    ap.add_argument("--selftest", action="store_true", help="prove the logic offline")
    args = ap.parse_args(argv)
    if args.selftest:
        return _selftest()
    if args.hook:
        return run_hook()
    try:
        today = resolve_today(args.now)
    except CannotCheck as e:
        print(f"{TAG}: {e}", file=sys.stderr)
        return 2
    return check(args.repo, today, args.verbose)


if __name__ == "__main__":
    sys.exit(main())
