## Quick Start

```jsonc
// wrangler.jsonc
{
  "placement": {
    "mode": "smart"  // or "off" to explicitly disable
  }
}
```

Deploy and wait 15 minutes for analysis. Check status via API or dashboard metrics.

**To disable:** Set `"mode": "off"` or remove `placement` field entirely (both equivalent).

