"""The single-sourced exit-code contract and common report lines shared by the
floor scanners (`115/080`, part 3).

Before this module every scanner spelled its own copy of the same contract:

  * the exit codes — 0 nothing blocking, 1 blocking findings, 2 the scan
    itself is broken (a broken scan is not a pass);
  * the `main()` wrapper that turns a config error (an unreasoned ignore
    glob, an unusable declaration) into one stderr line and exit 2 — eleven
    textually identical copies;
  * the exit-2 stderr lines for a missing root, a missing path, an unreadable
    file, a failed `git diff` and an absolute `--staged` path;
  * the rule-(b) tally line (`  suppressed: a · b · c`, its allow-marker
    breakdown and its disabled-rules line), the finding-cap part and the
    over-cap list line;
  * the `(--warn: advisory only …)` notice that `floor.py` names as the
    estate-wide spelling.

It also holds one thing no scanner printed before: the namespaced finding ID
(`finding_id`, `with_id`, `finding_dicts`), `<scanner>:<kind>` at the end of
each finding line and as an `id` in `--json`, whose kind is the scope the
scanner's own allow-marker accepts (the second half of `115/080` part 3).

And one thing that is not output at all: the readers of git's path output
(`nul_paths`, `diff_header_path`, `unquote_c`, at the foot of the file), so that
no guard parses a C-quoted path as though it were a bare one (`115/260`), and
the one reader of the staged diff (`staged_added`, also at the foot), so that
no guard takes an added line for a file header (`115/280`).

LINES STILL SPELT PRIVATELY, AND WHY (RT6, `160/730`; each is a line a future
shared edit will miss, so they are listed here rather than left to be found):
`licenscan`'s missing-root line (`not a directory: <root>`), `publishscan`'s and
`reviewscan`'s (`--root <raw> is not a directory`), `reviewscan`'s per-path
refusal, and `stampscan`'s `--warn` notice (`drift not blocking this build`, not
`WARN_NOTICE`). Each is pinned byte for byte in `test_report.py`, the converted
scanners' output is a contract with every child, and folding a line means
changing its bytes, which this consolidation does not do. `pointerscan.py` and
`board.py` stay unconverted (README says so). The advisory-count line WAS folded
(`advisory_count_line`), because `floor.py` parses it and a copy that drifts
breaks that read.

WHAT THIS MODULE DELIBERATELY DOES NOT DO: unify behaviour or wording. Every
difference between the scanners is a PARAMETER here — the scanner's name, the
tally's parts, the finding noun, a head line's tail, the over-cap indent, the
example path in the `--staged` refusal, which exception classes count as
config errors — never a default a scanner can drift into. A scanner whose line
genuinely differs (leakscan's clean head, indexscan's over-cap line, the `⚠`
heads of the advisory-by-construction checks) keeps its own spelling.

`tools/test_report.py` tests each helper against literal strings, and pins the
lines each converted scanner prints, so a shared edit that changes any one
scanner's output fails loudly.

What the scanners print is a contract with every child: they run atelier's
floor at `main`, so a change to a string here reaches every child's CI at its
next run.
"""

from __future__ import annotations

import io
import os
import posixpath
import re
import subprocess
import sys
import traceback
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from dataclasses import asdict
from pathlib import Path
from typing import Callable, Iterable, Iterator, Sequence

# The house exit-code contract.
EXIT_CLEAN = 0      # nothing blocking (clean, advisory-only, or --warn)
EXIT_FINDINGS = 1   # blocking findings
EXIT_BROKEN = 2     # the scan itself is broken — never read as a pass

# Printed after the report when findings exist under --warn. `floor.py`'s
# `WARN_MODE_FLAGS` comment names this as the estate-wide spelling.
WARN_NOTICE = "\n  (--warn: advisory only — not blocking this build.)"


def exit_code(blocking: "int | bool", *, warn: bool = False) -> int:
    """0 or 1 from the truthiness of `blocking` (a count or a bool); always 0
    under `warn`. Exit 2 is never computed here - it is returned by `broken` at
    the point the scan finds it cannot be trusted.

    Typed `int | bool` on purpose (RT8, `160/730`): an object whose truthiness
    is not a finding count (a generator is always true, an empty-but-truthy
    tally object too) must not decide the exit code. Every caller passes an
    `int` or a `bool`."""
    if warn:
        return EXIT_CLEAN
    return EXIT_FINDINGS if blocking else EXIT_CLEAN


# RT3 (`160/730`): a message reaches the committer's terminal and the CI log,
# and carries text from a path or an ignore-file glob that a pull request can
# land. C0 controls (newline kept: some messages are deliberately multi-line),
# DEL, C1 controls and the bidi override/isolate controls are dropped, so an
# escape sequence cannot clear a screen or reorder what the reader sees.
_MESSAGE_CONTROL_RX = re.compile(
    "[\x00-\x09\x0b-\x1f\x7f-\x9f\u202a-\u202e\u2066-\u2069]")


def broken(name: str, message: str) -> int:
    """Print `<name>: <message>` to stderr and return exit 2. Control
    characters in `message` are stripped first (RT3)."""
    print(f"{name}: {_MESSAGE_CONTROL_RX.sub('', message)}", file=sys.stderr)
    return EXIT_BROKEN


def guarded_main(name: str, run: Callable[[list[str] | None], int],
                 argv: list[str] | None,
                 config_errors: tuple[type[BaseException], ...]) -> int:
    """Run a scanner's `_main`, turning any of `config_errors` into exit 2.
    An unexplained exemption or an unusable declaration makes the scan's own
    scope untrustworthy, so it is a broken scan, not a pass.

    A file the scan could not read, escaping every guard's own handler, is the
    shared `cannot read` line and exit 2 (RT4a).

    Any OTHER exception is a broken scan too (RT4, `160/730`): the traceback is
    printed in full, so nothing is swallowed, and the exit code is 2, not
    Python's 1 - which is the code for "blocking findings" and misreported a
    crash as one. `SystemExit` (argparse's usage errors) and
    `KeyboardInterrupt` are not `Exception`s and pass through untouched."""
    try:
        return run(argv)
    except config_errors as e:
        return broken(name, str(e))
    except OSError as e:
        # A read that no guard caught (an unreadable ignore file, a file the
        # scan could not open) is the contract's own "cannot read" line, exit
        # 2, not a traceback (RT4a, 160/730). An OSError that names no file
        # is not that line and falls through to the traceback.
        if e.filename is not None:
            return cannot_read(name, e)
        traceback.print_exc()
        print(f"{name}: internal error - the scan did not complete "
              "(a broken scan is not a pass)", file=sys.stderr)
        return EXIT_BROKEN
    except Exception:
        traceback.print_exc()
        print(f"{name}: internal error - the scan did not complete "
              "(a broken scan is not a pass)", file=sys.stderr)
        return EXIT_BROKEN


def is_vanished(e: OSError) -> bool:
    """True for the one read failure a scan may skip without saying so: the
    file went away between the walk listing it and the scan opening it (a race
    with another process). Anything else - a permission error, an I/O error -
    is a file the scan could not read, and a broken scan is not a pass
    (RT1, `160/730`)."""
    return isinstance(e, (FileNotFoundError, NotADirectoryError,
                          IsADirectoryError))


def resolve_targets(root: Path, paths: Iterable[str]) -> list[Path]:
    """Each path as given if absolute, else under `root` — never the caller's
    cwd: mixing the two reads one repo's file under another repo's rules
    (roadmap 010/110)."""
    return [(root / p) if not Path(p).is_absolute() else Path(p) for p in paths]


def refuse_escaping_targets(name: str, root: Path,
                            paths: Iterable[str]) -> int | None:
    """Exit 2 if a RELATIVE target climbs out of `root`, else None (RT7,
    `160/730`). `resolve_targets` promises "never the caller's cwd"; nothing
    promised "never outside the root", and a `../x` target was scanned under
    the ignore file and anchors of a root they were not written for. An
    absolute target is the caller's explicit choice and is left alone. The
    check is lexical (`normpath`), so a symlink inside the root is not
    refused."""
    rootp = os.path.normpath(str(root))
    escaping = []
    for p in paths:
        if Path(p).is_absolute():
            continue
        full = os.path.normpath(os.path.join(rootp, p))
        if full != rootp and not full.startswith(rootp.rstrip(os.sep) + os.sep):
            escaping.append(p)
    if escaping:
        return broken(
            name,
            f"path(s) climb out of --root: {', '.join(escaping)}\n"
            "  A relative path is read under --root, with that root's ignore "
            "file and anchors, so one that leaves it\n"
            "  would be scanned under rules written for another tree. Give "
            "an absolute path, or run with the right --root.")
    return None


def refuse_missing_root(name: str, root: Path, raw: str) -> int | None:
    """Exit 2 (after one stderr line) if `root` is not a directory, else None."""
    if not root.is_dir():
        return broken(name, f"root does not exist: {raw}")
    return None


def refuse_missing_paths(name: str, targets: Sequence[Path]) -> int | None:
    """Exit 2 if any target does not exist, else None: a typo'd path that
    scans nothing must never read as a clean pass."""
    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        return broken(name, f"path does not exist: {', '.join(missing)}")
    return None


def cannot_read(name: str, e: OSError) -> int:
    """Exit 2 for a file the scan could not open."""
    return broken(name, f"cannot read {e.filename}: {e.strerror}")


def quiet_selftest(name: str, fn: Callable[[], int]) -> int:
    """Run a scanner's `--selftest` body with its output CAPTURED, and print
    only the verdict (roadmap 320/690).

    A selftest proves the engine by running it against deliberate fixtures,
    and the engine's reports about those fixtures are, by design, findings:
    `✗ conflictscan: 7 finding(s) — commit blocked.` over `docs/broken.md`.
    Printed, they sit in a CI log in the floor's own shape, in the same stream
    and with the same glyph as a real finding, and a red run was once
    diagnosed from them (the report lying while the work was fine, `370`).
    So the passing run prints one line and nothing else. A FAILING run prints
    the verdict and then what it captured, each line prefixed
    `selftest (<name>):`, because the captured output is the evidence the
    failure needs, and the prefix and the red verdict say whose it is.

    `fn` returns the exit code (0 = the engine proved itself)."""
    buf = io.StringIO()

    def replay() -> None:
        for line in buf.getvalue().splitlines():
            print(f"selftest ({name}): {line}")

    try:
        with redirect_stdout(buf), redirect_stderr(buf):
            rc = fn()
    except BaseException:
        print(f"selftest FAILED — {name} raised")
        replay()
        raise
    if rc == 0:
        print(f"selftest OK — {name}")
    else:
        print(f"selftest FAILED — {name}")
        replay()
    return rc


def staged_added_by_path() -> dict[str, set[int]]:
    """Path -> the set of real new-file line numbers the staged diff adds,
    read by `staged_added` (so it shares that reader's refusals). The shape a
    scanner needs when it must read a staged file WHOLE, for context (is this
    line inside a fence?), and then report only on the lines a commit adds
    (roadmap 320/600)."""
    added: dict[str, set[int]] = {}
    for path, lineno, _text in staged_added():
        added.setdefault(path, set()).add(lineno)
    return added


def staged_paths() -> list[str]:
    """Every path the staged change adds, copies, modifies or renames to, with
    no regard to whether it adds a LINE (`git diff --cached --name-only -z`;
    the filter is `ACMR`, narrower than `STAGED_DIFF_CMD`'s). For a scanner
    that judges a whole file rather than a line (`reviewscan`, `sizescan`,
    roadmap 320/600): a deletion-only edit adds no line, yet it can make the
    whole file wrong (it removed the file's review line). Raises `subprocess.CalledProcessError`
    if git fails; callers catch `STAGED_DIFF_FAILURES`."""
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "-z", "--no-ext-diff",
         "--diff-filter=ACMR"], capture_output=True, check=True)
    return nul_paths(out.stdout)


@contextmanager
def staged_blob(path: str):
    """The INDEX copy of `path` (what the commit will hold, not the working
    tree's), as a binary stream git feeds incrementally, so a large staged file
    is never held whole in memory. Inherits the environment on purpose: a hook
    runs with `GIT_INDEX_FILE` set (a partial commit uses a temporary index),
    and the blob must come from the same index the diff was read from.

    Raises `subprocess.CalledProcessError` (a member of `STAGED_DIFF_FAILURES`)
    if git cannot produce the blob, so a missing or unreadable staged file is a
    broken scan (exit 2), never an empty and therefore clean one. The caller
    must read the stream to its end inside the `with`."""
    proc = subprocess.Popen(["git", "cat-file", "blob", f":0:{path}"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        yield proc.stdout
    finally:
        proc.stdout.close()
        err = proc.stderr.read()
        proc.stderr.close()
        rc = proc.wait()
    if rc != 0:
        raise subprocess.CalledProcessError(rc, proc.args, stderr=err)


def git_diff_failed(name: str, e: BaseException) -> int:
    """Exit 2 when the staged diff cannot be read. A diff the reader refuses
    (`DiffReadError`) also says what that means for the committer, because the
    bare "does not fit its hunk's counts" names no cause and no way forward
    (160/800 SX2)."""
    msg = f"git diff failed: {e}"
    if isinstance(e, DiffReadError):
        msg += ("\n  This is not a finding: the guard could not read the staged "
                "diff, so it refuses to guess.\n"
                "  The usual cause is a git setting or environment variable "
                "that changes how `git diff`\n"
                "  prints (diff.* config, GIT_DIFF_OPTS). The guard pins the "
                "ones it knows; see the raw\n"
                "  diff with: git diff --cached --unified=0 --no-ext-diff")
    return broken(name, msg)


def refuse_absolute_staged(name: str, paths: Iterable[str],
                           example: str) -> int | None:
    """Exit 2 if any `--staged` path is absolute, else None. git lists staged
    paths repo-relative, so an absolute one matches nothing, the filter
    empties, and a scan that covered nothing would exit 0."""
    absolute = [p for p in paths if Path(p).is_absolute()]
    if absolute:
        return broken(
            name,
            f"--staged needs repo-relative path(s), got absolute: "
            f"{', '.join(absolute)}\n"
            "  git lists staged paths relative to the repo root, so an "
            "absolute path matches nothing\n"
            "  and the scan would pass while covering nothing. Pass e.g. "
            f"'{example}' instead.")
    return None


# The pathspec magic that makes a positional mean exactly one thing to git:
# `top` anchors it at the repo root whatever the cwd (a subdirectory run reads
# the same scope as a root run), `literal` stops `*`, `?` and `[` from becoming
# globs. Environment switches that would change what these mean are dropped.
_LITERAL_TOP = ":(top,literal)"
_PATHSPEC_ENV_DROP = ("GIT_GLOB_PATHSPECS", "GIT_NOGLOB_PATHSPECS",
                      "GIT_ICASE_PATHSPECS")


def _git_scope_names(*cmd: str) -> set[str]:
    """The NUL-separated names a read-only git command lists, as a set.
    Raises `subprocess.CalledProcessError` if git fails."""
    env = {k: v for k, v in os.environ.items() if k not in _PATHSPEC_ENV_DROP}
    env["GIT_LITERAL_PATHSPECS"] = "0"
    return set(nul_paths(subprocess.run(
        ["git", "-c", "core.quotePath=false", *cmd],
        capture_output=True, check=True, env=env).stdout))


def resolve_staged_scope(name: str, paths: Iterable[str],
                         example: str) -> tuple[int | None, frozenset | None]:
    """Resolve the positional `paths` of a `--staged` scan; (rc, allowed).

    The one reader the three staged-diff guards share (roadmap 115/360). A
    positional is a repo-root-relative path in git's own spelling, and GIT
    decides what it names (`160/950` QS1/QS2): `git ls-files` for what the
    index holds (every staged addition, change and rename target) plus `git
    diff --cached --diff-filter=D` for what this commit removes, each given
    the positional as one literal root-anchored pathspec. A path is then in
    scope when git listed it. The comparison is against git's own output, so
    a case fold or a Unicode normalisation the filesystem forgives (`Docs`
    for `docs`, an NFD directory name for git's NFC) cannot decide whether
    the scan runs: git either resolves the spelling or the positional is
    refused here.

    `allowed` is None when nothing is restricted (no positional, or `.`, the
    repo root); otherwise the frozenset of in-scope paths. Spelling is
    normalised first with `posixpath.normpath` (git's paths are POSIX
    whatever the host): `./docs` and `docs//` mean `docs`.

    Refusals (rc 2), each a scope that would cover less than it names:
      * an absolute path (`refuse_absolute_staged`);
      * one that normalises to `..` or `../x`, outside the repo;
      * one that names nothing git knows, neither indexed nor removed by this
        commit: a typo, the wrong case, a glob, an unexpanded `~`, a
        directory the repo lacks. Tree mode already refuses the same typo
        (`refuse_missing_paths`) and the floor blocks a declared scope that
        resolves to nothing, so no floor invocation is turned away by this.
    NOT a refusal: a positional that names tracked paths none of which this
    commit stages. That is a commit outside the scope, a legitimate pass.
    """
    paths = list(paths)
    rc = refuse_absolute_staged(name, paths, example)
    if rc is not None:
        return rc, None
    norm = [posixpath.normpath(p) for p in paths]
    escaping = [p for p, n in zip(paths, norm)
                if n == ".." or n.startswith("../")]
    if escaping:
        return broken(
            name,
            f"--staged path(s) climb out of the repo with '..': "
            f"{', '.join(escaping)}\n"
            "  A staged path is read from the repo root, in git's spelling, "
            "so one that leaves the root names nothing git lists\n"
            "  and the scan would pass while covering nothing. Pass e.g. "
            f"'{example}' instead."), None
    if "." in norm or not norm:
        return None, None            # the repo root: no restriction
    allowed: set[str] = set()
    unknown: list[str] = []
    try:
        for p, n in zip(paths, norm):
            spec = _LITERAL_TOP + n
            found = _git_scope_names("ls-files", "-z", "--full-name",
                                     "--", spec)
            found |= _git_scope_names(
                "diff", "--cached", "--name-only", "-z", "--no-renames",
                "--no-ext-diff", "--diff-filter=D", "--", spec)
            if not found:
                unknown.append(p)
            allowed |= found
    except subprocess.CalledProcessError as e:
        return git_diff_failed(name, e), None
    if unknown:
        return broken(
            name,
            f"--staged path(s) name nothing git knows: {', '.join(unknown)}\n"
            "  git lists neither an indexed path nor a removal under it, so "
            "it can match no staged file\n"
            "  and the scan would pass while covering nothing. Spell it as "
            "git does: repo-root-relative, exact case, no glob or '~'.\n"
            f"  Pass e.g. '{example}' instead."), None
    return None, frozenset(allowed)


def restrict_to_scope(items: dict, allowed: frozenset | None) -> dict:
    """`items` (keyed by path) cut to the paths `allowed` lists; the whole of
    it when `allowed` is None (nothing restricted)."""
    if allowed is None:
        return items
    return {path: v for path, v in items.items() if path in allowed}


def scope_staged(name: str, staged: dict, paths: Iterable[str],
                 example: str) -> tuple[int | None, dict]:
    """Restrict the staged set to the positional `paths`; (rc, staged).
    `resolve_staged_scope` decides what the positionals name; this applies
    the answer to one path-keyed dict."""
    paths = list(paths)
    rc, allowed = resolve_staged_scope(name, paths, example)
    if rc is not None:
        return rc, staged
    kept = restrict_to_scope(staged, allowed)
    note_empty_scope(name, len(staged), len(kept), paths)
    return None, kept


def note_empty_scope(name: str, staged: int, in_scope: int,
                     paths: Iterable[str]) -> None:
    """Say, on stderr, when a positional scope left nothing to scan (RT2,
    `160/730`). A commit that touches only files outside the scope is a
    legitimate pass and stays one (exit code unchanged), but "clean" over zero
    files read is the same line as "clean" over a hundred; this is the line that
    tells them apart. Silent unless the scope was restricted, something was
    staged, and none of it was in scope."""
    paths = list(paths)
    if paths and staged and not in_scope:
        print(f"{name}: none of the {staged} staged file(s) is in the "
              f"--staged scope ({', '.join(paths)}): nothing was scanned",
              file=sys.stderr)


def refuse_other_repo(name: str, root: Path) -> int | None:
    """Exit 2 if the staged diff the process would read (git in the cwd) is not
    the repo `--root` names (`160/950` QS3). The staged readers run git in the
    cwd; `--root` otherwise only locates ignore files and manifests, so a cwd
    in a different repo read that repo's index under this repo's rules and
    printed clean. A cwd in a subdirectory of the same repo is fine: positionals
    are root-anchored and the diff paths are root-relative whatever the cwd."""
    def top(*pre: str) -> str | None:
        try:
            out = subprocess.run(
                ["git", *pre, "rev-parse", "--show-toplevel"],
                capture_output=True, check=True).stdout
        except (subprocess.CalledProcessError, OSError):
            return None
        return os.path.realpath(out.decode("utf-8", "surrogateescape").strip())

    here, there = top(), top("-C", str(root))
    if here is not None and here == there:
        return None
    return broken(
        name,
        "--staged reads the git index of the directory it is run in, and that "
        f"is not the repo --root names ({root}).\n"
        + ("  The current directory is not inside a git repo.\n"
           if here is None else
           f"  The current directory belongs to the repo at {here}.\n")
        + "  A scan of one repo's index under another's rules would pass "
        "while covering nothing. Run it from inside the repo, or drop --root.")


def advisory_count_line(name: str, n: int) -> str:
    """The one line that always says how many advisory findings this run made:
    `  <name> advisory: N finding(s) - reported, not blocking.`

    The single home of the wording `floor.py`'s `advisory_count_rx(name)` reads
    back off a scanner's output (RT6, `160/730`; it was built three times, in
    `secretscan`, `leakscan` and `licenscan`, and a drift between any copy and
    the pattern breaks the board's read silently).

    ALWAYS printed, zero included: a line printed only when non-zero makes "no
    line" mean two things, nothing found or the wording drifted and the board
    is now parsing a message that no longer exists. Printing the zero collapses
    that, so a count that disappears is a defect somebody can see."""
    return f"  {name} advisory: {n} finding(s) \u2014 reported, not blocking."


def clean_head(name: str, detail: str) -> str:
    """`✓ <name> clean — <detail>`."""
    return f"✓ {name} clean — {detail}"


def findings_head(name: str, count: int, noun: str = "finding(s)",
                  tail: str = ".") -> str:
    """`✗ <name>: <count> <noun><tail>` — the tail carries each guard's own
    consequence wording (` — commit blocked.`, ` (limit 80 columns).`)."""
    return f"✗ {name}: {count} {noun}{tail}"


def cap_part(over: int, cap: int) -> str:
    """The tally part counting findings past the materialisation cap."""
    return f"{over} beyond the {cap}-finding cap (counted, not listed)"


def over_cap_line(over: int, cap: int, *, noun: str = "finding(s)",
                  indent: str = "  ") -> str:
    """The list line standing in for findings counted but never built."""
    return (f"{indent}…and {over} more {noun}, counted but not listed "
            f"(past the {cap}-finding memory cap).")


def finding_id(name: str, kind: str) -> str:
    """The namespaced finding ID, `<scanner>:<kind>` (`115/080`, part 3).

    `kind` is each guard's own parameter: exactly the scope its allow-marker
    accepts to exempt this finding — a rule name (`secretscan`, `leakscan`),
    a finding kind (`linkscan`, `datescan`, `pathscan`, `licenscan`,
    `sizescan`, `pointerscan`) or the matched word (`spellscan`). So the ID
    copies straight into `<scanner>:allow:<kind>: <reason>`, the narrowest
    marker there is. A finding with no line to carry a marker (a hit in a
    path name, a missing LICENSE) still gets one: the ID names it either way."""
    return f"{name}:{kind}"


def with_id(line: str, name: str, kind: str) -> str:
    """A finding line with its ID appended, the rest of the line unchanged:
    `<line>  [<scanner>:<kind>]`."""
    return f"{line}  [{finding_id(name, kind)}]"


def finding_dicts(name: str, findings: Iterable[object],
                  kind_of: Callable[[object], str]) -> list[dict]:
    """The `--json` findings list: each dataclass finding as before, plus an
    `id` field (`finding_id`), added last so every existing key keeps its
    place."""
    return [dict(asdict(f), id=finding_id(name, kind_of(f))) for f in findings]


def suppressed_line(parts: Sequence[str], *,
                    breakdown: dict[str, int] | None = None,
                    disabled: Sequence[str] = ()) -> str:
    """The rule-(b) tally: one stable line, known zeros printed, so two runs
    compare. `parts` is the scanner's own field list, in its own order (the
    order is part of its contract). The allow-marker breakdown and the
    disabled rules follow on their own lines, only when non-empty."""
    line = "  suppressed: " + " · ".join(parts)
    if breakdown:
        detail = ", ".join(f"{k}×{n}" for k, n in sorted(breakdown.items()))
        line += f"\n    allow-marker breakdown: {detail}"
    if disabled:
        line += f"\n    disabled: {', '.join(disabled)}"
    return line


# --- reading git's path output (115/260) ------------------------------------
#
# git C-quotes a path it thinks unsafe: wrapped in double quotes, with C
# escapes. With the default `core.quotePath` that is any non-ASCII byte; with
# `core.quotePath=false` it is still any control character (tab, newline), a
# double quote or a backslash. A parser that expects a bare path then either
# misses the file (`+++ b/` no longer matches `+++ "b/…"`) or keeps the quotes
# as part of the name. Two ways to read paths correctly, one helper each:
#
#   * a command with a `-z` form (`ls-files`, `ls-tree`, `diff --name-only`)
#     writes the raw bytes, NUL-terminated, never quoted: `nul_paths`;
#   * the `+++` header of a unified diff has no `-z` form: pass
#     `-c core.quotePath=false` (so non-ASCII arrives raw) and read the header
#     with `diff_header_path`, which undoes the quoting git still applies.

_C_ESCAPES = {"a": 7, "b": 8, "f": 12, "n": 10, "r": 13, "t": 9, "v": 11,
              "\\": 92, '"': 34}
_OCTAL_RX = re.compile(r"[0-3][0-7]{2}")


def unquote_c(s: str) -> str:
    """Undo git's C-style quoting of `s`, the text BETWEEN the double quotes:
    `\\a \\b \\f \\n \\r \\t \\v \\\\ \\"` and three-digit octal bytes (what
    `core.quotePath=true` writes for a non-ASCII byte). The octal bytes join
    any raw characters and the whole is decoded as UTF-8, so `caf\\303\\251`
    and `café` give the same string. Bytes that are not UTF-8 come back as
    U+FFFD rather than raising. A backslash git would never write (not
    followed by an escape letter or three octal digits) is kept as it stands."""
    raw = bytearray()
    i, n = 0, len(s)
    while i < n:
        ch = s[i]
        if ch == "\\" and i + 1 < n:
            if s[i + 1] in _C_ESCAPES:
                raw.append(_C_ESCAPES[s[i + 1]])
                i += 2
                continue
            if _OCTAL_RX.fullmatch(s[i + 1:i + 4]):
                raw.append(int(s[i + 1:i + 4], 8))
                i += 4
                continue
        raw += ch.encode("utf-8", "surrogateescape")
        i += 1
    return raw.decode("utf-8", "replace")


def diff_header_path(line: str) -> str | None:
    """The new-side path from a unified-diff `+++` header line, or None if
    `line` is not one. Only git's two spellings with the default `b/` prefix
    count: `+++ b/<path>` and the quoted `+++ "b/<path>"`. A looser test would
    take an added line whose text is `++ …` (it prints as `+++ …`) for a header.

    A path containing a space is followed by one literal TAB (git's marker
    for a name that could otherwise be confused with a timestamp) and nothing
    else, quoted or not (`+++ "b/say \\"hi\\".md"<TAB>`), so the tab is
    stripped. A tab INSIDE a name is always written as the two characters
    `\\t`, so stripping trailing tabs never eats part of a name."""
    line = line.rstrip("\t")
    if line.startswith('+++ "b/') and line.endswith('"') and len(line) > 8:
        return unquote_c(line[len('+++ "'):-1])[len("b/"):]
    if line.startswith("+++ b/"):
        return line[len("+++ b/"):]
    return None


def nul_paths(raw: bytes) -> list[str]:
    """The paths in `-z` output: NUL-terminated, never quoted, so any byte
    but NUL is a legal name. Decoded as the filesystem decodes (surrogate-
    escaped), so an undecodable name still round-trips into a later `git`
    argument. An empty token (the trailing NUL) is dropped."""
    return [os.fsdecode(tok) for tok in raw.split(b"\0") if tok]


# --- reading the staged diff (115/280) --------------------------------------
#
# Three guards scan what a commit would add: secretscan, conflictscan and
# leakscan, each from `git diff --cached --unified=0`. Each used to find the
# file a line belongs to by testing every line for `+++ `. But an ADDED line
# whose own text begins `++ ` prints as `+++ …`: it looked like a header, moved
# the attribution of every added line after it to whatever name followed, and
# (the other half of the same test) was itself dropped as "not an added line".
# A posed name that a guard ignores or exempts hid the real lines after it, on
# a blocking guard. `diff_header_path` narrowed what counts as a header; it
# could not say WHERE one may appear, and git's own `b/…` spelling is exactly
# what a poser types.
#
# So the reader follows the diff's structure, not its look. Outside a hunk
# every line is git's: `diff --git` opens a file and the `+++` line before that
# file's first `@@` names it. Inside a hunk, the `@@ -a,b +c,d @@` counts say
# how many old and new lines the body holds, so a line is body until those
# counts reach zero, whatever it starts with (an omitted count means 1). The
# counts are the whole argument: git used them to write the body, so a hunk's
# last line is known without reading its text.
#
# Fail closed: a line that cannot sit where the counts put it means the output
# is not a shape this reader understands. That is `DiffReadError` (exit 2 via
# `git_diff_failed`), never a guess that might hide a line.

# What the command pins, and why each pin is there (160/800):
#   * `core.quotePath=false`: a non-ASCII name is printed as itself.
#   * `diff.suppressBlankEmpty=false` and `diff.interHunkContext=0`, with
#     `GIT_DIFF_OPTS` dropped from the environment (`_diff_env`): the plane is
#     `-U0` as designed. A user setting that prints a blank context line bare
#     (`suppressBlankEmpty`), or fuses nearby hunks and so brings context in
#     (`interHunkContext`, or a `-u3` in `GIT_DIFF_OPTS`, which git applies OVER
#     the `--unified=0` below), made the reader refuse a legitimate diff on all
#     three blocking guards (SX1).
#   * `--no-ext-diff` and the two prefixes: the header shape is git's own.
#   * `--no-relative`: paths are root-relative whatever `diff.relative` says or
#     the directory a hand run starts from.
#   * `ACMRT`: T is a typechange. A file that replaces a symlink (or the
#     reverse) is not "modified" to git, so `ACMR` never showed it to any guard
#     (SX3). R stays on purpose: git detects renames by default and a renamed
#     AND edited file's added lines are as leak-capable as a modified file's.
#
# Left unpinned on purpose, and recorded as a choice (SX4): `diff.<driver>.
# textconv`. It lives in the user's own config (a commit cannot stage it), and
# pinning `--no-textconv` would also remove the extra cover a textconv for
# PDF or DOCX gives. What a commit CAN stage, a `-diff` or `binary` attribute
# that makes git print "Binary files differ" for text, is closed another way:
# `staged_added` reads such a file's added lines with `--text` when its index
# copy is text (`_hidden_text_paths`).
#
# Not bounded (SX6, SX11): the diff is captured whole and every added line is
# materialised, so this plane's memory grows with the commit, unlike the
# whole-tree plane (020/370, 020/380). Streaming it needs a ruling on what an
# over-long staged line does; it is routed to the principal, not guessed here.
_DIFF_PINS = (
    "-c", "core.quotePath=false", "-c", "diff.suppressBlankEmpty=false",
    "-c", "diff.interHunkContext=0")

STAGED_DIFF_CMD = (
    "git", *_DIFF_PINS, "diff", "--cached", "--unified=0",
    "--no-color", "--no-ext-diff", "--no-relative", "--src-prefix=a/",
    "--dst-prefix=b/", "--diff-filter=ACMRT")


def _diff_env() -> dict[str, str]:
    """The environment `git diff` runs in: ours, minus `GIT_DIFF_OPTS`, the one
    variable git applies over the command line. `GIT_INDEX_FILE` and the rest
    stay: a partial commit uses a temporary index and the diff must read it."""
    return {k: v for k, v in os.environ.items() if k != "GIT_DIFF_OPTS"}


_HUNK_RX = re.compile(
    r"^@@ -\d+(?:,(?P<old_n>\d+))? \+(?P<new_start>\d+)(?:,(?P<new_n>\d+))? @@")


class DiffReadError(Exception):
    """The staged diff is not shaped the way git writes one."""


STAGED_DIFF_FAILURES = (subprocess.CalledProcessError, DiffReadError)


def parse_added_lines(raw: bytes) -> Iterator[tuple[str, int, str]]:
    """Every added line of a `--unified=0` diff as (path, real new-file line
    number, text without the leading `+`).

    Split on the newline byte only: `str.splitlines` also breaks on form feed,
    vertical tab, NEL and the Unicode separators, and universal newlines break
    on a lone CR, and each lets an added line's own text start a line of its
    own. One trailing CR (a CRLF file) is dropped, as universal newlines did.
    The prefixes are pinned by `STAGED_DIFF_CMD`, so a header that is not
    `b/…` or `/dev/null` is not git's and is refused."""
    lines = raw.split(b"\n")
    if lines and lines[-1] == b"":
        lines.pop()
    path: str | None = None
    in_file = False          # a `diff --git` has been seen
    in_header = False        # between `diff --git` and the file's first `@@`
    old_rem = new_rem = 0    # lines the current hunk still owes
    lineno = 0
    for n, b in enumerate(lines, 1):
        line = b.decode("utf-8", "replace")
        if line.endswith("\r"):
            line = line[:-1]
        if old_rem or new_rem:
            kind = line[:1]
            if kind == "+" and new_rem and path is not None:
                new_rem -= 1
                yield path, lineno, line[1:]
                lineno += 1
            elif kind == "-" and old_rem:
                old_rem -= 1
            elif kind == " " and old_rem and new_rem:
                old_rem -= 1
                new_rem -= 1
                lineno += 1
            elif kind != "\\":     # `\ No newline at end of file`: no count
                raise DiffReadError(
                    f"diff line {n} does not fit its hunk's counts: {line[:60]!r}")
            continue
        if line.startswith("diff --git "):
            path, in_file, in_header = None, True, True
        elif line.startswith("@@"):
            m = _HUNK_RX.match(line)
            if m is None or not in_file:
                raise DiffReadError(
                    f"diff line {n}: a hunk with no file or no counts: "
                    f"{line[:60]!r}")
            in_header = False
            old_n, new_n = m.group("old_n"), m.group("new_n")
            old_rem = 1 if old_n is None else int(old_n)
            new_rem = 1 if new_n is None else int(new_n)
            lineno = int(m.group("new_start"))
        elif in_header and line.startswith("+++ "):
            if line.rstrip("\t") == "+++ /dev/null":
                path = None
            else:
                path = diff_header_path(line)
                if path is None:
                    raise DiffReadError(
                        f"diff line {n}: an unrecognised file header: "
                        f"{line[:60]!r}")
        elif line.startswith("+"):
            # Git writes a `+` line outside a hunk only as the `+++` header
            # handled above. Any other is added text the counts did not
            # account for: refuse it rather than drop it.
            raise DiffReadError(
                f"diff line {n}: added text outside a hunk: {line[:60]!r}")
        # Any other line outside a hunk is git's own (`index`, `---`, `mode`,
        # `rename`, `Binary files … differ`, `\ No newline`): never added text.
    if old_rem or new_rem:
        raise DiffReadError("the diff ends inside a hunk")


def staged_binary_paths() -> set[str]:
    """Paths the staged change adds, modifies, copies, renames or retypes that
    git reads as BINARY (`numstat` prints `-` for both counts). `--no-textconv`
    so the verdict is about the bytes, not a driver's text. Shared by
    `staged_added` (to find text a `-diff` attribute hid) and leakscan's binary
    gate. Raises `subprocess.CalledProcessError`."""
    out = subprocess.run(
        ["git", "diff", "--cached", "-z", "--numstat", "--no-textconv",
         "--no-relative", "--diff-filter=ACMRT"],
        capture_output=True, check=True, env=_diff_env())
    toks = nul_paths(out.stdout)
    binary: set[str] = set()
    i = 0
    while i < len(toks):
        added, deleted, rest = toks[i].split("\t", 2)
        if rest:
            path, i = rest, i + 1
        else:  # rename/copy: the source and destination follow as tokens
            path, i = toks[i + 2], i + 3
        if added == "-" and deleted == "-":
            binary.add(path)
    return binary


# git's own test for "binary": a NUL in the first 8000 bytes.
_BINARY_PROBE_BYTES = 8000


def _blob_looks_text(path: str) -> bool:
    """Does the INDEX copy of `path` have no NUL in its first 8000 bytes? Reads
    only that much, so a large binary is never read whole."""
    proc = subprocess.Popen(["git", "cat-file", "blob", f":0:{path}"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        head = proc.stdout.read(_BINARY_PROBE_BYTES)
    finally:
        proc.kill()
        proc.stdout.close()
        proc.stderr.close()
        proc.wait()
    return b"\0" not in head


def _hidden_text_paths() -> list[str]:
    """Staged paths git calls binary although their bytes are text: a `-diff`
    or `binary` attribute, staged in the same commit as the file, makes
    `git diff` print "Binary files differ" and no line at all, so a secret in
    the file reached no guard (160/800 SX4, driven through a real commit)."""
    return sorted(p for p in staged_binary_paths() if _blob_looks_text(p))


def staged_added() -> list[tuple[str, int, str]]:
    """The added lines of the staged diff as (path, line number, text), read by
    `parse_added_lines`. Raises `subprocess.CalledProcessError` if git fails and
    `DiffReadError` if its output is not a diff the reader understands; callers
    catch `STAGED_DIFF_FAILURES` and exit 2. The pins and the reasons for the
    filter are on `STAGED_DIFF_CMD`.

    A file git calls binary whose index copy is text is read again with
    `--text`, one path at a time. A genuinely binary file is never read: it is
    the reason the first pass does not use `--text` for everything (a staged
    photograph would arrive as megabytes of "lines")."""
    out = subprocess.run(list(STAGED_DIFF_CMD), capture_output=True,
                         check=True, env=_diff_env())
    added = list(parse_added_lines(out.stdout))
    for path in _hidden_text_paths():
        out = subprocess.run(
            [*STAGED_DIFF_CMD, "--text", "--", f":(top,literal){path}"],
            capture_output=True, check=True, env=_diff_env())
        added.extend(parse_added_lines(out.stdout))
    return added
