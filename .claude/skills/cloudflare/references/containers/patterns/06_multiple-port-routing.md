## Multiple Port Routing

```typescript
export class MultiPortContainer extends Container {
  requiredPorts = [8080, 8081, 9090];

  async fetch(request: Request) {
    const path = new URL(request.url).pathname;
    if (path.startsWith("/grpc")) this.switchPort(8081);
    else if (path.startsWith("/metrics")) this.switchPort(9090);
    return super.fetch(request);
  }
}
```

**Use:** Multi-protocol services (HTTP + gRPC), separate metrics endpoints.

