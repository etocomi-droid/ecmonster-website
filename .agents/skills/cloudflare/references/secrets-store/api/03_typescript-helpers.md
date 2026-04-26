## TypeScript Helpers

Official types available via `@cloudflare/workers-types`:

```typescript
import type { SecretsStoreSecret } from "@cloudflare/workers-types";

interface Env {
  STRIPE_API_KEY: SecretsStoreSecret;
  DATABASE_URL: SecretsStoreSecret;
  WORKER_SECRET: string; // Regular Worker secret (direct access)
}
```

Custom helper type:

```typescript
interface SecretsStoreBinding {
  get(): Promise<string>;
}

// Fallback helper
async function getSecretWithFallback(
  primary: SecretsStoreBinding,
  fallback?: SecretsStoreBinding
): Promise<string> {
  try {
    return await primary.get();
  } catch (error) {
    if (fallback) return await fallback.get();
    throw error;
  }
}

// Batch helper
async function getAllSecrets(
  secrets: Record<string, SecretsStoreBinding>
): Promise<Record<string, string>> {
  const entries = await Promise.all(
    Object.entries(secrets).map(async ([k, v]) => [k, await v.get()])
  );
  return Object.fromEntries(entries);
}
```

See: [configuration.md](./configuration.md), [patterns.md](./patterns.md), [gotchas.md](./gotchas.md)
