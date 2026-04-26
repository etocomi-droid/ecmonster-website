## Critical Rules

### ❌ Skipping Server-Side Validation
**Problem:** Client-only validation is easily bypassed.

**Solution:** Always validate on server.
```javascript
// CORRECT - Server validates token
app.post('/submit', async (req, res) => {
  const token = req.body['cf-turnstile-response'];
  const validation = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
    method: 'POST',
    body: JSON.stringify({ secret: SECRET, response: token })
  }).then(r => r.json());
  
  if (!validation.success) return res.status(403).json({ error: 'CAPTCHA failed' });
});
```

### ❌ Exposing Secret Key
**Problem:** Secret key leaked in client-side code.

**Solution:** Server-side validation only. Never send secret to client.

### ❌ Reusing Tokens (Single-Use Rule)
**Problem:** Tokens are single-use. Revalidation fails with `timeout-or-duplicate`.

**Solution:** Generate new token for each submission. Reset widget on error.
```javascript
if (!response.ok) window.turnstile.reset(widgetId);
```

### ❌ Not Handling Token Expiry
**Problem:** Tokens expire after 5 minutes.

**Solution:** Handle expiry callback or use auto-refresh.
```javascript
window.turnstile.render('#container', {
  sitekey: 'YOUR_SITE_KEY',
  'refresh-expired': 'auto', // or 'manual' with expired-callback
  'expired-callback': () => window.turnstile.reset(widgetId)
});
```

