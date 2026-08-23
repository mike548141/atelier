# 🔀 Concurrency doctrine stops at the repo edge — Mike-commissioned, 2026-08-23

> *"a clean tree tells you nothing about who's holding a 348 GB hash walk on a NAS"*
> — the agent, reporting to Mike, who commissioned this: *"that's a good point —
> roadmap that to atelier to consider and work on improved doctrine."*

`CONCURRENCY.md` is good and it is **git-centric**. Every rule it gives —
`pull --rebase --autostash` at session start, push after each commit, take a
worktree for write-heavy work, stage explicit paths, read the whole staged index —
protects **the repository**. In an estate repo, the repository is often not where
the damaging collision happens.

## What the gap looked like, measured rather than imagined

Two docker-heap sessions ran in parallel on 2026-08-23. The git side behaved
exactly as doctrine intends: both took worktrees, both pushed, one had already
merged to main, and there was no conflict at any point. Meanwhile, off-repo:

- one session held **two multi-hour hash walks** over 348 GB and 68 GB on a NAS,
  plus a long `rsync`, none of which appears in any `git status`;
- it also held a **shared file on that host** — `~claude/media-split.sh`, which it
  overwrites by `scp` on every tool change. A peer running or replacing that file
  mid-job breaks the job;
- the peer session did a `docker pull`, a `docker run` against the **secret
  store**, and one **failed login** against a rate-limited API (5 attempts per
  15 seconds — two sessions probing it concurrently is a lockout, not a
  collision);
- and the peer's own container census **misattributed the first session's two
  verification containers**, reporting `elegant_williams` and `nostalgic_jones` as
  "neither is mine". They were the first session's, running
  `media-split.sh --verify-only`. Docker had named them at random.

🔎 **Nobody was careless.** Both sessions announced, both stood off on contact,
and the collision still had to be resolved by a human noticing. The doctrine did
its job on the surface it covers, and was silent on four others.

## The generalisation worth having

The estate's shared surfaces are not one thing. A partial list, all of them
invisible to `git status`: a **NAS or filesystem**; a **running container fleet**
(restarting one container can break a peer's job — the first session proved this
by restarting *its own*); a **shared file on a remote host**; a **live
database**; a **cloud account, DNS zone or scheduled job**; and a **rate-limited
API**, which is the nastiest because contention there looks like a credential
failure rather than a conflict.

🔑 **And the existing rule already generalises, if it is read carefully.**
`CONCURRENCY.md` says *"a message reserves nothing; only a pushed artefact does"*.
That is exactly right and it is not about git — the point is that a claim must
live in the shared medium, durably, where a peer will actually look. Off-repo the
artefact is not a commit; it is a **marker on the host itself**.

## Three candidate rules, cheapest first

- **Name what you launch.** Anything started on a shared host — container,
  process, scheduled job — carries an owner marker, so a peer's census can
  attribute it without asking. This session is its own proof: `media-split-Photos`
  was attributable at a glance and `elegant_williams` was not, and they were the
  **same tool** doing the **same job**. Nearly free, and it fixes the specific
  confusion that actually occurred.
- **Announce the non-git claims too.** The file-set announcement on open should
  cover hosts, long-running jobs, shared remote files and live services — not
  only paths in the repo.
- **A long job's claim outlives its session.** A lockfile or marker beside the
  work, not a chat message, because the session that holds it may be gone or
  compacted when a peer arrives. This is the *"only a pushed artefact"* rule
  applied to the surface the work is actually on.

## ⚠️ What would make this worse rather than better

A locking protocol. The estate has a standing lesson about guards that produce
more noise than signal, and a distributed-lock design for a household would be
both over-built and quietly ignored the first time it was inconvenient. **The
cheap 80% is naming what you launch and announcing what you hold.** Decide those
first, and decide whether anything stronger is needed separately, on evidence
that the cheap version failed.
