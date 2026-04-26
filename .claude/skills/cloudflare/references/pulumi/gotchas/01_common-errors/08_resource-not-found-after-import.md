### "Resource not found after import"

**Problem:** Imported resource shows as changed on next `pulumi up`  
**Cause:** State mismatch between actual resource and Pulumi config  
**Solution:** Check property names/types match exactly

```bash
pulumi import cloudflare:index/workerScript:WorkerScript my-worker <account_id>/<worker_name>
pulumi preview # If shows changes, adjust Pulumi code to match actual resource
```

