## Workers Subrequests

**Problem:** Rate limit hit faster than expected in Workers.

**Cause:** Workers subrequests count as separate API calls.

**Solution:** Use bindings instead of REST API in Workers (see ../bindings/).

```typescript
// ❌ WRONG - REST API in Workers (counts against rate limit)
const client = new Cloudflare({ apiToken: env.CLOUDFLARE_API_TOKEN });
const zones = await client.zones.list();

// ✅ CORRECT - Use bindings (no rate limit)
// Access via env.MY_BINDING
```

