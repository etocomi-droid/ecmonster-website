## Config Format

**wrangler.jsonc recommended** (v3.91.0+) - provides schema validation.

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01",  // Use current date
  "vars": { "API_KEY": "dev-key" },
  "kv_namespaces": [{ "binding": "MY_KV", "id": "abc123" }]
}
```

