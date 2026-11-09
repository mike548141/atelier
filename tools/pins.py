#!/usr/bin/env python3
"""pins — the fleet view of "which children are stale" against atelier's mainline.

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

  pins                 fetch, then discover children under atelier's parent dir
                       + report against the published mainline (origin/main)
  pins --head          offline: measure against the local checkout's HEAD instead
  pins --child <path>  report only the named child repo(s)
  pins --json          machine-readable (for a dashboard or a CI gate)
  pins --check         exit 1 if any child is not current (for CI/hooks); from
                       2026-12-09 also if a child's floor copy differs, is
                       unstamped, is malformed or cannot be compared (an
                       archived repo is exempt)
  pins --log           also print the commits each stale child would inspect

The reference is the parent's *published* mainline (`origin/main`, after a
`git fetch`), the same reference a child's own session-start drift check uses
(PROPAGATION § The mechanism, point 4), never whatever branch or stale commit
the atelier checkout happens to sit on (160/310 HF3, `320/260`). A fetch that
fails is *no result*, not *no drift*: the tool exits 2 and says so, rather than
report a fleet measured against a checkout it could not refresh. `--head` is
the explicit offline choice, and the report names which reference it used.
The remote is assumed to be named `origin`.

How a child is classified (pin = the child's pinned SHA, HEAD = the reference
above; with `--head`, atelier's local HEAD):
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
  2  environment error (not run against an atelier repo, the reference
     unreadable, the fetch failed, a named --child is missing) — we could not truthfully compute the fleet, so
     we do not report a green fleet we did not verify.

THE FLOOR-COPY REPORT (`160/340`; Mike, 2026-11-09: "The approve the report
only option for 1 month and then we move to blocking per option 2"). Every child
inlines atelier's safety floor between `stamp:begin`/`stamp:end` markers, and
nothing reached a child's copy: a pin bump without a re-copy reddened nowhere
(`020/215` LR4, `160/340` FV3, FV11). For each child with a pin this also compares
that copy with the canonical `floor` region, using `stampscan`'s own comparison
(`find_stamp_blocks`, `extract_region`, `evaluate_block`) and no second one.
Two things the comparison needs that `stampscan` alone cannot give:
  - the REFERENCE is the floor text AT THE CHILD'S OWN PIN, read with
    `git show <pin>:docs/method/PROPAGATION.md`, not the current text. A child
    pinned in the past is lawfully verbatim to what it pinned; comparing it with
    today's text would red every stale child for being stale, which `pins` already
    reports as `behind`. A copy that differs from its OWN pin is the thing this
    finds: a hand-edit, a compression, a partial re-copy. The report also says
    whether the floor text itself has moved since the pin (`floor moved`), so a
    child that is verbatim but out of date shows as both.
  - the four placeholders a child fills (`<SHA>`, `<atelier-path>`,
    `<visibility fact>`, `<owner/repo>`) are read out of the child's own lines
    and put back into the reference before `stampscan` compares, so a compliant
    copy reads `identical`. Anything else that differs is `drift`.
REPORT-ONLY until `COPY_BLOCKS_FROM` (2026-12-09), the date printed on every run.
From it, four states fail `--check` and the exit code like a stale pin: `drift`
(the copy differs: option 2, "block any repo whose copy differs"), and, from the
principal's answer of 2026-11-09 to a later ask, "Require a stamp by 9 Dec":
`unstamped` (no stamp for the floor in CLAUDE.md, so nothing can be compared),
`no-reference` (an old pin, from before the floor region was marked, or one this
checkout does not hold: bumping the pin fixes it) and `malformed` (the stamp
markers are broken, so the stamp is not there to read). One dated constant, as
leakscan's `BINARY_GRACE_UNTIL`: no flag, env var or config key moves it.
**An archived repo is exempt.** A repo archived on GitHub can no longer be
changed, so it can neither be stamped nor re-pinned. The tool asks GitHub, with
`gh`, and only after the date and only for a child that would otherwise fail
(so a clean fleet makes no call, and a test never does). When it cannot
establish the answer (no `gh`, no GitHub remote, no network) the child is NOT
exempt: a lookup that failed reads as "not archived", never as an exemption, and
the line says the archive state was not established. Two states are still only
reported, never failed: `skipped` (a `stampscan:allow` marker; the floor's own
stamp no longer honours one, so this is the legacy reading) and `unchecked`
(CLAUDE.md could not be read after its pin was).

Zero third-party dependencies; stdlib only — a peer who adopts atelier runs it
with the system python3 and no install.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import estate  # noqa: E402  — where the main checkout and the estate root are
import stampscan  # noqa: E402  — the floor-copy comparison is stampscan's, not a second one

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
# measurement: a real CLAUDE.md is a thin onramp of about 200 lines (the
# class reference sizescan once held for it, since removed by 115/270 c;
# nothing here reads that number); two-plus orders of magnitude past that
# leaves generous headroom while giving a fixed ceiling. Refused, reported (stderr), never
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


# --- the floor-copy report ---------------------------------------------------

# THE CUT-OFF. Report-only before this date (UTC), blocking from it: Mike,
# 2026-11-09, `160/340` — "The approve the report only option for 1 month and
# then we move to blocking per option 2". One constant compared with the UTC
# clock, in leakscan's `BINARY_GRACE_UNTIL` style: no flag, env var or config key
# moves it, and the date is printed on every run. Delete the report-only path
# once it has passed and the blocking is wanted for good.
COPY_BLOCKS_FROM = datetime.date(2026, 12, 9)

# The four values a child fills into the floor block. A line of the canonical
# region may carry one or more; anything else in the region is literal.
COPY_PLACEHOLDERS = ("<SHA>", "<atelier-path>", "<visibility fact>", "<owner/repo>")
_PLACEHOLDER_RX = re.compile("(" + "|".join(re.escape(t) for t in COPY_PLACEHOLDERS) + ")")

COPY_IDENTICAL = "identical"      # word for word the floor at the child's pin
COPY_DRIFT = "drift"              # differs
COPY_SKIPPED = "skipped"          # a stampscan:allow marker skipped the comparison
COPY_UNSTAMPED = "unstamped"      # no stamp for the floor in CLAUDE.md
COPY_NO_REFERENCE = "no-reference"  # no floor region at the pin (or the pin is unknown)
COPY_MALFORMED = "malformed"      # stamp markers broken, nothing to compare
COPY_UNCHECKED = "unchecked"      # not asked for, or the pin could not be read

# The states that fail the check from `COPY_BLOCKS_FROM` (160/340; Mike,
# 2026-11-09, "Require a stamp by 9 Dec"). Drift is the original option 2. The
# other three each have a fix the child can make: stamp the copy, bump the pin,
# repair the markers. `skipped` and `unchecked` are not here: nothing the
# child can do changes what they say, or they say nothing about the copy.
COPY_BLOCKING_STATES = (COPY_DRIFT, COPY_UNSTAMPED, COPY_NO_REFERENCE, COPY_MALFORMED)

# Shown with the report, one mark per state.
_COPY_MARK = {COPY_IDENTICAL: "✓", COPY_DRIFT: "✗", COPY_SKIPPED: "!",
              COPY_UNSTAMPED: "✗", COPY_NO_REFERENCE: "✗", COPY_MALFORMED: "✗",
              COPY_UNCHECKED: "·"}


def _utc_today() -> datetime.date:
    return datetime.datetime.now(datetime.timezone.utc).date()


def copy_blocking(today: datetime.date | None = None) -> bool:
    """True from `COPY_BLOCKS_FROM` (UTC) on. Tests patch `_utc_today`; nothing a
    caller can pass at the command line reaches it."""
    return (today or _utc_today()) >= COPY_BLOCKS_FROM


def floor_region_at(atelier: Path, ref: str) -> list[str] | None:
    """The canonical `floor` region of PROPAGATION.md as it stood at `ref`
    (a commit in `atelier`), or None when that commit has no such file or no
    region markers (a pin from before the region was marked) or git cannot say.
    The region is extracted by `stampscan.extract_region`, fence stripping
    included, so it is exactly the text `stampscan` would compare."""
    out = git(["-C", str(atelier), "show", f"{ref}:{stampscan.FLOOR_SOURCE}"], check=False)
    if out.returncode != 0:
        return None
    return stampscan.extract_region(out.stdout, stampscan.FLOOR_REGION)


# A placeholder's value may run over several lines (the visibility fact usually
# does); this many child lines at most are joined to fit one canonical line.
_MAX_VALUE_LINES = 8


def fill_placeholders(canonical: list[str], child_lines: list[str]) -> list[str]:
    """The canonical region with the child's own placeholder values put back.

    Each canonical line that carries a placeholder becomes a pattern, and the
    child's lines are scanned once, in order, for the first run of one to
    `_MAX_VALUE_LINES` lines that fits it; what the placeholders matched there is
    what the child filled in. The first value seen for a placeholder wins, and a
    later line that disagrees then fails `stampscan`'s own comparison, which is
    the only judge of a difference. A placeholder no child line fills (or that
    the child left as the bare placeholder) is marked «… left unfilled» in the
    reference, so the comparison reds on it and names the line. Nothing here
    decides whether a copy is right."""
    values: dict[str, str] = {}
    child = [ln.rstrip() for ln in child_lines]
    at = 0
    for line in canonical:
        parts = _PLACEHOLDER_RX.split(line.rstrip())
        if len(parts) == 1:
            continue
        names = [p for n, p in enumerate(parts) if n % 2]
        rx = re.compile("".join(
            re.escape(p) if i % 2 == 0 else "(.+?)" for i, p in enumerate(parts)), re.DOTALL)
        found = False
        for j in range(at, len(child)):
            for k in range(1, _MAX_VALUE_LINES + 1):
                m = rx.fullmatch("\n".join(child[j:j + k]))
                if m:
                    for name, val in zip(names, m.groups()):
                        # A value that is itself a placeholder is a blank left
                        # blank, not a value: it stays unfilled.
                        if not _PLACEHOLDER_RX.search(val):
                            values.setdefault(name, val)
                    at = j + k
                    found = True
                    break
            if found:
                break
    filled = [_PLACEHOLDER_RX.sub(
        lambda m: values.get(m.group(1), f"«{m.group(1)[1:-1]} left unfilled»"), ln)
        for ln in canonical]
    return "\n".join(filled).split("\n")


def check_copy(label: str, text: str, canonical: list[str]) -> tuple[str, str]:
    """(state, detail) for one child's CLAUDE.md text against the canonical floor
    region it should copy. The verdict on a stamped block is
    `stampscan.evaluate_block`'s; this only finds the block and fills the four
    placeholders. When a file stamps the floor more than once the worst wins
    (drift, then skipped, then identical)."""
    blocks, malformed = stampscan.find_stamp_blocks(label, text)
    floor = [b for b in blocks
             if b.source == stampscan.FLOOR_SOURCE and b.region == stampscan.FLOOR_REGION]
    if not floor:
        if malformed:
            return COPY_MALFORMED, malformed[0].detail
        return COPY_UNSTAMPED, "no stamp for the floor in CLAUDE.md, so there is no copy to compare"
    rank = {COPY_IDENTICAL: 0, COPY_SKIPPED: 1, COPY_DRIFT: 2}
    worst, detail = COPY_IDENTICAL, ""
    for b in floor:
        f = stampscan.evaluate_block(b, fill_placeholders(canonical, b.payload))
        state = {"identical": COPY_IDENTICAL, "skipped": COPY_SKIPPED}.get(f.kind, COPY_DRIFT)
        if rank[state] >= rank[worst]:
            worst, detail = state, f.detail
            left = sorted({t for ln in b.payload for t in _PLACEHOLDER_RX.findall(ln)})
            if state == COPY_DRIFT and left:
                detail = (f"the copy still carries the unfilled placeholder(s) "
                          f"{', '.join(left)} — fill each one in; {detail}")
    return worst, detail


def copy_would_block(info: "ChildPin") -> bool:
    """Would this child's copy fail the check once `COPY_BLOCKS_FROM` has come,
    ignoring the clock and any archive exemption? Pure: a state, nothing else."""
    return info.copy in COPY_BLOCKING_STATES


def copy_blocks(info: "ChildPin", today: datetime.date | None = None) -> bool:
    """Does this child's copy fail its check today? A copy in a blocking state
    does, from `COPY_BLOCKS_FROM`, unless the repo is known to be archived. Only
    `archived is True` exempts: `None` (never asked, or the lookup failed) and
    `False` both leave the child failing."""
    return (copy_would_block(info) and copy_blocking(today)
            and info.archived is not True)


GITHUB_REMOTE_RX = re.compile(
    r"github\.com[:/]+([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9._-]+?)(?:\.git)?/?$")


def archived_on_github(child_dir: Path) -> bool | None:
    """Is the child's GitHub repo archived? True or False when GitHub said so,
    None when that could not be established: no `origin`, a remote that is not on
    GitHub, no `gh`, no network, no access, or an answer that is not a boolean.
    One `gh repo view` call; only reached for a child that would otherwise fail,
    and only from `COPY_BLOCKS_FROM`. Tests patch this function and never reach
    the network."""
    remote = git(["-C", str(child_dir), "remote", "get-url", "origin"], check=False)
    if remote.returncode != 0:
        return None
    m = GITHUB_REMOTE_RX.search(remote.stdout.strip())
    if not m:
        return None
    try:
        proc = subprocess.run(
            ["gh", "repo", "view", f"{m.group(1)}/{m.group(2)}",
             "--json", "isArchived", "-q", ".isArchived"],
            capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    answer = proc.stdout.strip().lower()
    if proc.returncode != 0 or answer not in ("true", "false"):
        return None
    return answer == "true"


def resolve_archive_state(infos: list["ChildPin"], today: datetime.date | None = None) -> None:
    """Ask GitHub about each child that would otherwise fail, from the cut-off
    on, and record the answer on the child. Nothing is asked before the date or
    of a child that passes."""
    if not copy_blocking(today):
        return
    for i in infos:
        if copy_would_block(i) and i.archived is None:
            i.archived = archived_on_github(Path(i.path))
            i.archive_checked = True


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
    `estate.main_checkout`, the one shared answer (`320/180`). See PU-5
    (2026-08-22): `pins` run from a worktree resolved `resolve_atelier()` to the
    WORKTREE (its own `--show-toplevel`), so `discover()` walked the worktree's
    parent directory instead of atelier's, and silently reported that wrong
    denominator as the whole fleet."""
    return estate.main_checkout(repo)


def is_icloud(path: Path) -> bool:
    hay = str(path.expanduser()).lower()
    return any(m in hay for m in ICLOUD_MARKERS)


def read_claude_text(claude_md: Path) -> str | None:
    """A child's CLAUDE.md text, or None when it is over `MAX_CLAUDE_MD_BYTES`
    (reported to stderr) or cannot be read. One bounded read, shared by the pin
    and the floor-copy check."""
    try:
        if claude_md.stat().st_size > MAX_CLAUDE_MD_BYTES:
            print(f"pins: warning — {claude_md} is over the "
                 f"{MAX_CLAUDE_MD_BYTES}-byte cap; not read for a pin "
                 "(020/380)", file=sys.stderr)
            return None
        return claude_md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def read_pin(claude_md: Path) -> str | None:
    """The first `atelier@<sha>` in a child CLAUDE.md, lower-cased, or None.

    020/380: refuses to read a CLAUDE.md over `MAX_CLAUDE_MD_BYTES` whole —
    reported to stderr, then treated the same as "no pin found" (the same
    safe direction an unreadable file already takes)."""
    text = read_claude_text(claude_md)
    if text is None:
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
    # The floor-copy report (see the module docstring). `copy` is one of the
    # COPY_* states; `copy_detail` says why in a line; `floor_moved` is whether
    # the canonical floor text changed between the child's pin and the reference
    # (None when either end could not be read).
    copy: str = "unchecked"
    copy_detail: str = ""
    floor_moved: bool | None = None
    # Whether the repo is archived on GitHub (an archived repo is exempt from
    # the floor-copy block). `None` until asked, and still `None` when GitHub
    # could not be reached; `archive_checked` says which. Asked only from
    # `COPY_BLOCKS_FROM`, and only of a child that would otherwise fail.
    archived: bool | None = None
    archive_checked: bool = False


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


def _copy_report(atelier: Path, head: str, pin: str, claude: Path, info: ChildPin,
                 cache: dict) -> None:
    """Fill `info.copy*` and `info.floor_moved` for a child whose pin is a commit
    in `atelier`. `cache` holds one floor region per commit across children."""
    def region(ref):
        if ref not in cache:
            cache[ref] = floor_region_at(atelier, ref)
        return cache[ref]

    at_pin = region(pin)
    at_head = region(head)
    if at_pin is not None and at_head is not None:
        norm = stampscan._trim_blank_boundary
        info.floor_moved = norm(stampscan._normalise(at_pin)) != norm(stampscan._normalise(at_head))
    if at_pin is None:
        info.copy = COPY_NO_REFERENCE
        info.copy_detail = (f"no floor region in {stampscan.FLOOR_SOURCE} at the pin "
                            f"{pin[:7]}, so there is no text to compare the copy with")
        return
    text = read_claude_text(claude)
    if text is None:
        info.copy = COPY_UNCHECKED
        info.copy_detail = "CLAUDE.md could not be read"
        return
    info.copy, info.copy_detail = check_copy(f"{info.name}/CLAUDE.md", text, at_pin)


def evaluate(atelier: Path, head: str, child_dir: Path, want_log: bool,
             copy_cache: dict | None = None) -> ChildPin:
    claude = child_dir / "CLAUDE.md"
    pin = read_pin(claude) if claude.is_file() else None
    info = ChildPin(child_dir.name, str(child_dir), pin, STATUS_NO_PIN, 0, 0, [])
    if pin is None:
        return info

    if not _known(atelier, pin):
        info.status = STATUS_UNKNOWN
        info.copy = COPY_NO_REFERENCE
        info.copy_detail = f"the pin {pin[:7]} is not a commit in this atelier checkout"
        return info
    _copy_report(atelier, head, pin, claude, info, {} if copy_cache is None else copy_cache)

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


def _pinned_child(d: Path, found: dict[str, Path]) -> bool:
    claude = d / "CLAUDE.md"
    if claude.is_file() and read_pin(claude) is not None:
        found[str(d.resolve())] = d
        return True
    return False


def _names(items: list[str], limit: int = 12) -> str:
    shown = ", ".join(items[:limit])
    extra = len(items) - limit
    return f"{shown}, and {extra} more" if extra > 0 else shown


def discover(roots: list[Path], atelier: Path, quiet: bool = False,
             grouped: bool | None = None) -> list[Path]:
    """One level under each search root, the git repos that carry an atelier pin.
    A directory qualifies if it has a .git entry and a CLAUDE.md that names a pin.
    atelier itself is excluded — it is the parent, not a child. Unreadable roots
    degrade to a warning (fail-safe: report the children we could see, don't
    crash the whole fleet view on one bad path).

    `grouped` (`320/660`; default: whether `ATELIER_ESTATE_ROOT` or
    `hooks.atelierEstateRoot` is set, see `estate.py`): a directory under a
    search root that is not a repo is treated as a group folder and walked one
    level deeper, and only one. A repo is never descended into. A hidden folder
    or a symlink is not walked, and is named as skipped.

    Always reports what it looked at and what it found (to stderr, unless
    `quiet`) — PU-5 was not just a wrong root, it was a wrong root that reported
    its (small, plausible-looking) count as the fleet with no hint anything was
    off. Printing the search root and the funnel (entries seen -> git repos ->
    pinned children) alongside the answer means a reader can judge for
    themselves whether "1 of 1" is a clean fleet or a fleet nobody found."""
    if grouped is None:
        grouped = estate.root_setting(atelier) is not None
    found: dict[str, Path] = {}
    home = atelier.resolve()
    for root in roots:
        try:
            entries = sorted(p for p in root.iterdir() if p.is_dir())
        except OSError as e:
            print(f"pins: warning — cannot read search root {root}: {e}", file=sys.stderr)
            continue
        git_repos = 0
        pinned = 0
        walked: list[str] = []
        skipped: list[str] = []
        not_repos = 0
        for d in entries:
            if d.resolve() == home:
                continue
            if (d / ".git").exists():
                git_repos += 1
                pinned += _pinned_child(d, found)
                continue
            if not grouped:
                continue
            if d.name.startswith(".") or d.is_symlink():
                skipped.append(d.name)
                continue
            try:
                inside = sorted(p for p in d.iterdir() if p.is_dir())
            except OSError as e:
                print(f"pins: warning — cannot read group folder {d}: {e}",
                      file=sys.stderr)
                skipped.append(d.name)
                continue
            repos_here = 0
            for c in inside:
                if c.resolve() == home:
                    continue
                if not (c / ".git").exists():
                    not_repos += 1
                    continue
                repos_here += 1
                pinned += _pinned_child(c, found)
            git_repos += repos_here
            walked.append(f"{d.name} ({repos_here})")
        if not quiet:
            print(f"pins: searched {root} — {len(entries)} entries, "
                 f"{git_repos} are git repos, {pinned} carry an atelier pin",
                 file=sys.stderr)
            if grouped:
                print(f"pins: grouped layout — walked {len(walked)} group "
                      f"folder(s) one level deeper, repos in each: "
                      f"{_names(walked) or 'none'}; skipped {len(skipped)} "
                      f"hidden, symlinked or unreadable: "
                      f"{_names(skipped) or 'none'}; {not_repos} folder(s) "
                      "inside a group are not repos and were not descended",
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


MAINLINE_REF = "origin/main"


def reference(atelier: Path, use_head: bool) -> tuple[str, str]:
    """(sha, label) of the commit the fleet is measured against.

    Default is the published mainline after a fetch. A failed fetch raises —
    an empty or stale answer would read as "current", the silent-negative
    shape the verify-the-act bullet names — and the message points at `--head`
    for the offline case instead of falling back on its own."""
    if use_head:
        return git(["-C", str(atelier), "rev-parse", "HEAD"]).stdout.strip(), "HEAD"
    fetched = git(["-C", str(atelier), "fetch", "-q", "origin"], check=False)
    if fetched.returncode != 0:
        raise GitError(
            "could not fetch origin in the atelier checkout "
            f"({fetched.stderr.strip() or 'no output'}) — a fetch error is no "
            "result, not no drift; pass --head to measure the local checkout "
            "offline")
    ref = git(["-C", str(atelier), "rev-parse", "--verify", "-q",
               f"{MAINLINE_REF}^{{commit}}"], check=False)
    if ref.returncode != 0 or not ref.stdout.strip():
        raise GitError(f"the atelier checkout has no {MAINLINE_REF} after the "
                       "fetch (the published-mainline remote is assumed to be "
                       "named origin); pass --head to measure the local checkout")
    return ref.stdout.strip(), MAINLINE_REF


def cmd_report(args) -> int:
    try:
        atelier = resolve_atelier(args.atelier)
        head, ref_label = reference(atelier, getattr(args, "head", False))
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
        roots = [Path(r).expanduser() for r in args.root] if args.root \
            else [estate.parent(atelier)]
        children = discover(roots, atelier)

    cache: dict = {}
    infos = [evaluate(atelier, head, c, args.log, cache) for c in
             sorted(children, key=lambda p: p.name.lower())]
    today = _utc_today()
    resolve_archive_state(infos, today)
    blocked = [i for i in infos if copy_blocks(i, today)]

    if args.json:
        out = {
            "atelier": str(atelier),
            "ref": ref_label,
            "head": head,
            "floor_copy": {
                "blocks_from": COPY_BLOCKS_FROM.isoformat(),
                "blocking": copy_blocking(today),
                "differing": [i.name for i in infos if i.copy == COPY_DRIFT],
                # Every child in a state that fails from the date, unless
                # archived. Always present, so a consumer's keys do not vary.
                "blocking_states": list(COPY_BLOCKING_STATES),
                "would_fail": [i.name for i in infos if copy_would_block(i)],
                "failing": [i.name for i in blocked],
                "archived_exempt": [i.name for i in infos
                                    if copy_would_block(i) and i.archived is True],
            },
            "children": [asdict(i) for i in infos],
        }
        if roots is not None:
            out["searched"] = [str(r) for r in roots]
        print(json.dumps(out, indent=2))
    else:
        print(render(infos, atelier, head, args.log, roots, ref_label, today))

    if not infos:
        # Nothing discovered is not "all clean" — say so, and treat as actionable
        # under --check (a fleet view that finds no fleet is usually a wrong root).
        return 1 if args.check else 0
    not_current = any(i.status in ACTIONABLE for i in infos) or bool(blocked)
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


def render_copy(infos: list[ChildPin], today: datetime.date | None = None) -> list[str]:
    """The floor-copy section: one line per child, and the cut-off date always."""
    blocking = copy_blocking(today)
    when = COPY_BLOCKS_FROM.isoformat()
    lines = ["", "  floor copy — each child's stamped floor block against the floor text at its own pin"]
    lines.append(f"  {'BLOCKING since' if blocking else 'report-only until'} {when}"
                 + (": a copy that differs, has no stamp, has a broken stamp or "
                    "pins a commit with no floor text to compare fails this check."
                    if blocking else
                    ": from then a copy that differs, has no stamp, has a broken "
                    "stamp or pins a commit with no floor text to compare fails "
                    "this check."))
    lines.append("  A repo archived on GitHub is exempt: it can no longer be changed.")
    width = max(len(i.name) for i in infos)
    for i in infos:
        mark = _COPY_MARK.get(i.copy, " ")
        moved = ("  floor moved since the pin" if i.floor_moved else "")
        exempt = ("  archived, exempt" if copy_would_block(i) and i.archived is True else "")
        lines.append(f"   {mark} {i.name:<{width}}  {i.copy:<12}{moved}{exempt}")
        if i.copy_detail and (i.copy in COPY_BLOCKING_STATES
                              or i.copy in (COPY_SKIPPED, COPY_UNCHECKED)):
            lines.append(f"       {i.copy_detail[:240]}")
        if blocking and copy_would_block(i) and i.archived is None and i.archive_checked:
            lines.append("       archive state not established (no GitHub remote, gh or "
                         "network), so this repo is not exempt")
    differ = [i for i in infos if i.copy == COPY_DRIFT]
    other = [i for i in infos if i.copy in COPY_BLOCKING_STATES and i.copy != COPY_DRIFT]
    exempt_n = [i for i in infos if copy_would_block(i) and i.archived is True]
    not_compared = [i for i in infos if i.copy in (COPY_SKIPPED, COPY_UNCHECKED)]
    lines.append(f"  {len(differ)} of {len(infos)} copies differ"
                 + (f" — {'failing now' if blocking else 'they would fail from ' + when}"
                    if differ else "") + ".")
    if other:
        lines.append(
            f"  {len(other)} more cannot be compared because they are unstamped, "
            "malformed or pin a commit with no floor text"
            + (f" — {'failing now' if blocking else 'they would fail from ' + when}"
               " unless archived") + ".")
    if exempt_n:
        lines.append(f"  {len(exempt_n)} exempt as archived.")
    if not_compared:
        lines.append(f"  {len(not_compared)} not compared (a skip marker, or CLAUDE.md "
                     "unreadable), which never fail.")
    return lines


def render(infos: list[ChildPin], atelier: Path, head: str, want_log: bool,
          roots: list[Path] | None = None, ref: str = "HEAD",
          today: datetime.date | None = None) -> str:
    lines = [f"atelier fleet pins  ({ref} {head[:7]}  {atelier})"]
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
    lines.extend(render_copy(infos, today))
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="pins",
        description="Fleet view of child-repo atelier pins — who is stale, by how much.")
    ap.add_argument("--atelier", help="atelier repo path (default: the repo this script lives in)")
    ap.add_argument("--root", action="append",
                    help="search root for discovery (repeatable; default: "
                         "ATELIER_ESTATE_ROOT, else atelier's parent dir)")
    ap.add_argument("--child", action="append",
                    help="report only this child repo (repeatable; bypasses discovery)")
    ap.add_argument("--log", action="store_true",
                    help="also print the commits each stale child would inspect")
    ap.add_argument("--head", action="store_true",
                    help="measure against the local checkout's HEAD, offline, "
                         "instead of fetching and using origin/main")
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
