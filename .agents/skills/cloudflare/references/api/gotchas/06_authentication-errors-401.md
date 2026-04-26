## Authentication Errors (401)

**Problem:** "Authentication failed" or "Invalid token"

**Causes:**
- Token expired
- Token deleted/revoked
- Token not set in environment
- Wrong token format

**Solution:**

```typescript
// Verify token is set
if (!process.env.CLOUDFLARE_API_TOKEN) {
  throw new Error('CLOUDFLARE_API_TOKEN not set');
}

// Test token
const user = await client.user.tokens.verify();
console.log('Token valid:', user.status);
```

