## Multipart Uploads

```typescript
const multipart = await env.MY_BUCKET.createMultipartUpload(key, {
  httpMetadata: { contentType: 'video/mp4' }
});

const uploadedParts: R2UploadedPart[] = [];
for (let i = 0; i < partCount; i++) {
  const part = await multipart.uploadPart(i + 1, partData);
  uploadedParts.push(part);
}

const object = await multipart.complete(uploadedParts);
// OR: await multipart.abort();

// Resume
const multipart = env.MY_BUCKET.resumeMultipartUpload(key, uploadId);
```

