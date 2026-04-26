## Best Practices

**Security:**
- Never commit tokens
- Use minimal permissions
- Rotate tokens regularly
- Set token expiration

**Performance:**
- Batch operations
- Use pagination wisely
- Cache responses
- Handle rate limits

**Code Organization:**

```typescript
// Create reusable client instance
export const cfClient = new Cloudflare({
  apiToken: process.env.CLOUDFLARE_API_TOKEN,
  maxRetries: 5,
});

// Wrap common operations
export async function getZoneDetails(zoneId: string) {
  return await cfClient.zones.get({ zone_id: zoneId });
}
```

