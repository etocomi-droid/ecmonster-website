## Common Errors

### "Container running indefinitely"

**Cause:** `keepAlive: true` without calling `destroy()`
**Solution:** Always call `destroy()` when done with keepAlive containers

```typescript
const sandbox = getSandbox(env.Sandbox, 'temp', { keepAlive: true });
try {
  const result = await sandbox.exec('python script.py');
  return result.stdout;
} finally {
  await sandbox.destroy();  // REQUIRED to free resources
}
```

### "CONTAINER_NOT_READY"

**Cause:** Container still provisioning (first request or after sleep)
**Solution:** Retry after 2-3s

```typescript
async function execWithRetry(sandbox, cmd) {
  for (let i = 0; i < 3; i++) {
    try {
      return await sandbox.exec(cmd);
    } catch (e) {
      if (e.code === 'CONTAINER_NOT_READY') {
        await new Promise(r => setTimeout(r, 2000));
        continue;
      }
      throw e;
    }
  }
}
```

### "Connection refused: container port not found"

**Cause:** Missing `EXPOSE` directive in Dockerfile
**Solution:** Add `EXPOSE <port>` to Dockerfile (only needed for `wrangler dev`, production auto-exposes)

### "Preview URLs not working"

**Cause:** Custom domain not configured, wildcard DNS missing, `normalizeId` not set, or `proxyToSandbox()` not called
**Solution:** Check:
1. Custom domain configured? (not `.workers.dev`)
2. Wildcard DNS set up? (`*.domain.com → worker.domain.com`)
3. `normalizeId: true` in getSandbox?
4. `proxyToSandbox()` called first in fetch?

### "Slow first request"

**Cause:** Cold start (container provisioning)
**Solution:**
- Use `sleepAfter` instead of creating new sandboxes
- Pre-warm with cron triggers
- Set `keepAlive: true` for critical sandboxes

### "File not persisting"

**Cause:** Files in `/tmp` or other ephemeral paths
**Solution:** Use `/workspace` for persistent files

### "Bucket mounting doesn't work locally"

**Cause:** Bucket mounting requires FUSE, not available in `wrangler dev`
**Solution:** Test bucket mounting in production only. Use mock data locally.

### "Different normalizeId = different sandbox"

**Cause:** Changing `normalizeId` option changes Durable Object ID
**Solution:** Set `normalizeId` consistently. `normalizeId: true` lowercases the ID.

```typescript
// These create DIFFERENT sandboxes:
getSandbox(env.Sandbox, 'MyApp');              // DO ID: hash('MyApp')
getSandbox(env.Sandbox, 'MyApp', { normalizeId: true });  // DO ID: hash('myapp')
```

### "Code context variables disappeared"

**Cause:** Container restart clears code context state
**Solution:** Code contexts are ephemeral. Recreate context after container sleep/wake.

