## Self-Sign JWT (High Volume Tokens)

For >1k tokens/day. Prerequisites: Create signing key (see configuration.md).

```typescript
async function selfSignToken(keyId: string, jwkBase64: string, videoId: string, expiresIn = 3600) {
  const key = await crypto.subtle.importKey(
    'jwk', JSON.parse(atob(jwkBase64)), { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['sign']
  );
  const now = Math.floor(Date.now() / 1000);
  const header = btoa(JSON.stringify({ alg: 'RS256', kid: keyId })).replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
  const payload = btoa(JSON.stringify({ sub: videoId, kid: keyId, exp: now + expiresIn, nbf: now }))
    .replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
  const message = `${header}.${payload}`;
  const sig = await crypto.subtle.sign('RSASSA-PKCS1-v1_5', key, new TextEncoder().encode(message));
  const b64Sig = btoa(String.fromCharCode(...new Uint8Array(sig))).replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
  return `${message}.${b64Sig}`;
}

// With access rules (geo-restriction)
const payloadWithRules = {
  sub: videoId, kid: keyId, exp: now + 3600, nbf: now,
  accessRules: [{ type: 'ip.geoip.country', action: 'allow', country: ['US'] }]
};
```

