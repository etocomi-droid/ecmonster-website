## Rate Limiting by User

```javascript
// Rate Limiting Rule (modern syntax)
(http.host eq "api.example.com" and
 is_jwt_valid(http.request.jwt.payload["{config_id}"][0]))

// Rate: 100 req/60s
// Counting expression: lookup_json_string(http.request.jwt.payload["{config_id}"][0], "sub")
```

