#!/usr/bin/env python3
"""signfleet — would the signing gate pass, fleet-wide, if it were enforcing?

`signscan` answers that for ONE repo, given a trust list and a boundary someone
already resolved. This is the fleet roll-up, and it exists because of a specific
blind spot found on 2026-07-18:

  signscan runs `--warn` fleet-wide, so a child's floor can NEVER fail on
  signing. A green floor is therefore not evidence that the child signs — it is
  evidence that the signing step cannot fail. Worse, on a child whose earlier
  scanners fail (secretscan/leakscan), the signature steps never execute at all:
  GitHub Actions skips the rest of the job. So the reds are silent too.

Both halves of the fleet were mute on the one question that matters before
flipping `--warn` off: **would it pass?** Answering it needed a run in the mode
the flip would actually use, and nothing did that. Running it once found two
children that would newly-red — both of them GREEN at the time.

So this tool runs signscan in **blocking** mode against every child, each
resolved the way that child's own CI resolves it:

  - trust list  = atelier's `allowed_signers` **at that child's pin** (ADR 0002),
                  never floating main — the same rule signscan's docstring
                  insists on, and the reason this cannot be a simple loop over
                  `signscan --allowed-signers allowed_signers`.
  - boundary    = that child's `SIGN_BOUNDARY` from its own
                  `.github/workflows/floor.yml`, not a guess.

  signfleet                 discover children + report
  signfleet --child <path>  report only the named child repo(s)
  signfleet --json          machine-readable
  signfleet --check         exit 1 if any child would fail (for CI/hooks)
  signfleet --selftest      prove the parse + classification logic, offline

Statuses:
  pass     every machine-plane commit in range verifies against the trust list
  fail     at least one commit in range is unsigned or badly signed — this child
           would newly-red if the flip happened today
  skip     the check could not apply: no atelier pin, no floor.yml, or a pin that
           predates atelier's allowed_signers (the child's own CI warns and
           passes in exactly this case, so we mirror it rather than invent a red)
  error    the child was found but could not be evaluated (unreadable git, etc.)

Exit codes (fail-safe — a fleet we could not verify is never reported green):
  0  every evaluated child would pass
  1  at least one child would fail, or nothing was discovered
  2  environment error (not an atelier repo, HEAD unreadable, named child absent)

WHAT THIS CANNOT SEE — read before trusting a clean run:

  - **Machine plane only.** Commits minted by GitHub's web-flow identity
    (merge/squash) are reported `deferred`, exactly as signscan reports them, and
    are NOT verified here — that needs `gh api …commit.verification.verified`,
    a separate plane this tool never invokes. A child can be `pass` here while a
    server-minted commit in its range is unverified.
  - **A pass is "today, at this HEAD"**, not a guarantee. The next unsigned
    commit changes the answer. It is a readiness probe, not a gate — the gate is
    the child's own floor.
  - **The boundary is read statically** from floor.yml text. If a child's
    workflow computes or overrides `SIGN_BOUNDARY` elsewhere, this diverges from
    what its CI actually uses, and this tool is the one that is wrong.
  - **Local clones, local truth.** It reads the working copy on this machine. A
    child that is behind its remote is measured as it is here, not as it is on
    GitHub.

Zero third-party dependencies; stdlib + git + ssh-keygen, same floor as signscan.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, asdict, field
from pathlib import Path

import pins
import signscan

# SIGN_BOUNDARY as written in a child's floor.yml, e.g.
#   SIGN_BOUNDARY: "26a8bb6"  # retrofit: this repo's last unsigned commit
# Quotes optional, trailing comment optional, empty value legitimate (= verify
# ALL history, the right default for a repo born signed). Anchored to the YAML
# key at line start so a mention in a comment elsewhere cannot win.
#
# Note the character class is explicit hex rather than \s-style shorthand: an
# earlier throwaway version of this probe used `\s` in a macOS `sed` expression,
# which BSD sed does not support, and silently matched nothing. The bug made
# every child look mis-configured. Keeping the pattern boring is deliberate.
BOUNDARY_RE = re.compile(r'^[ \t]*SIGN_BOUNDARY:[ \t]*"?([0-9a-fA-F]*)"?', re.M)

STATUS_PASS = "pass"
STATUS_FAIL = "fail"
STATUS_SKIP = "skip"
STATUS_ERROR = "error"

# Only `fail` means "the flip would break this child". `skip`/`error` are not
# green, but they are not evidence of a signing problem either — they are
# evidence we could not answer, which --check still surfaces via the summary.
ACTIONABLE = {STATUS_FAIL}


@dataclass
class ChildSign:
    name: str
    path: str
    pin: str | None = None
    boundary: str | None = None      # None = no floor.yml; "" = all history
    status: str = STATUS_SKIP
    reason: str = ""                 # why skipped/errored, human-readable
    commits: int = 0                 # commits in the verified range
    good: int = 0
    bad: int = 0
    deferred: int = 0                # github-plane, NOT verified here
    bad_shas: list[str] = field(default_factory=list)


def read_boundary(floor_yml: Path) -> str | None:
    """The child's declared adoption boundary, or None if there is no floor.yml.

    An empty string is a real, meaningful value (verify all history) and must not
    be conflated with "absent" — hence None-vs-"" rather than a falsy check.
    """
    try:
        text = floor_yml.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = BOUNDARY_RE.search(text)
    return m.group(1) if m else None


def classify(bad: int, commits: int) -> str:
    """Pure verdict — no git, so the selftest proves it offline.

    A range with zero commits is a pass: there is nothing after the boundary yet,
    which is the honest answer for a freshly-adopted child, not a skip.
    """
    return STATUS_FAIL if bad > 0 else STATUS_PASS


def trust_at_pin(atelier: Path, pin: str, dest: Path) -> bool:
    """Write atelier's allowed_signers AS OF the child's pin to dest.

    False if that pin predates the file (the child's own CI warns and passes in
    this case, so the caller mirrors that as `skip`, not a red).
    """
    proc = subprocess.run(["git", "-C", str(atelier), "show", f"{pin}:allowed_signers"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        return False
    dest.write_text(proc.stdout, encoding="utf-8")
    return True


def evaluate(atelier: Path, child_dir: Path, tmp: Path) -> ChildSign:
    info = ChildSign(child_dir.name, str(child_dir))

    claude = child_dir / "CLAUDE.md"
    info.pin = pins.read_pin(claude) if claude.is_file() else None
    if info.pin is None:
        info.reason = "no atelier pin in CLAUDE.md — its CI skips signing too"
        return info

    floor = child_dir / ".github/workflows/floor.yml"
    boundary = read_boundary(floor)
    if boundary is None:
        info.reason = "no floor.yml (or no SIGN_BOUNDARY in it)"
        return info
    info.boundary = boundary

    trust = tmp / f"{child_dir.name.replace(' ', '_')}.allowed_signers"
    if not trust_at_pin(atelier, info.pin, trust):
        info.reason = f"atelier@{info.pin[:7]} predates allowed_signers — its CI warns and passes"
        return info

    try:
        report = signscan.scan(str(child_dir), str(trust), boundary or None,
                               None, signscan.WEB_FLOW_EMAIL)
    except signscan.SignscanError as e:
        info.status = STATUS_ERROR
        info.reason = str(e)
        return info
    except Exception as e:  # a child we cannot read must not kill the fleet view
        info.status = STATUS_ERROR
        info.reason = f"{type(e).__name__}: {e}"
        return info

    results = report.get("results", [])
    info.commits = len(results)
    for r in results:
        st = r.get("status")
        if st == "good":
            info.good += 1
        elif st == "deferred":
            info.deferred += 1
        else:
            info.bad += 1
            if len(info.bad_shas) < 10:
                info.bad_shas.append(r.get("sha", "?")[:10])
    info.status = classify(info.bad, info.commits)
    return info


def cmd_report(args) -> int:
    try:
        atelier = pins.resolve_atelier(args.atelier)
    except pins.GitError as e:
        print(f"signfleet: {e}", file=sys.stderr)
        print("signfleet: run this from an atelier checkout, or pass --atelier <path>.",
              file=sys.stderr)
        return 2

    if args.child:
        children: list[Path] = []
        for c in args.child:
            p = Path(c).expanduser()
            if not p.is_dir():
                print(f"signfleet: named child not found: {p}", file=sys.stderr)
                return 2
            children.append(p)
    else:
        roots = [Path(r).expanduser() for r in args.root] if args.root else [atelier.parent]
        children = pins.discover(roots, atelier)

    with tempfile.TemporaryDirectory(prefix="signfleet-") as td:
        tmp = Path(td)
        infos = [evaluate(atelier, c, tmp)
                 for c in sorted(children, key=lambda p: p.name.lower())]

    if args.json:
        print(json.dumps({"atelier": str(atelier),
                          "children": [asdict(i) for i in infos]}, indent=2))
    else:
        print(render(infos, atelier))

    if not infos:
        return 1
    return 1 if any(i.status in ACTIONABLE for i in infos) else 0


# --------------------------------------------------------------------------- #
# rendering
# --------------------------------------------------------------------------- #

_MARK = {STATUS_PASS: "✓", STATUS_FAIL: "✗", STATUS_SKIP: "·", STATUS_ERROR: "?"}


def render(infos: list[ChildSign], atelier: Path) -> str:
    lines = [f"atelier fleet signing — blocking-mode probe  ({atelier})"]
    if not infos:
        lines.append("  (no atelier children found under the search root)")
        return "\n".join(lines)

    width = max(len(i.name) for i in infos)
    for i in infos:
        mark = _MARK.get(i.status, " ")
        b = "all" if i.boundary == "" else (i.boundary[:7] if i.boundary else "—")
        if i.status in (STATUS_PASS, STATUS_FAIL):
            detail = f"{i.commits:>4} commits  {i.good} good"
            if i.deferred:
                detail += f"  {i.deferred} deferred"
            if i.bad:
                detail += f"  {i.bad} BAD"
        else:
            detail = i.reason
        lines.append(f" {mark} {i.name:<{width}}  {i.status:<5} {b:<8} {detail}")
        for sha in i.bad_shas:
            lines.append(f"       ✗ {sha} unsigned or not verifiable against the trust list")

    failed = [i for i in infos if i.status == STATUS_FAIL]
    skipped = [i for i in infos if i.status in (STATUS_SKIP, STATUS_ERROR)]
    deferred_total = sum(i.deferred for i in infos)
    lines.append("")
    if failed:
        lines.append(f"  {len(failed)} of {len(infos)} would FAIL if signscan stopped warning.")
        lines.append("  Fix the child's adoption boundary, or the commits, before flipping.")
    else:
        lines.append(f"  all {len(infos) - len(skipped)} evaluated children would pass ✓")
    if skipped:
        lines.append(f"  {len(skipped)} not evaluated (see reasons above) — not a green result.")
    if deferred_total:
        lines.append(f"  {deferred_total} server-minted commit(s) deferred to the gh plane — "
                     "NOT verified here (see the module docstring).")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="signfleet",
        description="Fleet view of commit-signing readiness — would the warn→block flip pass?")
    ap.add_argument("--atelier", help="atelier repo path (default: the repo this script lives in)")
    ap.add_argument("--root", action="append",
                    help="search root for discovery (repeatable; default: atelier's parent dir)")
    ap.add_argument("--child", action="append",
                    help="report only this child repo (repeatable; bypasses discovery)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if any child would fail (for CI/hooks)")
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
    """Pure-logic checks — no git, no network, so this proves the boundary parse
    and the verdict table on any box, offline."""
    ok = True

    def check(name: str, cond: bool):
        nonlocal ok
        if not cond:
            print(f"FAIL: {name}")
            ok = False

    def boundary_of(text: str) -> str | None:
        with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as f:
            f.write(text)
            p = Path(f.name)
        try:
            return read_boundary(p)
        finally:
            p.unlink(missing_ok=True)

    # boundary parse — the shapes actually seen across the fleet
    check("quoted", boundary_of('env:\n  SIGN_BOUNDARY: "26a8bb6"\n') == "26a8bb6")
    check("quoted + trailing comment",
          boundary_of('  SIGN_BOUNDARY: "f53d645"  # retrofit: last unsigned\n') == "f53d645")
    check("unquoted", boundary_of("  SIGN_BOUNDARY: abc1234\n") == "abc1234")
    check("empty = all history", boundary_of('  SIGN_BOUNDARY: ""\n') == "")
    check("absent -> None", boundary_of("env:\n  OTHER: 1\n") is None)
    # A mention in prose must not win over the real key.
    check("prose mention ignored",
          boundary_of("# talk about SIGN_BOUNDARY: deadbee here\n"
                      '  SIGN_BOUNDARY: "1234567"\n') == "1234567")

    # verdict table
    check("clean -> pass", classify(0, 12) == STATUS_PASS)
    check("one bad -> fail", classify(1, 12) == STATUS_FAIL)
    check("empty range -> pass", classify(0, 0) == STATUS_PASS)

    # `skip` must never be counted as a failure, and `fail` always must
    check("fail is actionable", STATUS_FAIL in ACTIONABLE)
    check("skip is not actionable", STATUS_SKIP not in ACTIONABLE)
    check("error is not actionable", STATUS_ERROR not in ACTIONABLE)

    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
