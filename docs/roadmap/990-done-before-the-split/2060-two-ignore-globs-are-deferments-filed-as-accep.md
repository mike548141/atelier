- [x] **Two ignore-globs are deferments filed as acceptances.** ✅ **RULED and
      landed 2026-08-09** — Mike took the recommendation below: `2026-09-01`,
      the re-judge reading. Written into all four globs
      (`ec2_builder` `49a8f436`, `homenetwork` `63e070c`), in the comment
      beside each reason, cover unchanged. **What the ruling exposed, and it
      is the more useful half:** the date could not be declared where it
      belongs. `review-by` exists **only** on floor `advisory` declarations —
      `floor.py` states outright that `scope` and `flags` carry none, and a
      path glob has no expiry field at all. So `GUARDS.md` requires every
      deferment to expire, and the mechanism can only express an expiry at
      **check** granularity. A repo deferring at **path** or **line**
      granularity is structurally unable to comply, and the rule reads as
      satisfiable only because nobody had tried. Both repos now carry the date
      as prose beside the reason, with that limit stated in the file rather
      than papered over: nothing will go red when it lapses. See the follow-up
      below.
