# 2026-07-26 · 2210 UTC · Queue take — nine rule-4 cold passes in one fan-out (Fable)

**Provenance.** Mike opened a fresh session and pointed it at the queue
("Please do any review work") — the rule-4 worked example. The session ran on
Fable, the required tier for cold passes (the principal's 2026-07-26 ruling
after the withdrawn 0647 Opus pass), and authored none of the nine deltas. All
nine open `⏳` items were claimed on `main` first (`94275e6`), the work ran in
worktree `atelier-review-2210-take`, and nine refs-only briefs were committed
cold (`9aef298`) before any reviewer was spawned — seeds and intent records
deferred below each brief's divider. Nine fresh-context Fable subagents ran the
passes (two-hop shape, 2208 precedent); agents ran no git; the taker verified
at least one load-bearing claim per verdict independently before committing
it, one commit per verdict.

**Results — all nine PASS-WITH-FINDINGS, 56 findings, nothing applied
(REVIEW rules 3–4: every finding is counsel; the decisions are Mike's):**

| Pass | Verdict | Taker's independent check |
|---|---|---|
| ADR 0008 | 3M/5m/1L/1n (EP1–EP10) | floorfleet reads no `scope`/`flags`; floor.py:228 concedes structural-only leakscan |
| pathscan S2 | 3M/5m (PS1–PS8) — keep advisory | the one doctrine-surface TP is live: `docs/build/README.md:28` → `tools/check_links.py` missing |
| stampscan S4 | 3M/3m/1n (ST1–ST7) — do NOT wire | `stampscan --warn` over `docs/` exits 2 at HEAD today |
| floor local seam | 3 medium/2 low (LS1–LS5) | child `why` reaches the Actions command stream raw (floor.py:766); invalid-shebang `OSError` uncaught |
| EVIDENCE §13 | 0M/3m/3n (EE1–EE6) | the cited "ban on fitting" has no method/ home; the verbatim quote drops "from anthropic" unmarked |
| RECORD pushed-floor | 1M/4m (RF1–RF5) | both planes serve the identical nine-scanner registry — the sub-point's "why" is false post-ADR-0008 |
| apex accountability | 0M/3m/2n (AA1–AA5) | two-roots join and the CI-runners overstatement live at 00-APEX.md:67,74 |
| apex Zeroth Law | 1M/2m/2n (ZL1–ZL5) | session-onramp SKILL.md:33–35 still teaches the pre-Zeroth Laws |
| PRINCIPLES §1 way-out | 0M/3m/2n (WO1–WO5) | "never mint access you can't withdraw" exists only in the bullet, not in REACH |

Every pass re-ran the floor (9/9 scanners exit 0 at `9aef298`), the Python
suite (694 OK) and the Node suite (207 pass), and discharged lens 4's
`/security-review` in one explicit line with grounds (landed deltas; manual
code-altitude passes run where the work is code). The taker's own baseline
run agreed before any verdict landed.

**Honesty ledger.**

- **Taker contamination, owned in every affected brief:** a `git log --all`
  grep for the scanner names surfaced the *subject lines* of the withdrawn
  0647 pass's commits (verdict counts + headline directions) before the
  briefs were written. Nothing from them entered any brief above its divider;
  the fresh-context reviewers were the firewall, and no reviewer opened
  anything under `docs/reviews/withdrawn/`.
- **Two brief errors, both caught by their reviewers:** the pathscan brief
  asserted a floor-registry registration that does not exist at HEAD (PS5
  corrects it); the ADR 0008 brief's path list omitted `tools/test_floorfleet.py`,
  so the reviewer's enacting set was short one commit until the intent record
  named it (no finding changed — that suite was run anyway).
- **Date-stamp corrections:** several verdicts arrived stamped `2026-07-27`
  (the NZ-local date; `date -u` said 2026-07-26 throughout). Corrected
  mechanically before commit, named in each commit message, no verdict
  content touched — the at-rest-UTC rule.
- **Reviewer deviations** are owned inside each verdict (two over-broad greps
  that echoed lines from out-of-bounds files without opening them; sanctioned
  `git show`s that necessarily displayed the delta's own ROADMAP hunks).
- **Scale divergence:** the local-seam reviewer graded medium/low rather than
  MAJOR/minor; recorded as reported, not translated — whether a "medium"
  triggers the MAJOR cycle rule is folded into Mike's ruling on that pass.

**Open at close.** Nine 🎯 ruling sets (56 findings) await Mike — rule 3
walk-throughs owed one-by-one with plain-language impacts when he engages.
No `⏳` remains in the queue; the withdrawn 0647 files stay quarantined and
unread by every reviewer in this take. Cycle shape on ruling: ADR 0008,
pathscan, stampscan, RECORD and Zeroth carry MAJORs (application inherits
rule-4 status); EVIDENCE, accountability, way-out — and local seam, subject
to the scale ruling — close terminal on their ruling application.
