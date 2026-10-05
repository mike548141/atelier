"""The single-sourced exit-code contract and common report lines shared by the
floor scanners (`115/080`, part 3).

Before this module every scanner spelled its own copy of the same contract:

  * the exit codes — 0 nothing blocking, 1 blocking findings, 2 the scan
    itself is broken (a broken scan is not a pass);
  * the `main()` wrapper that turns a config error (an unreasoned ignore
    glob, an unusable declaration) into one stderr line and exit 2 — eleven
    textually identical copies;
  * the exit-2 stderr lines for a missing root, a missing path, an unreadable
    file, a failed `git diff` and an absolute `--staged` path;
  * the rule-(b) tally line (`  suppressed: a · b · c`, its allow-marker
    breakdown and its disabled-rules line), the finding-cap part and the
    over-cap list line;
  * the `(--warn: advisory only …)` notice that `floor.py` names as the
    estate-wide spelling.

WHAT THIS MODULE DELIBERATELY DOES NOT DO: unify behaviour or wording. Every
difference between the scanners is a PARAMETER here — the scanner's name, the
tally's parts, the finding noun, a head line's tail, the over-cap indent, the
example path in the `--staged` refusal, which exception classes count as
config errors — never a default a scanner can drift into. A scanner whose line
genuinely differs (leakscan's clean head, indexscan's over-cap line, the `⚠`
heads of the advisory-by-construction checks) keeps its own spelling.

`tools/test_report.py` tests each helper against literal strings, and pins the
lines each converted scanner prints, so a shared edit that changes any one
scanner's output fails loudly.

What the scanners print is a contract with every child: they run atelier's
floor at `main`, so a change to a string here reaches every child's CI at its
next run.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable, Iterable, Sequence

# The house exit-code contract.
EXIT_CLEAN = 0      # nothing blocking (clean, advisory-only, or --warn)
EXIT_FINDINGS = 1   # blocking findings
EXIT_BROKEN = 2     # the scan itself is broken — never read as a pass

# Printed after the report when findings exist under --warn. `floor.py`'s
# `WARN_MODE_FLAGS` comment names this as the estate-wide spelling.
WARN_NOTICE = "\n  (--warn: advisory only — not blocking this build.)"


def exit_code(blocking: object, *, warn: bool = False) -> int:
    """0 or 1 from the truthiness of `blocking` (a count, a list or a bool);
    always 0 under `warn`. Exit 2 is never computed here — it is returned by
    `broken` at the point the scan finds it cannot be trusted."""
    if warn:
        return EXIT_CLEAN
    return EXIT_FINDINGS if blocking else EXIT_CLEAN


def broken(name: str, message: str) -> int:
    """Print `<name>: <message>` to stderr and return exit 2."""
    print(f"{name}: {message}", file=sys.stderr)
    return EXIT_BROKEN


def guarded_main(name: str, run: Callable[[list[str] | None], int],
                 argv: list[str] | None,
                 config_errors: tuple[type[BaseException], ...]) -> int:
    """Run a scanner's `_main`, turning any of `config_errors` into exit 2.
    An unexplained exemption or an unusable declaration makes the scan's own
    scope untrustworthy, so it is a broken scan, not a pass."""
    try:
        return run(argv)
    except config_errors as e:
        return broken(name, str(e))


def resolve_targets(root: Path, paths: Iterable[str]) -> list[Path]:
    """Each path as given if absolute, else under `root` — never the caller's
    cwd: mixing the two reads one repo's file under another repo's rules
    (roadmap 010/110)."""
    return [(root / p) if not Path(p).is_absolute() else Path(p) for p in paths]


def refuse_missing_root(name: str, root: Path, raw: str) -> int | None:
    """Exit 2 (after one stderr line) if `root` is not a directory, else None."""
    if not root.is_dir():
        return broken(name, f"root does not exist: {raw}")
    return None


def refuse_missing_paths(name: str, targets: Sequence[Path]) -> int | None:
    """Exit 2 if any target does not exist, else None: a typo'd path that
    scans nothing must never read as a clean pass."""
    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        return broken(name, f"path does not exist: {', '.join(missing)}")
    return None


def cannot_read(name: str, e: OSError) -> int:
    """Exit 2 for a file the scan could not open."""
    return broken(name, f"cannot read {e.filename}: {e.strerror}")


def git_diff_failed(name: str, e: BaseException) -> int:
    """Exit 2 when the staged diff cannot be read."""
    return broken(name, f"git diff failed: {e}")


def refuse_absolute_staged(name: str, paths: Iterable[str],
                           example: str) -> int | None:
    """Exit 2 if any `--staged` path is absolute, else None. git lists staged
    paths repo-relative, so an absolute one matches nothing, the filter
    empties, and a scan that covered nothing would exit 0."""
    absolute = [p for p in paths if Path(p).is_absolute()]
    if absolute:
        return broken(
            name,
            f"--staged needs repo-relative path(s), got absolute: "
            f"{', '.join(absolute)}\n"
            "  git lists staged paths relative to the repo root, so an "
            "absolute path matches nothing\n"
            "  and the scan would pass while covering nothing. Pass e.g. "
            f"'{example}' instead.")
    return None


def clean_head(name: str, detail: str) -> str:
    """`✓ <name> clean — <detail>`."""
    return f"✓ {name} clean — {detail}"


def findings_head(name: str, count: int, noun: str = "finding(s)",
                  tail: str = ".") -> str:
    """`✗ <name>: <count> <noun><tail>` — the tail carries each guard's own
    consequence wording (` — commit blocked.`, ` (limit 80 columns).`)."""
    return f"✗ {name}: {count} {noun}{tail}"


def cap_part(over: int, cap: int) -> str:
    """The tally part counting findings past the materialisation cap."""
    return f"{over} beyond the {cap}-finding cap (counted, not listed)"


def over_cap_line(over: int, cap: int, *, noun: str = "finding(s)",
                  indent: str = "  ") -> str:
    """The list line standing in for findings counted but never built."""
    return (f"{indent}…and {over} more {noun}, counted but not listed "
            f"(past the {cap}-finding memory cap).")


def suppressed_line(parts: Sequence[str], *,
                    breakdown: dict[str, int] | None = None,
                    disabled: Sequence[str] = ()) -> str:
    """The rule-(b) tally: one stable line, known zeros printed, so two runs
    compare. `parts` is the scanner's own field list, in its own order (the
    order is part of its contract). The allow-marker breakdown and the
    disabled rules follow on their own lines, only when non-empty."""
    line = "  suppressed: " + " · ".join(parts)
    if breakdown:
        detail = ", ".join(f"{k}×{n}" for k, n in sorted(breakdown.items()))
        line += f"\n    allow-marker breakdown: {detail}"
    if disabled:
        line += f"\n    disabled: {', '.join(disabled)}"
    return line
