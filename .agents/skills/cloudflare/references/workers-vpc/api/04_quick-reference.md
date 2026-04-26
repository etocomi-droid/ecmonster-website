## Quick Reference

| Task | Code |
|------|------|
| Import | `import { connect } from 'cloudflare:sockets';` |
| Connect | `connect({ hostname: "host", port: 443 })` |
| With TLS | `connect(addr, { secureTransport: "on" })` |
| StartTLS | `socket.startTls()` after handshake |
| Write | `await writer.write(data); await writer.close();` |
| Read | `const { value } = await reader.read();` |
| Error handling | `try { await socket.opened; } catch { }` |
| Always close | `try { } finally { await socket.close(); }` |

