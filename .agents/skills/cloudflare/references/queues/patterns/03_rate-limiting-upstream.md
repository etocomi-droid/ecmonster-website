## Rate Limiting Upstream

```typescript
async queue(batch: MessageBatch, env: Env): Promise<void> {
  for (const msg of batch.messages) {
    try {
      await callRateLimitedAPI(msg.body);
      msg.ack();
    } catch (error) {
      if (error.status === 429) {
        const retryAfter = parseInt(error.headers.get('Retry-After') || '60');
        msg.retry({ delaySeconds: retryAfter });
      } else throw error;
    }
  }
}
```

