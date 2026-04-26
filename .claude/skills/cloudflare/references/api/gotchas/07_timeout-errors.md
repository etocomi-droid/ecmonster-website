## Timeout Errors

**Problem:** Request times out (default 60s).

**Cause:** Large operations (bulk DNS, zone transfers).

**Solution:** Increase timeout or split operations.

```typescript
// Increase timeout
const client = new Cloudflare({
  timeout: 300000, // 5 minutes
});

// Or split operations
const batchSize = 100;
for (let i = 0; i < records.length; i += batchSize) {
  const batch = records.slice(i, i + batchSize);
  await processBatch(batch);
}
```

