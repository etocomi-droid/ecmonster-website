## Debugging Tips

```bash
# Check configuration
npx wrangler deploy --dry-run       # Validate config without deploying
npx wrangler kv namespace list      # List KV namespaces
npx wrangler secret list            # List secrets (not values)
npx wrangler deployments list       # Recent deployments

# Inspect bindings
npx wrangler kv key list --binding=MY_KV
npx wrangler kv key get --binding=MY_KV "key-name"
npx wrangler r2 object get my-bucket/file.txt
npx wrangler d1 execute my-db --command="SELECT * FROM sqlite_master"

# Test locally
npx wrangler dev                  # Local mode
npx wrangler dev --remote         # Production bindings
npx wrangler dev --persist        # Persist data across restarts

# Verify types
npx wrangler types
cat .wrangler/types/runtime.d.ts | grep "interface Env"

# Debug specific binding issues
npx wrangler tail                 # Stream logs in real-time
npx wrangler tail --format=pretty # Formatted logs
```

