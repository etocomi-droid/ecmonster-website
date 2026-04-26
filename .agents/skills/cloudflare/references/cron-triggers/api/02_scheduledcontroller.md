## ScheduledController

```typescript
interface ScheduledController {
  scheduledTime: number;  // Unix ms when scheduled to run
  cron: string;           // Expression that triggered (e.g., "*/5 * * * *")
  type: string;           // Always "scheduled"
  noRetry(): void;        // Prevent automatic retry on failure
}
```

**Prevent retry on failure:**
```typescript
export default {
  async scheduled(controller, env, ctx) {
    try {
      await riskyOperation(env);
    } catch (error) {
      // Don't retry - failure is expected/acceptable
      controller.noRetry();
      console.error("Operation failed, not retrying:", error);
    }
  },
};
```

**When to use noRetry():**
- External API failures outside your control (avoid hammering failed services)
- Rate limit errors (retry would fail again immediately)
- Duplicate execution detected (idempotency check failed)
- Non-critical operations where skip is acceptable (analytics, caching)
- Validation errors that won't resolve on retry

