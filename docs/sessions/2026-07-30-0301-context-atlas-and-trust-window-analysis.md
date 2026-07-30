# 2026-07-30 · 0301 UTC · The Context Atlas, and what the instruments could not see

*Opus 5, inline on `main` (analysis only — no worktree; the sole repo change is
this record and its ROADMAP follow-ups).*

## What was asked

Four things, in sequence, each reframing the last:

1. Run `ccrepo` and show the output.
2. Render it well, add an analysis of context size across all sessions, and
   cross-reference context size against issues/problems/incidents — mocked up
   loosely, to be refined.
3. How much context would loading all of atelier's doctrine cost?
4. Sessions across 2026-07-24 → 2026-07-26 carried a high number of issues that
   damaged trust in Claude and in the work it produced. Against every other
   session, what can be inferred as root causes?

## What was built

A **Context Atlas** — an interactive page plotting all 470 priced sessions on a
single context axis, rowed by repo, coloured by the worst failure class the
harness recorded, with per-session drill-down (context distribution, incident
list, cost). It lives outside this repo, in the session scratchpad, and was
published as a private artifact: it carries per-repo cost and usage detail that
is estate context, not doctrine, and this repo is public.

Its one structural idea worth keeping: **atelier's own doctrine-load cost is
plotted on the same axis as the sessions**, so "what filling a window costs" and
"what a session actually used" are directly comparable. Measured at `ecc9f49`:
`method/` alone ≈ 81k tokens; `method/` + `build/` + `decisions/` + ROADMAP +
README + CLAUDE.md ≈ 163k; every markdown file under `docs/` ≈ 854k. Estimated
at 3.7 bytes/token — an estimate, not a tokeniser count. The median session peak
across the estate is ~168k, which is to say **a typical session is already
carrying about as much as the whole binding doctrine plus the roadmap**, and the
full `docs/` tree is deeper than every session ever run bar one. That is the
quantitative case for CLAUDE.md's read-on-demand order.

## The finding that matters, and it is about the instruments

The cross-reference was built on an incident taxonomy read out of the raw logs:
tool failures, API errors, session and model limits, prompt overflow, forced
compaction, interrupts. Across the estate the honest result was that **context
size does not degrade the work** — tool-failure *rate* is flat from 28k to 934k
(Spearman ρ = −0.05), and the apparent link between deep context and more errors
is a length effect (context vs message count ρ = 0.85). What context genuinely
causes is a rarer, separate mode — overflow and compaction — concentrated almost
entirely in the deepest handful of sessions.

Then the trust question arrived, and the same taxonomy said the affected days
were **cleaner than baseline**: tool failures at 0.71× the estate rate, zero
limit hits, zero overflow, zero compaction.

That is the finding. **The mechanical instruments cannot see a trust failure.**
Tool errors, dropped connections and exhausted windows measure whether the
machinery ran. Trust is damaged by work that *ran perfectly* and was wrong,
unverified, or not the agent's decision to make. An observability layer built
only on harness error flags will report a clean week for the worst week — and
this session's own Atlas would have done exactly that.

The signal that did carry it was the principal's own language: corrective
markers counted in human-typed turns only. Overall correction rate was flat
(0.94×), but *trust* language ran 5.8× and frustration 3.9× — a specific
signature. Not "that's wrong" more often; "I don't trust this" more often. Work
that was plausible and unverifiable, rather than visibly broken.

## The root-cause analysis, and three hypotheses it killed

Reading the flagged turns surfaced five incidents in the window, all one class:
**the agent acted unilaterally on ground the doctrine reserves to the
principal** — recording a deferral as a decision never made; deleting records as
"duplicates" without showing the removal list; running a cold review on the
wrong model tier, voiding the pass; running a queue against claimed work.

Widening from one repo to the estate is what made the analysis honest. Only five
repos ran in the window, and the damage sat in the two whose work is
change-producing and governed. Which falsified, in turn:

- **A new model tier as the cause** — `shed` ran the same new model on the same
  days, build-heavy and established, with zero corrective turns.
- **A new harness version** — same control, same result.
- **Context size** — same control at 342k peak, clean.

And one hypothesis was **falsified and then withdrawn**: a research-heavy repo's
2,403-message subagent run was used to kill the "orchestration causes it"
hypothesis, until the principal pointed out that repo is a week old and almost
entirely deep research. Re-profiling by tool use confirmed it — 50.6% research
share against a next-highest of 24.6% — so it was never a valid control for
orchestrated *change* work. Orchestration went back on the table.

What survives is narrower than any single cause: **distance without a review
step, on work that changes things.** Orchestrated fleets are one route there;
long solo autonomous runs are another (the worst single session had no subagents
at all, and ran 12 assistant messages per turn of the principal's). The common
factor is that the interval between the principal's checkpoints grew while the
work was altering records — and the review tier that would normally catch it was
not running on those days.

**This is a hypothesis fitted after the fact on five incidents.** It has a
mechanism and a clean recovery signal, and it is not proof. Its forward test is
named in ROADMAP.

## Corrections made in flight — three, all mine

Recorded because the apex requires it and because each is a reusable failure
shape, not because the count flatters anyone:

- **The overflow signal was self-contaminating.** The first scanner text-matched
  the literal refusal string, and so counted every transcript that *discussed*
  the error — including the session running the scan. It inflated overflow from
  4 real events to 12. Fixed by keying every error class to a harness-set flag
  that conversation cannot fake. The general shape: **a scanner that greps for
  the name of a failure will find the sessions that talked about it**, and an
  agent analysing its own logs is inside its own corpus.
- **A premise correction stated too broadly.** The archive was reported as "not
  a superset" on a session count, without naming the unit; the principal
  correctly pushed back that it holds over a thousand transcripts. Both were
  true — 1,404 archived files, of which 892 are transcripts against 902 live.
  Measuring in one unit and asserting in another is how a true number becomes a
  wrong statement.
- **A tool-use profile with broken attribution.** Subagent transcripts live
  under `<session>/subagents/`, so grouping by parent directory filed every
  repo's delegated work into a single bucket — and delegated work is precisely
  where the research happened. It reported one repo as 2% research when the
  corrected figure is 50.6%. Caught only because the principal's own account of
  that repo contradicted the output.

## Also established, incidentally

**Message count bounds context; wall-clock time does not.** Across 448 sessions,
message count vs peak context is ρ = +0.877, elapsed minutes only ρ = +0.525,
and no session estate-wide is short-but-deep (<30 messages, >250k peak). A
session deliberately shortened in *time* by 84% but in *messages* by 58% saw its
peak context **rise**. Anyone throttling context should cap messages, not
minutes — and the larger lever is still what gets read into the window early.

## Owed

Nothing is claimed as done that is not. No doctrine was written this session:
the evidence-hygiene finding is strong and repeatable enough to belong in
`EVIDENCE.md`, but landing doctrine at wrap-up would queue a fifth `⏳` review
onto an already-loaded queue and half-land a change that deserves its own scope.
Both it and the trust-window follow-ups are queued in ROADMAP as candidates
instead.

The Atlas remains a **first mockup**, unrefined, and the run against the archive
that the principal asked for has not happened — the mockup was overtaken by the
trust-window question and never refined. Both carried in ROADMAP.
