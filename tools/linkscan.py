#!/usr/bin/env python3
"""linkscan — the mechanical check that atelier's internal links resolve.

atelier's whole architecture is "thin anchor, fat pointer" (PROPAGATION.md): a
child inlines a safety floor and *points up* to the canonical doctrine; a doc
states a bearing and *points* to the case-law. That design is only as sound as
its pointers. A relative link that 404s — a renamed file, a moved doc, a typo'd
anchor — is a silent hole in the doctrine graph: the reader is told "see X" and X
isn't there. Intent doesn't catch that; a machine does. This is the machine.

Scope, deliberately narrow (a broad flaky tool is worse than a sharp honest one):

  * INTERNAL links only. `[text](path)` and `![alt](path)` whose destination is a
    relative or root-relative path. External schemes (http, https, mailto, tel,
    ftp…) and protocol-relative `//host` are SKIPPED — verifying them means the
    network, which is flaky, slow, and a different tool's job.

  * FILE existence — the destination path must resolve to a real file or dir,
    relative to the linking file (or the repo root for a leading `/`).

  * ANCHOR existence — for a `#fragment` into a Markdown file (or same-file), the
    fragment must match a heading, using GitHub's slug algorithm. `#L42`-style
    line anchors are line references, not headings, and are skipped. Anchors into
    non-Markdown targets aren't validated (nothing to validate against).

Links inside fenced (``` ```) or inline (`` `…` ``) code are ignored — they are
examples, not live pointers. Wiki-style `[[name]]` memory links are NOT Markdown
links (no `](`) and are out of scope by design.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean
  1  broken link(s) found
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can run
it with the system python3 and no install — and CI needs nothing but Python.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import unquote

# A line carrying this marker is intentionally exempt (e.g. a deliberately
# dangling pointer in a doc, or a template placeholder). Keep the reason on the
# same line so the exemption is self-documenting and greppable.
ALLOW_MARKER = "linkscan:allow"

# Only these extensions are parsed for links and headings; everything else is a
# link *target* (checked for existence) but never a *source*.
MARKDOWN_SUFFIXES = {".md", ".markdown"}

# Paths never worth walking — binary/vendored/VCS noise. Repo-specific globs
# come from .linkscanignore at the scan root.
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache", "dist",
                  "build", ".idea", ".vscode"}

# A URI scheme (http:, mailto:, tel:…) or a protocol-relative //host prefix:
# not our link to check.
_SCHEME = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.\-]*:|//)")

# `#L12` or `#L12-L20`: a GitHub line reference into source, not a heading.
_LINE_ANCHOR = re.compile(r"^L\d+(?:-L\d+)?$")

# An inline Markdown link/image destination: `](dest)` or `](dest "title")`,
# where dest is either <bracketed> (may hold spaces) or a bare run of non-space,
# non-`)` chars. Captures the raw destination group.
_LINK = re.compile(r"!?\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)")

# An ATX heading line: leading #'s then the text (trailing #'s stripped).
_ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


@dataclass
class Finding:
    path: str          # the linking Markdown file (repo-relative)
    line: int
    kind: str          # "missing-file" | "missing-anchor"
    target: str        # the raw link destination, as written
    detail: str        # human hint at what's missing


def slugify(heading: str) -> str:
    """GitHub's heading-anchor slug: strip inline formatting, lowercase, drop
    punctuation (keeping word chars, spaces, hyphens), spaces→hyphens. Good
    enough for the ATX headings atelier writes; deliberately not a full CommonMark
    renderer (an exotic heading that mis-slugs costs one `linkscan:allow`)."""
    text = heading.strip()
    # Unwrap the commonest inline formatting so `` `foo` `` / `**foo**` /
    # `[foo](x)` slug to their visible text, matching GitHub.
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_~]", "", text)
    text = text.lower()
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    text = text.replace(" ", "-")
    return text


def heading_slugs(text: str) -> set[str]:
    """Every anchor GitHub would mint for this Markdown file's ATX headings,
    including the `-1`, `-2` disambiguation suffixes for repeated headings.
    Headings inside fenced code blocks are not headings."""
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        if in_fence:
            if fence and stripped.startswith(fence):
                in_fence = False
                fence = None
            continue
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = True
            fence = stripped[:3]
            continue
        m = _ATX.match(line)
        if not m:
            continue
        base = slugify(m.group(2))
        n = counts.get(base, 0)
        counts[base] = n + 1
        slugs.add(base if n == 0 else f"{base}-{n}")
    return slugs


def _strip_inline_code(line: str) -> str:
    """Blank out inline `code spans` so a link-shaped example inside them isn't
    read as a live link. Backtick runs must match in length (CommonMark)."""
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        if line[i] == "`":
            j = i
            while j < n and line[j] == "`":
                j += 1
            ticks = line[i:j]
            close = line.find(ticks, j)
            if close != -1 and line[close:close + len(ticks)] == ticks \
                    and (close + len(ticks) >= n or line[close + len(ticks)] != "`"):
                out.append(" " * (close + len(ticks) - i))
                i = close + len(ticks)
                continue
        out.append(line[i])
        i += 1
    return "".join(out)


def iter_links(text: str):
    """Yield (lineno, raw_destination) for every inline link/image destination
    in a Markdown file, skipping fenced and inline code and `linkscan:allow`
    lines."""
    in_fence = False
    fence: str | None = None
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if in_fence:
            if fence and stripped.startswith(fence):
                in_fence = False
                fence = None
            continue
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = True
            fence = stripped[:3]
            continue
        if ALLOW_MARKER in line:
            continue
        for m in _LINK.finditer(_strip_inline_code(line)):
            dest = m.group(1).strip()
            if dest.startswith("<") and dest.endswith(">"):
                dest = dest[1:-1].strip()
            yield lineno, dest


def is_external(dest: str) -> bool:
    return bool(_SCHEME.match(dest))


def split_target(dest: str) -> tuple[str, str]:
    """(path, anchor) for a link destination. A leading `#` means same-file."""
    path, _, anchor = dest.partition("#")
    return unquote(path), anchor


def resolve(md_file: Path, root: Path, path: str) -> Path:
    """Resolve a link's path part to a filesystem path: root-relative for a
    leading `/`, else relative to the linking file's directory."""
    if path.startswith("/"):
        return (root / path.lstrip("/"))
    return (md_file.parent / path)


def check_file(md_file: Path, root: Path, text: str,
               slug_cache: dict[Path, set[str]]) -> list[Finding]:
    rel = _rel(md_file, root)
    own_slugs: set[str] | None = None
    findings: list[Finding] = []
    for lineno, dest in iter_links(text):
        if not dest or is_external(dest):
            continue
        path, anchor = split_target(dest)

        if path == "":
            # Same-file anchor. `#` alone (top-of-page) always resolves.
            if not anchor or _LINE_ANCHOR.match(anchor):
                continue
            if own_slugs is None:
                own_slugs = heading_slugs(text)
            if slugify(anchor) not in own_slugs:
                findings.append(Finding(rel, lineno, "missing-anchor", dest,
                                        f"no heading '#{anchor}' in this file"))
            continue

        target = resolve(md_file, root, path)
        if not target.exists():
            findings.append(Finding(rel, lineno, "missing-file", dest,
                                    f"{_rel(target, root)} does not exist"))
            continue

        # Path resolves. Validate a Markdown anchor if one was given.
        if anchor and not _LINE_ANCHOR.match(anchor) \
                and target.is_file() and target.suffix.lower() in MARKDOWN_SUFFIXES:
            key = target.resolve()
            if key not in slug_cache:
                slug_cache[key] = heading_slugs(
                    target.read_text(encoding="utf-8", errors="replace"))
            if slugify(anchor) not in slug_cache[key]:
                findings.append(Finding(rel, lineno, "missing-anchor", dest,
                                        f"no heading '#{anchor}' in {_rel(target, root)}"))
    return findings


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".linkscanignore"
    if not f.exists():
        return []
    globs: list[str] = []
    for raw in f.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            globs.append(line)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


def iter_markdown(paths: list[Path], root: Path, globs: list[str]):
    for base in paths:
        if base.is_file():
            candidates = [base]
        else:
            candidates = [p for p in base.rglob("*")
                          if p.is_file() and not (SKIP_DIR_NAMES & set(p.parts))]
        for p in candidates:
            if p.suffix.lower() not in MARKDOWN_SUFFIXES:
                continue
            if _ignored(_rel(p, root), globs):
                continue
            yield p


def scan_paths(paths: list[Path], root: Path) -> list[Finding]:
    globs = load_ignore_globs(root)
    slug_cache: dict[Path, set[str]] = {}
    findings: list[Finding] = []
    for md in iter_markdown(paths, root, globs):
        text = md.read_text(encoding="utf-8", errors="replace")
        findings.extend(check_file(md, root, text, slug_cache))
    return findings


def render_human(findings: list[Finding]) -> str:
    if not findings:
        return "✓ linkscan clean — every internal link resolves."
    lines = [f"✗ linkscan: {len(findings)} broken internal link(s).\n"]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.target} → {f.detail}")
    lines.append("\n  A real break: fix the path/anchor (or the moved/renamed target).")
    lines.append(f"  A deliberate dangling pointer: append '<!-- {ALLOW_MARKER}: <reason> -->'")
    lines.append("  to the line, or add a path glob to .linkscanignore.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="linkscan",
        description="Check that internal Markdown links (paths + anchors) resolve.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo)")
    ap.add_argument("--root", default=".",
                    help="repo root for root-relative (/…) links and .linkscanignore")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    targets = [Path(p) for p in (args.paths or [str(root)])]
    findings = scan_paths(targets, root)

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        print(render_human(findings))

    return 1 if findings else 0


def _selftest() -> int:
    """Minimal smoke test so `linkscan --selftest` proves the engine on any box,
    even where the unittest file isn't shipped. Builds a tiny doc tree in a temp
    dir and asserts the four core behaviours."""
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="linkscan-self-"))
    (tmp / "target.md").write_text("# Real Heading\n\nbody\n")
    (tmp / "index.md").write_text(
        "# Top\n\n"
        "## A Section\n"
        "[ok file](target.md)\n"                       # resolves
        "[ok anchor](target.md#real-heading)\n"        # slug matches
        "[ok same](#a-section)\n"                       # same-file anchor
        "[ok external](https://example.com/x)\n"       # skipped
        "[ok line](target.md#L5)\n"                     # line ref, skipped
        "`[not a link](nope.md)`\n"                     # inline code, skipped
        "[bad file](missing.md)\n"                      # BREAK 1
        "[bad anchor](target.md#ghost)\n"              # BREAK 2
        "[bad same](#no-such)\n"                         # BREAK 3
        "```\n[fenced](also-missing.md)\n```\n"        # fenced, skipped
    )
    findings = scan_paths([tmp], tmp)
    kinds = sorted((f.kind, f.target) for f in findings)
    expected = sorted([
        ("missing-file", "missing.md"),
        ("missing-anchor", "target.md#ghost"),
        ("missing-anchor", "#no-such"),
    ])
    ok = kinds == expected
    if not ok:
        print(f"FAIL: got {kinds}, expected {expected}")
    # slug edge cases
    for heading, want in [("Hello World", "hello-world"),
                          ("`code` & punct!", "code--punct"),
                          ("A—B", "ab")]:
        got = slugify(heading)
        if got != want:
            print(f"FAIL slug: {heading!r} → {got!r}, expected {want!r}")
            ok = False
    print("selftest OK" if ok else "selftest FAILED")
    import shutil
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
