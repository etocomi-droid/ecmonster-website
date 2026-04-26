## Common Errors

### "Race Condition in Concurrent Calls"

**Cause:** Multiple concurrent storage operations initiated from same event (e.g., `Promise.all()`) are not protected by input gate  
**Solution:** Avoid concurrent storage operations within single event; input gate only serializes requests from different events, not operations within same event

### "Direct SQL Transaction Statements"

**Cause:** Using `BEGIN TRANSACTION` directly instead of transaction methods  
**Solution:** Use `this.ctx.storage.transactionSync()` for sync operations or `this.ctx.storage.transaction()` for async operations

### "Async in transactionSync"

**Cause:** Using async operations inside `transactionSync()` callback  
**Solution:** Use async `transaction()` method instead of `transactionSync()` when async operations needed

### "TypeScript Type Mismatch at Runtime"

**Cause:** Query doesn't return all fields specified in TypeScript type  
**Solution:** Ensure SQL query selects all columns that match the TypeScript type definition

### "Silent Data Corruption with Large IDs"

**Cause:** JavaScript numbers have 53-bit precision; SQLite INTEGER is 64-bit  
**Symptom:** IDs > 9007199254740991 (Number.MAX_SAFE_INTEGER) silently truncate/corrupt  
**Solution:** Store large IDs as TEXT:

```typescript
// BAD: Snowflake/Twitter IDs will corrupt
this.sql.exec("CREATE TABLE events(id INTEGER PRIMARY KEY)");
this.sql.exec("INSERT INTO events VALUES (?)", 1234567890123456789n); // Corrupts!

// GOOD: Store as TEXT
this.sql.exec("CREATE TABLE events(id TEXT PRIMARY KEY)");
this.sql.exec("INSERT INTO events VALUES (?)", "1234567890123456789");
```

### "Alarm Not Deleted with deleteAll()"

**Cause:** `deleteAll()` doesn't delete alarms automatically  
**Solution:** Call `deleteAlarm()` explicitly before `deleteAll()` to remove alarm

### "Slow Performance"

**Cause:** Using async KV API instead of sync API  
**Solution:** Use sync KV API (`ctx.storage.kv`) for better performance with simple key-value operations

### "High Billing from Storage Operations"

**Cause:** Excessive `rowsRead`/`rowsWritten` or unused objects not cleaned up  
**Solution:** Monitor `rowsRead`/`rowsWritten` metrics and ensure unused objects call `deleteAll()`

### "Durable Object Overloaded"

**Cause:** Single DO exceeding ~1K req/sec soft limit  
**Solution:** Shard across multiple DOs with random IDs or other distribution strategy

