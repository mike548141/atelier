# Review — CONCURRENCY "Claiming work" applied-batch cold pass

**Reviewed:** `docs/method/CONCURRENCY.md` § *"Claiming work — make selection
collide like naming does"* (lines 132–229) **and** the `[~]`→`[ ]` reversion
folded into the following section *"Every branch ends put away"* (lines 251–253),
as they stand at **HEAD `db11213`** ("method: apply the Claiming-work review — all
seven findings [fixed]"). Read against the whole of `CONCURRENCY.md` for
coherence, plus `EVIDENCE.md` and `REVIEW.md`.

**Why this pass exists:** the first cold pass
(`2026-07-13-concurrency-claiming-work.md`) returned PASS-WITH-FINDINGS carrying
one MAJOR; the principal ruled all seven [fixed] and they were applied in
`db11213`. REVIEW.md's cycle rule owes an applied-batch cold pass whenever the
prior pass carried a MAJOR: **confirm the fixes landed faithfully, and that no
new MAJOR was introduced.** The cycle closes when a pass returns no MAJOR.

**Attack surface I named first (before reading the prior verdict):**
(1) does "claim on `main` before branching" cohere with the doc's own
worktree=branch substrate — *where* does a parallel session physically make a
`main` commit? (2) is the adjacent-item keep-both conflict claim actually what
git does, and is the stated mechanism right? (3) does a same-item claim really
yield a same-line conflict, and a non-adjacent one stay silent? (4) is the
`[~]`→`[ ]` reversion actually present in the put-away section? (5) can an
off-estate adopter (issue-tracker queue) still apply the principle?

**Method — grounded mechanically.** Built throwaway git repos and drove the
rebase behaviour live: same-item, adjacent (0 unchanged lines between),
two-apart (1 unchanged line between), and far-apart claims. Also confirmed git
refuses to check out `main` in a second worktree (bears on finding 1). Verified
the reversion text and that the live `ROADMAP.md` already carries the `[~]`
claimed-state legend and the doc's exact claim format.

**Fixes confirmed landed (all seven):**

1. ✅ Decoupled from worktree-mode — claiming now keys on "selects it from the
   shared queue — not when it enters a worktree" (145–148); the old
   "worktree-mode discipline / solo claims nothing" framing is gone, and the
   unaware-parallel gap is explicitly closed (176–181).
2. ✅ "Where the claim lands is load-bearing … claim on `main`, then branch"
   (154–159), with the invisible-on-a-feature-branch failure named.
3. ✅ Fan-out precondition named — leaves must exist as own lines; a bundled
   line is claimed as a unit and serialises; split first (190–195).
4. ✅ Reversion present in **both** homes — the claiming release paragraph
   (197–202) and the put-away abandonment procedure (251–253:
   "salvage → tag → delete → record → revert `[~]`→`[ ]`"); the "no separate
   step to forget" overclaim is replaced with an honest "with one added step …
   don't trust it to happen by itself."
5. ✅ Git-text-queue precondition stated + tracker primitive named for
   adopters (215–222).
6. ✅ Guarantee softened — same-item = real yield, adjacent = keep-both;
   `[~]` on the checkbox line (168–171). Behaviour verified live (below).
7. ✅ Timestamp demoted to a tiebreak; branch-existence is the primary
   staleness signal (204–213).

All seven landed faithfully and honestly. The mechanical claims reproduce:

| claim pair | doc says | live result |
|---|---|---|
| same item, two sessions | same-line conflict (yield) | ✅ CONFLICT |
| adjacent one-line items (0 lines between) | keep-both conflict | ✅ CONFLICT |
| items with 1 unchanged line between | (implied clean) | ✅ CLEAN |
| non-adjacent items | usually no conflict | ✅ CLEAN |

---

## Verdict: PASS-WITH-FINDINGS — **no MAJOR; the cycle closes here.**

The applied batch is faithful: every one of the seven decided fixes is in the
text as ruled, the core same-line-collision mechanism reproduces live, and the
grounding incident (atelier 2026-07-13) is intact. No new MAJOR was introduced.
Two residual findings remain — one MEDIUM coherence/adopter gap that the *fix
for finding 2 opened a layer beneath*, and one LOW mechanism inaccuracy carried
over verbatim from the prior verdict. Both are backlog-grade; neither blocks the
cycle from terminating.

### 1. [MEDIUM] "Claim on `main`, then branch" leaves *how* a parallel session reaches a `main` checkout unstated — and the worktree substrate makes that non-trivial.

Fix 2 correctly routes the claim to `main` so the collision can fire. But the
doc's own substrate is **one worktree = one branch**, and I confirmed git
refuses to check out `main` in a second worktree (`fatal: 'main' is already used
by worktree at …`). So `main` lives in exactly **one** checkout — the primary
one. A parallel session therefore cannot commit its claim to `main` from its own
worktree; it must make the claim in the **shared primary checkout** *before*
`git worktree add`. Two frictions the text never resolves:

- The *trigger* section (36–38) tells a known-second session it "works in a
  worktree **from its first action**." But the claim is now its first action and
  it lands on `main` — i.e. in the shared primary checkout, not the worktree.
  The two sections read in opposite directions and are not cross-referenced.
- The dirty-tree rule (42–43) forbids touching a stranger's shared checkout. A
  claim is an atomic one-line edit + immediate commit + push, so in the
  solo-default steady state (primary tree clean) it's the benign
  "two sessions landing on the same integration branch" case sync-bookends
  already cover (92–93) — but the doc never *says* this, so an adopter meets the
  question "main is checked out in the other session's worktree; how do I commit
  my claim to it?" with silence. (An adopter using two clones rather than
  worktrees has no issue — each clone has its own `main` — which is exactly why
  naming the substrate assumption matters.)

**Concrete fix:** add one sentence to the "Where the claim lands is load-bearing"
paragraph: the claim is made **from the primary `main` checkout** (a fast
edit → commit → push), *before* `git worktree add` — it is the same
integration-branch landing the sync-bookend rule already sanctions, not a second
session working inside another's tree; then the worktree is created for the work.
Optionally add a back-reference from the trigger section's "worktree from its
first action" noting the claim commit precedes the worktree.

### 2. [LOW] The parenthetical mechanism "(git's three-line diff context overlaps)" is inaccurate — the real boundary is *zero* unchanged lines between the changes.

The behavioural claim (adjacent one-line items → keep-both conflict) is correct
and verified. But the stated *reason* is wrong: I drove it live — two claims with
a **single** unchanged line between them rebase **cleanly**, which cannot be true
if a three-line context window governed (a one-line gap would still overlap and
conflict). The operative threshold is **adjacency with no unchanged line
between**, not three lines of context. This phrase was carried over verbatim from
the prior verdict's own finding 6, so it's an inherited imprecision, not a fresh
error — but in a repo whose whole point is grounding (EVIDENCE §2: never state a
mechanism with more confidence than its evidence), a wrong mechanism sitting next
to a correct behaviour is worth correcting.

**Concrete fix:** replace "(git's three-line diff context overlaps)" with
something like "(adjacent changed lines with no unchanged line between them can't
be cleanly separated by the three-way merge)" — or simply drop the parenthetical;
the behavioural claim stands on its own and is what the reader acts on.

---

*Cycle status: this pass returns **no MAJOR**, so per REVIEW.md
("closes when a pass returns no MAJOR") the review cycle for the Claiming-work
section **terminates here**. The two findings above are the principal's to decide
and, if taken, fold into the ROADMAP follow-ups slice — they do not spawn another
full ceremony. Findings on self-authored doctrine: per REVIEW.md rule 3 the
disposition is the principal's, not the author's.*

---

## Decision — Mike, 2026-07-13: both [fixed]

Ruled directly: **take both.** Applied same day to `method/CONCURRENCY.md`; the
cycle was already closed (no MAJOR), so these corrections spawn no further pass.

1. **[fixed]** — the "Where the claim lands is load-bearing" paragraph now states
   the claim is made **from the primary `main` checkout** (fast edit → commit →
   push) *before* `git worktree add`, names it as the sync-bookend integration
   landing (not a second session inside another's tree), and notes separate-clone
   adopters skip the issue. A back-reference added to the trigger section's
   "worktree from its first action" (the claim precedes the worktree).
2. **[fixed]** — the inaccurate "(git's three-line diff context overlaps)"
   parenthetical replaced: adjacency is **no unchanged line between the two
   lines**; a one-line gap already rebases clean (reviewer-verified live).
