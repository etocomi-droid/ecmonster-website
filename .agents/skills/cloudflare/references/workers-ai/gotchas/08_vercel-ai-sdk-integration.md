## Vercel AI SDK Integration

```typescript
import { openai } from '@ai-sdk/openai';
const model = openai('gpt-3.5-turbo', {
  baseURL: 'https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai/v1',
  headers: { Authorization: 'Bearer <API_TOKEN>' }
});
```
