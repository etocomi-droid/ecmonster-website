## Authentication Posture

### Detect Missing Auth
```javascript
// Log endpoints lacking authentication
(cf.api_gateway.cf-risk-missing-auth and http.host eq "api.example.com")
// Action: Log (for audit)
```

### Detect Mixed Auth
```javascript
// Alert on inconsistent auth patterns
(cf.api_gateway.cf-risk-mixed-auth and http.host eq "api.example.com")
// Action: Log (review required)
```

