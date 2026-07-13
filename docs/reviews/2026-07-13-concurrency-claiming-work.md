# Review brief — CONCURRENCY "Claiming work" section

**Reviewed:** `docs/method/CONCURRENCY.md` § *"Claiming work — make selection
collide like naming does"* (lines 132–195), landed in commit `534bfe9`. Read
against the whole of `CONCURRENCY.md` for coherence, plus `REVIEW.md`,
`EVIDENCE.md`, and the live `ROADMAP.md` it operates on.

**Commissioned:** cold, un-briefed, self-authored doctrine — reviewer chose its
own attack surface (REVIEW.md rule 1); no prior review read before the findings
below were drafted (rule 2); findings are the principal's to decide, not the
author's (rule 3). The author's session log / commit message framing ("generalises
the record-ID bearing", "zero cost to the solo default") was treated as a claim to
test, not settled scope.

**Attack surface I named first (before reading the section's own framing of what
matters):** (1) the mechanism only fires if every concurrent session actually
*claims* — what flips a session into claim-mode, and who is left out? (2) where
does the claim commit physically land, given worktrees are on separate branches
whose pushes never collide? (3) does the "fan-out at leaf grain" property survive
a real roadmap, or does it assume a decomposition the roadmap doesn't have? (4)
is the git behaviour it promises ("same item → conflict, different item → silent")
actually what git does? (5) does an off-estate adopter have the substrate (a
git-tracked markdown queue) the whole mechanism assumes? (6) does "release =
put-away, nothing separate to forget" match what the referenced section actually
carries?

**Method:** claims verified mechanically where possible — the same-line and
adjacent-line rebase behaviours were driven live in throwaway repos (results in
findings 1 and 6); the leaf-grain claim was checked against the actual
`ROADMAP.md` structure; the release-path and record-ID claims were cross-read
against the sections they cite.

---

## Verdict: PASS-WITH-FINDINGS

The core mechanism is sound and honestly grounded: forcing selection onto one
shared line so a same-item double-claim lands as a trivial same-line rebase
conflict **works** (verified live), it coheres with the doc's "make the silent
collision a visible git conflict" spine, and the incident it grounds on is real
and specific. It does not contradict the KISS/no-locking line in a way the text
doesn't already reconcile (it pre-empts "no lease timer, no lock server"), and
the "generalises the record-ID bearing" claim is defensible — the record-ID bullet
already frames its own worst case as "two sessions wanting the same name is a
visible git conflict, the trivial kind", which is exactly the property claiming
reuses. (Caveat worth a footnote, not a finding: coordination-free naming *avoids*
the shared resource in the common case while claiming *manufactures* one — same
conflict-shape, opposite lever on shared state. The "same move" language is true
of the structural worst case, slightly loose about the direction.)

But one MAJOR gap means the section does not fully close its own grounding
incident, and four MEDIUM gaps would leave an adopter — or a future session on
this estate — unable to apply it as written without filling in load-bearing
detail the text omits.

### 1. [MAJOR] The mechanism is gated to worktree-mode, but nothing reliably flips a session into worktree-mode for a *selection* collision — so the grounding incident can recur unclosed.

Claiming is explicitly "a worktree-mode discipline … A session alone on the repo …
claims nothing." Worktree-mode fires on one of two triggers (per *The trigger*
section): the principal's **say-so at open**, or the **dirty-tree backstop**. The
dirty-tree backstop **cannot** detect a selection collision: (a) the section tells
every session to commit-and-push its claim *before* any work, so nothing lingers
uncommitted to be discovered; and (b) parallel sessions live in **separate worktree
directories** and never see each other's working tree at all. So the *only* trigger
that switches claiming on is the principal explicitly saying "you are a parallel
session."

That is precisely the condition the grounding incident violated: sessions "each
told only 'the next thing in the queue'." If the principal fans out N sessions with
that instruction and does *not* flag each as parallel, none enters worktree-mode,
none claims, and the duplication recurs exactly as before — the new doctrine never
fires. The section closes the incident only under an unstated precondition (the
principal now always flags concurrency at open) that is itself the thing that failed.

There's a second, quieter case even when flagging works: a session opened first as
*solo* (trunk-based, claims nothing) is still mid-item when a second, flagged
session opens, reads the roadmap line as `[ ]`, claims it, and both build it. The
first session never retroactively claims.

**Fix (author's suggestion, principal decides):** decouple claiming from
worktree-mode. Claiming an item you pick from the *shared* queue costs one commit
whether or not you're isolated — make it unconditional on *selection from the shared
roadmap*, not on worktree-mode. That preserves "zero standing ceremony for solo"
(a genuinely-alone session's claim simply never collides) while closing the hole
that a session which *didn't know* it was parallel leaves open. If claiming is to
stay worktree-gated, the section must state plainly that its precondition is
"every concurrent session is flagged parallel at open," name the un-flagged first
session as an uncovered residual, and stop implying it closes the fan-out incident
that arose from exactly that un-flagged case.

### 2. [MEDIUM] Where the claim commit lands is unspecified — and the whole push-reject/rebase story only works if it lands on the shared integration branch, which contradicts the worktree-branch model.

The mechanism's narrative ("Push succeeds → yours; Push rejected → pull --rebase →
same-line conflict") is a *shared-branch* story: push rejection and rebase happen
only when two commits target the same ref. But the doc's substrate is one
**worktree = one branch**, and two different branches' pushes **never** collide —
each succeeds, and neither session sees the other's claim until a much later PR
merge. For the collision to fire as described, the claim commit must go to the
**integration branch (`main`)** that every session `pull --rebase`s, *then* the
session enters its worktree/feature branch for the work. The section never says
this. An adopter who reasonably commits the claim on their feature branch (where
all their work lives) gets a claim that is invisible to every other session and a
mechanism that silently does nothing.

**Fix:** state explicitly that the claim is committed and pushed to the *integration
branch* (the branch all sessions share and rebase onto) *before* creating/entering
the worktree for the work — the claim is a direct-to-main commit even though the
work is not.

### 3. [MEDIUM] The "fan-out at leaf grain" property assumes a roadmap already decomposed into per-leaf lines; the actual ROADMAP bundles many items per line, where the mechanism *serialises* instead of fanning out.

The section claims two sessions both told "do the reviews" each claim a *different*
review item and coexist — "what lets one themed instruction fan out across sessions
without collision." That holds only if each review is already its own claimable
line. The live `ROADMAP.md` is the counter-example: the review-owed backlog carries
`REACH/AUTONOMY backlog — the cold pass's H1–H8 + residuals` as **one line** for
eight findings, and there is no per-review enumeration for a "do the reviews"
theme. Two sessions handed a bundled/themed line both claim that **one** line →
same-line conflict → one wins, the other takes the *next* line (a different theme),
not a different leaf of the same theme. The result is serialisation of themed work
— the opposite of the advertised fan-out.

**Fix:** name the precondition — fan-out requires the leaves to *exist as their own
lines*; a themed or bundled line must be split into claimable per-leaf lines before
it can fan out, otherwise the theme is claimed as a unit and serialises. (This is a
real constraint on the estate's own lean-roadmap habit, not just adopters.)

### 4. [MEDIUM] "Release is put-away … no separate release step to forget" overclaims: the referenced put-away ceremony contains no line-reversion step, so on abandonment the `[~]`→`[ ]` revert *is* a separate step.

The section delegates release to *Every branch ends put away* and asserts "There is
no separate release step to forget." But that section's abandonment procedure is
**salvage → tag → delete → record** — it says nothing about a roadmap line (it
predates this section and governs branches, not the queue). For the completion path
the line goes to `[x]` as part of finishing, fine. For the **abandonment** path, the
put-away ceremony deletes the branch and records the decision but leaves the roadmap
showing `[~]` — reverting it to `[ ]` is an extra, manual, easily-forgotten step,
which is exactly what produces an orphan-looking `[~]` (finding-5 territory) even
after a *clean* abandonment. So the claim "nothing separate to forget" is untrue for
the path most likely to forget it.

**Fix:** either add the line-reversion explicitly to the put-away section's
abandonment procedure (making the claim true), or drop the "no separate step to
forget" reassurance and name `[~]`→`[ ]` as a step of abandonment that the session
must perform.

### 5. [MEDIUM] The mechanism is hard-coupled to "the queue is checkbox lines in a git-tracked markdown file" — an adopter whose queue is an issue tracker cannot apply any of it, and no alternative is named.

Every moving part — editing a line in place, the same-line rebase conflict,
`pull --rebase` before push — requires the work queue to be **text lines under git**.
An adopter running their backlog in GitHub Issues / Projects / Jira (a common case,
and this doc is explicitly built to be shareable) has **no shared text line to
collide on**; the entire mechanism is inapplicable to them and the section offers no
substitute. This is a silent applicability cliff.

**Fix:** state the precondition (the queue must be a git-tracked text file for this
mechanism to work) and, for tracker-based queues, point at the tracker's own claim
primitive (assignee / status transition) as the equivalent — outside this
mechanism's scope but named so the adopter isn't left with a dead rule.

### 6. [MEDIUM] "Different items → different lines, no conflict, both proceed … silent everywhere else" is empirically false for *adjacent* items — the common case in a lean one-line-per-item roadmap (the section's own example).

Verified live: two sessions claiming items on **adjacent lines** (consecutive
single-line items, no blank line between) produce a rebase **CONFLICT**, not the
promised silent pass — git's 3-line diff context overlaps. Items **≥2 lines apart**
rebase cleanly. So the "resolves *exactly* at the contested grain and stays silent
everywhere else" guarantee holds only when claimed items are separated; for a dense,
lean, one-line-per-item roadmap — which the section's own example models
(`- [~] REACH/AUTONOMY backlog …`) — two sessions claiming *neighbouring* items
collide spuriously. The conflict is trivial to resolve (keep both edits), so the
harm is small, but the absolute "no conflict, both proceed" claim is wrong and an
adopter reasoning from it will be surprised.

**Fix:** soften the guarantee — a same-item claim is a genuine "yield" conflict; a
different-but-adjacent-item claim may raise a *keep-both* conflict that is trivial
but not silent. And state that the `[~]` marker always goes on the item's **checkbox
line** (for multi-line items) so the same-item collision reliably fires on one line.

### 7. [LOW] Orphan reclaim: "its timestamp bounding how long is too long" over-reads a claim-*time* stamp — a long-but-live task and a dead orphan are indistinguishable by timestamp alone.

The section's real staleness signal is sound and stated ("branch/worktree is gone
and … commits have stopped"). But "timestamp bounding staleness" leans on the wrong
fact: the recorded timestamp is *claim time*, not last-activity time, so a large
legitimately-in-progress item claimed six hours ago carries the same old timestamp
as a dead orphan claimed six hours ago. The branch-existence + commits-stopped test
already does the real work; the timestamp adds little and risks implying a time
threshold the section elsewhere disavows ("not a clock that fires").

**Fix:** demote the timestamp from "bounds staleness" to "a tiebreak fact once
branch-gone + commits-stopped already indicate staleness" — keep branch existence
as the primary signal it already is.

---

*Reviewer note per REVIEW.md: this is a verdict on self-authored doctrine, so every
finding above is the principal's to decide — tag each [fixed] / [backlog] /
[rejected: grounds] in this file; the author applies nothing on its own. The MAJOR
(finding 1) is the one to rule on first: it decides whether the section closes its
grounding incident or merely names a mechanism that fires under a precondition the
incident itself broke.*

---

## Decision — Mike, 2026-07-13: all seven [fixed]

Ruled directly: **take all seven.** Applied same day to
`method/CONCURRENCY.md` by the section's author (a neutral applier wasn't
required — these are corrections to self-authored doctrine the principal ruled,
not a fresh doctrine call), decisions stamped here.

1. **[fixed] — decouple (the reviewer's option A, not the document-the-precondition
   option B).** Claiming now fires on **selection from the shared queue**, not on
   worktree-mode; the worktree-gating and the "solo claims nothing" framing are
   gone. Simpler and strictly stronger — it closes the un-flagged-session case
   (both the fan-out incident and the solo-mid-item-when-a-second-opens case) that
   option B could only document as a residual.
2. **[fixed]** — the section now states the claim commit lands on the integration
   branch (`main`) *before* branching: "claim on `main`, then branch".
3. **[fixed]** — fan-out precondition named: leaves must exist as their own lines;
   a bundled/themed line is claimed as a unit and serialises. Split first to fan out.
4. **[fixed]** — the "no separate step to forget" overclaim dropped; `[~]`→`[ ]`
   reversion added both to the claiming section's release paragraph *and* to the
   put-away section's abandonment procedure (salvage → tag → delete → record → revert).
5. **[fixed]** — git-tracked-text-queue precondition named; tracker-based adopters
   pointed at the assignee/in-progress-column primitive as the equivalent.
6. **[fixed]** — the "silent everywhere else" guarantee softened: same-item = real
   yield conflict, adjacent-item = trivial keep-both conflict; `[~]` goes on the
   checkbox line so same-item collisions fire on one line.
7. **[fixed]** — timestamp demoted to a tiebreak; branch-existence is the primary
   staleness signal.

Also folded in the reviewer's footnote caveat (not a finding): the section now
says claiming *manufactures* the shared resource where coordination-free naming
*avoids* it — "same shape of move", honest about the opposite lever.

**Applied-batch cold pass owed** per REVIEW.md's cycle rule (the first pass
carried a MAJOR): a fresh un-briefed pass confirms the fixes landed and no new
MAJOR arose. Tracked in ROADMAP.
