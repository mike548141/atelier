# 2026-07-10 · first keeper repo (numen) + fleet pin bumps + REVIEW re-run rule (Opus)

The post-sweep execution session: three owed items closed, one small doctrine
touch. Order was pins-first (quick), then the keeper scaffold (the owed outward
step), then the atelier record.

## Pin bumps — the fleet carried the reworded block down

Both children were deliberately behind HEAD, holding the unquoted drift-check
line. Read each delta first, then bumped:

- **ros** `f72031c → bbdeece` (9 behind). The one change reaching the block was
  the C2 reword — the drift-check path is now quoted (`git -C "../atelier" …`)
  so it survives a spacey atelier path run verbatim. The delta's method/ edits
  (ACCESS/EVIDENCE/RECORD/SECRETS) are docs ros points *up* to, not copies — no
  ros doctrine change. leakscan hook fired clean on commit.
- **faves** `dde4170 → bbdeece` (30 behind — last bumped before the whole
  method-review era). Two changes reached its block: the C2 reword **and** the
  **P1 trust-surface floor clause** (the "stop and confirm" floor now covers
  *adding a new trust surface* — deploy keys, webhooks, OAuth/app grants) that
  faves had lagged since before the method review. This was the exact pin bump
  the ROADMAP flagged faves to adopt the P1 wording at.

Fleet now reads all-current (`tools/pins.py`).

## numen — the first keeper repo, and the owed `gh repo create --push` proof

Mike's call on which repo: the home-automation-devices project, framed by his
vision — a home that "exists invisibly and silently, making a safe, secure,
healthy environment for its inhabitants without them having to enable, support,
manage, fix, and operate it. Like a great butler + house staff." Named
**numen** (the unseen presiding presence that watches over a place) for that
invisibility; owner `mike548141`, PRIVATE.

Driven through the rewired `create-repo`, live, end to end:

- **Sized honest: pre-code.** No firmware/orchestration/board designs exist, and
  the stack is a *deliberate open decision* (ARCHITECTURE names the candidate
  `firmware/`/`orchestration/`/`hardware/` shape; ROADMAP makes "decide the
  first slice + write ADR-0001" the next move). The scaffold does not imply a
  system that isn't built.
- **The honest-CI call.** Nothing is buildable and the content scans can't run
  in child CI yet (deferred distribution item), so there is no honest automated
  gate — recorded as a **stated no-gate**, not a silent absence
  (`.github/workflows/README.md` + ARCHITECTURE Testing). The pre-commit scan
  hook is the only automated gate, and it was **proven live**: blocked a planted
  `AKIA…` key (both scanners, exit 1), then passed the real scaffold commit
  clean. Sibling-relative `../atelier/tools` config resolved correctly (matched
  to CONTRIBUTING, proven not assumed).
- **Stamp proven mechanically** (not just written): no unfilled placeholders
  anywhere; the block's own drift check runs empty verbatim.
- **Privacy framing like ros:** estate device/access topology is the repo's
  legitimate subject and lives here (private); health/family/finance never do.
- **Outward step:** `gh repo create numen --private --source=. --remote=origin
  --push` — exit 0; verified `isPrivate: true` / `visibility: PRIVATE`;
  `settings.local.json` correctly not committed (gitignored). This is the one
  part of create-repo never driven before now. https://github.com/mike548141/numen

The mechanism paid out: born with the doctrine block, scans wired + proven,
docs honest about being pre-code — the costume-vs-doctrine gap the rewire
existed to close, verified on a real repo.

## Small atelier touch — REVIEW.md "re-run the proofs" rule

New subsection **"Re-run every 'live-proven' claim in scope"**: a recorded proof
is a claim that can be stale by the commit that records it, so a review re-runs
the work's asserted proofs rather than reading them, and treats a proof that no
longer reproduces as a finding. Grounded twice — B1 (a scan's "live-proven
clean" false at its recording commit) and C2 (a stamped, recorded proof that
broke run-verbatim). Lens 2 applied to the record itself; feeds the close-rule.
The batch review's owed recommendation, now landed. Review-owed like any
doctrine edit.

## Not this session (correctly)

The **ros consolidated estate access map** (B14) is a ros session's job —
sensitive content, ros context, not an atelier session. Left for its own run.
