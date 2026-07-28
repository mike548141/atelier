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

# Paths never worth scanning. Hardcode-skip ONLY names that are never
# human-authored content — VCS, dependency, and tool-cache dirs. `build`/`dist`
# are DELIBERATELY absent (2026-07-11 child-CI-floor review, N1 — the same
# masking linkscan fixed at d0870a4): a content dir can legitimately share the
# name (atelier's own docs/build/ doctrine layer), and skipping it by name made
# a whole-tree scan blind to a planted key there. Masking a layer is the worst
# failure a publish-safety scanner has; a repo with a real build-output dir
# names it in `.secretscanignore` (one line). Repo-specific globs come from
# .secretscanignore at the scan root.
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

# The key-name half of the ASSIGNED-secret heuristic: a word that means "this is
# a credential". Bounded so `password`, `api_key`, `client-secret`, `authToken`
# all hit but plain `key`/`id` (too generic, huge FP) do not.
# The leading boundary is NOT a plain `\b`. `_` is a word character, so `\b`
# never matches between `REDIS` and `PASSWORD` — which silently exempted every
# prefixed environment variable (`REDIS_PASSWORD`, `POSTGRES_PASSWORD`,
# `DB_TOKEN`), the single most common shape a real credential takes in compose
# and `.env` files. Found 2026-07-28 with 15 live assignments unflagged across
# the estate. So: a word boundary, OR an underscore prefix, OR a camelCase hump
# (`redisPassword`). The hump is matched case-SENSITIVELY via `(?-i:…)` — under
# the pattern's global `(?i)` a case-insensitive lookbehind would also fire
# inside `BYPASS` and re-introduce the false positives `\b` was there to stop.
_LEAD = r"(?:\b|_|(?-i:(?<=[a-z0-9])(?=[A-Z])))"
SECRET_KEY_RX = re.compile(
    r"(?i)" + _LEAD + r"("
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
# case-insensitively; a substring match is enough for the word-shaped markers.
PLACEHOLDER_SUBSTRINGS = (
    "example", "changeme", "change-me", "change_me", "placeholder", "redacted",
    "your-", "your_", "yourtoken", "yourkey", "my-secret", "dummy", "sample",
    "xxxxxx", "todo", "fixme", "notreal", "fake", "test-token", "test_token",
    "******", "……", "...",
)

# Templating markers are NOT substring-matched. They used to be — `${`, `$(`,
# `%(`, `<`, `>`, `{{`, `}}` sat in the tuple above — and an OPENING marker
# occurring anywhere in a value was enough to write it off as a template. A
# randomly generated 60-char key that happened to contain the two characters
# `$(` was therefore exempted by coincidence, which is exactly how a real
# NetBox SECRET_KEY (entropy 5.29) went unflagged (found 2026-07-28). Requiring
# the marker to be CLOSED keeps genuine templates suppressed and makes chance
# collisions harmless: a real secret would have to contain the opener *and* a
# matching closer, with no intervening delimiter, to slip through.
TEMPLATE_RX = re.compile(
    r"\$\{[^{}]*\}"        # ${VAR}
    r"|\$\([^()]*\)"       # $(command)
    r"|%\([^()]*\)"        # %(python)s
    r"|\{\{[^{}]*\}\}"     # {{ template }}
    r"|<[^<>]{1,64}>"      # <placeholder>
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

# An absolute, multi-segment, path-shaped value — `/run/secrets/netbox_key`.
# Deliberately excludes the base64 padding/alphabet extras (`+`, `=`) so a
# standard-base64 secret cannot masquerade as a path on shape alone.
ABS_PATH_RX = re.compile(r"/(?:[A-Za-z0-9._@-]+/)+[A-Za-z0-9._@-]+")

# A code expression used as a value: `get_secret()`, `os.getenv("KEY")`,
# `inv.effective(device).factory_password`, `function(a){return`. Defined by its
# CHARACTER SET — code is built from identifiers, dots, calls, subscripts and
# braces. `{}` and `$` are in the set because JS puts them in ordinary
# expressions (`encodeShortlist({`, jQuery's `$`); omitting them flagged
# vendored minified JS as credentials. Random key material still fails the set:
# it carries `% # ! @ +`, which no identifier expression contains.
# `-` is admitted because prose fragments land here too — a comment reading
# `# without password= (live-proven 2026-07-04)` yields the value `(live-proven`.
# It stays safe because a value must ALSO contain a bracket to be called code,
# and the base64url alphabet (`A-Za-z0-9-_`) has no brackets at all.
CODE_EXPR_RX = re.compile(r"[A-Za-z0-9_.\-()\[\]{}$'\"]+")

# kebab-case is the same class of thing as snake_case: a slug or enum value
# (`yes-access-request`), not key material. IDENTIFIER_RX covers the snake form,
# but `-` is not an identifier character so the hyphenated twin needs saying.
# Deliberately letters-only — admitting digits would swallow lowercase hex
# secrets, which is a real (pre-existing) gap and not one to widen.
SLUG_RX = re.compile(r"[a-z]+(?:[-_][a-z]+)+")


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
    if TEMPLATE_RX.search(value):
        return True
    # a run of one repeated character (xxxx, ****, ----) is never a real secret
    if len(set(value)) <= 1:
        return True
    return False


def _is_indirection(value: str) -> bool:
    return INDIRECTION_RX.match(value) is not None


def _looks_like_path(value: str) -> bool:
    # `private_key = /etc/ssl/server.key` names a file, not a secret.
    if " " not in value and not value.startswith("http") and "/" in value:
        if re.search(r"\.[A-Za-z0-9]{1,6}$", value) is not None:
            return True
        # An EXTENSIONLESS mount path is the secret-store form we actively want
        # people to use (`/run/secrets/netbox_key`, a K8s projected volume). The
        # extension requirement above meant those flagged as high-severity
        # secrets — so following Docker's recommended pattern is what turned a
        # repo red, while the plaintext value on the next line stayed green
        # (found 2026-07-28). Recognise absolute, multi-segment, path-shaped
        # values; guard with the SAME mixed-class + entropy signature the
        # high-entropy net uses, so a standard-base64 blob that merely contains
        # `/` still flags rather than passing as a path.
        if ABS_PATH_RX.fullmatch(value):
            return not any(_has_mixed_classes(seg) and shannon(seg) >= HIGH_ENTROPY_MIN
                           for seg in value.strip("/").split("/"))
    return False


def _looks_like_code_ref(value: str) -> bool:
    """A variable reference, attribute access or call — not a literal secret."""
    # The mixed upper+lower+digit signature of key material wins over every code
    # shape below — `Gk8xQvie2mNf` is a secret even though it is identifier-
    # shaped. Hoisted to the top so it guards the call/expression branch too.
    if _has_mixed_classes(value):
        return False
    # Testing for a stray `(` or `)` ANYWHERE was the same unclosed-marker bug as
    # TEMPLATE_RX above: the real NetBox SECRET_KEY carries `(` and `)` among its
    # random symbols and was written off as a function call (found 2026-07-28).
    # Require the whole value to be code-SHAPED instead — and to actually contain
    # a call/attribute/subscript, so a bare word still falls through to the
    # identifier branch and its own reasoning.
    if CODE_EXPR_RX.fullmatch(value) and re.search(r"[.()\[\]{}]", value):
        return True
    if SLUG_RX.fullmatch(value):
        return True
    # a bare or dotted identifier that lacks the mixed-class signature of key
    # material (admin_password, self.conn.password) — but NOT a mixed-class token
    # that merely happens to be alphanumeric (Gk8xQvie2mNf, a real secret shape)
    if IDENTIFIER_RX.match(value):
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
            # Resolve BOTH sides so rel is root-relative no matter the caller's
            # CWD (2026-07-11 review N3): floor.yml runs `--root repo repo` from
            # the workspace, where the unresolved relative_to raised and the
            # fallback quietly produced CWD-relative paths — so the scanned
            # repo's own .secretscanignore globs never matched.
            try:
                rel = str(p.resolve().relative_to(root.resolve()))
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
        # An ABSOLUTE path here scans NOTHING and exits 0 — the silent-success
        # class (linkscan L1) this tool already closes for a missing path, found
        # again on 2026-07-25 while building tools/floor.py. git lists staged
        # paths repo-relative, so `/Users/…/repo/x.py` matches no prefix, the
        # filter empties the set, and a boundary scan that covered nothing looks
        # exactly like one that found nothing wrong. Refuse it.
        absolute = [p for p in args.paths if Path(p).is_absolute()]
        if absolute:
            print(f"secretscan: --staged needs repo-relative path(s), got absolute: "
                  f"{', '.join(absolute)}\n"
                  "  git lists staged paths relative to the repo root, so an "
                  "absolute path matches nothing\n"
                  "  and the scan would pass while covering nothing. Pass e.g. "
                  "'src/' instead.", file=sys.stderr)
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
        missing = [str(p) for p in targets if not p.exists()]
        if missing:
            # A typo'd path scanning nothing must never read as a clean pass —
            # the linkscan L1 silent-success class, closed here too
            # (2026-07-11 review N2).
            print(f"secretscan: path does not exist: {', '.join(missing)}",
                  file=sys.stderr)
            return 2
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
