## Anthropic SDK

```typescript
const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
  baseURL: `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/anthropic`,
  defaultHeaders: { 'cf-aig-authorization': `Bearer ${cfToken}` }
});
```

