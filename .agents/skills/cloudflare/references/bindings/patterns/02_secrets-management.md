## Secrets Management

```bash
# Set secret
npx wrangler secret put API_KEY
cat api-key.txt | npx wrangler secret put API_KEY
npx wrangler secret put API_KEY --env staging
```

```typescript
// Use secret
const response = await fetch('https://api.example.com', {
  headers: { 'Authorization': `Bearer ${env.API_KEY}` }
});
```

**Never commit secrets:**
```jsonc
// ❌ NEVER
{ "vars": { "API_KEY": "sk_live_abc123" } }
```

