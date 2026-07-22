# 2026-07-21 · 2208 UTC · scope-mandate/lens-4 cold pass — PASS-WITH-FINDINGS 2M/3M/2L (Fable, wt: review-scope-lens4-cold-pass)

## The cycle

The queued `⏳` on deltas `f9db922` + `a059e49` (REVIEW.md scope mandate +
security & privacy lens 4) taken by a rule-4 taker: Mike-spawned ("Please do
any review work"), authored none of the delta. Claim on `main` (`3909d76`)
first, then the worktree.

**Two-hop spawn shape, a first**: the taker had already read the author's
intent record before knowing it was contaminating — so instead of reviewing
directly, it named the exposure in the brief, kept everything above the
divider refs-only, put its seeded questions below it, and spawned a
fresh-context subagent as the reviewer. The subagent read the brief to the
divider, named its own attack surface, committed its findings draft
(`reviews/drafts/`, kept as the deferral-order evidence), and only then
opened the deferred material. Rule 4's criterion holds through both hops;
the taker's contamination never reached the reviewer — except via the
doctrine's own scanner instruction, which is finding SL2.

## Verdict

**PASS-WITH-FINDINGS — 2 MAJOR · 3 MEDIUM · 2 LOW**
(`reviews/2026-07-21-2158-review-scope-security-lens4-cold.md`). The
doctrine itself judged sound; the MAJORs are propagation and executability:

- **SL1 (MAJOR)** — `skills/review-brief/SKILL.md` still stamps *three*
  lenses, no security & privacy, no scope mandate — a narrowing-free
  point-of-use surface now contradicting the parent, plugin-bundled to the
  fleet. Same drift class the 2026-07-19 F3 caught; second shipping.
- **SL2 (MAJOR)** — lens 4's `/security-review` mandate misfires
  **live-proven in this very pass**: it scans *pending* changes, so on a
  cold pass it analysed the taker's brief (the only dirty file) instead of
  the landed delta — and in doing so injected the brief's deferred section
  into the cold reviewer pre-draft (contamination disclosed and
  timeline-attributed in the draft). Its own exclusion list bars markdown
  findings, so for doctrine work the "mechanical floor" is definitionally
  empty. The `a059e49` grant was permissive ("if it is useful"); the text
  escalated it to a mandate, and the mandate is what forces the misfire.
- SL3/SL4 (MEDIUM) — two template surfaces still carry pre-delta scope text
  ("not just correctness" in CONTRIBUTING; a "correctness only" review Type
  in the reviews README the delta itself amended).
- SL5 (MEDIUM) — widest-scope vs "scoped and short" unreconciled; non-goals
  are the only narrowing lever yet authors write them in warm briefs.
- SL6/SL7 (LOW) — "where possible" carries no grounds burden; wrap stubs.

Lens 4 ran on itself: repo scanner floor re-run green at HEAD (secret ·
leak · licen · link · review · size), design-altitude surface none beyond
SL2's information-flow defect.

## Status

🎯 **SL1–SL7 await Mike's ruling** (rule 3 — self-authored doctrine; the
reviewer's counsel is in the verdict's follow-ups). MAJORs present ⇒ after
rulings land, the application is reviewable and the cycle stays open until
a pass returns no MAJOR. Verdict + draft + records merged to `main`;
worktree away.

## Addendum — 2026-07-22 0028 UTC · Mike's accept-all applied (wt: scope-lens4-sl-apply)

Mike ruled **"accept all as recommended"**: SL1–SL7 **[fixed]**, applied by
the taker session (authored neither doctrine nor verdict; claim `fe39f04`
on `main` first). Delta `d553045`: the review-brief skill gains the scope
mandate + four lenses + scanner clause with a **mechanical lens-roster
parity floor** (LensRosterParityTest — REVIEW.md's numbered list is the one
source; red leg proven; suite 298→302); lens 4's scanner sentence rewritten
reach-per-review-shape on the restored permissive grant, with both
live-proven cautions stated; scope-vs-"scoped and short" reconciled and
non-goals made explicitly reviewable; impossibility claims carry grounds;
CONTRIBUTING + reviews templates swept (SL3/SL4/SL7). Decisions stamped in
the verdict's dated addendum. **MAJORs in the pass ⇒ the application
inherits rule-4 status: its cold pass queued `⏳` refs-only; this session
spawns nothing further.**
