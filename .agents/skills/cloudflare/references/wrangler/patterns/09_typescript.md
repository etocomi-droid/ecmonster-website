## TypeScript

```bash
wrangler types  # Generate types from config
```

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    return Response.json({ value: await env.MY_KV.get("key") });
  }
} satisfies ExportedHandler<Env>;
```

