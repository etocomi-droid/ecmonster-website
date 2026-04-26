### "Placement not reducing latency"

**Cause:** Misunderstanding of Smart Placement
**Solution:** Smart Placement only helps when Worker accesses D1 or Durable Objects. It doesn't affect KV, R2, or external API latency.
```jsonc
{ "placement": { "mode": "smart" } }  // Only beneficial with D1/DOs
```

