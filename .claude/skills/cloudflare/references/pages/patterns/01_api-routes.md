## API Routes

```typescript
// functions/api/todos/[id].ts
export const onRequestGet: PagesFunction<Env> = async ({ env, params }) => {
  const todo = await env.DB.prepare('SELECT * FROM todos WHERE id = ?').bind(params.id).first();
  if (!todo) return new Response('Not found', { status: 404 });
  return Response.json(todo);
};

export const onRequestPut: PagesFunction<Env> = async ({ env, params, request }) => {
  const body = await request.json();
  await env.DB.prepare('UPDATE todos SET title = ?, completed = ? WHERE id = ?')
    .bind(body.title, body.completed, params.id).run();
  return Response.json({ success: true });
};
// Also: onRequestDelete, onRequestPost
```

