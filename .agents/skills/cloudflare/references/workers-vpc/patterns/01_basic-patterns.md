## Basic Patterns

### Simple Request-Response

```typescript
const socket = connect({ hostname: "echo.example.com", port: 7 }, { secureTransport: "on" });
try {
  await socket.opened;
  const writer = socket.writable.getWriter();
  await writer.write(new TextEncoder().encode("Hello\n"));
  await writer.close();
  
  const reader = socket.readable.getReader();
  const { value } = await reader.read();
  return new Response(value);
} finally {
  await socket.close();
}
```

### Reading All Data

```typescript
async function readAll(socket: Socket): Promise<Uint8Array> {
  const reader = socket.readable.getReader();
  const chunks: Uint8Array[] = [];
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    chunks.push(value);
  }
  const total = chunks.reduce((sum, c) => sum + c.length, 0);
  const result = new Uint8Array(total);
  let offset = 0;
  for (const chunk of chunks) { result.set(chunk, offset); offset += chunk.length; }
  return result;
}
```

### Streaming Response

```typescript
// Stream socket data directly to HTTP response
const socket = connect({ hostname: "stream.internal", port: 9000 }, { secureTransport: "on" });
const writer = socket.writable.getWriter();
await writer.write(new TextEncoder().encode("STREAM\n"));
await writer.close();
return new Response(socket.readable);
```

