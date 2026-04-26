## Quick Decision: Which Technology?

Need private network connectivity from Workers?

| Requirement | Use | Why |
|------------|-----|-----|
| HTTP/HTTPS APIs in private network | VPC Services (beta, separate docs) | SSRF-safe, declarative bindings |
| PostgreSQL/MySQL databases | [Hyperdrive](../hyperdrive/) | Connection pooling, caching, optimized |
| Custom TCP protocols (SSH, MQTT, proprietary) | **TCP Sockets (this doc)** | Full protocol control |
| Simple HTTP with lowest latency | TCP Sockets + [Smart Placement](../smart-placement/) | Manual optimization |
| Expose on-prem to internet (inbound) | [Cloudflare Tunnel](../tunnel/) | Not Worker-specific |

