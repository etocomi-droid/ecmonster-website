### "Idempotency Issues"

**Problem:** At-least-once delivery causes duplicate side effects (double charges, duplicate emails)  
**Cause:** No deduplication mechanism  
**Solution:** Use KV to track execution IDs:

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const executionId = `${controller.cron}-${controller.scheduledTime}`;
    const existing = await env.EXECUTIONS.get(executionId);
    
    if (existing) {
      console.log("Already executed, skipping");
      controller.noRetry();
      return;
    }
    
    await env.EXECUTIONS.put(executionId, "1", { expirationTtl: 86400 }); // 24h TTL
    await performIdempotentOperation(env);
  },
};
```

