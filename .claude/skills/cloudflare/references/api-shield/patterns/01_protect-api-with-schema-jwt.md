## Protect API with Schema + JWT

```bash
# 1. Upload OpenAPI schema
POST /zones/{zone_id}/api_gateway/user_schemas

# 2. Configure JWT validation
POST /zones/{zone_id}/api_gateway/token_validation
{
  "name": "Auth0",
  "location": {"header": "Authorization"},
  "jwks": "{...}"
}

# 3. Create JWT rule
POST /zones/{zone_id}/api_gateway/jwt_validation_rules

# 4. Set schema validation action
PUT /zones/{zone_id}/api_gateway/settings/schema_validation
{"validation_default_mitigation_action": "block"}
```

