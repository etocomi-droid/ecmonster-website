## Backend Integration

### Token Generation (Workers)
```typescript
export interface Env { CLOUDFLARE_API_TOKEN: string; CLOUDFLARE_ACCOUNT_ID: string; REALTIMEKIT_APP_ID: string; }

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    
    if (url.pathname === '/api/join-meeting') {
      const { meetingId, userName, presetName } = await request.json();
      const response = await fetch(
        `https://api.cloudflare.com/client/v4/accounts/${env.CLOUDFLARE_ACCOUNT_ID}/realtime/kit/${env.REALTIMEKIT_APP_ID}/meetings/${meetingId}/participants`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${env.CLOUDFLARE_API_TOKEN}` },
          body: JSON.stringify({ name: userName, preset_name: presetName })
        }
      );
      const data = await response.json();
      return Response.json({ authToken: data.result.authToken });
    }
    
    return new Response('Not found', { status: 404 });
  }
};
```

