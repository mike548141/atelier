#!/usr/bin/env python3
"""worktree — one command for CONCURRENCY.md's "one worktree per line of work".

The doctrine (method/CONCURRENCY.md) says: never run parallel lines of work in a
single working tree — two sessions editing the same files race the git index and
stomp each other. Each independent line gets its own git worktree: own checkout,
own branch, off the same repo, living OUTSIDE iCloud so sync churn can't corrupt
an in-flight index. They reconcile on `main` via PR/merge.

Said once, that's easy to forget at 11pm. This is the machine that makes the
right thing the one-liner and the wrong thing hard:

  worktree start <feature>   fork a line   -> a checkout at ~/worktrees/<repo>-<feature>
  worktree list              hygiene view  -> which lines exist, which are stale/dirty
  worktree land [<feature>]  reconcile     -> push the branch + open a PR back to main
  worktree remove <feature>  clean up      -> git worktree remove, guarded against data loss

Every subcommand answers the same from any checkout in the repo — the main one or
any linked worktree. Repo identity comes from the main working tree (which `git
worktree list` always names first), never from the cwd, because the cwd when you
land a line of work is normally the worktree you were working in.

Mechanical guards that encode the doctrine (not left to memory):
  * REFUSES to create a worktree inside an iCloud-synced path (the #1 forgotten
    rule; iCloud + a live .git index = corruption).
  * Branches off the repo's integration branch (`main`) by default, so a line of
    work never silently inherits whatever half-done branch you happened to be on.
  * `list` flags worktrees that have diverged for days (merge hazard) or carry
    uncommitted changes (the concurrency equivalent of a leaked file handle).
  * `remove` refuses to delete a worktree with uncommitted or unmerged work
    unless you say --force — losing work is the failure mode this whole doctrine
    exists to prevent. "Merged" is measured against the *remote* integration
    branch (`origin/main`) as well as the local one, so work landed by a direct
    push counts as landed; if neither ref exists the branch is treated as
    unmerged and removal is refused. The check reads local refs only — no
    network — so `remove` stays fast and works offline; `--fetch` refreshes
    `origin/main` first when someone else may have merged the branch for you.

Exit codes (fail-safe — anything but success is non-zero):
  0  success / clean
  1  a guard tripped or an actionable problem (dirty/unmerged/stale)
  2  usage / environment error (not a git repo, iCloud refusal, git failed)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier runs it
with the system python3 and no install.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path

DEFAULT_BASE = "~/worktrees"

# A worktree that has diverged this long without landing is a merge hazard
# (CONCURRENCY "rebase/merge small and often"). Advisory — never blocks by itself.
DEFAULT_STALE_DAYS = 3

# Path fragments that mean "this lives in an iCloud-synced tree". A live .git
# index inside iCloud is the corruption trap the doctrine puts worktrees outside
# iCloud to avoid, so creating one there is refused, not warned.
ICLOUD_MARKERS = ("com~apple~clouddocs", "mobile documents", "library/cloudstorage")

# A feature slug becomes both a branch name and a directory name, so keep it to
# characters safe in both. Slashes would nest directories and complicate the
# <repo>-<feature> pairing; whitespace breaks paths.
FEATURE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


class GitError(RuntimeError):
    pass


def git(args: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(["git", *args], cwd=str(cwd) if cwd else None,
                          capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise GitError(f"git {' '.join(args)} failed: {proc.stderr.strip() or proc.stdout.strip()}")
    return proc


def toplevel(start: Path) -> Path:
    proc = git(["-C", str(start), "rev-parse", "--show-toplevel"])
    return Path(proc.stdout.strip())


def integration_branch(root: Path) -> str:
    """The branch everything reconciles onto. Prefer the remote's default HEAD,
    then a local main/master, then fall back to 'main' by name."""
    proc = git(["-C", str(root), "symbolic-ref", "--quiet", "refs/remotes/origin/HEAD"],
               check=False)
    if proc.returncode == 0 and proc.stdout.strip():
        return proc.stdout.strip().rsplit("/", 1)[-1]
    for cand in ("main", "master"):
        if git(["-C", str(root), "rev-parse", "--verify", "--quiet", cand],
               check=False).returncode == 0:
            return cand
    return "main"


def integration_refs(root: Path, main: str) -> list[str]:
    """Refs that count as "this work has landed", most authoritative first.

    A direct `git push <branch>:main` moves the remote integration branch and the
    local remote-tracking ref, but never local `main` — so a guard that only
    knows local `main` calls landed work unmerged, and teaches --force as the
    routine way past a safety check. The remote branch is the real integration
    point, so it is checked first. Local `main` still counts: a merge that has
    not been pushed yet has still landed.

    Returns short names, verified as real refs. Offline or in a fresh repo,
    whichever of the two exists is used. If NEITHER resolves the list is empty
    and the caller must treat the branch as unmerged — refusing to delete work
    it cannot verify, rather than assuming it is safe.
    """
    candidates = ((f"origin/{main}", f"refs/remotes/origin/{main}"),
                  (main, f"refs/heads/{main}"))
    return [short for short, full in candidates
            if git(["-C", str(root), "rev-parse", "--verify", "--quiet", full],
                   check=False).returncode == 0]


def is_merged(root: Path, rev: str, refs: list[str]) -> bool:
    """True if `rev` is contained in any of `refs`. Empty `refs` → False (fail safe).

    `merge-base --is-ancestor` exits 0 for "contained", 1 for "not", and >1 on
    error, so only an explicit 0 counts as merged.
    """
    for ref in refs:
        if git(["-C", str(root), "merge-base", "--is-ancestor", rev, ref],
               check=False).returncode == 0:
            return True
    return False


def has_remote(root: Path) -> bool:
    return bool(git(["-C", str(root), "remote"], check=False).stdout.strip())


def is_icloud(path: Path) -> bool:
    hay = str(path.expanduser()).lower()
    return any(m in hay for m in ICLOUD_MARKERS)


@dataclass
class WorktreeInfo:
    path: str
    branch: str          # branch name, or "(detached)"
    is_main: bool        # the primary working tree
    ahead: int           # commits on this branch not on the integration branch
    behind: int          # commits on the integration branch not here
    dirty: bool          # uncommitted changes present
    age_days: float      # days since the last commit on this branch
    stale: bool          # diverged past the stale threshold with unlanded work


def _now() -> float:
    return time.time()


def parse_worktrees(root: Path) -> list[dict]:
    """`git worktree list --porcelain` → a list of {path, head, branch?, detached?}.

    Order is git's: the main working tree first, then the linked worktrees. Each
    entry's `branch` is that worktree's own branch, whatever cwd we ran from.
    """
    out = git(["-C", str(root), "worktree", "list", "--porcelain"]).stdout
    entries: list[dict] = []
    cur: dict = {}
    for line in out.splitlines():
        if not line:
            if cur:
                entries.append(cur)
                cur = {}
            continue
        if line.startswith("worktree "):
            cur = {"path": line[len("worktree "):]}
        elif line.startswith("HEAD "):
            cur["head"] = line[len("HEAD "):]
        elif line.startswith("branch "):
            cur["branch"] = line[len("branch "):].rsplit("/", 1)[-1]
        elif line == "detached":
            cur["detached"] = True
    if cur:
        entries.append(cur)
    return entries


def main_worktree(root: Path) -> Path:
    """The repo's primary working tree, from any checkout inside it.

    `rev-parse --show-toplevel` answers "which checkout am I standing in", which
    is the *linked* worktree whenever a session is inside one — so it must never
    stand in for "the repo". Using it that way made `list` label the current
    worktree as main (and hide its ahead/behind counts), and made `land`/`remove`
    build the <repo>-<feature> directory name out of the linked worktree's own
    name, so they found no worktree at all. `git worktree list` always names the
    main working tree first, and says the same thing from every cwd.
    """
    entries = parse_worktrees(root)
    return Path(entries[0]["path"]) if entries else root


def collect(root: Path, main: str, stale_days: float) -> list[WorktreeInfo]:
    entries = parse_worktrees(root)
    main_root = entries[0]["path"] if entries else str(root)
    infos: list[WorktreeInfo] = []
    for e in entries:
        wt = Path(e["path"])
        is_main = str(wt) == main_root
        # Per-worktree branch, from that worktree's own porcelain entry — not
        # from HEAD in the cwd.
        branch = e.get("branch") or "(detached)"
        ahead = behind = 0
        if branch != "(detached)" and branch != main:
            rl = git(["-C", str(wt), "rev-list", "--left-right", "--count",
                      f"{main}...{branch}"], check=False)
            if rl.returncode == 0 and rl.stdout.strip():
                b, a = rl.stdout.split()
                behind, ahead = int(b), int(a)
        dirty = bool(git(["-C", str(wt), "status", "--porcelain"], check=False).stdout.strip())
        age_days = 0.0
        ct = git(["-C", str(wt), "log", "-1", "--format=%ct"], check=False)
        if ct.returncode == 0 and ct.stdout.strip():
            age_days = (_now() - int(ct.stdout.strip())) / 86400.0
        stale = (not is_main) and age_days > stale_days and (ahead > 0 or dirty)
        infos.append(WorktreeInfo(str(wt), branch, is_main, ahead, behind,
                                  dirty, round(age_days, 1), stale))
    return infos


# --------------------------------------------------------------------------- #
# commands
# --------------------------------------------------------------------------- #

def cmd_start(args) -> int:
    try:
        root = toplevel(Path.cwd())
    except GitError as e:
        print(f"worktree: {e}", file=sys.stderr)
        return 2
    if not FEATURE_RE.match(args.feature):
        print(f"worktree: bad feature name {args.feature!r} — use letters, digits, "
              "'.', '_', '-' (no spaces or slashes).", file=sys.stderr)
        return 2

    base = Path(args.base).expanduser()
    if is_icloud(base):
        print(f"worktree: refusing to create a worktree inside an iCloud path\n"
              f"  {base}\n"
              "  A live .git index in iCloud corrupts under sync. Pick a base "
              "outside iCloud (default ~/worktrees).", file=sys.stderr)
        return 2

    # The repo's own name, not the name of whichever worktree we're standing in —
    # otherwise starting a line from inside a worktree yields <repo>-<old>-<new>,
    # which land/remove can then never resolve.
    repo = main_worktree(root).name
    path = base / f"{repo}-{args.feature}"
    branch = args.branch or args.feature
    if path.exists():
        print(f"worktree: {path} already exists — pick another feature name or "
              "remove it first.", file=sys.stderr)
        return 1

    start_point = args.start or integration_branch(root)
    base.mkdir(parents=True, exist_ok=True)
    try:
        git(["-C", str(root), "worktree", "add", str(path), "-b", branch, start_point])
    except GitError as e:
        print(f"worktree: {e}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({"path": str(path), "branch": branch,
                          "start_point": start_point}, indent=2))
    else:
        print(f"✓ worktree ready: {path}")
        print(f"  branch {branch}  (off {start_point})")
        print(f"  cd {_shquote(str(path))}")
        print(f"  when it lands:  worktree land {args.feature}   # push + PR back to "
              f"{integration_branch(root)}")
    return 0


def cmd_list(args) -> int:
    try:
        root = toplevel(Path.cwd())
    except GitError as e:
        print(f"worktree: {e}", file=sys.stderr)
        return 2
    main = integration_branch(root)
    infos = collect(root, main, args.stale_days)

    if args.json:
        print(json.dumps({"integration_branch": main,
                          "worktrees": [asdict(i) for i in infos]}, indent=2))
    else:
        print(render_list(infos, main))

    problems = any(i.stale or i.dirty for i in infos if not i.is_main)
    return 1 if (args.check and problems) else 0


def cmd_land(args) -> int:
    try:
        root = toplevel(Path.cwd())
    except GitError as e:
        print(f"worktree: {e}", file=sys.stderr)
        return 2
    main = integration_branch(root)

    if args.feature:
        target = _feature_worktree(root, args)
        if target is None:
            print(f"worktree: no worktree found for feature {args.feature!r}.",
                  file=sys.stderr)
            return 1
        wt = Path(target["path"])
    else:
        wt = root  # land the worktree we're standing in

    branch = git(["-C", str(wt), "rev-parse", "--abbrev-ref", "HEAD"]).stdout.strip()
    if branch == main:
        print(f"worktree: refusing to land {main} onto itself — run this from a "
              "feature worktree.", file=sys.stderr)
        return 1
    if git(["-C", str(wt), "status", "--porcelain"], check=False).stdout.strip():
        print(f"worktree: {wt} has uncommitted changes — commit them before landing.",
              file=sys.stderr)
        return 1

    if not has_remote(wt):
        print(f"⚠ no remote configured — reconcile locally instead:\n"
              f"    git -C {_shquote(str(main_worktree(root)))} merge {branch}\n"
              f"  then: worktree remove {branch.split('-')[-1]}")
        return 0

    try:
        git(["-C", str(wt), "push", "-u", "origin", branch])
    except GitError as e:
        print(f"worktree: push failed: {e}", file=sys.stderr)
        return 2

    if shutil.which("gh"):
        pr = subprocess.run(["gh", "pr", "create", "--fill", "--base", main,
                             "--head", branch], cwd=str(wt), capture_output=True, text=True)
        if pr.returncode == 0:
            print(f"✓ pushed {branch} and opened PR → {main}\n  {pr.stdout.strip()}")
        else:
            print(f"✓ pushed {branch}; open the PR manually "
                  f"(gh said: {pr.stderr.strip()})")
    else:
        print(f"✓ pushed {branch} → origin. Open a PR to {main} (gh not installed).")
    return 0


def cmd_remove(args) -> int:
    try:
        root = toplevel(Path.cwd())
    except GitError as e:
        print(f"worktree: {e}", file=sys.stderr)
        return 2
    main = integration_branch(root)
    target = _feature_worktree(root, args)
    if target is None:
        print(f"worktree: no worktree found for feature {args.feature!r}.",
              file=sys.stderr)
        return 1
    wt = Path(target["path"])

    dirty = bool(git(["-C", str(wt), "status", "--porcelain"], check=False).stdout.strip())
    # Read the branch off the worktree we matched. A detached worktree has no
    # branch to name, so its HEAD commit is what gets checked for containment —
    # never the string "HEAD", which would resolve in the wrong tree.
    branch = target.get("branch") or ""
    head = target.get("head") or git(["-C", str(wt), "rev-parse", "HEAD"]).stdout.strip()
    rev, label = ((branch, f"branch {branch}") if branch
                  else (head, f"detached HEAD {head[:9]}"))

    if args.fetch and has_remote(root):
        git(["-C", str(root), "fetch", "--quiet", "origin", main], check=False)
    refs = integration_refs(root, main)
    merged = is_merged(root, rev, refs)

    if (dirty or not merged) and not args.force:
        why = []
        if dirty:
            why.append("uncommitted changes")
        if not merged:
            why.append(f"{label} is not merged into {' or '.join(refs)}" if refs
                       else f"{label} cannot be verified as merged — neither "
                            f"origin/{main} nor local {main} exists")
        print(f"worktree: refusing to remove {wt} — {', and '.join(why)}.\n"
              "  Land it first (worktree land), or pass --force to discard the work.",
              file=sys.stderr)
        return 1

    try:
        git(["-C", str(root), "worktree", "remove", str(wt)]
            + (["--force"] if args.force else []))
    except GitError as e:
        print(f"worktree: {e}", file=sys.stderr)
        return 2
    deleted = False
    if args.delete_branch and branch:
        # `git branch -d` measures "merged" against local main itself, so it can
        # refuse a branch this command just cleared against origin/main. Say so
        # rather than claiming a deletion that did not happen.
        bd = git(["-C", str(root), "branch", "-D" if args.force else "-d", branch],
                 check=False)
        deleted = bd.returncode == 0
        if not deleted:
            print(f"⚠ kept branch {branch} — git refused to delete it: "
                  f"{(bd.stderr or bd.stdout).strip()}")
    print(f"✓ removed {wt}" + (f" and branch {branch}" if deleted else ""))
    return 0


# --------------------------------------------------------------------------- #
# helpers / rendering
# --------------------------------------------------------------------------- #

def _feature_worktree(root: Path, args) -> dict | None:
    """Find a worktree by feature slug: match a directory named <repo>-<feature>.

    <repo> is the *main* working tree's name, so the same slug resolves whether
    you run from the main checkout or from a linked worktree. Returns the
    porcelain entry (path, head, branch) so callers read the branch from the
    worktree they matched, not from their own HEAD.
    """
    entries = parse_worktrees(root)
    if not entries:
        return None
    suffix = f"{Path(entries[0]['path']).name}-{args.feature}"
    for e in entries:
        if Path(e["path"]).name == suffix:
            return e
    return None


def _shquote(s: str) -> str:
    return f'"{s}"' if " " in s else s


def render_list(infos: list[WorktreeInfo], main: str) -> str:
    lines = [f"worktrees (integration branch: {main})"]
    others = [i for i in infos if not i.is_main]
    if not others:
        lines.append("  (only the main working tree — no parallel lines open)")
    for i in sorted(infos, key=lambda x: (not x.is_main, x.branch)):
        tag = "main" if i.is_main else i.branch
        flags = []
        if i.dirty:
            flags.append("dirty")
        if i.stale:
            flags.append(f"stale {i.age_days:g}d")
        if not i.is_main and (i.ahead or i.behind):
            flags.append(f"↑{i.ahead} ↓{i.behind}")
        suffix = ("  [" + ", ".join(flags) + "]") if flags else ""
        marker = "*" if i.is_main else " "
        lines.append(f" {marker} {tag:<28} {i.path}{suffix}")
    hints = [i for i in others if i.stale or i.dirty]
    if hints:
        lines.append("")
        lines.append("  ⚠ stale/dirty worktrees are merge hazards + leaked file handles —")
        lines.append("    land them (worktree land) or remove them (worktree remove).")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="worktree",
        description="One worktree per line of work — CONCURRENCY.md as a command.")
    ap.add_argument("--base", default=DEFAULT_BASE,
                    help=f"where worktrees live (default {DEFAULT_BASE}; must be outside iCloud)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    sub = ap.add_subparsers(dest="cmd")

    p = sub.add_parser("start", help="fork a new line of work into its own worktree")
    p.add_argument("feature", help="short slug; becomes <repo>-<feature> + branch <feature>")
    p.add_argument("--branch", help="branch name (default: the feature slug)")
    p.add_argument("--start", help="start-point ref (default: the integration branch)")
    p.set_defaults(func=cmd_start)

    p = sub.add_parser("list", aliases=["ls"], help="show worktrees + hygiene flags")
    p.add_argument("--stale-days", type=float, default=DEFAULT_STALE_DAYS,
                   help=f"divergence age that counts as stale (default {DEFAULT_STALE_DAYS})")
    p.add_argument("--check", action="store_true",
                   help="exit 1 if any worktree is stale or dirty (for CI/hooks)")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("land", help="push the branch + open a PR back to main")
    p.add_argument("feature", nargs="?",
                   help="feature slug (default: the worktree you're standing in)")
    p.set_defaults(func=cmd_land)

    p = sub.add_parser(
        "remove", aliases=["clean"],
        help="remove a worktree (guarded)",
        description="Remove a worktree. Refuses if it has uncommitted changes, or "
                    "if its branch is not contained in origin/<main> or local "
                    "<main> — so a branch landed by a direct push counts as "
                    "landed. If neither ref exists the branch counts as unmerged. "
                    "Reads local refs only (no network) unless --fetch is given.")
    p.add_argument("feature", help="feature slug of the worktree to remove")
    p.add_argument("--force", action="store_true",
                   help="remove even with uncommitted/unmerged work (discards it)")
    p.add_argument("--fetch", action="store_true",
                   help="fetch origin/<main> first (touches the network) — use when "
                        "someone else may have merged the branch on the remote")
    p.add_argument("--delete-branch", action="store_true", help="also delete the branch")
    p.set_defaults(func=cmd_remove)

    ap.add_argument("--selftest", action="store_true", help="run built-in checks and exit")
    return ap


def main(argv: list[str] | None = None) -> int:
    ap = build_parser()
    args = ap.parse_args(argv)
    if getattr(args, "selftest", False):
        return _selftest()
    if not getattr(args, "cmd", None):
        ap.print_help()
        return 2
    return args.func(args)


def _selftest() -> int:
    """Pure-logic smoke checks — no git required, so `worktree --selftest` proves
    the guard logic on any box even offline."""
    ok = True

    def check(name: str, cond: bool):
        nonlocal ok
        if not cond:
            print(f"FAIL: {name}")
            ok = False

    check("icloud detected", is_icloud(Path("~/Library/Mobile Documents/com~apple~CloudDocs/x")))
    check("plain path not icloud", not is_icloud(Path("~/worktrees/repo-feat")))
    check("cloudstorage detected", is_icloud(Path("/Users/x/Library/CloudStorage/Dropbox")))
    check("good feature ok", bool(FEATURE_RE.match("perf-harness")))
    check("dotted feature ok", bool(FEATURE_RE.match("v2.1_fix")))
    check("slash feature rejected", not FEATURE_RE.match("feature/foo"))
    check("space feature rejected", not FEATURE_RE.match("bad name"))
    check("empty feature rejected", not FEATURE_RE.match(""))
    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
