## Local Dev

**Option 1: Local (RECOMMENDED):**
```bash
# Env var (takes precedence)
export CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_HYPERDRIVE="postgres://user:pass@localhost:5432/dev"
npx wrangler dev

# wrangler.jsonc
{"hyperdrive": [{"binding": "HYPERDRIVE", "localConnectionString": "postgres://..."}]}
```

**Remote DB locally:**
```bash
# PostgreSQL
export CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_HYPERDRIVE="postgres://user:pass@remote:5432/db?sslmode=require"

# MySQL
export CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_HYPERDRIVE="mysql://user:pass@remote:3306/db?sslMode=REQUIRED"
```

**Option 2: Remote execution:**
```bash
npx wrangler dev --remote  # Uses deployed config, affects production
```

See [api.md](./api.md), [patterns.md](./patterns.md), [gotchas.md](./gotchas.md).
