"""Test support: derive sample lines from a compiled regex (`160/720`, GT2).

A gate is a cheap necessary condition for a rule, and the suite proves it
necessary by showing it passes every line the rule matches. That proof is only
as good as the lines. A hand-kept corpus covers a rule per RULE, so a regex
widened under the same name (a second key prefix, a new IPv6 form) leaves the
old gate rejecting the new shape while the suite stays green.

This module removes the maintainer from that loop: `samples(rx)` walks the
regex's own parse tree and builds lines from it, one per alternative of every
alternation (at any depth), so a branch added to a rule is exercised the day it
is added. It needs Python 3.11+ (`re._parser`), like the rest of the tests.

Not a general regex fuzzer: it builds the SHORTEST sample per choice (repeats at
their minimum, and once above it), ignores lookarounds and anchors (the caller
checks that a sample really matches before trusting it), and does not follow
back-references.
"""

import re
import unittest

try:                                    # 3.11+
    import re._parser as _sre
    import re._constants as _c
except ImportError:                     # pragma: no cover - older interpreters
    import sre_parse as _sre
    import sre_constants as _c

_CATEGORY_CHAR = {
    _c.CATEGORY_DIGIT: "1", _c.CATEGORY_NOT_DIGIT: "a",
    _c.CATEGORY_SPACE: " ", _c.CATEGORY_NOT_SPACE: "a",
    _c.CATEGORY_WORD: "a", _c.CATEGORY_NOT_WORD: " ",
}
_FALLBACKS = "aZ0 .-_:@/é"


def _in_chars(items) -> list[str]:
    """Every character class member we can name (a few per range)."""
    negate = any(op is _c.NEGATE for op, _ in items)
    members: list[str] = []
    for op, av in items:
        if op is _c.LITERAL:
            members.append(chr(av))
        elif op is _c.RANGE:
            lo, hi = av
            members.extend(chr(x) for x in {lo, (lo + hi) // 2, hi})
        elif op is _c.CATEGORY:
            members.append(_CATEGORY_CHAR.get(av, "a"))
    if negate:
        banned = set(members)
        return [ch for ch in _FALLBACKS if ch not in banned][:1] or ["~"]
    return members or ["a"]


class _Gen:
    """Builds samples, forcing one alternative at one alternation at a time."""

    def __init__(self):
        self.branch_ids: list[int] = []   # alternations met, in walk order

    def build(self, parsed, force: dict[int, int], extra_repeat: bool) -> str:
        self.branch_ids = []
        return self._seq(parsed, force, extra_repeat)

    def _seq(self, seq, force, extra) -> str:
        out = []
        for op, av in seq:
            out.append(self._node(op, av, force, extra))
        return "".join(out)

    def _node(self, op, av, force, extra) -> str:
        if op is _c.LITERAL:
            return chr(av)
        if op is _c.NOT_LITERAL:
            return "b" if av == ord("a") else "a"
        if op is _c.ANY:
            return "x"
        if op is _c.IN:
            lits = [chr(x) for o, x in av if o is _c.LITERAL]
            if 2 <= len(lits) <= 6 and len(lits) == len(av):
                # `(?:1|2)` compiles to the class `[12]`: still an alternation.
                idx = len(self.branch_ids)
                self.branch_ids.append(len(lits))
                return lits[force.get(idx, 0) % len(lits)]
            return _in_chars(av)[0]
        if op is _c.CATEGORY:
            return _CATEGORY_CHAR.get(av, "a")
        if op in (_c.MAX_REPEAT, _c.MIN_REPEAT) or op.name == "POSSESSIVE_REPEAT":
            lo, hi, sub = av
            n = lo + (1 if extra and hi > lo else 0)
            return "".join(self._seq(sub, force, extra) for _ in range(n))
        if op is _c.SUBPATTERN:
            return self._seq(av[-1], force, extra)
        if op.name == "ATOMIC_GROUP":
            return self._seq(av, force, extra)
        if op is _c.BRANCH:
            idx = len(self.branch_ids)
            self.branch_ids.append(len(av[1]))
            return self._seq(av[1][force.get(idx, 0) % len(av[1])], force, extra)
        return ""                         # AT, ASSERT, ASSERT_NOT, GROUPREF, ...


def samples(rx: "re.Pattern[str]") -> list[str]:
    """Lines built from `rx`: the default path, one per alternative of each
    alternation met on it (and on the paths those open), each with repeats at
    their minimum and once above it."""
    parsed = _sre.parse(rx.pattern, rx.flags)
    gen = _Gen()
    out: list[str] = []
    seen_forces: set[tuple] = set()
    queue: list[dict[int, int]] = [{}]
    while queue and len(seen_forces) < 400:
        force = queue.pop()
        key = tuple(sorted(force.items()))
        if key in seen_forces:
            continue
        seen_forces.add(key)
        for extra in (False, True):
            out.append(gen.build(parsed, force, extra))
        for idx, n in enumerate(gen.branch_ids):
            for alt in range(n):
                queue.append({**force, idx: alt})
    return list(dict.fromkeys(out))


def top_level_branches(pattern: str) -> list[str]:
    """The source text of each top-level alternative of `pattern`: split at a
    `|` outside every group and character class, honouring escapes."""
    out, depth, in_class, cur, i = [], 0, False, [], 0
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\":
            cur.append(pattern[i:i + 2])
            i += 2
            continue
        if in_class:
            in_class = ch != "]"
        elif ch == "[":
            in_class = True
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "|" and depth == 0:
            out.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    out.append("".join(cur))
    return out


class SamplesSelfTest(unittest.TestCase):
    def test_every_alternative_of_a_nested_alternation_is_produced(self):
        got = samples(re.compile(r"\bx(?:aa|bb|cc)y(?:1|2)\b"))
        for want in ("xaay1", "xbby1", "xccy1", "xaay2"):
            self.assertIn(want, got)

    def test_each_sample_matches_the_pattern_it_came_from(self):
        for src in (r"\bAKIA[0-9A-Z]{16}\b", r"\bgh[posru]_[A-Za-z0-9]{36,}\b",
                    r"(?<!\d)(?:\+64[\s-]?|0)(?:2\d|[3-9])[\s-]?\d{3}[\s-]?\d{3,4}(?!\d)"):
            rx = re.compile(src)
            ok = [s for s in samples(rx) if rx.search(s)]
            self.assertTrue(ok, src)

    def test_top_level_branches_split_only_outside_groups_and_classes(self):
        self.assertEqual(["a", "b[|]c", r"d\|e"],
                         top_level_branches(r"a|b[|]c|d\|e"))
        self.assertEqual(["(?:a|b)c"], top_level_branches("(?:a|b)c"))


if __name__ == "__main__":
    unittest.main()
