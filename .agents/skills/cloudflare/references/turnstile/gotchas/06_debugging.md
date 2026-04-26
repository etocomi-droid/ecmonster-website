## Debugging

### Console Logging
```javascript
window.turnstile.render('#container', {
  sitekey: 'YOUR_SITE_KEY',
  callback: (token) => console.log('✓ Token:', token),
  'error-callback': (code) => console.error('✗ Error:', code),
  'expired-callback': () => console.warn('⏱ Expired'),
  'timeout-callback': () => console.warn('⏱ Timeout')
});
```

### Check Token State
```javascript
const token = window.turnstile.getResponse(widgetId);
console.log('Token:', token || 'NOT READY');
console.log('Expired:', window.turnstile.isExpired(widgetId));
```

### Test Keys (Use First)
Always develop with test keys before production:
- Site: `1x00000000000000000000AA`
- Secret: `1x0000000000000000000000000000000AA`

### Network Tab
- Verify `api.js` loads (200 OK)
- Check siteverify request/response
- Look for 4xx/5xx errors

