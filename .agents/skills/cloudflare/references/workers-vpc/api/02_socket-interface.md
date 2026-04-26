## Socket Interface

```typescript
interface Socket {
  // Streams
  readable: ReadableStream<Uint8Array>;
  writable: WritableStream<Uint8Array>;
  
  // Connection state
  opened: Promise<SocketInfo>;
  closed: Promise<void>;
  
  // Methods
  close(): Promise<void>;
  startTls(): Socket;
}
```

### Properties

#### `readable: ReadableStream<Uint8Array>`

Stream for reading data from the socket. Use `getReader()` to consume data.

```typescript
const reader = socket.readable.getReader();
const { done, value } = await reader.read(); // Read one chunk
```

#### `writable: WritableStream<Uint8Array>`

Stream for writing data to the socket. Use `getWriter()` to send data.

```typescript
const writer = socket.writable.getWriter();
await writer.write(new TextEncoder().encode("HELLO\r\n"));
await writer.close();
```

#### `opened: Promise<SocketInfo>`

Promise that resolves when connection succeeds, rejects on failure.

```typescript
interface SocketInfo {
  remoteAddress?: string; // May be undefined
  localAddress?: string;  // May be undefined
}

try {
  const info = await socket.opened;
} catch (error) {
  // Connection failed
}
```

#### `closed: Promise<void>`

Promise that resolves when socket is fully closed (both directions).

### Methods

#### `close(): Promise<void>`

Closes the socket gracefully, waiting for pending writes to complete.

```typescript
const socket = connect({ hostname: "api.internal", port: 443 });
try {
  // Use socket
} finally {
  await socket.close(); // Always call in finally block
}
```

#### `startTls(): Socket`

Upgrades connection to TLS. Only available when `secureTransport: "starttls"` was specified.

```typescript
const socket = connect(
  { hostname: "db.internal", port: 5432 },
  { secureTransport: "starttls" }
);

// Send protocol-specific StartTLS command
const writer = socket.writable.getWriter();
await writer.write(new TextEncoder().encode("STARTTLS\r\n"));

// Upgrade to TLS - use returned socket, not original
const secureSocket = socket.startTls();
const secureWriter = secureSocket.writable.getWriter();
```

