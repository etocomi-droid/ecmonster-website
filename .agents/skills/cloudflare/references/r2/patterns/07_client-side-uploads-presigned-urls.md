## Client-Side Uploads (Presigned URLs)

```typescript
import { S3Client } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';
import { PutObjectCommand } from '@aws-sdk/client-s3';

// Worker: Generate presigned upload URL
const s3 = new S3Client({
  region: 'auto',
  endpoint: `https://${env.ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: { accessKeyId: env.R2_ACCESS_KEY_ID, secretAccessKey: env.R2_SECRET_ACCESS_KEY }
});

const url = await getSignedUrl(s3, new PutObjectCommand({ Bucket: 'my-bucket', Key: key }), { expiresIn: 3600 });
return Response.json({ uploadUrl: url });

// Client: Upload directly
const { uploadUrl } = await fetch('/api/upload-url').then(r => r.json());
await fetch(uploadUrl, { method: 'PUT', body: file });
```

