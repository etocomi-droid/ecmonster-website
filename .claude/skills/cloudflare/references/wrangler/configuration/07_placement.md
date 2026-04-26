## Placement

Control where Workers run geographically.

```jsonc
{
  "placement": {
    "mode": "smart"  // or "off"
  }
}
```

- `"smart"`: Run Worker near data sources (D1, Durable Objects) to reduce latency
- `"off"`: Default distribution (run everywhere)

