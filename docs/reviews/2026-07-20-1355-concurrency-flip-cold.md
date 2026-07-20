# Cold pass — CONCURRENCY posture flip, "assume you are not alone" (delta `295d94a`)

- **Date/time**: 2026-07-20 1355 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike spawned with "do any reviews waiting". This session authored none of:
  the flip delta (`295d94a`), the CONCURRENCY.md doctrine it edits, the
  CLAUDE.md onramp restatement, or any record of the authoring session. Claim
  landed on `main` (`69b8de0`) before this worktree was created; this brief is
  taker-written.
- **Named exposure**: before claiming, the taker read the ROADMAP `⏳` entry
  (which carries the author's evaluative summary and two "Watch:" seeds — the
  ladder's cost to light sessions, and whether "positive evidence" is crisp)
  and `295d94a`'s commit message (the author's account of the blind spot and
  the fix). Both are author framing; both are treated as claims to re-derive,
  not facts, and the seeded watches sit below the divider until this pass's
  own findings are committed. The taker also read CONCURRENCY.md in full
  before writing this brief — unavoidable, since following the claim/worktree
  procedure *is* executing the doctrine under review; that execution doubles
  as a live re-run of the mechanism.
- **Deferred material (opened only after findings are committed)**: the
  ROADMAP entry's *review:* paragraph and Watch seeds; any session record of
  the authoring session (2026-07-20); the sibling onramp-rhythm delta's
  account of CONCURRENCY.md (a separate pass, same taker — read after both
  findings sets are committed).

## What the work is (refs only)

Commit `295d94a` — edits to `docs/method/CONCURRENCY.md` (§ The trigger,
§ The solo default) and `CLAUDE.md` (read-order rule 1). In-scope at HEAD:
those two files, plus consistency of every other section of CONCURRENCY.md
and any sibling doc that states or relies on the concurrency prior.

## Lenses and the taker's attack surface

Lens 1 — approach & assumptions (named by the taker as its first act):

- **A1 — "positive evidence you are alone" must be operationalisable.** If no
  listed signal can actually establish solitude, the solo default becomes a
  dead letter and every session pays worktree ceremony — the doctrine would
  have flipped from a blind spot to an unfalsifiable prior. What counts as
  evidence, per the text, and can a session ever hold it?
- **A2 — the claim mechanism must survive the flip.** Claiming requires a
  commit on `main` *from the primary checkout*. Under the new prior, a session
  must assume the primary checkout may hold another session's in-flight state
  at the moment it goes there to claim. Does the doctrine's own claim
  procedure stay safe under the doctrine's own prior?
- **A3 — the two firing cues must still have a job.** "Say so at open" and
  the dirty-tree backstop were the *triggers* under the old prior. If the
  prior is now concurrent-by-default, are the cues coherently re-purposed
  (they now tell you when you may *relax*), or does stale trigger language
  survive?
- **A4 — the ladder's middle rung.** "Light, single-commit write — sync +
  claim; trunk-based is enough" — is the boundary between rung 2 and rung 3
  decidable at session open, when a session often doesn't yet know how many
  commits the work will take?

Lens 2 — correctness & quality: does the flipped text contradict any other
section of CONCURRENCY.md at HEAD; does the CLAUDE.md rule-1 restatement match
the doctrine it points to; any overclaim (a "grounded" or "proven" that isn't).

Lens 3 — completeness / harvest: what else states the old prior and was not
caught — the PROPAGATION.md child block (the author flags it as out of scope;
verify the catch-up is genuinely queued somewhere, else it is silently
dropped), templates, sibling method docs, memory-facing text.

Live re-runs owed in scope: the claim→push→worktree sequence (this session
executed it — result is evidence); grep sweep for pre-flip phrasing at HEAD.

---
