## Quick Start

```bash
# Interactive setup (recommended)
npx wrangler pipelines setup
```

**Minimal Worker example:**
```typescript
interface Env {
  STREAM: Pipeline;
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const event = { user_id: "123", event_type: "purchase", amount: 29.99 };
    
    // Fire-and-forget pattern
    ctx.waitUntil(env.STREAM.send([event]));
    
    return new Response('OK');
  }
} satisfies ExportedHandler<Env>;
```

