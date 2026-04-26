## BOLA Detection

### Enumeration Detection
Detects sequential resource access (e.g., `/users/1`, `/users/2`, `/users/3`).

```javascript
// Block BOLA enumeration attempts
(cf.api_gateway.cf-risk-bola-enumeration and http.host eq "api.example.com")
// Action: Block or Challenge
```

### Parameter Pollution
Detects duplicate/excessive parameters in requests.

```javascript
// Block parameter pollution
(cf.api_gateway.cf-risk-bola-pollution and http.host eq "api.example.com")
// Action: Block
```

### Combined BOLA Protection
```javascript
// Comprehensive BOLA rule
(cf.api_gateway.cf-risk-bola-enumeration or cf.api_gateway.cf-risk-bola-pollution)
and http.host eq "api.example.com"
// Action: Block
```

