## Wrangler Config

### Basic Binding

**wrangler.jsonc**:

```jsonc
{
  "secrets_store_secrets": [
    {
      "binding": "API_KEY",
      "store_id": "abc123",
      "secret_name": "stripe_api_key"
    }
  ]
}
```

**wrangler.toml** (alternative):

```toml
[[secrets_store_secrets]]
binding = "API_KEY"
store_id = "abc123"
secret_name = "stripe_api_key"
```

Fields:
- `binding`: Variable name for `env` access
- `store_id`: From `wrangler secrets-store store list`
- `secret_name`: Identifier (no spaces)

### Environment-Specific

**wrangler.jsonc**:

```jsonc
{
  "env": {
    "production": {
      "secrets_store_secrets": [
        {
          "binding": "API_KEY",
          "store_id": "prod-store",
          "secret_name": "prod_api_key"
        }
      ]
    },
    "staging": {
      "secrets_store_secrets": [
        {
          "binding": "API_KEY",
          "store_id": "staging-store",
          "secret_name": "staging_api_key"
        }
      ]
    }
  }
}
```

**wrangler.toml** (alternative):

```toml
[env.production]
[[env.production.secrets_store_secrets]]
binding = "API_KEY"
store_id = "prod-store"
secret_name = "prod_api_key"

[env.staging]
[[env.staging.secrets_store_secrets]]
binding = "API_KEY"
store_id = "staging-store"
secret_name = "staging_api_key"
```

