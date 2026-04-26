## Crypto

```javascript
crypto.randomUUID();                 // UUID v4
crypto.getRandomValues(new Uint8Array(16));

// SHA-256 hash
const hash = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(data));
```

