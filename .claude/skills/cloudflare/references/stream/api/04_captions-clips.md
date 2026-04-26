## Captions & Clips

### Upload Captions

```typescript
async function uploadCaption(
  accountId: string, videoId: string, apiToken: string,
  language: string, captionFile: File
) {
  const formData = new FormData();
  formData.append('file', captionFile);
  return fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/stream/${videoId}/captions/${language}`,
    {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${apiToken}` },
      body: formData
    }
  ).then(r => r.json());
}
```

### Generate AI Captions

```typescript
// TODO: Requires Workers AI integration - see workers-ai reference
async function generateAICaptions(accountId: string, videoId: string, apiToken: string) {
  return fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/stream/${videoId}/captions/generate`,
    {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${apiToken}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ language: 'en' })
    }
  ).then(r => r.json());
}
```

### Clip Video

```typescript
async function clipVideo(
  accountId: string, videoId: string, apiToken: string,
  startTime: number, endTime: number
) {
  return fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/stream/clip`,
    {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${apiToken}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        clippedFromVideoUID: videoId,
        startTimeSeconds: startTime,
        endTimeSeconds: endTime
      })
    }
  ).then(r => r.json());
}
```

