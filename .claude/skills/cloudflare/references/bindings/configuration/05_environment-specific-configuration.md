## Environment-Specific Configuration

```jsonc
{
  "name": "my-worker",
  "vars": { "ENV": "production" },
  "kv_namespaces": [{ "binding": "CACHE", "id": "prod-kv-id" }],
  
  "env": {
    "staging": {
      "vars": { "ENV": "staging" },
      "kv_namespaces": [{ "binding": "CACHE", "id": "staging-kv-id" }]
    }
  }
}
```

**Deploy:**
```bash
npx wrangler deploy              # Production
npx wrangler deploy --env staging
```

