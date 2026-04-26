## When to Use Which Pattern

| Need | Pattern | ID Strategy |
|------|---------|-------------|
| Rate limit per user/IP | Rate Limiting | `idFromName(identifier)` |
| Mutual exclusion | Distributed Lock | `idFromName(resource)` |
| >1K req/s throughput | Sharding | `newUniqueId()` or hash |
| Real-time updates | WebSocket Collab | `idFromName(room)` |
| User sessions | Session Management | `idFromName(sessionId)` |
| Background cleanup | Alarm-based | Any |

