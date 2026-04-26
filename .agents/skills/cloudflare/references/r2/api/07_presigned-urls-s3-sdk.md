## Presigned URLs (S3 SDK)

```typescript
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

const s3 = new S3Client({
  region: 'auto',
  endpoint: `https://${accountId}.r2.cloudflarestorage.com`,
  credentials: { accessKeyId: env.R2_ACCESS_KEY_ID, secretAccessKey: env.R2_SECRET_ACCESS_KEY }
});

const uploadUrl = await getSignedUrl(s3, new PutObjectCommand({ Bucket: 'my-bucket', Key: key }), { expiresIn: 3600 });
return Response.json({ uploadUrl });
```

