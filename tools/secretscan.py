#!/usr/bin/env python3
"""secretscan — the mechanical gate that keeps plaintext credentials out of a
git commit.

leakscan guards the *public boundary* (personal/estate data must not enter a
repo that can go public). secretscan guards a different boundary that exists in
*every* repo, private ones included: a committed credential is burned the moment
it lands in history, regardless of who can see the repo — history is forever and
a private repo can be shared, forked or leaked later. So this runs everywhere,
and pairs with the SECRETS doctrine's other half: detect → rotate immediately →
the burn cost is minutes, not a breach.

Unlike leakscan there is no machine-local vocabulary: a secret is not a
person-specific name, it is a *shape*. Two detector classes:

  * NAMED credentials (high confidence) — formats that are unambiguously a
    secret by construction: private-key headers, AWS/GitHub/Slack/Google/Stripe/
    Anthropic tokens, JWTs. These always flag; no entropy gate needed.

  * ASSIGNED secrets (context + entropy) — a key that *names* a credential
    (`password`, `api_key`, `token`, `client_secret`…) assigned a value that is
    long, high-entropy, and not an obvious placeholder or indirection. This is
    the workhorse for home-grown secrets that match no vendor format. Context
    (the key name) plus entropy is far more precise than raw entropy scanning,
    which drowns in git hashes and base64 blobs.

Deliberately does NOT flag the safe indirection patterns — `!secret foo` (tiki),
`${VAR}`, `$(cmd)`, `<placeholder>` — because those are the *correct* way to
reference a secret without embedding it. Flagging them would train people to
disable the scanner.

The report never prints a secret value: findings carry path:line + a redacted
fingerprint (length + entropy), enough to locate, not enough to re-leak.

Some overlap with leakscan is intentional (both catch private-key headers, AWS
key ids, JWTs) — the tools have different *purposes* and are each self-contained
so a peer can copy either one alone. The small plumbing duplication (staged
diff, ignore globs, file iteration) is the price of that zero-coupling; if a
third scanner ever lands, factor a shared base then, not speculatively now.

Exit codes (fail-safe — anything but a clean scan is non-zero):
  0  clean
  1  findings (blocks the commit)
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import math
import os
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

# A line carrying this marker is intentionally exempt (e.g. a documented example
# credential, or a known-public test key). Keep the reason on the same line.
ALLOW_MARKER = "secretscan:allow"

# Paths never worth scanning — binary/vendored/VCS noise. Repo-specific globs
# come from .secretscanignore at the scan root.
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache", "dist",
                  "build", ".idea", ".vscode"}

# The key-name half of the ASSIGNED-secret heuristic: a word that means "this is
# a credential". Bounded so `password`, `api_key`, `client-secret`, `authToken`
# all hit but plain `key`/`id` (too generic, huge FP) do not.
SECRET_KEY_RX = re.compile(
    r"(?i)\b("
    r"pass(?:word|wd|phrase)?"
    r"|secret(?:[_-]?key)?"
    r"|token"
    r"|api[_-]?key|apikey"
    r"|access[_-]?key"
    r"|auth(?:[_-]?token)?"
    r"|client[_-]?secret"
    r"|private[_-]?key"
    r"|credentials?"
    r"|bearer"
    r")\b\s*[:=]\s*[\"']?([^\s\"'`,;:]{6,})")
# The value class excludes ':' so a doc line like `secret: foo: !secret x` stops
# at the field name (a code ref, rejected) rather than swallowing the colon; real
# secrets don't carry ':' (auth/connection strings are the basic-auth-url rule).

# Values that are indirections or placeholders, never a real secret. Checked
# case-insensitively; a substring match is enough for the templating markers.
PLACEHOLDER_SUBSTRINGS = (
    "example", "changeme", "change-me", "change_me", "placeholder", "redacted",
    "your-", "your_", "yourtoken", "yourkey", "my-secret", "dummy", "sample",
    "xxxxxx", "todo", "fixme", "notreal", "fake", "test-token", "test_token",
    "******", "……", "...", "<", ">", "{{", "}}", "${", "$(", "%(",
)
PLACEHOLDER_EXACT = frozenset({
    "none", "null", "nil", "undefined", "true", "false", "password", "secret",
    "token", "changeit", "admin", "root", "test", "", "-", "n/a", "na",
})

# The safe secret-indirection patterns. A value starting like this is a
# *reference* to a secret store, not the secret — the pattern we WANT people to
# use. Never flag it.
INDIRECTION_RX = re.compile(r"""^(?:
      !\s*secret\b        # tiki / RouterOS / YAML  !secret foo
    | \$\{                # ${VAR} / ${{ ci }}
    | \$\(                # $(command)
    | \$[A-Za-z_]         # $VAR
    | %\(                 # %(python)s
    | <[^>]+>             # <placeholder>
    | \{\{                # {{ template }}
    | @@                  # sops / templating sentinel
    | env:                # env:FOO
    | vault:              # vault:path
    | sops:               # sops:...
)""", re.VERBOSE)


@dataclass(frozen=True)
class Pattern:
    name: str
    severity: str  # "high" | "medium" — advisory; any hit still blocks
    regex: "re.Pattern[str]"


def _p(name: str, severity: str, rx: str, flags: int = 0) -> Pattern:
    return Pattern(name, severity, re.compile(rx, flags))


# NAMED credential formats — unambiguous by construction, so they flag on shape
# alone. Ordered by how self-evidently they are a secret.
NAMED: list[Pattern] = [
    _p("private-key-header", "high",
       r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"),
    _p("pgp-private-key", "high", r"-----BEGIN PGP PRIVATE KEY BLOCK-----"),  # secretscan:allow: this is the detection pattern, not a key
    _p("aws-access-key-id", "high", r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    _p("github-token", "high",
       r"\bgh[posru]_[A-Za-z0-9]{36,}\b|\bgithub_pat_[0-9A-Za-z_]{22,}\b"),
    _p("slack-token", "high", r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b"),
    _p("slack-webhook", "high",
       r"https://hooks\.slack\.com/services/[A-Za-z0-9/]+"),
    _p("google-api-key", "high", r"\bAIza[0-9A-Za-z_-]{35}\b"),
    _p("gcp-oauth-secret", "medium", r"\bGOCSPX-[0-9A-Za-z_-]{20,}\b"),
    _p("stripe-key", "high", r"\b[rsp]k_(?:live|test)_[0-9A-Za-z]{20,}\b"),
    _p("anthropic-key", "high", r"\bsk-ant-[A-Za-z0-9-]{20,}\b"),
    _p("openai-key", "high", r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    _p("npm-token", "high", r"\bnpm_[A-Za-z0-9]{36}\b"),
    _p("twilio-key", "high", r"\bSK[0-9a-fA-F]{32}\b"),
    _p("sendgrid-key", "high", r"\bSG\.[A-Za-z0-9_-]{16,}\.[A-Za-z0-9_-]{16,}\b"),
    _p("jwt", "high",
       r"\beyJ[A-Za-z0-9_-]{6,}\.eyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}"),
    _p("basic-auth-url", "high",
       r"\b[a-zA-Z][a-zA-Z0-9+.-]*://[^/\s:@]+:[^/\s:@]{4,}@"),
]

# The context-free high-entropy net. Requires mixed character classes (lower +
# upper + digit) which excludes the two biggest false-positive families —
# single-case hex hashes (git SHAs, sha256 checksums) and ALL-CAPS constants.
# `/` is deliberately NOT in the class: it is the URL/path separator, and
# including it turned every long URL path into a false hit. A standard-base64
# secret (which uses `/`) is caught by assignment context or a vendor format
# instead; base64url tokens (the modern default) use `-_` and still match.
HIGH_ENTROPY_RX = re.compile(r"(?<![A-Za-z0-9+=_-])[A-Za-z0-9+_-]{32,}={0,2}(?![A-Za-z0-9+=_-])")
HIGH_ENTROPY_MIN = 4.0        # bits/char; random base64 sits ~5.0, prose ~3-4
ASSIGNED_ENTROPY_MIN = 3.0    # assigned values get context, so a lower bar

# A line naming PUBLIC key material — a public key or certificate is meant to be
# shared, so its high-entropy body is not a secret. Suppress the entropy net on
# these lines. Private-key indicators are deliberately absent: a `private_key:`
# line must still flag.
PUBLIC_KEY_RX = re.compile(
    r"(?i)\b(?:ssh-(?:ed25519|rsa|dss)|ecdsa-sha2[\w-]*|public[_-]?key|pubkey"
    r"|sshkey|authorized_keys)\b"
    r"|-----BEGIN (?:PUBLIC KEY|CERTIFICATE|[A-Z ]*PUBLIC)")

# A value that is a code reference — a bare/dotted identifier or a function call
# — is a variable, not a literal secret. `password=admin_password`,
# `self.conn.password`, `get_secret()` are the dominant false positives in real
# source. Identifier-shaped values are rejected UNLESS they carry the mixed
# upper+lower+digit signature of real key material (so `Gk8xQvie2mNfR7pL` stays).
IDENTIFIER_RX = re.compile(r"[A-Za-z_][A-Za-z0-9_.]*$")


@dataclass
class Finding:
    path: str
    line: int
    rule: str
    kind: str          # "named" | "assigned" | "entropy"
    severity: str
    excerpt: str       # redacted — locates the hit, never re-leaks it


def shannon(s: str) -> float:
    if not s:
        return 0.0
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())


def redact(value: str, kind: str) -> str:
    """A fingerprint precise enough to locate, useless to re-leak. For a named
    token we keep the recognisable prefix (e.g. `AKIA…`, already public-shaped);
    for entropy/assigned hits we surface only length + entropy."""
    if kind == "named":
        head = value[:4]
        return f"{head}… ({len(value)} chars)"
    return f"<{len(value)} chars, entropy {shannon(value):.1f}>"


def _has_mixed_classes(s: str) -> bool:
    return (any(c.islower() for c in s)
            and any(c.isupper() for c in s)
            and any(c.isdigit() for c in s))


def _is_placeholder(value: str) -> bool:
    low = value.lower()
    if low in PLACEHOLDER_EXACT:
        return True
    if any(sub in low for sub in PLACEHOLDER_SUBSTRINGS):
        return True
    # a run of one repeated character (xxxx, ****, ----) is never a real secret
    if len(set(value)) <= 1:
        return True
    return False


def _is_indirection(value: str) -> bool:
    return INDIRECTION_RX.match(value) is not None


def _looks_like_path(value: str) -> bool:
    # `private_key = /etc/ssl/server.key` names a file, not a secret.
    return ("/" in value and re.search(r"\.[A-Za-z0-9]{1,6}$", value) is not None
            and " " not in value and not value.startswith("http"))


def _looks_like_code_ref(value: str) -> bool:
    """A variable reference, attribute access or call — not a literal secret."""
    if "(" in value or ")" in value:
        return True
    # a bare or dotted identifier that lacks the mixed-class signature of key
    # material (admin_password, self.conn.password) — but NOT a mixed-class token
    # that merely happens to be alphanumeric (Gk8xQvie2mNf, a real secret shape)
    if IDENTIFIER_RX.match(value) and not _has_mixed_classes(value):
        return True
    return False


def _assigned_is_secret(value: str) -> bool:
    if len(value) < 6:
        return False
    if _is_placeholder(value) or _is_indirection(value) or _looks_like_path(value):
        return False
    if _looks_like_code_ref(value):
        return False
    # A value with whitespace-free high entropy, or mixed classes at length, is
    # credential-shaped. Short dictionary words assigned to `password=` are
    # weak/example creds, not the leak class this gate is for.
    if shannon(value) >= ASSIGNED_ENTROPY_MIN and (len(value) >= 12 or _has_mixed_classes(value)):
        return True
    return False


def scan_text(path: str, text: str,
              disabled: frozenset[str] = frozenset()) -> list[Finding]:
    findings: list[Finding] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if ALLOW_MARKER in line:
            continue

        for pat in NAMED:
            if pat.name in disabled:
                continue
            for m in pat.regex.finditer(line):
                findings.append(Finding(path, lineno, pat.name, "named",
                                        pat.severity, redact(m.group(0), "named")))

        if "assigned" not in disabled:
            for m in SECRET_KEY_RX.finditer(line):
                value = m.group(2)
                if _assigned_is_secret(value):
                    findings.append(Finding(path, lineno, "assigned-secret",
                                            "assigned", "high",
                                            redact(value, "assigned")))

        if "high-entropy" not in disabled and not PUBLIC_KEY_RX.search(line):
            for m in HIGH_ENTROPY_RX.finditer(line):
                span = m.group(0)
                if (_has_mixed_classes(span) and not _is_placeholder(span)
                        and shannon(span) >= HIGH_ENTROPY_MIN):
                    findings.append(Finding(path, lineno, "high-entropy",
                                            "entropy", "medium",
                                            redact(span, "entropy")))
    # A named/assigned hit and a bare entropy hit often fire on the same token;
    # keep the more specific one so the report isn't doubled.
    return _dedupe_same_span(findings)


def _dedupe_same_span(findings: list[Finding]) -> list[Finding]:
    by_line: dict[int, list[Finding]] = {}
    for f in findings:
        by_line.setdefault(f.line, []).append(f)
    kept: list[Finding] = []
    for line_findings in by_line.values():
        has_specific = any(f.kind in ("named", "assigned") for f in line_findings)
        for f in line_findings:
            if f.kind == "entropy" and has_specific:
                continue
            kept.append(f)
    return kept


def _looks_binary(data: bytes) -> bool:
    return b"\x00" in data[:8192]


ALL_RULES = frozenset({p.name for p in NAMED} | {"assigned", "high-entropy"})


def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".secretscanignore"
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


def iter_files(paths: list[Path], root: Path, globs: list[str]):
    for base in paths:
        if base.is_file():
            files = [base]
        else:
            files = [p for p in base.rglob("*")
                     if p.is_file() and not (SKIP_DIR_NAMES & set(p.parts))]
        for p in files:
            try:
                rel = str(p.relative_to(root))
            except ValueError:
                rel = str(p)
            if _ignored(rel, globs):
                continue
            yield p, rel


def scan_paths(paths: list[Path], root: Path,
               disabled: frozenset[str] = frozenset()) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p, rel in iter_files(paths, root, globs):
        data = p.read_bytes()
        if _looks_binary(data):
            continue
        findings.extend(scan_text(rel, data.decode("utf-8", errors="replace"),
                                  disabled))
    return findings


def staged_added_lines() -> dict[str, str]:
    """Path → the added-line text of the staged diff. Scans only what a commit
    would introduce (the pre-commit hot path), not the whole tree.
    R is in the filter deliberately (review B4): git detects renames by
    default, and a renamed-AND-edited file's added lines are exactly as
    leak-capable as a modified file's — ACM alone silently skipped them."""
    out = subprocess.run(
        ["git", "diff", "--cached", "--unified=0", "--no-color",
         "--diff-filter=ACMR"],
        capture_output=True, text=True, check=True).stdout
    files: dict[str, list[str]] = {}
    current: str | None = None
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            current = line[len("+++ b/"):]
            files.setdefault(current, [])
        elif line.startswith("+") and not line.startswith("+++") and current:
            files[current].append(line[1:])
    return {path: "\n".join(lines) for path, lines in files.items() if lines}


def render_human(findings: list[Finding]) -> str:
    lines: list[str] = []
    if not findings:
        lines.append("✓ secretscan clean — no credentials in the scanned lines.")
        return "\n".join(lines)
    lines.append(f"✗ secretscan: {len(findings)} finding(s) — commit blocked.\n")
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.severity}/{f.kind}] {f.rule} → {f.excerpt}")
    lines.append("\n  A true positive: remove the secret, move it to the secret store")
    lines.append("  (e.g. a `!secret`/env reference), and ROTATE it — commit history is forever.")
    lines.append(f"  A false positive: append '# {ALLOW_MARKER}: <reason>' to the line,")
    lines.append("  or add a path glob to .secretscanignore.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="secretscan",
        description="Scan for plaintext credentials before they reach git history.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo, or --staged)")
    ap.add_argument("--staged", action="store_true",
                    help="scan only lines added in the git staging area (pre-commit hook)")
    ap.add_argument("--root", default=".",
                    help="repo root for relative paths/.secretscanignore")
    ap.add_argument("--disable", default="",
                    help="comma-separated rules to skip (named rule, 'assigned', "
                         "or 'high-entropy'). Use to quiet a noisy generic rule "
                         "while keeping the high-confidence vendor formats.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()

    disabled = frozenset(r.strip() for r in args.disable.split(",") if r.strip())
    unknown = disabled - ALL_RULES
    if unknown:
        print(f"secretscan: unknown rule(s) in --disable: {', '.join(sorted(unknown))}",
              file=sys.stderr)
        return 2

    if args.staged:
        try:
            staged = staged_added_lines()
        except subprocess.CalledProcessError as e:
            print(f"secretscan: git diff failed: {e}", file=sys.stderr)
            return 2
        prefixes = tuple(p.rstrip("/") + "/" for p in args.paths)
        if prefixes:
            staged = {path: text for path, text in staged.items()
                      if path.startswith(prefixes) or path in args.paths}
        globs = load_ignore_globs(root)
        findings = [f for path, text in staged.items() if not _ignored(path, globs)
                    for f in scan_text(path, text, disabled)]
    else:
        targets = [Path(p) for p in (args.paths or [str(root)])]
        findings = scan_paths(targets, root, disabled)

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        print(render_human(findings))

    return 1 if findings else 0


def _selftest() -> int:
    """Smoke test so `secretscan --selftest` proves the engine on any box, even
    where the unittest file isn't shipped. Fixtures are fictional/example
    credentials — the shapes are the point."""
    should_flag = [
        "aws_key = AKIAIOSFODNN7EXAMPLE",                       # secretscan:allow / leakscan:allow: selftest fixture
        "-----BEGIN OPENSSH PRIVATE KEY-----",                  # secretscan:allow / leakscan:allow: selftest fixture
        "github: ghp_012345678901234567890123456789abcdef",    # secretscan:allow: selftest fixture
        'password = "Gk8xQvie2mNfR7pLzW3dTaHb"',                # secretscan:allow: selftest fixture
        "slack xoxb-1234567890-abcdefghijklmno",                # secretscan:allow: selftest fixture
    ]
    should_pass = [
        "password = changeme",                     # placeholder
        "api_key = ${API_KEY}",                    # env indirection
        'psk = "!secret wg_home"',                 # tiki secret reference
        "private_key = /etc/ssl/server.key",       # a path, not a secret
        "commit 9f3a1c2b4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f90",  # git SHA (single-case hex)
        "version = 1.2.3",                         # not a secret
        "token = abc  # secretscan:allow: doc example",
    ]
    ok = True
    for text in should_flag:
        if not scan_text("t", text):
            print(f"FAIL (expected a finding): {text!r}")
            ok = False
    for text in should_pass:
        fs = scan_text("t", text)
        if fs:
            print(f"FAIL (expected clean): {text!r} → {[f.rule for f in fs]}")
            ok = False
    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
