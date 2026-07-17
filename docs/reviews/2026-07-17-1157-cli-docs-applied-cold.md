# Cold review — CLI-docs standard, the F1–F7 applied batch

**Scope:** the CLI-docs hunks of application commit `e6a295e` (2026-07-17) —
the rulings of the first cold pass applied to doctrine and instruments:
`build/REPO-STANDARD.md` (the CLI-docs convention hunks: scope predicate,
anti-drift wording, the `--help` letter), `instruments/README.md`,
`instruments/ccarchive` (the `--help` register), `instruments/ccarchive.test.js`
(the superset drift test), `instruments/install` (stale-owned-link cleanup
pass), `instruments/man/ccarchive.1`, and `.github/workflows/ci.yml` (guarded
mandoc step). Review the edited doctrine **at HEAD** plus those hunks. The core
question of an applied-batch pass: **does the new wording faithfully implement
the principal's rulings — no drift, no overreach, no silent miss — and is it
sound doctrine in its own right at HEAD?**

Out of scope: the ccarchive F1–F4 hunks interleaved in the same files — that
cycle is CLOSED (0 MAJOR, terminal application closes without a queued
pointer). They matter here only where they interact with CLI-docs claims
(e.g. new flags owing `--help`/man coverage under the superset relation).
Record hunks (`ROADMAP`, `SESSIONS`, session/review files) are context, not
target — but see sequencing: the review-file hunks stay closed until your
findings are committed.

**Sequencing (REVIEW.md rules 1–2, application-review form):** (1) read this
brief **only above the first `---` divider** (use a limited read); (2) review
the doctrine at HEAD and the scoped delta, naming and attacking the
load-bearing assumptions yourself, and **write your attack surface and findings
durably into the verdict section of this file first**; (3) only then open the
deferred section below the divider, the prior verdict + `§ Decision` in
`reviews/2026-07-17-1000-cli-docs-standard-cold.md`, and the intent record
`sessions/2026-07-17-0958-three-queued-cold-reviews-taken.md` — reconcile,
never anchor: check the application implements each ruling as decided. An
application review cannot fully honour rule 2 (the delta carries the prior
verdict's decision stamps); that residual exposure is named, not denied — keep
those hunks unopened until your findings are committed.

**Spawn provenance (rule 4, tested against the delta's author — the applier):**
this brief is written by a **non-author** taking session that Mike (the
principal) opened fresh and pointed at the queue ("do any review work queued");
the applier session (Fable, intent record above) neither started nor instructed
the taking session or this reviewer. The reviewer is a cold spawn of the taking
session, which authored neither the doctrine, the prior verdict, nor the
applied delta. Disclosure: the taking session read the intent record and the
prior verdict file in full to scope this brief; above-the-divider text is kept
to scope and refs. The verdict must repeat this provenance.

**This is self-authored doctrine (by function):** all findings are the
principal's to decide (rule 3) — record counsel per finding, labelled as the
reviewer's counsel; apply nothing.

**Re-run live proofs in scope:** the application claims 247 tool tests · 75
instrument tests · mandoc lint clean · sizescan · linkscan · scan triad all
green; the superset drift test present and green; the installer cleanup pass
proven in throwaway XDG dirs (stale owned links removed, real tools kept) and
the live `~/.local/bin` residue (`fixtures`, `browser-fetch`) gone. Re-run
what falls in scope, including a fresh installer drive into throwaway XDG dirs
with a planted stale owned link.

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict to this file below the second
`---` divider.

---

## Deferred — refs (open only after your attack surface and findings are committed)

No seed questions were queued this time (the `⏳` pointer was refs-only, per
spec). Refs for the reconcile step:

- Prior verdict + rulings: `docs/reviews/2026-07-17-1000-cli-docs-standard-cold.md`
  (findings F1–F7, reviewer's counsel, and `§ Decision` — Mike ruled all seven
  [fixed] as counselled).
- Intent record: `docs/sessions/2026-07-17-0958-three-queued-cold-reviews-taken.md`
  (the taker/applier's account, including its application highlights — the
  author's claims to test, not settled scope).

---
