#!/usr/bin/env python3
"""floor — ONE list of which policy checks run, for every repo and every caller.

WHY THIS FILE EXISTS (the bug it closes, 2026-07-25)
----------------------------------------------------
atelier's scanners were already one-source: a child vendors no scanner code, and
CI fetches `atelier@main` at run time. But the *list of which scanners run* was
copied into every child — 247 lines of `floor.yml` per repo, plus four hard-coded
`run_scan` lines in each clone's pre-commit hook. Code was shared; **policy was
vendored**.

The consequence, measured across the estate on 2026-07-25: of 13 children, 12
carried a `floor.yml` frozen at scaffold time and therefore ran **none** of the
five guards added since — sizescan, datescan, wrapscan, spellscan, reviewscan.
One of those five (sizescan's harvest-integrity gate) had been live in atelier
since 2026-07-22, built after a real incident, and had never executed anywhere
but atelier. When it was finally pointed at one child it found exactly the seven
buried items that child had just spent a session reconstructing by hand.

Nobody was careless. The mechanism simply had no way to reach a repo that had
already been scaffolded, and "remember to update the children" is not a
mechanism. So the fix is not a reminder — it is to leave nothing in the child to
update. This module is the list; the child holds a caller that names no scanner
at all.

That is `PROPAGATION.md`'s own **thin anchor, fat pointer** applied to the
enforcement layer, where it had only ever been applied to doctrine prose. The
same file's closing clause warns "do not mistake the anchor for the enforcement";
the enforcement was the half that got vendored.

THE PLANES — the same policy, two honestly different covers
------------------------------------------------------------
A scanner is not invoked identically everywhere, and pretending otherwise would
be the wrong kind of uniformity:

  hook  a pre-commit gate on a real machine. Boundary scanners read only the
        STAGED diff so the commit hot path stays fast, and leakscan has its
        machine-local term list, so its cover is FULL.
  ci    a backstop on a runner nobody configured. Reads the whole TREE (the
        scanners read files, not the log, and a rename breaks a link outside the
        diff). leakscan runs STRUCTURAL-ONLY here and always will: its literal
        person/estate term list is machine-local by design and must never enter
        a repo or a runner (`SECRETS.md`). A degraded, *declared* CI cover is the
        honest answer; the full cover lives on the hook.

Both planes read this one registry, so a scanner added here reaches every child's
hook and every child's CI at once, with no child edit.

NOTHING IS SILENTLY ABSENT
--------------------------
The old opt-out was "delete the run_scan line" — invisible the moment it was
done, and indistinguishable from a line that was never added. Here a child that
does not enforce a check must SAY SO, in a committed file
(`.atelier-floor.json`), in one of exactly two declared states:

  advisory   the check runs and reports, but does not block. For a repo
             RE-BASELINING onto a newly-adopted hygiene check — the first red is
             the signal, and this is how you keep the signal while you work
             through it. Tracked debt, not a hole.
  disabled   the check does not run. A deliberate, reviewable choice on the
             record, with a stated reason.

`floorfleet.py` reads those declarations across the estate and shows them, so
"this repo is not enforcing X" is a visible board state rather than an absence
nobody can see. **A guard that is off and known is a decision; a guard that is
off and unseen is the failure this file exists to end.**

Which checks may be softened is NOT the child's call. The boundary scanners
(secretscan, leakscan) and the integrity scanners (linkscan, reviewscan,
sizescan) have no advisory form here: a burned secret, a leaked personal fact and
a botched harvest are not re-baselining problems. Only the prose-hygiene checks
(datescan, wrapscan, spellscan) carry one, because adopting them genuinely does
demand a one-off cleanup pass. Asking for an advisory state that a scanner does
not offer is an error, not a silent downgrade.

FAIL CLOSED
-----------
A gate whose whole job is to block bad commits must not pass silently when its
scanner is missing — that defeats it exactly when it matters most (a child with
no scanners of its own). A missing scanner BLOCKS, with the remedy printed. So
does an unparseable config, an unknown scanner name, and an advisory request for
a scanner that has no advisory form.

WHAT THIS CANNOT SEE — read before trusting a clean run
--------------------------------------------------------
- It runs the scanners; it does not improve them. Every structural blind spot in
  `tools/README.md` ("What these scans cannot see") applies unchanged, and a
  green floor still means "no known shape matched", never "safe to publish".
- It proves the checks ran HERE, in this invocation. Whether a given child's CI
  is wired to call it at all is a different question, and deliberately a
  different tool's job — `floorfleet.py`. This file cannot detect its own
  absence.
- signscan is NOT in this registry. It needs a trust list resolved from the
  child's own atelier pin (never floating main — a floated trust root would let
  anyone with write to atelier mint trust for every child, 2026-07-12 review G7)
  plus a second GitHub-API plane for web-flow commits. It is not a tree scanner
  and forcing it into this shape would misrepresent what it does, so it stays as
  explicit steps in the reusable workflow.
- licenscan is a PUBLISH gate, not an always-on floor: with no LICENSE it
  hard-fails ("all-rights-reserved"), which is right before going public and
  wrong for a private pre-licence repo. It runs only when a child declares the
  licence it expects.

Usage:
  floor.py --plane hook --root <repo>    the pre-commit gate (staged, full cover)
  floor.py --plane ci   --root <repo>    the CI backstop (whole tree)
  floor.py --list                        show the registry and exit
  floor.py --selftest                    prove the logic offline, then exit
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

CONFIG_NAME = ".atelier-floor.json"

# Placeholders resolved per invocation: {root} = the repo being scanned,
# {docs} = its records tree (configurable — not every child keeps records in
# docs/), {licence} = the SPDX id a publish-ready repo asserts.


@dataclass(frozen=True)
class Scanner:
    """One check, and exactly how each plane invokes it.

    `hook`/`ci` are argument templates; a None plane means the check does not run
    there at all. `advisory` is the argument form that reports without blocking —
    None means this check may not be softened (see the module docstring: boundary
    and integrity checks have no advisory form, by design).

    `{scope}` is the tree the check reads. `default_scope` says what that is when
    the child declares nothing: the whole repo, or its records subtree.
    """

    name: str
    hook: list[str] | None
    ci: list[str] | None
    advisory: list[str] | None
    why: str
    default_scope: str = "root"  # "root" | "docs"
    opt_in: bool = False  # runs only when the child's config asks for it


# The registry. Adding a line here is how a new policy reaches the whole estate.
SCANNERS: tuple[Scanner, ...] = (
    Scanner(
        "secretscan",
        hook=["--staged", "--root", "{root}", "{scope}"],
        ci=["--root", "{root}", "{scope}"],
        advisory=None,  # a burned secret is burned whatever the repo's visibility
        why="no plaintext credential enters git history",
    ),
    Scanner(
        "leakscan",
        hook=["--staged", "--root", "{root}", "{scope}"],
        ci=["--root", "{root}", "{scope}"],  # structural-only: no --require-terms
        advisory=None,  # the personal-data boundary is not a re-baselining matter
        why="no personal/estate data enters a repo that can go public",
    ),
    Scanner(
        "linkscan",
        hook=["--root", "{root}", "{scope}"],  # whole tree: a rename breaks links
        ci=["--root", "{root}", "{scope}"],    # outside the diff that caused it
        advisory=None,
        why="internal links resolve — thin anchor, fat pointer needs live pointers",
    ),
    Scanner(
        "reviewscan",
        hook=["--root", "{root}", "{scope}"],
        ci=["--root", "{root}", "{scope}"],
        advisory=None,  # REVIEW.md: omission IS the bug, so it cannot be advisory
        why="a new decision record states its review judgement",
    ),
    Scanner(
        "sizescan",
        hook=["--check", "--root", "{root}", "{scope}"],
        ci=["--check", "--root", "{root}", "{scope}"],
        advisory=["--root", "{root}", "{scope}"],  # drop --check
        why="current-truth files stay honest; archive stores hold no live state",
    ),
    Scanner(
        "datescan",
        hook=["--root", "{root}", "{scope}"],
        ci=["--root", "{root}", "{scope}"],
        advisory=["--warn", "--root", "{root}", "{scope}"],
        why="records date in absolute UTC, never a drifting 'today'",
        default_scope="docs",
    ),
    Scanner(
        "wrapscan",
        hook=["--root", "{root}", "{scope}"],
        ci=["--root", "{root}", "{scope}"],
        advisory=["--warn", "--root", "{root}", "{scope}"],
        why="doctrine prose stays within its column budget",
        default_scope="docs",
    ),
    Scanner(
        "spellscan",
        hook=["--root", "{root}", "{scope}"],
        ci=["--root", "{root}", "{scope}"],
        advisory=["--warn", "--root", "{root}", "{scope}"],
        why="NZ-English spelling across the doc surface",
        default_scope="docs",
    ),
    Scanner(
        "licenscan",
        hook=["--expect", "{licence}", "{scope}"],
        ci=["--expect", "{licence}", "{scope}"],
        advisory=None,
        why="the declared licence is the one actually asserted",
        opt_in=True,  # only with a declared `licence` — see the docstring
    ),
)

# Flags a child may NOT add through `flags`. Each would change what a check
# MEANS rather than where it looks — and would do it invisibly, which is the one
# thing this design refuses. Softening has exactly one declared spelling
# (`advisory`), and it is validated against the scanner's own advisory form.
FORBIDDEN_FLAGS = {"--warn", "--check", "--selftest", "--json"}

BY_NAME = {s.name: s for s in SCANNERS}


class ConfigError(RuntimeError):
    """A child's floor config is unusable. Fail closed — never scan on a guess."""


@dataclass
class Config:
    docs: str = "docs"
    licence: str | None = None
    advisory: tuple[str, ...] = ()
    disabled: dict[str, str] = field(default_factory=dict)  # name -> reason
    # Per-scanner overrides of WHERE a check looks. atelier itself needs this
    # (its prose checks are scoped to the doctrine surface, not all of docs/) and
    # so does any repo whose shareable subtree is narrower than its whole tree —
    # a networking repo scanning only the part that can go public, say. Modelling
    # it as config rather than special-casing the parent is what lets atelier run
    # the SAME floor it ships: a parent with its own private list would be the
    # two-lists bug all over again, one level up.
    scope: dict[str, tuple[str, ...]] = field(default_factory=dict)
    # Per-scanner extra arguments — for a check that needs tuning to a repo's
    # subject matter rather than its layout. A networking repo disabling
    # leakscan's IP/MAC rules is the worked case: those shapes are legitimate
    # CONTENT there, not leaked estate data. This genuinely weakens a check,
    # which is why it lives in a committed file that `floorfleet` reads out
    # estate-wide — declared and visible, never quietly applied.
    flags: dict[str, tuple[str, ...]] = field(default_factory=dict)

    @staticmethod
    def load(root: Path) -> "Config":
        """Read `.atelier-floor.json` if present. Absent = full enforcement, which
        is the right default: a repo that has declared nothing has opted out of
        nothing."""
        path = root / CONFIG_NAME
        if not path.is_file():
            return Config()
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            raise ConfigError(f"{CONFIG_NAME} is unreadable: {e}") from e
        if not isinstance(raw, dict):
            raise ConfigError(f"{CONFIG_NAME} must be a JSON object")

        docs = raw.get("docs", "docs")
        licence = raw.get("licence") or None
        advisory = tuple(raw.get("advisory", []) or ())

        # `disabled` takes {name: reason}. A bare list is refused rather than
        # accepted with an empty reason: the reason is the whole point of making
        # an opt-out visible, so a reasonless one is a config bug, not a default.
        raw_disabled = raw.get("disabled", {}) or {}
        if isinstance(raw_disabled, list):
            raise ConfigError(
                f"{CONFIG_NAME}: `disabled` must be an object of "
                '{"scanner": "why"} — a disabled check states its reason'
            )
        if not isinstance(raw_disabled, dict):
            raise ConfigError(f"{CONFIG_NAME}: `disabled` must be an object")
        disabled = {k: str(v) for k, v in raw_disabled.items()}

        def _str_map(key: str, allow_empty: bool) -> dict[str, tuple[str, ...]]:
            raw_map = raw.get(key, {}) or {}
            if not isinstance(raw_map, dict):
                raise ConfigError(f"{CONFIG_NAME}: `{key}` must be an object")
            out: dict[str, tuple[str, ...]] = {}
            for k, v in raw_map.items():
                entries = [v] if isinstance(v, str) else list(v or ())
                if not entries and not allow_empty:
                    raise ConfigError(
                        f"{CONFIG_NAME}: `{key}.{k}` is empty — an override that "
                        "narrows a check to nothing is a silent hole, not a scope"
                    )
                out[k] = tuple(str(e) for e in entries)
            return out

        cfg = Config(docs=docs, licence=licence, advisory=advisory,
                     disabled=disabled,
                     scope=_str_map("scope", allow_empty=False),
                     flags=_str_map("flags", allow_empty=False))
        cfg.validate()
        return cfg

    def validate(self) -> None:
        """Reject a config that does not mean what it says. Every one of these is
        a block, not a warning — a floor that quietly ignores half its config is
        worse than no config, because it reads as covered."""
        for name in (*self.advisory, *self.disabled, *self.scope, *self.flags):
            if name not in BY_NAME:
                raise ConfigError(
                    f"{CONFIG_NAME}: unknown scanner {name!r} "
                    f"(known: {', '.join(sorted(BY_NAME))})"
                )
        for name in self.advisory:
            if name in self.disabled:
                raise ConfigError(
                    f"{CONFIG_NAME}: {name!r} is both advisory and disabled — pick one"
                )
            if BY_NAME[name].advisory is None:
                raise ConfigError(
                    f"{CONFIG_NAME}: {name!r} has no advisory form and may not be "
                    "softened — it is a boundary or integrity check. Fix the "
                    "finding, or disable it deliberately with a stated reason."
                )
        for name, reason in self.disabled.items():
            if not reason.strip():
                raise ConfigError(
                    f"{CONFIG_NAME}: disabling {name!r} needs a stated reason"
                )
        # A flag that changes what a check MEANS is not a scoping decision, and
        # must not be reachable by this route: `--warn` here would be a silent
        # advisory downgrade that bypasses every guard on `advisory` above.
        for name, extra in self.flags.items():
            bad = sorted(FORBIDDEN_FLAGS.intersection(extra))
            if bad:
                raise ConfigError(
                    f"{CONFIG_NAME}: `flags.{name}` may not contain "
                    f"{', '.join(bad)} — that changes what the check means, not "
                    "where it looks. To soften a check, declare it `advisory`."
                )


@dataclass
class Result:
    name: str
    state: str  # enforced | advisory | disabled | skipped
    rc: int
    reason: str = ""

    @property
    def failed(self) -> bool:
        return self.state == "enforced" and self.rc != 0


def resolve_tools_dir(explicit: str | None) -> Path:
    """Where atelier's scanners live. Env wins (so a test or CI run can redirect
    without touching a repo's config), then the baked git config, then this
    file's own directory — which is the answer inside atelier itself."""
    for candidate in (
        explicit,
        os.environ.get("ATELIER_TOOLS"),
        _git_config("hooks.atelierTools"),
    ):
        if candidate:
            return Path(candidate).expanduser()
    return Path(__file__).resolve().parent


def _git_config(key: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", "config", "--get", key],
            capture_output=True, text=True, check=False,
        )
        return out.stdout.strip() or None
    except OSError:
        return None


def subtrees(root: Path, cfg: Config, name: str) -> list[str]:
    """The paths a check reads in this repo: the scanner's own `scope` override
    if it declared one, else its registered default — the whole repo, or the
    repo's records tree."""
    override = cfg.scope.get(name)
    if override:
        return list(override)
    scanner = BY_NAME.get(name)
    if scanner is not None and scanner.default_scope == "docs":
        return [cfg.docs]
    return ["."]


def _render(args: list[str], root: Path, cfg: Config,
            name: str | None = None,
            trees: list[str] | None = None) -> list[str]:
    """Resolve an argument template against a repo. `{scope}` expands to EVERY
    path the check reads — which is why this returns a list rather than mapping
    arg-for-arg. A child's extra `flags` are appended LAST, so they can add to
    the template's arguments but never displace them."""
    paths = trees if trees is not None else subtrees(root, cfg, name or "")

    # STAGED MODE TAKES REPO-RELATIVE PATHS, and this is a genuine sharp edge.
    # secretscan/leakscan filter the staged diff by PREFIX against git's own
    # path list, which is always repo-relative. An absolute path (or a bare ".")
    # therefore matches nothing at all — and a scan that matches nothing exits 0,
    # so the failure looks exactly like a clean pass. Caught here by the planted-
    # secret tests in test_precommit.py, which is the only reason it is not
    # shipping: the first draft of this function rendered absolute paths for both
    # planes and every boundary check silently passed.
    if "--staged" in args:
        scoped = [p.strip("/") for p in paths if p not in (".", "")]
    else:
        scoped = [str((root / p).resolve()) for p in paths] or [str(root)]

    out: list[str] = []
    for a in args:
        if a == "{scope}":
            out.extend(scoped)  # empty in staged mode = the whole staged diff
            continue
        out.append(a.format(root=str(root),
                            scope=scoped[0] if scoped else str(root),
                            licence=cfg.licence or ""))
    out.extend(cfg.flags.get(name or "", ()))
    return out


def plan(plane: str, cfg: Config) -> list[tuple[Scanner, str]]:
    """Decide what runs, in what state, before running anything. Kept separate
    from execution so `--list` and the selftest can prove the decision without
    invoking a single scanner."""
    out: list[tuple[Scanner, str]] = []
    for s in SCANNERS:
        args = s.hook if plane == "hook" else s.ci
        if args is None:
            continue
        if s.name in cfg.disabled:
            out.append((s, "disabled"))
        elif s.opt_in and not cfg.licence:
            out.append((s, "skipped"))
        elif s.name in cfg.advisory:
            out.append((s, "advisory"))
        else:
            out.append((s, "enforced"))
    return out


def run(plane: str, root: Path, tools: Path, cfg: Config, ci: bool,
        json_mode: bool = False) -> list[Result]:
    """Run the plan. In `--json` mode the scanners' own reports are routed to
    stderr so stdout carries nothing but the JSON document — a caller parsing
    this must not have to strip nine scanners' prose out of it first."""
    child_stdout = sys.stderr if json_mode else None
    results: list[Result] = []
    for scanner, state in plan(plane, cfg):
        if state == "disabled":
            results.append(Result(scanner.name, state, 0, cfg.disabled[scanner.name]))
            continue
        if state == "skipped":
            results.append(Result(scanner.name, state, 0, "no licence declared"))
            continue

        path = tools / f"{scanner.name}.py"
        if not path.is_file():
            # Fail closed, loudly. This is the case the whole design exists for:
            # a child pointed at a tools dir that isn't there must NOT sail past.
            print(
                f"floor: {scanner.name}.py not found under {tools} — BLOCKING "
                "(fail closed).\n"
                "  The scanners live in atelier's tools/. Point at them with:\n"
                "    git config hooks.atelierTools <atelier-path>/tools\n"
                "  or set ATELIER_TOOLS in the environment.",
                file=sys.stderr,
            )
            results.append(Result(scanner.name, "enforced", 1, "scanner missing"))
            continue

        base = scanner.advisory if state == "advisory" else (
            scanner.hook if plane == "hook" else scanner.ci
        )

        # A check scoped to a subtree has nothing to read in a repo that keeps
        # none. The scanners exit 2 (environment error) on a missing path, which
        # would block every code-only repo — so skip, but SAY SO, and let
        # floorfleet surface it estate-wide. A repo whose records simply live
        # somewhere else sets `docs` (or a per-scanner `scope`); this branch is
        # what makes that misconfiguration visible instead of silently uncovered.
        declared = subtrees(root, cfg, scanner.name)
        trees = [p for p in declared if (root / p).exists()]
        if not trees:
            results.append(Result(scanner.name, "skipped", 0,
                                  f"no {', '.join(declared)} tree in this repo"))
            continue

        argv = [sys.executable, str(path),
                *_render(base, root, cfg, scanner.name, trees)]
        # Actions' workflow commands go to the SAME stream the scanners' own
        # prose does (`child_stdout`: stderr under --json, stdout otherwise) —
        # not unconditionally to stdout. Under --json, stdout is reserved for
        # the JSON document by this function's contract above, and grouping
        # markers written there corrupt it for every caller inside Actions
        # (`json.loads` on a `::group::` line). Real CI invokes floor.py without
        # --json, so grouping still renders exactly where it is consumed.
        if ci:
            print(f"::group::{scanner.name} ({state})", file=child_stdout, flush=True)
        rc = subprocess.run(argv, check=False, stdout=child_stdout).returncode
        if ci:
            print("::endgroup::", file=child_stdout, flush=True)
            if rc != 0 and state == "enforced":
                print(f"::error::{scanner.name} failed — {scanner.why}",
                      file=child_stdout, flush=True)
        results.append(Result(scanner.name, state, rc))
    return results


def render(results: list[Result], plane: str) -> str:
    icon = {"enforced": "✅", "advisory": "⚠️ ", "disabled": "⏭ ", "skipped": "⏭ "}
    lines = [f"atelier floor — {plane} plane"]
    for r in results:
        mark = "❌" if r.failed else icon[r.state]
        note = f"  ({r.reason})" if r.reason else ""
        lines.append(f"  {mark} {r.name:<11} {r.state}{note}")
    bad = [r.name for r in results if r.failed]
    if bad:
        lines.append("")
        lines.append(f"BLOCKED by: {', '.join(bad)}")
        lines.append(
            "Fix the finding(s) above — remove and ROTATE a real secret, fix a "
            "broken link,\nharvest a stranded item — or exempt a false positive "
            "with the scanner's\n`<name>:allow: <reason>` line marker or a "
            "`.<name>ignore` glob, then retry."
        )
    return "\n".join(lines)


def _selftest() -> int:
    """Prove the decision logic offline — no scanner is invoked. What matters
    here is that the config cannot quietly mean less than it says."""
    import tempfile

    fails: list[str] = []

    def check(label: str, cond: bool) -> None:
        if not cond:
            fails.append(label)

    # Every registered scanner runs on both planes unless deliberately absent.
    for s in SCANNERS:
        check(f"{s.name} has a hook form", s.hook is not None)
        check(f"{s.name} has a ci form", s.ci is not None)

    # The boundary/integrity checks must have NO advisory form — this is the
    # rule the whole "nothing is silently absent" design rests on.
    for name in ("secretscan", "leakscan", "linkscan", "reviewscan"):
        check(f"{name} cannot be softened", BY_NAME[name].advisory is None)
    for name in ("sizescan", "datescan", "wrapscan", "spellscan"):
        check(f"{name} can re-baseline", BY_NAME[name].advisory is not None)

    default = Config()
    states = {s.name: st for s, st in plan("ci", default)}
    check("default enforces secretscan", states["secretscan"] == "enforced")
    check("default enforces sizescan", states["sizescan"] == "enforced")
    check("licenscan is opt-in", states["licenscan"] == "skipped")

    cfg = Config(advisory=("wrapscan",), disabled={"spellscan": "no prose"})
    states = {s.name: st for s, st in plan("ci", cfg)}
    check("advisory honoured", states["wrapscan"] == "advisory")
    check("disabled honoured", states["spellscan"] == "disabled")
    check("others still enforced", states["secretscan"] == "enforced")

    # Advisory selects the softened argv, and only for the named scanner.
    root = Path("/repo")
    soft = _render(BY_NAME["wrapscan"].advisory, root, cfg)
    check("advisory form warns", "--warn" in soft)
    hard = _render(BY_NAME["wrapscan"].ci, root, cfg)
    check("enforced form does not warn", "--warn" not in hard)
    check("sizescan advisory drops --check",
          "--check" not in _render(BY_NAME["sizescan"].advisory, root, cfg))

    def rejects(label: str, payload: object) -> None:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)
            (p / CONFIG_NAME).write_text(json.dumps(payload), encoding="utf-8")
            try:
                Config.load(p)
            except ConfigError:
                return
            fails.append(f"accepted bad config: {label}")

    # Scope overrides widen a check to several subtrees, and stay local to the
    # scanner that declared one.
    scoped = Config(scope={"wrapscan": ("docs/method", "docs/build")})
    rendered = _render(BY_NAME["wrapscan"].ci, root, scoped, "wrapscan")
    check("override expands to every subtree",
          sum(1 for a in rendered if a.endswith(("method", "build"))) == 2)
    check("override leaves --root intact", "--root" in rendered)
    check("unscoped scanner keeps its own default",
          len(_render(BY_NAME["datescan"].ci, root, scoped, "datescan")) ==
          len(BY_NAME["datescan"].ci))

    # Extra flags append, and cannot displace the template's own arguments —
    # the networking-repo case (leakscan's IP/MAC rules are content there).
    flagged = Config(flags={"leakscan": ("--disable", "ipv4,ipv6,mac-address")})
    argv = _render(BY_NAME["leakscan"].hook, root, flagged, "leakscan")
    check("extra flags appended", argv[-2:] == ["--disable", "ipv4,ipv6,mac-address"])
    check("template args survive extra flags", "--staged" in argv and "--root" in argv)
    check("flags stay local to their scanner",
          "--disable" not in _render(BY_NAME["secretscan"].hook, root,
                                     flagged, "secretscan"))

    rejects("unknown scanner", {"disabled": {"nosuchscan": "why"}})
    rejects("empty scope override", {"scope": {"wrapscan": []}})
    # The sharpest one: --warn via `flags` would be an advisory downgrade that
    # bypasses every guard on `advisory`, on a scanner that has no advisory form.
    rejects("softening flag smuggled in", {"flags": {"secretscan": ["--warn"]}})
    rejects("mode flag smuggled in", {"flags": {"sizescan": ["--json"]}})
    rejects("reasonless disable", {"disabled": {"spellscan": "  "}})
    rejects("unsoftenable advisory", {"advisory": ["secretscan"]})
    rejects("advisory+disabled", {"advisory": ["wrapscan"],
                                  "disabled": {"wrapscan": "x"}})
    rejects("disabled as a list", {"disabled": ["spellscan"]})
    rejects("not an object", [1, 2, 3])

    # A missing config is full enforcement, not an error.
    with tempfile.TemporaryDirectory() as td:
        loaded = Config.load(Path(td))
        check("absent config enforces everything",
              not loaded.disabled and not loaded.advisory)

    for f in fails:
        print(f"floor selftest FAIL: {f}", file=sys.stderr)
    print(f"floor selftest: {'FAILED' if fails else 'ok'} "
          f"({len(SCANNERS)} scanners, {len(fails)} failure(s))")
    return 1 if fails else 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="floor", description=__doc__.split("\n")[0])
    p.add_argument("--plane", choices=("hook", "ci"), default="hook",
                   help="hook = staged/full-cover pre-commit; ci = whole-tree backstop")
    p.add_argument("--root", default=".", help="the repo to scan")
    p.add_argument("--tools", help="atelier's tools dir (default: env, git config, then here)")
    p.add_argument("--list", action="store_true", help="show the plan and exit")
    p.add_argument("--json", action="store_true", help="machine-readable result")
    p.add_argument("--selftest", action="store_true", help="prove the logic offline")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    try:
        cfg = Config.load(root)
    except ConfigError as e:
        # Fail closed: an unusable config blocks. A floor that guesses is not a floor.
        print(f"floor: {e}", file=sys.stderr)
        return 1

    if args.list:
        for s, state in plan(args.plane, cfg):
            print(f"{s.name:<11} {state:<9} {s.why}")
        return 0

    tools = resolve_tools_dir(args.tools)
    ci = args.plane == "ci" and os.environ.get("GITHUB_ACTIONS") == "true"
    results = run(args.plane, root, tools, cfg, ci, json_mode=args.json)

    if args.json:
        print(json.dumps({"plane": args.plane, "root": str(root),
                          "results": [r.__dict__ for r in results]}, indent=2))
    else:
        print(render(results, args.plane), file=sys.stderr)
    return 1 if any(r.failed for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
