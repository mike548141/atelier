#!/usr/bin/env python3
"""pdlistscan — in a public repo, personal data stands only where the closed list names it.

WHY (board `160/630`, the third slice of `320/810`; the principal, 2026-11-09:
"all six, warnings at first and then move to blocking action"). A cold pass found
atelier claiming every personal-data exception was "declared where it appears"
while the account name stood on 27 lines with no declaration and the leak guard
passed it unmarked. The fix was one closed list, `docs/PERSONAL-DATA.md`, which
`tools/test_personal_data.py` keeps true for atelier alone, and the rule that in
a public repo only the principal grants an exception, in his own words. A test
in atelier's suite reaches no child. This is the same check, in the floor, for
any repo that declares itself public (`visibility` in `.atelier-floor.json`,
`260/050`).

WHAT IT READS. A repo not declaring `"visibility": "public"` is out of scope and
says so: in a private repo the principal's order for the work is the grant
(his answer, 2026-11-09), which no scanner can read. In scope:

  no-list           `docs/PERSONAL-DATA.md` is missing.
  unlisted-marker   a personal-data allow-marker (`leakscan:allow:<scope>:` where
                    a scope is a personal-data rule) stands in a tracked file no
                    entry's `May stand in` names. A marker is not a grant.
  unlisted-holder   a string an entry pins under `Data` stands in a tracked file
                    no entry's `May stand in` for it names.

A marker or string in `tools/` or `instruments/` is not counted WHEN `tools/leakscan.py`
exists at the root: those paths in atelier itself hold the scanners' own invented
fixtures (the exemption `tools/test_personal_data.py` makes). A child's `tools/`
is read like any other path.

THE DATE. Before `PERSONAL_DATA_WARN_UNTIL` a finding is reported and exits 0.
On and after it the finding exits 1 unless `--warn` was given. The constant is
compared with the UTC clock; no flag, environment variable or config key moves
it, in leakscan's `BINARY_GRACE_UNTIL` shape, and the date is the run's choice,
not his (`320/810`: four weeks after `attribscan`'s). No child declares itself
public yet with a list, so today this reads only atelier.

WHAT IT DOES NOT SEE. Personal data the list never pinned: the given name and
commit headers (`PD4`, `PD5` in atelier's list) carry no string to find, and a
name nobody listed is the leak scanner's job, not this one's. A marker without
a scope (the unscoped form exempts every structural rule) is the leak scanner's
to judge. A list that lies about why a place holds its data: this checks where,
never whether the reason is good.

Exit codes: 0 nothing blocking (clean, out of scope, a warning before the date,
or `--warn`) · 1 a finding on or after the date · 2 the scan is broken (an
unparseable config or list, or no git repository to list files from).

Stdlib-only, like every sibling.
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
import report  # noqa: E402

NAME = "pdlistscan"
LIST_PATH = "docs/PERSONAL-DATA.md"

# 320/810 slice 3 (see THE DATE above). A run's choice of date, not the
# principal's: four weeks after `attribscan`'s `ATTRIBUTION_WARN_UNTIL`.
PERSONAL_DATA_WARN_UNTIL = datetime.date(2027, 3, 8)

# The personal-data rules whose allow-marker is an excuse for personal data, as
# opposed to a credential or a network shape; the same set as
# `tools/test_personal_data.py`, which pins it against leakscan's real rules.
PERSONAL_SCOPES = frozenset({
    "local-term", "email", "pii-key-context", "nz-phone", "nz-address",
    "nz-bank-account", "nz-ird", "payment-card", "iban", "coordinates",
    "diagnosis-key",
})
MARKER_RX = re.compile(r"leakscan:allow:([a-z0-9,-]+):")
MECHANISM_PREFIXES = ("tools/", "instruments/")
MAX_FILE_BYTES = 4 * 1024 * 1024  # a tracked file over this is not read whole
MAX_LISTED = 40


class ConfigError(RuntimeError):
    """A declaration or list this scan depends on is unusable; fail closed."""


def _utc_today() -> datetime.date:
    return datetime.datetime.now(datetime.timezone.utc).date()


def warn_only_today(today: datetime.date | None = None) -> bool:
    """True strictly before `PERSONAL_DATA_WARN_UNTIL` (UTC). Tests patch
    `_utc_today`; nothing a caller can pass at the command line reaches it."""
    return (today or _utc_today()) < PERSONAL_DATA_WARN_UNTIL


@dataclass
class Finding:
    kind: str   # "no-list" | "unlisted-marker" | "unlisted-holder"
    path: str
    line: int
    detail: str


# ------------------------------------------------------------- the list --

def glob_rx(pattern: str) -> re.Pattern:
    """`*` stays inside a path segment, `**` crosses them."""
    out, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**", i):
            out, i = out + ".*", i + 2
        elif pattern[i] == "*":
            out, i = out + "[^/]*", i + 1
        else:
            out, i = out + re.escape(pattern[i]), i + 1
    return re.compile(out + r"\Z")


def ticks(text: str) -> list[str]:
    text = re.sub(r"<!--.*?-->", "", text)
    return re.findall(r"`([^`]+)`", text)


def parse_list(text: str) -> list[dict]:
    """Entries from `## PDn — title` sections and their `- **Field:**` bullets,
    the shape `docs/PERSONAL-DATA.md` keeps."""
    entries: list[dict] = []
    cur: dict | None = None
    field: str | None = None
    for line in text.splitlines():
        m = re.match(r"## (PD\d+) ", line)
        if m:
            cur = {"id": m.group(1), "fields": {}}
            entries.append(cur)
            field = None
            continue
        if cur is None:
            continue
        m = re.match(r"- \*\*([^*:]+):\*\*(.*)", line)
        if m:
            field = m.group(1)
            cur["fields"][field] = m.group(2)
        elif field and line.startswith("  "):
            cur["fields"][field] += " " + line.strip()
        else:
            field = None
    return entries


def pinned(entry: dict) -> list[str]:
    data = entry["fields"].get("Data", "")
    return [] if "not pinned" in data else ticks(data)


def declared_public(root: Path) -> bool:
    cfg = root / ".atelier-floor.json"
    if not cfg.is_file():
        return False
    try:
        raw = json.loads(cfg.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise ConfigError(f"cannot read {cfg}: {e}") from e
    return raw.get("visibility") == "public"


def tracked(root: Path) -> list[str]:
    out = subprocess.run(["git", "-C", str(root), "ls-files", "-z"],
                         capture_output=True)
    if out.returncode != 0:
        raise ConfigError(f"git ls-files failed under {root}: "
                          f"{out.stderr.decode('utf-8', 'replace').strip()}")
    return [p for p in out.stdout.decode("utf-8").split("\0") if p]


def read(root: Path, rel: str) -> str | None:
    """A tracked file's text, or None for a binary or an oversized one."""
    p = root / rel
    try:
        if p.stat().st_size > MAX_FILE_BYTES:
            return None
        data = p.read_bytes()
    except OSError:
        return None
    if b"\0" in data:
        return None
    return data.decode("utf-8", "replace")


# ------------------------------------------------------------- the scan --

def scan(root: Path) -> list[Finding]:
    """The findings for a repo already known to be in scope."""
    list_file = root / LIST_PATH
    if not list_file.is_file():
        return [Finding("no-list", LIST_PATH, 0,
                        f"this repo declares itself public and has no {LIST_PATH}: "
                        "only the principal grants a personal-data exception, and "
                        "the list is where each grant is written down")]
    try:
        entries = parse_list(list_file.read_text(encoding="utf-8", errors="replace"))
    except OSError as e:
        raise ConfigError(f"cannot read {LIST_PATH}: {e}") from e
    named = [glob_rx(g) for e in entries
             for g in ticks(e["fields"].get("May stand in", ""))]
    per_entry = [(e, [glob_rx(g) for g in ticks(e["fields"].get("May stand in", ""))],
                  pinned(e)) for e in entries]
    mechanism_exempt = (root / "tools" / "leakscan.py").is_file()
    findings: list[Finding] = []
    for rel in tracked(root):
        if rel == LIST_PATH or (mechanism_exempt and rel.startswith(MECHANISM_PREFIXES)):
            continue
        text = read(root, rel)
        if not text:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for m in MARKER_RX.finditer(line):
                if set(m.group(1).split(",")) & PERSONAL_SCOPES \
                        and not any(rx.match(rel) for rx in named):
                    findings.append(Finding(
                        "unlisted-marker", rel, i,
                        "a personal-data allow-marker stands in a file no entry "
                        f"names ({m.group(1)}); a marker is not a grant"))
            for entry, rxs, strings in per_entry:
                if not strings or any(rx.match(rel) for rx in rxs):
                    continue
                if any(s in line for s in strings):
                    findings.append(Finding(
                        "unlisted-holder", rel, i,
                        f"{entry['id']}'s listed data stands in a file its entry "
                        "does not name"))
    return findings


def render(findings: list[Finding], *, blocking: bool, scope_note: str) -> str:
    until = PERSONAL_DATA_WARN_UNTIL.isoformat()
    lines: list[str] = []
    if scope_note:
        lines.append(report.clean_head(NAME, scope_note))
    elif not findings:
        lines.append(report.clean_head(NAME, "every listed place and marker checked."))
    elif blocking:
        lines.append(report.findings_head(
            NAME, len(findings), "closed-list finding(s)",
            " — blocked (only the principal grants an exception)."))
    else:
        lines.append(f"⚠ {NAME}: {len(findings)} closed-list finding(s) "
                     f"(warning; blocking from {until}).")
    for f in findings[:MAX_LISTED]:
        where = f.path + (f":{f.line}" if f.line else "")
        lines.append(f"  {where}  [{f.kind}] {report.safe_text(f.detail)}")
    if len(findings) > MAX_LISTED:
        lines.append(report.over_cap_line(len(findings) - MAX_LISTED, MAX_LISTED))
    if findings:
        lines.append(f"  Remove the data, or ask the principal for a grant and "
                     f"write it to {LIST_PATH}.")
    return "\n".join(lines)


def _main(argv: list[str] | None) -> int:
    ap = argparse.ArgumentParser(
        prog=NAME, description="In a public repo, personal data stands only "
                               "where the closed list names it.")
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--warn", action="store_true",
                    help="report findings but exit 0 for them")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the tool against its own fixtures, then exit")
    args = ap.parse_args(argv)
    if args.selftest:
        return report.quiet_selftest(NAME, _selftest)

    root = Path(args.root).resolve()
    rc = report.refuse_missing_root(NAME, root, args.root)
    if rc is not None:
        return rc

    if declared_public(root):
        findings = scan(root)
        scope_note = ""
    else:
        findings = []
        scope_note = ("not in scope - this repo does not declare "
                      '"visibility": "public" in .atelier-floor.json.')

    blocks = bool(findings) and not args.warn and not warn_only_today()
    reported_not_blocking = 0 if blocks else len(findings)

    if args.json:
        print(json.dumps({
            "clean": not blocks,
            "in_scope": not scope_note,
            "warn": args.warn,
            "blocking": blocks,
            "until": PERSONAL_DATA_WARN_UNTIL.isoformat(),
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        print(render(findings, blocking=blocks, scope_note=scope_note))
        print(report.advisory_count_line(NAME, reported_not_blocking))
        if args.warn and findings:
            print(report.WARN_NOTICE)
    return report.exit_code(blocks)


def main(argv: list[str] | None = None) -> int:
    return report.guarded_main(NAME, _main, argv, (ConfigError,))


def _selftest() -> int:
    fails: list[str] = []

    def check(name: str, got, want) -> None:
        if got != want:
            fails.append(f"{name}: got {got!r}, want {want!r}")

    entries = parse_list("## PD1 - x\n- **Data:** `abc`\n"
                         "- **May stand in:** `docs/*.md`, `README.md`\n")
    check("parsed one entry", len(entries), 1)
    check("pinned", pinned(entries[0]), ["abc"])
    check("glob stays in segment", bool(glob_rx("docs/*.md").match("docs/a/b.md")), False)
    check("glob matches", bool(glob_rx("docs/*.md").match("docs/a.md")), True)
    check("double star crosses", bool(glob_rx("docs/**").match("docs/a/b.md")), True)
    for f in fails:
        print(f"{NAME} selftest FAIL: {f}", file=sys.stderr)
    print(f"{NAME} selftest: {'FAILED' if fails else 'ok'} ({len(fails)} failure(s))")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
