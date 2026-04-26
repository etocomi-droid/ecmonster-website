## Local Dev

```bash
# Basic
npx wrangler pages dev ./dist

# With bindings
npx wrangler pages dev ./dist --kv KV --d1 DB=local-db-id

# Remote bindings (production data)
npx wrangler pages dev ./dist --remote

# Persistence
npx wrangler pages dev ./dist --persist-to=./.wrangler/state/v3

# Proxy mode (SSR frameworks)
npx wrangler pages dev -- npm run dev
```

