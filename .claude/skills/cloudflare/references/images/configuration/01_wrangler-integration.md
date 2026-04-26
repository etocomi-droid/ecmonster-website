## Wrangler Integration

### Workers Binding Setup

Add to `wrangler.toml`:

```toml
name = "my-image-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"

[images]
binding = "IMAGES"
```

Access in Worker:

```typescript
interface Env {
  IMAGES: ImageBinding;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    return await env.IMAGES
      .input(imageBuffer)
      .transform({ width: 800 })
      .output()
      .response();
  }
};
```

### Upload via Script

Wrangler doesn't have built-in Images commands, use REST API:

```typescript
// scripts/upload-image.ts
import fs from 'fs';
import FormData from 'form-data';

async function uploadImage(filePath: string) {
  const accountId = process.env.CLOUDFLARE_ACCOUNT_ID!;
  const apiToken = process.env.CLOUDFLARE_API_TOKEN!;
  
  const formData = new FormData();
  formData.append('file', fs.createReadStream(filePath));
  
  const response = await fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/images/v1`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiToken}`,
      },
      body: formData,
    }
  );
  
  const result = await response.json();
  console.log('Uploaded:', result);
}

uploadImage('./photo.jpg');
```

### Environment Variables

Store account hash for URL construction:

```toml
[vars]
IMAGES_ACCOUNT_HASH = "your-account-hash"
ACCOUNT_ID = "your-account-id"
```

Access in Worker:

```typescript
const imageUrl = `https://imagedelivery.net/${env.IMAGES_ACCOUNT_HASH}/${imageId}/public`;
```

