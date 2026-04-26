## Transform & Store to R2

```typescript
async fetch(request: Request, env: Env): Promise<Response> {
  const file = (await request.formData()).get('image') as File;
  const transformed = await env.IMAGES
    .input(await file.arrayBuffer())
    .transform({ width: 800, format: 'avif', quality: 80 })
    .output();
  await env.R2.put(`images/${Date.now()}.avif`, transformed.response().body);
  return Response.json({ success: true });
}
```

