# 2026-10-16 · 2345 UTC — Filing: the close declaration must cover subagents

**Tier:** Fable 5.1, a session with no repo (the principal's home directory),
touching atelier only to file one board item. No workers.

**The brief.** The principal asked for every session he had closed in the
previous day to be checked for subagents still running when he closed it. He
had been closing tabs on the "ready to close" signal, trusting it covered
subagents. Then: *"lets make sure atelier address this in its close out checker
tool and the doctrine so its not left to me remembering to check for subagents
still running"*, and *"File it with atelier to do the work"*.

## What was done

- **The audit, outside this repo.** Every session transcript touched in the
  previous 24 hours was read fresh: 30 sessions, 21 closed, 240 subagents
  launched by the closed ones. Every "ready to close" claim in a closed session
  was made with no agent still working. Eleven agents in four sessions were cut
  by the host crash of 2026-10-16 07:35 UTC and recovered only because each
  session was resumed; one was stopped on purpose and named at the close. No
  agent worktree remained anywhere. One merged agent branch from 2026-10-06 was
  found lingering here and deleted.
- **Filed `020/420`:** `ccclose` gains a twelfth check, *Subagents finished*,
  and `RECORD.md` and `CONCURRENCY.md` gain the agent list in what a close
  declaration carries and measures. The item holds the transcript facts the
  build needs (where agent transcripts live, their metadata, the three shapes
  the completion notification takes, the finished test), so the builder does
  not rediscover them.

## Not done, and why

- The build and the doctrine edits. The principal's instruction was to file,
  not build, so the work waits for a queue run. No claim was taken.
