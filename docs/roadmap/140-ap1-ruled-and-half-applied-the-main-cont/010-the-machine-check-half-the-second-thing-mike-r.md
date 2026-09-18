- [x] 🔎 **The machine-check half — the second thing Mike ruled, and it is not
      built.** Nothing enumerates the boundary that makes the floating `@main`
      call safe: `floorfleet` reports whether children *call* the floor and is
      silent on the control protecting what they call. Owed: a parent-row check
      reading branch-protection/ruleset state and going **RED when absent** — the
      same absences-raise-their-hands doctrine already applied to children. Until
      it exists, this control is exactly what AP1 condemned: real today, unwatched
      tomorrow, and nothing would notice if the ruleset were deleted.

      ✅ **BUILT 2026-09-18** (`15bc1e7`, merged from `main-boundary-check-0918`):
      `floorfleet` reads `repos/{owner}/{repo}/rules/branches/main` whenever a
      plane already talks to GitHub and prints a **boundary** line under the
      parent row — 🛑 red when `deletion` or `non_fast_forward` is missing, ⚠️
      unknown when the API cannot be read (never a pass), ✅ green otherwise —
      and `--check` fails on red or unknown. `required_signatures` is shown but
      informational: the ADR amendment calls signing warn-first and never
      names it as the ruled control. Live run: green — the active ruleset
      blocks deletion and force-push and requires signatures.
      🔎 **Noticed:** the ADR's 2026-08-23 amendment still says `main` carries
      *no* ruleset; one is now active. That is `140/020`'s ground (the clause
      closer to true), not this build's.
