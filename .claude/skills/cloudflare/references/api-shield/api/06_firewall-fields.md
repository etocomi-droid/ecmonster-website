## Firewall Fields

### Core Fields
```js
cf.api_gateway.auth_id_present           // Session ID present
cf.api_gateway.request_violates_schema   // Schema violation
cf.api_gateway.fallthrough_triggered     // No endpoint match
cf.tls_client_auth.cert_verified         // mTLS cert valid
cf.tls_client_auth.cert_fingerprint_sha256
```

### JWT Validation (2026)
```js
// Modern validation syntax
is_jwt_valid(http.request.jwt.payload["{config_id}"][0])

// Legacy (still supported)
cf.api_gateway.jwt_claims_valid

// Extract claims
lookup_json_string(http.request.jwt.payload["{config_id}"][0], "claim_name")
```

### Risk Labels (2026)
```js
// BOLA detection
cf.api_gateway.cf-risk-bola-enumeration  // Sequential resource access detected
cf.api_gateway.cf-risk-bola-pollution    // Parameter pollution detected

// Authentication posture
cf.api_gateway.cf-risk-missing-auth      // Endpoint lacks authentication
cf.api_gateway.cf-risk-mixed-auth        // Inconsistent auth patterns
```

