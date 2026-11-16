#!/usr/bin/env python3
"""flipcheck — a read-only report of the pre-flip platform settings (260/130).

Before a repo goes public, `docs/method/AUTONOMY.md`'s gate reads five GitHub
settings the tracked tree cannot show: the wiki, the Actions policy, fork-PR
approval, private vulnerability reporting, and rulesets or branch protection.
`publishscan` judges the path set and cannot see a setting; this reads them.

  flipcheck <owner/name> [<owner/name> ...]    one table per repo
  flipcheck --json <owner/name> ...            the same, machine-readable

Report only. It makes `gh api` GET calls and nothing else: no PATCH, PUT, POST
or DELETE exists in this file, and a test pins that. It records the value it
read so the gate can put it in front of the confirmation where no house value
is ruled (Actions policy, fork-PR approval); for the wiki (off) and private
vulnerability reporting (enabled) it adds the house value and whether the read
matches it.

A SETTING IT CANNOT READ SAYS SO. Fork-PR approval and branch protection cannot
be read as set on a private free-plan repo (a 403 or 404), and a token without
admin rights is refused too. Each such read prints `not available` with the
reason `gh` gave, and the run carries on. It never reads as "set", never reads as
"off", and never fails the run: a read we could not make is not an answer in
either direction (the rule `floorfleet._gh_json` already states). A setting with
several reads, one of them refused, is `partial`: the parts it did read are
printed beside the part it could not.

Exit codes: 0 the report was printed (whatever it could not read); 2 a repo
argument is not `owner/name`. There is no exit 1, because nothing here is a
verdict. The gate's judgement stays with the session that follows it.

WHAT THIS CANNOT SEE. It reads one moment: a setting changed after the run is
not in it, and the gate's own "flip and harden are one sitting" rule exists
because the read-back after the flip is a second run. It reads the repo's own
settings, not an organisation's: an organisation policy that overrides the
repo's Actions permissions is not in `actions/permissions`. It does not judge
whether a value is right where no house value is ruled.

Zero third-party dependencies; `gh` must be installed and authenticated. The `gh`
runner is `floorfleet._gh_run`, so a missing `gh` is one documented ending
(every setting `not available`) and not a traceback.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from dataclasses import dataclass, field, asdict

import floorfleet  # noqa: E402  — the gh runner and the HTTP status pattern

SLUG_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")

READ = "read"
PARTIAL = "partial"
NA = "not available"
NO_HOUSE = ("no house value ruled: the value read goes in front of the "
            "confirmation")


@dataclass
class Part:
    """One `gh api` read inside a setting."""
    name: str
    value: str | None   # what was read; None when the read could not be made
    reason: str | None = None  # why it could not be, when value is None


@dataclass
class Setting:
    key: str
    label: str
    status: str                      # read | partial | not available
    value: str
    house: str                       # the ruled house value, or a pointer
    matches_house: bool | None       # None where no house value is ruled
    parts: list[Part] = field(default_factory=list)


def _get(path: str) -> tuple[object | None, str | None]:
    """One GET. (parsed JSON, None) on success, (None, reason) otherwise.

    The reason is `gh`'s own stderr line less the `gh: ` prefix, so a 403 that
    says "Upgrade to GitHub Pro or make this repository public" reaches the
    report as written. `gh api` with no `--method` is a GET; nothing else is
    ever passed (a test pins it)."""
    r = floorfleet._gh_run(["api", path])
    if r is None:
        return None, "gh could not be run (not installed?)"
    if r.returncode != 0:
        line = (r.stderr or "").strip().splitlines()
        text = line[0].strip() if line else "gh api failed"
        if text.startswith("gh: "):
            text = text[4:]
        m = floorfleet.HTTP_STATUS_RE.search(text)
        if m is None:
            text = f"{text} (no HTTP status)"
        return None, text
    try:
        return json.loads(r.stdout), None
    except ValueError:
        return None, "unparseable response"


def _yes(v: object) -> str:
    return "ON" if v is True else "off" if v is False else f"unexpected {v!r}"


def _roll(parts: list[Part]) -> str:
    got = [p for p in parts if p.value is not None]
    if len(got) == len(parts):
        return READ
    return PARTIAL if got else NA


def _value(parts: list[Part]) -> str:
    return "; ".join(
        f"{p.name}: {p.value}" if p.value is not None
        else f"{p.name}: not available ({p.reason})" for p in parts)


def read_wiki(repo: object | None, why: str | None) -> Setting:
    if not isinstance(repo, dict) or "has_wiki" not in repo:
        parts = [Part("has_wiki", None, why or "field absent from the response")]
        return Setting("wiki", "Wiki", NA, _value(parts),
                       "off (a second git repo the floor never sees)", None, parts)
    v = repo["has_wiki"]
    parts = [Part("has_wiki", _yes(v))]
    return Setting("wiki", "Wiki", READ, _value(parts),
                   "off (a second git repo the floor never sees)",
                   v is False, parts)


def read_actions_policy(slug: str) -> Setting:
    parts: list[Part] = []
    perms, why = _get(f"repos/{slug}/actions/permissions")
    for k in ("enabled", "allowed_actions", "sha_pinning_required"):
        if isinstance(perms, dict) and k in perms:
            parts.append(Part(k, str(perms[k]).lower()))
        else:
            # allowed_actions is legitimately absent when Actions is disabled;
            # an absent key on a good response is still "not read", not "none".
            parts.append(Part(k, None, why or "field absent from the response"))
    wf, why = _get(f"repos/{slug}/actions/permissions/workflow")
    for k in ("default_workflow_permissions", "can_approve_pull_request_reviews"):
        if isinstance(wf, dict) and k in wf:
            parts.append(Part(k, str(wf[k]).lower()))
        else:
            parts.append(Part(k, None, why or "field absent from the response"))
    return Setting("actions_policy", "Actions policy", _roll(parts),
                   _value(parts), NO_HOUSE, None, parts)


def read_fork_pr_approval(slug: str) -> Setting:
    data, why = _get(
        f"repos/{slug}/actions/permissions/fork-pr-contributor-approval")
    if isinstance(data, dict) and "approval_policy" in data:
        parts = [Part("approval_policy", str(data["approval_policy"]))]
    else:
        parts = [Part("approval_policy", None,
                      why or "field absent from the response")]
    return Setting("fork_pr_approval", "Fork-PR approval", _roll(parts),
                   _value(parts), NO_HOUSE, None, parts)


def read_pvr(slug: str) -> Setting:
    data, why = _get(f"repos/{slug}/private-vulnerability-reporting")
    if isinstance(data, dict) and isinstance(data.get("enabled"), bool):
        v = data["enabled"]
        parts = [Part("enabled", str(v).lower())]
        return Setting("private_vulnerability_reporting",
                       "Private vulnerability reporting", READ, _value(parts),
                       "enabled: true", v is True, parts)
    parts = [Part("enabled", None, why or "field absent from the response")]
    return Setting("private_vulnerability_reporting",
                   "Private vulnerability reporting", NA, _value(parts),
                   "enabled: true", None, parts)


def read_protection(slug: str, branch: str | None,
                    branch_why: str | None) -> Setting:
    parts: list[Part] = []

    rulesets, why = _get(f"repos/{slug}/rulesets")
    if isinstance(rulesets, list):
        active = sum(1 for r in rulesets
                     if isinstance(r, dict) and r.get("enforcement") == "active")
        parts.append(Part("rulesets", f"{len(rulesets)} ({active} active)"))
    else:
        parts.append(Part("rulesets", None, why or "not a list"))

    if branch is None:
        why = f"default branch unknown ({branch_why})"
        parts.append(Part("rules on the default branch", None, why))
        parts.append(Part("classic branch protection", None, why))
    else:
        rules, why = _get(f"repos/{slug}/rules/branches/{branch}")
        if isinstance(rules, list):
            types = sorted({r.get("type", "?") for r in rules
                            if isinstance(r, dict)})
            parts.append(Part(f"rules on {branch}",
                              ", ".join(types) if types else "none"))
        else:
            parts.append(Part(f"rules on {branch}", None, why or "not a list"))

        prot, why = _get(f"repos/{slug}/branches/{branch}/protection")
        if isinstance(prot, dict):
            parts.append(Part(f"classic protection on {branch}", "set"))
        elif why is not None and "Branch not protected" in why:
            # A real answer: the endpoint says there is none. Not the 403 that
            # says the plan cannot be asked.
            parts.append(Part(f"classic protection on {branch}", "none"))
        else:
            parts.append(Part(f"classic protection on {branch}", None,
                              why or "not an object"))
    return Setting("protection", "Rulesets / branch protection", _roll(parts),
                   _value(parts), NO_HOUSE, None, parts)


def read_repo(slug: str) -> dict:
    repo, why = _get(f"repos/{slug}")
    branch = None
    visibility = None
    if isinstance(repo, dict):
        visibility = repo.get("visibility")
        branch = repo.get("default_branch")
    settings = [
        read_wiki(repo, why),
        read_actions_policy(slug),
        read_fork_pr_approval(slug),
        read_pvr(slug),
        read_protection(slug, branch if isinstance(branch, str) else None,
                        why or "field absent from the response"),
    ]
    return {"repo": slug, "visibility": visibility,
            "default_branch": branch,
            "settings": [asdict(s) for s in settings]}


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%MZ")


def render(report: dict) -> str:
    """A table: one row per read, the setting's label and status on its first
    row; the house values (and whether each read matches) follow under it."""
    rows: list[tuple[str, ...]] = [("Setting", "Status", "Read", "Value")]
    for s in report["settings"]:
        for i, p in enumerate(s["parts"]):
            val = (p["value"] if p["value"] is not None
                   else f"not available ({p['reason']})")
            rows.append((s["label"] if i == 0 else "",
                         s["status"] if i == 0 else "", p["name"], val))
    w = [max(len(r[c]) for r in rows) for c in range(4)]
    lines = [f"flipcheck: {report['repo']}  "
             f"visibility={report['visibility'] or 'not available'}  "
             f"read {report['read_at']}  (read-only: gh api GET)", ""]
    for n, r in enumerate(rows):
        lines.append(("  " + "  ".join(
            c.ljust(w[i]) for i, c in enumerate(r))).rstrip())
        if n == 0:
            lines.append("  " + "  ".join("-" * x for x in w))
    lines.append("")
    lines.append("  House values:")
    for s in report["settings"]:
        if s["matches_house"] is None:
            verdict = ""
        else:
            verdict = " -> " + ("matches" if s["matches_house"] else "DIFFERS")
        lines.append(f"    {s['label']}: {s['house']}{verdict}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="flipcheck",
        description="Read-only report of the five pre-flip GitHub settings "
                    "for each named repo (gh api GET calls only). A setting "
                    "that cannot be read prints 'not available' and the "
                    "reason; the run never fails on one.")
    p.add_argument("repos", nargs="+", metavar="owner/name")
    p.add_argument("--json", action="store_true", help="machine-readable")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    bad = [r for r in args.repos if not SLUG_RE.match(r)]
    if bad:
        print("flipcheck: not an owner/name repo: " + ", ".join(bad),
              file=sys.stderr)
        return 2
    now = _now()
    reports = []
    for slug in args.repos:
        rep = read_repo(slug)
        rep["read_at"] = now
        reports.append(rep)
    if args.json:
        print(json.dumps({"read_only": True, "repos": reports}, indent=2))
    else:
        print("\n\n".join(render(r) for r in reports))
    return 0


if __name__ == "__main__":
    sys.exit(main())
