## Error Handling

**Automatic retries:**
- Failed cron executions are retried automatically unless `noRetry()` is called
- Retry happens after a delay (typically minutes)
- Only first `waitUntil()` failure is recorded in Cron Events

**Best practices:**
```typescript
export default {
  async scheduled(controller, env, ctx) {
    try {
      await criticalOperation(env);
    } catch (error) {
      // Log error details
      console.error("Cron failed:", {
        cron: controller.cron,
        scheduledTime: controller.scheduledTime,
        error: error.message,
        stack: error.stack,
      });
      
      // Decide: retry or skip
      if (error.message.includes("rate limit")) {
        controller.noRetry(); // Skip retry for rate limits
      }
      // Otherwise allow automatic retry
      throw error;
    }
  },
};
```

