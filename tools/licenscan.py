#!/usr/bin/env python3
"""licenscan — the third pre-publish gate: is this repo safe to publish under ONE
coherent licence?

leakscan keeps personal/estate data out; secretscan keeps credentials out. Both
guard *content*. licenscan guards a different publish trap: a repo whose licence
story is inconsistent or incompatible — publish it and you either grant the wrong
rights, grant none (no LICENSE ⇒ all-rights-reserved by default), or relicense
someone else's copyleft code you had no right to relicense. The three together are
the pre-publish triad: no personal data · no secrets · no licence surprise.

Unlike the other two this is a *pre-publish* check, not an every-commit one — a
private repo can carry licence mess harmlessly; it only bites at the public
boundary (AUTONOMY: making a repo public is a floor action, and this is part of
the scrub that floor implies).

Three checks, in rising specificity:

  1. LICENSE present and recognised. A repo about to go public with no LICENSE
     file defaults to "all rights reserved" — the opposite of what an open repo
     intends. An unrecognised LICENSE means we can't verify the rest.

  2. Every licence DECLARATION agrees with LICENSE. Metadata that names a licence
     — pyproject.toml, package.json, Cargo.toml, *.gemspec, setup.cfg, a README
     shields.io badge — must name the same SPDX licence the LICENSE file is. A
     repo that says Apache-2.0 in LICENSE and MIT in pyproject contradicts itself.

  3. No incompatible foreign SPDX header. A source file carrying an
     `SPDX-License-Identifier` header differing from the repo licence is either a
     vendored-in file (needs attention) or a poison pill: copyleft (GPL/AGPL/
     LGPL/MPL) code cannot be relicensed under a permissive repo licence.

The compatibility judgement is deliberately CONSERVATIVE and advisory — it flags
for a human, it is not legal advice. It does not encode the deep cases (e.g. the
Apache-2.0/GPLv2 patent-clause incompatibility); it encodes the one that bites in
practice: copyleft-into-permissive is a block, permissive-into-permissive and
anything-into-copyleft is a warn (inconsistency worth a look, not a stopper).

What it structurally CANNOT see (review B3 — a clean scan means "no known shape
matched", not "licence-safe"): a vendored file carrying the traditional PROSE
licence header with no `SPDX-License-Identifier` tag — the commonest real-world
copyleft shape — is invisible to check 3; the human pre-publish scrub owns that
case. Dual-licence expressions (`MIT OR Apache-2.0`) and `LicenseRef-` custom
ids degrade conservatively to an unknown-declaration warn (friction, never a
false pass). A legitimately bundled copyleft component (the NOTICE case) will
block — the allow-marker / .licenscanignore hatch, with its reason recorded, is
the sanctioned way to express "bundled, not relicensed".

Exit codes (fail-safe — anything but a clean, verifiable scan is non-zero):
  0  clean — one coherent, recognised licence, no incompatible headers
  1  findings (blocks a publish)
  2  usage / config error (a scan that couldn't run is NOT a pass)

Zero third-party dependencies; stdlib only.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

# A line carrying this marker is intentionally exempt (e.g. a documented example
# header in test data, or a deliberately dual-licensed file). Keep the reason on
# the same line.
ALLOW_MARKER = "licenscan:allow"

# GUARDS.md rule (c): a marker only counts with a colon and a non-empty reason,
# so prose that merely mentions the marker text exempts nothing. Tightened
# 2026-08-05 — a bare marker used to exempt on a substring match.
ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER) + r"(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>\w)")


def parse_allow(text: str) -> str | None:
    """The scope of the allow-marker, or None if there is no reasoned one.

    `""` means every declaration on the line. A marker with no reason
    returns None — a mention, not an exemption."""
    m = ALLOW_RX.search(text)
    if not m:
        return None
    return m.group("kind") or ""


SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache", "dist",
                  "build", ".idea", ".vscode"}

# Filenames that carry the canonical licence text.
LICENSE_FILENAMES = ("LICENSE", "LICENSE.txt", "LICENSE.md", "LICENCE",
                     "LICENCE.txt", "LICENCE.md", "COPYING", "COPYING.txt")

# ---- SPDX classification -------------------------------------------------------
# The three families that decide compatibility. Permissive code flows anywhere;
# copyleft code cannot be relicensed under a permissive repo licence.
PERMISSIVE = frozenset({
    "Apache-2.0", "MIT", "BSD-2-Clause", "BSD-3-Clause", "ISC",
    "Unlicense", "BSL-1.0", "0BSD", "Zlib",
})
WEAK_COPYLEFT = frozenset({"MPL-2.0", "LGPL-2.1", "LGPL-3.0", "EPL-2.0"})
STRONG_COPYLEFT = frozenset({"GPL-2.0", "GPL-3.0", "AGPL-3.0"})
COPYLEFT = WEAK_COPYLEFT | STRONG_COPYLEFT
KNOWN_SPDX = PERMISSIVE | COPYLEFT


def family(spdx: str) -> str:
    if spdx in PERMISSIVE:
        return "permissive"
    if spdx in WEAK_COPYLEFT:
        return "weak-copyleft"
    if spdx in STRONG_COPYLEFT:
        return "strong-copyleft"
    return "unknown"


# Signature phrases that identify a full LICENSE body → SPDX id. Ordered: the
# more specific string first (AGPL/LGPL contain "GENERAL PUBLIC LICENSE", so they
# must be tested before GPL; BSD-3 before BSD-2 since 3-clause is 2-clause + a
# clause). All matched case-insensitively against whitespace-collapsed text.
_TEXT_SIGNATURES: list[tuple[str, tuple[str, ...]]] = [
    ("AGPL-3.0", ("gnu affero general public license", "version 3")),
    ("LGPL-3.0", ("gnu lesser general public license", "version 3")),
    ("LGPL-2.1", ("gnu lesser general public license", "version 2.1")),
    ("GPL-3.0", ("gnu general public license", "version 3")),
    ("GPL-2.0", ("gnu general public license", "version 2")),
    ("Apache-2.0", ("apache license", "version 2.0")),
    ("MPL-2.0", ("mozilla public license version 2.0",)),
    ("EPL-2.0", ("eclipse public license - v 2.0",)),
    ("BSL-1.0", ("boost software license",)),
    ("BSD-3-Clause", ("redistribution and use in source and binary forms",
                      "neither the name")),
    ("BSD-2-Clause", ("redistribution and use in source and binary forms",)),
    ("ISC", ("permission to use, copy, modify, and/or distribute this software",)),
    ("MIT", ("permission is hereby granted, free of charge, to any person "
             "obtaining a copy",)),
    ("Unlicense", ("this is free and unencumbered software released into the "
                   "public domain",)),
    ("0BSD", ("permission to use, copy, modify, and/or distribute this software "
              "for any purpose with or without fee is hereby granted",)),
]


def identify_license_text(text: str) -> str | None:
    """Best-effort SPDX id for a full licence body, or None if unrecognised."""
    hay = re.sub(r"\s+", " ", text).lower()
    for spdx, needles in _TEXT_SIGNATURES:
        if all(n in hay for n in needles):
            return spdx
    return None


# SPDX ids people actually write in metadata, normalised to our canonical form.
# Covers the common aliases (apache 2.0 spellings, "gplv3", classifier strings).
_SPDX_ALIASES = {
    "apache-2.0": "Apache-2.0", "apache 2.0": "Apache-2.0",
    "apache license 2.0": "Apache-2.0", "asl 2.0": "Apache-2.0",
    "apache-2": "Apache-2.0",
    "mit": "MIT", "mit license": "MIT", "expat": "MIT",
    "bsd-3-clause": "BSD-3-Clause", "bsd-3": "BSD-3-Clause",
    "bsd 3-clause": "BSD-3-Clause", "new bsd": "BSD-3-Clause",
    "bsd-2-clause": "BSD-2-Clause", "bsd-2": "BSD-2-Clause",
    "simplified bsd": "BSD-2-Clause",
    "isc": "ISC", "unlicense": "Unlicense", "the unlicense": "Unlicense",
    "bsl-1.0": "BSL-1.0", "boost": "BSL-1.0",
    "0bsd": "0BSD", "zlib": "Zlib",
    "mpl-2.0": "MPL-2.0", "mpl 2.0": "MPL-2.0", "mozilla public license 2.0": "MPL-2.0",
    "epl-2.0": "EPL-2.0",
    "lgpl-3.0": "LGPL-3.0", "lgpl-3.0-or-later": "LGPL-3.0", "lgplv3": "LGPL-3.0",
    "lgpl-2.1": "LGPL-2.1", "lgplv2.1": "LGPL-2.1",
    "gpl-3.0": "GPL-3.0", "gpl-3.0-or-later": "GPL-3.0", "gpl-3.0-only": "GPL-3.0",
    "gplv3": "GPL-3.0", "gpl3": "GPL-3.0",
    "gpl-2.0": "GPL-2.0", "gpl-2.0-or-later": "GPL-2.0", "gplv2": "GPL-2.0",
    "agpl-3.0": "AGPL-3.0", "agpl-3.0-or-later": "AGPL-3.0", "agplv3": "AGPL-3.0",
}


def normalise_spdx(raw: str) -> str | None:
    """A metadata licence string → canonical SPDX id, or None if unrecognised.
    Strips the OSI classifier prefix and common decoration first."""
    s = raw.strip().strip("\"'").lower()
    s = s.replace("license :: osi approved ::", "").strip()
    s = re.sub(r"\s+license$", "", s).strip()
    # Modern SPDX writes GPL-family ids with an -only/-or-later suffix (and the
    # deprecated `GPL-2.0+` form). Our family tables key on the base id, and
    # only/or-later never changes the copyleft family — so strip the suffix
    # rather than alias every combination. Review B2: without this, a
    # `GPL-2.0-only` header mis-tiered from a high/incompatible BLOCK to a
    # medium unknown-declaration warn.
    s = re.sub(r"-(?:only|or-later)$", "", s).rstrip("+")
    if s in _SPDX_ALIASES:
        return _SPDX_ALIASES[s]
    # a bare canonical id written exactly (case-insensitive) still resolves
    for spdx in KNOWN_SPDX:
        if s == spdx.lower():
            return spdx
    return None


# ---- declaration extractors ----------------------------------------------------
# Each returns the raw licence string(s) a metadata file declares. Kept simple and
# forgiving — we want the common shapes, not a TOML/JSON parser per ecosystem.

_PYPROJECT_LICENSE = re.compile(
    r"""(?im)^\s*license\s*=\s*(?:\{[^}]*?(?:text|expression)\s*=\s*)?["']([^"']+)["']""")
_PYPROJECT_CLASSIFIER = re.compile(
    r"""(?im)["']\s*License\s*::\s*OSI Approved\s*::\s*([^"']+?)["']""")
_JSON_LICENSE = re.compile(r'(?im)(?:^|[{,])\s*"license"\s*:\s*"([^"]+)"')
_TOML_LICENSE = re.compile(r"""(?im)^\s*license\s*=\s*["']([^"']+)["']""")
_SETUPCFG_LICENSE = re.compile(r"""(?im)^\s*license\s*=\s*([^\n#]+)""")
_GEMSPEC_LICENSE = re.compile(
    r"""(?im)\.licenses?\s*=\s*(?:\[)?\s*["']([^"']+)["']""")
# A shields.io / img.shields.io licence badge: .../license-<NAME>-...  (README)
_BADGE_LICENSE = re.compile(r"""(?i)/license-([A-Za-z0-9._%+-]+?)(?:-[a-z]+)?\.svg""")
# An inline SPDX header line in any source file.
_SPDX_HEADER = re.compile(r"""SPDX-License-Identifier:\s*([^\s*/#]+)""")  # licenscan:allow: this is the header-detection pattern, not a real header


@dataclass
class Declaration:
    path: str
    line: int
    source: str        # "pyproject" | "package.json" | "badge" | "spdx-header" | ...
    raw: str
    spdx: str | None   # normalised, or None if unrecognised


def _line_at(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def _line_text_at(text: str, pos: int) -> str:
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos)
    return text[start:(end if end != -1 else len(text))]


def declarations_in(rel: str, text: str,
                    suppressed: list[int] | None = None) -> list[Declaration]:
    """Licence declarations a single file makes (not the LICENSE body itself).
    Line numbers come from the match offset, not a re-search for the captured
    text — a captured fragment can recur elsewhere and mislocate the finding."""
    out: list[Declaration] = []
    if suppressed is None:
        suppressed = []
    name = rel.rsplit("/", 1)[-1]

    def add(source: str, m: "re.Match[str]", raw: str | None = None):
        pos = m.start()
        if parse_allow(_line_text_at(text, pos)) is not None:
            suppressed.append(1)
            return
        value = m.group(1) if raw is None else raw
        out.append(Declaration(rel, _line_at(text, pos), source, value,
                               normalise_spdx(value)))

    if name == "pyproject.toml":
        for m in _PYPROJECT_LICENSE.finditer(text):
            add("pyproject", m)
        for m in _PYPROJECT_CLASSIFIER.finditer(text):
            add("pyproject-classifier", m)
    elif name == "package.json":
        for m in _JSON_LICENSE.finditer(text):
            add("package.json", m)
    elif name in ("Cargo.toml",) or name.endswith(".toml"):
        for m in _TOML_LICENSE.finditer(text):
            add("cargo/toml", m)
    elif name == "setup.cfg":
        for m in _SETUPCFG_LICENSE.finditer(text):
            add("setup.cfg", m)
    elif name.endswith(".gemspec"):
        for m in _GEMSPEC_LICENSE.finditer(text):
            add("gemspec", m)

    if name.lower().startswith("readme"):
        for m in _BADGE_LICENSE.finditer(text):
            add("badge", m, m.group(1).replace("%20", " "))

    for m in _SPDX_HEADER.finditer(text):
        add("spdx-header", m)
    return out


# ---- findings ------------------------------------------------------------------
@dataclass
class Finding:
    kind: str          # "no-license" | "unknown-license" | "mismatch" |
                       # "incompatible" | "unknown-declaration" | "expect-mismatch"
    severity: str      # "high" | "medium"
    message: str
    path: str = ""
    line: int = 0


def compatibility(repo: str, header: str) -> str:
    """Is a file carrying `header` publishable under repo licence `repo`?
    Returns "ok" | "warn" | "block". Conservative; not legal advice."""
    if header == repo:
        return "ok"
    rf, hf = family(repo), family(header)
    if rf == "permissive" and hf in ("weak-copyleft", "strong-copyleft"):
        return "block"   # cannot relicense copyleft as permissive
    if hf == "unknown" or rf == "unknown":
        return "warn"
    return "warn"        # any other cross-licence mix: inconsistency, human call


@dataclass
class Report:
    repo_license: str | None = None
    repo_license_path: str = ""
    findings: list[Finding] = field(default_factory=list)
    # Rule (b): declarations an allow-marker removed, and files an ignore glob
    # skipped. Counted so a clean report cannot look identical to one where
    # everything was exempted.
    suppressed_declarations: int = 0
    files_by_glob: int = 0

    @property
    def clean(self) -> bool:
        return not self.findings


def scan_repo(root: Path, files: list[tuple[str, str]],
              expect: str | None) -> Report:
    """`files` is (relpath, text) for every scanned file. Pure — no I/O — so the
    engine is trivially testable."""
    rep = Report()
    _suppressed: list[int] = []

    # 1. locate + identify the LICENSE body.
    license_bodies = [(rel, txt) for rel, txt in files
                      if rel.rsplit("/", 1)[-1] in LICENSE_FILENAMES]
    if not license_bodies:
        rep.findings.append(Finding(
            "no-license", "high",
            "no LICENSE file found — an open repo with no licence defaults to "
            "all-rights-reserved. Add one before publishing."))
    else:
        rel, txt = license_bodies[0]
        rep.repo_license_path = rel
        rep.repo_license = identify_license_text(txt)
        if rep.repo_license is None:
            rep.findings.append(Finding(
                "unknown-license", "medium",
                "LICENSE text not recognised as a known SPDX licence — cannot "
                "verify declarations/headers against it.", rel, 1))

    if expect is not None:
        want = normalise_spdx(expect) or expect
        if rep.repo_license is not None and rep.repo_license != want:
            rep.findings.append(Finding(
                "expect-mismatch", "high",
                f"LICENSE is {rep.repo_license} but --expect {want} was asserted.",
                rep.repo_license_path, 1))

    # 2/3. every declaration + header must agree with (or be compatible with) it.
    repo = rep.repo_license
    for rel, txt in files:
        if rel == rep.repo_license_path:
            continue
        for d in declarations_in(rel, txt, _suppressed):
            if d.spdx is None:
                rep.findings.append(Finding(
                    "unknown-declaration", "medium",
                    f"{d.source} declares licence '{d.raw}', not a recognised "
                    f"SPDX id — can't verify it.", d.path, d.line))
                continue
            if repo is None:
                continue  # nothing to compare against; no-license already flagged
            if d.source == "spdx-header":
                verdict = compatibility(repo, d.spdx)
                if verdict == "block":
                    rep.findings.append(Finding(
                        "incompatible", "high",
                        f"file carries SPDX header {d.spdx} ({family(d.spdx)}), "
                        f"incompatible with repo licence {repo} — cannot be "
                        f"relicensed on publish.", d.path, d.line))
                elif verdict == "warn" and d.spdx != repo:
                    rep.findings.append(Finding(
                        "mismatch", "medium",
                        f"file SPDX header {d.spdx} differs from repo licence "
                        f"{repo} — vendored code needing attention or a stray "
                        f"header.", d.path, d.line))
            elif d.spdx != repo:
                rep.findings.append(Finding(
                    "mismatch", "high",
                    f"{d.source} declares {d.spdx} but LICENSE is {repo} — the "
                    f"repo contradicts itself.", d.path, d.line))
    rep.suppressed_declarations = len(_suppressed)
    return rep


# ---- file plumbing (mirrors the sibling scans; kept self-contained) ------------
def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".licenscanignore"
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


def _looks_binary(data: bytes) -> bool:
    return b"\x00" in data[:8192]


def collect_files(root: Path, globs: list[str],
                  skipped: list[int] | None = None) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for p in root.rglob("*"):
        if not p.is_file() or (SKIP_DIR_NAMES & set(p.parts)):
            continue
        rel = str(p.relative_to(root))
        if _ignored(rel, globs):
            if skipped is not None:
                skipped.append(1)
            continue
        data = p.read_bytes()
        if _looks_binary(data):
            continue
        out.append((rel, data.decode("utf-8", errors="replace")))
    return out


def _suppression_line(rep: Report) -> str:
    """Rule (b): known zeros printed, so two runs can be compared."""
    return (f"  suppressed: {rep.suppressed_declarations} declaration(s) by "
            f"allow-marker · {rep.files_by_glob} file(s) by .licenscanignore")


def render_human(rep: Report) -> str:
    lines: list[str] = []
    lic = rep.repo_license or "unrecognised"
    if rep.clean:
        return (f"✓ licenscan clean — repo licence {lic}, all declarations agree."
                + "\n" + _suppression_line(rep))
    lines.append(f"✗ licenscan: {len(rep.findings)} finding(s) — repo licence "
                 f"{lic}. Publish blocked.\n")
    for f in sorted(rep.findings, key=lambda x: (x.severity != "high", x.path, x.line)):
        loc = f"  {f.path}:{f.line}  " if f.path else "  "
        lines.append(f"{loc}[{f.severity}/{f.kind}] {f.message}")
    lines.append("")
    lines.append(_suppression_line(rep))
    lines.append(f"\n  A false positive: append '# {ALLOW_MARKER}: <reason>' to the")
    lines.append("  line, or add a path glob to .licenscanignore. Not legal advice —")
    lines.append("  a conservative flag for a human to resolve before going public.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="licenscan",
        description="Pre-publish gate: one coherent, compatible licence across the repo.")
    ap.add_argument("root", nargs="?", default=".",
                    help="repo root to scan (default: cwd)")
    ap.add_argument("--expect", default=None, metavar="SPDX",
                    help="assert the repo licence is this SPDX id (e.g. Apache-2.0); "
                         "fail if LICENSE says otherwise (CI use)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"licenscan: not a directory: {root}", file=sys.stderr)
        return 2

    globs = load_ignore_globs(root)
    _skipped: list[int] = []
    files = collect_files(root, globs, _skipped)
    rep = scan_repo(root, files, args.expect)
    rep.files_by_glob = len(_skipped)

    if args.json:
        print(json.dumps({
            "clean": rep.clean,
            "repo_license": rep.repo_license,
            "repo_license_path": rep.repo_license_path,
            "findings": [asdict(f) for f in rep.findings],
        }, indent=2))
    else:
        print(render_human(rep))
    return 1 if rep.findings else 0


def _selftest() -> int:
    """Prove the engine on any box without the unittest file. Fictional fixtures;
    the licence shapes are the point."""
    apache = ("Apache License\nVersion 2.0, January 2004\n"
              "http://www.apache.org/licenses/")
    mit = ("MIT License\n\nPermission is hereby granted, free of charge, to any "
           "person obtaining a copy of this software")
    gpl3 = "GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007"

    checks: list[tuple[str, bool]] = []

    # recognised bodies
    checks.append(("id apache", identify_license_text(apache) == "Apache-2.0"))
    checks.append(("id mit", identify_license_text(mit) == "MIT"))
    checks.append(("id gpl3", identify_license_text(gpl3) == "GPL-3.0"))
    checks.append(("id junk", identify_license_text("hello world") is None))

    # normalisation
    checks.append(("norm gplv3", normalise_spdx("GPLv3") == "GPL-3.0"))
    checks.append(("norm classifier",
                   normalise_spdx("License :: OSI Approved :: MIT License") == "MIT"))
    # review B2: modern -only/-or-later/+ forms must resolve to the base id,
    # or a strong-copyleft header mis-tiers from block to unknown-declaration
    checks.append(("norm gpl-2.0-only", normalise_spdx("GPL-2.0-only") == "GPL-2.0"))
    checks.append(("norm agpl-3.0-only", normalise_spdx("AGPL-3.0-only") == "AGPL-3.0"))
    checks.append(("norm gpl-2.0+", normalise_spdx("GPL-2.0+") == "GPL-2.0"))
    only_poison = scan_repo(Path("."), [
        ("LICENSE", apache),
        ("vendor/z.py", "# SPDX-License-Identifier: GPL-2.0-only\n"),  # licenscan:allow: selftest fixture, not a real header
    ], None)
    checks.append(("-only copyleft still blocks",
                   any(f.kind == "incompatible" for f in only_poison.findings)))

    # clean repo: apache LICENSE + agreeing pyproject
    clean = scan_repo(Path("."), [
        ("LICENSE", apache),
        ("pyproject.toml", 'license = "Apache-2.0"\n'),
    ], None)
    checks.append(("clean repo", clean.clean))

    # contradiction: apache LICENSE, MIT pyproject
    mism = scan_repo(Path("."), [
        ("LICENSE", apache),
        ("pyproject.toml", 'license = "MIT"\n'),
    ], None)
    checks.append(("declaration mismatch",
                   any(f.kind == "mismatch" and f.severity == "high"
                       for f in mism.findings)))

    # poison pill: permissive repo, GPL header in a file
    poison = scan_repo(Path("."), [
        ("LICENSE", apache),
        ("vendor/x.py", "# SPDX-License-Identifier: GPL-3.0\n"),  # licenscan:allow: selftest fixture, not a real header
    ], None)
    checks.append(("copyleft poison blocks",
                   any(f.kind == "incompatible" for f in poison.findings)))

    # permissive-into-permissive header: a warn, not a block
    mixp = scan_repo(Path("."), [
        ("LICENSE", apache),
        ("vendor/y.py", "// SPDX-License-Identifier: MIT\n"),  # licenscan:allow: selftest fixture, not a real header
    ], None)
    checks.append(("permissive header warns",
                   any(f.kind == "mismatch" and f.severity == "medium"
                       for f in mixp.findings)
                   and not any(f.severity == "high" for f in mixp.findings)))

    # no LICENSE at all
    none_lic = scan_repo(Path("."), [("pyproject.toml", 'license = "MIT"\n')], None)
    checks.append(("no license flags",
                   any(f.kind == "no-license" for f in none_lic.findings)))

    # --expect assertion
    exp = scan_repo(Path("."), [("LICENSE", apache)], "MIT")
    checks.append(("expect mismatch",
                   any(f.kind == "expect-mismatch" for f in exp.findings)))
    exp_ok = scan_repo(Path("."), [("LICENSE", apache)], "Apache-2.0")
    checks.append(("expect ok", exp_ok.clean))

    ok = True
    for label, passed in checks:
        if not passed:
            print(f"FAIL: {label}")
            ok = False
    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
