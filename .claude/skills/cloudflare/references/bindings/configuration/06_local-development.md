## Local Development

```jsonc
{
  "kv_namespaces": [{
    "binding": "MY_KV",
    "id": "prod-id",
    "preview_id": "dev-id"  // Used in wrangler dev
  }]
}
```

**Or use remote:**
```bash
npx wrangler dev --remote  # Uses production bindings
```

