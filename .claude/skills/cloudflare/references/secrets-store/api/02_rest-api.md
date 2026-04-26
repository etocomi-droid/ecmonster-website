## REST API

Base: `https://api.cloudflare.com/client/v4`

### Auth

```bash
curl -H "Authorization: Bearer $CF_TOKEN" \
  https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/secrets_store/stores
```

### Store Operations

```bash
# List
GET /accounts/{account_id}/secrets_store/stores

# Create
POST /accounts/{account_id}/secrets_store/stores
{"name": "my-store"}

# Delete
DELETE /accounts/{account_id}/secrets_store/stores/{store_id}
```

### Secret Operations

```bash
# List
GET /accounts/{account_id}/secrets_store/stores/{store_id}/secrets

# Create (single)
POST /accounts/{account_id}/secrets_store/stores/{store_id}/secrets
{
  "name": "my_secret",
  "value": "secret_value",
  "scopes": ["workers"],
  "comment": "Optional"
}

# Create (batch)
POST /accounts/{account_id}/secrets_store/stores/{store_id}/secrets
[
  {"name": "secret_one", "value": "val1", "scopes": ["workers"]},
  {"name": "secret_two", "value": "val2", "scopes": ["workers", "ai-gateway"]}
]

# Get metadata
GET /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}

# Update
PATCH /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}
{"value": "new_value", "comment": "Updated"}

# Delete (single)
DELETE /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}

# Delete (batch)
DELETE /accounts/{account_id}/secrets_store/stores/{store_id}/secrets
{"secret_ids": ["id-1", "id-2"]}

# Duplicate
POST /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}/duplicate
{"name": "new_name"}

# Quota
GET /accounts/{account_id}/secrets_store/quota
```

### Responses

Success:
```json
{
  "success": true,
  "result": {
    "id": "secret-id-123",
    "name": "my_secret",
    "created": "2025-01-11T12:00:00Z",
    "scopes": ["workers"]
  }
}
```

Error:
```json
{
  "success": false,
  "errors": [{"code": 10000, "message": "Name exists"}]
}
```

