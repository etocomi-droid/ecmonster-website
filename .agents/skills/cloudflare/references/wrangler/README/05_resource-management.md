## Resource Management

### KV
```bash
wrangler kv namespace create NAME
wrangler kv key put "key" "value" --namespace-id=<id>
wrangler kv key get "key" --namespace-id=<id>
```

### D1
```bash
wrangler d1 create NAME
wrangler d1 execute NAME --command "SQL"
wrangler d1 migrations create NAME "description"
wrangler d1 migrations apply NAME
```

### R2
```bash
wrangler r2 bucket create NAME
wrangler r2 object put BUCKET/key --file path
wrangler r2 object get BUCKET/key
```

### Other Resources
```bash
wrangler queues create NAME
wrangler vectorize create NAME --dimensions N --metric cosine
wrangler hyperdrive create NAME --connection-string "..."
wrangler workflows create NAME
wrangler constellation create NAME
wrangler pages project create NAME
wrangler pages deployment create --project NAME --branch main
```

### Secrets
```bash
wrangler secret put NAME          # Set Worker secret
wrangler secret list              # List Worker secrets
wrangler secret delete NAME       # Delete Worker secret
wrangler secret bulk FILE.json    # Bulk upload from JSON

# Secrets Store (centralized, reusable across Workers)
wrangler secret-store:secret put STORE_NAME SECRET_NAME
wrangler secret-store:secret list STORE_NAME
```

### Monitoring
```bash
wrangler tail                     # Real-time logs
wrangler tail --env production    # Tail specific env
wrangler tail --status error      # Filter by status
```

