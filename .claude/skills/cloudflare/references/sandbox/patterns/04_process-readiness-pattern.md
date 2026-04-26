## Process Readiness Pattern

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const sandbox = getSandbox(env.Sandbox, 'app-server');
    
    // Start server
    const process = await sandbox.startProcess(
      'node server.js',
      { processId: 'server' }
    );
    
    // Wait for server to be ready
    await process.waitForPort(8080);  // Wait for port listening
    
    // Now safe to expose
    const { url } = await sandbox.exposePort(8080);
    return Response.json({ url });
  }
};
```

