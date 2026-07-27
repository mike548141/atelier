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

Exit codes (fail-safe — an estate we could not verify is never reported green):
  0  every child is wired (or pinned, which is a declared choice)
  1  at least one child is vendored, absent, or unknown — with --check
  2  environment error (not an atelier checkout, nothing discovered)

WHAT THIS CANNOT SEE — read before trusting a clean board
----------------------------------------------------------
- **Wired is not passing.** This proves a repo CALLS the floor, never that the
  floor is green there. A wired repo with 40 findings shows as wired. Whether the
  checks pass is that repo's CI run, and deliberately not this tool's claim.
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
- It reads workflow TEXT. A repo whose floor.yml calls the reusable workflow
  inside a job that never runs (a condition, a disabled workflow) reads as wired.
  Detecting that needs the Actions API and is not attempted.
- **A local check is reported as DECLARED, never as working.** The `➕` lines
  come from the child's `.atelier-floor.json` — its own checks, whose code this
  tool never fetches and could not run. Whether the script is there at all is
  `floor.py`'s question, answered where the repo is (it fails closed if not).
  Here the claim is only "this repo says it enforces this", which is still worth
  a line: it is the one class of check no other repo's board will ever mention.

Usage:
  floorfleet                 discover children + report
  floorfleet --remote        read each repo's default branch from GitHub
  floorfleet --check         exit 1 if any child is unguarded
  floorfleet --child <path>  report only the named child
  floorfleet --json          machine-readable
  floorfleet --selftest      prove the classification logic, offline
"""

from __future__ import annotations

import argparse
import base64
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
    advisory: list[str] = field(default_factory=list)
    disabled: dict[str, str] = field(default_factory=dict)
    # Checks this repo declares for itself (floor.py's repo-local seam). Read
    # here for the same reason `disabled` is: a rule the estate cannot see is a
    # rule the estate cannot reason about — and unlike a fleet check, nobody
    # else's floor will ever mention it.
    local: dict[str, str] = field(default_factory=dict)  # name -> why
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

    @property
    def ok(self) -> bool:
        return self.state in ("wired", "pinned")


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


def evaluate(child: Path, remote: bool) -> ChildFloor:
    read = _read_remote if remote else _read_local
    state, detail = classify(read(child, FLOOR_PATH))

    advisory: list[str] = []
    disabled: dict[str, str] = {}
    local: dict[str, str] = {}
    scope: dict[str, list[str]] = {}
    flags: dict[str, list[str]] = {}
    docs = ""
    raw = read(child, CONFIG_PATH)
    if raw:
        try:
            cfg = json.loads(raw)
            advisory = list(cfg.get("advisory", []) or [])
            scope = _str_lists(cfg.get("scope"))
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

    return ChildFloor(name=child.name, path=str(child), state=state, detail=detail,
                      hook=hook_state(child), shim=shim_state(read, child),
                      advisory=advisory, disabled=disabled, local=local,
                      scope=scope, flags=flags, docs=docs)


ICON = {"wired": "✅", "pinned": "📌", "vendored": "🛑", "absent": "🛑",
        "unknown": "⚠️"}
HOOK_ICON = {"tracked": "✅", "installed": "✅", "legacy": "⚠️", "none": "❌",
             "unknown": "⚠️"}
# The tracked shim, unlike the installed hook, is a fact about the REPO — so on
# --remote these icons carry an estate-wide claim, not a machine-local one.
SHIM_ICON = {"current": "✅", "legacy": "⚠️", "absent": "❌", "unknown": "⚠️"}


def render(infos: list[ChildFloor], remote: bool) -> str:
    plane = "GitHub default branches" if remote else "local working copies"
    lines = [f"atelier floor — estate conformance  ({plane})", ""]
    width = max((len(i.name) for i in infos), default=10)
    for i in sorted(infos, key=lambda x: (x.ok, x.name.lower())):
        lines.append(f"  {ICON.get(i.state, '?')} {i.name:<{width}}  "
                     f"{i.state:<9} {SHIM_ICON.get(i.shim, '?')} shim:{i.shim:<8} "
                     f"{HOOK_ICON.get(i.hook, '?')} hook:{i.hook:<9} "
                     f"{i.detail}")
        for name in i.advisory:
            lines.append(f"      ⚠️  {name} advisory — declared, still visible")
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
    else:
        lines.append(f"  all {len(infos)} children call atelier's floor ✓")

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
    p.add_argument("--check", action="store_true",
                   help="exit 1 if any child is not running the floor")
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
        roots = [Path(r).expanduser() for r in args.root] if args.root \
            else [atelier.parent]
        children = pins.discover(roots, atelier)

    if not children:
        print("floorfleet: no atelier children found under the search root",
              file=sys.stderr)
        return 2

    infos = [evaluate(c, args.remote) for c in
             sorted(children, key=lambda p: p.name.lower())]

    if args.json:
        terms_present, terms_detail = terms_state()
        print(json.dumps({"plane": "remote" if args.remote else "local",
                          # Machine-local, not per-child — see terms_state().
                          "terms": {"present": terms_present,
                                    "detail": terms_detail},
                          "children": [asdict(i) for i in infos]}, indent=2))
    else:
        print(render(infos, args.remote))

    return 1 if (args.check and any(not i.ok for i in infos)) else 0


if __name__ == "__main__":
    sys.exit(main())
