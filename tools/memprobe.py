#!/usr/bin/env python3
"""memprobe — a small, reusable harness for measuring a child process's peak
resident memory (RSS).

Board item 020/370 needed this to test secretscan's bounded-memory fix; the
API is deliberately tiny so 020/380 can point every other guard at the same
harness without re-deriving how to measure a process from outside itself.

WHY A SUBPROCESS, NOT `tracemalloc` OR IN-PROCESS MEASUREMENT: peak RSS is a
whole-process, OS-level number — it includes C buffers, the regex engine's
compiled tables, `mmap`'d pages, and interpreter/library baseline, not just
Python-heap objects. `tracemalloc` only sees the last of those, so a fix that
moves the leak from a Python `list` into a wide C read buffer would look
"fixed" to `tracemalloc` while the machine still swaps. Measuring the whole
OS process, from outside it, is the only number that matches what actually
thrashed the principal's machine (020/370's incident).

WHY `os.wait4`, NOT `resource.getrusage(RUSAGE_CHILDREN)` OR `subprocess.run`:
`RUSAGE_CHILDREN` is CUMULATIVE across every child this interpreter has ever
reaped — call it twice in one test run (two measurements in one process, or
one test file with several `TestCase`s) and the second reading silently
includes the first child's peak. `wait4(pid, ...)` returns the rusage for
EXACTLY the one child it reaps, so two measurements never bleed into each
other. This is also why `run_and_measure` never calls `Popen.wait()`,
`.poll()` or `.communicate()` — every one of those reaps the child itself
(via `waitpid`) before we get a chance to, and a second `wait4` on an
already-reaped pid raises `ChildProcessError`. Output is instead captured to
temp files, and `os.wait4` is the ONLY call that consumes the child's exit
status.

UNITS: `ru_maxrss` is KiB on Linux, bytes on macOS/BSD — a decades-old kernel
inconsistency, not a bug here. `_maxrss_to_bytes` normalises it away. This is
the only platform branch in the module; `sys.platform` is enough because the
unit never changes for the life of a kernel (no runtime probe needed).

API surface, kept intentionally small:
  ProbeResult          — returncode, peak_rss_bytes, stdout, stderr
  run_and_measure(argv, cwd=None, timeout=None, rss_limit_bytes=None)
                        — run argv to completion, return a ProbeResult

Zero third-party dependencies; stdlib only (matches every other tool here).
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass


def _maxrss_to_bytes(ru_maxrss: int) -> int:
    """Normalise a `resource.struct_rusage.ru_maxrss` reading to bytes."""
    if sys.platform == "darwin":
        return ru_maxrss
    return ru_maxrss * 1024  # Linux (and other non-Darwin) report KiB.


def _current_rss_bytes(pid: int) -> int | None:
    """The RUNNING process's current (not peak) RSS, via `ps` — the one
    portable way to read a LIVE process's memory on both macOS and Linux
    without `/proc` (Linux-only) or a third-party dependency. Used only for
    the safety limit below; `None` if the process has already exited or `ps`
    can't be run (never raises — a safety net must not itself be a new way to
    crash the caller)."""
    try:
        out = subprocess.run(["ps", "-o", "rss=", "-p", str(pid)],
                             capture_output=True, text=True, timeout=5)
    except Exception:
        return None
    text = out.stdout.strip()
    if not text:
        return None
    try:
        return int(text) * 1024  # `ps -o rss=` reports KiB on both platforms.
    except ValueError:
        return None


@dataclass
class ProbeResult:
    returncode: int
    peak_rss_bytes: int
    stdout: bytes
    stderr: bytes
    timed_out: bool = False
    killed_over_limit: bool = False


def run_and_measure(argv: list[str], *, cwd: str | None = None,
                    timeout: float | None = None,
                    rss_limit_bytes: int | None = None,
                    poll_interval: float = 0.02) -> ProbeResult:
    """Run `argv` as a child process to completion and report its peak RSS.

    `timeout` kills the child (and still returns a `ProbeResult`, with
    `timed_out=True`) rather than raising — a probe that raises on a hang
    loses the partial measurement a caller may still want to report.

    `rss_limit_bytes` is the hard safety net this repo's own incident (020/370
    — a probe that thrashed the principal's machine to ~9 GB) requires of
    anything that measures memory by actually allocating it: if the child's
    LIVE rss (polled via `ps`, see `_current_rss_bytes`) ever exceeds this, it
    is killed immediately and `killed_over_limit=True` is set. Callers
    building new synthetic-memory tests should always pass this.
    """
    with tempfile.TemporaryFile() as out_f, tempfile.TemporaryFile() as err_f:
        proc = subprocess.Popen(argv, stdout=out_f, stderr=err_f, cwd=cwd)
        deadline = None if timeout is None else time.monotonic() + timeout
        timed_out = False
        killed_over_limit = False
        status = None
        rusage = None
        while True:
            # WNOHANG: never block inside wait4 itself, so the loop can also
            # enforce the timeout and the rss limit while the child runs.
            reaped_pid, status, rusage = os.wait4(proc.pid, os.WNOHANG)
            if reaped_pid != 0:
                break
            if rss_limit_bytes is not None:
                live = _current_rss_bytes(proc.pid)
                if live is not None and live > rss_limit_bytes:
                    proc.kill()
                    killed_over_limit = True
                    _reaped_pid, status, rusage = os.wait4(proc.pid, 0)
                    break
            if deadline is not None and time.monotonic() > deadline:
                proc.kill()
                timed_out = True
                _reaped_pid, status, rusage = os.wait4(proc.pid, 0)
                break
            time.sleep(poll_interval)
        out_f.seek(0)
        stdout = out_f.read()
        err_f.seek(0)
        stderr = err_f.read()

    if hasattr(os, "waitstatus_to_exitcode"):
        returncode = os.waitstatus_to_exitcode(status)
    elif os.WIFEXITED(status):
        returncode = os.WEXITSTATUS(status)
    else:
        returncode = -os.WTERMSIG(status)

    # `Popen` doesn't know we reaped its child ourselves (via `wait4`, so we
    # could get the rusage `Popen.wait()` throws away) — left alone, it
    # thinks the process is still running and raises a `ResourceWarning` when
    # this `proc` is garbage collected. Telling it the outcome directly is
    # the documented way to reconcile the two without a second, failing
    # `waitpid` call.
    proc.returncode = returncode

    return ProbeResult(returncode=returncode,
                       peak_rss_bytes=_maxrss_to_bytes(rusage.ru_maxrss),
                       stdout=stdout, stderr=stderr,
                       timed_out=timed_out, killed_over_limit=killed_over_limit)


def _selftest() -> int:
    """`python3 tools/memprobe.py --selftest` — proves the harness itself on
    this box before anyone trusts a number it reports."""
    r = run_and_measure([sys.executable, "-c", "print('hi')"], timeout=10)
    ok = (r.returncode == 0 and r.stdout.strip() == b"hi"
          and r.peak_rss_bytes > 0 and not r.timed_out)
    if not ok:
        print(f"FAIL: {r}")
        return 1
    r2 = run_and_measure([sys.executable, "-c", "import time; time.sleep(5)"],
                         timeout=0.2)
    if not r2.timed_out:
        print(f"FAIL (expected timeout): {r2}")
        return 1
    print("selftest OK")
    return 0


if __name__ == "__main__":
    sys.exit(_selftest() if "--selftest" in sys.argv[1:] else 0)
