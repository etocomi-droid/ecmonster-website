## Communication

### fetch() - HTTP with WebSocket support

```typescript
// ✅ Supports WebSocket upgrades
const response = await container.fetch(request);
const response = await container.fetch("http://container/api", {
  method: "POST",
  body: JSON.stringify({ data: "value" })
});
```

**Use for:** All HTTP, especially WebSocket.

### containerFetch() - HTTP only (no WebSocket)

```typescript
// ❌ No WebSocket support
const response = await container.containerFetch(request);
```

**⚠️ Critical:** Use `fetch()` for WebSocket, not `containerFetch()`.

### TCP Connections

```typescript
const port = this.ctx.container.getTcpPort(8080);
const conn = port.connect();
await conn.opened;

if (request.body) await request.body.pipeTo(conn.writable);
return new Response(conn.readable);
```

### switchPort() - Change default port

```typescript
this.switchPort(8081);  // Subsequent fetch() uses this port
```

