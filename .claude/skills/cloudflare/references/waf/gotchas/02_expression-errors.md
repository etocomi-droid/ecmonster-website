## Expression Errors

**Problem:** Syntax errors prevent deployment
**Cause:** Invalid field/operator/syntax
**Solution:**

```typescript
// Common mistakes
'http.request.path' → 'http.request.uri.path' // Correct field
'ip.geoip.country eq US' → 'ip.geoip.country eq "US"' // Quote strings
'http.user_agent eq "Mozilla"' → 'lower(http.user_agent) contains "mozilla"' // Case sensitivity
'matches ".*[.jpg"' → 'matches ".*\\.jpg$"' // Valid regex
```

Test expressions in Security Events before deploying.

