## Volumetric Abuse Response

```javascript
// Detect abnormal traffic spikes
(cf.api_gateway.volumetric_abuse_detected and http.host eq "api.example.com")
// Action: Challenge or Rate Limit

// Combined with rate limiting
(cf.api_gateway.volumetric_abuse_detected or
 cf.threat_score gt 50) and http.host eq "api.example.com"
// Action: JS Challenge
```

