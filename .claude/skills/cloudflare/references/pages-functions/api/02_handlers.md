## Handlers

```typescript
// Generic (fallback for any method)
export async function onRequest(ctx: EventContext): Promise<Response> {
  return new Response('Any method');
}

// Method-specific (takes precedence over generic)
export async function onRequestGet(ctx: EventContext): Promise<Response> {
  return Response.json({ message: 'GET' });
}

export async function onRequestPost(ctx: EventContext): Promise<Response> {
  const body = await ctx.request.json();
  return Response.json({ received: body });
}
// Also: onRequestPut, onRequestPatch, onRequestDelete, onRequestHead, onRequestOptions
```

