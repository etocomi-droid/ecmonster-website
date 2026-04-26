## Cloudflare Pages/Assets Warning

**CRITICAL PERFORMANCE ISSUE:** Enabling Smart Placement with `assets.run_worker_first = true` in Pages projects **severely degrades asset serving performance**. This is one of the most common misconfigurations.

**Why this is bad:**
- Smart Placement routes ALL requests (including static assets) away from edge to remote locations
- Static assets (HTML, CSS, JS, images) should ALWAYS be served from edge closest to user
- Result: 2-5x slower asset loading times, poor user experience

**Problem:** Smart Placement routes asset requests away from edge, but static assets should always be served from edge closest to user.

**Solutions (in order of preference):**
1. **Recommended:** Split into separate Workers (frontend at edge + backend with Smart Placement)
2. Set `"mode": "off"` to explicitly disable Smart Placement for Pages/Assets Workers
3. Use `assets.run_worker_first = false` (serves assets first, bypasses Worker for static content)

```jsonc
// ❌ BAD - Degrades asset performance by 2-5x
{
  "name": "pages-app",
  "placement": { "mode": "smart" },
  "assets": { "run_worker_first": true }
}

// ✅ GOOD - Frontend at edge, backend optimized
// frontend-worker/wrangler.jsonc
{
  "name": "frontend",
  "assets": { "run_worker_first": true }
  // No placement - runs at edge
}

// backend-worker/wrangler.jsonc
{
  "name": "backend-api",
  "placement": { "mode": "smart" },
  "d1_databases": [{ "binding": "DB", "database_id": "xxx" }]
}
```

**Key takeaway:** Never enable Smart Placement on Workers that serve static assets with `run_worker_first = true`.

