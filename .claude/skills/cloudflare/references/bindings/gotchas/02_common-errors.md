## Common Errors

### "env.MY_KV is undefined"

**Cause:** Name mismatch or not configured  
**Solution:** Check wrangler.jsonc (case-sensitive), run `npx wrangler types`, verify `npx wrangler kv namespace list`

### "Property 'MY_KV' does not exist on type 'Env'"

**Cause:** Types not generated  
**Solution:** `npx wrangler types`

### "preview_id is required for --remote"

**Cause:** Missing preview binding  
**Solution:** Add `"preview_id": "dev-id"` or use `npx wrangler dev` (local mode)

### "Secret updated but Worker still uses old value"

**Cause:** Cached in global scope or not redeployed  
**Solution:** Avoid global caching, redeploy after secret change

### "KV get() returns null for existing key"

**Cause:** Eventual consistency (60s), wrong namespace, wrong environment  
**Solution:**
```bash
# Check key exists
npx wrangler kv key get --binding=MY_KV "your-key"

# Verify namespace ID
npx wrangler kv namespace list

# Check environment
npx wrangler deployments list
```

### "D1 database not found"

**Solution:** `npx wrangler d1 list`, verify ID in wrangler.jsonc

### "Service binding returns 'No such service'"

**Cause:** Target Worker not deployed, name mismatch, environment mismatch  
**Solution:**
```bash
# List deployed Workers
npx wrangler deployments list --name=target-worker

# Check service binding config
cat wrangler.jsonc | grep -A2 services

# Deploy target first
cd ../target-worker && npx wrangler deploy
```

### "Rate limit exceeded" on KV writes

**Cause:** >1 write/second per key  
**Solution:** Use different keys, Durable Objects, or Queues

