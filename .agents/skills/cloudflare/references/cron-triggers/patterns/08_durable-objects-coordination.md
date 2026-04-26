## Durable Objects Coordination

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const stub = env.COORDINATOR.get(env.COORDINATOR.idFromName("cron-lock"));
    const acquired = await stub.tryAcquireLock(controller.scheduledTime);
    if (!acquired) {
      controller.noRetry();
      return;
    }
    try {
      await performTask(env);
    } finally {
      await stub.releaseLock();
    }
  },
};
```

