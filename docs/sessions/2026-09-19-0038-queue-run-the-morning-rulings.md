# 2026-09-19 · Queue run — building this morning's rulings

**Session:** Opus 5 (VS Code) orchestrating, Sonnet 5 workers in isolation
worktrees · `main` for claims, records and inline doctrine · in progress; each
item closes in its own commit, so this record grows per item.

## The ask

Mike's standing queue-run brief: *"I have a long list of work queued and I want
you to deliver it — across this session and any that follow. Start here, then
use your own judgement on what's next."* Run per `CONCURRENCY.md` §
*Orchestrated queue runs*. Tier check at open: Opus 5 orchestrating, stated
and not put to Mike (`ECONOMICS.md` § *Match the model to the job*, the
2026-09-16 standing default); the `⏳` review pointers name Fable, so this run
takes none of them.

## Opening state

`main` at `f1b34e7`, clean, no stashes, one worktree. The last two commits
(the 2026-09-19 rulings on `020/370`, `020/380`, `320/300`, `115/030`,
`320/010`) came after the previous run's closing entry, but they appended to
that run's own record, so they read as its tail rather than a live peer. One
open PR, #81, a child hand-up.

## Items

### PR #81 — the tier-question hand-up (merged as `320/320`)

The child filed at `320/310`; the ruling sitting took `320/310` an hour later
on `main` for *"should `pathscan` block"*. Two new files never text-conflict,
so only the number collided. Merged `--no-ff`, renumbered to `320/320`, index
regenerated. Its substance bears on this run's own open: the role check
against the 2026-09-16 "don't ask which tier" default. This run followed the
newer default (stated the tier, did not ask); the contradiction itself stays
a decision for Mike on `320/320`.

### Wave 1 — the three items ruled this morning

Claimed together (`9847c3d`): `020/370` (bounded-memory `secretscan`),
`320/010` part 1 (declared `pathscan` resolution roots), `115/030` (the floor
copied verbatim). Three Sonnet 5 workers, disjoint files; the `115/030`
doctrine half written inline by the orchestrator, because no scanner catches
a wrong rule.

### 320/320 — the tier contradiction, ruled mid-run and swept (inline)

The session was cut overnight with the three wave-1 workers still running;
their worktrees survived, two with commits, one dirty, and all three were
resumed from their transcripts rather than re-dispatched. Mike then ruled the
hand-up merged above, mid-run: *"the cheapest model that can do a good job is
the one that should be used for every job including orchestration. Fix
everything that is causing this mess"*, and on the one question it raised —
whether that reopened the principal-named review tier — *"fable reviews remain
fable reviews"*.

The mess was a **four-link chain**, and cutting any one link would have left
the question reachable by the other three: the run brief told a session to
confirm it was on the capable tier, `CONCURRENCY.md`'s role check told it to
stop if it wasn't, `ECONOMICS.md` defined the capable tier as *the most
capable model available*, and the estate's records rank the models. All four
are cut (`c38b7da`), plus `AUTONOMY.md`'s first-of-kind bullet and the two
places review read as *most capable available* rather than *the named tier*.
The run-open check now **states the tier and proceeds**. Two stops survive,
neither about rank: work that outruns the model doing it, and a `⏳` pass whose
named tier the session cannot honour.

Worth recording because it is the pattern's own failure mode: **the prompt
Mike pastes carried the defect too** — `session-open-prompt.md` said *"confirm
you're on the capable tier … stop and say so"*, so every run he opened
re-injected the stop the doctrine was being fixed to remove. A doctrine sweep
that had only touched `docs/method/` would have read clean and changed
nothing. Rule-4 cold pass queued at `160/330`; this author may not take it.
