"""Linear-time stand-ins for three greedy-run regexes (`160/720`, GT1).

THE DEFECT. Three rules each begin with a greedy character class that must be
followed by a literal:

  leakscan   email            `\\b[A-Za-z0-9._%+-]+@…`
  secretscan basic-auth-url   `\\b[a-zA-Z][a-zA-Z0-9+.-]*://…:…@`
  secretscan URL_RX           `\\b[A-Za-z][A-Za-z0-9+.-]*://…`

The regex engine restarts the class run at EVERY word boundary and scans on to
the end of the run before it fails on the literal. On a line made of short
boundary-rich runs (`1-1-1-`, `sk-`, `eyJ.`) with no literal after them, cost
is O(n^2): about 22 minutes for a 1 MiB line, in a blocking hook. Python 3.9 is
the stdlib floor, so possessive quantifiers (3.11) are not available, and they
would not help in any case: the restarts, not the backtracking, are the cost.

THE FIX, exact rather than approximate. A match can only begin inside the one
maximal run of class characters that ends at the literal. So:

  1. enumerate the maximal runs once (`RUN.finditer`, linear);
  2. keep the runs the literal follows;
  3. in each, the match starts at the FIRST position that satisfies the
     pattern's own start condition (`\\b`, or `\\b` plus a letter) at or after
     both the run's start and the end of the previous match;
  4. try the ORIGINAL compiled pattern, anchored there, ONCE. If it fails, the
     tail after the literal failed, and no other start in that run can do
     better - the tail does not depend on the start.

So a run costs O(run) once, not once per boundary. The result is the same
match objects the original `finditer` yields, in the same order: step 3
inherits the original's non-overlap rule and its `\\b` context (the lookbehind
sees the real preceding character because the search uses `pos`, never a
slice). `test_anchoredrx.py` proves the equivalence against the original
pattern on a fuzzed corpus, including adjacent matches.

Stdlib only, so it can sit beside the scanners that import it.
"""

from __future__ import annotations

import re
from typing import Iterator


class AnchoredRx:
    """Drop-in for the `.finditer`/`.search` of a compiled pattern shaped
    `START RUN LITERAL TAIL`.

    `original` is the compiled pattern, kept as the single statement of what
    matches; `run` matches ONE maximal run of the leading class; `literal` is
    the text that must follow the run; `start` finds the first valid start
    position (it is searched with `pos`/`endpos`, so it sees real context)."""

    def __init__(self, original: "re.Pattern[str]", run: str, literal: str,
                 start: str) -> None:
        self.original = original
        self._run = re.compile(run)
        self._literal = literal
        self._start = re.compile(start)

    # The attributes callers and tests read off a compiled pattern.
    @property
    def pattern(self) -> str:
        return self.original.pattern

    @property
    def flags(self) -> int:
        return self.original.flags

    def finditer(self, line: str) -> Iterator["re.Match[str]"]:
        pos = 0
        for run in self._run.finditer(line):
            end = run.end()
            if end < pos or not line.startswith(self._literal, end):
                continue
            first = self._start.search(line, max(run.start(), pos), end)
            if first is None or first.start() >= end:
                continue
            m = self.original.match(line, first.start())
            if m is None:
                continue
            yield m
            pos = m.end()

    def search(self, line: str) -> "re.Match[str] | None":
        return next(self.finditer(line), None)
