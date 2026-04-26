## Secrets Management

Store sensitive credentials as secrets (not in wrangler.jsonc):

```bash
wrangler secret put DB_PASSWORD  # Enter value when prompted
```

Access in Worker via `env.DB_PASSWORD`. Use in protocol handshake or authentication.

