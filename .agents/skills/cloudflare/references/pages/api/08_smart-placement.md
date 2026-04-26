## Smart Placement

Automatically optimizes function execution location based on traffic patterns.

**Configuration** (in wrangler.jsonc):
```jsonc
{
  "placement": {
    "mode": "smart"  // Enables optimization (default: off)
  }
}
```

**How it works**: Analyzes traffic patterns over time and places functions closer to users or data sources (e.g., D1 databases). Requires no code changes.

**Trade-offs**: Initial requests may see slightly higher latency during learning period (hours-days). Performance improves as system optimizes.

**When to use**: Global apps with centralized databases or geographically concentrated traffic sources.

