## Dynamic Routes

```typescript
// Single segment: functions/users/[id].ts
export const onRequestGet: PagesFunction = async ({ params }) => {
  // /users/123 → params.id = "123"
  return Response.json({ userId: params.id });
};

// Multi-segment: functions/files/[[path]].ts
export const onRequestGet: PagesFunction = async ({ params }) => {
  // /files/docs/api/v1.md → params.path = ["docs", "api", "v1.md"]
  const filePath = (params.path as string[]).join('/');
  return new Response(filePath);
};
```

