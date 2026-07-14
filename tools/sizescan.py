#!/usr/bin/env python3
"""sizescan — the signal that a current-truth file has quietly bloated.

The operating model assumes a session resumes *cold* by reading a handful of
files at the start: the roadmap (what's open), the session index (where the last
one stopped), the README, the architecture note. That only stays cheap if those
files stay lean. RECORD.md already prescribes the fix — a **current-truth /
history split**: `ROADMAP.md` holds what's open and completed detail moves to
`ROADMAP-DONE.md`; `SESSIONS.md` is a one-line-per-session index and detail lives
in `docs/sessions/`; specs live in a grepped-on-demand `SPECS.md`. The split
works — but nothing *triggered* it. The session log got split once, by hand, and
the discipline then decayed silently: a roadmap grew past three thousand lines,
each finished item accreting a running log of how it got done, and no signal
fired. sizescan is that missing signal.

It measures the one thing that matters for the always-loaded surface — **length**
(a line count, a cheap honest proxy for the tokens a session pays to load the
file) — and reports any *current-truth* file over its budget. It is deliberately
narrow in two directions:

  * It budgets only the files that are **supposed to stay lean** — the
    session-start reads and current-truth docs (`ROADMAP.md`, `SESSIONS.md`,
    `README.md`, `ARCHITECTURE.md`, `CLAUDE.md`). A long *reference* doc
    (`PRINCIPLES.md`, a doctrine file) is not bloat — it is read on demand, not
    every session — so it is not budgeted.

  * It **ignores the append-only stores by design** — `ROADMAP-DONE.md`,
    `CHANGELOG.md`, `SPECS.md`, and everything under `sessions/`, `reviews/`,
    `decisions/`, and archive dirs. Those are the *destinations* the split moves
    detail into; they are meant to grow. Flagging them would punish the very fix
    the tool exists to encourage.

Advisory by default. Bloat is a recoverable hygiene threshold, not a defect like
a leaked secret or a 404 pointer — the fix (harvest the completed detail aside)
is a judgement call a session makes at a good moment, not a hard stop on every
commit. So a bare `sizescan` **reports and exits 0**: drop it in CI to surface
the numbers without ever breaking a build. `--check` is the opt-in gate — it
exits 1 when any budgeted file is over, for a repo that wants teeth once the tool
is reviewed. (It is NOT wired into any gate yet — see tools/README.md.)

Budgets are starting points, not law. A file that is legitimately long can
declare its own ceiling inline with `sizescan:budget=N`, or opt out entirely with
`sizescan:allow` or a glob in `.sizescanignore` — the same self-documenting,
greppable hatches the other scans use.

Exit codes (fail-safe — anything but a clean/advisory run is non-zero):
  0  clean, OR over budget in advisory mode (the default — a report, not a gate)
  1  over budget AND --check was given (the opt-in gate)
  2  usage / config error (a scan that read nothing is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can run
it with the system python3 and no install — and CI needs nothing but Python.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

# A file carrying this marker anywhere is exempt from the budget entirely (e.g. a
# repo that deliberately keeps a flat session log rather than an index). Keep the
# reason on the same line so the exemption is self-documenting and greppable.
ALLOW_MARKER = "sizescan:allow"

# An inline per-file budget override: `sizescan:budget=400` (or `: 400`, or a
# space). Lets a legitimately long current-truth file state its own ceiling
# instead of opting out wholesale — the honest middle between the default and
# `sizescan:allow`.
_BUDGET_MARKER = re.compile(r"sizescan:budget\s*[=:]?\s*(\d+)")

# The current-truth files that must stay lean, and the line budget each starts
# with. Keyed by exact basename. These are the files a session loads at start or
# leans on as "what's true / open now"; a reference doc read on demand is not
# here by design. Numbers are deliberately round and generous — the value is the
# *signal plus the override*, not a precisely tuned threshold. Ground: across the
# fleet the healthy instances of each sit well under these (session-index ~74,
# small-repo roadmaps 120-240); the bloated ones (a 3000-line roadmap, a
# 1100-line flat session log) clear them by a wide margin.
DEFAULT_BUDGETS = {
    "ROADMAP.md": 300,        # open + prioritised only; done detail → ROADMAP-DONE.md
    "SESSIONS.md": 250,       # one line per session; detail → docs/sessions/
    "README.md": 250,
    "ARCHITECTURE.md": 250,
    "CLAUDE.md": 200,
}

# `README.md` and `CLAUDE.md` are current-truth only at the **repo root** — the
# front door and the session onramp. A nested `tools/README.md` or
# `docs/decisions/README.md` is a reference index, read on demand, and budgeting
# it would dilute the signal. The other budgeted names are singular by
# convention (one ROADMAP, one SESSIONS index per repo) so they're budgeted
# wherever they live — root or `docs/`.
ROOT_ONLY = {"README.md", "CLAUDE.md"}

# Where completed / append-only detail is *meant* to accumulate — never budgeted.
# `ROADMAP-DONE.md`, `CHANGELOG.md`, `SPECS.md` fall out naturally (their
# basenames aren't in DEFAULT_BUDGETS); these path components catch a budgeted
# basename that lives inside a growth store (an `ARCHITECTURE.md` snapshotted
# under `_archive/`, a `README.md` inside `reviews/`).
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache", ".idea",
                  ".vscode", "sessions", "reviews", "decisions",
                  "_archive", "archive", "intake"}


@dataclass
class Finding:
    path: str          # the over-budget file, repo-relative
    lines: int         # its actual line count
    budget: int        # the budget it exceeded
    over: int          # lines - budget
    store: str         # where its completed/history detail should move


# The harvest hint per current-truth file — where its overflow belongs, so the
# report points at the fix, not just the symptom.
_STORE_HINT = {
    "ROADMAP.md": "harvest completed items to ROADMAP-DONE.md (keep only what's open)",
    "SESSIONS.md": "move to a one-line-per-session index + docs/sessions/ detail files",
    "README.md": "move depth to docs/ (ARCHITECTURE.md, a guide) and point to it",
    "ARCHITECTURE.md": "split by subsystem or move detail to a design doc",
    "CLAUDE.md": "point to docs/ for detail; the onramp stays a thin index",
}


def budget_for(text: str, basename: str) -> int | None:
    """The budget this file is held to, or None if it isn't budgeted. An inline
    `sizescan:budget=N` overrides the default for a legitimately long file."""
    m = _BUDGET_MARKER.search(text)
    if m:
        return int(m.group(1))
    return DEFAULT_BUDGETS.get(basename)


def count_lines(text: str) -> int:
    """Line count, newline-agnostic and not fooled by a trailing newline (a file
    ending in "\\n" is not one line longer than the same file without it)."""
    if not text:
        return 0
    return len(text.splitlines())


def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".sizescanignore"
    if not f.exists():
        return []
    globs: list[str] = []
    for raw in f.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            globs.append(line)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


def iter_candidates(paths: list[Path], root: Path, globs: list[str]):
    """Yield budgeted files under the given paths, skipping growth stores and
    ignored globs. A file is a candidate iff its basename is budgeted."""
    for base in paths:
        if base.is_file():
            candidates = [base]
        else:
            candidates = [p for p in base.rglob("*")
                          if p.is_file() and not (SKIP_DIR_NAMES & set(p.parts))]
        for p in candidates:
            if p.name not in DEFAULT_BUDGETS:
                continue
            if SKIP_DIR_NAMES & set(p.parts):
                continue
            if p.name in ROOT_ONLY and p.resolve().parent != root.resolve():
                continue
            if _ignored(_rel(p, root), globs):
                continue
            yield p


def scan_paths(paths: list[Path], root: Path) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p in iter_candidates(paths, root, globs):
        text = p.read_text(encoding="utf-8", errors="replace")
        if ALLOW_MARKER in text:
            continue
        budget = budget_for(text, p.name)
        if budget is None:
            continue
        n = count_lines(text)
        if n > budget:
            findings.append(Finding(_rel(p, root), n, budget, n - budget,
                                    _STORE_HINT.get(p.name, "")))
    return findings


def render_human(findings: list[Finding]) -> str:
    if not findings:
        return "✓ sizescan clean — every current-truth file within budget."
    lines = [f"⚠ sizescan: {len(findings)} current-truth file(s) over budget "
             "(advisory — the split doctrine wants these lean).\n"]
    for f in sorted(findings, key=lambda x: -x.over):
        lines.append(f"  {f.path}  {f.lines} lines (budget {f.budget}, +{f.over})")
        if f.store:
            lines.append(f"      → {f.store}")
    lines.append("\n  Fix: harvest the overflow to its on-demand store (RECORD.md, "
                 "the current-truth/history split).")
    lines.append(f"  Legitimately long: add 'sizescan:budget=N' inline, "
                 f"'{ALLOW_MARKER}' to exempt, or a glob in .sizescanignore.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="sizescan",
        description="Flag current-truth files (roadmap, session index, README…) "
                    "that have grown past their budget.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo)")
    ap.add_argument("--root", default=".",
                    help="repo root for .sizescanignore and relative paths")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if any file is over budget (opt-in gate; "
                         "default is advisory, exit 0)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"sizescan: root does not exist: {args.root}", file=sys.stderr)
        return 2
    targets = [Path(p) for p in (args.paths or [str(root)])]
    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        # A typo'd path scanning nothing must never read as a clean pass.
        print(f"sizescan: path does not exist: {', '.join(missing)}", file=sys.stderr)
        return 2
    try:
        findings = scan_paths(targets, root)
    except OSError as e:
        print(f"sizescan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        print(render_human(findings))

    # Advisory by default: over-budget is a report, not a failure. --check gives
    # it teeth for a repo that opts in.
    return 1 if (findings and args.check) else 0


def _selftest() -> int:
    """Minimal smoke test so `sizescan --selftest` proves the engine on any box,
    even where the unittest file isn't shipped. Builds a tiny tree and asserts
    the core behaviours: budgeted-and-over flags, budgeted-and-under passes,
    growth stores and reference docs are ignored, and the inline override wins."""
    import tempfile
    import shutil

    tmp = Path(tempfile.mkdtemp(prefix="sizescan-self-"))
    docs = tmp / "docs"
    docs.mkdir()
    (docs / "sessions").mkdir()

    over = "x\n" * (DEFAULT_BUDGETS["ROADMAP.md"] + 5)   # over every default budget
    under = "x\n" * (min(DEFAULT_BUDGETS.values()) - 5)  # under every default budget
    (docs / "ROADMAP.md").write_text(over)                       # BUDGETED, over → flag
    (docs / "ROADMAP-DONE.md").write_text(over)                  # growth store → ignore
    (docs / "SPECS.md").write_text(over)                         # on-demand → ignore
    (tmp / "CHANGELOG.md").write_text(over)                      # append-only → ignore
    (tmp / "PRINCIPLES.md").write_text(over)                     # reference doc → not budgeted
    (docs / "sessions" / "SESSIONS.md").write_text(over)         # inside a store → ignore
    (tmp / "README.md").write_text(under)                        # root README, under → pass
    (tmp / "tools").mkdir()
    (tmp / "tools" / "README.md").write_text(over)               # nested README → not budgeted
    # inline override lifts a legitimately long file above default
    (tmp / "ARCHITECTURE.md").write_text("sizescan:budget=100000\n" + over)

    findings = scan_paths([tmp], tmp)
    flagged = sorted(f.path.replace("\\", "/") for f in findings)
    expected = ["docs/ROADMAP.md"]
    ok = flagged == expected
    if not ok:
        print(f"FAIL: flagged {flagged}, expected {expected}")

    # allow-marker exempts a would-be-flagged file
    (docs / "ROADMAP.md").write_text(f"<!-- {ALLOW_MARKER}: living doc -->\n" + over)
    if any(f.path.replace("\\", "/") == "docs/ROADMAP.md" for f in scan_paths([tmp], tmp)):
        print("FAIL: allow-marker did not exempt")
        ok = False

    # count_lines: trailing newline doesn't inflate the count
    if count_lines("a\nb\n") != 2 or count_lines("a\nb") != 2:
        print("FAIL: count_lines mishandles trailing newline")
        ok = False

    # budget_for: inline override beats the default; unbudgeted basename is None
    if budget_for("sizescan:budget=42\n", "ROADMAP.md") != 42:
        print("FAIL: inline budget override not honoured")
        ok = False
    if budget_for("body\n", "PRINCIPLES.md") is not None:
        print("FAIL: non-current-truth basename should not be budgeted")
        ok = False

    print("selftest OK" if ok else "selftest FAILED")
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
