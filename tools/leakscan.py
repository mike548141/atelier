#!/usr/bin/env python3
"""leakscan — the mechanical boundary that keeps personal/estate data out of a
shareable repo.

The doctrine (atelier apex + AUTONOMY floor) says personal, health, family,
financial and estate-topology detail must never enter a repo that can go public.
A rule enforced by intent alone fails the first tired session. This is the
machine that enforces it: a denylist scan run as a pre-commit hook and in CI, so
a leak fails the commit instead of reaching the remote.

Two layers, split so the scanner itself leaks nothing:

  * STRUCTURAL patterns (in this file, shareable) match the *shape* of sensitive
    data — an email, an IPv4, a MAC, a private-key header — naming no real
    value. They need no secrets, so they ALWAYS run: partial cover even with no
    local list (graceful degradation).

  * LITERAL terms (machine-local, never in a repo) are the actual names,
    addresses, medications, device IDs and deal figures unique to one person's
    estate. That list would itself be the leak if committed, so it lives at
    $ATELIER_LEAKSCAN_TERMS or ~/.claude/leakscan-terms.txt — outside every repo.
    Absent ⇒ the scan says so LOUDLY and runs structural-only, never silently
    weaker (legibility).

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean
  1  findings (blocks the commit)
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can run
it with the system python3 and no install.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

# A line carrying this marker is intentionally exempt (e.g. an illustrative
# example in doctrine). Keep the reason on the same line so the exemption is
# self-documenting and greppable.
#
# GOVERNED BY `method/GUARDS.md` — narrow, noisy, reasoned:
#
#   * NARROW. Two forms. `leakscan:allow: <reason>` exempts every STRUCTURAL
#     rule on the line; `leakscan:allow:<rule>: <reason>` exempts only that one
#     (`leakscan:allow:ipv4: rendered example`), so a marker written for a
#     false-positive email no longer silently exempts a MAC address sitting on
#     the same line. A scoped name that matches no rule exempts NOTHING — a
#     typo fails closed and the finding still reports.
#   * REASONED. The marker only counts with a colon and a non-empty reason, so
#     prose that merely mentions the marker text does not exempt anything. A
#     bare `leakscan:allow` with no reason is a MENTION, not an exemption —
#     tightened 2026-08-05; it used to exempt the whole line.
#   * NOISY. Every suppression is counted and reported (see `Tally`). The scan
#     finds first and subtracts second, so a clean run states what it removed
#     rather than looking identical to a run that found nothing.
#
# D1 (Mike ruled 2026-08-04): an allow-marker exempts STRUCTURAL rules only.
# The machine-local term list always runs — it is the highest-confidence layer,
# and switching it off because a human judged the line safe for an unrelated
# structural reason is exactly backwards. A term-list misfire is fixed in the
# term list, which is the operator's own config.
ALLOW_MARKER = "leakscan:allow"

# `<marker>[:<rule>]: <non-empty reason>`. The optional rule group cannot
# swallow a plain reason: `leakscan:allow: a reason` fails the inner `:` after
# `a` and backtracks to the unscoped form, so both spellings parse correctly.
ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER) + r"(?::(?P<rule>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>\S)")


def parse_allow(line: str) -> str | None:
    """The scope of the line's allow-marker, or None if it carries none.

    Returns `""` for the unscoped form (every structural rule) or the rule name
    for the scoped form. A marker without a reason returns None — it is a
    mention, not an exemption."""
    m = ALLOW_RX.search(line)
    if not m:
        return None
    return m.group("rule") or ""

# Documentation-reserved / non-routable ranges that are safe to appear in
# shareable docs (RFC 5737 TEST-NET + the unspecified address). Real private
# addresses are NOT here — those are estate topology and must be flagged.
SAFE_IP_PREFIXES = ("192.0.2.", "198.51.100.", "203.0.113.", "0.0.0.0")

DEFAULT_LOCAL_TERMS = "~/.claude/leakscan-terms.txt"

# Paths never worth scanning. Hardcode-skip ONLY names that are never
# human-authored content — VCS, dependency, and tool-cache dirs. `build`/`dist`
# are DELIBERATELY absent (2026-07-11 child-CI-floor review, N1 — the same
# masking linkscan fixed at d0870a4): a content dir can legitimately share the
# name (atelier's own docs/build/ doctrine layer), and skipping it by name made
# a whole-tree scan blind to a planted leak there. Masking a layer is the worst
# failure a publish-safety scanner has; a repo with a real build-output dir
# names it in `.leakscanignore` (one line). Repo-specific globs come from
# .leakscanignore at the scan root.
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}


@dataclass(frozen=True)
class Pattern:
    name: str
    severity: str  # "high" | "medium" — advisory only; any hit still blocks
    regex: "re.Pattern[str]"


def _p(name: str, severity: str, rx: str, flags: int = 0) -> Pattern:
    return Pattern(name, severity, re.compile(rx, flags))


# Structural patterns. Ordered high→medium. Tuned to catch real estate/PII shapes
# while keeping false positives survivable (fail-safe favours over-flagging: a
# false positive costs a `leakscan:allow`, a false negative costs a leak).
STRUCTURAL: list[Pattern] = [
    _p("private-key-header", "high",
       r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"),
    _p("aws-access-key-id", "high", r"\bAKIA[0-9A-Z]{16}\b"),
    _p("jwt", "high", r"\beyJ[A-Za-z0-9_-]{6,}\.eyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}"),
    _p("email", "high",
       r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    _p("mac-address", "high",
       r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b"),
    _p("ipv4", "medium", r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    _p("ipv6", "medium",
       r"\b(?:[0-9A-Fa-f]{1,4}:){2,7}[0-9A-Fa-f]{1,4}\b"),
    _p("nz-phone", "medium",
       r"(?<!\d)(?:\+64[\s-]?|0)(?:2\d|[3-9])[\s-]?\d{3}[\s-]?\d{3,4}(?!\d)"),
    _p("nz-address", "medium",
       r"\b\d{1,4}[A-Za-z]?\s+(?:[A-Z][a-z]+\s+){0,2}"
       r"(?:Street|St|Road|Rd|Avenue|Ave|Lane|Ln|Drive|Dr|Place|Pl|"
       r"Terrace|Tce|Way|Close|Crescent|Cres|Grove|Hill|Green)\b"),
    _p("coordinates", "medium",
       r"[-+]?\d{1,2}\.\d{4,}\s*,\s*[-+]?\d{1,3}\.\d{4,}"),
    _p("nz-ird", "medium", r"\b\d{2,3}-\d{3}-\d{3}\b"),
]


@dataclass
class Tally:
    """What the scan removed AFTER finding it — rule (b) of `method/GUARDS.md`.

    Without this, a guard that subtracts silently prints the same clean tick
    for "nothing matched" and "forty things matched and every one of them was
    exempted", which are opposite states of the world. The second is where an
    allowance has quietly grown past what anyone approved."""
    by_marker: dict[str, int] = field(default_factory=dict)   # rule name -> hits
    files_by_glob: int = 0
    disabled_rules: tuple[str, ...] = ()

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def note_marker(self, rule: str) -> None:
        self.by_marker[rule] = self.by_marker.get(rule, 0) + 1

    def summary(self) -> str:
        """One stable line, zeros printed. The field set never varies between
        runs so two runs can be read side by side (a missing field would read
        as a zero rather than as 'this run did not measure it')."""
        parts = [f"{self.marker_total} by allow-marker",
                 f"{self.files_by_glob} file(s) by .leakscanignore",
                 f"{len(self.disabled_rules)} rule(s) disabled"]
        line = "  suppressed: " + " · ".join(parts)
        if self.by_marker:
            detail = ", ".join(f"{r}×{n}" for r, n in sorted(self.by_marker.items()))
            line += f"\n    allow-marker breakdown: {detail}"
        if self.disabled_rules:
            line += f"\n    disabled: {', '.join(self.disabled_rules)}"
        return line


@dataclass
class Finding:
    path: str
    line: int
    rule: str          # pattern name or "local-term"
    kind: str          # "structural" | "local"
    severity: str
    excerpt: str       # the matched span, redacted to keep the report shareable


def redact(match: str) -> str:
    """Keep enough to locate the hit, not enough to re-leak it in the report."""
    if len(match) <= 6:
        return match[0] + "*" * (len(match) - 1)
    return f"{match[:3]}…{match[-2:]} ({len(match)} chars)"


def _ipv4_is_safe(text: str) -> bool:
    return any(text.startswith(pfx) for pfx in SAFE_IP_PREFIXES) or text == "0.0.0.0"


def load_local_terms(path: Path | None) -> tuple[list[tuple[str, "re.Pattern[str]"]], str | None]:
    """Return (compiled terms, warning). Each line is a case-insensitive
    whole-word literal, unless prefixed `regex:` for a raw pattern. `#` comments
    and blank lines are ignored."""
    if path is None:
        return [], (
            "no local term list found — scanned STRUCTURAL patterns only. "
            f"Set $ATELIER_LEAKSCAN_TERMS or create {DEFAULT_LOCAL_TERMS} for full cover.")
    terms: list[tuple[str, "re.Pattern[str]"]] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("regex:"):
            body = line[len("regex:"):].strip()
            terms.append((body, re.compile(body, re.IGNORECASE)))
        else:
            terms.append((line, re.compile(r"\b" + re.escape(line) + r"\b", re.IGNORECASE)))
    return terms, None


def scan_text(path: str, text: str,
              local_terms: list[tuple[str, "re.Pattern[str]"]],
              disabled: frozenset[str] = frozenset(),
              tally: Tally | None = None) -> list[Finding]:
    findings: list[Finding] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        allow_scope = parse_allow(line)
        for pat in STRUCTURAL:
            if pat.name in disabled:
                continue
            for m in pat.regex.finditer(line):
                span = m.group(0)
                if pat.name == "ipv4" and _ipv4_is_safe(span):
                    continue
                # FIND FIRST, SUBTRACT SECOND (rule b). The hit is fully
                # formed before the allowance is consulted, so the exemption
                # can be counted rather than vanishing at the top of the loop.
                if allow_scope is not None and allow_scope in ("", pat.name):
                    if tally is not None:
                        tally.note_marker(pat.name)
                    continue
                findings.append(Finding(path, lineno, pat.name, "structural",
                                        pat.severity, redact(span)))
        # D1: the term list runs on EVERY line, allow-marker or not.
        for term, rx in local_terms:
            if rx.search(line):
                findings.append(Finding(path, lineno, "local-term", "local",
                                        "high", f"term:{term[:2]}…"))
    return findings


def _looks_binary(data: bytes) -> bool:
    return b"\x00" in data[:8192]


def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".leakscanignore"
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


def iter_files(paths: list[Path], root: Path, globs: list[str],
               tally: Tally | None = None):
    for base in paths:
        if base.is_file():
            files = [base]
        else:
            files = [p for p in base.rglob("*")
                     if p.is_file() and not (SKIP_DIR_NAMES & set(p.parts))]
        for p in files:
            # Resolve BOTH sides so rel is root-relative no matter the caller's
            # CWD (2026-07-11 review N3): floor.yml runs `--root repo repo` from
            # the workspace, where the unresolved relative_to raised and the
            # fallback quietly produced CWD-relative paths — so the scanned
            # repo's own .leakscanignore globs never matched.
            try:
                rel = str(p.resolve().relative_to(root.resolve()))
            except ValueError:
                rel = str(p)
            if _ignored(rel, globs):
                if tally is not None:
                    tally.files_by_glob += 1
                continue
            yield p, rel


def scan_paths(paths: list[Path], root: Path,
               local_terms: list[tuple[str, "re.Pattern[str]"]],
               disabled: frozenset[str] = frozenset(),
               tally: Tally | None = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p, rel in iter_files(paths, root, globs, tally):
        data = p.read_bytes()
        if _looks_binary(data):
            continue
        findings.extend(scan_text(rel, data.decode("utf-8", errors="replace"),
                                  local_terms, disabled, tally))
    return findings


def staged_added_lines() -> dict[str, str]:
    """Map path → the added-line text of the staged diff. Scans only what a
    commit would introduce (the pre-commit hot path), not the whole tree.
    R is in the filter deliberately (review B4): git detects renames by
    default, and a renamed-AND-edited file's added lines are exactly as
    leak-capable as a modified file's — ACM alone silently skipped them."""
    out = subprocess.run(
        ["git", "diff", "--cached", "--unified=0", "--no-color",
         "--diff-filter=ACMR"],
        capture_output=True, text=True, check=True).stdout
    files: dict[str, list[str]] = {}
    current: str | None = None
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            current = line[len("+++ b/"):]
            files.setdefault(current, [])
        elif line.startswith("+") and not line.startswith("+++") and current:
            files[current].append(line[1:])
    return {path: "\n".join(lines) for path, lines in files.items() if lines}


def resolve_terms_path(cli: str | None) -> Path | None:
    for candidate in (cli, os.environ.get("ATELIER_LEAKSCAN_TERMS"), DEFAULT_LOCAL_TERMS):
        if candidate:
            p = Path(candidate).expanduser()
            if p.exists():
                return p
    return None


def render_human(findings: list[Finding], warning: str | None,
                 scanned_local: bool, tally: Tally | None = None) -> str:
    lines: list[str] = []
    if warning:
        lines.append(f"⚠ {warning}")
    if not findings:
        cover = "structural + local" if scanned_local else "structural only"
        lines.append(f"✓ leakscan clean ({cover}).")
        if tally is not None:
            lines.append(tally.summary())
        return "\n".join(lines)
    lines.append(f"✗ leakscan: {len(findings)} finding(s) — commit blocked.\n")
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.severity}/{f.kind}] {f.rule} → {f.excerpt}")
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append("\n  A true positive: remove the data (and rotate if it's a secret).")
    lines.append(f"  A false positive: append '# {ALLOW_MARKER}: <reason>' to the line")
    lines.append(f"  (or '# {ALLOW_MARKER}:<rule>: <reason>' to exempt just one rule —")
    lines.append("  the narrowest allowance that covers the case), or add a path glob")
    lines.append("  to .leakscanignore. A marker with no reason exempts nothing.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="leakscan",
        description="Scan for personal/estate data before it reaches a shareable repo.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo, or --staged)")
    ap.add_argument("--staged", action="store_true",
                    help="scan only lines added in the git staging area (pre-commit hook)")
    ap.add_argument("--terms", help="path to the local literal-term list")
    ap.add_argument("--require-terms", action="store_true",
                    help="fail (exit 2) if no local term list is found, instead of "
                         "degrading to structural-only. For hooks/CI on a machine "
                         "that is EXPECTED to have full cover — review B5: to "
                         "automation, a degraded exit-0 pass is indistinguishable "
                         "from a full one.")
    ap.add_argument("--root", default=".", help="repo root for relative paths/.leakscanignore")
    ap.add_argument("--disable", default="",
                    help="comma-separated structural rules to skip (e.g. "
                         "ipv4,ipv6,mac-address for a networking repo where those "
                         "shapes are unavoidable noise). Local terms always run.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true", help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    terms_path = resolve_terms_path(args.terms)
    if args.require_terms and terms_path is None:
        print("leakscan: --require-terms set but no local term list found "
              f"(--terms, $ATELIER_LEAKSCAN_TERMS, or {DEFAULT_LOCAL_TERMS}). "
              "A structural-only scan is partial cover — refusing to report it "
              "as a pass.", file=sys.stderr)
        return 2
    local_terms, warning = load_local_terms(terms_path)
    scanned_local = terms_path is not None

    disabled = frozenset(r.strip() for r in args.disable.split(",") if r.strip())
    unknown = disabled - {p.name for p in STRUCTURAL}
    if unknown:
        print(f"leakscan: unknown rule(s) in --disable: {', '.join(sorted(unknown))}",
              file=sys.stderr)
        return 2
    # A scope reduction taken at invocation is itself an allowance, and rule (b)
    # says a reduction nobody can see is a reduction nobody reviewed — so
    # `--disable` now reports itself in the output instead of narrowing the scan
    # silently from a flag nobody reading the result will ever see.
    tally = Tally(disabled_rules=tuple(sorted(disabled)))

    if args.staged:
        try:
            staged = staged_added_lines()
        except subprocess.CalledProcessError as e:
            print(f"leakscan: git diff failed: {e}", file=sys.stderr)
            return 2
        # Positional paths, in --staged mode, restrict the scan to staged files
        # under those prefixes — e.g. scan only the shareable `tiki/` subtree of
        # an otherwise-private repo.
        # An ABSOLUTE path here scans NOTHING and exits 0 — the silent-success
        # class (linkscan L1) already closed for a missing path, found again on
        # 2026-07-25 while building tools/floor.py. git lists staged paths
        # repo-relative, so an absolute one matches no prefix, the filter empties
        # the set, and a boundary scan covering nothing looks exactly like one
        # that found nothing wrong. Refuse it — this is the subtree-scoping
        # entry point for private repos with a shareable subtree, so a silent
        # miss here is precisely the case that matters.
        absolute = [p for p in args.paths if Path(p).is_absolute()]
        if absolute:
            print(f"leakscan: --staged needs repo-relative path(s), got absolute: "
                  f"{', '.join(absolute)}\n"
                  "  git lists staged paths relative to the repo root, so an "
                  "absolute path matches nothing\n"
                  "  and the scan would pass while covering nothing. Pass e.g. "
                  "'tiki/' instead.", file=sys.stderr)
            return 2
        prefixes = tuple(p.rstrip("/") + "/" for p in args.paths)
        if prefixes:
            staged = {path: text for path, text in staged.items()
                      if path.startswith(prefixes) or path in args.paths}
        # .leakscanignore applies in staged mode too, so an exemption means the
        # same thing whether you scan the tree or a commit.
        globs = load_ignore_globs(root)
        findings = []
        for path, text in staged.items():
            if _ignored(path, globs):
                tally.files_by_glob += 1
                continue
            findings.extend(scan_text(path, text, local_terms, disabled, tally))
    else:
        targets = [Path(p) for p in (args.paths or [str(root)])]
        missing = [str(p) for p in targets if not p.exists()]
        if missing:
            # A typo'd path scanning nothing must never read as a clean pass —
            # the linkscan L1 silent-success class, closed here too
            # (2026-07-11 review N2).
            print(f"leakscan: path does not exist: {', '.join(missing)}",
                  file=sys.stderr)
            return 2
        findings = scan_paths(targets, root, local_terms, disabled, tally)

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "scanned_local_terms": scanned_local,
            "warning": warning,
            "findings": [asdict(f) for f in findings],
            "suppressed": {
                "by_allow_marker": tally.marker_total,
                "by_allow_marker_rule": tally.by_marker,
                "files_by_ignore_glob": tally.files_by_glob,
                "disabled_rules": list(tally.disabled_rules),
            },
        }, indent=2))
    else:
        print(render_human(findings, warning, scanned_local, tally))

    return 1 if findings else 0


def _selftest() -> int:
    """Minimal smoke test so `leakscan --selftest` proves the engine on any box,
    even where the unittest file isn't shipped."""
    cases = [  # fictional fixtures; the shapes here are the point of the test
        ("contact me at jane.doe@example.com", "email", True),      # leakscan:allow: selftest fixture
        ("gateway 172.16.31.7 is the igw", "ipv4", True),           # leakscan:allow: selftest fixture
        ("example host 192.0.2.10 in docs", None, False),      # TEST-NET is safe
        ("mac aa:bb:cc:dd:ee:ff", "mac-address", True),            # leakscan:allow: selftest fixture
        ("version 1.2.3 released", None, False),              # semver, not an IP
        ("secret@host.com  # leakscan:allow: doc example", None, False),
    ]
    ok = True
    for text, expect_rule, expect_hit in cases:
        fs = scan_text("t", text, [])
        hit = bool(fs)
        if hit != expect_hit:
            print(f"FAIL: {text!r} expected hit={expect_hit} got {hit}")
            ok = False
        elif expect_rule and not any(f.rule == expect_rule for f in fs):
            print(f"FAIL: {text!r} expected rule {expect_rule}, got {[f.rule for f in fs]}")
            ok = False
    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
