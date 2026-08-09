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
