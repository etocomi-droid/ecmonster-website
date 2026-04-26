## Video State Polling

```typescript
async function waitForVideoReady(client: Cloudflare, accountId: string, videoId: string) {
  for (let i = 0; i < 60; i++) {
    const video = await client.stream.videos.get(videoId, { account_id: accountId });
    if (video.readyToStream || video.status.state === 'error') return video;
    await new Promise(resolve => setTimeout(resolve, 5000));
  }
  throw new Error('Video processing timeout');
}
```

