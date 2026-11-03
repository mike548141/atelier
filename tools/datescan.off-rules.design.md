# datescan — what it let pass now reports without blocking

Status: **built** (2026-11-03), roadmap `115/090`. The code is in
`datescan.py` (`Finding.response`, `WHERE_BLOCKQUOTE`, `_line_hits`,
`render_advisory`); the tests are in `test_datescan.py` (`BlockingSetPinned`,
`BlockquoteReports`, and the hook-plane case in `StagedPlane`) and
`test_floor.py` (the advisory-count contract).

## 1. The authority, and what it does not cover

Mike's answer of 2026-11-03, through the decision device at the close of the
queue run that built leakscan's tier, was **"Carry on to datescan"**: the
2026-10-16 "leakscan first" answer carries on to datescan, built the same way,
so nothing that blocks today stops blocking. It does not cover harvestscan,
which still needs its own go. All three answers are recorded on the item.

Out of scope, by that answer: **demotion.** Every check that blocked blocks
exactly as before.

## 2. What datescan let pass, and what now reports

The `115/090` audit named two things datescan gives up silently: every `>`
line is exempt, and a bare "today" with no date cue passes. datescan has no
per-rule switch a repo can turn off (no `--disable`); a repo can only soften
the whole check with its advisory form, `--warn`, which already prints every
finding. So the candidates were the audit's two, and one of them is built.

| Candidate | Before | Now | Why |
|---|---|---|---|
| **A blockquoted (`>`) line** | skipped whole | every check runs; hits report, never block | `>` is a quoted source's words and also the house's own callout style (the module docstring, DSR1). The callout half was a silent miss. Measured: 48 hits across the estate |
| **A bare "today"** with no cue and no ISO date nearby | passes | **unchanged: not reported** | too noisy even as report-only (§ 3) |

Not changed, so still silent:

- **Code.** A fenced or indented code block, and an inline code span, are
  quoted text, not the repo's own dating. They stay exempt whole, inside a
  blockquote too. An indented line that starts with `>` is code first.
- **A quoted mention** (`"yesterday"`). It is how the rule's own examples
  read, and reporting it would list the doctrine about the rule.
- **Shapes no check reads** (`2026/07/23`, an implausible numeral triple).
  They were never detected, so there is nothing to report; widening detection
  is a different change.
- **An exemption.** An allow-marker or a `.datescanignore` glob applies to a
  report-only hit exactly as to a blocking one, and is counted in the
  `suppressed:` line either way.

## 3. Left out: the bare "today"

Measured 2026-11-03 over every git repository in the estate (30), whole
`docs/` tree: **about 2,650 bare "today" hits** outside blockquotes, more than
1,000 in the largest repository and 193 in this one. Of 40 drawn at random
from this repository, one or two read as a calendar date ("for the second
time today"). The rest are the "currently" sense ("nothing answers this
today", "exploitability is low today"), which the rule does not ban. The
original corpus review found the same, about 9:1 (DSR3).

A report that is about 95% correct prose would be a list nobody reads, and a
count nobody reads is cover, not coverage (EI1). So it is left out, and the
silent miss stays named in the module docstring as before.

One way it could report without flooding is untried and is not built here:
report it on the **hook plane only**, on the lines a commit adds, where the
writer can fix it in the moment, and keep it off the whole-tree CI read and
the board's count. That would be the first check whose report differs by
plane, so it is a posture choice, not a build detail.

## 4. How it reports

The shape is leakscan's (and secretscan's E6b tier), reused rather than
invented:

- Each `Finding` carries `response`, `block` or `advisory`, defaulting to
  `block`, so a finding built anywhere without saying fails safe into the
  gate. It also carries `where`: empty for a prose line, `blockquote` for a
  report-only hit. Its `kind` is the check that found it, so the finding ID
  and the narrow marker `datescan:allow:<kind>: <reason>` work as before.
- **Human output.** The blocking list is unchanged. A line
  `datescan advisory: N finding(s) — reported, not blocking.` prints on every
  run, zero included, and a `🟡 REPORT-ONLY FINDINGS` block lists the hits in
  wording that shares nothing with the blocking block.
- **JSON.** `clean` and `findings` keep their meaning: blocking findings only,
  which before this change was every finding. New fields: `blocked`, `counts`
  (`blocking`, `advisory`) and `advisory` (`findings`).
- **The board.** datescan's registry entry in `floor.py` sets
  `advisory_count=True`, so the board shows `🟡 datescan enforced` with the
  count read from this run's output. Its advisory form is unchanged.
- **Planes.** The hook plane reports the hits on the lines a commit adds, as
  it keeps blocking findings. The CI plane prints every one, tree-wide, and
  the board's count comes from that run, with no stored number to go stale.

## 5. The invariant: nothing that blocks today stops blocking

- The exit code is computed from blocking findings alone. A hit is
  `advisory` only on a blockquoted line, which was skipped before, so no hit
  that blocked can become report-only.
- **Pinned.** `BlockingSetPinned` lists the seventeen relative-time terms, the
  four dating cues for "today", the four non-ISO shapes and the invalid ISO
  date that blocked when this was built. It asserts that the term list is
  unchanged, that each fixture still blocks with exit 1 and reports nothing,
  and that only the same fixture behind `>` reports.

## 6. Costs and residuals

- **A fence inside a blockquote** (`> ` then three backticks) is not seen as a
  fence, as before; its lines now report rather than pass. That costs a
  report-only line, never a block.
- **Read, not acted on.** Whether a repo fixes a reported callout is not
  enforced. The count on the board is how it gets read.

## 7. Blast radius (2026-11-03)

Measured with this change's tool against the tool before it, over every git
repository in the estate (30), on the CI plane's whole-tree read of `docs/`
with `--json`. The one repository that declares datescan advisory was also run
with `--warn`, as its floor runs it: 31 runs in all.

- **No exit code moved, and no blocking count moved**, in any of the 31 runs.
  In the one repository with blocking findings, the blocking set is identical,
  finding for finding.
- **New report-only counts** in 5 repositories: 1, 2, 3, 14 and 28. They are a
  mix of quoted sources' own dates and the repo's own callouts. Each board
  shows its count from that repo's next CI run.
- Every other repository reports 0.
