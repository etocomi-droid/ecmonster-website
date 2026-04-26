## Timeout Configuration

**When to increase:**
- Large zone transfers
- Bulk DNS operations
- Worker script uploads

```typescript
const client = new Cloudflare({
  timeout: 300000, // 5 minutes
});
```

