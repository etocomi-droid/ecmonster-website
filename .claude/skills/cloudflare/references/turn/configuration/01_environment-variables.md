## Environment Variables

```bash
# .env
CLOUDFLARE_ACCOUNT_ID=your_account_id
CLOUDFLARE_API_TOKEN=your_api_token
TURN_KEY_ID=your_turn_key_id
TURN_KEY_SECRET=your_turn_key_secret
```

Validate with zod:

```typescript
import { z } from 'zod';

const envSchema = z.object({
  CLOUDFLARE_ACCOUNT_ID: z.string().min(1),
  CLOUDFLARE_API_TOKEN: z.string().min(1),
  TURN_KEY_ID: z.string().min(1),
  TURN_KEY_SECRET: z.string().min(1)
});

export const config = envSchema.parse(process.env);
```

