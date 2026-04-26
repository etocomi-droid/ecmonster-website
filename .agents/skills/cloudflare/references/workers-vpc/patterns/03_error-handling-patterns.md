## Error Handling Patterns

### Retry with Backoff

```typescript
async function connectWithRetry(addr: SocketAddress, opts: SocketOptions, maxRetries = 3): Promise<Socket> {
  for (let i = 1; i <= maxRetries; i++) {
    try {
      const socket = connect(addr, opts);
      await socket.opened;
      return socket;
    } catch (error) {
      if (i === maxRetries) throw error;
      await new Promise(r => setTimeout(r, 1000 * Math.pow(2, i - 1))); // Exponential backoff
    }
  }
  throw new Error('Unreachable');
}
```

### Timeout

```typescript
async function connectWithTimeout(addr: SocketAddress, opts: SocketOptions, ms = 5000): Promise<Socket> {
  const socket = connect(addr, opts);
  const timeout = new Promise<never>((_, reject) => setTimeout(() => reject(new Error('Timeout')), ms));
  await Promise.race([socket.opened, timeout]);
  return socket;
}
```

### Fallback

```typescript
async function connectWithFallback(primary: string, fallback: string, port: number): Promise<Socket> {
  try {
    const socket = connect({ hostname: primary, port }, { secureTransport: "on" });
    await socket.opened;
    return socket;
  } catch {
    return connect({ hostname: fallback, port }, { secureTransport: "on" });
  }
}
```

