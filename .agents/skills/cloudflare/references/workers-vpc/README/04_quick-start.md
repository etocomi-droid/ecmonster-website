## Quick Start

```typescript
import { connect } from 'cloudflare:sockets';

export default {
  async fetch(req: Request): Promise<Response> {
    // Connect to private service
    const socket = connect(
      { hostname: "db.internal.company.net", port: 5432 },
      { secureTransport: "on" }
    );

    try {
      await socket.opened; // Wait for connection
      
      const writer = socket.writable.getWriter();
      await writer.write(new TextEncoder().encode("QUERY\r\n"));
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

