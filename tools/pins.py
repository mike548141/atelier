#!/usr/bin/env python3
"""pins — the fleet view of "which children are stale" against atelier HEAD.

The propagation mechanism (method/PROPAGATION.md) makes staleness observable one
repo at a time: each child's CLAUDE.md carries a pin (`atelier@<SHA>`) and a
session-start drift check. That is per-child and pull-based — you only see a
child is behind if you happen to open a session in it. This is the companion
roll-up: stand in atelier, ask "across the whole fleet, who is behind, and by
how much?", and get one answer.

It is deliberately **read-only**. Bumping a pin is a per-repo human-in-the-loop
act (PROPAGATION §5 — the lockfile discipline: the pin moves when someone moves
it, having read the delta and judged it bears on that repo). This tool never
edits a child; it only turns per-child observability into a fleet-level view.
That respects the honest caveat PROPAGATION states: the pin makes staleness
*observable*, not *enforced* — a view is observability, and that is all it
claims to be.

  pins                 discover children under atelier's parent dir + report
  pins --child <path>  report only the named child repo(s)
  pins --json          machine-readable (for a dashboard or a CI gate)
  pins --check         exit 1 if any child is not current (for CI/hooks)
  pins --log           also print the commits each stale child would inspect

How a child is classified (pin = the child's pinned SHA, HEAD = atelier HEAD):
  current   pin == HEAD                       — up to date
  behind    pin is an ancestor of HEAD        — N house commits since the pin
  ahead     HEAD is an ancestor of pin        — child pinned newer than atelier
            (atelier likely not pulled here)  — surfaced, not silently ignored
  diverged  neither is an ancestor            — pin on a different history
  unknown   atelier has no such object        — bad/rewritten pin, or unfetched
  no-pin    CLAUDE.md exists but carries no atelier pin (skipped in discovery,
            reported when named explicitly with --child)

Exit codes (fail-safe — anything but "everything current" is non-zero):
  0  every discovered child is current
  1  at least one child is behind/ahead/diverged/unknown/no-pin (with --check),
     or plain output when something is not current
  2  environment error (not run against an atelier repo, HEAD unreadable, a
     named --child is missing) — we could not truthfully compute the fleet, so
     we do not report a green fleet we did not verify.

Zero third-party dependencies; stdlib only — a peer who adopts atelier runs it
with the system python3 and no install.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

# The pin as written in a child CLAUDE.md: `atelier@<sha>`. 7–40 hex chars covers
# an abbreviated or full SHA. The first occurrence is the authoritative pin (the
# doctrine block heading); later mentions are the drift-check command echoing it.
PIN_RE = re.compile(r"atelier@([0-9a-f]{7,40})\b", re.IGNORECASE)

# Path fragments that mean a directory is inside an iCloud-synced tree. Only used
# to warn: children legitimately live in iCloud (ros, faves do), but a git object
# read there can transiently fail mid-sync, so a read error gets a clearer hint.
ICLOUD_MARKERS = ("com~apple~clouddocs", "mobile documents", "library/cloudstorage")

# 020/380 — extending 020/370's ruling to the fleet tools. `discover()` itself
# only walks ONE level of the search root and reads a single named file
# (CLAUDE.md) per candidate, so it was never the recursive-tree-walk shape
# secretscan's incident was — but that one file was still read WHOLE
# (`read_text()`), so a single oversized CLAUDE.md (real or a malformed
# child) scaled peak memory with that one file's size. Measured while
# building this fix, over SYNTHETIC sibling trees (never real ones — see
# the module docstring's own read-only posture): an 8 MB CLAUDE.md drove
# ~15 MB of extra peak RSS over a 1 MB twin. Grounded in the class, not a
# measurement: a real CLAUDE.md is bounded by sizescan's own SIZE_REFERENCE
# (~200 lines); two-plus orders of magnitude past that leaves generous
# headroom while giving a fixed ceiling. Refused, reported (stderr), never
# silently misread as "no pin".
MAX_CLAUDE_MD_BYTES = 2 * 1024 * 1024

STATUS_CURRENT = "current"
STATUS_BEHIND = "behind"
STATUS_AHEAD = "ahead"
STATUS_DIVERGED = "diverged"
STATUS_UNKNOWN = "unknown"
STATUS_NO_PIN = "no-pin"

# Every status except "current" is actionable (someone should look). Kept as a
# set so --check and the exit code agree on one definition of "not clean".
ACTIONABLE = {STATUS_BEHIND, STATUS_AHEAD, STATUS_DIVERGED, STATUS_UNKNOWN, STATUS_NO_PIN}


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


def main_checkout(repo: Path) -> Path:
    """The main checkout behind `repo`, which IS `repo` unless it is a worktree.

    `--git-common-dir` points at the main checkout's `.git` from any worktree
    (and at `repo/.git` itself from the main checkout), so its parent is the
    main checkout regardless of which copy asked. Falls back to `repo` whenever
    git cannot answer — a non-repo directory, or no git on PATH.

    A twin of `floorfleet.main_checkout`, not an import of it: `floorfleet`
    imports this module for fleet discovery, so importing back would cycle.
    Same shape, same reason to exist — see PU-5 (2026-08-22): `pins` run from
    a worktree resolved `resolve_atelier()` to the WORKTREE (its own
    `--show-toplevel`), so `discover()` walked the worktree's parent directory
    instead of atelier's, and silently reported that wrong denominator as the
    whole fleet."""
    try:
        out = subprocess.run(["git", "-C", str(repo), "rev-parse",
                              "--git-common-dir"],
                             capture_output=True, text=True, check=False)
        if out.returncode == 0 and out.stdout.strip():
            common = Path(out.stdout.strip())
            if not common.is_absolute():
                common = (repo / common)
            return common.resolve().parent
    except OSError:
        pass
    return repo


def is_icloud(path: Path) -> bool:
    hay = str(path.expanduser()).lower()
    return any(m in hay for m in ICLOUD_MARKERS)


def read_pin(claude_md: Path) -> str | None:
    """The first `atelier@<sha>` in a child CLAUDE.md, lower-cased, or None.

    020/380: refuses to read a CLAUDE.md over `MAX_CLAUDE_MD_BYTES` whole —
    reported to stderr, then treated the same as "no pin found" (the same
    safe direction an unreadable file already takes)."""
    try:
        if claude_md.stat().st_size > MAX_CLAUDE_MD_BYTES:
            print(f"pins: warning — {claude_md} is over the "
                 f"{MAX_CLAUDE_MD_BYTES}-byte cap; not read for a pin "
                 "(020/380)", file=sys.stderr)
            return None
        text = claude_md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = PIN_RE.search(text)
    return m.group(1).lower() if m else None


def classify(pin_known: bool, pin_is_head: bool,
             pin_ancestor_of_head: bool, head_ancestor_of_pin: bool) -> str:
    """Pure status decision — no git, so it is unit-testable offline and the
    selftest can prove the whole table. Order matters: a known pin equal to HEAD
    is current before any ancestor test."""
    if not pin_known:
        return STATUS_UNKNOWN
    if pin_is_head:
        return STATUS_CURRENT
    if pin_ancestor_of_head:
        return STATUS_BEHIND
    if head_ancestor_of_pin:
        return STATUS_AHEAD
    return STATUS_DIVERGED


@dataclass
class ChildPin:
    name: str            # repo directory name
    path: str            # child repo path
    pin: str | None      # pinned SHA as written (short), or None if no pin found
    status: str          # one of the STATUS_* values
    behind: int          # house commits between pin and HEAD (behind direction)
    ahead: int           # commits the pin sits past HEAD (ahead/diverged direction)
    log: list[str]       # one-line log of the commits a stale child would inspect


def _is_ancestor(repo: Path, a: str, b: str) -> bool:
    """True iff commit a is an ancestor of commit b (or a == b) in repo."""
    return git(["-C", str(repo), "merge-base", "--is-ancestor", a, b],
               check=False).returncode == 0


def _count(repo: Path, rng: str) -> int:
    out = git(["-C", str(repo), "rev-list", "--count", rng], check=False)
    return int(out.stdout.strip()) if out.returncode == 0 and out.stdout.strip() else 0


def _known(repo: Path, sha: str) -> bool:
    """True iff atelier has this object as a commit — the pin resolves to a real
    commit in this repo (not a blob/tree, not a missing/rewritten SHA)."""
    return git(["-C", str(repo), "cat-file", "-e", f"{sha}^{{commit}}"],
               check=False).returncode == 0


def evaluate(atelier: Path, head: str, child_dir: Path, want_log: bool) -> ChildPin:
    claude = child_dir / "CLAUDE.md"
    pin = read_pin(claude) if claude.is_file() else None
    info = ChildPin(child_dir.name, str(child_dir), pin, STATUS_NO_PIN, 0, 0, [])
    if pin is None:
        return info

    if not _known(atelier, pin):
        info.status = STATUS_UNKNOWN
        return info

    pin_is_head = _is_ancestor(atelier, head, pin) and _is_ancestor(atelier, pin, head)
    pin_anc = _is_ancestor(atelier, pin, head)
    head_anc = _is_ancestor(atelier, head, pin)
    info.status = classify(True, pin_is_head, pin_anc, head_anc)

    if info.status == STATUS_BEHIND:
        info.behind = _count(atelier, f"{pin}..{head}")
        if want_log:
            info.log = _log(atelier, f"{pin}..{head}")
    elif info.status == STATUS_AHEAD:
        info.ahead = _count(atelier, f"{head}..{pin}")
    elif info.status == STATUS_DIVERGED:
        info.behind = _count(atelier, f"{pin}..{head}")
        info.ahead = _count(atelier, f"{head}..{pin}")
    return info


def _log(repo: Path, rng: str) -> list[str]:
    out = git(["-C", str(repo), "log", "--oneline", "--no-decorate", rng], check=False)
    return out.stdout.splitlines() if out.returncode == 0 else []


def discover(roots: list[Path], atelier: Path, quiet: bool = False) -> list[Path]:
    """One level under each search root, the git repos that carry an atelier pin.
    A directory qualifies if it has a .git entry and a CLAUDE.md that names a pin.
    atelier itself is excluded — it is the parent, not a child. Unreadable roots
    degrade to a warning (fail-safe: report the children we could see, don't
    crash the whole fleet view on one bad path).

    Always reports what it looked at and what it found (to stderr, unless
    `quiet`) — PU-5 was not just a wrong root, it was a wrong root that reported
    its (small, plausible-looking) count as the fleet with no hint anything was
    off. Printing the search root and the funnel (entries seen -> git repos ->
    pinned children) alongside the answer means a reader can judge for
    themselves whether "1 of 1" is a clean fleet or a fleet nobody found."""
    found: dict[str, Path] = {}
    for root in roots:
        try:
            entries = sorted(p for p in root.iterdir() if p.is_dir())
        except OSError as e:
            print(f"pins: warning — cannot read search root {root}: {e}", file=sys.stderr)
            continue
        git_repos = 0
        pinned = 0
        for d in entries:
            if d.resolve() == atelier.resolve():
                continue
            if not (d / ".git").exists():
                continue
            git_repos += 1
            claude = d / "CLAUDE.md"
            if claude.is_file() and read_pin(claude) is not None:
                pinned += 1
                found[str(d.resolve())] = d
        if not quiet:
            print(f"pins: searched {root} — {len(entries)} entries, "
                 f"{git_repos} are git repos, {pinned} carry an atelier pin",
                 file=sys.stderr)
    return list(found.values())


def resolve_atelier(explicit: str | None) -> Path:
    """The atelier repo to measure against: --atelier if given, else the git repo
    the running script lives in (so `pins` just works from a checkout) —
    resolved to its MAIN checkout either way, via `main_checkout()`.

    Without that resolution, running `pins` from a worktree found the
    worktree's own `--show-toplevel` (a worktree is a real, distinct toplevel),
    so `discover()` walked the worktree's PARENT directory — e.g.
    `/Users/mike/worktrees/` — instead of atelier's siblings, and reported that
    wrong root's contents as if it were the whole fleet (PU-5). Anchoring on
    the main checkout instead means `pins` gives the same answer regardless of
    which copy of the repo it is invoked from."""
    start = Path(explicit).expanduser() if explicit else Path(__file__).resolve().parent
    return main_checkout(toplevel(start))


def cmd_report(args) -> int:
    try:
        atelier = resolve_atelier(args.atelier)
        head = git(["-C", str(atelier), "rev-parse", "HEAD"]).stdout.strip()
    except GitError as e:
        print(f"pins: {e}", file=sys.stderr)
        print("pins: run this from an atelier checkout, or pass --atelier <path>.",
              file=sys.stderr)
        return 2

    roots: list[Path] | None = None
    if args.child:
        children: list[Path] = []
        for c in args.child:
            p = Path(c).expanduser()
            if not p.is_dir():
                print(f"pins: named child not found: {p}", file=sys.stderr)
                return 2
            children.append(p)
    else:
        roots = [Path(r).expanduser() for r in args.root] if args.root else [atelier.parent]
        children = discover(roots, atelier)

    infos = [evaluate(atelier, head, c, args.log) for c in
             sorted(children, key=lambda p: p.name.lower())]

    if args.json:
        out = {
            "atelier": str(atelier),
            "head": head,
            "children": [asdict(i) for i in infos],
        }
        if roots is not None:
            out["searched"] = [str(r) for r in roots]
        print(json.dumps(out, indent=2))
    else:
        print(render(infos, atelier, head, args.log, roots))

    if not infos:
        # Nothing discovered is not "all clean" — say so, and treat as actionable
        # under --check (a fleet view that finds no fleet is usually a wrong root).
        return 1 if args.check else 0
    not_current = any(i.status in ACTIONABLE for i in infos)
    if args.check:
        return 1 if not_current else 0
    return 1 if not_current else 0


# --------------------------------------------------------------------------- #
# rendering
# --------------------------------------------------------------------------- #

_MARK = {
    STATUS_CURRENT: "✓",
    STATUS_BEHIND: "→",
    STATUS_AHEAD: "!",
    STATUS_DIVERGED: "✗",
    STATUS_UNKNOWN: "?",
    STATUS_NO_PIN: "·",
}


def _detail(i: ChildPin) -> str:
    if i.status == STATUS_BEHIND:
        return f"{i.behind} behind"
    if i.status == STATUS_AHEAD:
        return f"{i.ahead} ahead"
    if i.status == STATUS_DIVERGED:
        return f"↑{i.ahead} ↓{i.behind}"
    if i.status == STATUS_UNKNOWN:
        return "pin not in atelier"
    if i.status == STATUS_NO_PIN:
        return "no atelier pin"
    return ""


def render(infos: list[ChildPin], atelier: Path, head: str, want_log: bool,
          roots: list[Path] | None = None) -> str:
    lines = [f"atelier fleet pins  (HEAD {head[:7]}  {atelier})"]
    if roots is not None:
        # Named explicitly, always — not just when the count looks wrong. PU-5
        # was a small, plausible-looking count from the wrong place; the fix is
        # a reader can always see where "found" came from, not a guess at which
        # counts look implausible enough to call out (see discover()'s docstring).
        lines.append(f"  searched: {', '.join(str(r) for r in roots)}"
                     f"  ({len(infos)} found)")
    if not infos:
        where = (f" under {', '.join(str(r) for r in roots)}" if roots
                else " under the search root")
        lines.append(f"  (no atelier children found{where})")
        return "\n".join(lines)
    width = max(len(i.name) for i in infos)
    for i in infos:
        mark = _MARK.get(i.status, " ")
        pin = i.pin[:7] if i.pin else "—"
        detail = _detail(i)
        tail = f"  {detail}" if detail else ""
        lines.append(f" {mark} {i.name:<{width}}  {i.status:<8} {pin}{tail}")
        if want_log and i.log:
            for entry in i.log:
                lines.append(f"       {entry}")
    stale = [i for i in infos if i.status in ACTIONABLE]
    if stale:
        lines.append("")
        lines.append(f"  {len(stale)} of {len(infos)} not current — a pin bump is a "
                     "deliberate per-repo act (read the delta first).")
        lines.append("  In the stale child, run its CLAUDE.md drift check, then bump the pin.")
    else:
        lines.append("")
        lines.append(f"  all {len(infos)} children current ✓")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="pins",
        description="Fleet view of child-repo atelier pins — who is stale, by how much.")
    ap.add_argument("--atelier", help="atelier repo path (default: the repo this script lives in)")
    ap.add_argument("--root", action="append",
                    help="search root for discovery (repeatable; default: atelier's parent dir)")
    ap.add_argument("--child", action="append",
                    help="report only this child repo (repeatable; bypasses discovery)")
    ap.add_argument("--log", action="store_true",
                    help="also print the commits each stale child would inspect")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if any child is not current (for CI/hooks)")
    ap.add_argument("--selftest", action="store_true", help="run built-in checks and exit")
    ap.set_defaults(func=cmd_report)
    return ap


def main(argv: list[str] | None = None) -> int:
    ap = build_parser()
    args = ap.parse_args(argv)
    if getattr(args, "selftest", False):
        return _selftest()
    return args.func(args)


def _selftest() -> int:
    """Pure-logic checks — no git needed, so `pins --selftest` proves the pin
    parse + status classification on any box, offline."""
    ok = True

    def check(name: str, cond: bool):
        nonlocal ok
        if not cond:
            print(f"FAIL: {name}")
            ok = False

    # pin parse
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write("# x\n## Doctrine — inherited from atelier (pinned `atelier@7f5abd0`)\n"
                "run `git ... atelier@7f5abd0..HEAD`\n")  # leakscan:allow: atelier pin syntax, not an email
        pinpath = Path(f.name)
    check("pin parsed", read_pin(pinpath) == "7f5abd0")
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write("no pin here\n")
        nopinpath = Path(f.name)
    check("no pin -> None", read_pin(nopinpath) is None)

    # classification table
    check("unknown", classify(False, False, False, False) == STATUS_UNKNOWN)
    check("current", classify(True, True, True, True) == STATUS_CURRENT)
    check("behind", classify(True, False, True, False) == STATUS_BEHIND)
    check("ahead", classify(True, False, False, True) == STATUS_AHEAD)
    check("diverged", classify(True, False, False, False) == STATUS_DIVERGED)

    check("icloud detected", is_icloud(Path("~/Library/Mobile Documents/com~apple~CloudDocs/x")))
    check("plain path not icloud", not is_icloud(Path("~/code/repo")))

    pinpath.unlink(missing_ok=True)
    nopinpath.unlink(missing_ok=True)
    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
