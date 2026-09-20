#!/usr/bin/env python3
"""reviewscan — the mechanical half of REVIEW.md. Two checks, one doctrine
file: a decision record states its review judgement, and a review brief keeps
its deferred material out of the reviewer's way.

CHECK 2 — DEFERRED MATERIAL IS NOT IN THE BRIEF (added 2026-07-29, Mike)
------------------------------------------------------------------------
REVIEW.md rule 1 defers the author's seeded questions until the reviewer's own
findings are durably written. Until now the deferral was a *section below a
divider in the brief itself*, and rule 1 called that structural. It was not.
**Reading is atomic**: a reviewer told to read the brief reads the whole file,
so the deferred section is consumed by the very act it was meant to survive,
and its "open only after…" label sits inside the thing it warns about. The
rule was unfollowable, not merely unfollowed — nobody can know where the
divider falls without reading past it. It had already leaked once through a
side channel (the 2026-07-21 pass, where a pending-changes scanner swept the
dirty brief and fed its deferred section back to the reviewer pre-draft).

So deferred material moves to a sibling file, `<brief>.deferred.md`, and this
check reds a brief that carries a deferred SECTION with no verdict beneath it
— catching the defect when the AUTHOR writes it, before any reviewer is
exposed. A brief that already has its verdict is a finished record whose
deferral was folded back in (rule 1's "split for the duration, merged at
rest"), so it passes.

What this check deliberately does NOT do: demand the fold-back. A reviewer
commits its findings BEFORE opening the deferred file — that is the whole
point of the sequence — so at that moment the brief legitimately has a verdict
heading and the sibling file still exists. A fold-back lint would fire exactly
on correct behaviour at exactly the prescribed moment, which is how a check
gets trained away (Track E). The fold-back stays a convention, honestly named
here rather than half-enforced.

CHECK 1 — A DECISION RECORD STATES ITS REVIEW JUDGEMENT
--------------------------------------------------------

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

Stated residual (2026-07-21 cold-pass RS4): the boundary reads the FILENAME
date, so a record deliberately backdated below BOUNDARY escapes the lint.
The house's real date-error mode (NZ local stamped instead of UTC) errs
forward — the safe direction — and a gaming author has a cheaper honest
hatch in `reviewscan:allow:`. Accepted, not defended against.

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
import codecs
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
# bullet, blockquoted, or SHOUTED — the field, not one typography. The value
# must be non-empty (RS3): the thing whose presence the rule demands is a
# JUDGEMENT, and `**Review**:` with nothing after the colon is the blank the
# rule exists to make impossible, wearing the field's clothes.
REVIEW_LINE = re.compile(r"^[\s>*-]*(?:\*\*)?[Rr](?:eview|EVIEW)(?:\*\*)?\s*:\s*\S")

ALLOW_MARKER = "reviewscan:allow:"
ALLOW_BASE = "reviewscan:allow"

# GUARDS.md rule (c): a marker only counts with a colon and a non-empty reason,
# so prose that merely mentions the marker text exempts nothing. Tightened
# 2026-08-05 — a bare marker used to exempt on a substring match.
ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_BASE) + r"(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>[\w\"\'“‘])")


def parse_allow(text: str) -> str | None:
    """The scope of the allow-marker, or None if there is no reasoned one.

    `""` means the whole record; `"deferral"` is the DEFERRAL_ALLOW scope
    that check 2 requires (an unscoped allow must not silently waive the
    deferral guard too — DF3). A marker with no reason returns None."""
    m = ALLOW_RX.search(text)
    if not m:
        return None
    return m.group("kind") or ""


FENCE = re.compile(r"^\s*(```|~~~)")

# Check 2. A HEADING, never prose: "Deferral exposure — named, not denied" is a
# brief honestly declaring what it saw early, and reddening that would punish
# the disclosure the doctrine asks for. Only a section heading declares that
# deferred CONTENT is sitting in this file. The words `deferred`/`seeded`
# anywhere in the heading, not a "Deferred" prefix: the first cut was
# prefix-anchored and "## Seeded questions" or "## Author's deferred
# questions" passed green (DF1, the 2026-08-02 cold pass) — and the authors
# this net exists to catch are exactly the ones not using the canonical
# vocabulary. A renamed section using neither word still escapes; that limit
# is named in REVIEW.md rule 1 rather than implied away.
DEFERRED_HEADING = re.compile(r"^#{1,6}\s.*\b(deferred|seeded)\b",
                              re.IGNORECASE)

# Check 2's exemption is SCOPED: an unscoped `reviewscan:allow:` placed for a
# review-line reason must not silently waive the deferral guard too (DF3).
DEFERRAL_ALLOW = "reviewscan:allow:deferral:"

# Any heading carrying the word — "## Verdict", "# Verdict — PASS", "## Cold
# verdict (Fable, 2026-07-26)". Matching the word rather than one house
# spelling: the corpus already writes it three ways, and a lint that only knows
# one of them reds finished records for their typography.
VERDICT_HEADING = re.compile(r"^#{1,6}\s.*\bverdict\b", re.IGNORECASE)


# Streaming-read tuning (020/380, reusing 020/370's WINDOWING shape — see
# `tools/secretscan.py`'s identical mechanism). Fixed sizes independent of
# the file scanned: peak memory for reading ANY one record or brief is
# bounded by `LINE_WINDOW_BYTES + LINE_WINDOW_OVERLAP`, never by the file's
# own size. Duplicated here rather than imported so this tool stays
# self-contained and copyable alone.
#
# The WINDOW SIZE is grounded in THIS tool's own shapes (`tools/linkscan.py`
# makes the same argument in more detail, and measured the same effect):
# nothing this tool matches — `REVIEW_LINE`, `VERDICT_HEADING`,
# `DEFERRED_HEADING`, `FENCE` — is an open-ended token the way a credential
# is; every one is a short, `^`-anchored line shape. 256 KiB is generous by
# orders of magnitude over any real line here, and keeps an adversarial
# file's per-window footprint small enough that windowing many overlong
# lines does not itself compound allocator overhead.
READ_CHUNK_BYTES = 1 * 1024 * 1024
LINE_WINDOW_BYTES = 256 * 1024
LINE_WINDOW_OVERLAP = 4 * 1024


def _iter_file_lines(path: Path):
    """Yield (line, is_first_window) for `path`, reading it in fixed-size
    chunks so peak memory is bounded by a constant regardless of the file's
    size or its longest line (020/380) — replaces the old whole-file
    `read_text()` -> `text.splitlines()`, which held the file and its full
    line list at once.

    A fence delimiter, a review line, or a verdict/deferred heading is
    always a short, `^`-anchored line — so it is always resolved within a
    physical line's FIRST window. `is_first_window` lets callers skip
    re-running those start-anchored checks on a continuation window of an
    overlong line, the same reasoning `tools/linkscan.py`'s `_FenceState`
    documents for its own fence tracking. The allow-marker search is NOT
    gated on it — a marker can sit anywhere on a line, so every window is
    checked, matching the old whole-text `in` / `.search()` as closely as a
    bounded read can (a marker split exactly across one window's cut is the
    one stated residual, mitigated by the overlap)."""
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    pending = ""
    first = True
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(READ_CHUNK_BYTES)
            if not chunk:
                break
            pending += decoder.decode(chunk)
            while True:
                nl = pending.find("\n")
                if nl == -1:
                    break
                yield pending[:nl], first
                pending = pending[nl + 1:]
                first = True
            if len(pending) >= LINE_WINDOW_BYTES:
                yield pending, first
                pending = pending[-LINE_WINDOW_OVERLAP:]
                first = False
        pending += decoder.decode(b"", final=True)
        if pending:
            yield pending, first


def scan_record(path: Path, suppressed: list[int] | None = None) -> bool:
    """True if the record satisfies the rule (has the line, or is exempt).

    `suppressed` collects one entry per record an allow-marker exempted, so a
    clean run can state what it subtracted (`method/GUARDS.md`, rule b)."""
    # A `review:` inside a fenced code block is a QUOTED example, not the
    # record's own judgement (RS2) — track fence state and skip fenced lines.
    in_fence = False
    for line, is_first in _iter_file_lines(path):
        if parse_allow(line) is not None:
            if suppressed is not None:
                suppressed.append(1)
            return True
        if not is_first:
            continue
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and REVIEW_LINE.match(line):
            return True
    return False


def scan_brief(path: Path) -> bool:
    """True if the brief satisfies rule 1's placement rule (or is exempt).

    Fails only for the one mechanically-reliable shape: a deferred SECTION
    present in a brief that has no verdict yet — i.e. deferred content sitting
    where a reviewer will read it before its findings exist.
    """
    in_fence = False
    has_deferred = has_verdict = False
    for line, is_first in _iter_file_lines(path):
        if DEFERRAL_ALLOW in line:
            return True
        if not is_first:
            continue
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # Verdict wins on a dual-word heading ("## Verdict — deferred folded
        # in"): it IS a verdict heading, and any verdict passes the file.
        if VERDICT_HEADING.match(line):
            has_verdict = True
        elif DEFERRED_HEADING.match(line):
            has_deferred = True
    return has_verdict or not has_deferred


def _is_reviews_dir(p: Path) -> bool:
    return (p.is_dir() and p.name == "reviews" and p.parent.name == "docs"
            and "templates" not in p.parts)


def _dir_briefs(reviews_dir: Path) -> list[Path]:
    """Review briefs in a reviews dir.

    Skips README.md (the dir's own index, not a brief) and `*.deferred.md`
    (the sibling this rule EXISTS to create — reddening it would forbid the
    remedy).
    """
    return [f for f in sorted(reviews_dir.glob("*.md"))
            if f.name != "README.md" and not f.name.endswith(".deferred.md")]


def find_briefs(paths: list[Path]) -> list[Path]:
    """Review briefs in scope — same three invocation shapes as find_records."""
    briefs: list[Path] = []
    for base in paths:
        if base.is_file():
            if (_is_reviews_dir(base.parent) and base.suffix == ".md"
                    and base.name != "README.md"
                    and not base.name.endswith(".deferred.md")):
                briefs.append(base)
        elif _is_reviews_dir(base):
            briefs.extend(_dir_briefs(base))
        else:
            for reviews_dir in sorted(base.rglob("docs/reviews")):
                if _is_reviews_dir(reviews_dir):
                    briefs.extend(_dir_briefs(reviews_dir))
    return sorted(dict.fromkeys(briefs))


def _dir_records(decisions_dir: Path) -> list[Path]:
    records = []
    for f in sorted(decisions_dir.glob("*.md")):
        m = RECORD_NAME.match(f.name)
        if m and m.group(1) >= BOUNDARY:
            records.append(f)
    return records


def _is_decisions_dir(p: Path) -> bool:
    return (p.is_dir() and p.name == "decisions" and p.parent.name == "docs"
            and "templates" not in p.parts)


def find_records(paths: list[Path]) -> list[Path]:
    """Decision records in scope: docs/decisions/<date-named>.md, post-boundary.

    A base may be a tree to search, a decisions dir itself, or a single record
    file — the natural hand-run invocations (RS1: an explicitly-named path
    must be scanned, never silently matched by nothing and greened).
    """
    records: list[Path] = []
    for base in paths:
        if base.is_file():
            m = RECORD_NAME.match(base.name)
            if (m and m.group(1) >= BOUNDARY
                    and _is_decisions_dir(base.parent)):
                records.append(base)
        elif _is_decisions_dir(base):
            records.extend(_dir_records(base))
        else:
            for decisions_dir in sorted(base.rglob("docs/decisions")):
                if _is_decisions_dir(decisions_dir):
                    records.extend(_dir_records(decisions_dir))
    return sorted(dict.fromkeys(records))


def run(paths: list[Path], root: Path, as_json: bool) -> int:
    records = find_records(paths)
    _suppressed: list[int] = []
    failures = [r for r in records if not scan_record(r, _suppressed)]
    briefs = find_briefs(paths)
    misplaced = [b for b in briefs if not scan_brief(b)]
    if as_json:
        print(json.dumps({
            "checked": [str(r.relative_to(root)) for r in records],
            "failures": [str(r.relative_to(root)) for r in failures],
            "briefs_checked": [str(b.relative_to(root)) for b in briefs],
            "briefs_misplaced_deferral": [
                str(b.relative_to(root)) for b in misplaced],
        }, indent=2))
        return 1 if (failures or misplaced) else 0

    if failures:
        for r in failures:
            print(f"✗ {r.relative_to(root)} — no review line. Add one:")
        print()
        print("Every decision record states its review judgement (REVIEW.md):")
        print("  **Review**: queued — docs/reviews/<brief>.md")
        print("  **Review**: not warranted — <grounds>")
        print("Omission is the bug: a blank can't be disagreed with. A genuine")
        print(f"exception carries `{ALLOW_MARKER} <reason>` on a line.")
    if misplaced:
        if failures:
            print()
        for b in misplaced:
            print(f"✗ {b.relative_to(root)} — deferred section inside the "
                  "brief, with no verdict yet.")
        print()
        print("REVIEW.md rule 1: deferred material lives in a SIBLING file,")
        print("not below a divider — reading is atomic, so a deferred section")
        print("is consumed by the act of reading the brief it sits in.")
        print("  mv the section into <brief>.deferred.md and point at it;")
        print("  the reviewer opens it only once its findings are written,")
        print("  then folds it back below the verdict and deletes it.")
        print(f"A genuine exception carries `{DEFERRAL_ALLOW} <reason>` —")
        print("scoped, so a review-line exemption does not waive this check.")
    if not failures and not misplaced:
        print(f"✓ reviewscan clean — {len(records)} post-{BOUNDARY} decision "
              f"record(s) carry a review line; {len(briefs)} review brief(s) "
              "keep deferred material out of the brief.")
        print(f"  suppressed: {len(_suppressed)} record(s) by allow-marker")
    return 1 if (failures or misplaced) else 0


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

        r = Path(td) / "docs" / "reviews"
        r.mkdir(parents=True)
        (r / "2026-07-29-1200-leaky.md").write_text(
            "# Brief\n\n## Deferred — seeded questions\n\nQ1\n")
        (r / "2026-07-29-1300-split.md").write_text(
            "# Brief\n\nDeferred material: 2026-07-29-1300-split.deferred.md\n")
        (r / "2026-07-29-1300-split.deferred.md").write_text(
            "## Deferred — seeded questions\n\nQ1\n")
        (r / "2026-07-29-1400-finished.md").write_text(
            "# Brief\n\n## Deferred — folded back\n\n## Cold verdict\n\nPASS\n")
        (r / "2026-07-29-1500-prose.md").write_text(
            "# Brief\n\n- **Deferral exposure** — named, not denied: …\n")
        (r / "2026-07-29-1600-fenced.md").write_text(
            "# Brief\n\n```\n## Deferred — an EXAMPLE of the heading\n```\n")
        (r / "README.md").write_text("## Deferred — index, not a brief\n")

        records = find_records([Path(td)])
        failures = [rec.name for rec in records if not scan_record(rec)]
        briefs = find_briefs([Path(td)])
        misplaced = [b.name for b in briefs if not scan_brief(b)]
        ok = (sorted(rec.name for rec in records) == [
                  "2026-07-25-1200-good.md", "2026-07-25-1300-bad.md",
                  "2026-07-25-1400-exempt.md"]
              and failures == ["2026-07-25-1300-bad.md"]
              and sorted(b.name for b in briefs) == [
                  "2026-07-29-1200-leaky.md", "2026-07-29-1300-split.md",
                  "2026-07-29-1400-finished.md", "2026-07-29-1500-prose.md",
                  "2026-07-29-1600-fenced.md"]
              and misplaced == ["2026-07-29-1200-leaky.md"])
        print("reviewscan selftest:", "OK" if ok else "FAILED")
        if not ok:
            print("  in scope:", sorted(rec.name for rec in records))
            print("  failures:", failures)
            print("  briefs:", sorted(b.name for b in briefs))
            print("  misplaced:", misplaced)
        return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="REVIEW.md's mechanical half: decision records carry a "
                    "review line, and review briefs keep deferred material in "
                    "a sibling file")
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
    # A RELATIVE target resolves against --root, never the caller's cwd:
    # mixing the two reads one repo's file under another repo's rules,
    # and neither half of the output says so (roadmap 010/110).
    paths = [((root / p) if not Path(p).is_absolute()
              else Path(p)).resolve()
             for p in (args.paths or [args.root])]
    for p in paths:
        if not p.exists():
            print(f"reviewscan: {p} does not exist", file=sys.stderr)
            return 2
    return run(paths, root, args.json)


if __name__ == "__main__":
    sys.exit(main())
