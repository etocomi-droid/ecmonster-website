## Token Validation

```bash
GET /token_validation                  # List
POST /token_validation                 # Create: {name,location:{header:"..."},jwks:"..."}
POST /jwt_validation_rules             # Rule: {name,hostname,token_validation_id,action:"block"}
```

