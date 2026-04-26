## Complete Example

```typescript
import { connect } from 'cloudflare:sockets';

export default {
  async fetch(req: Request): Promise<Response> {
    const socket = connect({ hostname: "echo.example.com", port: 7 }, { secureTransport: "on" });

    try {
      await socket.opened;
      
      const writer = socket.writable.getWriter();
      await writer.write(new TextEncoder().encode("Hello, TCP!\n"));
      await writer.close();

      const reader = socket.readable.getReader();
      const { value } = await reader.read();
      
      return new Response(value);
    } finally {
      await socket.close();
    }
  }
};
```

See [patterns.md](./patterns.md) for multi-chunk reading, error handling, and protocol implementations.

