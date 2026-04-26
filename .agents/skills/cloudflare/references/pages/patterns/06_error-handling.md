## Error Handling

```typescript
// functions/_middleware.ts
const errorHandler: PagesFunction = async (context) => {
  try {
    return await context.next();
  } catch (error) {
    console.error('Error:', error);
    if (context.request.url.includes('/api/')) {
      return Response.json({ error: error.message }, { status: 500 });
    }
    return new Response(`<h1>Error</h1><p>${error.message}</p>`, { 
      status: 500, headers: { 'Content-Type': 'text/html' } 
    });
  }
};
export const onRequest = [errorHandler];
```

