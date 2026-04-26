## Config Source

Tunnels use one of two config sources:

| Config Source | Storage | Updates | Use Case |
|---------------|---------|---------|----------|
| Local | `config.yml` file | Edit file, restart | Dev, multi-env, version control |
| Cloudflare | Dashboard/API | Instant, no restart | Production, centralized management |

**Token-based tunnels** = config source: Cloudflare
**Locally-managed tunnels** = config source: local

