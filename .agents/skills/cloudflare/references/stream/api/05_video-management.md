## Video Management

```typescript
// List videos
const videos = await client.stream.videos.list({
  account_id: env.CF_ACCOUNT_ID,
  search: 'keyword' // optional
});

// Get video details
const video = await client.stream.videos.get(videoId, {
  account_id: env.CF_ACCOUNT_ID
});

// Update video
await client.stream.videos.update(videoId, {
  account_id: env.CF_ACCOUNT_ID,
  meta: { title: 'New Title' },
  requireSignedURLs: true
});

// Delete video
await client.stream.videos.delete(videoId, {
  account_id: env.CF_ACCOUNT_ID
});
```

