- [x] **LANDED 2026-10-18** (wt: atelier-qr-180-060)
      **The opening prompt's template history, mined from every transcript.**
      Mike, 2026-10-18, mid-run: *"Since I started first using claude code in
      approx June 2026 I have had various different versions of this opening
      prompt … I would like that to be recorded in my git history so I can
      see how my opening prompt changes over time. I think it should be in
      atelier (public) so others can learn from it too but it must, 1. Not
      include any private or personal information that may have been in the
      prompt 2. Not include the specific work I asked of that session.
      Essentially I want the template stored. All the parts of the session
      opening prompt(s) that were re-used across more than one session
      transcript. By definition if it were only used in one session then its
      not part of the "template"."*
      What exists: V1–V9 (2026-07-13 to 2026-09-16) were reconstructed by an
      earlier session and folded in by subtree merge (`0a949b4`), but by
      version, not by the reused-across-sessions test, and not audited for
      the two exclusions. Owed: mine every opening prompt in the live store
      and the transcript archive, keep only segments that recur in at least
      two sessions, drop private detail and session-specific work, and land
      the versions in date order as commits to one file, so `git log -p`
      shows the evolution.

  **Closed 2026-10-18.** `docs/method/session-open/template-history.md` holds
  50 versions as 50 commits, oldest first. Each commit's author date is the
  version's first use, and its message gives how many sessions used it and
  how often it was re-pasted later. Read it with `git log --follow -p` on
  that path. Method, exclusions and limits are in the directory's
  `README.md`. Sources: 946 sessions (live store and archive), 934 opening
  prompts, a family of 228 sessions plus four precursor openers
  (2026-07-08 to 2026-07-10). A Sonnet worker mined 86 raw versions. The
  orchestrator read all nine flagged units and dropped them: each recurred
  but was one run's themed work, and five also named private repos, tools
  or devices. It replaced one private repo name with `[estate-root repo]`,
  kept the six borderline units (generic selection wording, no named work),
  and collapsed re-pastes to 50 versions. Leak, secret and date scanners are
  clean on every version. The one spelling finding (`catalog`) is the
  principal's own, exempted under his 2026-07-23 ruling. **Not
  recoverable:** anything before 2026-07-08. The store holds one June
  session, and its opening is not this prompt. A privacy cold pass is queued
  at `160/940`, because private transcripts were mined into a public file.
