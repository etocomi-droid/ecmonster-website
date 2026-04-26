## Module Worker Pattern (Recommended)

```typescript
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    return new Response('Hello World!');
  },
};
```

**Handler parameters**:
- `request`: Incoming HTTP request (standard Request object)
- `env`: Environment bindings (KV, D1, R2, secrets, vars)
- `ctx`: Execution context (`waitUntil`, `passThroughOnException`)

