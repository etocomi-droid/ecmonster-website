## OpenAI SDK

```typescript
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/openai`,
  defaultHeaders: { 'cf-aig-authorization': `Bearer ${cfToken}` }
});

// Unified API - switch providers via model name
model: 'openai/gpt-4o'  // or 'anthropic/claude-sonnet-4-5'
```

