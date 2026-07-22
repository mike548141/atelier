# Cold pass — interruption-resilience doctrine (delta `9c11525`)

- **Date/time**: 2026-07-22 0257 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by the
  session Mike opened with "please do any review work" (continued after it
  closed the scope/lens-4 cycle). The delta's author was a sibling session,
  now closed, which neither started nor instructed this one; this session
  authored none of `9c11525` or its records. Claim `e0450ee` on `main`
  first; brief taker-written.
- **Named exposure**: before claiming, this taker had read (a) the claim
  commit `f59b1da`'s body — which names the three gaps as ratified ("the
  resume-state carrier missing at the cut, decision-limbo, and lifting the
  cmd+Q recovery procedure into method") — and (b) the tail of the ROADMAP
  gap-analysis section (Gap 3's full text), both incidentally while
  resolving mid-pass concurrency during the prior review. That is author
  framing this reviewer cannot un-read: the *problem statement* arrived
  warm. Mitigation: the framing names the gaps, not the encoding — the
  review attacks how the delta encodes them, where the author's account has
  not been read (the intent record, the commit body, and Gaps 1–2's
  analysis stay deferred until findings are committed). The diff is read
  via `git show --format=` so the body stays unseen.

## What the work is (refs only)

Delta `9c11525` (2026-07-22), at HEAD:

- `docs/method/CONCURRENCY.md` — a new section on surviving an interrupted
  session (+61 lines)
- `CLAUDE.md` — an onramp firing pointer to it (+5/−1)

Method doctrine by function — governs every future session's behaviour at
and after a cut — so the full rule-4 ceremony applies, and rule 3 puts all
decisions with Mike.

## Ask

Run all four lenses; scope is the whole commitment.

1. **Approach & assumptions** — name the load-bearing assumptions first.
   Is per-cut resilience the right frame, and is doctrine prose the right
   mechanism (vs a tool/checklist artefact)? Does the new section overlap,
   contradict, or duplicate what CONCURRENCY, RECORD, or the onramp already
   require? Is the firing condition actually findable at the moment it
   must fire — by a *resumer* session that doesn't know a cut happened?
2. **Correctness & quality** — does the text do what it claims; is every
   grounded claim real (the section will cite incidents/sessions — re-run
   or re-verify what is re-runnable, e.g. any commands the recovery
   procedure prescribes, against a live repo state); honest about what is
   doctrine vs hope.
3. **Completeness / harvest** — the pointer's flagged sub-question: should
   the template CLAUDE.md onramp carry the same died-mid-flight→sweep
   pointer so the firing condition propagates to children? Also: does the
   new section reach the surfaces that already describe session close
   (RECORD, the session-onramp skill, templates), or does it create a
   second telling that will drift?
4. **Security & privacy** — reach per shape: landed-delta, markdown-only —
   the harness scanner cannot genuinely be aimed at it; discharged on
   those grounds, per REVIEW.md lens 4. Manual pass: does the recovery
   procedure it prescribes (reflog sweeps, stash inspection, orphan
   worktrees) risk exposing or publishing another lane's in-flight
   content, and does the text guard that?

Live proofs: the repo floors at HEAD; any command sequence the section
prescribes, executed against this repo where safe; the CLAUDE.md pointer's
link target resolving (linkscan) and its firing grammar tested against the
reader who needs it.

Cycle context: first cold pass of this cycle — findings get IDs (IR1, …)
with severities; decisions are Mike's (rule 3); MAJORs present would keep
the cycle open past application.

---

## Deferred material (open only after findings are committed)

- `docs/sessions/2026-07-22-0245-interruption-resilience-doctrine.md`
  (intent record, incl. its addendum re the gitlink incident)
- The ROADMAP gap-analysis section (Gaps 1–2 unread portions)
- Commit bodies of `9c11525`, `b4b5142`, `c258451`
- The author seeded no questions beyond the pointer's flagged sub-question,
  which is carried in the Ask above; everything here is taker-written.
