## Session Storage

```typescript
async function createSession(userId: number, token: string, env: Env) {
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString();
  return await env.DB.prepare('INSERT INTO sessions (user_id, token, expires_at) VALUES (?, ?, ?)').bind(userId, token, expiresAt).run();
}

async function validateSession(token: string, env: Env) {
  return await env.DB.prepare('SELECT s.*, u.email FROM sessions s JOIN users u ON s.user_id = u.id WHERE s.token = ? AND s.expires_at > CURRENT_TIMESTAMP').bind(token).first();
}
```

