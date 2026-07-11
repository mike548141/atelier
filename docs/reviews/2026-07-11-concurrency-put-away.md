# Review — CONCURRENCY "Every branch ends put away"

**Scope:** the put-away rule added to `method/CONCURRENCY.md` (commit
`d8aa2ae`, 2026-07-11, session 34), review-owed as doctrine text (flagged, not
self-certified). The ROADMAP brief asked a light read: is the
landed/abandoned fork exhaustive; does salvage→tag→delete→record fight
RECORD/REVIEW; is the bearing (the `atelier-method-review` branch re-derived
across sessions) stated accurately.

**Reviewer:** Fable, cold fresh-context session (2026-07-11), read-only; fixes
applied by the coordinating session after the verdict. Verdict below verbatim.

---

VERDICT: PASS-WITH-FINDINGS

**Findings**

1. **[minor] The bearing's "multiple later sessions each re-derived its
   status" outruns the repo's own record.**
   Location: `docs/method/CONCURRENCY.md`, final paragraph.
   What the record shows: session 12
   (`../sessions/2026-07-10-12-worktree-reconciliation-e3-salvage.md`) did the
   salvage + archive tag and deliberately kept the remote branch; after that,
   exactly **one** recorded session re-derived it — session 34
   (`../sessions/2026-07-11-34-instruments-layer.md`, "the recurring one"). I
   found one further re-derivation event only off-record: PR #1 was
   closed-not-merged at 2026-07-10T13:57Z with a comment reciting the branch's
   disposition from session 12 — a status re-derivation by whoever closed it,
   but no session-log entry owns that act, and I cannot tell whether it was a
   Claude session or Mike by hand. So "multiple sessions" is plausible (two
   events) but only one is reconstructible from `docs/sessions/` alone.
   Why it matters: `docs/method/RECORD.md` sets the standard that a future
   reader reconstructs the why "from the repo alone"; a doctrine bearing whose
   evidence count partly lives in a GitHub PR timeline quietly fails its own
   house rule, and the commit message (`d8aa2ae`: "re-investigated by
   several") escalates it further.
   Fix: either soften the bearing ("kept resurfacing across later sessions")
   or ground the count explicitly — cite session 34 and the PR #1 close as
   the re-derivation events.

2. **[minor] The premise "a branch that exists must mean exactly one thing:
   open work" has unstated exemptions, so the landed/abandoned fork is
   exhaustive only within an implicit scope.**
   Location: `docs/method/CONCURRENCY.md`, "Every branch ends put away",
   opening sentence and the fork.
   The fork is exhaustive for branches that *end* — every terminal state I
   could construct (partially cherry-picked, superseded-and-renamed, rejected
   by review) reduces to landed or abandoned/superseded. But the premise
   sentence is stated absolutely, and two branch kinds never end: the
   integration branch itself, and (for adopters of this public doctrine)
   deliberately permanent lines — `gh-pages`, `stable/1.x` deploy or release
   branches — which are neither open work nor destined for the fork.
   atelier's own live `plugin-bundle` (PR #3, open-by-design, merge = go-live)
   *is* genuinely open work and consistent, but a cold reader will test the
   rule against exactly these cases.
   Fix: one scoping clause, e.g. "This governs lines of *work*; the
   integration branch and any deliberately permanent line (release, pages) are
   infrastructure, not open work."

3. **[nit] Tag convention omits the date the live precedent (and RECORD.md)
   carries.**
   Location: `docs/method/CONCURRENCY.md`, "(`archive/<name>` — the message
   states…)".
   The executed tag is `archive/2026-07-10-method-review-parallel-verdict` —
   date-prefixed, matching RECORD.md's "Absolute dating, everywhere in the
   record". The doctrine specifies only `archive/<name>`.
   Fix: write `archive/<date>-<name>` so the convention states what the
   precedent did and what RECORD.md requires.

**On question 2 (RECORD/REVIEW conflicts):** none found.
Salvage→tag→delete→record composes cleanly with RECORD.md — "record the
disposition in the session log" is exactly RECORD's session-log discipline;
deleting a ref is not editing history (append-only holds; the annotated tag
keeps every commit reachable, and the actual tag message names what was
salvaged where and what was consciously dropped, verified via `git tag -n99`).
REVIEW.md artifacts (briefs/verdicts) live in `docs/reviews/` on main, so
branch deletion loses nothing a review depends on; PR discussion survives
branch deletion on the host. The rule also correctly routed itself through
REVIEW's own gate: doctrine text, flagged review-owed in ROADMAP, not
self-certified — this review is that gate.

**Grounding.** Strong, and verified rather than assumed. The rule's every
mechanical claim reproduces: commit `d8aa2ae` (2026-07-11) added the section
together with the ROADMAP review-owed item and the session-34 record in one
commit (RECORD lockstep, lived); the annotated tag exists with a
disposition-bearing message; `git ls-remote` shows only `main` and
`plugin-bundle` — `atelier-method-review` is gone; `gh repo view` confirms
`deleteBranchOnMerge=true` on atelier (I did not verify the other 7 repos the
commit message claims were flipped — out of scope, unverified). The one place
grounding thins is finding 1: the *multiplicity* of re-derivations is the
single bearing claim the repo record alone cannot reproduce. Worth noting in
the rule's favour: session 12's record shows the branch was kept
*deliberately*, as a considered second archive copy — and it still generated
the re-derivation tax — which is stronger grounding for "never keep the
branch 'just in case'" than the half-closed-by-omission framing suggests.

---

**Disposition (2026-07-11, same day):** all three findings **[fixed]** — the
bearing now grounds the count explicitly (PR #1 close + session 34) and keeps
the reviewer's sharpened framing (a *considered* kept-branch still generated
the tax); the scoping clause for integration/permanent branches added; the tag
convention now reads `archive/<date>-<name>` per RECORD's absolute dating.
Gate cleared.
