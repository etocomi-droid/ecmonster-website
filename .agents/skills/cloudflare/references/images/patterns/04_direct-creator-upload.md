## Direct Creator Upload

```typescript
// Backend: Generate upload URL
const response = await fetch(
  `https://api.cloudflare.com/client/v4/accounts/${env.ACCOUNT_ID}/images/v2/direct_upload`,
  { method: 'POST', headers: { 'Authorization': `Bearer ${env.API_TOKEN}` },
    body: JSON.stringify({ requireSignedURLs: false, metadata: { userId } }) }
);

// Frontend: Upload to returned uploadURL
const formData = new FormData();
formData.append('file', file);
await fetch(result.uploadURL, { method: 'POST', body: formData });
// Use: https://imagedelivery.net/{hash}/${result.id}/public
```

