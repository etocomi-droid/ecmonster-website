## Pages Functions Binding

Pages Functions can trigger Workflows via service bindings:

```typescript
// functions/_middleware.ts
export const onRequest: PagesFunction<Env> = async ({ env, request }) => {
  const instance = await env.MY_WORKFLOW.create({
    params: { url: request.url }
  });
  return new Response(`Started ${instance.id}`);
};
```

Configure in wrangler.jsonc under `service_bindings`.

See: [api.md](./api.md), [patterns.md](./patterns.md)
