"""The single-sourced allow-marker grammar and ignore-file loader shared by the
scanners (`115/080`, part 2; the GA1 finding).

Before this module each scanner carried its own copy of two mechanisms:

  * the reasoned allow-marker regex plus its `parse_allow` reader
    (`<scanner>:allow[:<scope>]: <reason>`), at fourteen regex sites across
    twelve files; and
  * the reason-required `.<scanner>ignore` loader, its `_ignored` glob test
    and its `IgnoreFileError`, eleven textually identical copies.

On 2026-08-09 a change to shared parsing, applied copy by copy, silently
voided nine live allow-markers across three child repos — and a voided marker
reads exactly like an absent one. Single-sourcing is the upstream fix.

WHAT THIS MODULE DELIBERATELY DOES NOT DO: unify behaviour. The scanners'
acceptance rules differ on purpose or by history, and every difference is a
PARAMETER here, never a default someone can drift into:

  * `scope`   — None (the marker takes no sub-scope), "one" (one optional
                `:<name>` scope) or "list" (comma-joined names; `leakscan`).
  * `group`   — the regex group name (`rule` or `kind`); cosmetic to callers
                but kept so each scanner's compiled pattern is byte-identical
                to what it carried before.
  * `sep`     — what may sit between the colon and the reason: `[ \\t]*`
                (same line only) or `\\s*` (may cross a newline).
  * `named_reason` — whether the reason's first character is a named group.

The reason's first character must be a word character or an opening quote;
that rule is not a parameter because every scanner already shared it, and a
marker inside its own HTML comment (`<!-- x:allow: -->`) must not mistake the
comment closer for a reason (DSR8).

Each scanner keeps its own `ALLOW_MARKER` constant, its own `parse_allow`
wrapper and its own result type (str / frozenset / bool); only the mechanism
is shared. `tools/test_allowmarker.py` pins every parameter combination.
"""

from __future__ import annotations

import fnmatch
import re
from pathlib import Path

# First character of a reason: a word character or an opening quote.
REASON_START = r"[\w\"\'“‘]"

_SCOPE_ONE = r"[A-Za-z0-9_-]+"
_SCOPE_LIST = r"[A-Za-z0-9_-]+(?:,[A-Za-z0-9_-]+)*"

SEP_SAME_LINE = r"[ \t]*"
SEP_ANY_SPACE = r"\s*"


def marker_rx(marker: str, *, scope: str | None = None, group: str = "kind",
              sep: str = SEP_SAME_LINE, named_reason: bool = True) -> "re.Pattern[str]":
    """Compile the reasoned allow-marker pattern for `marker`
    (e.g. `"datescan:allow"`), word-boundary anchored, colon then a
    non-empty reason."""
    if scope is None:
        scope_part = ""
    elif scope == "one":
        scope_part = r"(?::(?P<" + group + r">" + _SCOPE_ONE + r"))?"
    elif scope == "list":
        scope_part = r"(?::(?P<" + group + r">" + _SCOPE_LIST + r"))?"
    else:
        raise ValueError(f"unknown scope mode: {scope!r}")
    reason = (r"(?P<reason>" + REASON_START + r")") if named_reason else REASON_START
    return re.compile(r"\b" + re.escape(marker) + scope_part + r":" + sep + reason)


def present(rx: "re.Pattern[str]", text: str) -> bool:
    """True if `text` carries a reasoned marker (the unscoped readers)."""
    return rx.search(text) is not None


def scope_of(rx: "re.Pattern[str]", text: str, group: str = "kind") -> str | None:
    """The marker's scope, `""` for the unscoped form, None when there is no
    reasoned marker. Needs a `scope="one"` pattern built with the same
    `group`."""
    m = rx.search(text)
    if not m:
        return None
    return m.group(group) or ""


def scopes_of(rx: "re.Pattern[str]", text: str, group: str = "rule") -> frozenset[str] | None:
    """As `scope_of` for a `scope="list"` pattern: the named scopes as a
    frozenset (empty for the unscoped form), None when there is no marker."""
    m = rx.search(text)
    if not m:
        return None
    names = m.group(group)
    return frozenset(names.split(",")) if names else frozenset()


class IgnoreFileError(ValueError):
    """An ignore file granted an exemption with no reason stated anywhere."""

    def __init__(self, filename: str, entries: list[tuple[int, str]]):
        self.filename = filename
        self.entries = entries
        detail = "; ".join(f"line {n}: '{g}'" for n, g in entries)
        super().__init__(
            f"{filename}: {len(entries)} glob(s) with no stated reason — "
            f"{detail}. Every exemption states its reason where a reviewer "
            f"reads it (method/GUARDS.md): put a comment above the stanza, or "
            f"a trailing '# reason' on the line.")


def load_ignore_globs(root: Path, filename: str) -> list[str]:
    """Globs from `<root>/<filename>`, each of which MUST carry a stated reason.

    GUARDS.md rule (c): an ignore glob is the widest allowance a scanner
    grants — a whole path, every rule, indefinitely — so it is the last place
    an unexplained exemption should be possible. A glob is reasoned if it
    carries a trailing `# reason` (publishscan's form) OR sits under a comment
    block in its own stanza. A blank line ends a stanza, so a bare glob under
    no comment at all is refused.

    An unreasoned glob is a CONFIG ERROR, not a warning: raised as
    `IgnoreFileError`, which callers surface as exit 2 — a broken scan is not
    a pass. An absent file is not an error: no globs."""
    f = root / filename
    if not f.exists():
        return []
    globs: list[str] = []
    unreasoned: list[tuple[int, str]] = []
    stanza_reason = False
    for n, raw in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw.strip()
        if not line:
            stanza_reason = False
            continue
        if line.startswith("#"):
            stanza_reason = True
            continue
        glob, _, trailing = line.partition("#")
        glob = glob.strip()
        if not glob:
            continue
        if not trailing.strip() and not stanza_reason:
            unreasoned.append((n, glob))
        globs.append(glob)
    if unreasoned:
        raise IgnoreFileError(filename, unreasoned)
    return globs


def ignored(rel: str, globs: list[str]) -> bool:
    """True if repo-relative `rel` matches any glob, or sits under a glob
    treated as a directory (`g/` or `g`)."""
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)
