## Configuration Options

| Option | TypeScript | Python | Go | Default |
|--------|-----------|--------|-----|---------|
| Timeout | `timeout` (ms) | `timeout` (s) | `WithRequestTimeout` | 60s |
| Retries | `maxRetries` | `max_retries` | `WithMaxRetries` | 2 (Go: 10) |
| Base URL | `baseURL` | `base_url` | `WithBaseURL` | api.cloudflare.com |

**Note:** Go SDK has higher default retries (10) than TypeScript/Python (2).

