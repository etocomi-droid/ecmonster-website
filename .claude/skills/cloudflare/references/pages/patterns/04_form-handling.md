## Form Handling

```typescript
// functions/api/contact.ts
export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  const formData = await request.formData();
  await env.QUEUE.send({name: formData.get('name'), email: formData.get('email')});
  return new Response('<h1>Thanks!</h1>', { headers: { 'Content-Type': 'text/html' } });
};
```

