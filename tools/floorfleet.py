#!/usr/bin/env python3
"""floorfleet — is every repo in the estate actually running atelier's floor?

THE QUESTION THIS EXISTS TO ANSWER
-----------------------------------
On 2026-07-25, 12 of 13 children were running a scanner list frozen at their
scaffold date and had never executed five of atelier's checks. Nothing was
broken; nothing reported it either. The guards existed, were tested, were
CI-wired in atelier — and were pointed at nothing.

ADR 0008 removed the cause: a child now calls atelier's reusable floor instead of
copying it, so a new check reaches every repo with no child edit. But that fixes
propagation for repos that are WIRED. It cannot tell you a repo was never wired,
a repo whose workflow someone edited back into a copy, or a clone that has no
hook installed. Those are absences, and an absence never raises its hand.

**Scaffolding is not proof.** create-repo only covers repos it created, and sees
nothing that drifts afterwards. Enumeration is the proof, and this is the
enumeration: every child, what state its floor is in, and a non-zero exit if any
is unguarded. That is the difference between believing the policy propagated and
knowing it.

It is deliberately the same shape as `signfleet` — one tool answers for one repo,
this answers for the estate — and reuses the same `pins.discover`, so a repo the
pin tooling can see is a repo this can see. Solve once, reuse the building block.

TWO PLANES, AND WHY THE REMOTE ONE IS THE REAL ANSWER
------------------------------------------------------
  local (default)  reads the working copies beside atelier. Fast, offline, and
                   proves what is on THIS machine right now — including the hook,
                   which exists nowhere else.
  --remote         reads each repo's default branch from GitHub via `gh`. Slower
                   and needs auth, but it answers the question that actually
                   matters: what will run when someone pushes. A local clone can
                   be ahead, behind, or dirty; CI runs the default branch.

Prefer `--remote` for an estate-wide assurance claim. Use local for the hook
column and for a quick pass while working.

STATES
  wired      calls atelier's reusable floor — new checks arrive automatically
  pinned     calls it at a fixed SHA: propagation is deliberately frozen here
  vendored   a floor.yml that names scanners itself — the pre-ADR-0008 copy, and
             the state that produced the incident. It will go stale, silently.
  absent     no floor.yml at all: this repo's CI enforces nothing
  unknown    could not be read (no remote, gh failure, unreadable tree)

RUN STATES (--status only — the compliance question, not the conformance one)
  passing       the floor is green on the default branch
  failing       the floor ran and did not pass — this repo is RED
  behind        the last GREEN run was an older commit: newer ones are unscanned
  actions-off   Actions disabled for the repo, or the floor workflow disabled
  no-runs       the floor workflow has never run once
  unregistered  floor.yml is in the tree but GitHub lists no such workflow
  running       a run is in flight; no conclusion yet
  no-result     cancelled or skipped — not a failure, and not proof of a pass
  unknown       could not read (no remote, no Actions permission, gh failure)

Exit codes (fail-safe — an estate we could not verify is never reported green):
  0  every child is wired (or pinned, which is a declared choice)
  1  at least one child is vendored, absent, or unknown — with --check
  2  environment error (not an atelier checkout, nothing discovered)

  With `--status`, exit 1 also covers any repo whose floor is not `passing`.
  Only `passing` is green: `unknown` is a red, because the whole posture of this
  tool is that an unproven floor is never reported as a proven one.

WHAT THIS CANNOT SEE — read before trusting a clean board
----------------------------------------------------------
- **Wired is not passing — use `--status` to ask the second question.** By
  default this proves a repo CALLS the floor and nothing more: a wired repo with
  40 findings shows as wired. `--status` adds the compliance half, reading each
  repo's latest floor run so the board answers *wired **and** passing*. What
  remains outside even that: a run's conclusion is GitHub's word for it, and a
  floor that passed because half its checks were `disabled` still concludes
  success — which is why the advisory/disabled lines above it are not decoration.
- **The hook question is now two columns, and only one of them is local.** Since
  the shim became a tracked file, `shim:` reports whether `.githooks/pre-commit`
  is in the repo and routes through the registry — a fact about the REPO, so
  under `--remote` it is a genuine estate-wide claim, and a fresh clone gets it.
  `hook:` remains machine-local, because what git will not transport is
  `core.hooksPath`: the config that makes the tracked shim actually run. So the
  residual has shrunk from "hooks are unknowable remotely" to "whether this
  clone points at them is unknowable remotely" — real, but much smaller. CI
  stays the backstop precisely because that last step cannot be guaranteed.
- **Discovery is one level under the search roots**, and only repos carrying an
  atelier pin in CLAUDE.md. A child nested deeper, or one that never took a pin,
  is invisible here — it will not show as a red, it will not show at all. That is
  the one absence this tool cannot report on itself.
- **Without `--status` it reads workflow TEXT only.** A repo whose floor.yml
  calls the reusable workflow inside a job that never runs — a condition, a
  disabled workflow, or GitHub Actions switched off for the whole repo — reads as
  wired, because wiring is a fact about a FILE and a file cannot tell you the
  runner was ever switched on. `--status` closes this: a repo with Actions off
  reports `actions-off` or `no-runs`, never green. The repo-level switch is read
  authoritatively when the token carries the **Administration** permission and
  inferred from run history when it does not; the board says which it used
  rather than leaving a reader to assume the stronger one.
- **A local check is reported as DECLARED, never as working.** The `➕` lines
  come from the child's `.atelier-floor.json` — its own checks, whose code this
  tool never fetches and could not run. Whether the script is there at all is
  `floor.py`'s question, answered where the repo is (it fails closed if not).
  Here the claim is only "this repo says it enforces this", which is still worth
  a line: it is the one class of check no other repo's board will ever mention.

Usage:
  floorfleet                 discover children + report
  floorfleet --remote        read each repo's default branch from GitHub
  floorfleet --status        also read each repo's latest floor RUN
  floorfleet --check         exit 1 if any child is unguarded
  floorfleet --child <path>  report only the named child
  floorfleet --json          machine-readable
  floorfleet --selftest      prove the classification logic, offline
"""

from __future__ import annotations

import argparse
import base64
import datetime
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pins  # noqa: E402  — the shared fleet-discovery building block
# Imported for its term-list resolution ONLY, so the board and the scanner
# cannot disagree about where the list lives. Re-implementing the lookup here
# would be the two-lists bug this whole design exists to avoid.
import leakscan  # noqa: E402

FLOOR_PATH = ".github/workflows/floor.yml"
CONFIG_PATH = ".atelier-floor.json"
# Mirrors floor.py's `Config.docs` default. Only a departure from it is worth a
# board line: every repo declaring the default would be noise, not signal.
DEFAULT_DOCS = "docs"

# The caller line a wired repo carries. Owner is matched loosely so an adopter
# pointing at their own atelier fork still classifies as wired rather than
# vendored — the doctrine travels, the account name is this estate's instance.
CALLER_RE = re.compile(
    r"uses:\s*[\w.-]+/[\w.-]+/\.github/workflows/floor\.yml@(?P<ref>\S+)"
)
SCANNER_RE = re.compile(r"\b\w+scan\.py")


def _strip_comments(text: str) -> str:
    """Only executable YAML counts. Both the thin caller and this tool discuss
    scanners in prose; a header sentence must not read as a vendored copy."""
    return "\n".join(ln for ln in text.splitlines()
                     if not ln.lstrip().startswith("#"))


def classify(floor_text: str | None) -> tuple[str, str]:
    """(state, detail) for one repo's floor.yml. Pure — the selftest drives it."""
    if floor_text is None:
        return "absent", "no floor.yml — this repo's CI enforces nothing"
    body = _strip_comments(floor_text)
    m = CALLER_RE.search(body)
    if m:
        ref = m.group("ref")
        if ref == "main":
            return "wired", "calls atelier's floor @main"
        return "pinned", f"calls atelier's floor @{ref} — propagation frozen here"
    if SCANNER_RE.search(body):
        return "vendored", "names scanners itself — a copy that will go stale"
    return "unknown", "floor.yml present but neither a caller nor a copy"


@dataclass
class ChildFloor:
    name: str
    path: str
    state: str
    detail: str
    hook: str = "unknown"
    shim: str = "unknown"
    # name -> (why, review-by). Empty strings mean a pre-C1 bare-list
    # declaration, which is exactly what the board needs to show as unmigrated.
    advisory: dict[str, tuple[str, str]] = field(default_factory=dict)
    disabled: dict[str, str] = field(default_factory=dict)
    # Checks this repo declares for itself (floor.py's repo-local seam). Read
    # here for the same reason `disabled` is: a rule the estate cannot see is a
    # rule the estate cannot reason about — and unlike a fleet check, nobody
    # else's floor will ever mention it.
    local: dict[str, str] = field(default_factory=dict)  # name -> why
    # atelier's own row. It conforms by RUNNING the floor it ships rather than
    # by calling a shared one, so it is counted and worded separately — but it
    # is held in the same list and judged by the same `ok`, because a parent
    # exempt from its own board is how the parent stopped being checked at all.
    is_parent: bool = False
    # WHERE a check looks and WHAT ARGUMENTS it gets. Both narrow a check's
    # cover without removing it, so before this they were the one softening no
    # board read — `floor.py` claimed they were "read out estate-wide by
    # floorfleet" and they were not (ADR 0008 cold pass, EP1/EP2). A reduced
    # boundary check is at least as reviewable as a removed one.
    scope: dict[str, list[str]] = field(default_factory=dict)   # name -> paths
    flags: dict[str, list[str]] = field(default_factory=dict)   # name -> argv
    # The records tree the prose checks read. Only surfaced when the child moved
    # it off the default: a non-default `docs` silently re-points every
    # docs-scoped check, and a `docs` naming no real tree skips them all.
    docs: str = ""
    # --status only. Conformance (`state`) and compliance (`run`) are two
    # different questions and this tool used to answer only the first; they are
    # held in separate fields for the same reason they are two questions.
    # "" means --status was not asked for, which is NOT the same as "unknown".
    run: str = ""
    run_detail: str = ""
    # Which authority answered the Actions-off question: "repo-switch" when the
    # `actions/permissions` read succeeded, "inferred" when it did not and the
    # answer rests on run history instead. Reported rather than assumed, because
    # a board that cannot say how well it knows something is the same failure as
    # a board that reports green on nothing.
    run_authority: str = ""
    # Which workflow file carries the floor. `floor.yml` for a child that calls
    # the reusable one; whichever of its own workflows actually runs `floor.py`
    # for the parent, which does not use a caller at all.
    workflow: str = ""

    @property
    def ok(self) -> bool:
        """CONFORMANCE — does this repo call the floor? Unchanged, deliberately:
        `--check` without `--status` must keep meaning exactly what it meant."""
        return self.state in ("wired", "pinned")

    @property
    def green(self) -> bool:
        """CONFORMANCE **and** COMPLIANCE — wired, and proven to be passing.

        Fail-safe by construction: every state that is not literally `passing`
        is not green, including `unknown`. The board exists because absences do
        not raise their hands, so an unread answer counts as a red one."""
        if not self.ok:
            return False
        return self.run in ("", "passing")


def _read_local(child: Path, rel: str) -> str | None:
    p = child / rel
    try:
        return p.read_text(encoding="utf-8") if p.is_file() else None
    except OSError:
        return None


def _slug(child: Path) -> str | None:
    """owner/repo from the origin remote, for the GitHub read."""
    r = subprocess.run(["git", "-C", str(child), "remote", "get-url", "origin"],
                       capture_output=True, text=True, check=False)
    if r.returncode != 0:
        return None
    url = r.stdout.strip()
    m = re.search(r"[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", url)
    return m.group(1) if m else None


def _read_remote(child: Path, rel: str) -> str | None:
    slug = _slug(child)
    if not slug:
        return None
    r = subprocess.run(
        ["gh", "api", f"repos/{slug}/contents/{rel}", "--jq", ".content"],
        capture_output=True, text=True, check=False,
    )
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        return base64.b64decode(r.stdout.strip()).decode("utf-8", "replace")
    except (ValueError, UnicodeError):
        return None


def _gh_json(path: str, *jq: str) -> object | None:
    """One `gh api` read, parsed. None on any failure — never a partial answer.

    Deliberately swallows the error rather than raising: every caller's fallback
    is the same, and it is `unknown`, which this tool already treats as
    not-green. A read we could not make must never become a pass."""
    cmd = ["gh", "api", path]
    for j in jq:
        cmd += ["--jq", j]
    r = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        return json.loads(r.stdout)
    except ValueError:
        return None


# The conclusions that mean the floor ran and did not pass. `cancelled` and
# `skipped` are held apart deliberately: they are not failures, but they are not
# evidence of a green floor either, and this tool's whole posture is that an
# unproven floor is never reported as proven.
FAILED_CONCLUSIONS = {"failure": "FAILED", "timed_out": "TIMED OUT",
                      "startup_failure": "FAILED TO START",
                      "stale": "went STALE"}
INCONCLUSIVE = {"cancelled", "skipped", "neutral", "action_required", None}


def classify_run(enabled: bool | None, wf_state: str | None,
                 latest: dict | None, head_sha: str | None,
                 runs_readable: bool) -> tuple[str, str]:
    """(state, detail) for one repo's floor RUN — the compliance question, as
    distinct from the conformance question `classify` answers.

    Pure, so the selftest drives every branch offline. Inputs:
      enabled        repo-level Actions switch: True / False / None (the
                     `actions/permissions` read needs the **Administration**
                     permission, which this tool deliberately does not require —
                     None means "not authorised to ask", not "fine").
      wf_state       'active' | 'disabled_manually' | 'disabled_inactivity' |
                     'missing' | None (unreadable)
      latest         newest run on the default branch, or None if none exist
      head_sha       default-branch head, or None if not read
      runs_readable  whether the runs listing succeeded at all

    WHY THE ORDER IS THE ORDER. Each branch above the next is a strictly better
    authority for the same question, so the first one that can answer does. The
    failure this closes is a board that read `wired ✅` for a repo running
    nothing at all (roadmap B3): wiring is a fact about a FILE, and a file
    cannot tell you the runner was ever switched on."""
    if enabled is False:
        return ("actions-off",
                "GitHub Actions is DISABLED for this repo — the floor is wired "
                "and cannot run")
    if wf_state is None and not runs_readable:
        return ("unknown",
                "could not read this repo's Actions — the token needs the "
                "Actions permission (read)")
    if wf_state == "missing":
        return ("unregistered",
                "floor.yml is in the tree but GitHub lists no such workflow — "
                "it has never landed on the default branch or never parsed")
    if wf_state in ("disabled_manually", "disabled_inactivity"):
        why = ("switched off by hand" if wf_state == "disabled_manually"
               else "auto-disabled by GitHub for repository inactivity")
        return ("actions-off", f"the floor workflow is disabled — {why}")
    if latest is None:
        # The inferential half of the Actions-off signal, and the reason this
        # tool does not need the Administration permission to close B3: a floor
        # that has never run once is the same practical absence, whether the
        # cause is a repo-level switch or something else.
        hedge = ("" if enabled is True else
                 " (repo-level Actions switch not readable — see the footer)")
        return ("no-runs",
                f"the floor workflow has NEVER run{hedge}")
    if latest.get("status") != "completed":
        return ("running", f"a run is {latest.get('status')} right now — "
                           "no conclusion yet")
    conclusion = latest.get("conclusion")
    if conclusion in FAILED_CONCLUSIONS:
        return ("failing", f"the last floor run {FAILED_CONCLUSIONS[conclusion]}"
                           " — this repo's floor is RED on its default branch")
    if conclusion in INCONCLUSIVE:
        ended = conclusion or "with no conclusion"
        return ("no-result",
                f"the last floor run ended {ended} — nothing was proven")
    if conclusion != "success":
        return ("unknown", f"unrecognised run conclusion {conclusion!r}")
    ran_on = latest.get("head_sha") or ""
    if head_sha and ran_on and ran_on != head_sha:
        # A green run against an older commit is the quietest way for this board
        # to be confidently wrong: it says PASSING about code that was never
        # scanned. Same family as the two defects above, one step subtler.
        return ("behind", f"last GREEN run was {ran_on[:8]}, but the default "
                          f"branch is now {head_sha[:8]} — newer commits are "
                          "unscanned")
    return ("passing", "the floor is green on the default branch")


SHIM_PATH = ".githooks/pre-commit"


def shim_state(read, child: Path) -> str:
    """Is the *tracked* pre-commit shim in the repo, and does it route through
    the registry rather than naming scanners itself?

    Unlike `hook_state` this is answerable on **either plane**, because
    `.githooks/pre-commit` is a file in the repository. It is the half of the
    hook question git actually transports: a fresh clone gets the shim, and all
    that remains machine-local is whether `core.hooksPath` points at it.
    """
    text = read(child, SHIM_PATH)
    if text is None:
        return "absent"
    return "current" if "floor.py" in text else "legacy"


def hook_state(child: Path) -> str:
    """Is a scan hook installed in THIS clone, and does it route through the
    registry? Machine-local by nature — see the docstring's residual."""
    hooks_path = subprocess.run(
        ["git", "-C", str(child), "config", "--get", "core.hooksPath"],
        capture_output=True, text=True, check=False).stdout.strip()
    candidates = []
    if hooks_path:
        candidates.append(child / hooks_path / "pre-commit")
    candidates.append(child / ".git" / "hooks" / "pre-commit")
    for hook in candidates:
        try:
            if not hook.is_file():
                continue
            text = hook.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "floor.py" in text:
            return "tracked" if hooks_path else "installed"
        return "legacy"  # a hook, but naming scanners itself
    return "none"


# The parent runs the floor from its OWN ci.yml, not through a caller — it
# holds the reusable workflow rather than pointing at one. Matching a caller
# line would therefore never fit it, and running the child classifier over its
# floor.yml reads the reusable workflow's scanner names as a stale vendored
# copy: exactly backwards.
PARENT_RUN_RE = re.compile(r"floor\.py\s+--plane\s+ci\b")
PARENT_WORKFLOWS = ".github/workflows"


def _live_yaml(text: str) -> str:
    """The workflow text with commented-out lines removed.

    TA5: the parent classifier matched anywhere in the concatenated workflow
    text, so a `ci.yml` whose only floor line was `# - run: python3
    tools/floor.py --plane ci` classified as `wired`. A parent that disabled
    its own floor and left the line in a comment — the ordinary way anyone
    disables a CI step — read GREEN on the board built to catch a parent
    quietly dropping its floor (A5b). The child classifier does not have this
    hole because it matches a structural caller line.

    Deliberately a lexer, not a YAML parse: a `#` outside quotes starts a
    comment, and that is the whole rule the failure needed. Parsing properly
    would mean a dependency the fleet board has always refused, and the board's
    idiom is text matching — the defect was that the matching was not
    line-aware, not that it was textual."""
    out: list[str] = []
    for line in text.splitlines():
        quote = ""
        for i, ch in enumerate(line):
            if quote:
                if ch == quote:
                    quote = ""
            elif ch in "\"'":
                quote = ch
            elif ch == "#":
                line = line[:i]
                break
        out.append(line)
    return "\n".join(out)


def main_checkout(repo: Path) -> Path:
    """The main checkout behind `repo`, which IS `repo` unless it is a worktree.

    `--git-common-dir` points at the main checkout's `.git` from any worktree,
    so its parent is the main checkout itself. Falls back to `repo` whenever
    git cannot answer — a non-repo directory, or no git on PATH."""
    try:
        out = subprocess.run(["git", "-C", str(repo), "rev-parse",
                              "--git-common-dir"],
                             capture_output=True, text=True, check=False)
        if out.returncode == 0 and out.stdout.strip():
            common = Path(out.stdout.strip())
            if not common.is_absolute():
                common = (repo / common)
            return common.resolve().parent
    except OSError:
        pass
    return repo


def _repo_name(repo: Path) -> str:
    """The repo's name, not the directory's. These differ inside a git worktree,
    and this repo's own doctrine says to take a worktree for write-heavy work —
    so the naive basename would label the parent row with a branch-shaped
    scratch name on exactly the sessions most likely to be changing the floor."""
    return main_checkout(repo).name


def evaluate_parent(atelier: Path) -> ChildFloor:
    """atelier's own row.

    Discovery walks CHILDREN, so the repo that defines the floor was
    structurally invisible to the board whose whole purpose is proving
    conformance — a parent that quietly dropped its own floor is precisely what
    ADR 0008 says enumeration must catch, and nothing would have. That is the
    same defect as an unwired child, one level up (roadmap A5b; A5a was its
    other half, where the parent genuinely was not running the floor it ships).

    Conformance means something different here and the row says which: a child
    proves it CALLS the shared floor, while the parent proves it RUNS the floor
    it ships, over its own tree, with its scoping declared the way a child
    declares it."""
    text = ""
    # WHICH workflow carries the floor, not just whether one does. --status has
    # to ask GitHub for a named workflow's runs, and the parent does not use the
    # caller filename its children do, so the run question is unanswerable for
    # the parent without this. Recorded per-file rather than inferred later.
    carrier = ""
    wf = atelier / PARENT_WORKFLOWS
    if wf.is_dir():
        for path in sorted(wf.glob("*.yml")):
            # floor.yml is the reusable workflow the CHILDREN call; it proves
            # nothing about whether the parent runs the floor over itself.
            if path.name == "floor.yml":
                continue
            try:
                # Newline-joined: concatenating raw would splice one file's
                # last line onto the next file's first and could manufacture a
                # match across a boundary that exists in neither file.
                body = path.read_text(encoding="utf-8") + "\n"
            except OSError:
                continue
            text += body
            if not carrier and PARENT_RUN_RE.search(_live_yaml(body)):
                carrier = path.name
    if PARENT_RUN_RE.search(_live_yaml(text)):
        state, detail = "wired", "runs the floor it ships, over its own tree"
    else:
        state, detail = "absent", ("ships the floor and does not run it — "
                                   "no `floor.py --plane ci` in its own workflows")
    info = _read_declarations(atelier, _read_local, state, detail)
    info.name = f"{_repo_name(atelier)} (parent)"
    info.path = str(atelier)
    info.is_parent = True
    info.hook = hook_state(atelier)
    info.shim = shim_state(_read_local, atelier)
    info.workflow = carrier
    return info


def terms_state() -> tuple[bool, str]:
    """Does this machine carry the leakscan term list? Returns (present, detail).

    Asked through leakscan's own resolver so the answer cannot drift from the
    scanner's. This is the measurement half of the two-plane design: the hook
    plane now REFUSES to pass without a term list, so the board reporting the
    list's absence is what turns "the hook has full cover" from an inference
    into something an operator can see before their first commit fails."""
    path = leakscan.resolve_terms_path(None)
    if path is None:
        return False, (f"absent on this machine (looked for $ATELIER_LEAKSCAN_TERMS, "
                       f"then {leakscan.DEFAULT_LOCAL_TERMS})")
    return True, f"present at {path}"


def _today() -> str:
    """Today in UTC, ISO 8601 — the same clock floor.py ages against, so the
    board and the hook never disagree about whether a date has passed."""
    return datetime.datetime.now(datetime.timezone.utc).date().isoformat()


def _days_over(review_by: str, today: str) -> str:
    """How long an expired advisory has been standing, in words. The count is
    the point: "expired" alone reads the same on day one and day two hundred,
    and it is the second one that means the declaration was abandoned."""
    try:
        days = (datetime.date.fromisoformat(today)
                - datetime.date.fromisoformat(review_by)).days
    except ValueError:
        return "date unreadable"
    if days < 1:
        return "today"
    if days == 1:
        return "1 day over"
    return f"{days} days over"


def _advisories(raw: object) -> dict[str, tuple[str, str]]:
    """`advisory` as declared, in either C1 spelling: name -> (why, review-by).

    A bare list is the pre-C1 form and yields empty strings for both, which is
    what makes an unmigrated declaration visible on the board rather than
    indistinguishable from a reasoned one. Same contract as everything else
    read here — report what the config SAYS, never what floor.py would make of
    it, and stay readable against a malformed one."""
    if isinstance(raw, (list, tuple)):
        return {str(name): ("", "") for name in raw}
    if not isinstance(raw, dict):
        return {}
    out: dict[str, tuple[str, str]] = {}
    for name, decl in raw.items():
        if isinstance(decl, dict):
            out[str(name)] = (str(decl.get("why", "") or ""),
                              str(decl.get("review-by", "") or ""))
        else:
            out[str(name)] = ("", "")
    return out


def _scope_paths(raw: object) -> dict[str, list[str]]:
    """`scope` as declared, in either C1 spelling: name -> list of paths. The
    A1(b) object form carries a `why` too, which the board does not print — the
    🔎 line's job is to say where a check looks, and a repo that narrowed a
    boundary check is already the thing being pointed at."""
    if not isinstance(raw, dict):
        return {}
    out: dict[str, list[str]] = {}
    for name, value in raw.items():
        if isinstance(value, str):
            out[str(name)] = [value]
        elif isinstance(value, list):
            out[str(name)] = [str(v) for v in value]
        elif isinstance(value, dict):
            paths = value.get("paths")
            if isinstance(paths, str):
                out[str(name)] = [paths]
            elif isinstance(paths, list):
                out[str(name)] = [str(p) for p in paths]
    return out


def _str_lists(raw: object) -> dict[str, list[str]]:
    """`scope`/`flags` as declared: name -> list of strings. Same contract as
    `local` below — report what the config SAYS, never what floor.py would make
    of it, and stay readable against a malformed one. A bare string is accepted
    for the same reason floor.py accepts it."""
    if not isinstance(raw, dict):
        return {}
    out: dict[str, list[str]] = {}
    for name, value in raw.items():
        if isinstance(value, str):
            out[str(name)] = [value]
        elif isinstance(value, list):
            out[str(name)] = [str(v) for v in value]
    return out


def _read_declarations(repo: Path, read, state: str, detail: str) -> ChildFloor:
    """The `.atelier-floor.json` half of a row, shared by the child path and the
    parent path. Only how a repo's floor is WIRED differs between them; what it
    declares is the same file in the same format, and reading it twice in two
    places is how the two rows would come to disagree."""
    advisory: list[str] = []
    disabled: dict[str, str] = {}
    local: dict[str, str] = {}
    scope: dict[str, list[str]] = {}
    flags: dict[str, list[str]] = {}
    docs = ""
    raw = read(repo, CONFIG_PATH)
    if raw:
        try:
            cfg = json.loads(raw)
            advisory = _advisories(cfg.get("advisory"))
            scope = _scope_paths(cfg.get("scope"))
            flags = _str_lists(cfg.get("flags"))
            raw_docs = cfg.get("docs")
            docs = str(raw_docs) if isinstance(raw_docs, str) else ""
            d = cfg.get("disabled", {}) or {}
            disabled = {k: str(v) for k, v in d.items()} if isinstance(d, dict) else {}
            loc = cfg.get("local", {}) or {}
            if isinstance(loc, dict):
                # Report what the declaration SAYS, not what floor.py would make
                # of it. This tool reads text off a default branch and must stay
                # readable against a malformed config — floor.py is the thing
                # that blocks on one, and it runs where the repo is.
                local = {k: str((v or {}).get("why", "") if isinstance(v, dict) else "")
                         for k, v in loc.items()}
        except ValueError:
            detail += " (unreadable .atelier-floor.json)"

    return ChildFloor(name=repo.name, path=str(repo), state=state, detail=detail,
                      hook=hook_state(repo), shim=shim_state(read, repo),
                      advisory=advisory, disabled=disabled, local=local,
                      scope=scope, flags=flags, docs=docs)


def read_run(child: Path, workflow: str) -> tuple[str, str]:
    """Gather the Actions facts for one repo and hand them to `classify_run`.

    All the I/O lives here so the decision stays pure and testable — the same
    split `classify` already uses. Three reads, and the tool is designed to work
    with only two of them authorised:

      actions/permissions  the repo-level Actions switch. Needs the
                           **Administration** permission, which is the
                           repo-SETTINGS permission — a large step up from
                           read-only content for one boolean. Treated as
                           optional on purpose: when it 403s we fall through to
                           the inferential signal (a floor that has never run)
                           rather than requiring a wider token estate-wide.
      actions/workflows    per-workflow state. Needs **Actions** (read).
      .../runs             the newest run on the default branch. Same.

    The default-branch head comes from the repo read, so a green run against an
    older commit reports as `behind` rather than as a pass."""
    slug = _slug(child)
    if not slug:
        return ("unknown", "no origin remote — nothing to ask GitHub about", "")

    perms = _gh_json(f"repos/{slug}/actions/permissions")
    enabled = perms.get("enabled") if isinstance(perms, dict) else None
    authority = "repo-switch" if isinstance(enabled, bool) else "inferred"

    repo = _gh_json(f"repos/{slug}")
    branch = repo.get("default_branch") if isinstance(repo, dict) else None
    head_sha = None
    if branch:
        ref = _gh_json(f"repos/{slug}/commits/{branch}", ".sha")
        head_sha = ref if isinstance(ref, str) else None

    listing = _gh_json(f"repos/{slug}/actions/workflows")
    wf_state = None
    if isinstance(listing, dict):
        want = f".github/workflows/{workflow}"
        wf_state = "missing"
        for w in listing.get("workflows", []):
            if w.get("path") == want:
                wf_state = w.get("state")
                break

    runs_readable = False
    latest = None
    q = f"repos/{slug}/actions/workflows/{workflow}/runs?per_page=1"
    if branch:
        q += f"&branch={branch}"
    got = _gh_json(q)
    if isinstance(got, dict) and "workflow_runs" in got:
        runs_readable = True
        runs = got.get("workflow_runs") or []
        latest = runs[0] if runs else None

    state, detail = classify_run(enabled, wf_state, latest, head_sha,
                                 runs_readable)
    return (state, detail, authority)


def evaluate(child: Path, remote: bool, status: bool = False) -> ChildFloor:
    read = _read_remote if remote else _read_local
    state, detail = classify(read(child, FLOOR_PATH))
    info = _read_declarations(child, read, state, detail)
    info.workflow = "floor.yml"
    if status:
        info.run, info.run_detail, info.run_authority = \
            read_run(child, info.workflow)
    return info


ICON = {"wired": "✅", "pinned": "📌", "vendored": "🛑", "absent": "🛑",
        "unknown": "⚠️"}
HOOK_ICON = {"tracked": "✅", "installed": "✅", "legacy": "⚠️", "none": "❌",
             "unknown": "⚠️"}
# The tracked shim, unlike the installed hook, is a fact about the REPO — so on
# --remote these icons carry an estate-wide claim, not a machine-local one.
SHIM_ICON = {"current": "✅", "legacy": "⚠️", "absent": "❌", "unknown": "⚠️"}
# Only `passing` is green. `behind` and `no-result` are amber because something
# ran; everything else is a red, including `unknown` — see ChildFloor.green.
RUN_ICON = {"passing": "✅", "failing": "🛑", "actions-off": "🛑",
            "no-runs": "🛑", "unregistered": "🛑", "behind": "⚠️",
            "no-result": "⚠️", "running": "⏳", "unknown": "⚠️"}


def render(infos: list[ChildFloor], remote: bool, status: bool = False) -> str:
    plane = "GitHub default branches" if remote else "local working copies"
    heading = "estate conformance" + (" + compliance" if status else "")
    lines = [f"atelier floor — {heading}  ({plane})", ""]
    width = max((len(i.name) for i in infos), default=10)
    # Parent first, then failures, then the rest — the two rows a reader needs
    # before the ones that are fine.
    # With --status the sort leads on `green`, not `ok`: a wired repo whose
    # floor is red is now one of the rows a reader needs first, and sorting it
    # among the healthy ones would re-hide exactly what --status exists to show.
    for i in sorted(infos, key=lambda x: (not x.is_parent,
                                          x.green if status else x.ok,
                                          x.name.lower())):
        lines.append(f"  {ICON.get(i.state, '?')} {i.name:<{width}}  "
                     f"{i.state:<9} {SHIM_ICON.get(i.shim, '?')} shim:{i.shim:<8} "
                     f"{HOOK_ICON.get(i.hook, '?')} hook:{i.hook:<9} "
                     f"{i.detail}")
        if status:
            # Its own line, not another column: the run detail is a sentence
            # (which commit, which conclusion) and the row is already at width.
            lines.append(f"      {RUN_ICON.get(i.run, '?')} run:{i.run:<12} "
                         f"{i.run_detail}")
        # The C1 line. An advisory is tracked debt, so the board shows the debt:
        # why it was taken on and when it was due. A passed date goes 🔴 and
        # says how long it has been standing — the board is the whole forcing
        # function here, deliberately, because nothing blocks on a review date
        # (ruled 2026-07-28). An unmigrated bare-list declaration is 🟡: it
        # cannot state a reason at all, which is the thing being fixed.
        today = _today()
        for name, (why, review_by) in sorted(i.advisory.items()):
            if not review_by:
                lines.append(
                    f"      🟡 {name} advisory — no reason or review date "
                    "(pre-C1 declaration, migrate it)")
            elif review_by < today:
                lines.append(
                    f"      🔴 {name} advisory EXPIRED {review_by} "
                    f"({_days_over(review_by, today)}) — {why}")
            else:
                lines.append(
                    f"      ⚠️  {name} advisory until {review_by} — {why}")
        for name, why in i.disabled.items():
            lines.append(f"      ⏭  {name} disabled — {why}")
        for name, why in i.local.items():
            lines.append(f"      ➕ {name} local — {why or 'no reason declared'}")
        # Cover reductions, printed beside the removals. `scope` is what a check
        # READS and `flags` is how it RUNS; either can shrink a boundary check
        # to a subtree, or to nothing, without ever appearing as `disabled`.
        for name, paths in i.scope.items():
            lines.append(f"      🔎 {name} scoped to {', '.join(paths)} — "
                         "reads nothing outside this")
        for name, argv in i.flags.items():
            lines.append(f"      🔧 {name} flags {' '.join(argv)} — "
                         "check runs modified")
        if i.docs and i.docs != DEFAULT_DOCS:
            lines.append(f"      📁 records tree is {i.docs}, not "
                         f"{DEFAULT_DOCS} — every docs-scoped check follows it")

    bad = [i for i in infos if not i.ok]
    lines.append("")
    if bad:
        lines.append(f"  {len(bad)} of {len(infos)} repo(s) are NOT running "
                     "atelier's floor:")
        for i in bad:
            lines.append(f"    - {i.name}: {i.detail}")
        lines.append("")
        lines.append("  Wire one with the thin caller in "
                     "docs/build/templates/workflows/floor.yml")
        if any(i.is_parent for i in bad):
            # Worth its own line: the parent's remedy is not a caller, so the
            # advice above does not fit it, and a parent that ships a floor it
            # does not run is the failure with the widest reach.
            lines.append("  The PARENT's remedy is different: it runs the floor "
                         "it ships, so its own")
            lines.append("  workflow needs `python3 tools/floor.py --plane ci "
                         "--root .`")
    else:
        kids = sum(1 for i in infos if not i.is_parent)
        lines.append(f"  all {kids} children call atelier's floor ✓  "
                     "(and the parent runs it)")

    if status:
        # Reported SEPARATELY from conformance, never folded into it. They are
        # two questions — "does this repo call the floor" and "is that floor
        # green" — and the roadmap item exists because one board answered only
        # the first while reading like it answered both.
        unproven = [i for i in infos if i.run != "passing"]
        lines.append("")
        if unproven:
            lines.append(f"  {len(unproven)} of {len(infos)} repo(s) are wired "
                         "but NOT PROVEN GREEN:")
            for i in unproven:
                lines.append(f"    - {i.name}: {i.run} — {i.run_detail}")
        else:
            lines.append(f"  all {len(infos)} floors are GREEN on their default "
                         "branches ✓")

        # The honesty line. Without it, "no repo has Actions disabled" reads as
        # a checked fact when it may be an unasked question.
        inferred = [i.name for i in infos if i.run_authority == "inferred"]
        if inferred:
            lines.append("")
            lines.append(f"  ⚠️  Actions-off was INFERRED (not read) for "
                         f"{len(inferred)} repo(s): the token cannot read the "
                         "repo-level")
            lines.append("     Actions switch, which needs the Administration "
                         "permission. A floor that has never")
            lines.append("     run still shows as a red here, so the blind spot "
                         "is covered — but by inference.")

    # The personal-data half of leakscan, reported as what it actually is: a
    # fact about THIS MACHINE, not about any repo. A per-child column would have
    # been the wrong shape — the term list lives in ~/.claude/, outside every
    # repo, so it is identical for all of them and belongs on the board once.
    # Under --remote the child rows describe GitHub's default branches while
    # this line still describes the machine you are standing on; the wording
    # says so rather than leaving a reader to infer it.
    present, terms_detail = terms_state()
    lines.append("")
    if present:
        lines.append(f"  ✅ personal-data term list: {terms_detail}")
        lines.append("     hook-plane leakscan has full cover on this machine.")
    else:
        lines.append(f"  ❌ personal-data term list: {terms_detail}")
        lines.append("     Every repo's hook-plane leakscan BLOCKS until one "
                     "exists — leakscan refuses to")
        lines.append("     report a structural-only scan as a pass. Copy "
                     "tools/leakscan-terms.example.txt")
        lines.append(f"     to {leakscan.DEFAULT_LOCAL_TERMS} and fill it in.")

    shimless = [i.name for i in infos if i.shim in ("absent", "legacy")]
    if shimless:
        lines.append("")
        lines.append(f"  Tracked shim missing or stale ({plane} — travels with a "
                     "clone): " + ", ".join(shimless))

    hookless = [i.name for i in infos if i.hook in ("none", "legacy")]
    if hookless:
        lines.append("")
        lines.append("  Local hook gaps (this machine only — core.hooksPath never "
                     "travels): " + ", ".join(hookless))
    return "\n".join(lines)


def _selftest() -> int:
    fails: list[str] = []

    def check(label: str, got: str, want: str) -> None:
        if got != want:
            fails.append(f"{label}: expected {want}, got {got}")

    thin = (
        "name: floor\n"
        "# this header mentions secretscan.py deliberately, in prose\n"
        "jobs:\n  floor:\n"
        "    uses: mike548141/atelier/.github/workflows/floor.yml@main\n"
    )
    check("thin caller", classify(thin)[0], "wired")

    pinned = thin.replace("@main", "@a1b2c3d4")
    check("pinned caller", classify(pinned)[0], "pinned")

    # An adopter pointing at their own fork is still wired — the doctrine
    # travels even when the account does not.
    check("forked owner", classify(thin.replace("mike548141", "someone-else"))[0],
          "wired")

    vendored = (
        "name: floor\njobs:\n  floor:\n    steps:\n"
        "      - run: python3 atelier/tools/secretscan.py --root repo repo\n"
    )
    check("vendored copy", classify(vendored)[0], "vendored")

    # The crux: a comment naming a scanner must NOT read as a vendored copy,
    # or every correctly-wired child reports as broken.
    commented = "# - run: python3 atelier/tools/sizescan.py\n" + thin
    check("commented scanner", classify(commented)[0], "wired")

    check("absent floor", classify(None)[0], "absent")
    check("unrecognised floor", classify("name: floor\njobs:\n  x:\n    steps: []\n")[0],
          "unknown")

    # --status: every branch of the run classifier, offline. The three that
    # matter most are the ones a board would previously have shown as green —
    # Actions switched off, a floor that never ran, and a green run against a
    # commit that is no longer the head.
    def run(enabled=True, wf="active", latest=None, head=None, readable=True):
        return classify_run(enabled, wf, latest, head, readable)

    def completed(conclusion, sha="aaaa1111"):
        return {"status": "completed", "conclusion": conclusion, "head_sha": sha}

    check("actions off (repo)", run(enabled=False)[0], "actions-off")
    check("actions off (workflow)", run(wf="disabled_manually")[0], "actions-off")
    check("auto-disabled", run(wf="disabled_inactivity")[0], "actions-off")
    check("never ran", run(latest=None)[0], "no-runs")
    check("no such workflow", run(wf="missing")[0], "unregistered")
    check("nothing readable", run(enabled=None, wf=None, readable=False)[0],
          "unknown")
    check("green", run(latest=completed("success"), head="aaaa1111")[0],
          "passing")
    check("red", run(latest=completed("failure"))[0], "failing")
    check("timed out", run(latest=completed("timed_out"))[0], "failing")
    check("cancelled", run(latest=completed("cancelled"))[0], "no-result")
    check("in flight", run(latest={"status": "in_progress"})[0], "running")
    # The subtle one: a SUCCESS conclusion that proves nothing about the code
    # sitting on the branch today.
    check("green but behind",
          run(latest=completed("success", "aaaa1111"), head="bbbb2222")[0],
          "behind")
    # ...and its mirror: no head read means no staleness claim, not a false one.
    check("green, head unknown",
          run(latest=completed("success"), head=None)[0], "passing")

    # The fail-safe contract `--check --status` rests on: only `passing` is
    # green, and `unknown` must never slip through as one.
    for state in ("failing", "actions-off", "no-runs", "unregistered",
                  "behind", "no-result", "running", "unknown"):
        info = ChildFloor(name="x", path="/x", state="wired", detail="",
                          run=state)
        check(f"green({state})", str(info.green), "False")
    check("green(passing)",
          str(ChildFloor(name="x", path="/x", state="wired", detail="",
                         run="passing").green), "True")
    # A repo that is not even wired is never green, whatever its runs say.
    check("green(unwired+passing)",
          str(ChildFloor(name="x", path="/x", state="absent", detail="",
                         run="passing").green), "False")

    for f in fails:
        print(f"floorfleet selftest FAIL: {f}", file=sys.stderr)
    print(f"floorfleet selftest: {'FAILED' if fails else 'ok'} "
          f"({len(fails)} failure(s))")
    return 1 if fails else 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="floorfleet",
                                description=__doc__.split("\n")[0])
    p.add_argument("--atelier", help="path to atelier (default: this checkout)")
    p.add_argument("--root", action="append",
                   help="search root for discovery (repeatable; default: "
                        "atelier's parent dir)")
    p.add_argument("--child", action="append", help="report only this child path")
    p.add_argument("--remote", action="store_true",
                   help="read each repo's default branch from GitHub via gh")
    p.add_argument("--status", action="store_true",
                   help="also read each repo's latest floor RUN — wired and "
                        "passing, not just wired (needs gh Actions read)")
    p.add_argument("--check", action="store_true",
                   help="exit 1 if any child is not running the floor "
                        "(with --status, also if any floor is not green)")
    p.add_argument("--json", action="store_true", help="machine-readable")
    p.add_argument("--selftest", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.selftest:
        return _selftest()

    try:
        atelier = pins.resolve_atelier(args.atelier)
    except Exception as e:
        print(f"floorfleet: {e}", file=sys.stderr)
        print("floorfleet: run this from an atelier checkout, or pass --atelier <path>.",
              file=sys.stderr)
        return 2

    if args.child:
        children = []
        for c in args.child:
            p = Path(c).expanduser()
            if not p.is_dir():
                print(f"floorfleet: named child not found: {p}", file=sys.stderr)
                return 2
            children.append(p)
    else:
        # Search beside the MAIN checkout, not beside this one (TA7). Run from
        # a worktree the naive `atelier.parent` is `.claude/worktrees/`, which
        # holds no children, so the board reported "no atelier children found"
        # in exactly the mode this repo's doctrine prescribes for write-heavy
        # work — i.e. whenever someone is changing the floor. `_repo_name`
        # already resolved the main checkout to label the parent row; the
        # intent reached the label and not the discovery.
        roots = [Path(r).expanduser() for r in args.root] if args.root \
            else [main_checkout(atelier).parent]
        children = pins.discover(roots, atelier)

    if not children:
        print("floorfleet: no atelier children found under the search root",
              file=sys.stderr)
        return 2

    infos = [evaluate(c, args.remote, args.status) for c in
             sorted(children, key=lambda p: p.name.lower())]
    # The parent goes on its own board. Discovery walks children, so without
    # this the one repo that DEFINES the floor is the one repo never checked
    # against it (roadmap A5b). Read locally even under --remote: --remote
    # answers "what runs on GitHub's default branch" for repos this machine may
    # not hold, whereas the parent is the checkout this tool is running from,
    # and claiming a remote reading of it would be the stronger claim.
    parent = evaluate_parent(atelier)
    # The parent's CONFORMANCE is read locally (above), but its run history only
    # exists on GitHub — so --status asks the same question of it as of any
    # child. A parent exempt from its own board is how the parent stopped being
    # checked at all; that argument does not weaken for the run column.
    if args.status:
        if parent.workflow:
            parent.run, parent.run_detail, parent.run_authority = \
                read_run(main_checkout(atelier), parent.workflow)
        else:
            parent.run, parent.run_detail = (
                "unknown", "no workflow of its own runs the floor — there is "
                           "no run history to read")
    infos.insert(0, parent)

    if args.json:
        terms_present, terms_detail = terms_state()
        print(json.dumps({"plane": "remote" if args.remote else "local",
                          "status": bool(args.status),
                          # Machine-local, not per-child — see terms_state().
                          "terms": {"present": terms_present,
                                    "detail": terms_detail},
                          "children": [asdict(i) for i in infos]}, indent=2))
    else:
        print(render(infos, args.remote, args.status))

    if not args.check:
        return 0
    # --status widens what `--check` demands, and says so in its help. Without
    # it the exit code answers conformance alone, exactly as before; nothing
    # that relied on the old meaning changes behaviour.
    failed = (not i.green for i in infos) if args.status \
        else (not i.ok for i in infos)
    return 1 if any(failed) else 0


if __name__ == "__main__":
    sys.exit(main())
