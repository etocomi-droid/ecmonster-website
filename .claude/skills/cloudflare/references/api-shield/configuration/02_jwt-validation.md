## JWT Validation

**Setup token config:**
```
Security > API Shield > Settings > JWT Settings > Add configuration
- Name: "Auth0 JWT Config"
- Location: Header/Cookie + name (e.g., "Authorization")
- JWKS: Paste public keys from IdP
```

**Create validation rule:**
```
Security > API Shield > API Rules > Add rule
- Hostname: api.example.com
- Deselect endpoints to ignore
- Token config: Select config
- Enforce presence: Ignore or Mark as non-compliant
- Action: Log/Block/Challenge
```

**Rate limit by JWT claim:**
```wirefilter
lookup_json_string(http.request.jwt.claims["{config_id}"][0], "sub")
```

**Special cases:**
- Two JWTs, different IdPs: Create 2 configs, select both, "Validate all"
- IdP migration: 2 configs + 2 rules, adjust actions per state
- Bearer prefix: API Shield handles with/without
- Nested claims: Dot notation `user.email`

