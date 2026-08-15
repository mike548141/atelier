- [ ] **`PRINCIPLES.md` §9 has no guard, and the only safe candidate is scoped
      to structured data.** §9 says data carries the time dimension its domain
      implies; nothing checks it, in any repo. `datescan` is not that guard and
      was never trying to be — it enforces `EVIDENCE.md` §7 over written prose,
      and a record with no dates at all passes it clean. §9's own closing
      paragraph already separates the two questions: this principle says the
      dimension must *exist*, `CONVENTIONS.md` says how a stamp is *written*
      once it does.
      **Why structured data only.** The case-file's second clean pattern is that
      guards over machine-shaped input — link resolution, licence headers,
      signatures, tracked-path globs, floor config — barely drift, while guards
      over prose drift constantly. A schema, a JSON document or a YAML document
      carries its own licensing context: the fields are there or they are not.
      A prose guard for the same concern would be the definite-description
      rule's failure repeated, and that one was built, measured at a 90.6%
      firing rate over 6,764 replies, and deleted the same day on its own
      numbers.
      **What it would check, at minimum:** two timestamps rather than one —
      world time and record time — which is the accepted floor in every
      temporal-modelling tradition, and the pair §9 already names as two clocks
      kept apart. Beyond that, acquisition method where a stored value is a
      conclusion rather than an observation.
      **Blocked on:** the confidence decision above, which changes the field set.
      **Owned by:** the repo that owns the data, per §9's scope clause — atelier
      builds the check and the propagation pointer, never the retrofit.
