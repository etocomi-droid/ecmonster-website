## Checksum Validation & Storage Transitions

```typescript
// Upload with checksum
const hash = await crypto.subtle.digest('SHA-256', data);
await env.MY_BUCKET.put(key, data, { sha256: hash });

// Transition storage class (requires S3 SDK)
import { S3Client, CopyObjectCommand } from '@aws-sdk/client-s3';
await s3.send(new CopyObjectCommand({
  Bucket: 'my-bucket', Key: key,
  CopySource: `/my-bucket/${key}`,
  StorageClass: 'STANDARD_IA'
}));
```

