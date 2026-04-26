### "waitUntil() Tasks Not Completing"

**Problem:** Background tasks in `ctx.waitUntil()` fail silently or don't execute  
**Cause:** Promises rejected without error handling, or handler returns before promise settles  
**Solution:** Always await or handle errors in waitUntil promises:

```typescript
export default {
  async scheduled(controller, env, ctx) {
    // BAD: Silent failures
    ctx.waitUntil(riskyOperation());
    
    // GOOD: Explicit error handling
    ctx.waitUntil(
      riskyOperation().catch(err => {
        console.error("Background task failed:", err);
        return logError(err, env);
      })
    );
  },
};
```

