## Common Errors

### "Asset not found"

**Cause:** Asset not in assets directory, wrong path, or assets not deployed  
**Solution:** Verify asset exists, check path case-sensitivity, redeploy if needed

### "Worker not invoked for asset"

**Cause:** Asset served directly, `run_worker_first` not configured  
**Solution:** Configure `run_worker_first` patterns to include asset routes (see configuration.md:66-106)

### "429 Too Many Requests on free tier"

**Cause:** `run_worker_first` patterns invoke Worker for many requests, hitting free tier limits (100k req/day)  
**Solution:** Use more selective patterns with negative exclusions, or upgrade to paid plan

### "Smart Placement increases latency"

**Cause:** `run_worker_first=true` + Smart Placement routes all requests through single smart-placed location  
**Solution:** Use selective patterns (array syntax) or disable Smart Placement for asset-heavy apps

### "CF-Cache-Status header unreliable"

**Cause:** Header is probabilistically added for privacy reasons  
**Solution:** Don't rely on `CF-Cache-Status` for critical routing logic. Use other signals (ETag, age).

### "JWT expired during deployment"

**Cause:** Large asset deployments exceed JWT token lifetime  
**Solution:** Update to Wrangler 4.34.0+ (automatic token refresh), or reduce asset count

### "Cannot use 'assets' with 'site'"

**Cause:** Legacy `site` config conflicts with new `assets` config  
**Solution:** Migrate from `site` to `assets` (see configuration.md). Remove `site` key from wrangler.jsonc.

### "Assets not updating after deployment"

**Cause:** Browser or CDN cache serving old assets  
**Solution:** 
- Hard refresh browser (Cmd+Shift+R / Ctrl+F5)
- Use cache-busting (hashed filenames)
- Verify deployment completed: `wrangler tail`

