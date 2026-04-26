## wrangler.jsonc

```jsonc
{
  "compatibility_date": "2025-01-01", // Use latest for new projects
  "compatibility_flags": ["nodejs_compat"],
  "hyperdrive": [
    {
      "binding": "HYPERDRIVE",
      "id": "<HYPERDRIVE_ID>",
      "localConnectionString": "postgres://user:pass@localhost:5432/dev"
    }
  ]
}
```

**Generate TypeScript types:** Run `npx wrangler types` to auto-generate `worker-configuration.d.ts` from your wrangler.jsonc.

**Multiple configs:**
```jsonc
{
  "hyperdrive": [
    {"binding": "HYPERDRIVE_CACHED", "id": "<ID1>"},
    {"binding": "HYPERDRIVE_NO_CACHE", "id": "<ID2>"}
  ]
}
```

