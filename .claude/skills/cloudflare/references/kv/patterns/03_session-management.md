## Session Management

```typescript
interface Session { userId: string; expiresAt: number; }

async function createSession(env: Env, userId: string): Promise<string> {
  const sessionId = crypto.randomUUID();
  const expiresAt = Date.now() + (24 * 60 * 60 * 1000);
  
  await env.SESSIONS.put(
    `session:${sessionId}`,
    JSON.stringify({ userId, expiresAt }),
    { expirationTtl: 86400, metadata: { createdAt: Date.now() } }
  );
  
  return sessionId;
}

async function getSession(env: Env, sessionId: string): Promise<Session | null> {
  const data = await env.SESSIONS.get<Session>(`session:${sessionId}`, "json");
  if (!data || data.expiresAt < Date.now()) return null;
  return data;
}
```

