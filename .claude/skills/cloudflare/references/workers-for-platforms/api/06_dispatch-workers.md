## Dispatch Workers

### Subdomain Routing
```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const userWorkerName = new URL(request.url).hostname.split(".")[0];
    const userWorker = env.DISPATCHER.get(userWorkerName);
    return await userWorker.fetch(request);
  },
};
```

### Path Routing
```typescript
const pathParts = new URL(request.url).pathname.split("/").filter(Boolean);
const userWorker = env.DISPATCHER.get(pathParts[0]);
return await userWorker.fetch(request);
```

### KV Routing
```typescript
const hostname = new URL(request.url).hostname;
const userWorkerName = await env.ROUTING_KV.get(hostname);
const userWorker = env.DISPATCHER.get(userWorkerName);
return await userWorker.fetch(request);
```

