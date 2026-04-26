## Error Handling

```typescript
try {
  const zone = await client.zones.get({ zone_id: 'xxx' });
} catch (err) {
  if (err instanceof Cloudflare.NotFoundError) {
    // 404
  } else if (err instanceof Cloudflare.RateLimitError) {
    // 429 - SDK auto-retries with backoff
  } else if (err instanceof Cloudflare.APIError) {
    console.log(err.status, err.message);
  }
}
```

**Common Error Types:**
- `AuthenticationError` (401) - Invalid token
- `PermissionDeniedError` (403) - Insufficient scope
- `NotFoundError` (404) - Resource not found
- `RateLimitError` (429) - Rate limit exceeded
- `InternalServerError` (≥500) - Cloudflare error

