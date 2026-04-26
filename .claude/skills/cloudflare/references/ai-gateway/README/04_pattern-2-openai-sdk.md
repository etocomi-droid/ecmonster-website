## Pattern 2: OpenAI SDK

Drop-in replacement for OpenAI API with multi-provider support.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/compat`,
  defaultHeaders: {
    'cf-aig-authorization': `Bearer ${cfToken}` // For authenticated gateways
  }
});

// Switch providers by changing model format: {provider}/{model}
const response = await client.chat.completions.create({
  model: 'openai/gpt-4o', // or 'anthropic/claude-sonnet-4-5'
  messages: [{ role: 'user', content: 'Hello!' }]
});
```

