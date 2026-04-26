## Context Object

```typescript
interface EventContext<Env, Params, Data> {
  request: Request;              // HTTP request
  env: Env;                      // Bindings (KV, D1, R2, etc.)
  params: Params;                // Route parameters
  data: Data;                    // Middleware-shared data
  waitUntil: (promise: Promise<any>) => void;  // Background tasks
  next: () => Promise<Response>; // Next handler
  passThroughOnException: () => void;  // Error fallback (not in advanced mode)
}
```

