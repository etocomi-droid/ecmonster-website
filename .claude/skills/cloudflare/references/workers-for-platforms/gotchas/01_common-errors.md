## Common Errors

### "Worker not found"

**Cause:** Attempting to get Worker that doesn't exist in namespace  
**Solution:** Catch error and return 404:

```typescript
try {
  const userWorker = env.DISPATCHER.get(workerName);
  return userWorker.fetch(request);
} catch (e) {
  if (e.message.startsWith("Worker not found")) {
    return new Response("Worker not found", { status: 404 });
  }
  throw e;  // Re-throw unexpected errors
}
```

### "CPU time limit exceeded"

**Cause:** User Worker exceeded configured CPU time limit  
**Solution:** Track violations in Analytics Engine and return 429 response; consider adjusting limits per customer tier

### "Hostname Routing Issues"

**Cause:** DNS proxy settings causing routing problems  
**Solution:** Use `*/*` wildcard route which works regardless of proxy settings for orange-to-orange routing

### "Bindings Lost on Update"

**Cause:** Not using `keep_bindings` flag when updating Worker  
**Solution:** Use `keep_bindings: true` in API requests to preserve existing bindings during updates

### "Tag Filtering Not Working"

**Cause:** Special characters not URL encoded in tag filters  
**Solution:** URL encode tags (e.g., `tags=production%3Ayes`) and avoid special chars like `,` and `&`

### "Deploy Failures with ES Modules"

**Cause:** Incorrect upload format for ES modules  
**Solution:** Use multipart form upload, specify `main_module` in metadata, and set file type to `application/javascript+module`

### "Static Asset Upload Failed"

**Cause:** Invalid hash format, expired token, or incorrect encoding  
**Solution:** Hash must be first 16 bytes (32 hex chars) of SHA-256, upload within 1 hour of session creation, deploy within 1 hour of upload completion, and Base64 encode file contents

### "Outbound Worker Not Intercepting Calls"

**Cause:** Outbound Workers don't intercept Durable Object or mTLS binding fetch  
**Solution:** Plan egress control accordingly; not all fetch calls are intercepted

### "TCP Socket Connection Failed"

**Cause:** Outbound Worker enabled blocks `connect()` API for TCP sockets  
**Solution:** Outbound Workers only intercept `fetch()` calls; TCP socket connections unavailable when outbound configured. Remove outbound if TCP needed, or use proxy pattern.

### "API Rate Limit Exceeded"

**Cause:** Exceeded Cloudflare API rate limits (1200 requests per 5 minutes per account, 200 requests per second per IP)  
**Solution:** Implement exponential backoff:

```typescript
async function deployWithBackoff(deploy: () => Promise<void>, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await deploy();
    } catch (e) {
      if (e.status === 429 && i < maxRetries - 1) {
        await new Promise(r => setTimeout(r, Math.pow(2, i) * 1000));
        continue;
      }
      throw e;
    }
  }
}
```

### "Gradual Deployment Not Supported"

**Cause:** Attempted to use gradual deployments with user Workers  
**Solution:** Gradual deployments not supported for Workers in dispatch namespaces. Use all-at-once deployment with staged rollout via dispatch worker logic (feature flags, percentage-based routing).

### "Asset Session Expired"

**Cause:** Upload JWT expired (1 hour validity) or completion token expired (1 hour after upload)  
**Solution:** Complete asset upload within 1 hour of session creation, and deploy Worker within 1 hour of upload completion. For large uploads, batch files or increase upload parallelism.

