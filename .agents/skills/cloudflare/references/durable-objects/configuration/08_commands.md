## Commands

```bash
# Development
npx wrangler dev                    # Local dev
npx wrangler dev --remote           # Test against production DOs

# Deployment
npx wrangler deploy                 # Deploy + auto-apply migrations
npx wrangler deploy --dry-run       # Validate migrations without deploying
npx wrangler deploy --env production

# Management
npx wrangler durable-objects list                      # List namespaces
npx wrangler durable-objects info <namespace> <id>     # Inspect specific DO
npx wrangler durable-objects delete <namespace> <id>   # Delete DO (destroys data)
```

