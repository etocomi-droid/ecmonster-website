## Checksum Limits

Only ONE checksum algorithm allowed per PUT:

```typescript
// ❌ WRONG: Multiple checksums
await env.MY_BUCKET.put(key, data, { md5: hash1, sha256: hash2 }); // Error

// ✅ CORRECT: Pick one
await env.MY_BUCKET.put(key, data, { sha256: hash });
```

