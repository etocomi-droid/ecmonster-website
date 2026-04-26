## Combining Multiple Workers

For complex schedules, use multiple workers:

```jsonc
// worker-frequent.jsonc
{
  "name": "data-sync-frequent",
  "triggers": { "crons": ["*/5 * * * *"] }
}

// worker-daily.jsonc
{
  "name": "reports-daily",
  "triggers": { "crons": ["0 2 * * *"] },
  "placement": { "mode": "smart" }
}

// worker-weekly.jsonc
{
  "name": "cleanup-weekly",
  "triggers": { "crons": ["0 3 * * SUN"] }
}
```

**Benefits:**
- Separate CPU limits per worker
- Independent error isolation
- Different Green Compute policies
- Easier to maintain and debug

