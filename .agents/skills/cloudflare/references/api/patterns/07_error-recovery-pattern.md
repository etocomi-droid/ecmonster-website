## Error Recovery Pattern

```typescript
async function createZoneWithRetry(name: string, maxAttempts = 3) {
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await client.zones.create({
        account: { id: 'account-id' },
        name,
        type: 'full',
      });
    } catch (err) {
      if (err instanceof Cloudflare.RateLimitError && attempt < maxAttempts) {
        const retryAfter = parseInt(err.headers['retry-after'] || '5');
        console.log(`Rate limited, waiting ${retryAfter}s (retry ${attempt}/${maxAttempts})`);
        await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
      } else {
        throw err;
      }
    }
  }
}
```

