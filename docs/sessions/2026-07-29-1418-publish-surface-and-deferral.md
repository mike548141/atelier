# Session — publication surface + the review deferral (2026-07-29 1418 UTC)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 226+1 -->
- [2026-07-29 · 1418 UTC · The deferral was unfollowable; the parent still had the bug the child fixed (Opus, wt: publish-surface-and-deferral)](2026-07-29-1418-publish-surface-and-deferral.md) — Mike's three asks in one sitting: *"cold reviewers are seeing what is below the divider… do we need a better mechanism?"*, *"study, learn and adapt from taking rpi public"* → *"this should be policy as code"*, and *"sessions are still running into the issue when it is written down 3 times"*. **All three were right, and each had an answer already written down that nothing enforced.** 🔎 **The deferral**: REVIEW.md rule 1 called the below-the-divider deferral *"structural, not willpower"* and it was neither — **reading a file is atomic**, so a deferred section is consumed by the act of reading the brief it sits in, and its *open only after…* label sits **inside the thing it warns about**; the rule was **unfollowable, not merely unfollowed**, since nobody can know where the divider falls without reading past it. It had already leaked once through a side channel — the 2026-07-21 pass, where a pending-changes scanner swept the dirty brief and fed its deferred section to the reviewer pre-draft — and that incident was on the record as a caution about the *scanner*, never about the *box*. Fixed by moving the bytes, not the wording: deferred material to a sibling `.deferred.md`, folded back below the verdict at close (split for the duration, one file at rest), with `reviewscan` gaining the mechanical half — it fires on the **author** at write time, before any reviewer is exposed. Verified against all 76 briefs and driven live red-then-green. **The doctrine now states what the split does NOT buy**: it makes early exposure a deliberate act that leaves a trace, not an impossibility — only a context partition (an orchestrator holding the bytes) is genuinely structural, and overclaiming twice would have been the same defect the rewrite was fixing. `reviewscan` deliberately does **not** lint the fold-back: a reviewer commits findings *before* opening the deferred file, so such a lint would fire on correct behaviour at exactly the prescribed moment. 🔎 **The rpi harvest**: its post-flip cold pass (F1) found the committed `.claude/settings.json` publishing the exact list of commands a session runs **unprompted**, as going public opened untrusted inbound into those sessions — and rpi's local fix **diverged from atelier doctrine**, which mandated committing that file in four places. The child was right, the parent was wrong, nothing carried it upward; Mike asking is what surfaced it. **Twelve repos tracked it** (swept, not estimated — the roadmap's blast-radius figures have been wrong five times). Mike ruled **ⓑ untrack everywhere, uniform** over public-only: a visibility-conditional rule becomes silently wrong the day a repo flips. 🎯 **The class was wider than the file, and is why `publishscan` exists**: every content scanner passed that allowlist *correctly* — it holds no credential and no personal fact — because **the exposure was the file's presence in the tree, not its contents**, and no check in the floor asked that question. New scanner, registry-wired blocking with an advisory form offered for adoption (eleven children would otherwise red on a file nobody told them about); patterns carry provenance per pattern rather than blurring one finding into a survey; it deliberately **allows** the self-describing guard files (`.atelier-floor.json`, the `.<scanner>ignore` set) — they map where the defences are weak *and* must travel for the floor to run, so that exposure is accepted and mitigated by requiring a stated reason for every exemption, never by hiding them. 🚩 **A design error in it was caught by `floor.py`'s own test suite, not by me** — the first cut hard-failed on a tree with no git, which would have made it unrunnable in every child's fixtures; fixed at the behaviour, not the test. 795 → 820 tests, green. 🔎 **The recurrence question**: PROPAGATION gains *When a rule keeps breaking — climb, never restate* (framing → mechanise at the moment of failure → **remove the situation**) and *One statement, stamped copies — never three originals* — three independent statements is the defect; one canonical plus **stamped** copies at the point of use is the mechanism working, and `stampscan`, built to watch exactly that, is shelved on a parser defect, so the stamp discipline is convention watched by nothing. The third rung is what this session actually did to the deferral. **Owed, and said rather than fudged**: the DRY *survey* was not run (R2) — the rule for handling triplication landed, the corpus was not swept, and guessing which passages are redundant is how a consolidation silently drops two of three real facets; the recurrence count is still unmechanical (R1); F5's public-records ruling (P6), the visibility-aware floor (P3), the GitHub-settings publish gate (P5) and the leakscan `--require-terms` ci-plane gap (P4) are queued, not done; P7's transcript harvest is a session of its own. Four rule-4 `⏳` pointers queued in the landing commits, **none spawned by this session**.


**Model:** Opus 5 (1M context) · **Worktree:** `publish-surface-and-deferral`
· **Principal:** Mike, three asks in one sitting.

## What Mike asked

1. *"I think we might have an issue with reviews. If I understand correctly
   cold reviewers are seeing what is below the divider / line before they
   produce a verdict… If that's true do we need a better mechanism?"*
2. *"We should study, learn, and adapt from taking rpi repo public tonight… <!-- datescan:allow: verbatim quotation of the principal's ask -->
   perhaps files like the claude settings file should not be published."* Then,
   after the finding landed: *"we also need to consider any other files, or
   scenarios… this should be policy as code."*
3. *"Sessions are still running into the issue when it is written down 3
   times"* — DRY the doctrine, and make recurrence structural.

## What was found, before anything was built

**The deferral was unfollowable, not merely unfollowed.** REVIEW.md rule 1
called the below-the-divider deferral *"structural, not willpower"*. It was
neither: reading a file is atomic, so a deferred section is consumed by the act
of reading the brief it sits in, and its *open only after…* label ends up
inside the thing it warns about. Nobody can know where the divider falls
without reading past it. It had **already leaked once through a side channel** —
the 2026-07-21 pass, where a pending-changes scanner swept the dirty brief and
fed its deferred section back to the reviewer pre-draft. That incident was on
the record as a caution about the *scanner*, never about the *box*.

**The parent still had the bug the child had fixed.** `rpi` went public
2026-07-29; its post-flip cold pass found (F1) that the committed
`.claude/settings.json` published the exact list of commands a session runs
unprompted, at the same moment going public opened untrusted inbound into those
sessions. `rpi` fixed it locally — and thereby **diverged from atelier
doctrine**, which mandated committing that file in four places
(`REPO-STANDARD`, `TOOLBOX`, `templates/gitignore`, `create-repo`). The child
was right, the parent was wrong, and nothing carried it upward; Mike asking is
what surfaced it. Twelve repos tracked the file (swept, not estimated).

**The class was wider than the file.** Every content scanner passed that
allowlist correctly — it holds no credential and no personal fact. *The
exposure was the file's presence in the tree, not its contents*, and no check
in the floor asked that question.

**The answer to ask 3 was already half-written and unenforced.** The ROADMAP's
anti-slop registry already held the promotion rule (recurrence, not severity,
earns a check); REVIEW.md already held Mike's 2026-07-19 framing rule. Neither
fires, because nothing can count recurrences.

## What landed

| Commit | What |
|---|---|
| `a9ab2cf` | Allowlist untracked estate-wide (Mike ruled ⓑ) + all four doctrine surfaces amended |
| `3acf7d2` | Deferral split to a sibling `.deferred.md` file; REVIEW.md rewritten; `reviewscan` gains the mechanical half |
| `8bdcfaa` | `publishscan` — new scanner, registry-wired blocking, 14 tests |
| this | PROPAGATION gains the recurrence ladder + the stamped-copy rule; session record; review pointers |

**Mike's rulings this session:** the allowlist question — option ⓑ (untrack
everywhere, one uniform rule) over public-only or trimmed-but-committed;
grounds recorded at the ruling. The split-file deferral mechanism — approved as
proposed.

## Honest notes

- **A design error in `publishscan` was caught by `floor.py`'s own test suite,
  not by me.** The first cut hard-failed on a tree with no git, which would
  have made the scanner unrunnable in every child's fixtures. Fixed at the
  behaviour rather than the test: with no git there is no tracked set to miss,
  so a visible exit-0 skip is honest, while git absent or a corrupt repo stays
  exit 2. The mechanical floor doing to my work exactly what it exists to do.
- **The split is not structural, and the doctrine now says so.** It makes early
  exposure a deliberate act that leaves a trace, rather than the unavoidable
  default. Only a context partition — an orchestrator holding the deferred
  bytes — is genuinely structural. Overclaiming this twice would have been the
  same defect the rewrite was fixing.
- **`publishscan` is a denylist**, so a novel defence-mapping file passes until
  someone teaches it (P2a). Its patterns carry provenance per pattern: one is
  grounded in F1, the rest are named as standard practice rather than dressed
  up as findings.
- **The DRY survey was not run.** The *rule* for handling triplication landed;
  the corpus was not surveyed, and guessing which passages are redundant is how
  a consolidation silently drops two of three real facets. R2 carries it.
- **`rpi`'s own records date some 2026-07-29 UTC work as 2026-07-30** — the NZ
  local/UTC slip `datescan` exists to catch. Not fixed here (another repo's
  records, and not this session's lane); worth a line when P7's harvest runs.

## Owed

Three cold passes queued as `⏳` in ROADMAP, all rule-4: the deferral doctrine
delta, the publication-surface doctrine delta, and `publishscan` as
first-of-kind tooling. **Not spawned by this session** — this session authored
all three (REVIEW.md rule 4: the review comes from a session the author neither
started nor instructed).
