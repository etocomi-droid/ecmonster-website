## Testing with Miniflare

Miniflare provides mock botManagement data for local development:

**Default values:**
- `score: 99` (human)
- `verifiedBot: false`
- `corporateProxy: false`
- `ja3Hash: "25b4882c2bcb50cd6b469ff28c596742"`
- `staticResource: false`
- `detectionIds: []`

**Override in tests:**
```typescript
import { getPlatformProxy } from 'wrangler';

const { cf, dispose } = await getPlatformProxy();
// cf.botManagement is frozen mock object
expect(cf.botManagement.score).toBe(99);
```

For custom test data, mock request.cf in your test setup.
