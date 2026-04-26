## ctx.waitUntil Usage

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const data = await fetchCriticalData(); // Critical path
    
    // Non-blocking background tasks
    ctx.waitUntil(Promise.all([
      logToAnalytics(data),
      cleanupOldRecords(env.DB),
      notifyWebhook(env.WEBHOOK_URL, data),
    ]));
  },
};
```

