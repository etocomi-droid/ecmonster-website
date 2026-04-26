## Core Function: `connect()`

```typescript
function connect(
  address: SocketAddress,
  options?: SocketOptions
): Socket
```

Creates an outbound TCP connection to the specified address.

### Parameters

#### `SocketAddress`

```typescript
interface SocketAddress {
  hostname: string; // DNS hostname or IP address
  port: number;     // TCP port (1-65535, excluding blocked ports)
}
```

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `hostname` | `string` | Target hostname or IP | `"db.internal.net"`, `"10.0.1.50"` |
| `port` | `number` | TCP port number | `5432`, `443`, `22` |

DNS names are resolved at connection time. IPv4, IPv6, and private IPs (10.x, 172.16.x, 192.168.x) supported.

#### `SocketOptions`

```typescript
interface SocketOptions {
  secureTransport?: "off" | "on" | "starttls";
  allowHalfOpen?: boolean;
}
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `secureTransport` | `"off" \| "on" \| "starttls"` | `"off"` | TLS mode |
| `allowHalfOpen` | `boolean` | `false` | Allow half-closed connections |

**`secureTransport` modes:**

| Mode | Behavior | Use Case |
|------|----------|----------|
| `"off"` | Plain TCP, no encryption | Testing, internal trusted networks |
| `"on"` | Immediate TLS handshake | HTTPS, secure databases, SSH |
| `"starttls"` | Start plain, upgrade later with `startTls()` | Postgres, SMTP, IMAP |

**`allowHalfOpen`:** When `false` (default), closing read stream auto-closes write stream. When `true`, streams are independent.

### Returns

A `Socket` object with readable/writable streams.

