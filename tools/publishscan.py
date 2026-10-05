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
  good. Before a flip, `--history` (below) shows what history would publish.
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
heading. Every pattern matches AT ANY DEPTH — these files are machine-local
wherever they sit, and a monorepo's `packages/api/.npmrc` is the same finding
as a root `.npmrc` (PB1, the 2026-08-02 cold pass: the first cut matched most
entries at the repo root only, because `fnmatch` globs are not path-aware).
Two tiers, both stated rather than blurred:

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

  * ROUND 2: the 2026-10-03 survey of the estate's tracked files. It found a
    few shapes tracked that nobody would publish deliberately: runtime logs
    (`*.log`), local databases (`*.db`) and compiled-Python caches. Those
    carry a "measured" note. The survey's secret-carrier finds are recorded
    here as standard practice and nothing more, because a public file must
    not describe a private repo's security posture, even unnamed. The rest
    of round 2 (key and keystore shapes, history files, dumps and captures,
    tool caches, OS cruft) is standard practice too, and each entry in
    NEVER_PUBLISH says which tier it is. Considered and left out: generic
    `*.pem`, `credentials*.json`, `*.rsc`, archives, `*.jsonl`, `*.pub`.

  * ROUND 3: `*.egg-info/`, the one shape the 2026-10-05 harvest of a flip's
    transcripts found (260/090): a committed Python build directory, removed
    later, so it lived in history only.

HISTORY MODE (`--history`, opt-in, for the pre-flip gate)
---------------------------------------------------------
The default planes read the current tree, but a private-to-public flip
publishes every path ever tracked on a pushed ref. `--history` applies the
same rules and the same ignore file to every path ADDED in any commit
reachable from a branch, tag or remote-tracking ref, and reports each hit with
the oldest commit that added it and whether the tip still tracks it.

  * The source is `git log --branches --tags --remotes --no-renames
    --diff-filter=A --diff-merges=first-parent --name-only -z`. Not
    `git rev-list --objects --all`: that walks BLOBS, prints one name per
    blob and so drops every other path holding the same bytes (an empty
    `.env` shares its blob with every empty file), and it cannot say which
    commit added a path. `--no-renames` makes a rename an add of the new name;
    first-parent merge diffs catch a path a merge itself introduced.
  * Refs, not `--all`: the stash and other local-only refs are never pushed,
    so they are not what a flip publishes. The clone's remote-tracking refs
    are only as fresh as its last fetch; fetch first.
  * A shallow clone is a broken scan (exit 2): the history it lacks is the
    history the flip publishes.
  * Bounded memory: git's output is streamed in chunks, and only the hits
    (path, oldest adding commit) are held. Memory grows with the findings,
    never with the length of the history.

HATCHES
-------
A glob in `.publishscanignore` exempts a path, and every glob line MUST carry
a trailing `# reason` — a bare glob is a config error (exit 2), because the
accepted-exposure story above rests on every exemption stating its reason
where a reviewer reads it (PB2: the first cut claimed that requirement
without enforcing it). There is deliberately NO
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
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report  # noqa: E402

IGNORE_FILE = ".publishscanignore"
# C0 controls plus DEL — stripped from everything this tool ingests, at the
# ingest seam. See `_strip_controls`.
CONTROL_CHARS_RE = re.compile(r"[\x00-\x1f\x7f]")

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
    (".envrc", "direnv environment — machine-local by definition"),
    (".netrc", "credential-bearing tool config"),
    (".npmrc", "credential-bearing tool config (auth tokens)"),
    (".pypirc", "credential-bearing tool config (upload tokens)"),
    (".vscode/settings.json", "editor-local config: local paths, tool config"),
    (".idea/*", "editor-local config: local paths, tool config"),

    # ---- Round 2 (2026-10-03 survey of every sibling repo's tracked set). ----
    # Provenance: "measured" = tracked in at least one repo of this estate at
    # survey time (counts only here; the survey names no repo); "standard
    # practice" = a file whose whole purpose is machine-local state or a secret
    # carrier, not yet seen tracked here. Deliberately NOT added, with reasons:
    # generic `*.pem` (public certificates and CA roots are legitimately
    # tracked; measured 3 repos, most of them public chains), `credentials*.json`
    # (a deliberate no-secret registry and test fixtures wear that name),
    # `*.rsc` RouterOS (the same extension is source code and device exports),
    # generic archives and `*.jsonl` (fixtures and shipped data), `*.pub` (public
    # keys), `.vscode/extensions.json` and `.editorconfig` (deliberate shared
    # editor policy). `.vscode/launch.json` is left to a later round.
    # -- keys and secret carriers
    ("privkey*.pem",
     "a private key (Let's Encrypt style name) — standard practice"),
    ("*.key", "a private key file — standard practice"),
    ("*.p12", "a private-key bundle — standard practice"),
    ("*.pfx", "a private-key bundle — standard practice"),
    ("*.ppk", "a PuTTY private key — standard practice"),
    ("*.jks", "a Java keystore — standard practice"),
    ("*.keystore", "a Java keystore — standard practice"),
    ("*.kdbx", "a password database — standard practice"),
    ("id_rsa", "an SSH private key — standard practice"),
    ("id_dsa", "an SSH private key — standard practice"),
    ("id_ecdsa", "an SSH private key — standard practice"),
    ("id_ed25519", "an SSH private key — standard practice"),
    ("*.google_authenticator",
     "a TOTP seed file (the second factor itself) — standard practice"),
    (".htpasswd", "a web-server password file — standard practice"),
    (".git-credentials", "stored git credentials — standard practice"),
    (".aws/credentials", "cloud credentials — standard practice"),
    (".kube/config", "cluster endpoints and credentials — standard practice"),
    (".docker/config.json",
     "registry auth — standard practice"),
    ("*.tfstate", "infrastructure state, holds secrets — standard practice"),
    ("*.tfstate.backup",
     "infrastructure state, holds secrets — standard practice"),
    ("*.tfvars", "infrastructure variables, often secrets — standard "
                 "practice"),
    (".terraform/*", "provider cache and local state — standard practice"),
    ("known_hosts", "the hosts one machine has connected to — standard "
                    "practice"),
    # -- machine-local state: history, databases, logs, dumps, captures
    (".*_history", "shell or REPL history — standard practice"),
    (".lesshst", "pager history — standard practice"),
    (".viminfo", "editor history — standard practice"),
    ("*.db",
     "a local database — measured in the 2026-10-03 survey"),
    ("*.sqlite", "a local database — standard practice"),
    ("*.sqlite3", "a local database — standard practice"),
    ("*.db-wal", "a local database's write-ahead log — standard practice"),
    ("*.db-shm", "a local database's shared memory — standard practice"),
    ("*.log",
     "a runtime log — measured: 1 repo, 6 files, 2026-10-03 survey"),
    ("*.dmp", "a crash dump — standard practice"),
    ("*.mdmp", "a crash dump — standard practice"),
    ("*.hprof", "a heap dump — standard practice"),
    ("*.stackdump", "a crash dump — standard practice"),
    ("*.pcap", "a packet capture — standard practice"),
    ("*.pcapng", "a packet capture — standard practice"),
    ("*.har", "a browser capture, holds cookies — standard practice"),
    # -- tool state and caches
    ("__pycache__/*",
     "compiled-Python cache — measured: 1 repo, 1 file, 2026-10-03 survey"),
    # Round 3 (260/110): the one shape the 2026-10-05 flip-transcript harvest
    # (260/090) found that nobody would publish. A committed Python build
    # directory, later removed; it restates the package's author metadata.
    # Tracked at the tip of 0 sibling repos when added (2026-10-05), so it
    # turned no repo red; it matters to `--history`.
    ("*.egg-info/*",
     "a Python build directory, regenerated by install, restates package "
     "metadata — measured: 1 repo's history, 2026-10-05 harvest"),
    ("*.pyc", "compiled-Python cache — measured with __pycache__ above"),
    (".pytest_cache/*", "tool cache — standard practice"),
    (".mypy_cache/*", "tool cache — standard practice"),
    (".ruff_cache/*", "tool cache — standard practice"),
    ("node_modules/*", "installed dependencies — standard practice"),
    ("xcuserdata/*", "per-user Xcode state — standard practice"),
    ("*.xcuserstate", "per-user Xcode state — standard practice"),
    ("*.iml", "editor-local project file — standard practice"),
    ("*.swp", "editor swap file — standard practice"),
    ("*.swo", "editor swap file — standard practice"),
    ("*.sublime-workspace",
     "editor-local workspace state — standard practice"),
    ("CLAUDE.local.md",
     "one person's agent instructions — machine-local by name, same class as "
     ".claude/settings.local.json"),
    (".claude/worktrees/*",
     "an agent session's nested worktree — local scratch, never repo content"),
    # -- OS cruft
    (".DS_Store", "macOS folder metadata — standard practice"),
    ("Thumbs.db", "Windows thumbnail cache — standard practice"),
    ("desktop.ini", "Windows folder metadata — standard practice"),
    ("._*", "macOS AppleDouble metadata — standard practice"),
)


class BadIgnoreFile(Exception):
    """A glob line without a trailing `# reason` — a config error, not a pass."""


def _strip_controls(text: str) -> str:
    """Drop C0 control characters (and DEL) from text this tool ingests.

    Both of this scanner's output surfaces echo strings it did not write. The
    `BadIgnoreFile` message embeds the offending glob verbatim, and a finding
    line prints the tracked path — so a hostile or careless child could put
    ANSI escape sequences in a `.publishscanignore` glob or a filename and
    repaint an operator's terminal, up to painting a clean-scan line over a
    red one. Stripping at the seam where the text ENTERS closes both surfaces
    at once, rather than at each of the six print sites that echo it (C1 cold
    pass, C1F3, ruled STRIP C0 CONTROLS AT PARSE 2026-07-28; widened to this
    tool by the PA4 ruling 2026-08-03, so one change closes the class
    everywhere).

    Same rule, same spelling as `floor.py`'s `_strip_controls`: dropped, not
    escaped. None of these characters belongs in a path or a glob, so nothing
    is lost — and a stripped path cannot match a never-publish pattern that
    the unstripped one missed, since the patterns hold no controls either."""
    return CONTROL_CHARS_RE.sub("", text)


def load_ignores(root: Path) -> list[str]:
    """Globs from .publishscanignore — blank lines and `#` comments skipped.

    Every glob line must carry a trailing `# reason` on the SAME line: the
    accepted-exposure mitigation is that a reviewer reading the tree sees why
    each exemption exists, and a comment on a neighbouring line does not bind
    to the glob it happens to sit near. A bare glob raises (exit 2 upstream).
    """
    f = root / IGNORE_FILE
    if not f.is_file():
        return []
    out = []
    for n, raw in enumerate(
            f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        # The ingest seam for this file: everything downstream — the glob that
        # is matched, and the glob echoed back in an error — is control-free
        # from here on (C1F3/PA4).
        line = _strip_controls(raw).strip()
        if not line or line.startswith("#"):
            continue
        idx = line.find("#")
        if idx == -1:
            raise BadIgnoreFile(
                f"{IGNORE_FILE}:{n}: '{line}' has no trailing '# reason' — "
                "every exemption states its reason where a reviewer reads it")
        if not line[idx - 1].isspace():
            # A '#' with no space before it would silently truncate the glob
            # into an exemption for a DIFFERENT path than written (PA3, ruled
            # 2026-08-03). A glob cannot contain '#'; the failure is loud.
            raise BadIgnoreFile(
                f"{IGNORE_FILE}:{n}: put a space before '# reason' — a glob "
                "may not contain '#', and a '#' glued to the glob would "
                "silently exempt a different path than written")
        glob = line[:idx].strip()
        reason = line[idx + 1:].strip()
        if not reason:
            raise BadIgnoreFile(
                f"{IGNORE_FILE}:{n}: '{glob}' has no trailing '# reason' — "
                "every exemption states its reason where a reviewer reads it")
        out.append(glob)
    return out


def _ignored(path: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, g) for g in globs)


def matches(path: str) -> str | None:
    """The reason this path must not be tracked, or None.

    Each pattern is tried at the repo root AND at any depth (`*/` + glob —
    `fnmatch`'s `*` spans `/`, which is also why the depth form needs no
    `**`). A machine-local file is machine-local wherever it sits.
    """
    for glob, why in NEVER_PUBLISH:
        if fnmatch.fnmatch(path, glob) or fnmatch.fnmatch(path, "*/" + glob):
            return why
    return None


class NotARepo(Exception):
    """The tree is not under git at all — a complete scan of an empty set."""


def _git(root: Path, *args: str) -> list[str]:
    r = subprocess.run(["git", "-C", str(root), *args],
                       capture_output=True, text=True)
    if r.returncode != 0:
        err = _strip_controls(r.stderr).strip()
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
    # The other ingest seam: a tracked path is printed in every finding line
    # and in the two remediation commands below it. git quotes most exotic
    # bytes on its own, but that is git's default and not this tool's
    # guarantee, so the guarantee is made here (C1F3/PA4).
    return [stripped for ln in r.stdout.splitlines()
            if (stripped := _strip_controls(ln))]


def repo_top(root: Path) -> Path:
    """The repo's top level. A --root inside the repo rebases to it: this
    scanner's unit is the repo's tracked set, and a silent subtree scan
    would report 'N tracked path(s)' while root-anchored patterns matched
    nothing (PB3)."""
    return Path(_git(root, "rev-parse", "--show-toplevel")[0])


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
    rebased = False
    try:
        top = repo_top(root)
        if top.resolve() != root.resolve():
            rebased = True
            # Stderr, not stdout: --json consumers parse stdout, and a prose
            # line before the document breaks them (PA1, ruled 2026-08-03).
            print(f"publishscan: --root is inside the repo — scanning the "
                  f"full tracked set from {top}", file=sys.stderr)
        paths = tracked_paths(top, staged)
        globs = load_ignores(top)
    except NotARepo:
        if as_json:
            print(json.dumps({"scanned": 0, "staged": staged,
                              "findings": [], "skipped": "not a git repo"},
                             indent=2))
        else:
            print("✓ publishscan — not a git repository, so nothing is "
                  "tracked and nothing can be published from here.")
        return 0
    except BadIgnoreFile as e:
        return report.broken("publishscan", str(e))
    except RuntimeError as e:
        return report.broken("publishscan", str(e))
    findings = [(p, why) for p in paths
                if not _ignored(p, globs) and (why := matches(p))]

    if as_json:
        # rebased_to is always present (null when --root was already the top)
        # so the field set stays comparable run to run.
        print(json.dumps({
            "scanned": len(paths),
            "staged": staged,
            "rebased_to": str(top) if rebased else None,
            "findings": [{"path": p, "why": w} for p, w in findings],
        }, indent=2))
        return report.exit_code(len(findings), warn=warn)

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
        print(f"exception: add a glob to {IGNORE_FILE} with a trailing")
        print(f"'# reason' on the same line (e.g. `{findings[0][0]}  # kept:")
        print("<why>`) — a bare glob is a config error, and no line marker")
        print("exists on purpose: a reason written inside an unpublishable")
        print("file is an exemption nobody reviewing the tree would see).")
        if warn:
            print(report.WARN_NOTICE)
    else:
        where = "staged path(s)" if staged else "tracked path(s)"
        print(report.clean_head(
            "publishscan", f"{len(paths)} {where}, none in the never-publish class."))
    return report.exit_code(len(findings), warn=warn)


# The history plane's git invocation (see HISTORY MODE in the docstring for
# why each flag is here). `%x01` marks a commit header, a byte no path the
# tool reports can carry once controls are stripped.
HISTORY_LOG = ("log", "--branches", "--tags", "--remotes", "--no-renames",
               "--diff-filter=A", "--diff-merges=first-parent", "--name-only",
               "-z", "--format=%x01%H %ct")
HISTORY_CHUNK = 64 * 1024


def _nul_tokens(stream, chunk: int = HISTORY_CHUNK):
    """Yield NUL-terminated tokens from a binary stream, one chunk at a time,
    so the size of git's output never sets the size of this process."""
    rest = b""
    while True:
        block = stream.read(chunk)
        if not block:
            break
        parts = (rest + block).split(b"\0")
        rest = parts.pop()
        yield from parts
    if rest:
        yield rest


def _git_stream(root: Path, *args: str):
    """Run git with stdout streamed; a non-zero exit raises after the stream
    is drained, so a scan git broke halfway is never read as complete."""
    proc = subprocess.Popen(["git", "-C", str(root), *args],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        yield from _nul_tokens(proc.stdout)
    finally:
        proc.stdout.close()
        err = proc.stderr.read().decode("utf-8", "replace")
        proc.stderr.close()
        code = proc.wait()
    if code != 0:
        raise RuntimeError(_strip_controls(err).strip() or "git failed")


def _decode(raw: bytes) -> str:
    return _strip_controls(raw.decode("utf-8", errors="replace"))


def history_findings(top: Path, globs: list[str]
                     ) -> tuple[int, int, dict[str, tuple[str, int, str]]]:
    """(path additions examined, commits with an addition, hits).

    hits maps path -> (oldest adding commit, its committer time, why). Only
    hits are held; every other path is counted and dropped."""
    additions = commits = 0
    hits: dict[str, tuple[str, int, str]] = {}
    sha, when, first = "", 0, False
    for tok in _git_stream(top, *HISTORY_LOG):
        if tok.startswith(b"\x01"):
            head = tok[1:].decode("ascii", "replace").split()
            sha, when, first = head[0], int(head[1]), True
            commits += 1
            continue
        if first:
            # git separates a commit's header from its names with one newline.
            tok, first = tok[1:] if tok.startswith(b"\n") else tok, False
        if not tok:
            continue
        additions += 1
        path = _decode(tok)
        if _ignored(path, globs):
            continue
        why = matches(path)
        if why is None:
            continue
        # The log runs newest-first, so a later-seen add of the same path is
        # older; committer time settles merge-order ties the walk leaves.
        prev = hits.get(path)
        if prev is None or when <= prev[1]:
            hits[path] = (sha, when, why)
    return additions, commits, hits


def _still_tracked(top: Path, hits: dict) -> set[str]:
    """Which hits the tip still tracks — streamed `ls-files -z`, so the
    membership test costs the hits, not the tracked set."""
    return {p for tok in _git_stream(top, "ls-files", "-z")
            if (p := _decode(tok)) in hits}


def _utc_day(ts: int) -> str:
    from datetime import datetime, timezone
    return datetime.fromtimestamp(ts, timezone.utc).date().isoformat()


def run_history(root: Path, warn: bool, as_json: bool) -> int:
    rebased = False
    try:
        top = repo_top(root)
        if top.resolve() != root.resolve():
            rebased = True
            print(f"publishscan: --root is inside the repo — scanning the "
                  f"full history from {top}", file=sys.stderr)
        globs = load_ignores(top)
        if _git(top, "rev-parse", "--is-shallow-repository") == ["true"]:
            return report.broken(
                "publishscan", "--history on a shallow clone — the missing "
                "history is what a flip publishes; `git fetch --unshallow`")
        if _git(top, "for-each-ref", "--count=1",
                "refs/heads", "refs/tags", "refs/remotes"):
            additions, commits, hits = history_findings(top, globs)
            tracked = _still_tracked(top, hits)
        else:
            additions, commits, hits, tracked = 0, 0, {}, set()
    except NotARepo:
        if as_json:
            print(json.dumps({"scanned": 0, "history": True, "commits": 0,
                              "findings": [], "skipped": "not a git repo"},
                             indent=2))
        else:
            print("✓ publishscan — not a git repository, so there is no "
                  "history to publish from here.")
        return 0
    except (BadIgnoreFile, RuntimeError) as e:
        return report.broken("publishscan", str(e))

    findings = sorted(hits.items())
    if as_json:
        print(json.dumps({
            "scanned": additions,
            "history": True,
            "commits": commits,
            "rebased_to": str(top) if rebased else None,
            "findings": [{"path": p, "why": why, "first_commit": sha,
                          "first_date": _utc_day(when),
                          "tracked_at_tip": p in tracked}
                         for p, (sha, when, why) in findings],
        }, indent=2))
        return report.exit_code(len(findings), warn=warn)

    if findings:
        for p, (sha, when, why) in findings:
            where = "still tracked" if p in tracked else "history only"
            print(f"✗ {p} — first added {sha[:12]} ({_utc_day(when)}), "
                  f"{where}: {why}")
        print()
        print("A flip publishes every path ever pushed, not only the tip.")
        print("'still tracked' paths: untrack them as the default scan says.")
        print("'history only' paths: untracking cannot recall them. Removing")
        print("them means rewriting history or publishing a fresh history,")
        print("and that is the owner's call, made before the flip.")
        print(f"A deliberate exception: a glob in {IGNORE_FILE} with a")
        print("trailing '# reason', exactly as for the default scan.")
        if warn:
            print(report.WARN_NOTICE)
    else:
        print(report.clean_head(
            "publishscan", f"{additions} path addition(s) across {commits} "
                           "commit(s) of history, none in the never-publish "
                           "class."))
    return report.exit_code(len(findings), warn=warn)


def selftest() -> int:
    """Prove the tool against its own fixtures — red, green and hatch legs."""
    red = [".claude/settings.json", ".claude/settings.local.json",
           ".mcp.json", ".env", ".env.production", "sub/.env", ".envrc",
           ".npmrc", ".vscode/settings.json", ".idea/workspace.xml",
           # Any depth — the PB1 probes that passed green in the first cut.
           "packages/api/.npmrc", "sub/.env.production", "docs/.envrc",
           "services/x/.claude/settings.json", "sub/.mcp.json",
           "apps/web/.vscode/settings.json", "x/.idea/workspace.xml",
           # Round 2.
           "pki/privkey.pem", "a/archive/privkey1.pem", "certs/server.key",
           "home/.ssh/id_ed25519", "u/user.google_authenticator",
           "log/access.log", "x/__pycache__/m.cpython-314.pyc", "data/app.db",
           ".DS_Store", "docs/.DS_Store", "docs/._notes.md",
           "h/.bash_history", "CLAUDE.local.md", "infra/terraform.tfstate",
           ".claude/worktrees/agent-1",
           # Round 3.
           "src/pkg.egg-info/PKG-INFO", "pkg.egg-info/SOURCES.txt"]
    green = [
        # The self-describing guard files this tool deliberately allows: they
        # MUST travel for the floor to run, and hiding them would weaken the
        # repo while looking like a fix.
        ".atelier-floor.json", ".leakscanignore", ".secretscanignore",
        ".gitignore", ".githooks/pre-commit", ".github/workflows/floor.yml",
        # Ordinary content that merely looks adjacent.
        "docs/method/REVIEW.md", "tools/floor.py", "src/env.py",
        "docs/build/templates/claude/settings.json",  # a TEMPLATE, not live
        # Round 2 look-alikes that are legitimately tracked.
        "pki/fullchain.pem", "etc/pki/ca-root.pem", "keys/id_rsa.pub",
        ".vscode/extensions.json", ".editorconfig", "docs/changelog.md",
        "src/core.2fa.py", "docs/release_history.md", "registry/credentials.json",
        "docs/egg-info-notes.md", "src/egg_info.py",
    ]
    bad_red = [p for p in red if matches(p) is None]
    bad_green = [p for p in green if matches(p) is not None]
    hatch_ok = _ignored(".mcp.json", [".mcp.json"])
    # Nothing this tool ingests can repaint the terminal it reports to
    # (C1F3/PA4). Checked here too: the selftest is what a child runs offline.
    controls_ok = _strip_controls("\x1b[2K.mcp\x07.json\x7f") == "[2K.mcp.json"
    ok = not bad_red and not bad_green and hatch_ok and controls_ok
    print("publishscan selftest:", "OK" if ok else "FAILED")
    if not ok:
        print("  missed (should red):", bad_red)
        print("  false positives (should pass):", bad_green)
        print("  ignore-file hatch works:", hatch_ok)
        print("  control characters stripped:", controls_ok)
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
    ap.add_argument("--history", action="store_true",
                    help="judge every path ever added on a branch, tag or "
                         "remote-tracking ref (the pre-flip gate); opt-in")
    ap.add_argument("--warn", action="store_true",
                    help="advisory: report findings, never block")
    ap.add_argument("--json", action="store_true", help="machine-readable")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the tool against its own fixtures, then exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    if args.history and args.staged:
        return report.broken("publishscan", "--history and --staged are two "
                             "different planes; pick one")
    root = Path(args.root).resolve()
    if not root.is_dir():
        return report.broken("publishscan", f"--root {args.root} is not a directory")
    if args.history:
        return run_history(root, args.warn, args.json)
    return run(root, args.staged, args.warn, args.json)


if __name__ == "__main__":
    sys.exit(main())
