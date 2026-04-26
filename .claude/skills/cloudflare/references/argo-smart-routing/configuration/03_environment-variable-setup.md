## Environment Variable Setup

**Required Environment Variables:**
```bash
# .env
CLOUDFLARE_API_TOKEN=your_api_token_here
CLOUDFLARE_ZONE_ID=your_zone_id_here
CLOUDFLARE_ACCOUNT_ID=your_account_id_here

# Optional
ARGO_ENABLED=true
ARGO_TIERED_CACHE=true
```

**TypeScript Configuration Loader:**
```typescript
// config/env.ts
import { z } from 'zod';

const envSchema = z.object({
  CLOUDFLARE_API_TOKEN: z.string().min(1),
  CLOUDFLARE_ZONE_ID: z.string().min(1),
  CLOUDFLARE_ACCOUNT_ID: z.string().min(1),
  ARGO_ENABLED: z.string().optional().default('false'),
  ARGO_TIERED_CACHE: z.string().optional().default('false'),
});

export const env = envSchema.parse(process.env);

export const argoConfig = {
  enabled: env.ARGO_ENABLED === 'true',
  tieredCache: env.ARGO_TIERED_CACHE === 'true',
};
```

