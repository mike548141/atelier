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
