## Stream Length Requirement

```typescript
// ❌ WRONG: Streaming unknown length fails silently
const response = await fetch(url);
await env.MY_BUCKET.put(key, response.body); // May fail without error

// ✅ CORRECT: Buffer or use Content-Length
const data = await response.arrayBuffer();
await env.MY_BUCKET.put(key, data);

// OR: Pass Content-Length if known
const object = await env.MY_BUCKET.put(key, request.body, {
  httpMetadata: {
    contentLength: parseInt(request.headers.get('content-length') || '0')
  }
});
```

**Reason:** R2 requires known length for streams. Unknown length may cause silent truncation.

