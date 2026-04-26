## Security Patterns

### Destination Allowlist (Prevent SSRF)

```typescript
const ALLOWED_HOSTS = ['db.internal.company.net', 'api.internal.company.net', /^10\.0\.1\.\d+$/];

function isAllowed(hostname: string): boolean {
  return ALLOWED_HOSTS.some(p => p instanceof RegExp ? p.test(hostname) : p === hostname);
}

export default {
  async fetch(req: Request): Promise<Response> {
    const target = new URL(req.url).searchParams.get('host');
    if (!target || !isAllowed(target)) return new Response('Forbidden', { status: 403 });
    const socket = connect({ hostname: target, port: 443 });
    // Use socket...
  }
};
```

### Connection Pooling

```typescript
class SocketPool {
  private pool = new Map<string, Socket[]>();
  
  async acquire(hostname: string, port: number): Promise<Socket> {
    const key = `${hostname}:${port}`;
    const sockets = this.pool.get(key) || [];
    if (sockets.length > 0) return sockets.pop()!;
    const socket = connect({ hostname, port }, { secureTransport: "on" });
    await socket.opened;
    return socket;
  }
  
  release(hostname: string, port: number, socket: Socket): void {
    const key = `${hostname}:${port}`;
    const sockets = this.pool.get(key) || [];
    if (sockets.length < 3) { sockets.push(socket); this.pool.set(key, sockets); }
    else socket.close();
  }
}
```

