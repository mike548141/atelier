"""commitmsg — reading a commit message, for the commit-message plane's checks.

Shared by the scanners that declare a `msg` template in `tools/floor.py`
(`namescan`, `quotescan`, `320/810`), so the message is cleaned one way and the
pushed range is worked out one way. Stdlib-only; not a scanner.

THE TWO SOURCES a check reads, one per plane. On the `msg` plane the file git
handed the `commit-msg` hook, read before git's own cleanup, so comment lines
and a `--verbose` scissors section may still be there and are removed here. On
the `ci` plane, `git log` over the pushed range (`pushed_range`), which history
already fixed; a check reports over it and never blocks.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

_NUL = "\x00"
_FIELD = "\x01"
_LOG_FORMAT = "--format=%H%x00%B%x01"  # git writes the two separator bytes itself
SHA_RX = re.compile(r"^[0-9a-f]{40,64}$")


def _git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args],
                          capture_output=True, text=True, errors="replace", check=False)


def comment_char(root: Path) -> str:
    """`core.commentChar`, or `#`. An `auto` setting reads as `#`: the file is
    the message as git wrote it, and auto has no one character to name."""
    out = _git(root, "config", "--get", "core.commentChar")
    value = out.stdout.strip() if out.returncode == 0 else ""
    return value[0] if value and value != "auto" else "#"


def clean(text: str, cc: str = "#") -> str:
    """Comment lines and anything from a verbose commit's scissors line down,
    removed. Git does this itself after the hook runs; the hook runs first."""
    scissors = re.compile(rf"^{re.escape(cc)} -+ >8 -+\s*$")
    kept: list[str] = []
    for line in text.splitlines():
        if scissors.match(line):
            break
        if line.startswith(cc):
            continue
        kept.append(line)
    return "\n".join(kept).rstrip("\n")


def read_message(path: Path, root: Path) -> str:
    return clean(path.read_text(encoding="utf-8", errors="replace"), comment_char(root))


def subject(message: str) -> str:
    """The first non-blank line, which is the title git and every host show."""
    for line in message.splitlines():
        if line.strip():
            return line.strip()
    return ""


def branch(root: Path, env: dict | None = None) -> str:
    """The branch being committed to or pushed. An empty string on a detached
    HEAD, which has no name to read."""
    env = os.environ if env is None else env
    for key in ("GITHUB_HEAD_REF", "GITHUB_REF_NAME"):
        if env.get(key):
            return env[key]
    out = _git(root, "symbolic-ref", "-q", "--short", "HEAD")
    return out.stdout.strip() if out.returncode == 0 else ""


def staged_files(root: Path) -> list[str]:
    """What this commit will carry, every status included, read through the
    index git has set for the hook (`GIT_INDEX_FILE` is inherited), so a
    path-scoped commit sees only what it named. A deletion counts."""
    out = _git(root, "diff", "--cached", "--name-only", "--no-renames", "-z")
    if out.returncode != 0:
        raise RuntimeError(f"git diff --cached failed: {out.stderr.strip()}")
    return [p for p in out.stdout.split("\0") if p]


@dataclass
class Commit:
    sha: str
    message: str


def commits(root: Path, spec: str) -> list[Commit]:
    """Every commit in `spec`, newest first. Raises RuntimeError if git cannot
    read the range: a range nobody could read is not a clean range. An empty
    `spec` is `pushed_range` saying there is nothing here to read."""
    if not spec:
        return []
    out = _git(root, "log", _LOG_FORMAT, spec)
    if out.returncode != 0:
        raise RuntimeError(f"git log {spec} failed: {out.stderr.strip()}")
    found: list[Commit] = []
    for record in out.stdout.split(_FIELD):
        record = record.lstrip()
        if _NUL in record:
            sha, message = record.split(_NUL, 1)
            found.append(Commit(sha, clean(message.rstrip(), "#")))
    return found


def commit_files(root: Path, sha: str) -> list[str]:
    """The paths one commit changed, deletions included."""
    out = _git(root, "diff-tree", "--no-commit-id", "--name-only", "--no-renames",
               "-r", "-z", "--root", sha)
    return [p for p in out.stdout.split("\0") if p] if out.returncode == 0 else []


def pushed_range(root: Path, env: dict | None = None) -> tuple[str, str]:
    """(git log spec, note) for the commits this CI run covers. Inside Actions
    the event's own `before` or a pull request's base; anywhere else, and for a
    new branch or an unreachable base, `HEAD^..HEAD` and a note saying so.
    Falls back rather than failing: this reading is report-only, and a shallow
    clone or a force-push must not red a build over a message nobody can edit."""
    env = os.environ if env is None else env
    base = _event_base(env)
    if base and _resolves(root, f"{base}^{{commit}}"):
        return f"{base}..HEAD", ""
    if not _resolves(root, "HEAD"):
        return "", "no commits to read here"
    note = "no pushed range known: reading HEAD only" if not base \
        else "pushed base not in this clone: reading HEAD only"
    return "HEAD^..HEAD" if _resolves(root, "HEAD^") else "HEAD", note


def _resolves(root: Path, rev: str) -> bool:
    return _git(root, "rev-parse", "--verify", "--quiet", rev).returncode == 0


def _event_base(env: dict) -> str:
    try:
        event = json.loads(Path(env.get("GITHUB_EVENT_PATH", "")).read_text(
            encoding="utf-8"))
    except (OSError, ValueError):
        return ""
    base = (event.get("pull_request") or {}).get("base", {}).get("sha") \
        or event.get("before") or ""
    return base if SHA_RX.match(base or "") and set(base) != {"0"} else ""
