# Cold pass — C5's re-measurement and the re-ruling it recommends

**Pass type:** design/intent cold pass (the work under review is an analysis and
a recommendation, not a landed build).
**Tier:** Fable (REVIEW.md rule 4 — the principal-named review tier).

## Spawn provenance

- **Author of the work under review:** the session that landed `f83a6f7`
  (2026-08-09), intent record
  [`sessions/2026-08-09-0352-c5-remeasure.md`](../sessions/2026-08-09-0352-c5-remeasure.md).
- **Who spawned this review:** the principal (Mike), in a session he opened, on
  2026-08-09. His words: *"I want a cold fable review of C5, I'm not sure I
  trust the findings of the session that decided that."*
- **Author's non-involvement:** the spawning session has authored no part of the
  C5 item, holds no commits in this repo, and was neither started nor instructed
  by the authoring session. Rule 4's single criterion is met.
- **Brief written by:** the spawning session (a non-author taker), per rule 4.
  No `.deferred.md` sibling exists — rules 1–2's deferral split binds briefs
  written by or on the author's framing, which this is not.

## What the work is

Two artefacts, and the reviewer should treat the boundary between them as
attackable rather than given:

1. **`docs/ROADMAP.md` lines 171–363** — the C5 item, comprising: a
   re-measurement of three premises that a previous ruling was executed and
   then reverted on; a statement of the defect said to sit under them; an
   account of how a same-day ruling (`c827705`, scoped `local-term` markers)
   changes it; four options; and a recommendation.
2. **`docs/sessions/2026-08-09-0352-c5-remeasure.md`** — the intent record.

Related surfaces the item leans on: [`tools/leakscan.py`](../../tools/leakscan.py),
[`docs/method/GUARDS.md`](../method/GUARDS.md),
[`docs/method/PROPAGATION.md`](../method/PROPAGATION.md), and the
`.leakscanignore` files across the estate's local clones.

## Why it is being reviewed

The principal does not trust the authoring session's findings. The item's own
history supplies independent grounds: the ruling of 2026-08-04 was executed and
reverted hours later when three of its premises failed on contact, none having
been measured before they were ruled on. The work under review is the sweep that
was supposed to correct that — so the question *"were these premises measured, or
reasoned?"* is being asked of the correction as well.

## Scope

Widest the work admits (REVIEW.md § *What a review actually checks*). In scope:
the intent, the measurement method, every numeric claim, the options as framed,
the recommendation, and the item's account of what other decisions (D1,
`c827705`, the 2026-08-06 term deletion) did to it.

**Non-goals — one, and it does not fence the risk:** the reviewer does **not**
rule. Which option is chosen is the principal's decision (REVIEW.md rule 3). The
reviewer's job is to say whether the findings are true and whether the options as
framed are the real ones. If the reviewer believes the option set itself is
wrong or incomplete, that is a finding, not a ruling.

## Hard constraint — read before running anything

**atelier is a PUBLIC repo.** The term this item is about is deliberately never
named in it; the item's whole subject is the harm of joining that name to the
posture of what it labels. The operator's real term list is machine-local
(`$ATELIER_LEAKSCAN_TERMS`, else `~/.claude/leakscan-terms.txt`), outside every
repo by design.

- Probe with a **scratch term list** written to the session scratchpad, exactly
  as the authoring session did. Do not modify the operator's list.
- **Never write the term** — or any other machine-local term — into any file in
  any repo, including this brief, your verdict, and any scratch file that lives
  inside a working tree. Counts and classes only.
- The same bar applies to the private repo names the item discusses: atelier's
  own records already breach this in places (the item says so at lines 407–417),
  which is itself in scope as a finding, but your verdict must not add to it.

## The four lenses

1. **Approach & assumptions** — is this the right problem, framed the right way?
   Name the load-bearing assumptions yourself before reading the list below.
2. **Correctness & quality** — is every measured claim true at HEAD? Is the item
   honest about what it measured versus what it inferred?
3. **Completeness / harvest** — what should the sweep have covered and did not;
   what existing decision or mechanism does the item duplicate, ignore, or
   mis-describe?
4. **Security & privacy** — mandatory. This item *is* a privacy-control question,
   so the lens is not discharged in a line. Consider at minimum: whether the
   recommended option weakens the guard in a way the item does not price; whether
   the item's own text commits the join it exists to prevent; and whether a
   per-term scope declaration creates a new place where a term can silently stop
   matching.

## Re-run obligation

REVIEW.md § *Re-run every "live-proven" claim in scope* binds here with unusual
force, because the failure mode this pass exists to catch is exactly a premise
recorded as measured that was not. Re-run, do not read, at least these:

| # | Claim | Where |
|---|---|---|
| 1 | 67 term findings in atelier, not 86; 60 in frozen records; 7 in live files | L193–197 |
| 2 | The 7 live ones break down 2 / 4 / 1 across this file, an instrument design doc, a tool docstring | L401–406 |
| 3 | 3 ordinary-English instances estate-wide against ~673 name uses | L199–205 |
| 4 | Two of those three are unrewordable (an upstream-bug-report quotation; a physical building) | L202–205 |
| 5 | Premise (c) is false: the estate root retired the scanner repo-wide by ADR with a `*` glob, and two further private repos did the same | L206–216 |
| 6 | `.leakscanignore` filters at the path level *before* the term list, on both the staged and tree planes | L210–213 |
| 7 | All three of those repos scan clean, exit 0, with the bare term live | L214–216 |
| 8 | Six private children that doctrine instructs to name the root carry 58 lines between them | L217–222 |
| 9 | Option 2 measures 21 here and 19 across children | L308–311 |
| 10 | Option 3 prices at ~125 permanent findings machine-wide | L312–314 |
| 11 | Option 1's build is one condition on the term loop, because `scan_text` already receives the repo-relative path and `scan_path_name` inherits it | L290–295 |
| 12 | The total marker cost of the Line hatch is 118 lines (60 + 58) | L245–251 |
| 13 | The tree-wide scan is green now, with the three published-identity lines carrying scoped `local-term` markers | L762–771 |

## Specific assumptions to attack

These are a floor, never a fence — add your own first.

- **That the residue is a volume problem.** The item's recommendation now rests
  on one ground: 118 lines is too many to mark. Is 118 the real number? Do the
  60 frozen-record lines need markers at all under any option, or is that cost
  imported from an assumption about what "red" obliges?
- **That frozen records may not be edited.** The item treats this as settled
  convention. Is it written down anywhere, and does adding an allow-marker count
  as rewriting a record?
- **That the sweep covered "every plane and every repo on the machine."** There
  are more git repositories on this machine than there are declared estate
  children. Establish what the denominator actually was.
- **That option 1 is cheap.** The item concedes the grammar is the work, then
  prices only the matching. What does "narrow, reasoned, dated, and noisily
  subtracted" cost in the loader, the tally, the report, the tests, and every
  adopting tree?
- **That option 4 is the status quo.** The item argues it is broken because
  nothing enforces it, then also argues `c827705` makes it safer than before.
  Both cannot be doing the work they are asked to do.
- **That the 2026-08-06 place-name deletion is the same defect.** The item calls
  it "the second instance of one defect". Test that: same cause, or two
  different causes with a shared symptom?
- **That the question shrank.** The item claims `c827705` discharged one of
  three grounds and answered another. If that is right, is what remains still
  worth a build — and does the honest recommendation change?

## Output

Findings with stable IDs (`C5R1`, `C5R2`, …), each with severity
(MAJOR / MODERATE / minor / note), the evidence you ran, and what you would do
about it. State the verdict as PASS / PASS-WITH-FINDINGS / FAIL. Repeat the spawn
provenance in the verdict (rule 4: a pass with no provenance trail is
unauditable). Append below a `---` divider **in this file**; write no other
file inside the repo, and run no git commands — the spawning session commits.

---

# Verdict — PASS-WITH-FINDINGS (2 MAJOR · 4 MODERATE · 3 minor · 3 notes)

**Spawn provenance (rule 4, repeated per the brief).** This pass was spawned by
the principal (Mike) on 2026-08-09, in a session he opened, on his stated
distrust of the authoring session's findings. The reviewer session was neither
started nor instructed by the authoring session (the one that landed `f83a6f7`,
intent record `sessions/2026-08-09-0352-c5-remeasure.md`), holds no commits in
this repo, and authored no part of the work under review. The brief was written
by the spawning session, a non-author. Tier: Fable, checked at selection. No
`.deferred.md` sibling existed; nothing was folded in.

**Privacy compliance.** Probed with a single-term scratch list written to the
session scratchpad; the operator's machine-local list was read once, read-only,
to confirm the subject term is absent (it is — consistent with the revert) and
was never modified. No machine-local term, and no private-repo detail beyond
what this repo's own records already carry, appears in this verdict — counts
and classes only. Exposure disclosure (SL2 class): the measurement itself
required reading term-hit lines inside session records across several trees —
those lines *are* the findings, so the exposure is inherent to the re-run
obligation and was limited to hit lines; the intent record was read as the
brief's named subject; no prior verdict and no ROADMAP-DONE history account was
opened at any point (the execution/revert history is taken from the item and
the commit log, not re-audited — stated as unverified below).

**Bottom line.** The sweep was real and the author was honest about method:
**every headline number reproduces exactly at the states the sweep measured.**
At `f83a6f7`: 67 findings / 60 frozen / 7 live splitting 2 + 4 + 1. Across the
six children at their pre-sweep commits: 4 + 7 + 11 + 2 + 32 + 2 = **58
exactly**. 118 = 60 + 58 and ~125 = 67 + 58 are straight arithmetic on those.
All three repo-wide opt-outs scan clean, exit 0, with the bare term live, each
`*` carrying a reasoned stanza and a dated ADR (the estate root's dated
2026-07-13, a month before the ruling — premise (c) is confirmed false).
Path-before-terms holds at source on both planes. The tree-wide scan with the
real list is green at exit 0 with `local-term×3`, on the three scoped identity
lines. This is the best-verified figure set the C5 programme has produced.
What does **not** survive contact is two of the frames the recommendation
leans on — the composition of the "sharpest cost", and the account of the
2026-08-06 deletion precedent — plus same-day drift that has already
falsified several figures at HEAD. None of it kills option 1; all of it
changes what Mike is actually ruling on.

## Re-run table (brief § Re-run obligation)

| # | Claim | Result |
|---|---|---|
| 1 | 67 / 60 frozen / 7 live | ✅ exact at `f83a6f7` · ⚠️ HEAD is 74 / 62 / 12 (C5R4) |
| 2 | Live split 2 / 4 / 1 | ✅ exact at `f83a6f7` · ⚠️ HEAD is 7 / 4 / 1 |
| 3 | 3 ordinary-English vs ~673 name uses | ⚠️ ratio confirmed (whole-word total 684 at HEAD, ordinary-English in single digits) but the census of 3 misses at least one instance (C5R7) |
| 4 | Two of three unrewordable | ✅ both instances located and class-confirmed; nuance in C5R7 |
| 5 | Premise (c) FALSE — root retired the scanner by ADR, `*` glob; two more repos same | ✅ all three `*` files + reasoned stanzas + dated ADRs sighted |
| 6 | Ignore filters path-level before terms, both planes | ✅ at source — tree plane in `iter_files`, staged plane before `scan_text` |
| 7 | All three scan clean exit 0, bare term live | ✅ re-run: 0 findings, exit 0, 99/36/40 files by glob |
| 8 | Six private children, 58 lines | ✅ count exact at pre-sweep states · ❌ composition: one child is PUBLIC (C5R1) |
| 9 | Option 2: 21 here / 19 children | ⚠️ reproduces **transposed** (19 / 21) under the natural shapes regex; no method recorded (C5R8) |
| 10 | Option 3: ~125 machine-wide | ✅ 67 + 58 at sweep states; 134 at HEAD; the 7 undeclared repos all contribute zero |
| 11 | Option 1's matching is one condition | ✅ at source — `scan_text` already threads the repo-relative path, `scan_path_name` inherits; the grammar cost is real and the item concedes it (C5R5 prices what it doesn't) |
| 12 | 118 = 60 + 58 | ✅ arithmetic; 122 at HEAD; one of the 118 is unmarkable at any price (C5R10) |
| 13 | Tree-wide green, `local-term×3` | ✅ exit 0, three scoped identity lines confirmed |

**Denominator (the brief's named attack).** 24 git repositories sit under the
estate clone directory; the declared fleet is the parent + 16 children, so
**seven git repos are outside the declared fleet** (plus two non-git content
dirs). All seven were probed: **zero term findings in every one**, so the
sweep's arithmetic survives the wider denominator, and a bounded search found
no git repos elsewhere in the home directory's usual places. "Every repo on
the machine" was true in effect, though the sweep never stated its
denominator — it should have, because it holds only by luck of where the term
lives. (Also: `floorfleet.py` has no `--list` flag — enumeration is `--json`.)

## Findings

### C5R1 — MAJOR. The "sharpest cost" is mis-composed: one of the "six private children" is PUBLIC, and ~90% of the 58 lines are not the prescribed act.
Evidence: the 58 reproduces exactly, but (i) one of the six is the estate's
**publish pilot, made public 2026-07-29** — eleven days before the sweep — so
its two lines put the root's name in a *public* tree, where PROPAGATION's
name↔posture split *forbids* the act the item says doctrine prescribes; (ii)
doctrine's instruction covers a private child's **onramp** — only ~6 of the 58
lines are onramp lines (three repos' CLAUDE.md); ~50 are incidental references
in records and decisions, lawful in private trees but nowhere prescribed;
(iii) one of the six is an archived repo. The "permanent friction on the
prescribed act" argument is real but applies to roughly a tenth of the volume
quoted for it. 🚩 **Cross-repo fact needing Mike's attention regardless of
C5:** the public pilot child's own 2026-08-09 session entry records *"Verified
before writing: the root's name appears nowhere in this tree"* — while two
lines in that tree carry it today (one in its session log, one in its
publish-review ADR; a term-scan or grep on that tree locates both instantly —
refs withheld here so this public verdict does not signpost the join). A false
live-proven claim in a public tree is exactly the class this programme exists
to catch. What I would do: restate the cost as *five private children · ~6
prescribed onramp lines + ~50 incidental private-tree lines*, and treat the
public child's 2 lines as **true positives** the bare term would correctly
catch — a point *for* the term, not a cost of it.

### C5R2 — MAJOR. The 2026-08-06 deletion precedent is materially misdescribed against its own source record.
Evidence: the child's publish-review ADR (gate 1) and the ruling comment
recorded beside the deletion both say: the **~70 findings were structural**
(venue addresses, phones, coordinates across 32 files) and were dispositioned
with four deliberately tight globs plus 18 prose markers — the ~70 was never
the deleted term's line count. The deleted term sat in **three venues' fields
plus app-shell fallback lines**, and the recorded *ratio decidendi* is
proportionality: a ten-thousand-person public suburb name *"is not an
identifying detail on its own"*, the street-level terms that actually pinpoint
the house remain — *"cover narrowed, not lost."* The item recasts this as "a
term that should still guard everywhere else was dropped instead" and claims
option 1 "would let [it] return to the list with the narrow exception it
should have had" — both contradict the recorded ruling, which judged the term
not worth guarding on its own merits. What *does* hold: the ADR explicitly
cites D1's marker-non-exemptibility as what left no hatch, so the no-hatch
defect genuinely forced the moment and removed the middle option. Honest
restatement: *the defect eliminated the narrow-exception option; the principal
then ruled deletion right on independent grounds.* "The second instance of one
defect" is half of that sentence. And the "~70 markers would have been owed"
figure borrows the structural-finding count: the term's own repo-wide count is
in the dozens (about 75 occurrence-lines at HEAD, most in docs and records,
roughly 20 in product data and tests already behind the globs).
Volume-in-the-tens survives; the stated basis does not.

### C5R3 — MODERATE. The quotation "noise that hides the next real finding" exists in no child repo.
Evidence: an estate-wide search finds the phrase only in this file — the C5
item itself, and a second roadmap item that cites *"(recorded in C5 above)"*
as its source. The child's actual record (the publish-review ADR) contains
neither the phrase nor a ~70-marker rejection in those terms. A coined
paraphrase presented in quotation marks has already become a citable source
for a second item — a testimony loop of exactly the kind EVIDENCE.md exists to
prevent. Strip the quote marks, attribute the substance to the ADR's actual
disposition (globs-over-markers, kept tight), and fix the second item's
citation.

### C5R4 — MODERATE. Every atelier-side figure is already stale at HEAD — same-day drift falsified them within hours.
Evidence: at HEAD the counts are 74 / 62 / 12 (live split 7 / 4 / 1), children
58 → 60. Five new root-name mentions landed in this public file's live text
*after* `f83a6f7` (the estate-floor items), including one line that states
outright that the named repo is the estate root — **the exact join, verbatim,
in the public tree**, landed the same day the item recorded a near-miss of the
same class. This is not the author's error, and it *proves* the item's
enforcement-gap thesis while falsifying its figures. But it means the
re-ruling must be made on classes and mechanisms, not on any frozen number in
the item — the numbers now decay in hours, and the item's own history says
adjusting them by intuition is how this programme got here. 🚩 The five new
live-file mentions widen the standing-gap item's "rewrite the seven live
lines" task — it is now twelve lines and growing.

### C5R5 — MODERATE (privacy lens). Option 1 moves the exception record to an unversioned, unreviewable file — a cost the item does not price.
The item prices scope-grammar enforcement (unreasoned ⇒ exit 2) and noisy
subtraction — both right. What it never names: `c827705`'s Line markers live
**in-repo** — versioned, diff-reviewed, greppable, floor-checked — while
option 1's scope declarations would live in the **machine-local term list**:
no git history, no review path, no floor check, visible only to someone
reading a scan tally on that machine. A typo'd or over-wide scope glob
silently de-guards a subtree with no audit trail, which is the brief's "new
place a term can silently stop matching" — noisy subtraction shows a scope
*being used*, not a scope *being wrong*. If option 1 is taken, the grant
record needs a versioned home (the private estate root is the obvious one)
and ideally a validation path; that is real scope the build must carry.

### C5R6 — MODERATE. Option 1's atelier scope entry silently pre-decides the un-ruled standing-gap question.
The item's sibling entry records scrub-vs-accept-vs-widen for the records
breach as "it was never ruled". But writing a scope entry that exempts this
repo's records paths from the term *is* ruling "accept the records as
historical" — under PROPAGATION those 60+ frozen lines are recorded breaches
of the name↔posture rule, not false positives, and a scope entry is their
acceptance instrument. The item cross-links the two questions but never says
option 1 embeds an answer to the second. They are one ruling and should be
put to Mike as one.

### C5R7 — minor. The ordinary-English census of 3 is method-dependent and under-counts.
On the grep plane there are at least **four distinct instances (six lines)**:
the docstring (verb), the upstream-workaround quotation in a child's research
doc (verified verbatim-quoted), the storage-building rows in a property repo's
build programme (two lines), and an **archived network config in a fourth repo
carrying the building sense twice beside coordinates** — missed by the census,
glob-ignored on the scan plane. Direction (rare) is unchanged. Nuance the item
omits: both *building* instances sit behind ignores or repo-wide opt-outs
today, so the only scan-reachable unrewordable case is the quotation — the
"physical building" leg of the durable argument is a class argument, not a
live cost.

### C5R8 — minor. Option 2's figures reproduce transposed, and no method is recorded.
Under the natural shapes reading (term adjacent to path/backtick/identifier
punctuation) the measurement gives **19 here / 21 across children** at the
sweep-time states — the item says 21 / 19. The totals and the conclusion
(still red everywhere; misses the bare name in prose, which is the leak's
actual shape) are confirmed. But the item records no regex for "shapes-only",
so the claim is unreproducible as stated — the same defect class the item
exists to correct, one size smaller.

### C5R9 — minor. "Already doctrine in GUARDS.md" over-attributes the grant-date half.
GUARDS § *Acceptance and deferment* requires a reason (acceptance) and a
reason + expiry (deferment). The **grant-date-always** requirement the item
presents as already-doctrine is not in GUARDS' text — it is Mike's 2026-08-09
restatement. If it binds (it should — the three `*` opt-outs already practise
it via dated ADRs), GUARDS owes a one-line harvest edit.

### C5R10 — note (strengthens the recommendation). One of the 118 cannot take a marker at any price.
One frozen finding is a **path finding** (a session record's filename carries
the term; reported at line 0). Per the source, a path cannot carry an inline
allow-marker — the only hatch is an ignore glob. So the Line-hatch route is
not merely 118 edits; it is 117 edits plus one finding it cannot reach. The
volume argument is slightly stronger than the item states it.

### C5R11 — note. The option-4 "both ways" tension resolves; the item is honest there.
"Broken four times because nothing enforced it" (enforcement axis) and
"stronger than before" (reversibility axis — the Line hatch means adding the
term later is no longer friction-locked) are different axes and can both be
true. The accidental near-miss evidence is properly disclosed against the
author's own fallback recommendation — above the honesty bar. One addition
from this pass: under option 1 the five new public-tree mentions of C5R4
would have been *caught at commit*; under option 4 they were not caught. That
is live, same-day evidence on exactly the option-1-vs-4 boundary Mike is
ruling on.

### C5R12 — note. The frozen-records premise is written doctrine, with one unstated edge.
RECORD.md: the session index is *append-only* ("an entry is never edited or
reordered once written"), ROADMAP-DONE is "the append-only store", archives
relocate "verbatim". So "frozen records are not rewritten" is grounded, not
folklore. Unstated: whether appending an allow-*marker* to a record line
counts as editing content. The item assumes yes; the stricter reading of
"verbatim" supports it, but the rule as written does not decide it — worth one
sentence in RECORD.md whichever way Mike rules, since 60 lines hang off the
answer.

## Lens discharge

1. **Approach & assumptions** — attacked above; the load-bearing ones this
   reviewer named first were the 58's composition, the deletion precedent, the
   denominator, and option 1's hidden governance cost (C5R1, C5R2, C5R5, C5R6).
2. **Correctness** — the re-run table; the sweep's numbers are genuine at
   their states; drift is the caveat, not dishonesty.
3. **Completeness** — the census gap (C5R7), the unstated denominator, the
   missing option-1 governance scope (C5R5). No missing fifth option found:
   records-path ignores are correctly rejected on narrowness, and per-repo
   opt-outs in the five private children are already available under existing
   doctrine without any build — worth naming in the walk-through as the
   zero-build partial mitigation, but it does not reach atelier's own residue.
4. **Security & privacy** — run at design altitude throughout (C5R1's public
   tree, C5R4's live join, C5R5's unversioned scope surface). The house
   scanner (`/security-review`) was not run: this is a landed markdown
   analysis, the scanner's file-class exclusions bar markdown documentation,
   so its clean pass would be definitionally empty — discharged here with
   grounds per REVIEW.md.

## Not verified, and why

- **The 2026-08-04 execution/revert history** (the 86-finding red, three
  passes in flight, the ~364-vs-492 self-reference correction): taken from the
  item, the intent record and the commit log. The term list's own edit history
  is machine-local and unversioned, so the execution/revert sequence is not
  independently reproducible; the root's self-reference count re-measures at
  ~496 today, consistent with the intent record's 492 correction.
- **Option 2's exact regex** (C5R8) — recorded nowhere.
- **Which repos the authoring sweep actually enumerated** — the record never
  states its denominator; this pass's 24-repo probe shows the omission
  happened to be harmless (all seven undeclared repos are term-free).

## What this leaves Mike ruling on

Not this reviewer's to rule (rule 3); what the findings change about the
*question*: the recommendation's single remaining ground — "118 lines is a
volume problem" — survives re-measurement in direction, but its composition
is: ~62 frozen lines in this public tree that are *accepted-breach* candidates
(one of them unmarkable), ~6 prescribed onramp lines plus ~50 incidental lines
across five *private* children, and 2 lines in a *public* child where the term
flagging them would be the guard working. Option 1 remains the only narrow
instrument for that volume, but it carries an unpriced governance cost (C5R5)
and embeds the standing-gap ruling (C5R6); option 4's fallback case gained
same-day evidence both ways (C5R11). The deletion precedent should not be
re-litigated on the item's account of it (C5R2).
