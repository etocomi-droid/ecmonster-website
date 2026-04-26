## Session Management

```typescript
async createSession(userId: string, data: object): Promise<string> {
  const id = crypto.randomUUID(), exp = Date.now() + 86400000;
  this.ctx.storage.sql.exec("INSERT INTO sessions VALUES (?, ?, ?, ?)", id, userId, JSON.stringify(data), exp);
  await this.ctx.storage.setAlarm(exp);
  return id;
}

async getSession(id: string): Promise<object | null> {
  const row = this.ctx.storage.sql.exec("SELECT data FROM sessions WHERE id = ? AND expires_at > ?", id, Date.now()).one();
  return row ? JSON.parse(row.data) : null;
}

async alarm() { this.ctx.storage.sql.exec("DELETE FROM sessions WHERE expires_at <= ?", Date.now()); }
```

