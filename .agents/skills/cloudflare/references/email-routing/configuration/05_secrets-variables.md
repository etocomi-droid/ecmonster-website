## Secrets & Variables

```bash
# Secrets (encrypted)
npx wrangler secret put API_KEY

# Variables (plain)
# wrangler.jsonc
{ "vars": { "THRESHOLD": "5.0" } }
```

```typescript
interface Env {
  API_KEY: string;
  THRESHOLD: string;
}
```

