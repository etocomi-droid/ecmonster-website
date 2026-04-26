## Plan-Based Availability

Not all datasets are available on all plans. Higher plans get more datasets, longer retention (`notOlderThan`), wider time ranges (`maxDuration`), more fields, and larger page sizes.

### "node is not available" / "node is disabled"

**Cause:** Dataset not on your plan, or product not enabled.

**Solution:** Check `settings { <nodeName> { enabled } }`. Some datasets require specific subscriptions (e.g., Network Analytics requires Magic Transit/Spectrum).

