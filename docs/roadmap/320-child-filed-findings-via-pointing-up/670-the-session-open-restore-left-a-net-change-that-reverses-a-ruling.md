- [x] **SUPERSEDED 2026-11-03** 🔎 **Hand-up: the session-open prompt's "restore" left a net change
      that reverses the 2026-09-19 tier ruling** `[S][doctrine]`. Handed up by
      a private child on 2026-10-17 at its drift check, under `PROPAGATION.md`
      § *Pointing up*. **Evidence, measured on `origin/main`:**
      `docs/method/session-open/session-open-prompt.md` is byte-identical at
      `09a61b4` and `170c3b9`; `4d80321` ("the missed intermediate version,
      inserted late") changes it; `6a0ac93` ("restore current content after
      inserting the missed historical commit") does **not** restore it — the
      net diff `170c3b9..6a0ac93` is 26 lines. Two hunks:
      1. *"Say which model you're on in your first report, then get on with
         it — don't ask me which tier to use, and don't stop because a more
         capable one exists. Stop only if the work outruns you"* became
         *"Confirm you're on the capable tier before claiming anything — if
         you're not, stop and say so instead of proceeding."* That is the
         wording `ECONOMICS.md` § *Know the marginal cost* retired on
         2026-09-19 (*"states and proceeds"*; the question had reached the
         principal from over a hundred sessions). The prompt now instructs
         the opposite of the doctrine it tells the session to follow.
      2. The close list dropped *"roadmap items closed (harvested, on a
         monolithic board)"* for *"roadmap harvested"* — smaller, and maybe
         intended; listed so the restore's scope is checked whole.
      Whether the historical insert was meant to carry forward, or the
      restore missed, is atelier's to judge; the child only reports that the
      commit message and the tree disagree. Reproduce with
      `git diff 170c3b9 6a0ac93 -- docs/method/session-open/session-open-prompt.md`.
      ✅ **No work owed, checked 2026-11-03 by queue run 4c65083c.** Both
      hunks are back at HEAD: the prompt's line 20 reads "don't ask me which
      tier to use", and line 128 reads "roadmap items closed (harvested, on a
      monolithic board)". `998c35f` (2026-10-18) reconciled them, and its
      commit body names this exact reversal (`6a0ac93` had put back the
      pre-2026-09-20 tier line and the pre-2026-10-03 harvest wording).
