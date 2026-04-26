## Local Dev & Deployment

```bash
# Dev server
npx wrangler pages dev ./dist

# With bindings
npx wrangler pages dev ./dist --kv=KV --d1=DB=db-id --r2=BUCKET

# Durable Objects (2 terminals)
cd do-worker && npx wrangler dev
cd pages-project && npx wrangler pages dev ./dist --do COUNTER=Counter@do-worker

# Deploy
npx wrangler pages deploy ./dist
npx wrangler pages deploy ./dist --branch preview

# Download config
npx wrangler pages download config my-project
```

**See also:** [api.md](./api.md) for binding usage examples
