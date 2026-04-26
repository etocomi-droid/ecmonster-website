## SQLite-backed (Recommended)

**wrangler.jsonc:**
```jsonc
{
  "migrations": [
    {
      "tag": "v1",
      "new_sqlite_classes": ["Counter", "Session", "RateLimiter"]
    }
  ]
}
```

**Migration lifecycle:** Migrations run once per deployment. Existing DO instances get new storage backend on next invocation. Renaming/removing classes requires `renamed_classes` or `deleted_classes` entries.

