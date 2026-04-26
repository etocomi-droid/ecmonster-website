## Misconfigurations

### Wrong Key Pairing
**Problem:** Site key from one widget, secret from another.

**Solution:** Verify site key and secret are from same widget in dashboard.

### Test Keys in Production
**Problem:** Using test keys in production.

**Solution:** Environment-based keys.
```javascript
const SITE_KEY = process.env.NODE_ENV === 'production'
  ? process.env.TURNSTILE_SITE_KEY
  : '1x00000000000000000000AA';
```

### Missing Environment Variables
**Problem:** Secret undefined on server.

**Solution:** Check .env and verify loading.
```bash
# .env
TURNSTILE_SECRET=your_secret_here

# Verify
console.log('Secret loaded:', !!process.env.TURNSTILE_SECRET);
```

