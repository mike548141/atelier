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
a leaked secret or a 404 pointer — so a bare `sizescan` **reports and exits 0**:
drop it in CI to surface the numbers without ever breaking a build. `--check` is
the opt-in gate. Reviewed 2026-07-14 (cold, PASS-WITH-FINDINGS) and wired in
`--check` mode into atelier's `ci.yml` and the child `floor.yml` template.

**A budget is a tripwire, never a target** (Mike's ruling, 2026-07-19). Crossing
one should summon judgement; it must never make trimming-to-the-number the work.
The gate therefore splits by **remedy class**:

  * `ROADMAP.md` and `SESSIONS.md` **gate** under `--check`. Their remedy is
    **lossless relocation** — harvest done items to `ROADMAP-DONE.md`, rotate
    older index entries to `SESSIONS-ARCHIVE.md` — so in the overwhelming case
    a red demands a move, not rewording, and the gate can have teeth because
    obeying it cannot damage content. The honest edge (2026-07-19 cold-pass
    F5): a file that is legitimately **all-current** — a roadmap of wholly open
    items — has nothing to relocate; there the sanctioned remedies are a
    class-grounded declared budget or a standing red, never trimming a true
    signal (the all-open-roadmap case, 2026-07-18).
  * `README.md`, `ARCHITECTURE.md`, `CLAUDE.md` are **advisory-only, always** —
    reported, never gate-failing, even under `--check`. Their remedy is
    editorial judgement, and a hard number on a judgement doc induces line-golf:
    the observed failure (2026-07-18) was source made *worse* — a wrapped bullet
    merged into one over-long line — purely to hit a round number.
    "Well-described" outranks any count.

The signal is also **one-sided by design**: nothing here flags a too-thin file.
A hollow ARCHITECTURE.md is the worse defect — it lies by omission — but
thinness is a judgement caught at review under the stub-honestly rule
(`00-APEX.md`), never measured; a numeric floor would be the same
target-not-tripwire trap mirrored.

Budgets are starting points, not law. A file that is legitimately long can
declare its own ceiling in its **header** (the first 15 lines) with
`sizescan:budget=N`, or opt out entirely with `sizescan:allow` or a glob in
`.sizescanignore`. Markers are read only in the header, never the body — a
budgeted file that merely *mentions* a marker in prose does not silently exempt
itself (the reviewer's F2).

**A declared budget must be GROUNDED, and must not be derived from the file's
current length.** The defaults earn their place as grounded heuristics (healthy
files across the fleet sit well under them; the offenders clear them by
multiples) — the 2026-07-14 cold review's standard. A number picked to sit just
above what the file happens to weigh today is circular: it can't be exceeded at
the moment it's written and says nothing about what the file *should* be. That
same review weighed raising a budget as a remedy and ruled it **"defers the
collision, doesn't resolve it"**. So: fix the file, or state grounds that are a
property of its *class* (e.g. "a generated table with one row per device").
If neither is honest, leave it red — a true signal beats a silenced one.
*(Grounded 2026-07-18: a session declared a budget of 320 on a 319-line file; the
principal caught it. The rule existed in the review verdict but not here, where
it would have been read.)*

Exit codes (fail-safe — anything but a clean/advisory run is non-zero):
  0  clean; over budget in advisory mode; or only advisory-class files over
     under --check (judgement docs never fail the build)
  1  a GATED file (ROADMAP/SESSIONS) over budget AND --check was given
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

# A file whose HEADER carries this marker is exempt from the budget entirely
# (e.g. a repo that deliberately keeps a flat session log rather than an index).
# Keep the reason on the same line so the exemption is self-documenting.
ALLOW_MARKER = "sizescan:allow"

# A per-file budget override in the HEADER: `sizescan:budget=400` (or `: 400`, or
# a space). Lets a legitimately long current-truth file state its own ceiling
# instead of opting out wholesale — the honest middle between the default and
# `sizescan:allow`.
_BUDGET_MARKER = re.compile(r"sizescan:budget\s*[=:]?\s*(\d+)")

# Markers are honoured ONLY in the file's header — the first MARKER_SCAN_LINES
# lines — never in the body. Matching anywhere let a budgeted file that merely
# *mentions* a marker in prose (a roadmap item about budgets, a doc of the hatch)
# silently exempt or re-budget itself (F2), a per-file blast radius blunter than
# the sibling scanners' per-line allows. A real exemption is a deliberate
# declaration at the top of the file, where a reader meets it first.
MARKER_SCAN_LINES = 15


def _header(text: str) -> str:
    return "\n".join(text.splitlines()[:MARKER_SCAN_LINES])

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

# The files whose over-budget finding FAILS a `--check` run. Only the two whose
# remedy is lossless relocation (harvest / rotate) — obeying the gate can never
# damage content. The judgement docs (README/ARCHITECTURE/CLAUDE) stay
# advisory-only even under --check: their remedy is editorial, and a hard number
# there turns the signal into a target (Mike's tripwire-not-target ruling,
# 2026-07-19; see the module docstring).
GATED = {"ROADMAP.md", "SESSIONS.md"}

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
    gated: bool        # True = fails --check (lossless remedy); False = advisory


# The harvest hint per current-truth file — where its overflow belongs, so the
# report points at the fix, not just the symptom.
_STORE_HINT = {
    "ROADMAP.md": "harvest completed items to ROADMAP-DONE.md (keep only what's open)",
    "SESSIONS.md": "if a flat log, split to an index + docs/sessions/ detail; if "
                   "already an index, rotate older entries to SESSIONS-ARCHIVE.md "
                   "(keep the recent tail)",
    "README.md": "move depth to docs/ (ARCHITECTURE.md, a guide) and point to it",
    "ARCHITECTURE.md": "split by subsystem or move detail to a design doc",
    "CLAUDE.md": "point to docs/ for detail; the onramp stays a thin index",
}


def budget_for(text: str, basename: str) -> int | None:
    """The budget this file is held to, or None if it isn't budgeted. A header
    `sizescan:budget=N` overrides the default for a legitimately long file."""
    m = _BUDGET_MARKER.search(_header(text))
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


def _in_skipped_dir(p: Path, walk_base: Path) -> bool:
    """Is p inside a growth-store directory *within the scanned tree*? The skip
    names are matched against the path **relative to the scan base**, never the
    absolute path. Matching absolute parts was a fail-open bug (F1): a repo that
    merely *lives under* an ancestor named `archive`/`sessions`/`reviews`/… — the
    store names are ordinary English words — had every file skipped, so the scan
    read nothing and reported "clean", the exact contract violation the tool's
    own exit codes forbid ("a scan that read nothing is NOT a pass")."""
    try:
        rel_parts = p.relative_to(walk_base).parts
    except ValueError:
        rel_parts = (p.name,)
    return bool(SKIP_DIR_NAMES & set(rel_parts[:-1]))   # intermediate dirs only


def iter_candidates(paths: list[Path], root: Path, globs: list[str]):
    """Yield budgeted files under the given paths, skipping growth stores and
    ignored globs. A file is a candidate iff its basename is budgeted. Results are
    de-duplicated by resolved path so overlapping args (`sizescan . docs`) don't
    double-report the same file (F4)."""
    seen: set[Path] = set()
    for base in paths:
        base = base.resolve()
        walk_base = base if base.is_dir() else base.parent
        candidates = [base] if base.is_file() else [
            p for p in base.rglob("*") if p.is_file()]
        for p in candidates:
            rp = p.resolve()
            if rp in seen or p.name not in DEFAULT_BUDGETS:
                continue
            if _in_skipped_dir(p, walk_base):
                continue
            if p.name in ROOT_ONLY and rp.parent != root.resolve():
                continue
            if _ignored(_rel(p, root), globs):
                continue
            seen.add(rp)
            yield p


def scan_paths(paths: list[Path], root: Path) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p in iter_candidates(paths, root, globs):
        text = p.read_text(encoding="utf-8", errors="replace")
        if ALLOW_MARKER in _header(text):
            continue
        budget = budget_for(text, p.name)
        if budget is None:
            continue
        n = count_lines(text)
        if n > budget:
            findings.append(Finding(_rel(p, root), n, budget, n - budget,
                                    _STORE_HINT.get(p.name, ""),
                                    p.name in GATED))
    return findings


def render_human(findings: list[Finding]) -> str:
    if not findings:
        return "✓ sizescan clean — every current-truth file within budget."
    n_gated = sum(1 for f in findings if f.gated)
    n_adv = len(findings) - n_gated
    head = (f"⚠ sizescan: {len(findings)} current-truth file(s) over budget "
            f"({n_gated} gated · {n_adv} advisory).\n")
    lines = [head]
    for f in sorted(findings, key=lambda x: (not x.gated, -x.over)):
        cls = "gate" if f.gated else "advisory"
        lines.append(f"  {f.path}  {f.lines} lines (budget {f.budget}, "
                     f"+{f.over}) [{cls}]")
        if f.store:
            lines.append(f"      → {f.store}")
    if n_gated:
        lines.append("\n  Gated (fails --check): the remedy is lossless relocation "
                     "(RECORD.md, the current-truth/history split) — move detail, "
                     "never reword to fit.")
    if n_adv:
        lines.append("\n  Advisory (never fails --check): a judgement doc — the "
                     "number summons a look; well-described outranks any count. "
                     "Trim only where content is misplaced or duplicated.")
    lines.append(f"  Legitimately long: declare 'sizescan:budget=N' in the file's "
                 f"first {MARKER_SCAN_LINES} lines (GROUNDED in the file's class, "
                 f"never its current length — see the module doc), "
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
                    help="exit 1 if a GATED file (ROADMAP/SESSIONS — lossless "
                         "remedy) is over budget; judgement docs stay advisory "
                         "(default: everything advisory, exit 0)")
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
    # it teeth for a repo that opts in — but only for the GATED files, whose
    # remedy is lossless relocation. A judgement doc can never fail the build
    # (tripwire, not target).
    return 1 if (args.check and any(f.gated for f in findings)) else 0


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

    # F1: a repo living UNDER a store-named ancestor must still be scanned (the
    # absolute-path skip check silently blanked the whole scan and reported clean)
    anc = tmp / "archive" / "child"
    (anc / "docs").mkdir(parents=True)
    (anc / "docs" / "ROADMAP.md").write_text(over)
    f1 = scan_paths([anc], anc)
    if not any(f.path.replace("\\", "/") == "docs/ROADMAP.md" for f in f1):
        print("FAIL: F1 — repo under a store-named ancestor was skipped (fail-open)")
        ok = False

    # F2: a marker only *mentioned* in the body (below the header) must NOT exempt
    body_mention = ("t\n" * 20) + f"discussion of {ALLOW_MARKER} and budgets\n" + over
    (tmp / "F2").mkdir()
    (tmp / "F2" / "ROADMAP.md").write_text(body_mention)
    if not any(f.path.replace("\\", "/") == "ROADMAP.md"
               for f in scan_paths([tmp / "F2"], tmp / "F2")):
        print("FAIL: F2 — a body-only marker mention silently exempted the file")
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

    # Gate split: ROADMAP findings are gated, ARCHITECTURE findings advisory —
    # and only gated findings carry --check teeth (tripwire-not-target ruling).
    gt = tmp / "gatesplit"
    (gt / "docs").mkdir(parents=True)
    (gt / "docs" / "ROADMAP.md").write_text(over)
    (gt / "ARCHITECTURE.md").write_text(over)
    gf = {f.path.replace("\\", "/"): f.gated for f in scan_paths([gt], gt)}
    if gf.get("docs/ROADMAP.md") is not True or gf.get("ARCHITECTURE.md") is not False:
        print(f"FAIL: gate split wrong: {gf}")
        ok = False

    print("selftest OK" if ok else "selftest FAILED")
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
