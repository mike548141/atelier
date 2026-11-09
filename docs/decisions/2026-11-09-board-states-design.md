# Board states: two tiers, a tick that means done, and waiting as a field

**Status**: proposed (draft; binds nothing until Mike rules on it) •
**Date**: 2026-11-09

**Review**: owed. A rule-4 design cold pass before acceptance, because this
sets a file format about ten repos build to. It is Fable work and waits for
Mike's approval.

Commissioned on `310/160`; his words are on `310/060`. Prior analysis:
`310/060`, `310/070`, `010/100`, `310/080`, `420/020`. Nothing below is built.

## Outcome

Keep one list and one state line. Split the box into two classes (work owed,
no more work) and add **two** boxes: `[-]` *closed without being delivered*,
which is what makes the tick mean done, and `[/]` *partly delivered*, which
stops `[~]` meaning two things. A `[-]` carries a required word (not required,
superseded, duplicate, moved). A parent with child items gets a counted
roll-up, checked against its children. Waiting becomes a field beside the box,
never a box. Every change is additive, so no child goes red unannounced.

## His words on states, found and quoted

Searched: `instruments/cctranscript --search --all`, the term set *status,
statuses, brackets, not required, superseded, mixed, in-flight, tier, mock-up,
part-done* and the literal bracket forms, over 1,208 sessions in every repo,
keeping his own turns (typed and mid-turn), plus the option-pick channel for
July, and a grep of every board and record. Before this commission, six of his
messages across five sessions carry his own list of statuses, and one page he
endorsed shows them. If he recalls more, they sit outside what this search can
reach (other option-pick turns, or a page that was never quoted back).

| When (UTC), where | His words |
|---|---|
| 2026-07-22, atelier session `1b189e23` (mid-turn 8+1) | Four situations a parent and children can be in, then: *"those item state could be completed, not completed, claimed (work underway)?, supersceeded, declined, and maybe other states. But perhaps those more detailed states are in the commentary and the brackets can just indicated `[x]` = no more work to be done on this, `[~]` claimed/work underway, `[ ]` work needs to be done still. I may have the state labels/names and indicators in the brackets wrong but it gives you the idea"* |
| 2026-07-22, same session (mid-turn 8+2), three minutes later | *"We could extend those states if you thought it was a good idea e.g. `[x]` = no more work to be done on this · `[~]` claimed i.e. work is underway · `[-]` work declined e.g. no longer required/wanted · `[^]` work superceeded or delivered in a different way · `[ ]` work has not started and needs to be done still. It makes sense to me but I could be making it more complicated than it needs to be"* |
| 2026-08-16, a child session | *"be clear on what is claimed, in-flight, or still to do"* |
| 2026-08-18, a child session (the ruling on `310/060`) | *"I support the idea of adding more status for the brackets on a job item to make indexing them easier to understand the state of work (e.g. not done, done, claimed, in-flight, declined, supersceeded etc etc)"* |
| 2026-08-18, a child session | *"Give me a full view of all the work claimed, underway/in-flight, or to be done"* |
| 2026-10-03, atelier session `c3355b80` (39+3) | *"I remember us specifying only `[ ]` `[-]` and `[*]`. I was pushing to add more but you (claude) pushed back and I said we could wait until we have clear use cases"* |
| 2026-09-09, a child session | The page he asked to have offered to every repo (`320/280`) grouped work as *open*, *part done*, *waiting on you* and *your call* |
| 2026-11-09, this commission | Two tiers, a general class *"no more work to be done on this item and any children"*, child classes *"done / work completed"*, *"not required"*, *"supersceeded"*, *"duplicate"*, *"a mixed status or an in-progress for when there are child pieces of work"* |

**🔑 A record here is wrong, and it matters.** `310/080` says he *"never typed
`[-]`, never typed `[^]`, and never enumerated states"*. He did, in the two
mid-turn messages above. `cctranscript` could not see mid-turn messages until
2026-09-18 (`210/100`), so the 2026-08-19 verification read the transcript
without them. The July record that credited him was closer to the truth than
the correction was.

**🔑 The "tri-state ruling" is an answer.** On 2026-07-23 a session asked
*"Keep the three checkbox states, or extend to five?"* with a recommended
option, and he picked *"Keep three (Recommended)"*. By `420/020` that is an
answer. The option's text carried the condition: *"Revisit only if we
repeatedly need dispositions machine-separable."* The measurements below meet
that condition, and on 2026-11-09 he accepted a further status in terms.

Two standing facts bound the design. The board is for sessions: *"I will never
read the board because it exists solely for you to track the work"* (2026-10-03,
same session). And the marker question is ours to fix, not his to pick
(2026-10-03, his acceptance of the close that said so). So the questions at the
end are about outcomes, never glyphs.

## What the boards show

Read from each repo's `docs/roadmap/` item files on 2026-11-09: 2,494 items in
twelve split boards (atelier and eleven children). Single-file boards were not
measured. Counts are censuses unless marked **sample**; a sample was read by
hand, one pass, by this author, and is not extrapolated.

| Measure | Method | Result |
|---|---|---|
| States | First line of each item | `[ ]` 1,245 · `[x]` 1,189 · `[~]` 52 · `⏳` 8 |
| `[x]` naming a non-delivery end | Word on the state line (first 260 characters) or a "closed as …" phrase | 45 (3.8%); a floor, since most items carry no such word |
| `[x]` that were not delivered | **Sample**, 50 random items | 3 not delivered (one superseded, one question answered with no change, one framing retracted); 2 delivered with a named remainder still open |
| `[~]` holding a claim | `(claimed …)` on the state paragraph | 16 of 52; the other 36 have no claim at all, 35 of them in one child; 20 of the 52 mention a released or stale claim |
| `⏳` on an open item's state line | Word split | 162: 59 name a review, 86 name waiting on a person, a date or an event, 17 neither |
| Open items flagged 🎯 | 🎯 on the state line | 412 of 1,245 (33%) |
| Open items that are takeable | **Sample**, 40 random items, first paragraph only | About 20 takeable, 10 needing him, 5 waiting on something named, 3 ideas or held, 2 reviews queued |
| Open items whose state line says done | `DONE/FIXED/BUILT/…` near the head | 60, mostly an honest part-done (*"step 1 DONE — steps 2–4 open"*) with no state to say so |
| Parents whose children differ, by section | Folder-level, every section | 96 of 172 sections mix closed and open items |
| Parents whose children differ, by sub-line | Indented checkbox lines | 491 files have them; 132 `[x]` items hold an open one |
| Those sub-lines are real child work | **Sample**, 16 of the 132 | 3 are real open work; 13 are prose bullets that happen to carry a box |
| Answer or ruling marked on an item | Files with the glyph | `RULED` 337 · ⚖️ 44 · 💬 66 |

**What sessions got wrong because of a state.**
- Two child sessions read parked, ruled-not-to-fix and superseded items, all
  `[ ]`, as takeable (`310/060`, 2026-08-18).
- A session reported 20 reviews queued when none were: 27 items still wore `⏳`
  after their verdict landed (`130/020`, 2026-10-03).
- A deleted credential stayed the top open item, `[ ]` and 🔥, above its own
  *"DONE"* (`320/280`, 2026-09-09).
- Seven requirements were ticked and not done, found only when he asked
  (a private child, 2026-09-11).
- A whole Fable pass ran twice because a live pass read as dead (memory
  `running-pointer-means-live`, 2026-08-09).
- An item whose own text said *"unruled"* was built and merged, because an
  open box reads as takeable (memory `triage-summary-is-not-the-item`,
  2026-10-03).

## What depends on the states today

Children call atelier's tools and float on `floor.yml@main`, so a tool change
reaches all of them at their next run. `board --check` blocks and has no
advisory form.

| Reader | How it reads a state | Cost of a new box |
|---|---|---|
| `tools/board.py` | `STATE_RE` accepts `[ ]`, `[x]`, `[~]`, `⏳`; anything else is "no state line" and exits 1. Renders `[x]` as ✅ | Accept the boxes; map glyphs and words |
| `tools/pointerscan.py` | `_MARKER`; `[x]` is never a pointer; `⏳` means a review | Treat `[-]` like `[x]`, `[/]` like `[ ]` |
| `tools/harvestscan.py` | `ITEM_RE` | Add the boxes |
| `tools/sizescan.py` | `[x]` is cold, `[ ]`, `[~]`, `⏳` are live | `[-]` cold, `[/]` live |
| `instruments/ccclose` | `^- \[(.)\]` and `STATE_LINE`; counts **every** `[~]` as a live claim, so the 36 non-claims read as claims today | Tighten to the claim fragment; add boxes |
| The review-queue tool in a private child | `STATE`: `[ ]`, `~`, `x`, `⏳` | One-line regex change, in that child |
| `tools/floor.py`, `tools/floorfleet.py`, the other scanners | Read no item state | None |
| Legends: `docs/roadmap/README.md`, `docs/build/templates/docs/ROADMAP.md`, each child's copy, `CONCURRENCY.md` § Claiming work | Prose | Rewrite the house legend; children point at it instead of copying it (`310/060` traced one failure to a dropped clause in a copy) |

## Problems

1. **`[x]` means five things and wears one green tick.** Delivered, superseded,
   not required, duplicate and moved all render ✅.
2. **`[~]` means two things.** The legend says a live claim; 36 of 52 are a
   part-delivered item nobody holds. A session obeying the legend skips work
   that is free; `ccclose` counts them as claims.
3. **An open box hides why it is open.** About half of a 40-item sample is not
   takeable now, and the box says nothing.
4. **`⏳` means two things.** A queued review in the legend and in
   `pointerscan`; waiting in most of its 162 uses on `[ ]` lines.
5. **A parent has no state of its own.** 96 of 172 sections are mixed; item
   sub-lines cannot be counted because most are prose.
6. **Nothing on the line says who decided.** `RULED` covers rulings and answers
   alike (`420/020`), and a closed-as-not-needed item carries no basis.

## The proposed model

Tiers, tested against his two-tier idea. His general class holds, and it is the
*bracket's* job: "is any work left". His child classes are right, with one
exception worth saying plainly. He placed *"a mixed status or an in-progress"*
inside the no-more-work class. The evidence splits it: an in-progress parent
still owes work (so it cannot be terminal), while a closed parent whose
children ended differently is no-more-work. The model gives each its own home.

**Tier 1, the class: the box, one meaning each.**

| Box | Means | Live or closed |
|---|---|---|
| `[ ]` | Work owed, nothing delivered | Live |
| `[/]` *new* | Partly delivered; the remainder is named; nobody holds it | Live |
| `[~]` | Held now by a live session, with `(claimed …)` | Live |
| `⏳` | A review queued for a non-author, as today (`130/020`) | Live |
| `[x]` | Delivered. The tick means done | Closed |
| `[-]` *new* | No more work, and it was not delivered | Closed |

**Tier 2, the sub-class: one word after a `[-]`, required.** Each carries the
detail that makes it checkable, and the why stays in the item's text.

| Word | Requires | From his words |
|---|---|---|
| `not-required` (also declined or dropped) | A reason, and who decided | *"not required"*; his 2026-07-22 *"declined e.g. no longer required/wanted"* |
| `superseded` | The item that replaces it | *"supersceeded"* |
| `duplicate` | The item it duplicates | *"duplicate"* |
| `moved` | The repo and item it moved to | Measured: 13 on state lines |

A closed item is never reopened by editing the word: it gets a dated note and
a new item, which keeps history legible.

**Parents.** A parent's state is **declared and checked**, not computed. A
parent is an item that names real child items on one line of its own file
(`children: 020/381 020/382`). Only named board items count; a checkbox in the
body stays prose and tools ignore it, which is the sample's lesson. The
generator prints a counted roll-up on the parent's index line, and the check
reds a parent whose box contradicts its children: closed while a child is live.
A part-delivered parent is `[/]`; a closed parent whose children ended
differently is `[x]` with the roll-up showing the mix (*"2 done, 1 not
required"*), which is his "mixed" with no extra state. A section is a parent
for free: the generator can roll up its folder, and that is phase 2 of the
migration (it touches every section line).

**Waiting is a field, not a state.** Waiting changes while the work does not,
several reasons can hold at once, and a box cannot say two things. It is one
fragment beside the box, in the same family as `(claimed …)`, lifted to the
index:

`(waiting: him)` · `(waiting: 2026-11-18)` · `(waiting: fable)` ·
`(waiting: <repo>)` · `(waiting: evidence)`, each with a short reason in the
text.

A session takes `[ ]` or `[/]` with no claim and no waiting field. `⏳` keeps
its one meaning, and a child's other `⏳` becomes a waiting field when next
touched (`310/070`'s `⏳` half). "Parked" (*not now, maybe later*) is an open
item with a waiting field, not a closed one: he drew that line himself, of a
register: *"the register should have a lost state because it is quite
different to disposed as it may come back"*.

**Who may set what.**

| Move | Who | Basis |
|---|---|---|
| Open → claim, `[/]`, `[x]` | Any session | Evidence at landing, as today |
| `[-] superseded`, `duplicate`, `moved` | Any session | The named target, checked to exist |
| `[-] not-required`, on work Mike commissioned | Mike only | His words or his answer, recorded |
| `[-] not-required`, on a session's own filing | The session | A stated reason, marked as a session's call |

Who may close Mike's own commissioned work is put to him below.

**Answer or ruling.** Where a state rests on his decision, the line carries
⚖️ (a ruling: his own words, quoted in the file) or 💬 (an answer: his pick
from options a session wrote), and a session's own call carries neither. This
only fixes *where* the mark shows; the doctrine stays `420/020`'s.

**How it renders.** The index stays one list. A no-more-work item never shows
a green tick unless it was delivered.

| State line | Index line starts | A session reads it as |
|---|---|---|
| `[ ]` | `- [ ]`, unchanged | Takeable, if no waiting field |
| `[/]` | `- 🟡` with the remainder word | Takeable; part-delivered |
| `[~] (claimed …)` | `- [~] (claimed …)`, unchanged | Do not start |
| `⏳` | `- ⏳`, unchanged | A review to take |
| `[x]` | `- ✅`, unchanged | Done |
| `[-] not-required` | `- ⛔ not required` | Closed, not done |
| `[-] superseded by X` | `- 🔁 superseded` | Closed, see X |
| `[-] duplicate of X` | `- 🪞 duplicate` | Closed, see X |
| `[-] moved to X` | `- ➡️ moved` | Closed here, lives elsewhere |
| `(waiting: him)` beside any live box | `- [ ] ⏸️ him` | Not takeable; a decision or hands |
| parent with roll-up | Its box, then *"3 done, 1 live, 2 open"* | Read the children |

## Shapes compared

| Shape | Pros | Cons | Cost | Risk |
|---|---|---|---|---|
| **A. Two tiers: a small box set plus a word (recommended)** | The tick means done; a `[-]` line says why it closed; scanners keep one question | Two new boxes to learn; a word grammar to hold | `board.py`, four scanners, ccclose, one child's tool, legends | Low: additive; an unknown word fails loud at check |
| **B. Flat, more boxes: his July list (`[-]` declined, `[^]` superseded, one box per end)** | Closest to his mock-up; one glyph per state | Every new end adds a box and a change to all readers; a box cannot name a target, so prose is still owed | The same seven readers, per state | A box vocabulary that keeps growing with the next end |
| **C. A `disposition:` field or frontmatter (`310/060` option 2)** | Structured and queryable | Reverses the 2026-08-15 store decision (*"a second state vocabulary … would be one fact in two homes"*); every file changes | Highest: every item file and the parser | Drift between box and field, the class this repo has recorded most |
| **D. Render from prose words already on the line (`310/060` option 1)** | Cheapest; no format change | 45 items carry a word and 1,144 do not; unchecked, so a stale word misleads silently | `board.py` only | The false tick remains for the unlabelled majority |

## Migration: every child stays green

1. **Readers first, additive, in atelier.** `board.py`, `pointerscan`,
   `harvestscan`, `sizescan` and `ccclose` accept `[/]` and `[-]` and the word.
   Nothing renders differently, so no committed index goes stale. Children get
   this at their next run with no change of their own.
2. **Render only what is new.** `[x]`, `[ ]`, `[~]` and `⏳` keep their index
   glyphs, so no index changes until a child marks a line with a new box. No
   grace period is needed for this phase.
3. **Atelier first, as the worked example** (the 2026-08-15 pattern): re-mark
   atelier's own items by reading each one, then write the legend, the
   `CONCURRENCY.md` claim rule and the review tool's note.
4. **Children, per item, at their own pace.** The 36 non-claim `[~]` are read
   one by one to `[/]` or `[ ]`: 36 judgements, not a migration (`010/100`). The
   45 named `[x]` go to `[-]` the same way (question 3). Anything else stays as
   it is.
   `board --check` warns, never reds, on old shapes.
5. **The check tightens later, on a date, after the warning has run.** `[~]`
   without a claim, `[-]` without a word or target, a closed parent with a live
   child. A red never arrives unannounced.
6. **Phase 2, the one change that touches existing lines:** section roll-ups.
   Land it after `010/190` retires the 2026-11-18 grace, on that same
   accept-both-forms mechanism and with one shared end date, so two graces
   never overlap. Pre-existing `board --check` semantics do not change.

**Tools must change:** `STATE_RE`, `index_line`'s glyph map and a word parser
in `board.py`, with the `(waiting: …)` and `children:` readers; `pointerscan`'s
`_MARKER`; `harvestscan`'s `ITEM_RE`; `sizescan`'s `_COLD_ITEM` and `_LIVE_ITEM`;
`ccclose`'s `ITEM_STATE`, `STATE_LINE` and `CLAIM_LINE` (a claim needs the
fragment); and the private child's queue tool. Legends: the house one and the
template, with children pointing at it instead of copying.

## Rejected

- **One new status only:** what he first accepted, and what he asked to go
  beyond; it leaves `[~]` and waiting as they are.
- **Computing a parent's state from sub-line checkboxes:** the sample shows
  most of those are prose. A checkbox is not a child.
- **Waiting as states** (`[w]`, on-hold): waiting moves while work does not,
  and two reasons can hold at once; the state count would grow with every new
  reason.

## 🎯 Questions for him

Each is in plain language and checked against what he has already said.

**1. Who may decide a piece of work is not needed?** He has closed work himself
(*"close this as not required by my ruling"*, 2026-10-20) and nothing covers
the rest. Options: (a) only he may, on work he or a client asked for; a session
may retire its own proposal, saying so and giving the reason. (b) Only he may,
always. (c) A session may close anything, with a dated reason, and he can
reverse it. **Recommended: (a).** It keeps his calls his, and stops a session
quietly dropping what he asked for. A session's own false alarm is not his to
adjudicate.

**2. "Not now, maybe later": does it stay on the to-do list?** Options: (a) it
stays, marked as waiting, so nothing vanishes and no session grabs it. (b) A
separate *parked* status that sits off the to-do list. (c) It closes, and a new
item reopens it if it returns. **Recommended: (a).** His own *"it may come
back"* (2026-10-20, on another list) is the reason it must not close; a
separate status adds a pile with no job to do.

**3. The roughly 1,190 already-closed items: how much to correct?** Most are
truly finished, but some are not, and we cannot tell which without reading
them. Reading all of them is about 7 MB, around 2 million tokens before any
judgement. Options: (a) correct the 45 items that already say they were not
delivered, leave the rest, and tell sessions not to rely on an old tick
without reading the item. (b) Have sessions re-read and label every closed
item now. (c) Take the green tick away from every old item so none looks
finished, at the cost of the many that are. **Recommended: (a):** a small
known cost, and it stops the error growing. Choose (b) if a false tick from the
past is expensive enough to pay for once.

## Consequences

The tick means done. A session can list what it may take without reading the
items, the stated condition for promotion is met, and the record of what closed
and why survives in the index. `[~]`'s meaning narrows, and the house takes on
one new parser and a word grammar to keep true. Old ticks stay ambiguous under
question 3's recommendation, and that is a stated cost. `310/080`'s text and
the legend's "ruling" wording are corrections owed by whoever lands this; this
draft changes neither.
