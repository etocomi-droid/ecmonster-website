## Rate Limiting

```typescript
async checkLimit(key: string, limit: number, windowMs: number): Promise<boolean> {
  const req = this.ctx.storage.sql.exec("SELECT COUNT(*) as count FROM requests WHERE key = ? AND timestamp > ?", key, Date.now() - windowMs).one();
  if (req.count >= limit) return false;
  this.ctx.storage.sql.exec("INSERT INTO requests (key, timestamp) VALUES (?, ?)", key, Date.now());
  return true;
}
```

