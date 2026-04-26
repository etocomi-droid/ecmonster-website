## Security & Rate Limiting

```typescript
// Security headers
const security = { 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'DENY' };

// Auth
const auth = request.headers.get('Authorization');
if (!auth?.startsWith('Bearer ')) return new Response('Unauthorized', { status: 401 });

// Gradual rollouts (deterministic user bucketing)
const hash = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(userId));
if (new Uint8Array(hash)[0] % 100 < rolloutPercent) return newFeature(request);
```

Rate limiting: See [Durable Objects](../durable-objects/README.md)

