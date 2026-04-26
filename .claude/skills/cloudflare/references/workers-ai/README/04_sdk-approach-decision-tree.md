## SDK Approach Decision Tree

### Native Binding (Recommended)

**When**: Building Workers/Pages with TypeScript  
**Why**: Zero external dependencies, best performance, native types

```typescript
await env.AI.run(model, input);
```

### REST API

**When**: External services, non-Workers environments, testing  
**Why**: Standard HTTP, works anywhere

```bash
curl https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai/run/@cf/meta/llama-3.1-8b-instruct \
  -H "Authorization: Bearer <API_TOKEN>" \
  -d '{"messages":[{"role":"user","content":"Hello"}]}'
```

### Vercel AI SDK Integration

**When**: Using Vercel AI SDK features (streaming UI, tool calling abstractions)  
**Why**: Unified interface across providers

```typescript
import { openai } from '@ai-sdk/openai';

const model = openai('model-name', {
  baseURL: 'https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai/v1',
  headers: { Authorization: 'Bearer <API_TOKEN>' }
});
```

