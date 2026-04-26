## Ack/Retry Precedence Rules

1. **Per-message calls take precedence**: If you call both `msg.ack()` and `msg.retry()`, last call wins
2. **Batch calls don't override**: `batch.ackAll()` only affects messages without explicit ack/retry
3. **No action = automatic retry**: Messages with no explicit action retry with configured delay

```typescript
async queue(batch: MessageBatch): Promise<void> {
  for (const msg of batch.messages) {
    msg.ack();        // Message marked for ack
    msg.retry();      // Overrides ack - message will retry
  }
  
  batch.ackAll();     // Only affects messages not explicitly handled above
}
```

