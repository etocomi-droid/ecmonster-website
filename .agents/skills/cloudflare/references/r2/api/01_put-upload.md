## PUT (Upload)

```typescript
// Basic
await env.MY_BUCKET.put(key, value);

// With metadata
await env.MY_BUCKET.put(key, value, {
  httpMetadata: {
    contentType: 'image/jpeg',
    contentDisposition: 'attachment; filename="photo.jpg"',
    cacheControl: 'max-age=3600'
  },
  customMetadata: { userId: '123', version: '2' },
  storageClass: 'Standard', // or 'InfrequentAccess'
  sha256: arrayBufferOrHex, // Integrity check
  ssecKey: arrayBuffer32bytes // SSE-C encryption
});

// Value types: ReadableStream | ArrayBuffer | string | Blob
```

