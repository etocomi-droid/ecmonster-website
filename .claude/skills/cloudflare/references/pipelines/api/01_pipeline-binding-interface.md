## Pipeline Binding Interface

```typescript
// From @cloudflare/workers-types
interface Pipeline {
  send(data: object | object[]): Promise<void>;
}

interface Env {
  STREAM: Pipeline;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // send() returns Promise<void> - no result data
    await env.STREAM.send([event]);
    return new Response('OK');
  }
} satisfies ExportedHandler<Env>;
```

**Key points:**
- `send()` accepts single object or array
- Always returns `Promise<void>` (no confirmation data)
- Throws on network/validation errors (wrap in try/catch)
- Use `ctx.waitUntil()` for fire-and-forget pattern

