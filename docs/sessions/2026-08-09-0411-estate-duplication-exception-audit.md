# 2026-08-09 · 0411 UTC — the estate duplication + exception audit

**Model:** Opus 5 (1M context) · **Worktree:** `doctrine-adoption-ruling-0809`
· **Landed:** `03bcfeb` (doctrine) + this commit

Mike commissioned two sweeps across all 16 children: what **duplicates or
conflicts** house doctrine, and whether every **exception to the guards** is
well-reasoned and properly recorded. He named a suspicion to test — that
`faves`' model-economics doc repeated atelier doctrine and broke DRY.

## The suspicion was right, and it was already half-fixed

`faves/docs/MODEL-ECONOMICS.md` *did* restate house doctrine, and had been
trimmed to repo-local facts eleven hours earlier on Mike's own DRY ruling
(`d61712a`, 83 lines deleted). Reported as remediated rather than discovered —
but the sweep found the same class **live in three other children**, and worse
than in the repo that prompted the question:

| Repo | Lines | Refs up | State |
|---|---|---|---|
| `faves` | 51 | 3 | ✅ fixed — points up, keeps only repo-local measurements |
| `ros` | 106 | **0** | ❌ full restatement, two superseded models |
| `rpi` | 69 | **0** | ❌ same, and the repo is **public** |
| `nova` | 30 | 0 | ❌ same, and names `ros` as *"the canonical version"* |

Two of these are **conflicts**, not merely repeats: a **two-pool** billing model
(`Fable 5 = usage-billed, real money`) that the parent superseded with
billing-state-of-the-marginal-token, and a **fixed model-to-role mapping**
(*"Opus the workhorse, Fable the reviewer"*) that the house replaced with
tier-by-risk. `nova` compounds it by pointing **sideways to a sibling** for
canon, minting a second root against ADR 0001.

The failure mode is evidenced, not predicted — `faves` recorded that its copy
*"drifted 17 days behind a provider change, and misled a session into arguing
from a falsified fact"*. The three above carry that same falsified claim today.
A repeat is not a redundant copy; it is a *falsifiable* copy, and it falsifies
quietly.

## The exception half came back strong

Worth recording plainly, because an audit that only reports defects
misrepresents the estate. Every one of the **11 ignore-file globs** and
**~120 line markers** read carries a stated reason. The three repo-wide
`leakscan` opt-outs (`shed`, `derry-hill`, `stewart-drive`) each cite a named
ADR — verified to exist, not taken on trust — state the inverted-premise ground
(the repo *is* the deliberate home for what the scanner hunts), and bound what
does **not** relax: secretscan stays on, no health data, no financial means.
`faves`' `.leakscanignore` is the model instance: it argues why globs beat ~70
markers for its case, draws the venue-vs-person line explicitly, and instructs
future readers not to widen it. **No unreasoned hatch was found anywhere.**

Rule (b) — *fail noisy, then subtract* — is genuinely built: a live run prints
`suppressed: 36 by allow-marker · 35 file(s) by .leakscanignore`, with a
per-rule breakdown.

Three governance gaps against `GUARDS.md`, none of them an exposure:

- **Two deferments filed as acceptances.** `ec2_builder`'s and `homenetwork`'s
  ignore-globs each name real security debt they intend to clear — which is the
  definition of a deferment, and a deferment must carry an expiry. Neither does,
  so both read as permanent.
- **The parent is not exempt, and is in breach.** atelier's own
  `.atelier-floor.json` `scope` block narrows three checks with **no `why`** —
  `ros`'s equivalent entry has one. The reasons exist, in the ignore-file
  comments, which is the other half of the same rule: a reason a reviewer of the
  config cannot see. Same shape on `ros`'s `flags.leakscan` entry.
- **Eight bare advisories, already in hand.** No reason, no expiry, across six
  repos — but the board already names each *"pre-C1 declaration, migrate it"*
  and **C1b/C2 are claimed and in flight** with Mike's `2026-09-01` horizon set.
  Recorded as covered, not missed, so a later sweep does not re-file them.

## The finding neither question asked for

Measured against the canonical floor region: **eight children carry a block
missing four of the seven irreducible floor concerns** — Concurrency, Session
rhythm, Estate resources, plus an apex bullet predating both the *adaptation*
clause and the *informed confirmation* sentence. All eight pin `atelier@d7e7afc`
(2026-07-12, **818 commits back**), so this is the pin mechanism working exactly
as designed and never being actioned — visible staleness, which is all a pin
promises.

It is also **undeclared narrowing**, and nothing mechanical can see it:
`stampscan` only compares stamped blocks, and only the four newest children
stamp theirs (`create-repo` stamps at scaffold; the older twelve were never
retrofitted). So **12 of 16 copies are invisible to the check built to watch
them** — the known D2-residue bar, seen from the child side. `shed` is the
instructive case: it omits the Estate-resources bullet *correctly*, being the
estate root that cannot point up to itself, and has no way to declare that
legitimate narrowing while unstamped.

## Adoption coverage — clean

Cross-checking every project path the agent has been used in against the child
list: **all 12 worked repos are children with the floor wired.**
`python-metaname` is a third-party clone, never worked in; the rest are not
repos. No exclusion ruling is owed today.

## What Mike ruled mid-audit, and what landed

Two rulings, neither previously written down — which is how the duplication
survived in four repos while every one passed every check:

1. **Adoption is the default.** Every repo he works an agent in is a child
   unless he rules a specific exclusion. This makes the enumerating boards'
   denominator honest: every repo he uses, not every repo already wired.
2. **Add freely; never repeat; never conflict absent a ruled exemption.** The
   third verb is the one the existing bullets could not express — they made an
   unresolved contradiction a defect to surface, with no way to record a
   *ruled* one, so a deliberate exemption reads as drift to the next session.
3. **Work lands in the repo it changes** — a fix is made by a session working
   that repo, never delivered sideways by the session that found it. The lane
   left open: the finder **may queue** the finding and its proposed fix in the
   target repo's roadmap, and stops there.

Landed in the files that already own those subjects rather than as new sections
— `PROPAGATION.md` § *layer-override* gains *Who is a child, and what a child
may hold*; `CONCURRENCY.md` § *Stay in your lane* sharpens its existing
another-repo fence. Minting a second original of either would have been the
defect the first ruling forbids.

## Discipline notes

- A parallel session was provably live (HEAD moved mid-session, C1b/C2 claimed
  `wt: none` — committing straight to `main`), so this work took a worktree and
  landed by fast-forward. Its claimed items were left untouched.
- Every child-repo finding was **queued, never delivered** — the work-locality
  ruling applied to the audit that produced it. No child repo was written to.
- `tools/worktree.py list` misreports the branch (shows `main` for a worktree on
  `doctrine-adoption-ruling-0809`), so `land <feature>` cannot find it. Queued,
  not fixed — out of the given lane.
- Floor green on the pushed SHA, conclusion read rather than assumed (the
  cancelled-run clause landed hours earlier applies directly).
- Self-authored doctrine ⇒ rule-4 `⏳` queued, not spawned.
