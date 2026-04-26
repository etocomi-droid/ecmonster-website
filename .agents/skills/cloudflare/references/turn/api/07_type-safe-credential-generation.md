## Type-Safe Credential Generation

```typescript
async function fetchTURNServers(
  config: CloudflareTURNConfig
): Promise<RTCIceServer[]> {
  // Validate TTL constraint
  const ttl = config.ttl ?? 3600;
  if (ttl > 172800) {
    throw new Error('TTL cannot exceed 172800 seconds (48 hours)');
  }

  const response = await fetch(
    `https://rtc.live.cloudflare.com/v1/turn/keys/${config.keyId}/credentials/generate`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${config.keySecret}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ ttl })
    }
  );

  if (!response.ok) {
    throw new Error(`TURN credential generation failed: ${response.status}`);
  }

  const data = await response.json();
  
  // Filter port 53 for browser clients
  const filteredUrls = data.iceServers.urls.filter(
    (url: string) => !url.includes(':53')
  );

  const iceServers = [
    { urls: 'stun:stun.cloudflare.com:3478' },
    {
      urls: filteredUrls,
      username: data.iceServers.username,
      credential: data.iceServers.credential,
      credentialType: 'password' as const
    }
  ];

  // Validate before returning
  if (!iceServers.every(validateRTCIceServer)) {
    throw new Error('Invalid ICE server configuration received');
  }

  return iceServers;
}
```

