## Protocol Examples

### Redis RESP

```typescript
// Send: *2\r\n$3\r\nGET\r\n$<keylen>\r\n<key>\r\n
// Recv: $<len>\r\n<data>\r\n or $-1\r\n for null
const socket = connect({ hostname: "redis.internal", port: 6379 });
const writer = socket.writable.getWriter();
await writer.write(new TextEncoder().encode(`*2\r\n$3\r\nGET\r\n$3\r\nkey\r\n`));
```

### PostgreSQL

**Use [Hyperdrive](../hyperdrive/) for production.** Raw Postgres protocol is complex (startup, auth, query messages).

### MQTT

```typescript
const socket = connect({ hostname: "mqtt.broker", port: 1883 });
const writer = socket.writable.getWriter();
// CONNECT: 0x10 <len> 0x00 0x04 "MQTT" 0x04 <flags> ...
// PUBLISH: 0x30 <len> <topic_len> <topic> <message>
```

