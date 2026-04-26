## Monolithic Full-Stack Worker

**Problem:** Frontend and backend logic in single Worker with Smart Placement enabled.

**Cause:** Smart Placement optimizes for backend latency but increases user-facing response time.

**Solution:** Split into two Workers:
```jsonc
// frontend/wrangler.jsonc
{
  "name": "frontend",
  "placement": { "mode": "off" },  // Explicit: stay at edge
  "services": [{ "binding": "BACKEND", "service": "backend-api" }]
}

// backend/wrangler.jsonc
{
  "name": "backend-api",
  "placement": { "mode": "smart" },
  "d1_databases": [{ "binding": "DB", "database_id": "xxx" }]
}
```

