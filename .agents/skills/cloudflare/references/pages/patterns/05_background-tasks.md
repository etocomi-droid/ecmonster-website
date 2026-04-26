## Background Tasks

```typescript
export const onRequestPost: PagesFunction = async ({ request, waitUntil }) => {
  const data = await request.json();
  waitUntil(fetch('https://api.example.com/webhook', {
    method: 'POST', body: JSON.stringify(data)
  }));
  return Response.json({ queued: true });
};
```

