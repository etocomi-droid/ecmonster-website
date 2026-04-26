## S3 SDK Setup

```typescript
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

const s3 = new S3Client({
  region: 'auto',
  endpoint: `https://${accountId}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: env.R2_ACCESS_KEY_ID,
    secretAccessKey: env.R2_SECRET_ACCESS_KEY
  }
});

await s3.send(new PutObjectCommand({
  Bucket: 'my-bucket',
  Key: 'file.txt',
  Body: data,
  StorageClass: 'STANDARD' // or 'STANDARD_IA'
}));
```

