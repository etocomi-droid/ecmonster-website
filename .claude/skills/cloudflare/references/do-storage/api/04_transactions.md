## Transactions

```typescript
// Sync (SQL/sync KV only)
this.ctx.storage.transactionSync(() => {
  this.sql.exec('UPDATE accounts SET balance = balance - ? WHERE id = ?', 100, 1);
  this.sql.exec('UPDATE accounts SET balance = balance + ? WHERE id = ?', 100, 2);
  return "result";
});

// Async
await this.ctx.storage.transaction(async () => {
  const value = await this.ctx.storage.get("counter");
  await this.ctx.storage.put("counter", value + 1);
  if (value > 100) this.ctx.storage.rollback(); // Explicit rollback
});
```

