# Cold review — MODEL-ECONOMICS triple delta (sub-agents · tier selection · context reset)

**Scope:** the working-tree delta to `docs/method/MODEL-ECONOMICS.md` (one
commit, 2026-07-15): (1) the one-paragraph "Subagents for fan-out" expanded to
a section *Sub-agents — isolation, not savings*; (2) a tier-selection paragraph
appended to *One doctrine, tiered authority*; (3) session-hygiene item 4
rewritten as *reset by record, not by compaction*. Review the edited doc at
HEAD, whole, plus the delta.

**Independence note:** this brief is author-written (the same session authored
the delta), so the independence rules bind in full (`REVIEW.md`): name your own
attack surface and commit it to your draft **before** opening the deferred
section below the divider; treat this brief's framing — including its account
of what the work is — as attackable; read no prior verdicts until your own
findings are committed. This is doctrine, self-authored: **all findings are the
principal's to decide** (rule 3) — the author may append labelled counsel only.

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict below a second `---` divider in
this file.

---

## Deferred — author's seeded questions (open only after your attack surface is committed)

- S1. The sub-agent section claims delegation "often spends *more* total
  tokens than inline" — is that honest across both pools, or does it overclaim
  for the plan-included case where parallel sub-agents mostly cost wall-clock
  allowance, not marginal dollars?
- S2. "The report is all that survives" — does the doc anywhere conflict with
  this (e.g. the inline-review pattern assumes the verdict file, not the
  transcript, carries the detail)? Is the fresh-context-verification bullet
  consistent with `REVIEW.md`'s independence rules, or does it invite
  author-framed spawn prompts without naming that bind?
- S3. Tier selection: does "cheapest model that genuinely does the work"
  collide with the existing pool split (plan-included builds vs usage-billed
  reviews), which selects by *pool*, not by *capability*? Are the two rules
  composable as written, and is the precedence between them stated or left to
  collide?
- S4. Hygiene item 4: is "the record is this method's compaction" a real
  equivalence or rhetoric — a session record is written for the *next* session,
  a compaction serves the *current* one mid-task; does the text honestly cover
  the mid-task case?
- S5. Naming drift: the doc now uses "sub-agent(s)" where the old text said
  "subagents" — check consistency doc-wide and against sibling docs.
