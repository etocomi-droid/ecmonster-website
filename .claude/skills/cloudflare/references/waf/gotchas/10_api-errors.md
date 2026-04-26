## API Errors

**Problem:** API calls fail with cryptic errors
**Cause:** Invalid parameters or permissions
**Solution:**

```typescript
// Error: "Invalid phase" → Use exact phase name
phase: 'http_request_firewall_custom'

// Error: "Ruleset already exists" → Use update() or list first
const rulesets = await client.rulesets.list({ zone_id, phase: 'http_request_firewall_custom' });
if (rulesets.result.length > 0) {
  await client.rulesets.update({ zone_id, ruleset_id: rulesets.result[0].id, rules: [...] });
}

// Error: "Action not supported" → Check phase/action compatibility
// 'execute' only in http_request_firewall_managed
// Rate limit config only in http_ratelimit phase

// Error: "Expression parse error" → Common fixes:
'ip.geoip.country eq "US"'   // Quote strings
'cf.waf.score gt 40'         // Use 'gt' not '>'
'http.request.uri.path'      // Not 'http.request.path'
```

**Tip**: Test expressions in dashboard Security Events before deploying.
