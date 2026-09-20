"""Stdlib-only tests for memprobe (no pytest needed): `python3 -m unittest`.

Small and fast by design: this module is the harness OTHER tests build on
(`test_secretscan.py::BoundedMemory`, and every guard 020/380 eventually
points at it), so it needs its own quick proof of correctness independent of
any of them — a bug here would look like a bug in whatever it's measuring.
"""

import subprocess
import sys
import time
import unittest
from pathlib import Path

import memprobe


class RunAndMeasure(unittest.TestCase):
    def test_reports_exit_code_and_output(self):
        r = memprobe.run_and_measure(
            [sys.executable, "-c", "import sys; print('hi'); sys.exit(3)"],
            timeout=10)
        self.assertEqual(3, r.returncode)
        self.assertEqual(b"hi\n", r.stdout)
        self.assertFalse(r.timed_out)
        self.assertFalse(r.killed_over_limit)

    def test_reports_stderr_separately(self):
        r = memprobe.run_and_measure(
            [sys.executable, "-c", "import sys; sys.stderr.write('oops')"],
            timeout=10)
        self.assertEqual(b"oops", r.stderr)
        self.assertEqual(b"", r.stdout)

    def test_peak_rss_is_positive_and_plausible(self):
        # Any Python interpreter startup allocates at least a few MB and
        # well under a few hundred — a sanity range, not a precise claim.
        r = memprobe.run_and_measure([sys.executable, "-c", "pass"], timeout=10)
        self.assertGreater(r.peak_rss_bytes, 1 * 1024 * 1024)
        self.assertLess(r.peak_rss_bytes, 500 * 1024 * 1024)

    # The allocating child must TOUCH what it allocates. `bytearray(N)` is
    # zero-filled, and on Linux a large zeroed allocation is served by mmap'd
    # copy-on-write zero pages that never become resident until written — so
    # the child allocated 50 MB and `ru_maxrss` moved by nothing, while the
    # baseline run happened to peak slightly higher on interpreter startup.
    # That inverted the assertion and turned this repo's CI red on a Linux
    # runner while every macOS run passed (2026-09-20). Writing one byte per
    # 4 KiB page faults them in, which is what makes the measurement mean
    # "memory this process really held" on both platforms.
    TOUCHED_ALLOC = ("x = bytearray({n});"
                     " [x.__setitem__(i, 1) for i in range(0, len(x), 4096)]")

    def test_a_process_that_allocates_more_measures_higher(self):
        small = memprobe.run_and_measure(
            [sys.executable, "-c", "pass"], timeout=10)
        big = memprobe.run_and_measure(
            [sys.executable, "-c",
             self.TOUCHED_ALLOC.format(n=50 * 1024 * 1024)],
            timeout=30)
        self.assertGreater(big.peak_rss_bytes, small.peak_rss_bytes + 40 * 1024 * 1024)

    def test_timeout_kills_the_child_and_is_reported(self):
        start = time.monotonic()
        r = memprobe.run_and_measure(
            [sys.executable, "-c", "import time; time.sleep(30)"], timeout=0.3)
        elapsed = time.monotonic() - start
        self.assertTrue(r.timed_out)
        self.assertLess(elapsed, 10, "must not wait out the child's own sleep")

    def test_rss_limit_kills_the_child_and_is_reported(self):
        # Touched, for the reason given above `TOUCHED_ALLOC`: an untouched
        # zero-filled allocation need never become resident, so the limit it
        # is meant to breach might never be breached at all. This case passed
        # on the Linux runner where its sibling failed, which is exactly the
        # kind of luck worth removing from a harness other tests trust.
        r = memprobe.run_and_measure(
            [sys.executable, "-c",
             RunAndMeasure.TOUCHED_ALLOC.format(n=80 * 1024 * 1024)
             + "; import time; time.sleep(10)"],
            timeout=15, rss_limit_bytes=30 * 1024 * 1024, poll_interval=0.01)
        self.assertTrue(r.killed_over_limit)

    def test_two_measurements_in_one_process_do_not_bleed_together(self):
        # The `RUSAGE_CHILDREN`-accumulation bug this module deliberately
        # avoids (see the module docstring) would make the SECOND reading
        # include the first child's peak, so a small process measured after a
        # big one would still read back big.
        #
        # It has to be exercised on the DIRECT path (`isolated=False`), since
        # that is where the bookkeeping lives — and a direct reading is only
        # meaningful from a SMALL parent: on Linux a forked child inherits
        # its parent's page accounting until it execs, and this test process
        # has a thousand-odd other tests' worth of footprint by the time it
        # gets here (measured on CI: a `python3 -c pass` read back 254 MB).
        # So the whole scenario runs inside a fresh interpreter, which is
        # also exactly what the isolated path does for real measurements.
        big, small = _in_a_fresh_interpreter(
            "big = m.run_and_measure([sys.executable, '-c', %r],"
            " isolated=False, timeout=60).peak_rss_bytes;"
            "small = m.run_and_measure([sys.executable, '-c', 'pass'],"
            " isolated=False, timeout=30).peak_rss_bytes;"
            "print(big, small)" % RunAndMeasure.TOUCHED_ALLOC.format(
                n=80 * 1024 * 1024))
        self.assertGreater(big, 80 * 1024 * 1024, "the big child must be seen")
        self.assertLess(small, big // 2,
                        "the second reading carried the first child's peak")


class MaxrssUnits(unittest.TestCase):
    def test_darwin_reports_bytes(self):
        real_platform = memprobe.sys.platform
        memprobe.sys.platform = "darwin"
        try:
            self.assertEqual(12345, memprobe._maxrss_to_bytes(12345))
        finally:
            memprobe.sys.platform = real_platform

    def test_linux_reports_kib(self):
        real_platform = memprobe.sys.platform
        memprobe.sys.platform = "linux"
        try:
            self.assertEqual(12345 * 1024, memprobe._maxrss_to_bytes(12345))
        finally:
            memprobe.sys.platform = real_platform



class Isolation(unittest.TestCase):
    """The default `isolated=True` path exists because a forked child inherits
    its parent's page accounting on Linux (see `memprobe.run_and_measure`'s
    ISOLATION note). These pin the property that matters: the caller's own
    footprint must not reach the measurement."""

    def test_a_fat_caller_does_not_inflate_the_measurement(self):
        baseline = memprobe.run_and_measure(
            [sys.executable, "-c", "pass"], timeout=30)
        ballast = bytearray(200 * 1024 * 1024)
        for i in range(0, len(ballast), 4096):   # touch, so it is real memory
            ballast[i] = 1
        try:
            while_fat = memprobe.run_and_measure(
                [sys.executable, "-c", "pass"], timeout=30)
        finally:
            del ballast
        # 200 MB of ballast in THIS process must move the reading by far less
        # than the ballast itself. The bound is deliberately loose (the point
        # is "not proportional to the caller", not a precise figure): before
        # isolation, this exact case is what read the parent's whole footprint
        # back as the child's.
        self.assertLess(abs(while_fat.peak_rss_bytes - baseline.peak_rss_bytes),
                        50 * 1024 * 1024)

    def test_the_reading_tracks_the_allocation_not_the_caller(self):
        n = 80 * 1024 * 1024
        r = memprobe.run_and_measure(
            [sys.executable, "-c", RunAndMeasure.TOUCHED_ALLOC.format(n=n)],
            timeout=60)
        # The reading must cover what the child really held, and must not run
        # far past it — an upper bound is what catches the failure mode this
        # isolation exists for, where the caller's own footprint is added in.
        self.assertGreater(r.peak_rss_bytes, n)
        self.assertLess(r.peak_rss_bytes, n + 80 * 1024 * 1024)


def _in_a_fresh_interpreter(snippet: str) -> tuple[int, ...]:
    """Run `snippet` in a new minimal Python with `memprobe` imported as `m`,
    and return the whitespace-separated integers it prints. Used where a case
    needs a SMALL parent process to mean anything (see the bleed test)."""
    code = ("import sys;"
            "sys.path.insert(0, %r);"
            "import memprobe as m;" % str(Path(memprobe.__file__).parent)
            ) + snippet
    out = subprocess.run([sys.executable, "-c", code],
                         capture_output=True, text=True, timeout=300)
    if out.returncode != 0:
        raise AssertionError("fresh-interpreter helper failed: " + out.stderr)
    return tuple(int(x) for x in out.stdout.split())


if __name__ == "__main__":
    unittest.main()
