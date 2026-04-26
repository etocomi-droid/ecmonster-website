## Pages/Assets + Smart Placement Performance Degradation

**Problem:** Static assets load 2-5x slower when Smart Placement enabled with `run_worker_first = true`.

**Cause:** Smart Placement routes ALL requests (including static assets like HTML, CSS, JS, images) to remote locations. Static content should ALWAYS be served from edge closest to user.

**Solution:** Split into separate Workers OR disable Smart Placement:
```jsonc
// ❌ BAD - Assets routed away from user
{
  "name": "pages-app",
  "placement": { "mode": "smart" },
  "assets": { "run_worker_first": true }
}

// ✅ GOOD - Assets at edge, API optimized
// frontend/wrangler.jsonc
{
  "name": "frontend",
  "assets": { "run_worker_first": true }
  // No placement field - stays at edge
}

// backend/wrangler.jsonc
{
  "name": "backend-api",
  "placement": { "mode": "smart" }
}
```

This is one of the most common and impactful Smart Placement misconfigurations.

