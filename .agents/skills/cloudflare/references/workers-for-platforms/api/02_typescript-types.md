## TypeScript Types

```typescript
import type { DispatchNamespace } from '@cloudflare/workers-types';

interface DispatchNamespace {
  get(name: string, options?: Record<string, unknown>, dispatchOptions?: DynamicDispatchOptions): Fetcher;
}

interface DynamicDispatchOptions {
  limits?: DynamicDispatchLimits;
  outbound?: Record<string, unknown>;
}

interface DynamicDispatchLimits {
  cpuMs?: number;        // Max CPU milliseconds
  subRequests?: number;  // Max fetch() calls
}

// Usage
const userWorker = env.DISPATCHER.get('customer-123', {}, {
  limits: { cpuMs: 50, subRequests: 20 },
  outbound: { customerId: '123', url: request.url }
});
```

