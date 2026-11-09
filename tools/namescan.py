#!/usr/bin/env python3
"""namescan — in a public repo, no private name in a branch name or a commit title.

WHY (board `160/360` finding NP2, the fifth slice of `320/810`; the principal,
2026-11-09: "all six, warnings at first and then move to blocking action").
A branch name and a commit title publish in full the moment they are pushed,
and no check read either: the failure had happened in head refs, more than
once, and the doctrine could only say so in prose.

WHAT COUNTS AS A PRIVATE NAME: exactly what leakscan already treats as one, read
through leakscan's own term sources and engine (`$ATELIER_LEAKSCAN_TERMS`, then
`~/.claude/leakscan-terms.txt`), plus its structural shapes, because a hostname
or address in a title leaks the same way. No new list exists or is made. A
finding names the rule and a redacted excerpt, never the term.

SCOPE. A repo that declares `"visibility": "public"` in `.atelier-floor.json`
(`260/050`). A private repo may name itself and its clients in its own titles,
and they are out of scope here, as in `pdlistscan`.

THE PLANES. `--message-file` is the `msg` plane: this commit's title and the
current branch. `--range` is the `ci` plane, over a pushed range: titles
already pushed cannot be fixed without rewriting history, so it only reports,
and the floor's CI template carries `--warn` to say so on the board. A branch
exists only on the `msg` plane and as the pushed ref name in CI. Bodies are not
read here; `leakscan --messages` is the sweep for those.

THE DATE. Before `NAME_WARN_UNTIL` a finding on the message plane is reported
and exits 0; on and after it, it exits 1, unless `--warn`. The constant is
compared with the UTC clock and no flag, environment variable or config key
moves it. The date is the run's choice, not his (`320/810`).

EXEMPTION. A line `namescan:allow: <reason>` in the message body. A subject
cannot exempt itself and a bare marker exempts nothing: a title is what the
world reads, so the reason has to sit where someone looking at the commit will
see it.

Exit codes: 0 nothing blocking · 1 a finding on the message plane on or after
the date · 2 the scan itself is broken, including `--require-terms` with no
list.

Stdlib-only, like every sibling.
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allowmarker  # noqa: E402
import commitmsg  # noqa: E402
import leakscan  # noqa: E402
import pdlistscan  # noqa: E402
import report  # noqa: E402

NAME = "namescan"

# 320/810 slice 5: before this date a finding is reported and exits 0; on and
# after it, it exits 1 unless `--warn`. A run's choice of date, not the
# principal's: four weeks after the last date already set for this sequence.
NAME_WARN_UNTIL = datetime.date(2027, 5, 3)

ALLOW_MARKER = f"{NAME}:allow"
ALLOW_RX = allowmarker.marker_rx(ALLOW_MARKER, sep=allowmarker.SEP_ANY_SPACE,
                                 named_reason=False)


class ConfigError(RuntimeError):
    """Something the scan needs is unusable; fail closed."""


def _utc_today() -> datetime.date:
    return datetime.datetime.now(datetime.timezone.utc).date()


def warn_only_today(today: datetime.date | None = None) -> bool:
    """True strictly before `NAME_WARN_UNTIL` (UTC). Tests patch `_utc_today`."""
    return (today or _utc_today()) < NAME_WARN_UNTIL


@dataclass
class Finding:
    where: str  # "branch", "subject", or a short commit id
    rule: str
    excerpt: str


def _scan_line(text: str, where: str,
               terms: list[tuple[str, "re.Pattern[str]"]]) -> list[Finding]:
    found = leakscan.scan_lines(where, [(1, text)], terms, honour_markers=False)
    return [Finding(where, f.rule, report.safe_text(f.excerpt)[:60])
            for f in found if f.response == leakscan.RESPONSE_BLOCK]


def scan_message(message: str, branch: str,
                 terms: list[tuple[str, "re.Pattern[str]"]]) -> list[Finding]:
    """Findings in this commit's title and branch, unless the message body
    carries a reasoned exemption."""
    if allowmarker.present(ALLOW_RX, message):
        return []
    findings = _scan_line(commitmsg.subject(message), "subject", terms)
    if branch:
        findings.extend(_scan_line(branch, "branch", terms))
    return findings


def scan_range(root: Path, spec: str, branch: str,
               terms: list[tuple[str, "re.Pattern[str]"]]) -> list[Finding]:
    findings: list[Finding] = []
    if branch:
        findings.extend(_scan_line(branch, "branch", terms))
    for c in commitmsg.commits(root, spec):
        if allowmarker.present(ALLOW_RX, c.message):
            continue
        for f in _scan_line(commitmsg.subject(c.message), c.sha[:12], terms):
            findings.append(f)
    return findings


def _load_terms(args) -> tuple[list, str]:
    """(terms, a cover note). A set-but-broken term path and `--require-terms`
    with no list are broken scans, the way they are for leakscan."""
    try:
        path = leakscan.resolve_terms_path(args.terms, args.require_terms)
    except leakscan.TermsPathError as e:
        raise ConfigError(str(e)) from e
    if args.require_terms and path is None:
        raise ConfigError("--require-terms set but no local term list found "
                          f"(--terms, $ATELIER_LEAKSCAN_TERMS, or "
                          f"{leakscan.DEFAULT_LOCAL_TERMS})")
    try:
        terms, warning = leakscan.load_local_terms(path)
    except OSError as e:
        raise ConfigError(f"the term list {path} cannot be read: {e}") from e
    return terms, ("" if terms else (warning or
                   "no term list on this machine: structural shapes only"))


def _main(argv: list[str] | None) -> int:
    ap = argparse.ArgumentParser(
        prog=NAME,
        description="In a repo that declares itself public, no private name "
                    "in a branch name or a commit title.")
    ap.add_argument("--message-file", default="", metavar="PATH",
                    help="the msg plane: this commit's message, as git hands it to commit-msg")
    ap.add_argument("--range", default="", metavar="SPEC",
                    help="the ci plane: a git log spec, or 'pushed' for the "
                         "range this run covers")
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--terms", help="path to the local literal-term list")
    ap.add_argument("--require-terms", action="store_true",
                    help="fail (exit 2) if no local term list is found")
    ap.add_argument("--warn", action="store_true",
                    help="report findings but exit 0 for them")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the tool against its own fixtures, then exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return report.quiet_selftest(NAME, _selftest)
    if bool(args.message_file) == bool(args.range):
        return report.broken(NAME, "give exactly one of --message-file and --range")

    root = Path(args.root).resolve()
    rc = report.refuse_missing_root(NAME, root, args.root)
    if rc is not None:
        return rc

    if not pdlistscan.declared_public(root):
        print(report.clean_head(NAME, "not declared public: out of scope."))
        print(report.advisory_count_line(NAME, 0))
        return 0

    terms, cover = _load_terms(args)
    if args.message_file:
        mode = "message"
        message = commitmsg.read_message(Path(args.message_file), root)
        findings = scan_message(message, commitmsg.branch(root, {}), terms)
        note = ""
    else:
        mode = "range"
        spec, note = (commitmsg.pushed_range(root) if args.range == "pushed"
                      else (args.range, ""))
        findings = scan_range(root, spec, commitmsg.branch(root), terms)

    gating = mode == "message"
    blocks = gating and bool(findings) and not args.warn and not warn_only_today()
    if args.json:
        print(json.dumps({
            "clean": not blocks, "mode": mode, "blocking": blocks, "warn": args.warn,
            "cover": cover or "full", "note": note,
            "findings": [asdict(f) for f in findings],
            "until": NAME_WARN_UNTIL.isoformat(),
        }, indent=2))
    else:
        print(render(findings, blocks, mode, note, cover))
        print(report.advisory_count_line(NAME, 0 if blocks else len(findings)))
        if args.warn and findings and gating:
            print(report.WARN_NOTICE)
    return report.exit_code(blocks)


def render(findings: list[Finding], blocks: bool, mode: str, note: str, cover: str) -> str:
    until = NAME_WARN_UNTIL.isoformat()
    what = "this commit" if mode == "message" else "the pushed range"
    extra = "".join(f" ({n})" for n in (note, cover) if n)
    if not findings:
        return report.clean_head(NAME, f"no private name in a branch or title on {what}.{extra}")
    head = (report.findings_head(NAME, len(findings), "private name(s)",
                                 " in a branch or title — commit blocked.")
            if blocks else
            f"⚠ {NAME}: {len(findings)} private name(s) in a branch or title on {what} "
            f"(warning; blocking from {until}).")
    lines = [head + extra]
    lines += [f"  {f.where}: [{f.rule}] {f.excerpt}" for f in findings[:40]]
    if blocks or mode == "message":
        lines.append("  Reword the title, or rename the branch, or add a line "
                     f"'{ALLOW_MARKER}: <reason>' to the message body.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    return report.guarded_main(NAME, _main, argv, (ConfigError, RuntimeError))


def _selftest() -> int:
    import re

    fails: list[str] = []

    def check(name, got, want):
        if got != want:
            fails.append(f"{name}: got {got!r}, want {want!r}")

    terms = [("zephyrcorp", re.compile(r"\bzephyrcorp\b", re.I))]
    check("clean title", scan_message("area: do a thing\n", "main", terms), [])
    check("term in the subject", len(scan_message("tools: zephyrcorp thing\n", "", terms)), 1)
    check("term in the branch", len(scan_message("x\n", "report-zephyrcorp-1", terms)), 1)
    check("a marker in the body exempts",
          scan_message("tools: zephyrcorp thing\n\nnamescan:allow: fixture\n", "", terms), [])
    check("a bare marker does not",
          len(scan_message("tools: zephyrcorp thing\n\nnamescan:allow\n", "", terms)), 1)
    for f in fails:
        print(f"{NAME} selftest FAIL: {f}", file=sys.stderr)
    print(f"{NAME} selftest: {'FAILED' if fails else 'ok'} ({len(fails)} failure(s))")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
