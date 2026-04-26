## Purging and Cache Management

### Purge by URL (Instant)

```typescript
// Purge specific URL from Cache Reserve immediately
const purgeCacheReserveByURL = async (
  zoneId: string,
  apiToken: string,
  urls: string[]
) => {
  const response = await fetch(
    `https://api.cloudflare.com/client/v4/zones/${zoneId}/purge_cache`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiToken}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ files: urls })
    }
  );
  return await response.json();
};

// Example usage
await purgeCacheReserveByURL('zone123', 'token456', [
  'https://example.com/image.jpg',
  'https://example.com/video.mp4'
]);
```

### Purge by Tag/Host/Prefix (Revalidation)

```typescript
// Purge by cache tag - forces revalidation, not immediate removal
await fetch(
  `https://api.cloudflare.com/client/v4/zones/${zoneId}/purge_cache`,
  {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${apiToken}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ tags: ['tag1', 'tag2'] })
  }
);
```

**Purge behavior:**
- **By URL**: Immediate removal from Cache Reserve + edge cache
- **By tag/host/prefix**: Revalidation only, assets remain in storage (costs continue)

### Clear All Cache Reserve Data

```typescript
// Requires Cache Reserve OFF first
await fetch(
  `https://api.cloudflare.com/client/v4/zones/${zoneId}/cache/cache_reserve_clear`,
  { method: 'POST', headers: { 'Authorization': `Bearer ${apiToken}` } }
);

// Check status: GET same endpoint returns { state: "In-progress" | "Completed" }
```

**Process**: Disable Cache Reserve → Call clear endpoint → Wait up to 24hr → Re-enable

