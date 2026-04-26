## Signed URLs

For private images, enable signed URLs:

```bash
# Upload with signed URLs required
curl -X POST \
  https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1 \
  -H "Authorization: Bearer {api_token}" \
  -F file=@private.jpg \
  -F requireSignedURLs=true
```

Generate signed URL:

```typescript
import { createHmac } from 'crypto';

function signUrl(imageId: string, variant: string, expiry: number, key: string): string {
  const path = `/${imageId}/${variant}`;
  const toSign = `${path}${expiry}`;
  const signature = createHmac('sha256', key)
    .update(toSign)
    .digest('hex');
  
  return `https://imagedelivery.net/{hash}${path}?exp=${expiry}&sig=${signature}`;
}

// Sign URL valid for 1 hour
const signedUrl = signUrl('image-id', 'public', Date.now() + 3600, env.SIGNING_KEY);
```

