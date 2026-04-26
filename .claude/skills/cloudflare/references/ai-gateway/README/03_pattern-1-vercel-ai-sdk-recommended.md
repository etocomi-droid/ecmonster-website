## Pattern 1: Vercel AI SDK (Recommended)

Most modern pattern using official `ai-gateway-provider` package with automatic fallbacks.

```typescript
import { createAiGateway } from 'ai-gateway-provider';
import { createOpenAI } from '@ai-sdk/openai';
import { generateText } from 'ai';

const gateway = createAiGateway({
  accountId: process.env.CF_ACCOUNT_ID,
  gateway: process.env.CF_GATEWAY_ID,
});

const openai = createOpenAI({ 
  apiKey: process.env.OPENAI_API_KEY 
});

// Single model
const { text } = await generateText({
  model: gateway(openai('gpt-4o')),
  prompt: 'Hello'
});

// Automatic fallback array
const { text } = await generateText({
  model: gateway([
    openai('gpt-4o'),              // Try first
    anthropic('claude-sonnet-4-5'), // Fallback
  ]),
  prompt: 'Hello'
});
```

**Install:** `npm install ai-gateway-provider ai @ai-sdk/openai @ai-sdk/anthropic`

