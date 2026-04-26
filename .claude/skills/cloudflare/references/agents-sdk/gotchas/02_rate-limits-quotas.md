## Rate Limits & Quotas

| Resource/Limit | Value | Notes |
|----------------|-------|-------|
| CPU per request | 30s (std), 300s (max) | Set in wrangler.jsonc |
| Memory per instance | 128MB | Shared with WebSockets |
| Storage per agent | 10GB | SQLite storage |
| Scheduled tasks | 1000 per agent | Monitor with `getSchedules()` |
| WebSocket connections | Unlimited | Within memory limits |
| SQL columns | 100 | Per table |
| SQL row size | 2MB | Key + value |
| WebSocket message | 32MiB | Max size |
| DO requests/sec | ~1000 | Per unique DO instance; rate limit if needed |
| AI Gateway (Workers AI) | Model-specific | Check dashboard for limits |
| MCP requests | Depends on server | Implement retry/backoff |

