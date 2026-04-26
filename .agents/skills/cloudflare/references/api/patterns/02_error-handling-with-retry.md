## Error Handling with Retry

**Problem:** Rate limits (429) and transient errors need retry.

**Solution:** SDKs auto-retry with exponential backoff. Customize as needed.

```typescript
// Increase retries for rate-limit-heavy operations
const client = new Cloudflare({ maxRetries: 5 });

try {
  const zone = await client.zones.create({ /* ... */ });
} catch (err) {
  if (err instanceof Cloudflare.RateLimitError) {
    // Already retried 5 times with backoff
    const retryAfter = err.headers['retry-after'];
    console.log(`Rate limited. Retry after ${retryAfter}s`);
  }
}
```

