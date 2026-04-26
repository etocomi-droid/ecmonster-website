## Multi-Environment

```bash
# wrangler.dev.jsonc
{ "name": "worker-dev", "vars": { "ENV": "dev" } }

# wrangler.prod.jsonc
{ "name": "worker-prod", "vars": { "ENV": "prod" } }

npx wrangler deploy --config wrangler.dev.jsonc
npx wrangler deploy --config wrangler.prod.jsonc
```

