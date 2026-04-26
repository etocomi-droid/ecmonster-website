## Config Options

Hyperdrive create/update CLI flags:

| Option | Default | Notes |
|--------|---------|-------|
| `--caching-disabled` | `false` | Disable caching |
| `--max-age` | `60` | Cache TTL (max 3600s) |
| `--swr` | `15` | Stale-while-revalidate |
| `--origin-connection-limit` | 20/100 | Free/paid |
| `--access-client-id` | - | Tunnel auth |
| `--access-client-secret` | - | Tunnel auth |
| `--sslmode` | `require` | PostgreSQL only |

