## Key Validation

```typescript
// ❌ DANGEROUS: Path traversal
const key = url.pathname.slice(1); // Could be ../../../etc/passwd
await env.MY_BUCKET.get(key);

// ✅ SAFE: Validate keys
if (!key || key.includes('..') || key.startsWith('/')) {
  return new Response('Invalid key', { status: 400 });
}
```

