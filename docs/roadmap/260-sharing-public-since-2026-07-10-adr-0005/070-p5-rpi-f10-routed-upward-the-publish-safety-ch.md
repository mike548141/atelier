- [x] **P5 — `rpi` F10, routed upward: the publish-safety checklist gates repo
      *content*, never platform *settings*.** ADR 0009's six gates cover what a
      repo contains; nothing covers what GitHub exposes — wiki (a second git
      repo the floor never sees), actions policy, fork-PR approval,
      vulnerability reporting, rulesets. Every settings-level finding in the
      `rpi` pass walked through that gap. Owed **before `ros`/`faves` flip**.
  - [x] ✅ **Landed 2026-11-09** (queue run d0ca5d24): `docs/method/AUTONOMY.md`
        carries the settings gate in the pre-flip list, as two bullets (what the
        gate reads, and flip and harden as one sitting, the addition from `090`).
        `docs/build/REPO-STANDARD.md` points at it from the PVR sentence. The
        endpoints were read live against atelier on 2026-11-09. A `gh api` read
        that automates it is `260/130`.
