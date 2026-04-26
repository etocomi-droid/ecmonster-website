## Multi-Protocol Gateway

```typescript
interface Protocol { name: string; defaultPort: number; test(host: string, port: number): Promise<string>; }

const PROTOCOLS: Record<string, Protocol> = {
  redis: {
    name: 'redis',
    defaultPort: 6379,
    async test(host, port) {
      const socket = connect({ hostname: host, port });
      try {
        const writer = socket.writable.getWriter();
        await writer.write(new TextEncoder().encode('*1\r\n$4\r\nPING\r\n'));
        writer.releaseLock();
        const reader = socket.readable.getReader();
        const { value } = await reader.read();
        return new TextDecoder().decode(value || new Uint8Array());
      } finally { await socket.close(); }
    }
  }
};

export default {
  async fetch(req: Request): Promise<Response> {
    const url = new URL(req.url);
    const proto = url.pathname.slice(1);  // /redis
    const host = url.searchParams.get('host');
    if (!host || !PROTOCOLS[proto]) return new Response('Invalid', { status: 400 });
    const result = await PROTOCOLS[proto].test(host, parseInt(url.searchParams.get('port') || '') || PROTOCOLS[proto].defaultPort);
    return new Response(result);
  }
};
```


