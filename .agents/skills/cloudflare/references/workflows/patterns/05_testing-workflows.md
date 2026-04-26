## Testing Workflows

### Setup

```typescript
// vitest.config.ts
import { defineWorkersConfig } from '@cloudflare/vitest-pool-workers/config';

export default defineWorkersConfig({
  test: {
    poolOptions: {
      workers: {
        wrangler: { configPath: './wrangler.jsonc' }
      }
    }
  }
});
```

### Introspection API

```typescript
import { introspectWorkflowInstance } from 'cloudflare:test';

const instance = await env.MY_WORKFLOW.create({ params: { userId: '123' } });
const introspector = await introspectWorkflowInstance(env.MY_WORKFLOW, instance.id);

// Wait for step completion
const result = await introspector.waitForStepResult({ name: 'fetch user', index: 0 });

// Mock step behavior
await introspector.modify(async (m) => {
  await m.mockStepResult({ name: 'api call' }, { mocked: true });
});
```

