- [ ] 🔎 **ADR 0008's clause is now closer to true and still not true.** Of its
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
