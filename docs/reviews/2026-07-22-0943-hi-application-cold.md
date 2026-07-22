# Cold pass — the applied HI-F1–F6 batch (delta `30d350c`)

- **Date/time**: 2026-07-22 0943 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike opened and pointed at the queue ("please do any review work"). This
  session authored **none** of: the sizescan/harvest-integrity doctrine deltas,
  the 2026-07-22 0819 cold pass that produced HI-F1–F6, or the application of
  Mike's accept-all ruling now under review (`30d350c`). The applier queued the
  `⏳` pointer and stopped; this brief is taker-written.
- **Named exposure**: at selection the taker read (a) the ROADMAP `⏳` pointer
  (which names the fix classes: "skip-dir bypass for stores, fence fail-safe,
  RECORD.md + template edits"), (b) `git log --oneline` subjects carrying the
  applier's and prior sessions' evaluative accounts — `30d350c`'s own subject
  ("integrity checked wherever a store lives"), the 0819 pass's finding count
  ("1M/3M/2n"), and the ruling shape ("Mike's accept-all") — (c) the file
  *names* in `git show --stat 30d350c` (no hunks), (d) `docs/method/REVIEW.md`
  in full at HEAD (needed to run the process; not an in-scope file of this
  delta), and (e) the closed SL application verdict
  (`reviews/2026-07-22-0244-sl-application-cold.md`) as the process precedent —
  a different cycle, but its shape may prime this pass's shape. Every
  evaluative claim in (a)–(b) is treated as a claim to re-run, not a fact.
  An application review cannot fully honour rule 2 — the sequence per
  REVIEW.md § Applying decisions: review the edited files at HEAD and commit
  findings *first*; open the prior verdict, decision stamps, and applier's
  intent record after. The residual exposure is named, not denied.

## What the work is (refs only)

Commit `30d350c` — the application of Mike's 2026-07-22 accept-all ruling on
the 0819 cold pass's HI-F1–F6 findings. In-scope files at HEAD:

- `tools/sizescan.py`
- `tools/test_sizescan.py`
- `docs/method/RECORD.md`
- `docs/build/templates/docs/ROADMAP.md`

**Deferred below the divider** (opened only after this reviewer's findings are
committed): the prior verdict file, the decision stamps, and the applier's
intent record.

## Ask

Run all four lenses on the applied delta; scope is the whole commitment.

1. **Approach & assumptions** — name the load-bearing assumptions first, then
   attack them. Does each applied fix discharge its finding *class*, or patch
   the instance? In particular: does whatever integrity checking the delta
   adds actually fire on the stores it claims to reach (re-drive it live, red
   leg included), and does any fail-safe genuinely fail safe — what happens on
   the malformed, the missing, and the adversarial input?
2. **Correctness & quality** — re-run every live proof in scope rather than
   reading it: the full test suite; any new test's red leg (revert the tool
   hunk → the suite must go red); sizescan itself against the live repo; the
   repo floors (linkscan, reviewscan, secretscan/leakscan via the hooks).
   Honest-labelling check: do the RECORD.md and template edits say what the
   tool now actually does — no overclaim, no silent scope-cut?
3. **Completeness / harvest** — anything the rulings required that the
   application skipped; any sibling doc or template still carrying retired
   wording; record hygiene consistent with the delta (CHANGELOG, ROADMAP,
   session index — read only after findings are committed where the record
   is evaluative).
4. **Security & privacy** — landed-delta shape: `/security-review` reads
   pending diffs, so it cannot genuinely be aimed at this work — discharge
   with grounds if that holds at run time. The lens still runs manually:
   the tool hunk is Python that walks the repo and parses files — check its
   input handling (paths, encodings, malformed frontmatter/fences), exec
   surface, and any way a crafted repo file could bypass or subvert the
   scan; design-altitude leakage in the doctrine/template text.

Cycle context: the 0819 pass returned a MAJOR, so this application inherited
rule-4 status; this pass is **terminal if it returns no MAJOR** (close rule) —
report findings either way; decisions are Mike's (rule 3: the chain is
self-authored doctrine).

---

## Deferred material (open only after findings are committed)

- `docs/reviews/2026-07-22-0819-harvest-integrity-gate-cold.md`
- `git show cfb0ae6` (decision stamps)
- `docs/sessions/2026-07-22-0819-harvest-integrity-cold-pass.md` (+ addendum)
- The record commits `f86e6ef`, `4e6e891`, `cc0bed3`
- The author seeded no questions; there is no author-written ask anywhere in
  this file. Everything above the divider is taker-written.
