## Dead Letter Queue Pattern

```typescript
// Main queue: After max_retries, goes to DLQ automatically
export default {
  async queue(batch: MessageBatch, env: Env): Promise<void> {
    for (const msg of batch.messages) {
      try {
        await riskyOperation(msg.body);
        msg.ack();
      } catch (error) {
        console.error(`Failed after ${msg.attempts} attempts:`, error);
      }
    }
  }
};

// DLQ consumer: Log and store failed messages
export default {
  async queue(batch: MessageBatch, env: Env): Promise<void> {
    for (const msg of batch.messages) {
      await env.FAILED_KV.put(msg.id, JSON.stringify(msg.body));
      msg.ack();
    }
  }
};
```

