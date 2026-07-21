#!/usr/bin/env python3
"""reviewscan — the mechanical check that a decision record states its review
judgement.

REVIEW.md's remedy for the invisible-decline failure mode: where a repo records
design or direction durably, each record carries a review line — a queued
pointer, or an explicit `review: not warranted — <grounds>`. **Omission is the
bug**: a reviewer or the principal can disagree with a stated judgement; neither
can disagree with a blank. Until this tool existed the remedy was one more
written rule — the exact "read is not complied with" class it was written
against (2026-07-19 cold-pass F6). This is the structural half.

Scope, deliberately narrow (the 2026-07-18-0820 record's own grounds):

  * DECISION RECORDS only — files under a `docs/decisions/` directory named on
    the coordination-free scheme (`YYYY-MM-DD[-HHMM]-slug.md`). They are
    discrete, one-decision files, so "this record lacks the line" is a reliable
    mechanical fact.

  * ROADMAP sections are NOT linted, on purpose. A lint that demands a review
    line under every roadmap heading fires on prose and gets trained away —
    the 0820 record rejected that rung, and this tool honours the rejection.
    For those records the convention remains a convention; REVIEW.md states
    that honestly rather than letting this tool imply wider cover than it has.

  * PRESENCE only. The tool proves the line exists; whether its grounds are
    honest is judgement — the reviewer's and the principal's work, never a
    validator's (REVIEW.md: layers, not alternatives).

Adoption boundary — records dated before BOUNDARY are skipped. Decision records
are append-only once accepted (RECORD.md): retrofitting the field into frozen
records would rewrite history, so the lint binds from the day the templates
began prompting for the field. Same shape as floor.yml's SIGN_BOUNDARY — the
boundary is the mechanism's own landing date, not a number picked to pass.
Records named under the retired numeric scheme (`0001-…`) all predate the
convention and are skipped by construction (they carry no date to test).

A line carrying `reviewscan:allow: <reason>` anywhere in a record exempts it —
self-documenting and greppable, same hatch as the sibling scanners.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean
  1  record(s) missing the review line
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can
run it with the system python3 and no install — and CI needs nothing but
Python.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# The day the record templates began carrying the field (the artefact's landing
# date). Records frozen before it are blameless and append-only — see docstring.
BOUNDARY = "2026-07-21"

# `2026-07-21-0736-slug.md` or `2026-07-13-slug.md` (pre-HHMM records keep
# their names — retired-scheme files are never renamed).
RECORD_NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})(?:-\d{4})?-.+\.md$")

# `**Review**: …` (ADR header), `review: not warranted — …` (inline), a list
# bullet, or a blockquoted line all count — the field, not one typography.
REVIEW_LINE = re.compile(r"^[\s>*-]*(?:\*\*)?[Rr]eview(?:\*\*)?\s*:")

ALLOW_MARKER = "reviewscan:allow:"


def scan_record(path: Path) -> bool:
    """True if the record satisfies the rule (has the line, or is exempt)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    if ALLOW_MARKER in text:
        return True
    return any(REVIEW_LINE.match(line) for line in text.splitlines())


def find_records(paths: list[Path]) -> list[Path]:
    """Decision records in scope: docs/decisions/<date-named>.md, post-boundary."""
    records: list[Path] = []
    for base in paths:
        for decisions_dir in sorted(base.rglob("docs/decisions")):
            if not decisions_dir.is_dir():
                continue
            # A templates tree ships the *blank* forms, not records — skip it.
            if "templates" in decisions_dir.parts:
                continue
            for f in sorted(decisions_dir.glob("*.md")):
                m = RECORD_NAME.match(f.name)
                if m and m.group(1) >= BOUNDARY:
                    records.append(f)
    return records


def run(paths: list[Path], root: Path, as_json: bool) -> int:
    records = find_records(paths)
    failures = [r for r in records if not scan_record(r)]
    if as_json:
        print(json.dumps({
            "checked": [str(r.relative_to(root)) for r in records],
            "failures": [str(r.relative_to(root)) for r in failures],
        }, indent=2))
    elif failures:
        for r in failures:
            print(f"✗ {r.relative_to(root)} — no review line. Add one:")
        print()
        print("Every decision record states its review judgement (REVIEW.md):")
        print("  **Review**: queued — docs/reviews/<brief>.md")
        print("  **Review**: not warranted — <grounds>")
        print("Omission is the bug: a blank can't be disagreed with. A genuine")
        print(f"exception carries `{ALLOW_MARKER} <reason>` on a line.")
    else:
        n = len(records)
        print(f"✓ reviewscan clean — {n} post-{BOUNDARY} decision record(s) "
              "carry a review line.")
    return 1 if failures else 0


def selftest() -> int:
    """Prove the tool detects its own fixtures — red and green legs."""
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        d = Path(td) / "docs" / "decisions"
        d.mkdir(parents=True)
        (d / "2026-07-25-1200-good.md").write_text(
            "# Good\n\n**Status**: draft • **Date**: 2026-07-25\n"
            "**Review**: not warranted — records-only edit\n")
        (d / "2026-07-25-1300-bad.md").write_text(
            "# Bad\n\n**Status**: draft • **Date**: 2026-07-25\n")
        (d / "2026-07-15-0900-frozen.md").write_text(
            "# Pre-boundary, frozen — must be skipped\n")
        (d / "0001-numeric-scheme.md").write_text(
            "# Retired scheme — must be skipped\n")
        (d / "README.md").write_text("# Not a record\n")
        (d / "2026-07-25-1400-exempt.md").write_text(
            "# Exempt\n<!-- reviewscan:allow: selftest fixture -->\n")
        tpl = Path(td) / "docs" / "build" / "templates" / "docs" / "decisions"
        tpl.mkdir(parents=True)
        (tpl / "2026-07-25-1500-shipped-example.md").write_text(
            "# A dated example inside a templates tree — must be skipped\n")

        records = find_records([Path(td)])
        failures = [r.name for r in records if not scan_record(r)]
        ok = (sorted(r.name for r in records) == [
                  "2026-07-25-1200-good.md", "2026-07-25-1300-bad.md",
                  "2026-07-25-1400-exempt.md"]
              and failures == ["2026-07-25-1300-bad.md"])
        print("reviewscan selftest:", "OK" if ok else "FAILED")
        if not ok:
            print("  in scope:", sorted(r.name for r in records))
            print("  failures:", failures)
        return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="check decision records carry a review line (REVIEW.md)")
    ap.add_argument("paths", nargs="*",
                    help="files or directories to scan (default: --root)")
    ap.add_argument("--root", default=".",
                    help="repo root, for relative reporting (default: .)")
    ap.add_argument("--json", action="store_true",
                    help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the tool against its own fixtures, then exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"reviewscan: --root {args.root} is not a directory",
              file=sys.stderr)
        return 2
    paths = [Path(p).resolve() for p in (args.paths or [args.root])]
    for p in paths:
        if not p.exists():
            print(f"reviewscan: {p} does not exist", file=sys.stderr)
            return 2
    return run(paths, root, args.json)


if __name__ == "__main__":
    sys.exit(main())
