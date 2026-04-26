## Smart Placement Integration

For Workers making **multiple queries** per request, enable Smart Placement to execute near your database:

```jsonc
{
  "compatibility_date": "2025-01-01",
  "compatibility_flags": ["nodejs_compat"],
  "placement": {
    "mode": "smart"
  },
  "hyperdrive": [
    {
      "binding": "HYPERDRIVE",
      "id": "<HYPERDRIVE_ID>"
    }
  ]
}
```

**Benefits:** Multi-query Workers run closer to DB, reducing round-trip latency. See [patterns.md](./patterns.md) for examples.

