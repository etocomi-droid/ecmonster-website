## Routes & Triggers

```jsonc
{
  "routes": [
    { "pattern": "example.com/*", "zone_name": "example.com" }
  ],
  "triggers": {
    "crons": ["0 */6 * * *"]  // Every 6 hours
  }
}
```

