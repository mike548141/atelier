# Cold review — doctrine "Pointing up: the child-to-parent route, and the two canonical-block fixes"

**Status: BRIEF ONLY — the review has NOT run.** Written 2026-08-21 by a
Mike-opened `claude-fable-5` session pointed at "any reviews and fable
dependent work"; it authored neither the delta (an atelier session,
2026-08-18) nor this section's items. Per Mike's rule for such sessions
(2026-08-15), *the session that writes a brief does not run its review* — so
this waits for a **further** cold Fable session that neither the delta's
author nor this brief's writer started or instructed; tier checked at
selection (REVIEW.md rule 4). The reviewer appends its verdict below the
`---` and states its own spawn provenance there.

**Brief-writer's exposure, disclosed:** this writer read the delta commit's
message and the seven `method/` diffs (as pin-bump catch-up work for two
child repos, earlier the same session, before taking this item) and applied
the corrected concurrency wording in those two children's floor blocks. The
**intent records were left unopened** — the section README (which carries
Mike's 2026-08-18 ruling), `docs/sessions/2026-08-18-0746-…`, and the
`SESSIONS.md` entry — so this brief is written from the delta and the queue
pointer only, and carries no account of the author session's reasoning
beyond what the delta text itself asserts.

- **Subject**: the delta of `f9eda42` (2026-08-18), whole — **doctrine by
  function** (REVIEW.md rule 3), so rules 3 and 4 bind:
  - `docs/method/PROPAGATION.md` — new § *Pointing up — when a child earns a
    house rule* (~150 lines: the check-the-parent-first rule, the
    whose-rule-is-it test, the four-step route, the closing-the-loop rule,
    § The instance), and the reworked concurrency bullet of § *The standard
    child doctrine block*.
  - `docs/build/templates/CLAUDE.md` — the same bullet, which the scaffold
    stamps into every new child.
  - `docs/method/CONCURRENCY.md` — § *The trigger* gains the whole-index
    clause and a *Bearing* recording the 2026-08-18 incident.
  - `docs/method/GUARDS.md` — § *A rule with no home is not a rule* gains
    the cross-repo paragraph routing house-shaped rules to § Pointing up.
  - This section's items (`010`–`050` as landed) and the CHANGELOG entry.
- **Type**: doctrine cold pass — a rule that governs every future child
  session's behaviour at the child/parent seam, stamped into the fleet at
  pin bumps.
- **Scope** (point, don't paste):
  - The four delta surfaces above, at HEAD — including whether the four
    files tell one consistent story of where the index rule lives.
  - The queue pointer
    ([`050-…`](../roadmap/310-pointing-up-the-child-to-parent-route/050-rule-4-cold-pass-queued-pointing-up.md))
    and the sibling items `010`–`040` as the delta's own account of itself.
  - Intent record: the section
    [`README.md`](../roadmap/310-pointing-up-the-child-to-parent-route/README.md)
    (Mike's commission and his 2026-08-18 ruling on the child-side
    allowance) and the session record
    [`2026-08-18-0746-…`](../sessions/2026-08-18-0746-pointing-up-the-child-to-parent-route.md)
    — under the reviewer's own deferral discipline.
  - Neighbours it must not contradict: PROPAGATION § *The layer-override
    rule*, § *Who is a child*, § *One statement, stamped copies*, § *When a
    rule keeps breaking*; CONCURRENCY § *Claiming work* and § *Stay in your
    lane* (the route asserts that filing a finding in the parent's board
    *is* the lane — test that against the rule as written); GUARDS' three
    axes and the fourth requirement; the public-repo constraint (this repo
    is public; the instance describes a private child).
- **Load-bearing claims the record rests on** (extracted from the delta
  text, not evaluated — the reviewer decides which are load-bearing and
  adds its own):
  1. The house had no gap: `git diff --cached` at CONCURRENCY § The trigger
     always covered unstaged paths, and the child's second rule sits
     verbatim at § Claiming work.
  2. The 2026-08-18 incident is as described: a session staged two paths
     explicitly, committed, and destroyed a sibling's session-log entry
     that predated its arrival in the shared index.
  3. The old block phrase ("read the staged hunk headers") and its pointer
     (§ The channel) were both defective, and both are fixed in the
     canonical block and the template by this commit.
  4. Ten children carry the defective block and each clears it at its next
     pin bump (item `030`'s count).
  5. The whose-rule test — *would this rule be true in a repo that shares
     none of this repo's stack?* — partitions child rules from house rules,
     with the learned-on-a-stack seam stated.
  6. A pending-upstream line is a **narrowing** under § The layer-override
     rule, and being dated, addressed and self-removing is what separates
     it from a second original.
  7. Mike ruled the child-side allowance on 2026-08-18, in preference to
     leaving the child unprotected in the window.
  8. GUARDS § A rule with no home and this route are complementary, not in
     tension: evidence stays in the child's record, the rule travels to
     where it governs.
  9. Nothing enumerates upward debt; the section is honestly rung 1 until
     the queued instrument (item `020`) exists.
  10. The instance carries the class and never the private child's
      specifics, as the public-repo constraint requires.
- **Grounding — what the reviewer can run or read**:
  - Re-run claim 1 against HEAD: read CONCURRENCY § The trigger and
    § Claiming work and check the delta's account of them is byte-honest.
  - Diff the canonical block against `docs/build/templates/CLAUDE.md` —
    the two stamped statements of the same bullet must match.
  - Re-derive claim 4's count from the fleet enumeration the repo ships
    (`tools/floorfleet.py`, read-only) or the pins list — and note that
    child bumps after 2026-08-18 (two landed 2026-08-21) change the live
    count without changing the item's truth at its date.
  - `tools/board.py`-rendered index lines for this section's items;
    `pointerscan` behaviour on the `050` pointer.
  - The public commit log: does the instance's detail (two staged paths, a
    sibling's session-log entry, the date) let a public reader identify the
    private child? The class/specifics line is testable, not assumable.
- **Non-goals**: re-ruling Mike's 2026-08-18 allowance (the review may test
  the *grounds* the text records for it); designing the upward-debt
  enumerator (item `020`, queued); repairing the child repo's own records
  (its lane); the 2026-08-17 ruling round (separately reviewed and queued).
- **Prior verdicts to open only after your findings are durably written**
  (rule 2): none address this delta. Nearest relatives, pointed at not
  summarised: `2026-08-17-1000-channel-doctrine-cold.md` (the neighbouring
  CONCURRENCY §) and `2026-08-17-1321-bs1-wording-cold.md` (the claim
  mechanics the reworked bullet sits beside).
- **Deferred material**: the brief-writer's own attack angles are in the
  sibling `2026-08-21-0820-pointing-up-cold.deferred.md`. Open it as a
  deliberate second act, after your own findings are written; then fold it
  below the verdict and delete it (REVIEW.md rule 1).

---

# Verdict — UPHELD-WITH-CONDITIONS (2026-08-22)

**Spawn provenance, repeated from the claim (rule 4).** Reviewer: a
Mike-opened `claude-fable-5` session ("any reviews and fable dependent
work"), tier checked at selection. It authored neither the delta
(2026-08-18) nor the brief (2026-08-21), was started and instructed by
neither, and ran with no orchestrator — the judgement that formed every
finding below and the hand that commits the record are the same Fable
session. Claim: `cd23746`, pushed before the pass began.

**Exposure disclosed first, because the discipline requires the trace.**
This session read the `.deferred.md` sibling **before** running the pass —
at queue triage, in the same batch read that opened the brief, before
deciding to take the item. The findings below were formed and grounded
after that exposure, so this pass cannot claim its findings are
independent of the seeded questions; each finding that lands on a seeded
angle is marked `[seeded angle]`. The intent records (section README, the
2026-08-18 session record) stayed closed until the findings here were
durably written; the reconcile section below records what they changed.
Prior verdicts: none address this delta (per the brief); none were opened.

**Security lens instrumentation:** `/security-review` cannot read markdown
doctrine — its pass here is definitionally empty and weighed as nothing.
The lens ran by hand at design altitude: the public-repo exposure surface
is examined at PU-2.

## Load-bearing assumptions, named as my first act

The delta rests on: (a) the house rule *as operationally written* always
covered the alien-path case; (b) the anonymisation of the instance holds
as published; (c) the route is executable by any child session, not only a
well-placed one; (d) the ten-child count and the two block defects are as
swept; (e) the stamped copies and the canonical statement now agree. (d)
and (e) verified true; (a), (b), (c) each produced a finding.

## Findings

### PU-1 · MAJOR — the corrected rule still prescribes a check that cannot
### show what the correction says is the point

`CONCURRENCY.md` § *The trigger* at HEAD prescribes, as *the check that
sees* a shared-index collision: `git diff --cached -U0 | grep '^@@'` —
then, two sentences later (this delta's addition), says **"the paths it
shows that you never staged are the point of the check."** The prescribed
command **shows no paths at all**. Demonstrated live during this pass: with
an alien file staged alongside the session's own edit, its entire output is

    @@ -1,0 +2 @@ base
    @@ -0,0 +1 @@

— the alien entry is an anonymous hunk header, attributable to no file.
Plain `git diff --cached` (what the corrected child block prescribes) shows
both paths. Three consequences:

- **The stamped copy is now more correct than its canonical source.** The
  block and template say "read the whole staged index — `git diff --cached`
  shows the paths you did not stage"; the canonical section still routes
  the reader through the path-stripping pipe. That is the exact inversion
  (§ *One statement, stamped copies*) this delta exists to teach against,
  landed by the commit that teaches it.
- **Claim 1 ("the house had no gap") overreaches.** The whole-index *diff*
  always covered the case in principle; the operational one-liner obscured
  precisely the information the new clause names as the point. The child's
  misreading was wrong about coverage — and the honest statement is "a
  smaller gap than the child found, not none": detection by unexplained
  extra hunk headers, identification by nothing.
- **Item `030` propagates the confusion**: its `shed` note calls the
  `-U0 | grep '^@@'` variant the form that lets "a reader there reach the
  whole index without the parent" — reach it blind, on the evidence above.

**Condition:** fix the one-liner at source (plain `git diff --cached`, or
`--cached --stat` before the `-U0` read), and align item `030`'s shed note.
Falsified by: any invocation of the prescribed pipe that names a path.

### PU-2 · MODERATE — the anonymisation is defeated by its own section
### `[seeded angle]`

Claim 10 ("the instance carries the class and never the private child's
specifics") is false **as a system property**. § *The instance* says "a
private child"; item `040` in the same section, public in the same commit,
quotes the principal naming **cbom** and orders the revert of "the changes
cbom has made to claude.md"; item `010` links the instance to the block
fixes. A public reader joins the veil to the name in one hop. The naming
was the principal's own word in his ruling — the defect is not that it
exists but that the section *also* wears an anonymising veil that no longer
protects anything, in the very doctrine that teaches "carry the class,
never the repo". Stakes: `cbom` has no public remote; its name is already
public throughout this repo's docs; the linkage newly publishes only the
incident's association with it — but `cbom` is a client-engagement repo,
which is precisely the class step 2 exists for. **The principal rules:**
keep the naming and drop the veil (honesty over cosmetics), or scrub the
linkage; the current state is the one shape with neither property.

### PU-3 · MODERATE — the route's first step is machine-shaped, and the
### live exercise already ran a variant the text does not describe
### `[seeded angle]`

Step 1 as written reads as the child session writing a board item into
atelier's `docs/roadmap/` — sanctioned by § *Stay in your lane*'s
queue-never-deliver carve-out, verified at HEAD ("the auditing session may
queue what it found in the target repo's own roadmap … Queue, never
deliver"), so the lane claim itself holds. But the route's celebrated first
exercise (section `320`, hours after landing) did something the text never
names: the child **sent findings over the cross-session channel** and an
atelier session did the filing. And a child with neither a sibling atelier
checkout nor a live channel — a fresh clone elsewhere, a CI context — has
no route at all; the text is silent. Three shapes deserve a sentence each:
write the item directly (carve-out), hand it over the channel (the worked
example), and hold-and-flag when neither exists. Falsified by: text in
§ *The route* naming the alternatives — none exists at HEAD.

### PU-4 · minor — "self-removing" is a hope with a watcher gap the step
### itself does not admit `[seeded angle]`

Step 3 distinguishes a pending-upstream line from a second original partly
by it being "dated, addressed and self-removing". Nothing removes it —
the *pin bump* is the occasion, a session is the actor, and nothing watches
for a line that outlives its parent item (`stampscan` cannot see unstamped
text; the enumerator is item `020`, unbuilt). The section's closing
paragraph is honest about the route being unwatched; the *step* still
carries the word doing unearned work. Honest wording: "removable at the
next pin bump, and watched by nobody until `020` lands."

### PU-5 · minor — `pins.py` reports a wrong denominator from a worktree,
### silently

Run from this review's worktree, `pins.py` printed "1 of 1 not current"
(`wt-cite`) — its sibling discovery is CWD-relative, so it enumerated
`/Users/mike/worktrees` instead of the fleet, with no warning that the
denominator was wrong. It matters here because item `030` names "the pins
list" as a way to re-derive the ten-child count, and this pass's own
grounding tripped it (`floorfleet.py`, run from the same directory, found
the fleet correctly). Queue-able tool defect, not a doctrine one.

## The load-bearing claims, verified

1. **Partially holds** — see PU-1: the whole-index diff covered the case;
   "no gap" overreaches the operational check. The § *Claiming work*
   verbatim half stands per item `040`'s recorded verification; the
   child-side text is out of this pass's lane to re-read in detail.
2. **Corroborated in outline** — the child's own history shows a
   concurrency-guard write to its `CLAUDE.md` in the incident window
   (read for existence, not content; a private client repo's details stay
   in its lane).
3. ✅ **Byte-honest.** The pre-fix template at `f9eda42^` carries exactly
   *"read the staged hunk headers before every commit (`CONCURRENCY.md`
   § The channel)"* — phrase and pointer both as quoted, both fixed, and
   the canonical block and template match byte-for-byte at HEAD.
4. ✅ **Re-derived by hand sweep this pass** (the enumerator does not
   exist; `pins.py` misfired — PU-5): seven children still carry the old
   phrase at 2026-08-22 (`derry-hill`, `kainga`, `ros`, `rpi`, `shed`,
   `stewart-drive`, `tuhura`); `faves` cleared 2026-08-18, `cbom` and
   `docker-heap` at their 2026-08-21 pin bumps — **ten at the delta's
   date**, matching item `030`'s list exactly. Both 2026-08-21 bumps
   cleared **both** defects (phrase and pointer), so the closing-the-loop
   rule's "the pin bump is a sufficient occasion" held in both live cases.
5. ✅ **The test partitions the hard cases cleanly.** Run against the
   estate's real lessons: *responses carry secrets* (learned on one stack,
   true of any API-consuming repo → house's); *never record a capability
   as absent without reading the error* (gcloud-learned, tool-generic →
   house's); *ZFS hands-off* (names one stack's substrate → child's). The
   learned-on-a-stack seam carries the first two without swallowing the
   third.
6. **Weakened, not overturned** — PU-4: "dated, addressed" hold;
   "self-removing" is currently aspiration.
7. **Confirmed as recorded** — the ruling's grounds are stated in the
   delta and the intent record (read at reconcile) matches; re-ruling it
   is a non-goal honoured.
8. ✅ **Complementary, verified at HEAD** — GUARDS' new paragraph routes
   without contradiction, and the evidence/rule split (step 4) is stated
   on both surfaces. The route also passes GUARDS' fourth requirement the
   honest way: its failure mode is declared ("a route, currently
   unwatched") rather than papered over.
9. ✅ **Honest** — rung 1 stated in the section, the enumerator funded at
   `020`, and nothing found that contradicts the admission. Answering the
   seeded worry directly: nothing structural stops rung-1-and-honest
   becoming a resting state *except* the funded item and the drift line —
   which is exactly what the section says, so the honesty is real.
10. ❌ **False as a system property** — PU-2.

## Why UPHELD-WITH-CONDITIONS rather than UPHELD

The route is sound, already exercised as designed (section `320`: three
findings filed class-only, parent checked first, verified adversarially in
both directions), the block fixes are real, byte-honest, and already
propagating, and the count was swept, not estimated. But the delta's
central mechanical correction is **incomplete at its own source** (PU-1) —
the canonical section now contradicts its stamped copies about what the
prescribed check shows, which is the defect class this whole section
exists to end. Conditions: PU-1's source fix; the principal's ruling on
PU-2. PU-3–PU-5 are backlog-shaped. Per rule 3, nothing here is applied by
this session: findings on self-authored doctrine are the principal's to
decide, and the delta's author may append its counsel below, labelled.

## Reconcile — the intent records, opened after the findings

Both records (section README; session record `2026-08-18-0746-…`) match the
delta's account of the commission, the ruling, and the sweep — claim 7's
grounds are as recorded, and the ruling was taken informed ("asked with the
impacts of each option stated first"). Two things they add to the findings:

- **PU-1 was in the author's model, not just the text.** The session record
  states: *"The parent's actual rule runs `git diff --cached -U0 | grep
  '^@@'` over the whole index, and covers precisely that case"* — the exact
  confusion the finding names, in the author's own account; and the README
  states the same rule as plain `git diff --cached`. The two intent records
  disagree with each other about what the command is, which is the finding
  in miniature.
- **The cbom naming originates with the principal** (his commissioning words,
  quoted in both records), which is why PU-2 is framed as a ruling to make —
  veil or naming, one of the two — rather than a leak to attribute.

## Deferred questions, folded (opened after the reconcile was drafted;
## exposure at queue triage disclosed above)

The seeded questions, with where each landed:

1. **Byte-honesty of the quoted phrase/pointer** — ✅ verified byte-exact
   against the pre-fix template at `f9eda42^` (claim 3).
2. **Is "self-removing" a mechanism or a hope?** — a hope: PU-4.
3. **Hard cases for the whose-rule test** — the test partitions all three
   cleanly (claim 5).
4. **Does the instance leak the child?** — yes, via its own sibling item:
   PU-2.
5. **The lane carve-out** — holds as asserted; § *Stay in your lane* at HEAD
   sanctions queue-never-deliver in the target repo's roadmap (PU-3 notes
   what the step still fails to say).
6. **The unreachable-parent case** — confirmed silent; the route is
   machine-shaped: PU-3.
7. **Rung-1 honesty vs § When a rule keeps breaking** — stated honesty is
   the compliant shape here; the ladder escalates on recurrence, not on
   landing; the guard against rung-1-forever is item `020` plus the drift
   line, which is what the section says (claim 9).
8. **The ten-children count** — re-derived by hand sweep; ten at the delta's
   date, seven at 2026-08-22, both 2026-08-21 bumps cleared both defects (claim 4).

The sibling's text, folded verbatim per the lifecycle (its header trimmed):

> 1. **Byte-honesty of the quoted block phrase.** § The instance rests on the
>    child having reasoned from the exact phrase *"read the staged hunk
>    headers"* and the pointer *§ The channel*. Are both quoted byte-exactly
>    from what children actually carried (the template's git history shows the
>    pre-fix block)? A ruling-bearing narrative resting on an inexact
>    quotation is a known house failure shape.
> 2. **Is "self-removing" a mechanism or a hope?** Claim 6 distinguishes a
>    pending-upstream line from a second original partly by it being
>    *self-removing* at the next pin bump. Nothing named watches for a line
>    that survives its parent item — stampscan cannot see unstamped text by
>    its own admission, and the section calls itself rung 1. Does the
>    distinguishing property therefore do any work, or is the honest wording
>    "removable, and watched by nobody"?
> 3. **Hard cases for the whose-rule test.** Run the estate's real recent
>    lessons through it: *responses carry secrets* (learned on TrueNAS —
>    provider-generic?), *never record a capability as absent without reading
>    the error* (learned on gcloud), the ZFS hands-off constraint
>    (stack-specific?). Does the test partition these cleanly, or does the
>    learned-on-a-stack seam swallow the test?
> 4. **Does the instance leak the child?** The public text says "a private
>    child, 2026-08-18" plus: two explicitly staged paths, a destroyed
>    sibling session-log entry, an index predating the session. Combined with
>    the fleet being enumerable from this public repo, is the child
>    identifiable? If yes, is that within the class-not-specifics line or
>    over it?
> 5. **The lane carve-out is asserted, not cross-referenced.** Route step 1
>    says filing in the parent's board "is the lane" and cites
>    CONCURRENCY § Stay in your lane. Does that section's text actually admit
>    this reading at HEAD, or does § Pointing up widen a rule that still
>    reads queue-in-the-target-repo (the child files in *atelier's* board —
>    which repo's lane is that)?
> 6. **The unreachable-parent case.** The route assumes a sibling atelier
>    checkout. A child session on a machine without one (a fresh clone
>    elsewhere, a CI context) cannot file in the parent's board. Where does
>    the rule go then — and does the doctrine say, or is the route silently
>    machine-shaped?
> 7. **Rung-1 honesty vs § When a rule keeps breaking.** The section admits
>    it is rung 1 and unwatched. Does the parent doctrine require more before
>    this counts as landed (an enumerator, a check), or is stated honesty the
>    compliant shape? If the latter, does anything stop rung-1-and-honest
>    becoming the resting state for every hard rule?
> 8. **The ten-children count.** Re-derive it. Does it count every repo with
>    a stamped floor block (shed, the private children, the public ones), and
>    was it true at 2026-08-18? Two children bumped 2026-08-21 (their floor
>    blocks now carry the corrected wording) — check the closing-the-loop
>    rule's claim that the pin bump is a sufficient occasion by whether those
>    two bumps actually cleared both defects (the phrase AND the pointer).
