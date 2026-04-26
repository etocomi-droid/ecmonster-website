## Graceful Cleanup

Use `ctx.waitUntil()` to complete work after response:

```typescript
async myMethod() {
  const response = { success: true };
  this.ctx.waitUntil(this.ctx.storage.sql.exec("DELETE FROM old_data WHERE timestamp < ?", cutoff));
  return response;
}
```

