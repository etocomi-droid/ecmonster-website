## Retry Configuration

**When to increase:** Rate-limit-heavy workflows, flaky network

**When to decrease:** Fast-fail requirements, user-facing requests

```typescript
// Increase retries for batch operations
const client = new Cloudflare({ maxRetries: 10 });

// Disable retries for fast-fail
const fastClient = new Cloudflare({ maxRetries: 0 });
```

