- [ ] 🎯 **Decide whether "make the instrument show a positive first" earns a
      line, and whether this sits inside `370` or beside it.** The narrative
      argues *beside*: `370`'s remedy is to re-read the report against the
      artefacts, and that remedy is unavailable when the failure IS the absence
      of a report. Two sessions hit this independently on 2026-08-24 and neither
      caught it from the inside.
  - [ ] **The candidate rule, stated tightly enough to be checkable:**
        **before an instrument's negative result carries weight, make it display
        a positive — same instrument, same run, same syntax, against a case
        already known to be present.** Where the negative will authorise
        something irreversible, the control is not optional.
  - [ ] 🔑 **Why it is not a restatement of "check your exit codes".** That rule
        is true and insufficient, and all three reasons were found the same
        night. An exit code can be **0** with the answer still empty for the
        wrong reason — a substring operator matched against a name a *separate
        pool* also carried, honest tool, wrong question, failing toward *false
        reassurance*. The shell hides status **structurally**: `x=$(cmd)` in a
        pipeline, a `$(...)` inside a `printf`, a value read into an `if` — none
        surfaces a non-zero status without deliberate work, and `2>/dev/null` is
        written reflexively. And the class **generalises past exit codes
        entirely**: a filter that can only match the broken form of a value, a
        comparison that treats an absent file as an identical one, a guard
        matching a naming convention the other copy does not use. No exit code is
        involved in any of those, and all three are the same defect.
  - [ ] ⚠️ **The reason this is doctrine and not a bug report: the conclusion was
        RIGHT.** The dataset really had no snapshots. Nothing downstream broke,
        nothing was lost, and neither session would ever have discovered the
        defect from its own results. It surfaced only because two sessions
        compared method and their answers disagreed — one had a wrong answer, the
        other had no answer wearing an answer's clothes. **A defect that is
        invisible when it does no harm is exactly the kind that has to be
        designed out rather than noticed.**
  - [ ] 🔎 **The cheapest possible form, for the doc that ends up carrying it:**
        one extra call. Not a test suite, not a framework — the same query
        against a case you already know the answer to, printed on the line above
        the real one, so the reader sees both.

        ```
        taupo/media   (known to hold snapshots)  ->  198   # the instrument works
        taupo/wakatipu                            ->    0   # measured absence
        ```

        Without the first line the second is indistinguishable from a broken
        tool. With it, the zero is a measurement.
  - [ ] 📄 **Provenance, and it matters to the argument.** docker-heap,
        2026-08-24, found across two concurrent sessions rather than within
        either. Session A's query timed out and returned nothing; session B's
        returned rows belonging to a different pool. Neither could see its own
        defect; each could see the other's. That is an argument for the cheap
        mechanical control **and** for cross-checking method between concurrent
        sessions, which `CONCURRENCY.md` currently treats as a claim-collision
        protocol rather than a correctness one.
