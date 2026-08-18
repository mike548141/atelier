- [ ] 🔎 **By-call enforcement resolves through a *working tree*, so "fresh"
      currently means whatever is on disk — including a parent session's
      uncommitted mid-edit state** `[S][tool]` — raised from a private child
      2026-08-18 via § *Pointing up*, as a question rather than a finding, and
      filed here because the mechanism is real.
      **Not a challenge to by-call, and the filer established that first.** Its
      first instinct was *"doctrine is pinned by SHA, enforcement is not — a
      lockfile gap"*. It then read `PROPAGATION.md` § *Enforcement propagates
      too — by call, never by copy*, found the ADR'd argument already made, and
      **declined to file it**. Worth recording as the check-the-parent rule
      paying out a second time the same day, in the direction of *not* writing
      something wrong.
      **The narrow residue that section does not address.** A child's hook
      resolves the scanners through `hooks.atelierTools`, a filesystem path to
      the parent's **working tree** — not a ref, not a SHA, not an install. So
      *fresh* means *whatever is on disk at that instant*, and a child
      committing while a parent session is mid-edit is gated by half-written
      scanner code.
      **Why it is a distinct failure mode and not a restatement of staleness.**
      The section's argument is that a copied gate silently enforces the
      standard current on the day it was copied. This is the mirror: a called
      gate can enforce a standard **nobody has chosen yet** — an in-progress
      edit, a debug print, a half-applied rule. Both end in the shape that
      section names, *a gate that reports success against a standard nobody
      chose*; they arrive by opposite routes, and only one of them is written
      down.
      **Honest scoping, from the filer, unprompted:** *"Your tree was clean when
      I checked, so this is a mechanism, not an incident."* No occurrence is
      claimed. It may also be adequately covered by the hook's existing trust
      note, which already says to point it only at a tools directory you own —
      whether that note is doing this work, or is about a different threat
      entirely, is the first question for whoever takes this.
      **Related and worth pricing together rather than twice:** the estate has
      an open strand on whether the scanner harness should be single-sourced,
      and the answer there may make this moot or may make it sharper.
