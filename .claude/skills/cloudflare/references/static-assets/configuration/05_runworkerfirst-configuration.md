### run_worker_first Configuration

Controls which requests invoke Worker before checking assets.

**Boolean syntax:**

```jsonc
{
  "assets": {
    "run_worker_first": true  // ALL requests invoke Worker
  }
}
```

**Array syntax (recommended):**

```jsonc
{
  "assets": {
    "run_worker_first": [
      "/api/*",           // Positive pattern: match API routes
      "/admin/*",         // Match admin routes
      "!/admin/assets/*"  // Negative pattern: exclude admin assets
    ]
  }
}
```

**Pattern rules:**

- Glob patterns: `*` (any chars), `**` (any path segments)
- Negative patterns: Prefix with `!` to exclude
- Precedence: Negative patterns override positive patterns
- Default: `false` (assets served directly)

**Decision guidance:**

- Use `true` for API-first apps (few static assets)
- Use array patterns for hybrid apps (APIs + static assets)
- Use `false` for static-first sites (minimal dynamic routes)

