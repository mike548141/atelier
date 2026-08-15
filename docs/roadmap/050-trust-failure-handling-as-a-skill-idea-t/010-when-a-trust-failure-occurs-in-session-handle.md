- [ ] **When a trust failure occurs in-session, handle it deterministically —
      with a skill (enforced actions, code), not doctrine (policy the agent may
      or may not apply under the same pressure that caused the failure).**
      Captured verbatim from Mike; not yet designed or decided.

      **The class it targets.** A *trust failure* is the moment the collaboration's
      evidence chain breaks: an all-clear reported past its evidence (the pushed
      floor was red for ~19 h while "9/9, exit 0" was being reported,
      2026-07-26) · a capability claim made unlooked ("no existing tool reports
      this" the day after the tool shipped, 2026-07-26) · a deletion asserted as
      safe with the diff never taken (the 185-line "duplicates" removal,
      2026-07-25). `00-APEX.md` names the stakes — a false "it works" poisons
      trust in every other report — but **nothing prescribes what happens
      next**: today the recovery (own it, re-verify, record it, correct the
      records) is doctrine the failing agent applies to itself, which is exactly
      the fail-open shape ADR 0008 exists to end.

      **Why a skill.** Same argument as the policy-as-code programme, one layer
      up: doctrine asks the agent to remember under pressure; a skill makes the
      recovery a *procedure* — invoked at the moment of failure, steps enforced
      in order, outputs (incident note, re-verification, record corrections,
      SESSIONS entry) produced as artefacts rather than promised. It also makes
      failures **instrumentable**: a consistent record shape means recurrence
      can be counted, which feeds the anti-slop invariant registry (repeat
      offences → always-on checks).

      **Open questions for the design pass (not answered here):**
      - Trigger: self-invoked on realising the failure? Mike-invoked? Or wired
        to a detector (e.g. CI catching a claim the hook would have failed)?
      - Scope: atelier-only, or estate-wide via the child-repo skill channel?
      - What's *enforced* vs *recorded* — can a skill actually gate anything, or
        is its value the deterministic checklist + artefact trail?
      - Relationship to `EVIDENCE.md` (the ladder the failure skipped) and
        `RECORD.md`'s all-clear rule — the skill would operationalise both, not
        duplicate them.
