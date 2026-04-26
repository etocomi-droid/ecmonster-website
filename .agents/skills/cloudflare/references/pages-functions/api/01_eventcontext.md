## EventContext

```typescript
interface EventContext<Env = any> {
  request: Request;              // Incoming request
  functionPath: string;          // Request path
  waitUntil(promise: Promise<any>): void;  // Background tasks (non-blocking)
  passThroughOnException(): void;          // Fallback to static on error
  next(input?: Request | string, init?: RequestInit): Promise<Response>;
  env: Env;                      // Bindings, vars, secrets
  params: Record<string, string | string[]>;  // Route params ([user] or [[catchall]])
  data: any;                     // Middleware shared state
}
```

**TypeScript:** See [configuration.md](./configuration.md) for `wrangler types` setup

