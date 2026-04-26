## CRITICAL: Top Production Mistakes

### 1. "Entire Batch Retried After Single Error"

**Problem:** Throwing uncaught error in queue handler retries the entire batch, not just the failed message  
**Cause:** Uncaught exceptions propagate to the runtime, triggering batch-level retry  
**Solution:** Always wrap individual message processing in try/catch and call `msg.retry()` explicitly

```typescript
// ❌ BAD: Throws error, retries entire batch
async queue(batch: MessageBatch): Promise<void> {
  for (const msg of batch.messages) {
    await riskyOperation(msg.body); // If this throws, entire batch retries
    msg.ack();
  }
}

// ✅ GOOD: Catch per message, handle individually
async queue(batch: MessageBatch): Promise<void> {
  for (const msg of batch.messages) {
    try {
      await riskyOperation(msg.body);
      msg.ack();
    } catch (error) {
      msg.retry({ delaySeconds: 60 });
    }
  }
}
```

### 2. "Messages Retry Forever"

**Problem:** Messages not explicitly ack'd or retry'd will auto-retry indefinitely  
**Cause:** Runtime default behavior retries unhandled messages until `max_retries` reached  
**Solution:** Always call `msg.ack()` or `msg.retry()` for each message. Never leave messages unhandled.

```typescript
// ❌ BAD: Skipped messages auto-retry forever
async queue(batch: MessageBatch): Promise<void> {
  for (const msg of batch.messages) {
    if (shouldProcess(msg.body)) {
      await process(msg.body);
      msg.ack();
    }
    // Missing: msg.ack() for skipped messages - they will retry!
  }
}

// ✅ GOOD: Explicitly handle all messages
async queue(batch: MessageBatch): Promise<void> {
  for (const msg of batch.messages) {
    if (shouldProcess(msg.body)) {
      await process(msg.body);
      msg.ack();
    } else {
      msg.ack(); // Explicitly ack even if not processing
    }
  }
}
```

