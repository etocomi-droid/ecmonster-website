## Workers Integration

### Access JWT Claims
```js
export default {
  async fetch(req, env) {
    // Access validated JWT payload
    const jwt = req.cf?.jwt?.payload?.[env.JWT_CONFIG_ID]?.[0];
    if (jwt) {
      const userId = jwt.sub;
      const role = jwt.role;
    }
  }
}
```

### Access mTLS Info
```js
export default {
  async fetch(req, env) {
    const tls = req.cf?.tlsClientAuth;
    if (tls?.certVerified === 'SUCCESS') {
      const fingerprint = tls.certFingerprintSHA256;
      // Authenticated client
    }
  }
}
```

### Dynamic JWKS Update
```js
export default {
  async scheduled(event, env) {
    const jwks = await (await fetch('https://auth.example.com/.well-known/jwks.json')).json();
    await fetch(`https://api.cloudflare.com/client/v4/zones/${env.ZONE_ID}/api_gateway/token_validation/${env.CONFIG_ID}`, {
      method: 'PATCH',
      headers: {'Authorization': `Bearer ${env.CF_API_TOKEN}`, 'Content-Type': 'application/json'},
      body: JSON.stringify({jwks: JSON.stringify(jwks)})
    });
  }
}
```

