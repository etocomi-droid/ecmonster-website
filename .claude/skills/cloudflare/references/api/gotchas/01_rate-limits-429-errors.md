## Rate Limits & 429 Errors

**Actual Limits:**
- **1200 requests / 5 minutes** per user/token (global)
- **200 requests / second** per IP address
- **GraphQL: 320 / 5 minutes** (cost-based)

**SDK Behavior:**
- Auto-retry with exponential backoff (default 2 retries, Go: 10)
- Respects `Retry-After` header
- Throws `RateLimitError` after exhausting retries

**Solution:**

```typescript
// Increase retries for rate-limit-heavy workflows
const client = new Cloudflare({ maxRetries: 5 });

// Add application-level throttling
import pLimit from 'p-limit';
const limit = pLimit(10); // Max 10 concurrent requests
```

