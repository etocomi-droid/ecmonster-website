## Error Classification Patterns

Classify errors to decide whether to retry or DLQ:

```typescript
async queue(batch: MessageBatch, env: Env): Promise<void> {
  for (const msg of batch.messages) {
    try {
      await processMessage(msg.body);
      msg.ack();
    } catch (error) {
      // Transient errors: retry with backoff
      if (isRetryable(error)) {
        const delay = Math.min(30 * (2 ** msg.attempts), 43200);
        msg.retry({ delaySeconds: delay });
      } 
      // Permanent errors: ack to avoid infinite retries
      else {
        console.error('Permanent error, sending to DLQ:', error);
        await env.ERROR_LOG.put(msg.id, JSON.stringify({ msg: msg.body, error: String(error) }));
        msg.ack(); // Prevent further retries
      }
    }
  }
}

function isRetryable(error: unknown): boolean {
  if (error instanceof Response) {
    // Retry: rate limits, timeouts, server errors
    return error.status === 429 || error.status >= 500;
  }
  if (error instanceof Error) {
    // Don't retry: validation, auth, not found
    return !error.message.includes('validation') && 
           !error.message.includes('unauthorized') &&
           !error.message.includes('not found');
  }
  return false; // Unknown errors don't retry
}
```

### "CPU Time Exceeded in Consumer"

**Problem:** Consumer fails with CPU time limit exceeded  
**Cause:** Consumer processing exceeding 30s default CPU time limit  
**Solution:** Increase CPU limit in wrangler.jsonc: `{ "limits": { "cpu_ms": 300000 } }` (5 minutes max)

