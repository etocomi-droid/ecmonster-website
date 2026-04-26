## Retry with Exponential Backoff

```typescript
async function fetchWithRetry(url: string, options: RequestInit, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const res = await fetch(url, options);
      if (res.ok) return res;
      if (res.status >= 500) throw new Error('Server error');
      return res; // Client error, don't retry
    } catch (err) {
      if (i === maxRetries - 1) throw err;
      const delay = Math.min(1000 * 2 ** i, 10000); // Cap at 10s
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}
```

