## Error Handling

```typescript
class HTTPError extends Error {
  constructor(public status: number, message: string) { super(message); }
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    try {
      return await handleRequest(request, env);
    } catch (error) {
      if (error instanceof HTTPError) {
        return new Response(JSON.stringify({ error: error.message }), {
          status: error.status, headers: { 'Content-Type': 'application/json' }
        });
      }
      return new Response('Internal Server Error', { status: 500 });
    }
  },
};
```

