## Connection String Patterns

Parse connection strings to extract host and port:

```typescript
function parseConnectionString(connStr: string): SocketAddress {
  const url = new URL(connStr); // e.g., "postgres://10.0.1.50:5432/mydb"
  return { hostname: url.hostname, port: parseInt(url.port) || 5432 };
}
```

