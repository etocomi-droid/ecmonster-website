## Write Coalescing Pattern

Multiple writes to same key coalesce atomically (last write wins):

```typescript
async updateMetrics(userId: string, actions: Action[]) {
  // All writes coalesce - no await needed
  for (const action of actions) {
    this.ctx.storage.put(`user:${userId}:lastAction`, action.type);
    this.ctx.storage.put(`user:${userId}:count`, 
      await this.ctx.storage.get(`user:${userId}:count`) + 1);
  }
  // Output gate ensures all writes confirm before response
  return new Response("OK");
}

// Atomic batch with SQL
async batchUpdate(items: Item[]) {
  this.sql.exec('BEGIN');
  for (const item of items) {
    this.sql.exec('INSERT OR REPLACE INTO items VALUES (?, ?)', item.id, item.value);
  }
  this.sql.exec('COMMIT');
}
```

