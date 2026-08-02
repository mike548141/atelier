# Cold pass — the publication-surface delta (`a9ab2cf`)

- **Subject** — the estate-wide untracking of `.claude/settings.json` (Mike's
  ruling ⓑ: untrack everywhere, one uniform rule) and the doctrine rewrite that
  carries it: `docs/build/REPO-STANDARD.md`, `docs/method/TOOLBOX.md`,
  `docs/build/templates/gitignore`, `skills/create-repo/SKILL.md`, `.gitignore`,
  and the removal of the tracked `.claude/settings.json`. Landed `a9ab2cf`,
  2026-07-29, by the 1418 session (Opus 5). Built and shipped.
- **Type** — built work applying a ruled decision, plus doctrine text
  (rule-4 class: the wording is the author session's own).
- **Scope** — the `a9ab2cf` diff and the same surfaces at HEAD; the decision's
  application, not the ruling itself (Mike ruled ⓑ — the ruling is settled;
  *how faithfully and completely it was applied* is the review).
- **Spawn provenance** — rule 4: this brief is written by the taker, a Fable
  session Mike started on 2026-08-02 and pointed at the review queue
  ("Please do any review work"). The author session (2026-07-29 1418, Opus 5)
  neither started nor instructed it. Reviewed cold from the refs-only ROADMAP
  pointer; the shared intent record stays unopened until all four queued
  verdicts are durably committed, then is read at reconcile.
- **Load-bearing assumptions to challenge**
  1. The untracking is *actually in force*: the file is untracked at HEAD,
     ignored so it cannot silently return, and the working copy survives for
     the harness to read.
  2. The four doctrine surfaces now say the same thing — no fifth surface
     still instructs committing the file, in this repo or its templates.
  3. The named cost is honest and complete: the allowlist stops being a
     shared reviewable record; history retains the published copy. Nothing
     *else* broke — hooks, CI, floor — that the record does not name.
  4. The class generalisation ("guard files are self-describing; presence,
     not contents, is the exposure") is sound, and the diff does not itself
     open a new instance of the class it closes.
  5. Untracking-by-gitignore is the right mechanism versus alternatives the
     ruling did not foreclose (e.g. a committed *template* allowlist beside an
     untracked live one).
- **Grounding to re-run** — `git ls-files` for the path; `git check-ignore`;
  a tree-wide sweep for surviving "commit settings.json" instructions; the
  floor (`tools/floor.py` scanners) and both test suites at HEAD.
- **Non-goals** — Mike's ruling itself (decided, not reviewable here);
  `publishscan` internals (its own queued pass); children's pin-bump adoption
  (queued estate work, not this delta).
- **Security scanner** — `/security-review` reads pending diffs; this delta is
  landed and its surfaces are markdown, gitignore text, and an untracking — no
  pending diff for it to reach, and markdown is excluded by the scanner's own
  file-class rules, so a clean pass would be definitionally empty. Discharged
  on those grounds; the security lens runs manually at both altitudes.

---

## Verdict — PASS-WITH-FINDINGS (1 MAJOR / 2 minor)

Reviewer: the taking session (Fable, started by Mike 2026-08-02, pointed at the
queue; the author session neither started nor instructed it — rule-4 provenance
restated per REVIEW.md). Reviewed cold from the refs-only pointer.

**Exposure disclosure, owed before the findings.** Mid-review, a tree-wide
sweep for surviving `settings.json` instructions returned, among its hits, the
`SESSIONS.md` index entry for the author session — a condensed author account
of all four queued deltas — into this reviewer's context before findings were
durably written. The sweep should have excluded the records files; this is the
same channel class as SL2 (a scan feeding deferred material to the reviewer),
now live-proven a second way. The central finding below (PS2's identical-bytes
observation) was formed before the exposure but was not yet durably written;
weigh it accordingly. The full intent record remained unopened until after all
four verdicts were committed (see the reconcile addendum).

### Findings

- **PS1 — MAJOR (correctness / completeness).** The canonical standardise
  process still re-creates the exposure the delta closes.
  `docs/build/REPO-STANDARD.md` § *Process — standardise an existing repo*,
  step 2, instructs: *"Apply the safe mechanical bits uniformly — committed
  `.claude/settings.json`, `.gitignore` hygiene…"*. That sentence survived the
  delta unchanged while the skill's stamped copy of the same step was fixed
  (`skills/create-repo/SKILL.md` § standardise now says `git rm --cached`
  either settings file). The canonical source now contradicts both its own
  file-set bullet (line ~98) and its stamped copy — inverted parent/child
  drift, the same shape the delta itself was correcting in `rpi`'s favour. A
  session standardising an existing repo from the canonical file would
  re-commit the allowlist estate-wide. The commit message's "mandated
  committing that file in four places" was a five-place reality — a count
  wrong in the familiar direction (the roadmap's blast-radius figures have
  been wrong five times; counts keep being estimated, not swept).
  *Counsel:* delete "committed `.claude/settings.json`," from step 2 and add
  the skill's pre-2026-07-29 untracking note to the canonical text; the fix is
  mechanically entailed by Mike's existing ⓑ ruling, so it needs application,
  not a new decision.
- **PS2 — minor (security & privacy / honesty of the named cost).** The
  published seed template `docs/build/templates/claude/settings.json` is
  byte-identical to the allowlist the delta untracked. The author saw the
  question — `publishscan` allowlists the path with "a TEMPLATE, not live",
  and TOOLBOX argues a template is "not per-repo state" — and the argument is
  sound as far as it goes: what stays published is the estate *default*, not
  any repo's live grant. But the named-cost passages (REPO-STANDARD, TOOLBOX,
  the commit message) never state the residual: any repo whose live allowlist
  never diverges from seed is still exactly mapped by the public template,
  and the template *is* atelier's own pre-delta live list, bytes unchanged.
  "Cannot be unpublished" is said of history; "still published at a template
  path, deliberately" is not said anywhere the cost is named.
  *Counsel:* one sentence naming the residual in TOOLBOX's named-cost
  paragraph (and/or REPO-STANDARD's bullet). Whether the residual is
  acceptable is the principal's call (rule 3); this reviewer's view is that
  it is — a generic seed is the shareable-repo product working as intended —
  provided it is named.
- **PS3 — minor (security & privacy, design altitude).** The sibling template
  `docs/build/templates/claude/settings.local.json` — tracked, published, and
  copied into every new repo by create-repo step 3 ("copy both in") — grants
  unrestricted `Bash` plus `defaultMode: acceptEdits`. It predates this delta
  (moved in `eba2e15`), but the delta promoted the template directory to the
  load-bearing seed path for every clone without auditing what sits there. A
  maximal unattended grant as the published, seeded default is a stronger
  reconnaissance-and-posture statement than the allowlist the delta untracked.
  *Counsel:* either narrow the template to a placeholder, or mark the grant
  deliberate in-file with its grounds; and note it is *outside* `publishscan`'s
  allowlisted-template reasoning, which was argued for `settings.json` only.

### Lens results

1. **Approach & assumptions** — the uniform (ⓑ) application is faithful where
   it landed; the visibility-conditional-drift reasoning is sound and is now
   carried in the text, not only the ruling. Assumption 1 held (untracked at
   HEAD, root-anchored ignore in force, seed template exists and is tracked).
   Assumption 2 failed → PS1. Assumption 3 partially failed → PS2. Assumption
   4 surfaced PS3. Assumption 5: the mechanism is sound; the ruled option set
   already weighed the alternatives.
2. **Correctness & quality** — `git ls-files` confirms the untracking;
   `git check-ignore` resolves to the new root-anchored pattern; the four
   *named* surfaces agree with each other; the fifth (PS1) does not.
3. **Completeness / harvest** — sweep found no other live commit-the-allowlist
   instruction outside PS1; CHANGELOG/session mentions are historical record,
   correctly untouched.
4. **Security & privacy** — design altitude: net exposure reduced (live
   per-repo grants unpublished); residuals are PS2/PS3. Code altitude: no
   executable surface in this delta. `/security-review` discharged in the
   brief — landed markdown/gitignore delta, nothing it can reach.

### Grounding re-run

- `git ls-files | grep settings.json` → only the two template paths tracked;
  `.claude/settings.json` absent from the index. `git check-ignore -v` →
  `.gitignore:15`. Working copy present in the primary checkout.
- Floor green at HEAD (all ten scanners, pre-commit plane); `python3 -m
  unittest discover -s tools` → 820 tests OK; `node --test
  instruments/*.test.js` → 207 pass, 0 fail.

Rule 3 applies throughout: the counsel above is the reviewer's position,
labelled as such; decisions are the principal's. PS1's MAJOR keeps this
delta's cycle open past its application.
