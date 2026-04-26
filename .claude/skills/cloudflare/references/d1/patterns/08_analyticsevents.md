## Analytics/Events

```typescript
async function logEvent(event: { type: string; userId?: number; metadata: object }, env: Env) {
  return await env.DB.prepare('INSERT INTO events (type, user_id, metadata) VALUES (?, ?, ?)').bind(event.type, event.userId || null, JSON.stringify(event.metadata)).run();
}

async function getEventStats(startDate: string, endDate: string, env: Env) {
  return await env.DB.prepare('SELECT type, COUNT(*) as count FROM events WHERE timestamp BETWEEN ? AND ? GROUP BY type ORDER BY count DESC').bind(startDate, endDate).all();
}
```

