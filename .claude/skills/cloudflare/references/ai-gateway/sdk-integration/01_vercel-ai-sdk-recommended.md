## Vercel AI SDK (Recommended)

```typescript
import { createAiGateway } from 'ai-gateway-provider';
import { createOpenAI } from '@ai-sdk/openai';
import { generateText } from 'ai';

const gateway = createAiGateway({
  accountId: process.env.CF_ACCOUNT_ID,
  gateway: process.env.CF_GATEWAY_ID,
  apiKey: process.env.CF_API_TOKEN // Optional for auth gateways
});

const openai = createOpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Single model
const { text } = await generateText({
  model: gateway(openai('gpt-4o')),
  prompt: 'Hello'
});

// Automatic fallback array
const { text } = await generateText({
  model: gateway([
    openai('gpt-4o'),
    anthropic('claude-sonnet-4-5'),
    openai('gpt-4o-mini')
  ]),
  prompt: 'Complex task'
});
```

### Options

```typescript
model: gateway(openai('gpt-4o'), {
  cacheKey: 'my-key',
  cacheTtl: 3600,
  metadata: { userId: 'u123', team: 'eng' }, // Max 5 entries
  retries: { maxAttempts: 3, backoff: 'exponential' }
})
```

