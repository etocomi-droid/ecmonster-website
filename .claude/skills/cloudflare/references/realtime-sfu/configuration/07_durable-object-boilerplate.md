## Durable Object Boilerplate

Minimal presence system:

```typescript
export class Room {
  private sessions = new Map<string, {userId: string, tracks: string[]}>();

  async fetch(req: Request) {
    const {pathname} = new URL(req.url);
    const body = await req.json();
    
    if (pathname === '/join') {
      this.sessions.set(body.sessionId, {userId: body.userId, tracks: []});
      return Response.json({participants: this.sessions.size});
    }
    
    if (pathname === '/publish') {
      this.sessions.get(body.sessionId)?.tracks.push(...body.tracks);
      // Broadcast to others via WebSocket (not shown)
      return new Response('OK');
    }
    
    return new Response('Not found', {status: 404});
  }
}
```

