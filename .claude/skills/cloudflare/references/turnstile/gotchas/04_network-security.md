## Network & Security

### CSP Blocking
**Problem:** Content Security Policy blocks script/iframe.

**Solution:** Add CSP directives.
```html
<meta http-equiv="Content-Security-Policy" 
      content="script-src 'self' https://challenges.cloudflare.com; 
               frame-src https://challenges.cloudflare.com;">
```

### IP Address Forwarding
**Problem:** Server receives proxy IP instead of client IP.

**Solution:** Use correct header.
```javascript
// Cloudflare Workers
const ip = request.headers.get('CF-Connecting-IP');

// Behind proxy
const ip = request.headers.get('X-Forwarded-For')?.split(',')[0];
```

### CORS (Siteverify)
**Problem:** CORS error calling siteverify from browser.

**Solution:** Never call siteverify client-side. Call your backend, backend calls siteverify.

