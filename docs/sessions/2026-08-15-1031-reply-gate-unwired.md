# 2026-08-15 · 1031 UTC · The reply gate unwired — the guard was the defect

**Model:** Opus · **Worktree:** `plain-reply-unwired-0816`

## What Mike asked

> Look at the transcripts from sessions active in the last 12 hours. They keep
> repeating text like verdicts/summaries
> Why is that happening and how do we fix it

He did not name a cause. The investigation found one, and it was ours.

## The finding

Every near-duplicate assistant reply in the last 12 hours of transcripts sits
directly after a block from `tools/hooks/plain-reply.py`, the `Stop` hook ruled
live on 2026-08-09. No exceptions, and no second cause was found.

**A `Stop` hook cannot un-print.** Claude Code streams assistant text to the
terminal as it is generated; the hook fires afterwards. Blocking does not
retract the reply — the model emits a second full copy underneath the first. The
gate built to make replies readable was the largest single source of unreadable
output in the session.

Measured across the 12-hour window, from the transcripts:

| Measure | Value |
|---|---|
| Sessions active | 24 |
| Sessions hit by the gate | 16 |
| Turns blocked at least once | 29 |
| Turns blocked twice — verdict on screen three times | 6 |
| Median blocked reply | 3,332 characters |
| Longest | 8,628 characters |
| Characters reprinted | ~123,500 |

Two amplifiers, both measured. The rewrite fixes the reported findings and
introduces fresh ones the first scan never saw, so the gate fires on its own
output — one session produced three copies of the same 4.5k table. And the
second attempt seldom works: of the 6 turns that took a second block, 4 still
failed into the give-up path, so the second rewrite succeeded about a third of
the time while charging a third full copy.

The triggers were not "genuinely unreadable output", which is what the hook's
own comment claims it is calibrated for. The undefined-reference rule fired 39
of 61 times, mostly on board item identifiers sitting in linked table cells that
name the item beside them. The rest were near-misses: 47, 50 and 51 words
against a 45-word limit; 72, 77 and 78 characters against a 60-character limit.

## The demonstration nobody planned

The reply carrying this diagnosis to Mike was itself blocked — by this hook, for
naming a rule code while explaining that rule's behaviour. He read the verdict
twice while being told the gate makes him read verdicts twice.

## Mike's ruling

He had recommended-to reservations on record with him, not with us:

> As I have already said this is the exact opposite of what I want, you
> recommended this guard and I said I had several reservations all of which are
> proving true
>
> You will unwire this plain speak guard as it is making the very thing it is
> supposed to prevent many times worse. You will roadmap that we will either
> destroy this guard as its not just USELESS but DANGEROUSLY bad, or fix it...
> perhaps by changing its purpose from a guard to a data collector to find when
> you are giving me unusable responses to the VS code sessions to try and find
> the root cause(s) and see what we can change to fix it

## What was done

1. **Unwired**, first action: the `Stop` stanza is out of the machine's
   `~/.claude/settings.json`, verified `hooks = {}`, and no other wiring for it
   exists on this machine. The change is machine-local; nothing in any repo
   installed it.
2. **Roadmapped**: `docs/roadmap/020-…/310-the-reply-gate-is-unwired-….md`,
   carrying his ruling verbatim, the measurement, and the two options costed —
   destroy, or repurpose as a silent collector. The item favours the collector
   unless he rules otherwise, and says why.
3. **The false premise corrected in all three places that asserted it** —
   `plain-reply.py`'s docstring, `tools/README.md`'s two-planes section, and
   `COMMUNICATION.md`'s enforcement clause. Each said a blocked reply is
   rewritten *before the principal reads it*. None had been checked against a
   terminal. The code stays in the tree, wired to nothing, with a stop notice at
   the top of the file.
4. **The repo plane left alone** — warn-only, no such failure mode, separately
   ruled in scope on 2026-08-10.

## What this cost, and the rules it earns

**The programme's organising defect, one surface over.** Track A exists because
a check can run, exit 0, and cover nothing. This is its sibling: a check that
runs, detects correctly, and whose *stated effect never existed*. Detection was
sound the whole time. The remedy was the unchecked half.

**Rule 1 — a machine-decidable rule can still have no machine-deliverable
remedy.** Before enforcing, establish that the enforcement point can deliver the
fix, not merely spot the fault. The `Stop` hook could always spot it and could
never fix it, and one look at a live terminal would have shown that on day one.

**Rule 2 — an approval is not the whole ruling.** Mike states he raised several
reservations when this guard was recommended. The record captured only *"switch
it on, proposed"*. The objections that would have predicted this failure were
never written down and never tested against the build. They are not
reconstructed here, because reconstructing them from memory is the same error
one level down. When a recommendation is approved with reservations, the
reservations belong in the record beside the approval, and each becomes a check
the build has to answer.

**A boundary for whatever replaces it.** A collector's log holds verbatim reply
text from every repo. It is machine-local, never committed — the same boundary
that keeps personal context out of this public tree, and it has to be stated in
the design before anything is built.

## Owed

- 🎯 **Mike's ruling**: destroy the guard, or fund the collector.
- ⏳ **Cold review** queued on the doctrine edit — self-authored, so a non-author
  session takes it (REVIEW rule 4).
