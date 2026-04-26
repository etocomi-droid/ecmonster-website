## wrangler.jsonc

```jsonc
{
  "name": "turn-credentials-api",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01",
  "vars": {
    "TURN_KEY_ID": "your-turn-key-id"  // Non-sensitive, can be in vars
  },
  "env": {
    "production": {
      "kv_namespaces": [
        {
          "binding": "CREDENTIALS_CACHE",
          "id": "your-kv-namespace-id"
        }
      ]
    }
  }
}
```

**Store secrets separately**:
```bash
wrangler secret put TURN_KEY_SECRET
```

