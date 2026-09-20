"""Stdlib-only tests for memprobe (no pytest needed): `python3 -m unittest`.

Small and fast by design: this module is the harness OTHER tests build on
(`test_secretscan.py::BoundedMemory`, and every guard 020/380 eventually
points at it), so it needs its own quick proof of correctness independent of
any of them — a bug here would look like a bug in whatever it's measuring.
"""

import sys
import time
import unittest

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
        # include the first child's peak too, so a small process measured
        # after a big one would still read back big.
        memprobe.run_and_measure(
            [sys.executable, "-c", "x = bytearray(80 * 1024 * 1024)"], timeout=10)
        small = memprobe.run_and_measure([sys.executable, "-c", "pass"], timeout=10)
        self.assertLess(small.peak_rss_bytes, 40 * 1024 * 1024)


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


if __name__ == "__main__":
    unittest.main()
