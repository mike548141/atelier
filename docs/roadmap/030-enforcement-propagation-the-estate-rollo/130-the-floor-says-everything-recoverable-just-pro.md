- [ ] 🔎 **The inlined floor says "everything recoverable — just proceed",
      and `RECORD.md` rules that recoverability is the wrong test for a record
      store. Nothing reconciles them.** Raised as a question by a child
      session, **verified here 2026-08-16** as a real contradiction rather
      than a misreading.
      **The two texts.** The floor region in `PROPAGATION.md` closes its
      always-confirm list with *"Everything recoverable — commit/push/PR
      included — just proceed."* The list it closes covers *"anything truly
      destructive or irreversible"*. Meanwhile `RECORD.md` rules that **bulk
      deletion from a record store is show-first, regardless of who created
      the mess**, on the explicit ground that *"Recoverability of bytes is the
      wrong test for a record store"* — and `AUTONOMY.md` restates it as
      floor-class.
      **Why the floor's own wording does not already cover it.** The carve-out
      cannot ride on *"truly destructive or irreversible"*, because the whole
      point of the `RECORD.md` ruling is that the act **is** byte-recoverable
      and is show-first anyway. So a child reading only the inlined region
      classifies a record-store bulk delete as recoverable, and proceeds. The
      permissive half propagates and the carve-out does not.
      **Which makes this a propagation defect, not just a wording one.** The
      region exists precisely so the floor binds a child that never reads
      atelier. A rule that only exists outside the region is a rule those
      children do not have.
      **Cheapest honest fix, offered not chosen:** name the record-store case
      in the region's confirm list rather than leaving it to the recoverable
      clause — one clause, at the point of use, in the text that actually
      travels. The alternative, pointing up to `RECORD.md`, reintroduces the
      dependency the region was built to remove.
