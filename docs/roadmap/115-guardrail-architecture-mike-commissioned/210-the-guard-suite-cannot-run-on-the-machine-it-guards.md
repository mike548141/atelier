- [ ] 🔎 **The guard test suite cannot run green on the principal's own
      machine, and nothing says so** — found 2026-09-20 by a worker that
      reported 3 errors and correctly proved them pre-existing before
      carrying on.
      **Measured at `main`:** `python3 -m unittest discover -s tools` →
      `Ran 1168 tests … FAILED (errors=3)`. The three are `test_floor`,
      `test_floorfleet` and `test_precommit`, all `ImportError` at *load*
      time from `X | None` annotations (PEP 604, Python 3.10+). macOS ships
      `/usr/bin/python3` as **3.9.6**, which is what a session here gets;
      CI pins **3.12** in both `ci.yml` and `floor.yml`, so the same suite is
      green there.
      **Why it is a guard problem and not a laptop problem.** Every session
      is told to run the suite before it commits, and what it sees is a red
      summary line with three loader errors in it. That trains exactly the
      skim the guard layer exists to prevent: a session that learns to read
      past `FAILED (errors=3)` reads past the fourth error too. It also
      means the floor's **own** three most infrastructural modules are the
      ones never exercised locally.
      **Candidate fixes, not chosen here:** declare a minimum Python in the
      repo (and in `tools/README.md` / the onramp) and have the runner fail
      with that sentence rather than an `ImportError` · drop the 3.10+
      syntax from those three modules so the suite loads on the shipped
      interpreter · pin a newer interpreter for local use and say where it
      comes from. The trade is real: the first two keep the estate honest
      about what it requires; the third moves the requirement onto every
      machine that ever runs a guard.
