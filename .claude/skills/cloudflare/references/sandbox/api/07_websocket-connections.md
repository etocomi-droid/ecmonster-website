## WebSocket Connections

```typescript
// Proxy WebSocket to sandbox service
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const proxyResponse = await proxyToSandbox(request, env);
    if (proxyResponse) return proxyResponse;

    if (request.headers.get('Upgrade')?.toLowerCase() === 'websocket') {
      const sandbox = getSandbox(env.Sandbox, 'realtime');
      return await sandbox.wsConnect(request, 8080);
    }
    
    return new Response('Not a WebSocket request', { status: 400 });
  }
};
```

