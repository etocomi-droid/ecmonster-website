## Testing with Mock Bindings

### Vitest Mock

```typescript
import { vi } from 'vitest';

const mockKV: KVNamespace = {
  get: vi.fn(async (key) => key === 'test' ? 'value' : null),
  put: vi.fn(async () => {}),
  delete: vi.fn(async () => {}),
  list: vi.fn(async () => ({ keys: [], list_complete: true, cursor: '' })),
  getWithMetadata: vi.fn(),
} as unknown as KVNamespace;

const mockEnv: Env = { MY_KV: mockKV };
const mockCtx: ExecutionContext = {
  waitUntil: vi.fn(),
  passThroughOnException: vi.fn(),
};

const response = await worker.fetch(
  new Request('http://localhost/test'),
  mockEnv,
  mockCtx
);
```

