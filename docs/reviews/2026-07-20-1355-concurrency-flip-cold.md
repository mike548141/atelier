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

# Verdict — 2026-07-20 ~1410 UTC

**Provenance repeated (rule 4):** reviewed by the rule-4 taker named in the
brief — Mike-spawned ("do any reviews waiting"), author of none of the flip,
the doctrine, or their records. Findings below were committed before any
deferred material (the ROADMAP *review:*/Watch seeds, the authoring session's
records) was opened. **Added exposure discovered mid-run:** `295d94a`'s own
diff carries its SESSIONS.md entry — the author's evaluative account
("Dogfooded…") — so reading the delta *is* reading some author framing. Named,
not denied; every claim in it was re-derived, none taken.

## Lens 1 — approach

**The flip itself is sound.** The blind spot is real and self-inflicted: the
doctrine's own commit-small-push-fast hygiene guarantees a disciplined
parallel session presents a clean tree most of the time, so the old
dirty-tree-only trigger was structurally blind to exactly the well-behaved
case. Flipping the prior and scaling precaution to the write is the right
shape of fix — the attack surface below found no assumption that breaks it.
This pass **executed the flipped procedure live** as its own first act
(claim on `main` `69b8de0` → push accepted → worktree
`atelier-review-triple-take`): the mechanism works end-to-end and the
pre-put-away cost was genuinely near-zero. The put-away cost lands at this
session's close and is noted under CF1.

## Findings

- **CF1 (MEDIUM, lens 2 — overclaim).** § The solo default closes with
  "Truly-alone sessions still pay nothing — the only change is that a clean
  tree no longer counts as the evidence." Not true as written: a session that
  *is* alone but holds no positive evidence of it (the common case — the
  principal rarely declares solitude) now pays the full worktree + put-away
  ceremony for write-heavy work. The cost lands precisely on
  *alone-but-unevidenced* sessions; the reassurance denies the trade the flip
  deliberately makes. The trade is right (a wasted worktree is cheap; a
  clobbered tree is not) — the sentence should own it, not deny it.
  *Taker's counsel: reword to "an* evidenced*-alone session still pays
  nothing; an alone-but-unevidenced one buys insurance at near-zero cost".*
- **CF2 (MEDIUM, lens 2 — internal contradiction).** § The trigger now
  introduces the two cues with "Read them as telling you when you may *relax*
  the worktree default". Backwards: both cues (say-so-at-open, dirty-tree)
  fire toward *escalation* — each tells a session it is concurrent; neither
  can ever license relaxing. Read as written, cue-silence becomes the relax
  signal — which is exactly the inference-from-silence the flip exists to
  ban. The only sanctioned relax path is § solo default's positive say-so.
  *Taker's counsel: "Read them as extra ways to discover you are concurrent,
  never as the only ones — their silence licenses nothing."*
- **CF3 (MEDIUM, lens 1/3 — doctrine gap the flip makes hotter).** Claiming
  requires an edit → commit → push *from the primary checkout* on `main`;
  the trigger forbids touching a tree holding a stranger's uncommitted edits
  ("never work around… never absorb"). No rule says what a claimer does when
  it arrives at a dirty primary checkout — and the flipped prior says to
  *expect* that case. If the stranger's edits don't touch the queue file,
  staging only the claim hunk is mechanically safe but doctrinally forbidden
  as written; if they do touch it, that is positive proof the other session
  is queue-active. Pre-existing gap (§ Claiming work, 2026-07-13), but the
  flip raises its expected frequency, so it lands here.
  *Taker's counsel: one bearing in § Claiming work — dirty primary + queue
  file untouched ⇒ stage the claim line alone, commit nothing else; dirty
  primary + queue file dirty ⇒ treat as a live claim in flight: sync, take
  the next item.*
- **CF4 (MEDIUM, lens 3 — the propagation half is homeless).** The child
  doctrine block — `PROPAGATION.md` canonical text and
  `build/templates/CLAUDE.md` — still teaches the pre-flip trigger
  ("Uncommitted changes… ⇒ another session is live: move to a worktree",
  nothing on the flipped prior or the write-scaled ladder). Every child
  session keeps operating on the old prior until this propagates.
  `PROPAGATION.md`'s own rule says the block's wording is reviewed when
  concurrency doctrine changes, and § Claiming work's fan-out rule says work
  must exist as its own claimable line — but the catch-up exists only as a
  *"Still owed on the block, but NOT this item's"* note inside the
  onramp-rhythm ROADMAP item. Un-lined work cannot be claimed; as queued, it
  is structurally invisible. *Taker's counsel: give the block catch-up its
  own `[ ]` ROADMAP line (it is small: reword one bullet in two files +
  fleet pin-bump note), or fold it into this cycle's application batch.*
- **CF5 (LOW, lens 2).** "or an equivalent positive signal" is the one open
  joint in the evidence test. The text already excludes the tempting false
  signal (clean tree); the residual risk is other silence-shaped signals
  being promoted to "equivalent" (no other terminals visible, no recent
  pushes). *Counsel: one clause — "equivalent means an affirmative statement
  or record, never an absence".*
- **CF6 (LOW, lens 2 — residue).** The say-so cue keeps its "(primary)"
  label — a pre-flip artefact from when it was the primary *trigger*. Under
  the flip it is one of two escalation cues, primary over nothing.
- **CF7 (LOW, lens 1).** The rung-2/rung-3 boundary ("light, single-commit"
  vs "multi-commit") must be judged at open, when commit count is often
  unknowable. The "by default" lean partially covers it. *Counsel: add
  "when unsure which rung, take the worktree" — five words closing the
  boundary case.*

Lens 2 checks run clean otherwise: the `CLAUDE.md` rule-1 restatement is a
faithful compression (it drops rung 2, but points to § The trigger for the
full ladder — no contradiction); no other section of CONCURRENCY.md at HEAD
still asserts the old prior; the sibling-doc sweep (`MODEL-ECONOMICS.md`,
`AUTONOMY.md`, `RECORD.md`) found no stale statement of the solo prior
outside the child block (CF4).

## Reconcile — deferred material opened after the findings above were committed

The author's two Watch seeds map onto findings this pass reached
independently: *ladder over-tax* ↔ CF1/CF7 (the tax is real but priced
honestly only after CF1's reword); *evidence crispness* ↔ CF5. Beyond the
seeds, the pass found CF2 (the backwards relax sentence), CF3 (the dirty-
primary claiming gap), and CF4 (the homeless propagation half) — none of
which the seeded questions point at, consistent with REVIEW.md's
floor-never-fence expectation. The authoring session's SESSIONS entry claims
"Dogfooded — done in a worktree despite a clean tree": verified — `295d94a`'s
records name wt `atelier-concurrency-assume-parallel`, and the branch is
absent at HEAD (put away). No discrepancy between the author's account and
the delta.

## Result

**PASS with findings — 0 MAJOR · 4 MEDIUM · 3 LOW.** The flip is the right
rule; the findings are wording that denies its own trade (CF1), a sentence
that quietly re-admits the banned inference (CF2), one procedural gap the
flip makes hotter (CF3), and a homeless propagation half (CF4). Doctrine is
self-authored in rule 3's sense — **decisions are Mike's**; taker's counsel
sits with each finding, labelled. No-MAJOR ⇒ on Mike's rulings this cycle
closes terminal per the close rule, with the application batch (and CF4's
line) the only follow-on.

## Decisions — ruled 2026-07-20, applied `87af9f9` (terminal application)

Mike: *"1–3 I rule that I accept your recommendations"* — all taker's counsel
accepted, applied by the taking session (a terminal application: rulings of a
no-MAJOR pass close without a further queued pointer, REVIEW.md close rule).

- **CF1 [fixed]** — § solo default now owns the trade: an *evidenced*-alone
  session pays nothing; an alone-but-unevidenced one buys insurance at
  near-zero cost. **CF5 [fixed]** in the same paragraph: an equivalent
  positive signal is affirmative, never an absence.
- **CF2 [fixed]** — the cues are discovery-only; their silence licenses
  nothing.
- **CF3 [fixed]** — § Claiming work gains the dirty-primary rule: queue file
  clean ⇒ stage the claim hunk alone; queue file dirty ⇒ the other session is
  queue-active, take the next item.
- **CF4 [fixed]** — the child block's Concurrency bullet caught up to the
  flipped prior in `PROPAGATION.md` + `build/templates/CLAUDE.md` (folded
  into this batch per counsel's second option); parity re-proven, suite
  20 OK. Children adopt at pin bump.
- **CF6 [fixed]** — "(primary)" residue dropped. **CF7 [fixed]** — "when
  unsure which rung, take the worktree."

**Cycle CLOSED terminal.**
