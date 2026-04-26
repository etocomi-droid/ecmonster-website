## Upload APIs

### Direct Creator Upload (Recommended)

**Backend: Create upload URL (SDK)**
```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({ apiToken: env.CF_API_TOKEN });

const uploadData = await client.stream.directUpload.create({
  account_id: env.CF_ACCOUNT_ID,
  maxDurationSeconds: 3600,
  requireSignedURLs: true,
  meta: { creator: 'user-123' }
});
// Returns: { uploadURL: string, uid: string }
```

**Frontend: Upload file**
```typescript
async function uploadVideo(file: File, uploadURL: string) {
  const formData = new FormData();
  formData.append('file', file);
  return fetch(uploadURL, { method: 'POST', body: formData }).then(r => r.json());
}
```

### Upload from URL

```typescript
const video = await client.stream.copy.create({
  account_id: env.CF_ACCOUNT_ID,
  url: 'https://example.com/video.mp4',
  meta: { name: 'My Video' },
  requireSignedURLs: false
});
```

