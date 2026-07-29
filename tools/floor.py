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
        STAGED diff so the commit hot path stays fast, and leakscan runs with
        --require-terms, so its cover is FULL or the commit does not happen.
        That flag is what makes this paragraph a fact: until it was added, a
        clone with no term list silently got the CI-grade cover described
        below while every artefact here claimed otherwise, and the floor still
        printed a green tick (ADR 0008 cold pass, EP3). A machine can hold the
        list; that is exactly what distinguishes this plane from the next.
  ci    a backstop on a runner nobody configured. Reads the whole TREE (the
        scanners read files, not the log, and a rename breaks a link outside the
        diff). leakscan runs STRUCTURAL-ONLY here and always will: its literal
        person/estate term list is machine-local by design and must never enter
        a repo or a runner (`SECRETS.md`). A degraded, *declared* CI cover is the
        honest answer; the full cover lives on the hook. Declared in prose is
        not enough on its own, so the result also renders 🟡 partial here
        rather than ✅ — identical output for materially different cover is the
        claim, not the check (`Scanner.full_cover_flag`).

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
             through it. Tracked debt, not a hole — and it states BOTH what the
             debt is and when it comes due:

               "advisory": {
                 "wrapscan": {"why": "adopting the check; 60 findings to
                                      clear", "review-by": "2026-09-01"}
               }

             Both fields are required (C1, ruled 2026-07-28). Until C1 the key
             was a bare list of scanner names carrying neither, so nothing
             distinguished three-days-into-a-cleanup from softened-and-forgotten
             — the exact decay ADR 0008 exists to end, and `disabled` (the
             HARDER opt-out) had demanded a reason all along. A passed
             `review-by` goes red on the fleet board and blocks NOTHING: a
             commit failing on a date set months earlier is how a forcing
             function becomes a --no-verify habit.
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

THE REPO-LOCAL SEAM — a child may ADD a check, never soften one
----------------------------------------------------------------
Everything above is subtraction: a child says which of atelier's checks it is
not enforcing. There was no addition. A repo with a rule of its own — one that
is genuinely repo-specific and could never be fleet-wide — had nowhere to put
it, because the tracked pre-commit hook is deliberately scanner-agnostic and
this registry is deliberately shared.

The worked case that forced this (`ros`, 2026-07-26): a tripwire whose blocklist
names the estate's own tokens. That list can never live in a shared repo, so the
check can never be a `SCANNERS` line — and with no seam, the repo's only options
were to keep a bespoke hook (falling out of propagation entirely, which is the
defect this whole file exists to end) or to lose the check. Both are worse than
the check running from a declaration the fleet board can see.

So `local` in `.atelier-floor.json` declares checks the CHILD owns:

  "local": {
    "tripwire": {
      "run": "tools/tripwire.py",        (required) repo-relative, inside the repo
      "why": "estate tokens never enter a commit",   (required) one line
      "planes": ["hook"],                 default both — hook-only is legitimate
      "args": ["--staged", "--root", "{root}"],      same templates as above
      "scope": ["src"]                    default the whole repo
    }
  }

Three properties make this an extension point rather than a hole:

  it only ADDS      a local name that collides with a registered scanner is a
                    hard config error. The seam cannot replace, shadow or
                    weaken a fleet check — PROPAGATION's narrow-not-contradict,
                    applied to enforcement.
  it fails CLOSED   a declared check whose script is missing BLOCKS, exactly as
                    a missing shared scanner does. Declaring a check you do not
                    ship is not a way to look guarded.
  it is VISIBLE     local checks are in `--list`, in `--json`, in the render, and
                    on `floorfleet`'s board. A repo's own rules are estate-legible
                    even though their CODE is not shared.

Softening works through the same two spellings as everything else: name a local
check in `advisory` or `disabled` and it reads identically on the board. One
honest difference — a shared scanner's advisory state swaps in that scanner's
own `--warn` form, so its OUTPUT says warning; the floor cannot know a local
check's flags, so advisory there is a floor-level downgrade and the check's own
output will still read as a failure. It does not block; it just still looks
alarming. If that matters, give the check a quieter form and declare it in
`args`.

What this seam is NOT: a way to run arbitrary work in the commit path of a repo
you do not control. `run` must resolve inside the repo being scanned, and it is
invoked directly — never through a shell. It is the child's own code, in the
child's own hook and the child's own CI, which is code both already run.

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
import datetime
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

CONFIG_NAME = ".atelier-floor.json"
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Placeholders resolved per invocation: {root} = the repo being scanned,
# {docs} = its records tree (configurable — not every child keeps records in
# docs/), {licence} = the SPDX id a publish-ready repo asserts.


@dataclass(frozen=True)
class Advisory:
    """A softened check, with the two facts that stop it becoming permanent.

    `advisory` used to be a bare list of scanner names, carrying no reason and
    no review date — so nothing distinguished "we are three days into adopting
    this check" from "someone softened it and left". `disabled`, the *harder*
    and more visible opt-out, has always required a stated reason; the softer
    one required nothing, which is backwards (Track C, C1, ruled 2026-07-28).

    `legacy` marks a declaration still in the bare-list spelling. Those parse
    during the transition and render 🟡 every run, so the estate migrates
    without a flag day; the spelling becomes a hard error once the board is
    clean (C1 phase 2). A declaration in the NEW spelling is held to the full
    rule immediately — there is no half-migrated state to reason about."""
    why: str = ""
    review_by: str | None = None  # ISO 8601 date, per CONVENTIONS.md
    legacy: bool = False

    def expired(self, today: str) -> bool:
        """Has the review date passed? String comparison is exact for ISO 8601
        dates and needs no timezone reasoning — the format is validated at parse
        precisely so this stays true."""
        return self.review_by is not None and self.review_by < today


@dataclass(frozen=True)
class Scope:
    """WHERE a check looks in this repo, and — for a check that may not be
    softened — WHY it was narrowed.

    Narrowing a boundary or integrity scanner reduces cover on exactly the
    checks a child may never soften, so it states its reason the same way a
    disabled check does (A1 option (b), deferred out of the A1 ruling into C1
    and ruled there, 2026-07-28). No `review-by`: unlike an advisory, a narrowed
    scope is a permanent structural fact about a repo — its shareable subtree is
    smaller than its tree — not dated debt waiting to be cleared."""
    paths: tuple[str, ...] = ()
    why: str = ""
    legacy: bool = False


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
    # Set only for a check the CHILD declares (see THE REPO-LOCAL SEAM). The
    # repo-relative path to its script — resolved against the repo being scanned,
    # never against atelier's tools dir, which is the whole point.
    run: str | None = None
    # A local check carries its own scope inline rather than through the shared
    # `scope` map: the child is declaring the check and where it looks in one
    # place, and there is no fleet-wide default to override.
    scope_paths: tuple[str, ...] = ()
    # The flag that makes this check's cover COMPLETE, for a check whose cover
    # depends on an input the repo does not carry. A plane whose template omits
    # it still passes, but it passes on less — so the result renders as partial
    # rather than as a plain green tick. Without this the two-plane design was
    # asserted and never shown: a structural-only leakscan rendered `✅
    # enforced`, identical to a full-cover one (ADR 0008 cold pass, EP3).
    full_cover_flag: str | None = None

    @property
    def is_local(self) -> bool:
        return self.run is not None


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
        # --require-terms is what makes "the full cover lives on the hook" a
        # fact rather than a claim. Without it a clone with no machine-local
        # term list silently degraded to a structural-only scan and still
        # rendered `✅ enforced` — CI-grade cover from the plane the design
        # says carries the personal-data boundary. It fails closed with the
        # remedy leakscan already prints; the term list lives in ~/.claude/,
        # outside every repo, so this costs one onboarding step and nothing in
        # CI, which runs the ci template below.
        hook=["--staged", "--root", "{root}", "--require-terms", "{scope}"],
        ci=["--root", "{root}", "{scope}"],  # structural-only: no --require-terms
        advisory=None,  # the personal-data boundary is not a re-baselining matter
        why="no personal/estate data enters a repo that can go public",
        full_cover_flag="--require-terms",
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
        why="a decision record states its review judgement, and a review "
            "brief keeps deferred material in a sibling file",
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


PLANES = ("hook", "ci")
# Every key a `local.<name>` declaration may carry. Kept beside the parser that
# reads them so adding a key here and reading it there stay one edit apart —
# a key added to the parser but not to this set would be rejected as unknown,
# which fails in the safe direction (loudly, at parse time).
LOCAL_KEYS = frozenset({"run", "why", "planes", "args", "scope"})


def _inside(root: Path, candidate: Path) -> bool:
    """Is `candidate` the root itself or a path beneath it, after symlinks?

    Both sides resolved, then compared as paths rather than strings —
    `commonpath` treats components as components, so `/x/repo2` is not inside
    `/x/repo` however the prefixes read."""
    try:
        r, c = root.resolve(), candidate.resolve()
        return os.path.commonpath([r, c]) == str(r)
    except (OSError, ValueError):
        # ValueError: different drives/roots — genuinely not inside. OSError: a
        # broken or looping symlink. Neither is a tree this repo can vouch for.
        return False


def _today() -> str:
    """Today, as an ISO 8601 date in UTC. UTC because the estate's records are
    stamped that way (`CONVENTIONS.md`) and because a review date that flips a
    day early or late depending on the committer's timezone would make the
    board disagree with itself across machines."""
    return datetime.datetime.now(datetime.timezone.utc).date().isoformat()


def _load_advisory(raw: object) -> dict[str, Advisory]:
    """Parse `advisory`, accepting both spellings during the C1 transition.

      ["wrapscan"]                                  legacy — parses, renders 🟡
      {"wrapscan": {"why": "...", "review-by": "2026-09-01"}}   the rule

    The legacy form exists so the schema can land without breaking every
    child's CI on the same afternoon (children fetch atelier@main at run time,
    so a hard error here is a flag day for the whole estate). It is a
    transition, not a dialect: phase 2 removes it."""
    if raw is None:
        return {}
    if isinstance(raw, (list, tuple)):
        return {str(name): Advisory(legacy=True) for name in raw}
    if not isinstance(raw, dict):
        raise ConfigError(
            f"{CONFIG_NAME}: `advisory` must be an object of "
            '{"scanner": {"why": ..., "review-by": ...}}'
        )

    out: dict[str, Advisory] = {}
    for name, decl in raw.items():
        name = str(name)
        if isinstance(decl, str):
            # The near-miss worth naming: a reason with no date reads like the
            # full spelling and is not. Say which half is missing.
            raise ConfigError(
                f"{CONFIG_NAME}: `advisory.{name}` is a bare reason — it also "
                'needs a review date: {"why": ..., "review-by": "YYYY-MM-DD"}'
            )
        if not isinstance(decl, dict):
            raise ConfigError(
                f"{CONFIG_NAME}: `advisory.{name}` must be an object with "
                "`why` and `review-by`"
            )
        why = str(decl.get("why", "") or "").strip()
        if not why:
            raise ConfigError(
                f"{CONFIG_NAME}: `advisory.{name}` needs a `why` — a softened "
                "check nobody can state the point of is one nobody will "
                "re-enable, and it prints on the fleet board with nothing "
                "beside it"
            )
        review_by = decl.get("review-by")
        if not review_by:
            raise ConfigError(
                f"{CONFIG_NAME}: `advisory.{name}` needs a `review-by` date — "
                "an advisory with no end is the 'honour it manually' failure "
                "wearing a new hat, which is the decay this rule exists to end"
            )
        review_by = str(review_by)
        if not ISO_DATE_RE.match(review_by):
            raise ConfigError(
                f"{CONFIG_NAME}: `advisory.{name}.review-by` must be an ISO "
                f"8601 date (YYYY-MM-DD), got {review_by!r}"
            )
        try:
            datetime.date.fromisoformat(review_by)
        except ValueError as e:
            raise ConfigError(
                f"{CONFIG_NAME}: `advisory.{name}.review-by` is not a real "
                f"date: {review_by!r}"
            ) from e
        unknown = sorted(set(decl) - {"why", "review-by"})
        if unknown:
            # Same call as the local seam's key check (LS4): a key read past in
            # silence is a declaration the writer believes is doing something.
            raise ConfigError(
                f"{CONFIG_NAME}: `advisory.{name}` has unknown "
                f"{', '.join(repr(k) for k in unknown)} (known: 'why', "
                "'review-by')"
            )
        out[name] = Advisory(why=why, review_by=review_by)
    return out


def _load_scope(raw: object) -> dict[str, Scope]:
    """Parse `scope`, accepting both spellings during the same transition.

      {"leakscan": ["tiki/"]}                       legacy — parses, renders 🟡
      {"leakscan": {"paths": ["tiki/"], "why": "..."}}          the rule

    The `why` is required only for a scanner with no advisory form; a softenable
    check's scope is an ordinary layout fact (A1(b), ruled 2026-07-28). That
    condition cannot be checked here — the registry lookup lives on Config — so
    it is enforced in `Config.validate`."""
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise ConfigError(f"{CONFIG_NAME}: `scope` must be an object")

    out: dict[str, Scope] = {}
    for name, decl in raw.items():
        name = str(name)
        if isinstance(decl, (str, list, tuple)):
            entries = [decl] if isinstance(decl, str) else list(decl or ())
            if not entries:
                raise ConfigError(
                    f"{CONFIG_NAME}: `scope.{name}` is empty — an override that "
                    "narrows a check to nothing is a silent hole, not a scope"
                )
            out[name] = Scope(paths=tuple(str(e) for e in entries), legacy=True)
            continue
        if not isinstance(decl, dict):
            raise ConfigError(
                f"{CONFIG_NAME}: `scope.{name}` must be a list of paths, or an "
                "object with `paths` and `why`"
            )
        raw_paths = decl.get("paths", [])
        if isinstance(raw_paths, str):
            raw_paths = [raw_paths]
        paths = tuple(str(p) for p in (raw_paths or ()))
        if not paths:
            raise ConfigError(
                f"{CONFIG_NAME}: `scope.{name}.paths` is empty — an override "
                "that narrows a check to nothing is a silent hole, not a scope"
            )
        unknown = sorted(set(decl) - {"paths", "why"})
        if unknown:
            raise ConfigError(
                f"{CONFIG_NAME}: `scope.{name}` has unknown "
                f"{', '.join(repr(k) for k in unknown)} (known: 'paths', 'why')"
            )
        out[name] = Scope(paths=paths,
                          why=str(decl.get("why", "") or "").strip())
    return out


def _reject_escaping_scope(where: str, path: str) -> None:
    """Refuse a scope path that names somewhere other than this repo's tree.

    The lexical half of the membership rule — absolute paths and `..` — held
    against a string, before any file system is consulted. `local.run` has had
    exactly this check since the local seam landed; fleet `scope` had neither
    this nor the resolved half, which is the asymmetry TA1 named inside a
    single diff. The resolved half lives at the run guard, where a root to
    resolve against exists."""
    p = PurePosixPath(path)
    if p.is_absolute() or ".." in p.parts:
        raise ConfigError(
            f"{CONFIG_NAME}: `{where}` must be a path INSIDE the repo, got "
            f"{path!r}. A scope that names another tree does not narrow the "
            "check, it points it somewhere else — and on the hook plane it "
            "matches nothing at all, which exits 0 and reads as a clean pass."
        )


def _load_local(raw: object) -> tuple[Scanner, ...]:
    """Parse the `local` block into Scanners — the child's own checks.

    Every rejection here is deliberate: a malformed local declaration must not
    become "no check", because the repo declaring it believes it is covered."""
    if isinstance(raw, list):
        raise ConfigError(
            f'{CONFIG_NAME}: `local` must be an object of {{"name": {{...}}}} — '
            "a check is named so it can be softened, disabled and read off the "
            "fleet board by that name"
        )
    if not isinstance(raw, dict):
        raise ConfigError(f"{CONFIG_NAME}: `local` must be an object")

    out: list[Scanner] = []
    for name, decl in raw.items():
        if name in BY_NAME:
            raise ConfigError(
                f"{CONFIG_NAME}: `local.{name}` collides with atelier's own "
                f"{name} — the local seam ADDS checks, it never replaces one. "
                "To vary a fleet check use `scope`/`flags`, or declare it "
                "`advisory`/`disabled` with a reason."
            )
        if not isinstance(decl, dict):
            raise ConfigError(
                f"{CONFIG_NAME}: `local.{name}` must be an object with at least "
                "`run` and `why`"
            )

        # Unknown keys were read past in silence, which relaxed this file's own
        # "a config cannot quietly mean less than it says" invariant exactly
        # where it is enforced for top-level scanner names. The cost is not
        # cosmetic: a `planes` typo leaves the default in place, so a tripwire
        # meant for the hook alone also runs on CI, and an `args` typo silently
        # drops the arguments so the check runs against nothing (local seam cold
        # pass, LS4). Same fail-closed shape as an unknown scanner name.
        unknown_keys = sorted(set(decl) - LOCAL_KEYS)
        if unknown_keys:
            raise ConfigError(
                f"{CONFIG_NAME}: `local.{name}` has unknown "
                f"{', '.join(repr(k) for k in unknown_keys)} "
                f"(known: {', '.join(sorted(LOCAL_KEYS))}). A typo here changes "
                "which planes run or drops the check's arguments, silently."
            )

        run = str(decl.get("run", "") or "").strip()
        why = str(decl.get("why", "") or "").strip()
        if not run:
            raise ConfigError(f"{CONFIG_NAME}: `local.{name}` needs a `run` path")
        if not why:
            # Same rule as a reasoned disable, for the same reason: a check
            # nobody can state the point of is one nobody will maintain, and it
            # prints on the board with nothing beside it.
            raise ConfigError(
                f"{CONFIG_NAME}: `local.{name}` needs a `why` — one line on what "
                "it protects, printed by --list and on the fleet board"
            )
        run_path = PurePosixPath(run)
        if run_path.is_absolute() or ".." in run_path.parts:
            raise ConfigError(
                f"{CONFIG_NAME}: `local.{name}.run` must be a path INSIDE the "
                f"repo, got {run!r}. The seam runs the repo's own committed "
                "code; anything else is not the repo's floor."
            )

        planes = decl.get("planes", list(PLANES)) or []
        if isinstance(planes, str):
            planes = [planes]
        planes = [str(p) for p in planes]
        unknown = [p for p in planes if p not in PLANES]
        if unknown:
            raise ConfigError(
                f"{CONFIG_NAME}: `local.{name}.planes` has unknown "
                f"{', '.join(unknown)} (known: {', '.join(PLANES)})"
            )
        if not planes:
            raise ConfigError(
                f"{CONFIG_NAME}: `local.{name}.planes` is empty — a check that "
                "runs on no plane is a declaration with nothing behind it"
            )

        raw_args = decl.get("args", []) or []
        if isinstance(raw_args, str):
            raw_args = [raw_args]
        args = [str(a) for a in raw_args]

        raw_scope = decl.get("scope", []) or []
        if isinstance(raw_scope, str):
            raw_scope = [raw_scope]
        scope = tuple(str(s) for s in raw_scope)
        if "scope" in decl and not scope:
            raise ConfigError(
                f"{CONFIG_NAME}: `local.{name}.scope` is empty — narrowing a "
                "check to nothing is a silent hole, not a scope"
            )

        out.append(Scanner(
            name=name,
            hook=args if "hook" in planes else None,
            ci=args if "ci" in planes else None,
            # A local check is softenable, and its advisory form is its ONLY
            # form: the floor cannot know this check's flags, so `advisory`
            # downgrades the RESULT rather than the invocation. Stated in the
            # module docstring, because the difference from a fleet scanner's
            # `--warn` is visible in the check's own output.
            advisory=args,
            why=why,
            run=run,
            scope_paths=scope,
        ))
    return tuple(out)


@dataclass
class Config:
    docs: str = "docs"
    licence: str | None = None
    advisory: dict[str, Advisory] = field(default_factory=dict)
    disabled: dict[str, str] = field(default_factory=dict)  # name -> reason
    # Per-scanner overrides of WHERE a check looks. atelier itself needs this
    # (its prose checks are scoped to the doctrine surface, not all of docs/) and
    # so does any repo whose shareable subtree is narrower than its whole tree —
    # a networking repo scanning only the part that can go public, say. Modelling
    # it as config rather than special-casing the parent is what lets atelier run
    # the SAME floor it ships: a parent with its own private list would be the
    # two-lists bug all over again, one level up.
    #
    # A narrowed scope reduces cover, so it is read out estate-wide on the
    # `floorfleet` board and in its --json (the 🔎 line). Say it here only
    # because it is true here: this comment previously claimed estate-wide
    # visibility that `floorfleet` did not implement, which is the honesty
    # defect the apex forbids and was the reason a shrunken scope went
    # unreported (ADR 0008 cold pass, EP1/EP2).
    scope: dict[str, Scope] = field(default_factory=dict)
    # Per-scanner extra arguments — for a check that needs tuning to a repo's
    # subject matter rather than its layout. A networking repo disabling
    # leakscan's IP/MAC rules is the worked case: those shapes are legitimate
    # CONTENT there, not leaked estate data. This genuinely weakens a check,
    # which is why it lives in a committed file and is read out estate-wide by
    # `floorfleet` (the 🔧 line) — declared and visible, never quietly applied.
    # `tools/test_floorfleet.py` pins both lines, so the claim stays checkable
    # rather than becoming true once and drifting back.
    flags: dict[str, tuple[str, ...]] = field(default_factory=dict)
    # Checks the CHILD declares and ships — see THE REPO-LOCAL SEAM. Held as
    # Scanners so every stage below (plan, scope, render, run) treats them
    # identically to a fleet check; the only thing that differs is where the
    # script is found.
    local: tuple[Scanner, ...] = ()

    def __post_init__(self) -> None:
        """Accept the shorthand shapes a caller naturally reaches for, and hold
        exactly one shape internally.

        `Config(advisory=["wrapscan"], scope={"leakscan": ("tiki/",)})` is what
        every construction site in the selftest and the tests already says, and
        what a reader writes without thinking. Normalising here means the rest
        of this module — plan, subtrees, render, validate — sees `Advisory` and
        `Scope` and never a union, which is the property that makes the C1
        fields safe to reason about. The JSON loaders stay the strict door:
        they are where a REPO's declaration is judged, and they reject what
        this accepts, because a config file is a claim and a keyword argument
        is just a shorthand."""
        if isinstance(self.advisory, (list, tuple, set)):
            self.advisory = {str(n): Advisory(legacy=True) for n in self.advisory}
        else:
            self.advisory = {
                str(n): (v if isinstance(v, Advisory) else Advisory(legacy=True))
                for n, v in dict(self.advisory).items()}
        normalised: dict[str, Scope] = {}
        for name, value in dict(self.scope).items():
            if isinstance(value, Scope):
                normalised[str(name)] = value
            elif isinstance(value, str):
                normalised[str(name)] = Scope(paths=(value,), legacy=True)
            else:
                normalised[str(name)] = Scope(
                    paths=tuple(str(p) for p in (value or ())), legacy=True)
        self.scope = normalised

    def scanner(self, name: str) -> Scanner | None:
        """The registered scanner or the child's local check of that name. One
        lookup, so no stage can accidentally honour only half the floor."""
        found = BY_NAME.get(name)
        if found is not None:
            return found
        return next((s for s in self.local if s.name == name), None)

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
        advisory = _load_advisory(raw.get("advisory", {}))

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
                     scope=_load_scope(raw.get("scope", {})),
                     flags=_str_map("flags", allow_empty=False),
                     local=_load_local(raw.get("local", {}) or {}))
        cfg.validate()
        return cfg

    def validate(self) -> None:
        """Reject a config that does not mean what it says. Every one of these is
        a block, not a warning — a floor that quietly ignores half its config is
        worse than no config, because it reads as covered."""
        local_names = {s.name for s in self.local}
        known = {*BY_NAME, *local_names}
        for name in (*self.advisory, *self.disabled, *self.scope, *self.flags):
            if name not in known:
                raise ConfigError(
                    f"{CONFIG_NAME}: unknown scanner {name!r} "
                    f"(known: {', '.join(sorted(known))})"
                )
        # `scope`/`flags` tune a check the child did NOT write, so they exist to
        # bend a fleet scanner to a repo. A local check's scope and arguments are
        # declared where the check is — one fact, one home. Accepting both spellings
        # would mean two places to read before you know what a check actually ran.
        for key, block in (("scope", self.scope), ("flags", self.flags)):
            for name in block:
                if name in local_names:
                    raise ConfigError(
                        f"{CONFIG_NAME}: `{key}.{name}` names a local check — "
                        f"declare it in `local.{name}.{'scope' if key == 'scope' else 'args'}` "
                        "instead, where the check itself is defined"
                    )
        # A scope path must name a tree INSIDE this repo, and this is the lexical
        # half of that — the same check `local.run` already carries, for the same
        # reason. Without it a declared path that merely EXISTS passes the run
        # guard: `/etc` renders to a staged prefix matching nothing and a scan
        # that matches nothing exits 0, so a boundary check reads ✅ while
        # covering none of the diff (Track A application cold pass, TA1, ruled
        # (a) 2026-07-28). Checked here rather than at the guard so it blocks on
        # every plane and for softenable scanners too — the guard is reached only
        # by checks that have no advisory form.
        for name, sc in self.scope.items():
            for p in sc.paths:
                _reject_escaping_scope(f"scope.{name}", p)
            # A1(b): narrowing a check that may NEVER be softened states why.
            # Only checkable here, where the registry lookup lives. Legacy
            # spellings are exempt for the length of the transition — they
            # cannot carry a `why` at all, and the 🟡 they render is the
            # migration prompt.
            scanner = self.scanner(name)
            if (not sc.legacy and not sc.why
                    and scanner is not None and scanner.advisory is None):
                raise ConfigError(
                    f"{CONFIG_NAME}: `scope.{name}` needs a `why` — {name} is a "
                    "boundary or integrity check that may never be softened, so "
                    "narrowing where it looks is a cover decision on the record, "
                    "not a layout detail."
                )
        # Both spellings, because both feed `subtrees` and render identically.
        for scanner in self.local:
            for p in scanner.scope_paths:
                _reject_escaping_scope(f"local.{scanner.name}.scope", p)
        for name in self.advisory:
            if name in self.disabled:
                raise ConfigError(
                    f"{CONFIG_NAME}: {name!r} is both advisory and disabled — pick one"
                )
            if self.scanner(name).advisory is None:
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
    local: bool = False  # declared by this repo, not inherited from the fleet
    # Why this pass covers less than the check's full form, when it does. A
    # partial pass is still a pass and still blocks on what it did check — but
    # it must not render as a plain green tick, because a reader who cannot
    # tell full cover from partial has been told the check ran, not what it
    # checked (ADR 0008 cold pass, EP3).
    partial: str = ""
    # C1: a softened check carries its reason and its review date wherever it
    # is reported, and says when that date has passed. An expired advisory
    # NEVER blocks — a commit failing on a date somebody set months earlier is
    # how a forcing function turns into a --no-verify habit — so this is a
    # reporting state only, red on the board and nowhere else (ruled
    # 2026-07-28). `legacy` marks the pre-C1 spelling, still parsing through
    # the transition.
    review_by: str = ""
    expired: bool = False
    legacy: bool = False

    @property
    def failed(self) -> bool:
        return self.state == "enforced" and self.rc != 0


def _wc(text: str) -> str:
    """Encode a value for interpolation into a GitHub Actions `::` workflow
    command.

    Actions parses its log commands line by line, so a newline inside an
    interpolated value ENDS the command and lets whatever follows be read as a
    fresh one. Before the repo-local seam this channel only ever carried
    hardcoded registry strings; the seam feeds it child-authored `name`/`why`
    text, and on a repo whose CI runs against pull requests that text can come
    from a contributor — a `why` carrying a newline plus `::error::` injects a
    spoofed annotation into the base repo's log (local seam cold pass, LS1).

    `%25` goes first or it would re-encode the escapes produced after it. This
    is GitHub's own documented mitigation for the workflow-command-injection
    class, so it belongs at the point of interpolation rather than in a
    validator someone can forget to call."""
    return (text.replace("%", "%25")
                .replace("\r", "%0D")
                .replace("\n", "%0A"))


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
    if override and override.paths:
        return list(override.paths)
    scanner = cfg.scanner(name)
    if scanner is not None and scanner.scope_paths:
        return list(scanner.scope_paths)
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


def _interpreter(path: Path) -> list[str]:
    """How to invoke a check. atelier's scanners are Python and are run with the
    SAME interpreter this file is running under — never a bare `python` off the
    PATH. A local check may be anything the repo ships, so a non-`.py` script is
    executed directly and carries its own shebang. Never through a shell: an
    argument is an argument, not something a repo's filename can turn into one."""
    if path.suffix == ".py":
        return [sys.executable]
    return []


def plan(plane: str, cfg: Config) -> list[tuple[Scanner, str]]:
    """Decide what runs, in what state, before running anything. Kept separate
    from execution so `--list` and the selftest can prove the decision without
    invoking a single scanner."""
    out: list[tuple[Scanner, str]] = []
    # Fleet checks first, then the child's own — the floor a repo inherits is
    # read before the floor it adds, in the output as in the doctrine.
    for s in (*SCANNERS, *cfg.local):
        args = s.hook if plane == "hook" else s.ci
        if args is None:
            # A local check may legitimately be hook-only — the ros tripwire's
            # blocklist is machine/repo-local, the same shape as leakscan's term
            # list. It still LISTS on the other plane, saying it did not run
            # there: a check absent from CI must not read as a check that passed.
            if s.is_local:
                out.append((s, "skipped"))
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
            # `local=` here for the same reason the other four branches carry
            # it: without it a --json consumer cannot tell a disabled LOCAL
            # check from a disabled fleet one, and the render drops the `· local`
            # tag that says which repo's decision this was (local seam cold
            # pass, LS5).
            results.append(Result(scanner.name, state, 0, cfg.disabled[scanner.name],
                                  local=scanner.is_local))
            continue
        if state == "skipped":
            reason = ("no licence declared" if scanner.opt_in
                      else f"not declared on the {plane} plane")
            results.append(Result(scanner.name, state, 0, reason,
                                  local=scanner.is_local))
            continue

        # A local check comes from the repo being scanned; a fleet check comes
        # from atelier's tools dir. That one line is the whole difference.
        path = (root / scanner.run) if scanner.is_local else (tools / f"{scanner.name}.py")
        if not path.is_file():
            # Fail closed, loudly. This is the case the whole design exists for:
            # a child pointed at a tools dir that isn't there must NOT sail past.
            if scanner.is_local:
                print(
                    f"floor: {scanner.name} declares run={scanner.run!r} in "
                    f"{CONFIG_NAME}, and it is not in this repo — BLOCKING "
                    "(fail closed).\n"
                    "  A declared check that is not there must not read as a "
                    "check that passed.\n"
                    "  Ship the script, fix the path, or remove the "
                    f"`local.{scanner.name}` declaration.",
                    file=sys.stderr,
                )
            else:
                print(
                    f"floor: {scanner.name}.py not found under {tools} — BLOCKING "
                    "(fail closed).\n"
                    "  The scanners live in atelier's tools/. Point at them with:\n"
                    "    git config hooks.atelierTools <atelier-path>/tools\n"
                    "  or set ATELIER_TOOLS in the environment.",
                    file=sys.stderr,
                )
            results.append(Result(scanner.name, "enforced", 1, "scanner missing",
                                  local=scanner.is_local))
            continue

        # "`run` must resolve inside the repo" was enforced on the declared
        # STRING only — `..` and absolute paths are refused at parse time — so a
        # committed symlink at the run path whose target sits outside the tree
        # executed out-of-tree code, proved live (local seam cold pass, LS3).
        # The lexical check cannot see that; only the resolved path can. Marginal
        # privilege is bounded, since the config author usually owns the repo,
        # but a stated invariant that holds only against typos and not against
        # the file system is exactly the kind of overstatement the apex forbids.
        if scanner.is_local:
            try:
                real = path.resolve(strict=True)
                inside = real.is_relative_to(root.resolve())
            except (OSError, RuntimeError):
                inside = False  # a broken or looping symlink is not inside either
            if not inside:
                print(
                    f"floor: {scanner.name} → {scanner.run} resolves outside this "
                    "repo — BLOCKING (fail closed).\n"
                    "  The seam runs the repo's OWN committed code. A symlink "
                    "pointing out of the tree\n"
                    "  is not this repo's floor, whatever the declared path "
                    "spells.",
                    file=sys.stderr,
                )
                results.append(Result(scanner.name, "enforced", 1,
                                      "run resolves outside the repo", local=True))
                continue

        # A non-Python check runs on its own shebang, so it needs the execute
        # bit. Without this it raises PermissionError deep inside subprocess and
        # takes the whole floor down with a traceback — a crash reads as broken
        # tooling, not as the config error it actually is.
        if scanner.is_local and path.suffix != ".py" and not os.access(path, os.X_OK):
            print(
                f"floor: {scanner.name} → {scanner.run} is not executable — "
                "BLOCKING (fail closed).\n"
                f"  chmod +x {scanner.run}, or give it a .py suffix to run under "
                "this interpreter.",
                file=sys.stderr,
            )
            results.append(Result(scanner.name, "enforced", 1, "not executable",
                                  local=True))
            continue

        base = scanner.advisory if state == "advisory" else (
            scanner.hook if plane == "hook" else scanner.ci
        )

        declared = subtrees(root, cfg, scanner.name)
        # The resolved half of the membership rule (TA1, ruled (a)). The lexical
        # half at `Config.validate` cannot see a symlink: `scope: ["logs"]` where
        # `logs` -> /var/log is a relative, `..`-free path that exists, and would
        # otherwise render as a scanned tree outside the repo. `os.path.commonpath`
        # rather than a string prefix so a sibling named like the root (`../repo2`
        # beside `repo`) cannot pass on spelling alone.
        outside = [p for p in declared if (root / p).exists()
                   and not _inside(root, root / p)]
        if outside:
            print(
                f"floor: {scanner.name} is scoped to "
                f"{', '.join(repr(p) for p in outside)}, which "
                f"{'resolves' if len(outside) == 1 else 'resolve'} OUTSIDE this "
                "repo — BLOCKING (fail closed).\n"
                "  A scope names a subtree of this repo. Pointing a check at "
                "another tree does not narrow it, and on the hook plane it "
                "matches nothing and exits 0 — a green tick over an unscanned "
                "diff.\n"
                f"  Fix the path in {CONFIG_NAME}, or remove the "
                f"`scope.{scanner.name}` entry to scan the whole repo.",
                file=sys.stderr,
            )
            results.append(Result(scanner.name, "enforced", 1, "scope resolves outside the repo",
                                  local=scanner.is_local))
            continue

        missing = [p for p in declared if not (root / p).exists()]
        trees = [p for p in declared if (root / p).exists()]

        # A declared path that does not resolve REDUCES a check's cover, and for
        # a scanner with no advisory form that is precisely the softening the
        # child may never make (`Config.validate`, and the module docstring's
        # boundary/integrity rule). Skipping it instead — the branch below —
        # meant one typo in a `scope` path turned secretscan or leakscan off and
        # the run still exited 0. This is the same call already made for an empty
        # `local.*.scope` ("narrowing a check to nothing is a silent hole, not a
        # scope") and for an absolute path in --staged mode.
        #
        # It is ONE member of that class, not the rest of it. The class is
        # "a declared scope that reads something other than the tree it names",
        # and this guard shuts only the first of its three members: does not
        # resolve (shut here) / resolves OUTSIDE the repo (open — `/etc` and
        # `..` both pass `.exists()`, render to a prefix that matches no staged
        # path, and exit 0 clean) / resolves outside via an in-tree symlink
        # (open). `local.run` has the lexical half of this check
        # (`is_absolute()` / `..`) and fleet `scope` has neither half — the
        # asymmetry is real and named, not designed. Track A application cold
        # pass, TA1, ruled (a) and closed 2026-07-28 — both the outside-the-repo
        # members are shut above; this branch keeps the does-not-resolve one.
        # Registry defaults for these scanners are the repo root, so only an
        # explicit declaration can reach here.
        if missing and scanner.advisory is None:
            print(
                f"floor: {scanner.name} is scoped to "
                f"{', '.join(repr(p) for p in missing)}, which "
                f"{'does' if len(missing) == 1 else 'do'} not exist in this repo "
                "— BLOCKING (fail closed).\n"
                f"  {scanner.name} has no advisory form, so a scope that reads "
                "nothing is a silent hole, not a narrower check.\n"
                f"  Fix the path in {CONFIG_NAME}, or remove the "
                f"`scope.{scanner.name}` entry to scan the whole repo.",
                file=sys.stderr,
            )
            results.append(Result(scanner.name, "enforced", 1, "scope resolves to nothing",
                                  local=scanner.is_local))
            continue

        # A check scoped to a subtree has nothing to read in a repo that keeps
        # none. The scanners exit 2 (environment error) on a missing path, which
        # would block every code-only repo — so skip, but SAY SO, and let
        # floorfleet surface it estate-wide. A repo whose records simply live
        # somewhere else sets `docs` (or a per-scanner `scope`); this branch is
        # what makes that misconfiguration visible instead of silently uncovered.
        # Reached only by softenable checks now: the guard above claims the rest.
        if not trees:
            results.append(Result(scanner.name, "skipped", 0,
                                  f"no {', '.join(declared)} tree in this repo",
                                  local=scanner.is_local))
            continue

        argv = [*_interpreter(path), str(path),
                *_render(base, root, cfg, scanner.name, trees)]
        # Actions' workflow commands go to the SAME stream the scanners' own
        # prose does (`child_stdout`: stderr under --json, stdout otherwise) —
        # not unconditionally to stdout. Under --json, stdout is reserved for
        # the JSON document by this function's contract above, and grouping
        # markers written there corrupt it for every caller inside Actions
        # (`json.loads` on a `::group::` line). Real CI invokes floor.py without
        # --json, so grouping still renders exactly where it is consumed.
        if ci:
            print(f"::group::{_wc(scanner.name)} ({state})",
                  file=child_stdout, flush=True)
        try:
            rc = subprocess.run(argv, check=False, stdout=child_stdout).returncode
        except OSError as exc:
            # The exec-bit guard above has a sibling: an EXECUTABLE non-Python
            # script with no valid shebang raises Errno 8 here and takes the
            # whole floor down with a traceback — no summary, and any local
            # check after it never runs. That is fail-closed by exit code but
            # not by clean message, which is the very failure the exec-bit
            # guard was written to prevent: a crash reads as broken tooling
            # rather than as the config error it is (local seam cold pass, LS2).
            print(
                f"floor: {scanner.name} → {scanner.run or path.name} could not be "
                f"executed ({exc.strerror or exc}) — BLOCKING (fail closed).\n"
                "  An executable script needs a valid shebang line (e.g. "
                "`#!/usr/bin/env bash`),\n"
                "  or give it a .py suffix to run under this interpreter.",
                file=sys.stderr,
            )
            results.append(Result(scanner.name, "enforced", 1, "not executable",
                                  local=scanner.is_local))
            if ci:
                print("::endgroup::", file=child_stdout, flush=True)
            continue
        if ci:
            print("::endgroup::", file=child_stdout, flush=True)
            if rc != 0 and state == "enforced":
                print(f"::error::{_wc(scanner.name)} failed — {_wc(scanner.why)}",
                      file=child_stdout, flush=True)
        # Read off the argv actually invoked, not off the plane name: the plane
        # does not determine the invocation, a child's config can vary it.
        #
        # What this can and cannot say (TA4). The argv knows what cover was
        # DEMANDED; only the scanner's own output knows what cover it got. On a
        # machine that happens to hold a term list, a --plane ci leakscan run
        # reports "structural + local" while this line used to assert "partial
        # cover" — the delta's own test (identical output for materially
        # different cover) failed in mirror image. Floor cannot read the
        # scanner's answer without capturing child output, and streaming it live
        # is worth more than closing a gap that errs toward claiming LESS. So
        # the line states the invocation, which is always true, instead of
        # asserting a cover level it cannot observe. The 🟡 stays: on a real
        # runner, which holds no list, the reduced cover is real.
        partial = ""
        if scanner.full_cover_flag and scanner.full_cover_flag not in argv:
            partial = (f"cover not guaranteed — the {plane} plane does not pass "
                       f"{scanner.full_cover_flag}")
        # Scope drift on a SOFTENABLE check (TA3). The blocking guard above
        # covers only checks with no advisory form; a softenable one whose
        # scope has partly stopped resolving just quietly ran on less, with no
        # line anywhere and the board showing the declared scope as if it were
        # the scanned one. It must not block — that is the code-only-repo case
        # the skip branch exists for — but shrunken cover reported as full is
        # the defect this whole track is about, so it renders 🟡 and reaches
        # `--json` and the fleet board by the same route as EP3's.
        elif missing:
            partial = (f"{len(missing)} of {len(declared)} scope paths missing "
                       f"({', '.join(missing)}) — ran on the rest")
        adv = cfg.advisory.get(scanner.name) if state == "advisory" else None
        results.append(Result(
            scanner.name, state, rc, local=scanner.is_local, partial=partial,
            reason=(adv.why if adv else ""),
            review_by=(adv.review_by or "" if adv else ""),
            expired=bool(adv and adv.expired(_today())),
            legacy=bool(adv and adv.legacy),
        ))
    return results


def render(results: list[Result], plane: str) -> str:
    icon = {"enforced": "✅", "advisory": "⚠️ ", "disabled": "⏭ ", "skipped": "⏭ "}
    lines = [f"atelier floor — {plane} plane"]
    for r in results:
        # A partial pass gets its own mark. It passed and it blocks, so it is
        # not ❌ — but rendering it ✅ beside a full-cover check is the exact
        # claim EP3 caught: identical output for materially different cover.
        mark = "❌" if r.failed else ("🟡" if r.partial and not r.failed
                                      else icon[r.state])
        # An advisory carries its reason and its end date on the line. Expired
        # is 🔴 and says so — it does not block (a commit failing on a date set
        # months ago is how a forcing function becomes a --no-verify habit), it
        # just stops looking like a decision anyone is still standing behind.
        if r.state == "advisory" and not r.failed:
            if r.legacy:
                mark = "🟡"
            elif r.expired:
                mark = "🔴"
        note = f"  ({r.reason})" if r.reason else (
            f"  ({r.partial})" if r.partial else "")
        if r.state == "advisory":
            if r.legacy:
                note += ("  ⚠️  no reason or review date — pre-C1 declaration, "
                         "migrate it")
            elif r.review_by:
                note += (f"  [review by {r.review_by}"
                         + (" — PASSED]" if r.expired else "]"))
        # A local check is marked, not segregated: it blocks the same commit as
        # a fleet check, so it belongs in the same list — but a reader must be
        # able to tell which line came from this repo's own decision.
        tag = " · local" if r.local else ""
        lines.append(f"  {mark} {r.name:<11} {r.state}{tag}{note}")
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

    # THE REPO-LOCAL SEAM — it must only ever ADD.
    tripwire = {"local": {"tripwire": {"run": "tools/tripwire.py",
                                       "why": "estate tokens never enter a commit",
                                       "planes": ["hook"]}}}
    with tempfile.TemporaryDirectory() as td:
        p = Path(td)
        (p / CONFIG_NAME).write_text(json.dumps(tripwire), encoding="utf-8")
        loaded = Config.load(p)
    check("local check parses", len(loaded.local) == 1)
    check("local check is marked local", loaded.local[0].is_local)
    hook_states = {s.name: st for s, st in plan("hook", loaded)}
    ci_states = {s.name: st for s, st in plan("ci", loaded)}
    check("local check enforces on its declared plane",
          hook_states["tripwire"] == "enforced")
    check("off-plane local check still lists, as skipped",
          ci_states["tripwire"] == "skipped")
    check("a local check does not disturb the fleet floor",
          hook_states["secretscan"] == "enforced" and len(hook_states) == len(SCANNERS) + 1)
    check("local scope is read from the declaration",
          subtrees(root, Config(local=(Scanner("x", [], [], [], "w", run="c.py",
                                               scope_paths=("src",)),)), "x") == ["src"])

    # Softening a local check uses the SAME two spellings as everything else.
    soft = {"local": tripwire["local"], "advisory": ["tripwire"]}
    with tempfile.TemporaryDirectory() as td:
        p = Path(td)
        (p / CONFIG_NAME).write_text(json.dumps(soft), encoding="utf-8")
        loaded = Config.load(p)
    check("local check can be advisory",
          dict((s.name, st) for s, st in plan("hook", loaded))["tripwire"] == "advisory")

    # The seam's own guards. The first is the load-bearing one: a local check
    # that could take a fleet scanner's name could silently replace it.
    rejects("local shadowing a fleet scanner",
            {"local": {"leakscan": {"run": "x.py", "why": "mine now"}}})
    rejects("local escaping the repo",
            {"local": {"t": {"run": "../../etc/evil.sh", "why": "w"}}})
    rejects("local with an absolute run path",
            {"local": {"t": {"run": "/usr/bin/env", "why": "w"}}})
    rejects("reasonless local", {"local": {"t": {"run": "x.py"}}})
    rejects("runless local", {"local": {"t": {"why": "w"}}})
    rejects("local on an unknown plane",
            {"local": {"t": {"run": "x.py", "why": "w", "planes": ["prod"]}}})
    rejects("local on no plane at all",
            {"local": {"t": {"run": "x.py", "why": "w", "planes": []}}})
    rejects("local as a list", {"local": [{"name": "t"}]})
    rejects("local tuned through the fleet blocks",
            {"local": {"t": {"run": "x.py", "why": "w"}},
             "flags": {"t": ["--quiet"]}})

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
            origin = "local" if s.is_local else "fleet"
            print(f"{s.name:<11} {state:<9} {origin:<6} {s.why}")
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
