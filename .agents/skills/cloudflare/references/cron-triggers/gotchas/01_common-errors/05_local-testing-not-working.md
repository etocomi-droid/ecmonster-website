### "Local Testing Not Working"

**Problem:** `/__scheduled` endpoint returns 404 or doesn't trigger handler  
**Cause:** Missing `scheduled()` export, wrangler not running, or incorrect endpoint format  
**Solution:**

1. Verify `scheduled()` is exported:
```typescript
export default {
  async scheduled(controller, env, ctx) {
    console.log("Cron triggered");
  },
};
```

2. Start dev server:
```bash
npx wrangler dev
```

3. Use correct endpoint format (URL-encode spaces as `+`):
```bash
# Correct
curl "http://localhost:8787/__scheduled?cron=*/5+*+*+*+*"

# Wrong (will fail)
curl "http://localhost:8787/__scheduled?cron=*/5 * * * *"
```

4. Update Wrangler if outdated:
```bash
npm install -g wrangler@latest
```

