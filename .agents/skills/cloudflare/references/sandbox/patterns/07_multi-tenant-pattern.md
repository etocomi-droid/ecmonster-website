## Multi-Tenant Pattern

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const userId = request.headers.get('X-User-ID');
    const sandbox = getSandbox(env.Sandbox, 'multi-tenant');
    
    // Each user gets isolated session
    let session;
    try {
      session = await sandbox.getSession(userId);
    } catch {
      session = await sandbox.createSession({
        id: userId,
        cwd: `/workspace/users/${userId}`,
        env: { USER_ID: userId }
      });
    }
    
    const code = await request.text();
    const result = await session.exec(`python3 -c "${code}"`);
    
    return Response.json({ output: result.stdout });
  }
};
```

