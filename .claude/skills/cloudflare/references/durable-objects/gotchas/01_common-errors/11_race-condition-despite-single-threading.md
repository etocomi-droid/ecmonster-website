### "Race Condition Despite Single-Threading"

**Problem:** Concurrent requests see inconsistent state  
**Cause:** Async operations allow request interleaving (await = yield point)  
**Solution:** Use `blockConcurrencyWhile()` for critical sections or atomic storage ops

```typescript
// ❌ Wrong - race condition
async incrementCounter() {
  const count = await this.ctx.storage.get("count") || 0;
  // ⚠️ Another request could execute here during await
  await this.ctx.storage.put("count", count + 1);
}

// ✅ Right - atomic operation
async incrementCounter() {
  return this.ctx.storage.sql.exec(
    "INSERT INTO counters (id, value) VALUES (1, 1) ON CONFLICT(id) DO UPDATE SET value = value + 1 RETURNING value"
  ).one().value;
}

// ✅ Right - explicit locking
async criticalOperation() {
  await this.ctx.blockConcurrencyWhile(async () => {
    const count = await this.ctx.storage.get("count") || 0;
    await this.ctx.storage.put("count", count + 1);
  });
}
```

