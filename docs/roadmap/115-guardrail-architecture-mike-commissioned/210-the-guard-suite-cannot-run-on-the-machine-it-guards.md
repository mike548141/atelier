- [ ] 🔎 **A session's default `python3` is too old to load three of the
      guard tests, and nothing says which interpreter to use** — found
      2026-09-20 by a worker that reported 3 errors and correctly proved them
      pre-existing before carrying on; two other workers hit the same thing
      independently in the same sitting.
      **Measured at `main`:** `python3 -m unittest discover -s tools` →
      `Ran 1168 tests … FAILED (errors=3)`. The three are `test_floor`,
      `test_floorfleet` and `test_precommit`, all `ImportError` at *load*
      time from `X | None` annotations (PEP 604, Python 3.10+).
      **The correction that matters, because the first framing of this item
      was wrong:** the machine is not short of a modern interpreter — it has
      **3.14.6** at `/Library/Frameworks/Python.framework/Versions/3.14/`,
      and a worker that pointed at it explicitly got `Ran 1440 tests … OK`.
      What a *session's* shell resolves is `/usr/bin/python3`, **3.9.6**,
      because that shell's `PATH` is the minimal one, without the directories
      an interactive login shell has. So this is a **which-interpreter**
      problem, not a missing-dependency one. CI pins **3.12** in both
      `ci.yml` and `floor.yml` and is green.
      **Why it is a guard problem and not a laptop problem.** Every session
      is told to run the suite before it commits, and what it sees is a red
      summary line with three loader errors in it. That trains exactly the
      skim the guard layer exists to prevent: a session that learns to read
      past `FAILED (errors=3)` reads past the fourth error too. It also
      means the floor's **own** three most infrastructural modules are the
      ones never exercised locally.
      **Candidate fixes, not chosen here:** state the minimum version and the
      interpreter to use where a session will actually read it (`tools/
      README.md`, the onramp) and fail with that sentence instead of an
      `ImportError` · drop the 3.10+ syntax from those three modules so the
      suite loads on whatever a bare shell resolves · have the scanners and
      tests resolve a suitable interpreter themselves rather than trusting
      `python3`. The trade is real: the first two keep the estate honest
      about what it requires, the third hides a version requirement that an
      adopter on someone else's machine still has to meet — and this repo's
      own selling point is that a peer can run the scanners with the system
      `python3` and no install, which the second candidate protects and the
      others do not.
      **Wider than the tests:** if `/usr/bin/python3` is what a session gets,
      every `python3 tools/<scanner>.py` invocation in the doctrine, the hook
      and the onramp runs on 3.9 too. Those work today; whether they are
      *meant* to is part of this item.
      📈 **Second instance, 2026-09-20, and it widens the item from "which
      interpreter" to "the session shell's PATH".** Running the full suite on
      the 3.14 interpreter this item names clears the three import errors and
      leaves **exactly one**:
      `test_floorfleet.DiscoveryAuthorityTest.test_from_github_end_to_end_…`
      fails with `FileNotFoundError` on `gh`, because `floorfleet.read_boundary`
      shells out to `gh api` and a session's minimal `PATH` has no `gh` — it
      lives at a user-local bin directory an interactive login shell adds and a
      session's shell does not. Re-run with that directory on `PATH`: **118
      tests, OK.** Whole suite, correct interpreter and `PATH`: **1,531 tests,
      all passing.**
      🔑 **So the cause is one rung up from the interpreter.** Two different
      tools — a modern `python3` and `gh` — are both absent for the same
      reason, and a session that trusts its own suite run sees a red it cannot
      attribute and did not cause. The first framing of this item read as a
      Python-version problem; it is an **environment-contract** problem, and
      the fix candidates should be re-read in that light (a named interpreter
      alone does not solve `gh`).
      ⚠️ Not established: what else the minimal `PATH` is missing that no test
      currently exercises. Two tools surfaced because two tests happened to
      need them; nothing has enumerated the contract.
