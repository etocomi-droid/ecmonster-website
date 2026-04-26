### "Cold Starts Are Slow"

**Problem:** First request after eviction takes longer  
**Cause:** DO constructor + initial storage access on cold start  
**Solution:** Expected behavior; optimize constructor, use connection pooling in clients, consider warming strategy for critical DOs

```typescript
// Warming strategy (periodically ping critical DOs)
export default {
  async scheduled(event: ScheduledEvent, env: Env) {
    const criticalIds = ["auth", "sessions", "locks"];
    await Promise.all(criticalIds.map(name => {
      const id = env.MY_DO.idFromName(name);
      const stub = env.MY_DO.get(id);
      return stub.ping();  // Keep warm
    }));
  }
};
```

