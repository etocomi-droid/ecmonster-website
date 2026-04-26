## CORS Configuration

CORS must be configured via S3 SDK or dashboard (not available in Workers API):

```typescript
import { S3Client, PutBucketCorsCommand } from '@aws-sdk/client-s3';

const s3 = new S3Client({
  region: 'auto',
  endpoint: `https://${accountId}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: env.R2_ACCESS_KEY_ID,
    secretAccessKey: env.R2_SECRET_ACCESS_KEY
  }
});

await s3.send(new PutBucketCorsCommand({
  Bucket: 'my-bucket',
  CORSConfiguration: {
    CORSRules: [{
      AllowedOrigins: ['https://example.com'],
      AllowedMethods: ['GET', 'PUT', 'HEAD'],
      AllowedHeaders: ['*'],
      ExposeHeaders: ['ETag'],
      MaxAgeSeconds: 3600
    }]
  }
}));
```

