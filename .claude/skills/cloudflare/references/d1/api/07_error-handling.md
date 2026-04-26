## Error Handling

```typescript
async function getUser(userId: number, env: Env): Promise<Response> {
  try {
    const result = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(userId).all();
    if (!result.success) return new Response('Database error', { status: 500 });
    if (result.results.length === 0) return new Response('User not found', { status: 404 });
    return Response.json(result.results[0]);
  } catch (error) {
    return new Response('Internal error', { status: 500 });
  }
}

// Constraint violations
try {
  await env.DB.prepare('INSERT INTO users (email, name) VALUES (?, ?)').bind(email, name).run();
} catch (error) {
  if (error.message?.includes('UNIQUE constraint failed')) return new Response('Email exists', { status: 409 });
  throw error;
}
```

