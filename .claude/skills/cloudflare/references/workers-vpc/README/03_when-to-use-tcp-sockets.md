## When to Use TCP Sockets

**Use TCP Sockets when you need:**
- ✅ Direct control over wire protocols (e.g., Postgres wire protocol, SSH, Redis RESP)
- ✅ Non-HTTP protocols (MQTT, SMTP, custom binary protocols)
- ✅ StartTLS or custom TLS negotiation
- ✅ Streaming binary data over TCP

**Don't use TCP Sockets when:**
- ❌ You just need HTTP/HTTPS (use `fetch()` or VPC Services)
- ❌ You need PostgreSQL/MySQL (use Hyperdrive for pooling)
- ❌ You need WebSocket (use native Workers WebSocket)

