## Credentials Caching Pattern

```typescript
class TURNCredentialsManager {
  private creds: { username: string; credential: string; urls: string[]; expiresAt: number; } | null = null;

  async getCredentials(keyId: string, keySecret: string): Promise<RTCIceServer[]> {
    const now = Date.now();
    
    if (this.creds && this.creds.expiresAt > now) {
      return this.buildIceServers(this.creds);
    }

    const ttl = 3600;
    if (ttl > 172800) throw new Error('TTL max 48hrs');

    const res = await fetch(
      `https://rtc.live.cloudflare.com/v1/turn/keys/${keyId}/credentials/generate`,
      {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${keySecret}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({ ttl })
      }
    );

    const data = await res.json();
    const filteredUrls = data.iceServers.urls.filter((url: string) => !url.includes(':53'));

    this.creds = {
      username: data.iceServers.username,
      credential: data.iceServers.credential,
      urls: filteredUrls,
      expiresAt: now + (ttl * 1000) - 60000
    };

    return this.buildIceServers(this.creds);
  }

  private buildIceServers(c: { username: string; credential: string; urls: string[] }): RTCIceServer[] {
    return [
      { urls: 'stun:stun.cloudflare.com:3478' },
      { urls: c.urls, username: c.username, credential: c.credential, credentialType: 'password' as const }
    ];
  }
}
```

