- [ ] 🔎 **The floor block's always-confirm stop list differs from
      `AUTONOMY.md` § *Always confirm*.** Found 2026-11-16 UTC by the `020/220`
      census, slice 2. Per the census, the floor's list adds bulk deletion and
      drops deploy-on-push and merging other people's work, so a child reading
      only its floor copy (the case the floor exists for) holds a different
      stop list from the canonical one. Either list may be the right one; the
      defect is that they differ silently. **Owed:** reconcile them, with the
      principal where a stop is added or dropped (the floor is his to
      narrow or widen), and consider a test that pins one list to the
      other the way `test_templates` pins the floor's copies. Not fixed in
      passing; a floor bundle was in flight in the same run.
