## Wrangler Commands

### Store Management

```bash
wrangler secrets-store store list
wrangler secrets-store store create my-store --remote
wrangler secrets-store store delete <store-id> --remote
```

### Secret Management (Production)

```bash
# Create (interactive)
wrangler secrets-store secret create <store-id> \
  --name MY_SECRET --scopes workers --remote

# Create (piped)
cat secret.txt | wrangler secrets-store secret create <store-id> \
  --name MY_SECRET --scopes workers --remote

# List/get/update/delete
wrangler secrets-store secret list <store-id> --remote
wrangler secrets-store secret get <store-id> --name MY_SECRET --remote
wrangler secrets-store secret update <store-id> --name MY_SECRET --new-value "val" --remote
wrangler secrets-store secret delete <store-id> --name MY_SECRET --remote

# Duplicate
wrangler secrets-store secret duplicate <store-id> \
  --name ORIG --new-name COPY --remote
```

### Local Development

**CRITICAL**: Production secrets (`--remote`) NOT accessible in local dev.

```bash
# Create local-only (no --remote)
wrangler secrets-store secret create <store-id> --name DEV_KEY --scopes workers

wrangler dev    # Uses local secrets
wrangler deploy # Uses production secrets
```

Best practice: Separate names for local/prod:

```jsonc
{
  "env": {
    "development": {
      "secrets_store_secrets": [
        { "binding": "API_KEY", "store_id": "store", "secret_name": "dev_api_key" }
      ]
    },
    "production": {
      "secrets_store_secrets": [
        { "binding": "API_KEY", "store_id": "store", "secret_name": "prod_api_key" }
      ]
    }
  }
}
```

