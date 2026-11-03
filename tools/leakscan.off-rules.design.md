# leakscan — rules that are off report without blocking

Status: **built** (2026-11-03), roadmap `115/090`. The code is in
`leakscan.py` (`WITHDRAWN`, `blocks`, `render_advisory`); the tests are in
`test_leakscan.py` (`BlockingSetPinned`, `DisabledClassReports`,
`WithdrawnRuleReports`) and `test_floor.py` (the advisory-count contract).

## 1. The authority, and what it does not cover

Mike's answer of 2026-10-16, given after he was re-briefed on the EI6 ruling
(2026-07-29, `docs/reviews/2026-07-29-1243-e6-intent-cold.md`: leakscan
"gains no advisory form", because leaked personal data cannot be rotated), was
**"Report-only for off rules"**, with nothing demoted. That answer lifts EI6
for this narrow case only. The earlier answer the same day, "leakscan first",
was given before he had been shown EI6, so it is not the authority for
anything here. Both are recorded on the item.

Out of scope, by that answer: **demotion.** The audit's candidates (`ipv4`,
`nz-address`, `nz-phone`, `coordinates`, `nz-ird`) block exactly as before.

## 2. What "a rule that is off today" means

Two kinds, and only these two:

| Kind | What it is | Today | Before | Now |
|---|---|---|---|---|
| **Withdrawn** | a rule written, measured, and taken out of the blocking set for noise | `diagnosis-key`: the diagnosis/diagnoses pair withdrawn from G1's key vocabulary (the note above `PII_KEY_RX`) | did not exist in code | runs on every scan, never blocks; `--disable` refuses its name (exit 2), since it has no blocking form to switch off and a flag never silences a report |
| **Disabled** | a `STRUCTURAL` rule named in `--disable`, which is how a child's `.atelier-floor.json` `flags` turns a class off | three children disable a class | skipped: its hits were never seen | runs, and its hits report without blocking |

Not off, so unchanged:

- **A rule narrowed for noise** (ipv6's D2 shape, nz-address's D4 suffix
  guard, the ipv4 safe set, placeholder suppression). It still blocks on its
  narrower shape. The shapes it leaves out are not reported.
- **An exemption.** An allow-marker or a `.leakscanignore` glob is a reasoned
  human judgement on a line or a path. It applies to a report-only hit exactly
  as to a blocking one, and is counted in the `suppressed:` line either way.
- **The binary gate rules.** `--disable` still refuses them, and their dated
  grace is untouched.

## 3. How it reports

The shape is secretscan's advisory tier (E6b), reused rather than invented:

- Each `Finding` carries `response`, `block` or `advisory`. It defaults to
  `block`, so a finding built anywhere without saying fails safe into the gate.
  `blocks(rule, disabled)` is the single decision.
- **Human output.** The blocking list is unchanged. A line
  `leakscan advisory: N finding(s) — reported, not blocking.` prints on every
  run, zero included, and a `🟡 REPORT-ONLY FINDINGS` block lists the hits in
  wording that shares nothing with the blocking block.
- **JSON.** `clean` and `findings` keep their meaning: blocking findings only,
  which before this change was every finding, so a consumer gating on `clean`
  gates on exactly what it did. New fields: `blocked`, `counts`
  (`blocking`, `advisory`) and `advisory` (`findings`, `over_cap`).
- **The board.** leakscan's registry entry in `floor.py` sets
  `advisory_count=True`, so the board shows `🟡 leakscan enforced` with the
  count read from this run's output. Its `advisory` stays `None`: a child still
  cannot soften leakscan.

EI1's precondition (where advisory findings surface durably, and whether they
must be acknowledged) is met the way secretscan's tier met it. The hook plane
prints the report-only hits on the lines a commit adds. The CI plane prints
every one, tree-wide, on every push, and the board's count comes from that run,
with no stored number to go stale. No acknowledgement is required, which is
also secretscan's answer. That is EI6's per-plane semantics for this tier.

## 4. The invariant: nothing that blocks today stops blocking

- The exit code is computed from blocking findings alone. A rule's response is
  `advisory` only if it is withdrawn or named in `--disable`; the term list and
  the binary gate always block.
- **The finding cap.** A report-only finding past the materialisation cap is
  counted in `advisory_over_cap`, never in `findings_over_cap`, which feeds the
  exit code.
- **One span, one finding (D5).** A blocking shadowed rule is shadowed only by
  blocking shadowers, as before, so `--disable mac-address` still leaves ipv6
  blocking a MAC. A report-only shadowed rule is shadowed by any shadower.
- **Pinned.** `BlockingSetPinned` lists the fifteen structural rules and the
  term list that blocked when this was built. For each one it asserts that the
  rule still exists, still blocks its fixture with exit 1, and still blocks
  with every other rule disabled. A rule leaving that list is a narrowing of
  the boundary, and that is the principal's decision (`SECRETS.md`
  § *The boundary's posture*).

## 5. Costs and residuals

- **A MAC can report twice.** In a repo that disables `mac-address` but not
  `ipv6`, a MAC blocks as `ipv6`, as before, and also reports as
  `mac-address`. A reverse shadow would remove the duplicate, but it would add
  a second shadowing rule to the engine to save one line, so the duplicate is
  kept and named here.
- **Shared cap.** Report-only and blocking findings share the 50,000-finding
  materialisation cap, as in secretscan. Past it a blocking finding is still
  counted and still blocks; it is only no longer listed.
- **Read, not acted on.** The board is the consumer. Whether a child acts on a
  report-only hit is not enforced, and a count nobody reads is cover, not
  coverage (EI1). The count is how it gets read.
- **Blast radius**, measured before landing over every repo in the estate,
  whole tree with the worktree's tool. No exit code changed. The new counts are
  in § 6.

## 6. Blast radius (2026-11-03)

Measured with this change's tool against the tool before it, over every git
repository in the estate (30), whole tree with `--json`. The four that
declare leakscan `flags` or `scope` in `.atelier-floor.json` were also run with
those, as the floor's CI plane runs them: 34 runs in all.

- **No exit code moved, and no blocking count moved**, in any of the 34 runs.
- **The withdrawn `diagnosis-key`** reports in 4 repositories: 1, 1, 3 and 11
  findings on a whole-tree run.
- **Disabled classes** report in the 3 repositories that disable one: 56,
  241 and 2,652 findings (the last also carries 10 `diagnosis-key` findings
  inside its declared scope). Each board shows its count from that repo's
  next CI run.
- Every other repository reports 0.
