## Cloudflare Worker Integration

### Worker Binding Types

```typescript
interface Env {
  TURN_KEY_ID: string;
  TURN_KEY_SECRET: string;
  CREDENTIALS_CACHE?: KVNamespace;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // See patterns.md for implementation
  }
}
```

### Basic Worker Example

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (request.url.endsWith('/turn-credentials')) {
      // Validate client auth
      const authHeader = request.headers.get('Authorization');
      if (!authHeader) {
        return new Response('Unauthorized', { status: 401 });
      }

      const response = await fetch(
        `https://rtc.live.cloudflare.com/v1/turn/keys/${env.TURN_KEY_ID}/credentials/generate`,
        {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${env.TURN_KEY_SECRET}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ ttl: 3600 })
        }
      );

      if (!response.ok) {
        return new Response('Failed to generate credentials', { status: 500 });
      }

      const data = await response.json();

      // Filter port 53 for browser clients
      const filteredUrls = data.iceServers.urls.filter(
        (url: string) => !url.includes(':53')
      );

      return Response.json({
        iceServers: [
          { urls: 'stun:stun.cloudflare.com:3478' },
          {
            urls: filteredUrls,
            username: data.iceServers.username,
            credential: data.iceServers.credential
          }
        ]
      });
    }

    return new Response('Not found', { status: 404 });
  }
};
```

