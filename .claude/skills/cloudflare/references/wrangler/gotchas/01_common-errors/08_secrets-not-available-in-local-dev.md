### "Secrets not available in local dev"

**Cause:** Secrets set with `wrangler secret put` only work in deployed Workers
**Solution:** For local dev, use `.dev.vars`

