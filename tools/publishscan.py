#!/usr/bin/env python3
"""publishscan — the mechanical check that a repo does not TRACK files whose
publication weakens it.

THE QUESTION NO OTHER SCANNER ASKS
-----------------------------------
Every content scanner here asks *does this file contain something private?* —
a credential (`secretscan`), a personal or estate fact (`leakscan`). This one
asks a different question: *does publishing this file, whatever it contains,
tell a reader something that helps them attack the repo or the estate?*

They come apart, and the gap is not theoretical. `rpi` went public on
2026-07-29; its post-flip cold pass found (F1) that the committed
`.claude/settings.json` published the exact list of commands an AI session runs
**unprompted**, at the same moment going public opened untrusted inbound
(issues, PRs) into those sessions — prompt-injection reconnaissance moving from
a guess to a plan. `secretscan` and `leakscan` both passed that file, correctly:
it holds no credential and no personal fact. **The exposure was the file's
presence in the tree, not its contents.**

So the unit of judgement here is the PATH, and the finding is *tracked at all*.

WHAT THIS DOES NOT COVER — read before trusting a clean run
-----------------------------------------------------------
- **It cannot unpublish.** A path already in pushed history stays there; this
  stops the next one. `rpi`'s and atelier's historic copies are published for
  good.
- **It does not read file contents.** A `.env` full of nothing still reds (it
  should not be tracked); a credential in `config.py` is `secretscan`'s job,
  not this tool's. Layers, not alternatives.
- **The self-describing files it deliberately allows.** A repo's guard
  declarations — `.atelier-floor.json` (which checks are advisory or off),
  the `.<scanner>ignore` files (where scanning is exempted) — are ALSO a map of
  where the defences are weak, and they are equally unavoidable: the floor
  cannot run without them travelling with the repo. That exposure is accepted,
  not overlooked, and the mitigation is the one already in force — every
  exemption carries a stated reason, and the estate board reads narrowed scope
  out loud. Do not "fix" it by untracking them; that breaks the floor and
  hides the weakening at the same time.
- **It is a denylist**, so it knows only the shapes below. A novel file that
  maps the repo's defences passes until someone adds it here.

THE PATTERNS, WITH THEIR PROVENANCE
------------------------------------
Grounding is per-pattern, because this repo does not invent rules to fill a
heading. Two tiers, both stated rather than blurred:

  * FOUND HERE — a real finding in this estate.
      `.claude/settings.json`, `.claude/settings.local.json`
        The agent's unprompted-command allowlist. `rpi` F1, 2026-07-29; Mike
        ruled the same day (option ⓑ) that it is untracked EVERYWHERE, not
        only on public repos — a visibility-conditional rule becomes silently
        wrong the day a repo flips, and that day is when attention is
        elsewhere. This is the pattern the tool exists for.

  * STANDARD PRACTICE — not yet a finding here, and named as such. Each is a
    file whose whole purpose is machine-local configuration, so tracking one is
    a mistake independent of what it currently holds.
      `.mcp.json`            connected-service endpoints and server inventory
      `.env`, `.env.*`, `.envrc`   environment, the canonical secret carrier
      `.netrc`, `.npmrc`, `.pypirc`   credential-bearing tool config
      `.vscode/settings.json`, `.idea/**`   editor-local paths and tool config

HATCHES
-------
A glob in `.publishscanignore` exempts a path. There is deliberately NO
`publishscan:allow:` line marker: the marker convention works by writing a
reason INTO the offending file, and this scanner's whole finding is that the
file should not be in the repo at all — a marker inside it would be an
exemption nobody reviewing the tree would ever see. The ignore file keeps the
exemption where a reviewer reads it.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean (or --warn, which never blocks)
  1  never-publish path(s) tracked
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import subprocess
import sys
from pathlib import Path

IGNORE_FILE = ".publishscanignore"

# (glob, why). The glob is matched against repo-relative POSIX paths.
NEVER_PUBLISH: tuple[tuple[str, str], ...] = (
    (".claude/settings.json",
     "the agent's unprompted-command allowlist — publishing it maps an "
     "agent's unattended reach (rpi F1, Mike ruled 2026-07-29)"),
    (".claude/settings.local.json",
     "one person's agent settings; same allowlist exposure, plus it is "
     "personal ergonomics rather than repo policy"),
    (".mcp.json",
     "connected-service endpoints and server inventory"),
    (".env", "environment file — the canonical secret carrier"),
    (".env.*", "environment file — the canonical secret carrier"),
    ("*/.env", "environment file — the canonical secret carrier"),
    (".envrc", "direnv environment — machine-local by definition"),
    (".netrc", "credential-bearing tool config"),
    (".npmrc", "credential-bearing tool config (auth tokens)"),
    (".pypirc", "credential-bearing tool config (upload tokens)"),
    (".vscode/settings.json", "editor-local config: local paths, tool config"),
    (".idea/*", "editor-local config: local paths, tool config"),
    (".idea/**/*", "editor-local config: local paths, tool config"),
)


def load_ignores(root: Path) -> list[str]:
    """Globs from .publishscanignore — blank lines and `#` comments skipped."""
    f = root / IGNORE_FILE
    if not f.is_file():
        return []
    out = []
    for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def _ignored(path: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, g) for g in globs)


def matches(path: str) -> str | None:
    """The reason this path must not be tracked, or None."""
    for glob, why in NEVER_PUBLISH:
        if fnmatch.fnmatch(path, glob):
            return why
    return None


class NotARepo(Exception):
    """The tree is not under git at all — a complete scan of an empty set."""


def _git(root: Path, *args: str) -> list[str]:
    r = subprocess.run(["git", "-C", str(root), *args],
                       capture_output=True, text=True)
    if r.returncode != 0:
        err = r.stderr.strip()
        # A tree with no git is not a DEGRADED scan, it is a complete scan of
        # an empty tracked set: nothing is tracked, so nothing can be published
        # through git, and "no never-publish path is tracked" is simply true.
        # Skipping visibly here is not the fail-open the floor forbids — the
        # check has no cover to lose. (Found by floor.py's own test suite,
        # whose fixture trees are plain directories; the first cut hard-failed
        # them, which would have made this scanner unrunnable in every child's
        # fixtures.) Every OTHER git failure — git absent, repo corrupt,
        # permissions — IS a broken scan and stays exit 2.
        if "not a git repository" in err.lower():
            raise NotARepo(err)
        raise RuntimeError(err or "git failed")
    return [ln for ln in r.stdout.splitlines() if ln]


def tracked_paths(root: Path, staged: bool) -> list[str]:
    """The paths this plane judges.

    --staged asks what THIS COMMIT adds or renames into the tree — the hook's
    question, and the only one that can stop the mistake before it lands.
    Otherwise: everything git tracks, which is the CI backstop's question and
    the one that catches a file that slipped in before the check existed.
    """
    if staged:
        return _git(root, "diff", "--cached", "--name-only",
                    "--diff-filter=ACMR")
    return _git(root, "ls-files")


def run(root: Path, staged: bool, warn: bool, as_json: bool) -> int:
    try:
        paths = tracked_paths(root, staged)
    except NotARepo:
        if as_json:
            print(json.dumps({"scanned": 0, "staged": staged,
                              "findings": [], "skipped": "not a git repo"},
                             indent=2))
        else:
            print("✓ publishscan — not a git repository, so nothing is "
                  "tracked and nothing can be published from here.")
        return 0
    except RuntimeError as e:
        print(f"publishscan: {e}", file=sys.stderr)
        return 2
    globs = load_ignores(root)
    findings = [(p, why) for p in paths
                if not _ignored(p, globs) and (why := matches(p))]

    if as_json:
        print(json.dumps({
            "scanned": len(paths),
            "staged": staged,
            "findings": [{"path": p, "why": w} for p, w in findings],
        }, indent=2))
        return 0 if (warn or not findings) else 1

    if findings:
        for p, why in findings:
            print(f"✗ {p} — tracked, but must not be published: {why}")
        print()
        print("These files are machine-local by nature. Untrack, keep the")
        print("file, and ignore it so it stays out of future commits:")
        print(f"  git rm --cached {findings[0][0]}")
        print(f"  echo '{findings[0][0]}' >> .gitignore")
        print()
        print("Already-pushed history cannot be unpublished — untracking stops")
        print("the next commit, it does not recall the last one. A deliberate")
        print(f"exception: add a glob to {IGNORE_FILE} (no line marker exists,")
        print("on purpose — a reason written inside an unpublishable file is")
        print("an exemption nobody reviewing the tree would ever see).")
        if warn:
            print()
            print("  (--warn: advisory only — not blocking this build.)")
    else:
        where = "staged path(s)" if staged else "tracked path(s)"
        print(f"✓ publishscan clean — {len(paths)} {where}, none in the "
              "never-publish class.")
    return 0 if (warn or not findings) else 1


def selftest() -> int:
    """Prove the tool against its own fixtures — red, green and hatch legs."""
    red = [".claude/settings.json", ".claude/settings.local.json",
           ".mcp.json", ".env", ".env.production", "sub/.env", ".envrc",
           ".npmrc", ".vscode/settings.json", ".idea/workspace.xml"]
    green = [
        # The self-describing guard files this tool deliberately allows: they
        # MUST travel for the floor to run, and hiding them would weaken the
        # repo while looking like a fix.
        ".atelier-floor.json", ".leakscanignore", ".secretscanignore",
        ".gitignore", ".githooks/pre-commit", ".github/workflows/floor.yml",
        # Ordinary content that merely looks adjacent.
        "docs/method/REVIEW.md", "tools/floor.py", "src/env.py",
        "docs/build/templates/claude/settings.json",  # a TEMPLATE, not live
    ]
    bad_red = [p for p in red if matches(p) is None]
    bad_green = [p for p in green if matches(p) is not None]
    hatch_ok = _ignored(".mcp.json", [".mcp.json"])
    ok = not bad_red and not bad_green and hatch_ok
    print("publishscan selftest:", "OK" if ok else "FAILED")
    if not ok:
        print("  missed (should red):", bad_red)
        print("  false positives (should pass):", bad_green)
        print("  ignore-file hatch works:", hatch_ok)
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="check no never-publish path is tracked by git")
    ap.add_argument("paths", nargs="*",
                    help="accepted and ignored — this scanner's unit is the "
                         "repo's tracked set, not a path list (kept for "
                         "registry-template compatibility)")
    ap.add_argument("--root", default=".", help="repo root (default: .)")
    ap.add_argument("--staged", action="store_true",
                    help="judge only what this commit adds (the hook plane)")
    ap.add_argument("--warn", action="store_true",
                    help="advisory: report findings, never block")
    ap.add_argument("--json", action="store_true", help="machine-readable")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the tool against its own fixtures, then exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"publishscan: --root {args.root} is not a directory",
              file=sys.stderr)
        return 2
    return run(root, args.staged, args.warn, args.json)


if __name__ == "__main__":
    sys.exit(main())
