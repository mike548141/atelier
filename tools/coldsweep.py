#!/usr/bin/env python3
"""coldsweep — the tree search a cold reviewer runs, with rule 2's bar built in.

THE DEFECT THIS EXISTS FOR (the principal's ruling, 2026-08-17, after the third
instance). A rule-4 cold reviewer must not read the author's records — the
session log, the session records, the harvested board, prior verdicts — because
the author's account of the work is exactly what a cold pass is meant to be
formed without (`REVIEW.md` rule 2). Reviewers were told to exclude those paths
and did try. Three times the exclusion silently did not apply, most often
because the pattern assumed a `./` prefix that `grep -r <dir>` does not emit, so
`--exclude-dir=./docs/sessions` matched nothing and the sweep ran wide open. The
reviewer then formed findings while holding the author's framing, and in the
worst case held a prior verdict's findings before writing its own.

The rule was restated after each instance. Three instances in, restatement is
measurably not the fix — so the exclusion becomes the DEFAULT and the wide sweep
becomes the exception you have to ask for by name.

WHY IT DOES NOT SHELL OUT TO GREP. The defect was never in the reviewer's care;
it was in matching a path by string prefix against output whose prefix is a
platform detail. This tool walks the tree with `pathlib` and filters on the
RELATIVE PATH PARTS, which have no prefix to get wrong. `./docs/sessions`,
`docs/sessions`, `docs/sessions/` and an absolute root all resolve to the same
exclusion because none of them is ever compared as text.

WHAT IT IS NOT. Not a floor check, and deliberately not in the registry: it
gates no commit and has no verdict. It is a reviewer's instrument, and its whole
value is being the path of least resistance at the moment a reviewer wants to
search. A guard that makes the safe thing easier is doing the same work as one
that makes the unsafe thing fail — see `GUARDS.md`.

USAGE

    python3 tools/coldsweep.py 'PATTERN'                # the barred set excluded
    python3 tools/coldsweep.py -i 'pattern'             # case-insensitive
    python3 tools/coldsweep.py --also-exclude docs/roadmap/160-x 'PATTERN'
    python3 tools/coldsweep.py --list-barred            # what would be excluded
    python3 tools/coldsweep.py --include-barred 'PAT'   # the exception, loudly

Exit codes follow grep so it drops into a pipeline: 0 matched, 1 no match,
2 the search itself failed. A broken sweep is not a clean one.

DISCLOSURE. Every run prints the exclusion set it used, in a form that can be
pasted into a verdict's provenance. `--include-barred` prints a banner saying
the reviewer must disclose the exposure, because under rule 2 a wide sweep is
not forbidden — an *undisclosed* one is.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# REVIEW.md rule 2's barred set, as paths relative to the repo root. These are
# the author's account of the work — history written for the next session's
# agent, and prior verdicts whose framing is the contamination rule 2 exists to
# prevent. Kept as a tuple of path STRINGS and split into parts at use, never
# matched as text against a search result.
BARRED = (
    "docs/SESSIONS.md",
    "docs/sessions",
    "docs/ROADMAP-DONE.md",
    "docs/reviews",
)

# Never worth searching and never worth the noise of excluding by hand.
NOISE = (".git", "node_modules", "__pycache__", ".venv")

BINARY_HINT = b"\x00"


def _parts(rel: str) -> tuple[str, ...]:
    """Path text → comparable parts. The whole point of the tool.

    Accepts `./a/b`, `a/b`, `a/b/`, `a//b` and an absolute path under the root,
    and yields the same parts for all of them, because a prefix that only
    sometimes appears is what broke this three times.
    """
    return tuple(p for p in Path(rel).parts if p not in (".", "/", ""))


def is_barred(rel: Path, barred: tuple[str, ...]) -> str | None:
    """The barred entry that covers `rel`, or None.

    A file is barred if a barred path IS it or is one of its ancestors.
    Compared parts-wise, so no prefix spelling can make the bar miss.
    """
    rel_parts = rel.parts
    for entry in barred:
        ep = _parts(entry)
        if not ep:
            continue
        if rel_parts[: len(ep)] == ep:
            return entry
    return None


def walk(root: Path, barred: tuple[str, ...]) -> tuple[list[Path], list[Path]]:
    """(searchable files, barred files) — both as paths relative to root."""
    kept: list[Path] = []
    skipped: list[Path] = []
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.is_symlink():
            continue
        rel = p.relative_to(root)
        if any(part in NOISE for part in rel.parts):
            continue
        (skipped if is_barred(rel, barred) else kept).append(rel)
    return kept, skipped


def search(root: Path, pattern: str, files: list[Path],
           ignore_case: bool) -> list[tuple[Path, int, str]]:
    flags = re.IGNORECASE if ignore_case else 0
    rx = re.compile(pattern, flags)
    hits: list[tuple[Path, int, str]] = []
    for rel in files:
        try:
            raw = (root / rel).read_bytes()
        except OSError:
            continue
        if BINARY_HINT in raw[:8192]:
            continue
        text = raw.decode("utf-8", errors="replace")
        for n, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                hits.append((rel, n, line.rstrip()))
    return hits


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="coldsweep",
        description="tree search with REVIEW.md rule 2's barred paths excluded")
    ap.add_argument("pattern", nargs="?", help="Python regex to search for")
    ap.add_argument("--root", default=".")
    ap.add_argument("-i", "--ignore-case", action="store_true")
    ap.add_argument("--also-exclude", action="append", default=[], metavar="PATH",
                    help="bar this path too — the board item under review, "
                         "a sibling brief; repeatable")
    ap.add_argument("--include-barred", action="store_true",
                    help="THE EXCEPTION: search the barred paths as well. "
                         "Prints a disclosure banner; the verdict must say so")
    ap.add_argument("--list-barred", action="store_true",
                    help="print the exclusion set and the files it covers, "
                         "then exit")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"coldsweep: --root is not a directory: {root}", file=sys.stderr)
        return 2

    barred = () if args.include_barred else BARRED + tuple(args.also_exclude)
    kept, skipped = walk(root, barred)

    if args.list_barred:
        if args.include_barred:
            print("coldsweep: --include-barred — nothing is excluded.")
            return 0
        print(f"coldsweep: {len(barred)} barred path(s), "
              f"{len(skipped)} file(s) excluded:")
        for entry in barred:
            n = sum(1 for rel in skipped if is_barred(rel, (entry,)) == entry)
            print(f"  {entry}  ({n} file(s))")
        return 0

    if not args.pattern:
        print("coldsweep: a PATTERN is required (or --list-barred)",
              file=sys.stderr)
        return 2

    try:
        hits = search(root, args.pattern, kept, args.ignore_case)
    except re.error as e:
        print(f"coldsweep: bad pattern: {e}", file=sys.stderr)
        return 2

    for rel, n, line in hits:
        print(f"{rel}:{n}:{line}")

    # The provenance line, printed on every run so it can be pasted into a
    # verdict without the reviewer reconstructing what it actually excluded.
    print()
    if args.include_barred:
        print("⚠️  coldsweep: --include-barred — the rule-2 barred paths WERE "
              "searched.")
        print("    Disclose this exposure in your verdict. Under rule 2 a wide "
              "sweep is not")
        print("    forbidden; an undisclosed one is.")
    else:
        print(f"✓ coldsweep: {len(hits)} hit(s) over {len(kept)} file(s); "
              f"{len(skipped)} file(s) excluded as rule-2 barred "
              f"({', '.join(barred)}).")
    return 0 if hits else 1


def selftest() -> int:
    """The regression corpus is the three real instances, reduced to shapes."""
    import shutil
    import tempfile

    ok = True

    def check(name: str, cond: bool) -> None:
        nonlocal ok
        if not cond:
            print(f"FAIL: {name}")
            ok = False

    tmp = Path(tempfile.mkdtemp())
    try:
        (tmp / "docs" / "sessions").mkdir(parents=True)
        (tmp / "docs" / "reviews").mkdir(parents=True)
        (tmp / "docs" / "method").mkdir(parents=True)
        (tmp / "docs" / "SESSIONS.md").write_text("the author's account TOKEN\n")
        (tmp / "docs" / "ROADMAP-DONE.md").write_text("harvested TOKEN\n")
        (tmp / "docs" / "sessions" / "rec.md").write_text("session record TOKEN\n")
        (tmp / "docs" / "reviews" / "prior.md").write_text("prior verdict TOKEN\n")
        (tmp / "docs" / "method" / "DOC.md").write_text("doctrine TOKEN\nother\n")

        hits = search(tmp, "TOKEN", walk(tmp, BARRED)[0], False)
        check("barred files are not searched by default",
              [str(r) for r, _, _ in hits] == ["docs/method/DOC.md"])

        # THE DEFECT ITSELF: every spelling of the same path must bar the same
        # files. This is the assertion the three real instances would have failed.
        for spelling in ("./docs/sessions", "docs/sessions", "docs/sessions/",
                         "docs//sessions"):
            check(f"spelling {spelling!r} bars the same file",
                  is_barred(Path("docs/sessions/rec.md"), (spelling,)) is not None)

        check("a sibling directory is NOT barred by a prefix accident",
              is_barred(Path("docs/sessions-notes/x.md"), ("docs/sessions",))
              is None)
        check("a file whose name starts with a barred name is not barred",
              is_barred(Path("docs/SESSIONS.md.bak"), ("docs/SESSIONS.md",))
              is None)
        check("the barred file itself is barred",
              is_barred(Path("docs/SESSIONS.md"), BARRED) == "docs/SESSIONS.md")

        _, skipped = walk(tmp, BARRED)
        check("all four barred surfaces are covered", len(skipped) == 4)

        check("--include-barred reaches them",
              len(search(tmp, "TOKEN", walk(tmp, ())[0], False)) == 5)

        check("--also-exclude bars an extra path",
              is_barred(Path("docs/method/DOC.md"), BARRED + ("docs/method",))
              is not None)

        check("exit 1 when nothing matched",
              _main(["--root", str(tmp), "NO-SUCH-TOKEN"]) == 1)
        check("exit 0 when something matched",
              _main(["--root", str(tmp), "TOKEN"]) == 0)
        check("exit 2 on a bad pattern",
              _main(["--root", str(tmp), "("]) == 2)
        check("exit 2 with no pattern and no --list-barred",
              _main(["--root", str(tmp)]) == 2)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    try:
        return _main(argv)
    except OSError as e:
        print(f"coldsweep: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
