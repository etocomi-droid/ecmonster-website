## Platform Limits

| Limit | Value | Notes |
|-------|-------|-------|
| Workers per namespace | Unlimited | Unlike regular Workers (500 per account) |
| Namespaces per account | Unlimited | Best practice: 1 production + 1 staging |
| Max tags per Worker | 8 | For filtering and organization |
| Worker mode | Untrusted (default) | No `request.cf` access unless trusted mode |
| Cache isolation | Per-Worker (untrusted) | Shared in trusted mode with key prefixes |
| Durable Object namespaces | Unlimited | No per-account limit for WfP |
| Gradual Deployments | Not supported | All-at-once only |
| `caches.default` | Disabled (untrusted) | Use Cache API with custom keys |

