- [x] 🔎 **ADR 0008's clause is now closer to true and still not true.** Of its
      three named legs, one is now in force (branch protection, via the ruleset),
      one is in force but **bypassable by the admin role** — the bypass Mike ruled
      for, so the control is a guard against accident and third-party push, never
      against compromise of his own token — and one remains **post-hoc** (registry
      changes land directly on `main` under the standing grant; review follows
      landing). The clause still reads as three flat controls. Re-wording it is a
      doctrine edit and earns its own `⏳` at landing; it was deliberately not
      done in the same commit as the platform change, so the record never claims
      an ADR revision that had no review behind it.
      ⚠️ **AP1 therefore stays OPEN.** The exposure is narrowed, not closed, and
      calling it closed would be exactly the rounding the apex forbids.

      🎯 **2026-10-16: blocked on Mike's ruling, with a draft ready.** A
      queue run claimed this, drafted the re-wording, then reverted it
      unlanded. The fix is the same edit as review finding AR1 (MAJOR) in
      [`../../reviews/2026-09-25-0715-ap-rulings-applied-cold.md`](../../reviews/2026-09-25-0715-ap-rulings-applied-cold.md),
      and that cycle's findings are Mike's to decide (`REVIEW.md` rule 3).
      AR8 there also finds that his 2026-08-23 ruling rested on a false
      premise: that no ruleset existed. So the first step is to re-brief
      him, not to apply a fix. The live read on 2026-10-16 matches the
      verdict's: ruleset `20603641` is active, with `deletion`,
      `non_fast_forward` and `required_signatures`, and its one bypass
      actor is the admin role with `bypass_mode: always`. The draft below
      was written against that read, for him to accept, change or drop.
      It is an appended amendment, so the earlier text stays as history:

      >
      > ## Amended 2026-10-16 — the boundary as it now stands: three legs, three strengths (`140/020`)
      >
      > **The 2026-08-23 amendment was already out of date when it was written.**
      > It says `main` carries "no branch protection and no ruleset". A live read on
      > 2026-10-16 shows ruleset `20603641`, `enforcement: active`, on the default
      > branch. Its `created_at` is 2026-08-09 09:58 UTC, two weeks before that
      > amendment. So the amendment's "re-affirmed at this amendment" read did not
      > see a control that existed. It is left above as written, because the record
      > of what was believed is part of the history. This section supersedes it.
      >
      > **Read live on 2026-10-16** (`repos/mike548141/atelier/rulesets/20603641`
      > and `rules/branches/main`), the clause's three legs stand at three different
      > strengths. None of them is the flat control the Consequences clause names:
      >
      > - **Branch protection — in force.** The ruleset's `deletion` and
      >   `non_fast_forward` rules stop `main` being deleted or rewritten. Neither
      >   blocks an ordinary signed fast-forward push, so the direct-to-`main`
      >   working the claim mechanics rely on is untouched. Mike ruled this shape
      >   on 2026-08-09: a ruleset with owner bypass, plus a machine check.
      > - **Signed commits — in force, but bypassable by the admin role.**
      >   `required_signatures` is active. The ruleset's one bypass actor is the
      >   repository admin role, with `bypass_mode: always`. That bypass is the one
      >   Mike ruled for. So the platform refuses an unsigned push from anyone
      >   *except* the owner's own account. This guards against accident and against
      >   a third party's push. It does **not** guard against a compromise of the
      >   owner's own token, which can bypass every rule in the set. `signscan`
      >   stays warn-first on both of the floor's planes.
      > - **Review on the registry — post-hoc.** Registry changes land directly on
      >   `main` under the standing autonomy grant. Review follows landing, through
      >   `REVIEW.md` rule 4's queued cold pass, and never gates the push.
      >
      > **The machine check is built.** `floorfleet` reads `rules/branches/main`
      > whenever a plane already talks to GitHub. It prints a boundary line under
      > the parent row: red when `deletion` or `non_fast_forward` is missing,
      > unknown (never a pass) when the API cannot be read, and green otherwise.
      > `--check` fails on red or unknown (`115/180`, built 2026-09-18 under
      > `140/010`). `required_signatures` is shown there but is informational.
      >
      > **What this does not close.** The supply-chain exposure the clause names
      > is narrowed, not removed: anyone holding the owner's credentials can still
      > put arbitrary code on `main`, and every child's CI would run it at its next
      > push. So AP1 stays open. The remaining exposure is the owner account itself,
      > whose controls are its 2FA, its single-writer status, and public
      > visibility, under which every push is published and can be inspected.

      ✅ **Landed 2026-10-16, on Mike's answer at the close of the run.** He
      was re-briefed in the device on AR1 and AR8: the false "no ruleset"
      premise behind his 2026-08-23 ruling, the live state, and the draft.
      He was offered three options: land the draft; land it and drop the
      admin bypass; or hold it for a ruling round. He picked **"Land draft
      + drop bypass"**. That is his *answer* to the question, recorded as
      such. Done:
      - The ruleset's `bypass_actors` was set to `[]` through the API. A
        read-back confirms it, and 30 of the 30 latest commits on `main`
        were verified first.
      - The amendment was appended to ADR 0008, revised from the draft above
        to state the post-change strength. Signing is now in force for every
        account. The owner can still edit the ruleset itself, so AP1 stays
        open.
      - Review queued at `160/820`. The draft quoted above is superseded by
        the landed text.
