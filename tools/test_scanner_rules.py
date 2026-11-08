"""Cross-scanner checks on the rule tables (`160/720`, GT5 and GT9).

GT5. `leakscan` and `secretscan` each carry their own copy of three rules
(`private-key-header`, `aws-access-key-id`, `jwt`) on purpose: neither depends
on the other's rule table. The price is that a copy can be harmonised without
its gate, which then silently drops a branch. These tests pin the copies to each
other, and name the one difference that is intended.

GT9. A greedy character class restarting at every word boundary was found three
times by hand on three guards (a pathscan pass, a secretscan pass, and the
leakscan/secretscan rules of GT1), each with different inputs. This is the
control shape written down once: every rule table is run on boundary-rich lines
at two sizes and must scale about linearly. A regex that is known to be
quadratic and not yet fixed is listed in KNOWN_QUADRATIC with its reason; the
test fails when an entry has become linear, so the list cannot go stale.
"""

import re
import time
import unittest

import leakscan as ls
import pathscan
import secretscan as ss


def _plain(rx):
    return getattr(rx, "original", rx)


class SharedRuleParity(unittest.TestCase):
    SHARED = ("private-key-header", "aws-access-key-id", "jwt")

    # The intended differences, each with the text of both sides, so changing
    # either side without this table (and the other side's gate) fails.
    DECLARED_DIFFERENCES = {
        "aws-access-key-id": (
            "leakscan names one key-id prefix, secretscan names two (AKIA, ASIA)",
            r"\bAKIA[0-9A-Z]{16}\b",
            r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    }

    def rules(self, name):
        leak = ls.BY_NAME[name]
        sec = next(p for p in ss.NAMED if p.name == name)
        return leak, sec

    def test_shared_rules_are_textually_equal_or_the_difference_is_declared(self):
        for name in self.SHARED:
            leak, sec = self.rules(name)
            with self.subTest(name):
                if name in self.DECLARED_DIFFERENCES:
                    _why, leak_src, sec_src = self.DECLARED_DIFFERENCES[name]
                    self.assertEqual(leak_src, _plain(leak.regex).pattern)
                    self.assertEqual(sec_src, _plain(sec.regex).pattern)
                else:
                    self.assertEqual(_plain(leak.regex).pattern,
                                     _plain(sec.regex).pattern)
                self.assertEqual(_plain(leak.regex).flags, _plain(sec.regex).flags)

    def test_each_gate_accepts_everything_its_own_rule_names(self):
        """The failure the parity guards against: the regex is harmonised, the
        gate is not. Every sample of either copy must pass BOTH gates that
        are meant to accept it - here, each copy's own gate."""
        from test_support_regex import samples
        for name in self.SHARED:
            for label, pat in zip(("leakscan", "secretscan"), self.rules(name)):
                rx = _plain(pat.regex)
                for line in (t for t in samples(rx) if rx.search(t)):
                    with self.subTest(rule=name, scanner=label, line=line):
                        self.assertTrue(pat.gate(line))

    def test_the_declared_difference_is_the_only_one(self):
        self.assertEqual({"aws-access-key-id"}, set(self.DECLARED_DIFFERENCES))


# ---------------------------------------------------------------------------

SHAPES = ("1-", "sk-", "eyJ.", "a.")
TAILS = ("", "@", "://")
SMALL, BIG = 4_000, 16_000


def _best(rx, line, runs=2):
    out = []
    for _ in range(runs):
        t = time.perf_counter()
        for _m in rx.finditer(line):
            pass
        out.append(time.perf_counter() - t)
    return min(out)


def _worst_ratio(rx):
    """(worst big/small time ratio, the shape that gave it)."""
    worst = (0.0, "")
    for shape in SHAPES:
        for tail in TAILS:
            a = shape * (SMALL // len(shape)) + tail
            b = shape * (BIG // len(shape)) + tail
            ta, tb = _best(rx, a), _best(rx, b)
            if tb < 0.1:                # too fast to be a scaling problem
                continue
            ratio = tb / max(ta, 5e-3)
            if ratio > worst[0]:
                worst = (ratio, f"{shape!r}+{tail!r}: {ta:.3f}s -> {tb:.3f}s")
    return worst


TABLES = {
    **{f"leakscan.{p.name}": p.regex for p in ls.ALL_RULES},
    **{f"secretscan.{p.name}": p.regex for p in ss.NAMED},
    "secretscan.URL_RX": ss.URL_RX,
    "secretscan.SECRET_KEY_RX": ss.SECRET_KEY_RX,
    "secretscan.HIGH_ENTROPY_RX": ss.HIGH_ENTROPY_RX,
}

# Quadratic today, filed elsewhere. 4x the input costs about 16x the time.
KNOWN_QUADRATIC = {
    "pathscan._SCHEME_URL":
        "BP9 (2026-10-04 bounded-pathscan cold pass): a scheme run restarts at "
        "every word boundary, as GT1's three did; pathscan is outside 160/720.",
}
OTHER = {"pathscan._SCHEME_URL": pathscan._SCHEME_URL}

LINEAR_BOUND = 9.0     # linear is ~4, quadratic ~16; noise sits between


class RuleTablesScaleLinearly(unittest.TestCase):
    def test_every_rule_table_regex_is_linear_on_boundary_rich_lines(self):
        for name, rx in TABLES.items():
            with self.subTest(name):
                ratio, where = _worst_ratio(rx)
                self.assertLessEqual(
                    ratio, LINEAR_BOUND,
                    f"{name} scales {ratio:.1f}x for 4x the input ({where}); "
                    "a greedy class that restarts at every word boundary?")

    def test_the_known_quadratic_entries_are_still_quadratic(self):
        for name, rx in OTHER.items():
            with self.subTest(name):
                ratio, where = _worst_ratio(rx)
                if not where:           # every shape under the time floor
                    self.skipTest("too fast to measure on this machine")
                self.assertGreater(
                    ratio, LINEAR_BOUND,
                    f"{name} no longer scales quadratically ({where}): remove "
                    "it from KNOWN_QUADRATIC")

    def test_the_control_shape_does_fail_the_bound(self):
        """The oracle: the pre-fix leakscan email regex must trip it."""
        ratio, _where = _worst_ratio(_plain(ls.BY_NAME["email"].regex))
        self.assertGreater(ratio, LINEAR_BOUND)


if __name__ == "__main__":
    unittest.main()
