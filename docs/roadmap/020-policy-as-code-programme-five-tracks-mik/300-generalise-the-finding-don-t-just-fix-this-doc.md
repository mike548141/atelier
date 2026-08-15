- [ ] **Generalise the finding, don't just fix this doc.** The census in (a)
      should treat "the rule declares itself unenforced" as a *search key* —
      this one was sitting in plain sight in a clause that reads as honesty.
      🛑 **The cold pass RAN 2026-08-15 and returned FAIL — 1 MAJOR / 5 MODERATE /
      2 minor / 2 note after reconcile (no severity amendments); the cycle stays
      OPEN and CMF1–CMF10 await Mike's ruling round** (taker: a cold session Mike
      opened 2026-08-15 ~1120 UTC, running the brief a *different* cold session
      wrote at 1024 UTC, under an orchestrator-held context partition; finding
      prefix `CMF`, not the brief's `CF`, which was already taken) →
      [`reviews/2026-08-15-1033-communication-floor-cold.md`](../../reviews/2026-08-15-1033-communication-floor-cold.md).
      One verdict closes both this pointer and the rescope pointer in this
      section's `README.md`. **CMF1 (MAJOR):** the reply plane's premise is false by the
      hook contract — a `Stop`-hook block cannot make the flawed reply unread —
      reached by the reviewer from the hook documentation *before* it read the
      2026-08-15 unwiring commit, which independently states the same. The
      MODERATEs: CMF2 — the give-up path is neither a give-up nor visible, and
      the guard is per session not per turn; CMF3 — the doctrine's measurement
      figures misstate the measurement (range, threshold, and which rules had
      prior doctrine); CMF4 — the rescope's argument is a class but the code is
      three paths, and most of the remaining tally is closed review text; CMF5 —
      P1's shape rule fires on product identifiers; CMF6 — no threat enumeration
      for a machine-wide, fail-open, silent hook. Verified true (CMF10): 47/47/51
      tests, 7,817 → 4,440 exact at `e390382`, the flake did not reproduce
      (5/5 full-suite, 11/11 module), floor exit 0 both planes.
      *Delta:* `docs/method/COMMUNICATION.md` § *The meta-rules that make it
      work*, landed `753adb6` (on `main` as `c374959`). *Intent record:* this
      item. The pointer was queued one commit late, against the
      landing-equals-queuing rule stated in this file's preamble.
