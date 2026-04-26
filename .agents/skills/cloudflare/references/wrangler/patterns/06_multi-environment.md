## Multi-Environment

```bash
wrangler deploy --env staging
wrangler deploy --env production
```

```jsonc
{ "env": { "staging": { "vars": { "ENV": "staging" } } } }
```

