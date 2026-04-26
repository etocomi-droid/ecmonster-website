## R2 Multipart Upload

```typescript
// For files > 100MB
const upload = await env.MY_BUCKET.createMultipartUpload('large-file.bin');
try {
  const parts = [];
  for (let i = 0; i < chunks.length; i++) {
    parts.push(await upload.uploadPart(i + 1, chunks[i]));
  }
  await upload.complete(parts);
} catch (err) { await upload.abort(); throw err; }
```

Parallel uploads, resume on failure, handle files > 5GB

