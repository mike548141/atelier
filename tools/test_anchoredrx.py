"""Tests for anchoredrx (`160/720`, GT1): the linear-time stand-ins for the
three greedy-run regexes must find exactly what the originals find, and must
not restart a run at every word boundary.

Every value is synthetic."""

import random
import re
import time
import unittest

import anchoredrx
import leakscan as ls
import secretscan as ss

# (label, wrapper, a token alphabet that exercises its boundaries)
CASES = []


def _case(label, wrapper):
    CASES.append((label, wrapper))


_case("leakscan email", ls.BY_NAME["email"].regex)
_case("secretscan basic-auth-url",
      next(p for p in ss.NAMED if p.name == "basic-auth-url").regex)
_case("secretscan URL_RX", ss.URL_RX)

# The fixtures below are assembled around AT so this file carries no literal
# address or credential-shaped URL for the boundary guards to flag.
AT = "@"

TOKENS = ["a", "B", "1", "-", ".", "_", "@", "://", ":", "/", " ", "sk-", "eyJ.",
          "x" + AT + "y.com", "http://u:pass1" + AT + "h.io", "é", "%", "+", "com", "org",
          "u:pw123", "\t", "<", '"', "?", "#"]


def spans(rx, line):
    return [(m.start(), m.end(), m.group(0)) for m in rx.finditer(line)]


class Equivalence(unittest.TestCase):
    """The wrapper yields the original's matches: same spans, same order."""

    def test_fuzzed_lines_match_the_original_exactly(self):
        rng = random.Random(720)
        for label, wrapper in CASES:
            original = wrapper.original
            with self.subTest(label):
                for _ in range(20000):
                    line = "".join(rng.choice(TOKENS)
                                   for _ in range(rng.randint(0, 14)))
                    self.assertEqual(spans(original, line), spans(wrapper, line),
                                     repr(line))

    def test_adjacent_matches_keep_the_originals_non_overlap_rule(self):
        # The second address starts inside the run the first one ended in.
        line = "a" + AT + "b.com.x" + AT + "y.org"
        wrapper = ls.BY_NAME["email"].regex
        self.assertEqual(spans(wrapper.original, line), spans(wrapper, line))
        self.assertEqual(2, len(spans(wrapper, line)))

    def test_word_boundary_context_is_the_real_preceding_character(self):
        wrapper = ls.BY_NAME["email"].regex
        for line in ("_ab" + AT + "x.com", "-foo" + AT + "x.com",
                     "é.a" + AT + "b.co", "x -a" + AT + "b.co",
                     "..." + AT + "b.co", "1.2.3" + AT + "b.co",
                     "a-" + AT + "b.co", AT + "b.co", "a" + AT):
            self.assertEqual(spans(wrapper.original, line), spans(wrapper, line),
                             repr(line))

    def test_a_scheme_needs_a_letter_to_start(self):
        wrapper = ss.URL_RX
        for line in ("1://x.y/z", "1a://x.y/z", "-a://x.y/z", "a+b://h.io/p",
                     "x 9.8.7://h.io", "://h.io", "a://"):
            self.assertEqual(spans(wrapper.original, line), spans(wrapper, line),
                             repr(line))

    def test_search_and_the_pattern_attributes_follow_the_original(self):
        wrapper = ls.BY_NAME["email"].regex
        self.assertEqual(wrapper.pattern, wrapper.original.pattern)
        self.assertEqual(wrapper.flags, wrapper.original.flags)
        self.assertIsNone(wrapper.search("no address here"))
        self.assertEqual("a.b" + AT + "c.io", wrapper.search("x a.b" + AT + "c.io y").group(0))

    def test_the_wrappers_return_real_match_objects(self):
        wrapper = next(p for p in ss.NAMED if p.name == "basic-auth-url").regex
        m = wrapper.search("db postgres://admin:hunter22" + AT + "host")
        self.assertEqual("postgres://admin:hunter22" + AT, m.group(0))
        self.assertIs(m.re, wrapper.original)


class Linear(unittest.TestCase):
    """A line of short boundary-rich runs, with and without the trailing
    literal that used to re-open the quadratic path. Linear work grows 4x for
    4x the input; the originals grow about 16x. The bound is generous (10x)
    because a loaded machine adds noise, but sits well below quadratic."""

    SHAPES = ("1-", "sk-", "eyJ.", "a.", "1.")
    TAILS = ("", "@", "://", "://x:y", "](")

    @staticmethod
    def best(fn, line, runs=3):
        out = []
        for _ in range(runs):
            t = time.perf_counter()
            for _m in fn(line):
                pass
            out.append(time.perf_counter() - t)
        return min(out)

    def test_cost_grows_linearly_with_the_line(self):
        small, big = 10_000, 40_000
        for label, wrapper in CASES:
            for shape in self.SHAPES:
                for tail in self.TAILS:
                    a = shape * (small // len(shape)) + tail
                    b = shape * (big // len(shape)) + tail
                    ta = self.best(wrapper.finditer, a)
                    tb = self.best(wrapper.finditer, b)
                    with self.subTest(label=label, shape=shape, tail=tail):
                        self.assertLessEqual(
                            tb, max(10 * ta, 0.05),
                            f"{ta:.4f}s -> {tb:.4f}s for 4x the input")

    def test_the_originals_really_are_quadratic_on_this_shape(self):
        """The oracle must fail the same bound, or the test proves nothing."""
        original = ls.BY_NAME["email"].regex.original
        ta = self.best(original.finditer, "1-" * 4_000 + "@", runs=2)
        tb = self.best(original.finditer, "1-" * 16_000 + "@", runs=1)
        self.assertGreater(tb, 8 * ta, f"{ta:.4f}s -> {tb:.4f}s")

    def test_a_one_megabyte_hostile_line_finishes_quickly(self):
        # The probe that took more than ten minutes before the fix.
        line = "1-" * 500_000 + "@"
        t = time.perf_counter()
        for _label, wrapper in CASES:
            list(wrapper.finditer(line))
        self.assertLess(time.perf_counter() - t, 30)

    def test_a_scan_of_a_long_hostile_line_is_bounded_end_to_end(self):
        line = "sk-" * 20_000 + "@"
        t = time.perf_counter()
        ls.scan_lines("p", [(1, line)], [])
        ss.scan_lines("p", [(1, line + "://x:y")])
        self.assertLess(time.perf_counter() - t, 20)


if __name__ == "__main__":
    unittest.main()
