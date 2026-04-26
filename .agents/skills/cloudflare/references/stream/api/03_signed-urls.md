## Signed URLs

```typescript
// Low volume (<1k/day): Use API
async function getSignedToken(accountId: string, videoId: string, apiToken: string) {
  const response = await fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/stream/${videoId}/token`,
    {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${apiToken}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        exp: Math.floor(Date.now() / 1000) + 3600,
        accessRules: [{ type: 'ip.geoip.country', action: 'allow', country: ['US'] }]
      })
    }
  );
  return (await response.json()).result.token;
}

// High volume: Self-sign with RS256 JWT (see "Self-Sign JWT" in patterns.md)
```

