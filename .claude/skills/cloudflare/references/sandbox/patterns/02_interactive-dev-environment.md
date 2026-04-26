## Interactive Dev Environment

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const proxyResponse = await proxyToSandbox(request, env);
    if (proxyResponse) return proxyResponse;
    
    const sandbox = getSandbox(env.Sandbox, 'ide', { normalizeId: true });
    
    if (request.url.endsWith('/start')) {
      await sandbox.exec('curl -fsSL https://code-server.dev/install.sh | sh');
      await sandbox.startProcess('code-server --bind-addr 0.0.0.0:8080', {
        processId: 'vscode'
      });
      
      const exposed = await sandbox.exposePort(8080);
      return Response.json({ url: exposed.url });
    }
    
    return new Response('Try /start');
  }
};
```

