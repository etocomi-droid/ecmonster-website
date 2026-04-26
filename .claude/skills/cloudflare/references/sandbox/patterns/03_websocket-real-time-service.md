## WebSocket Real-Time Service

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const proxyResponse = await proxyToSandbox(request, env);
    if (proxyResponse) return proxyResponse;

    if (request.headers.get('Upgrade')?.toLowerCase() === 'websocket') {
      const sandbox = getSandbox(env.Sandbox, 'realtime-service');
      return await sandbox.wsConnect(request, 8080);
    }

    // Non-WebSocket: expose preview URL
    const sandbox = getSandbox(env.Sandbox, 'realtime-service');
    const { url } = await sandbox.exposePort(8080, {
      hostname: new URL(request.url).hostname
    });
    return Response.json({ wsUrl: url.replace('https', 'wss') });
  }
};
```

**Dockerfile**:
```dockerfile
FROM docker.io/cloudflare/sandbox:latest
RUN npm install -g ws
EXPOSE 8080
```

