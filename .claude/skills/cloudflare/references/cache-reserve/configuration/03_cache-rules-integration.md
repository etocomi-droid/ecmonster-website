## Cache Rules Integration

Control Cache Reserve eligibility via Cache Rules:

```typescript
// Enable for static assets
{
  action: 'set_cache_settings',
  action_parameters: {
    cache_reserve: { eligible: true, minimum_file_ttl: 86400 },
    edge_ttl: { mode: 'override_origin', default: 86400 },
    cache: true
  },
  expression: '(http.request.uri.path matches "\\.(jpg|png|webp|pdf|zip)$")'
}

// Disable for APIs
{
  action: 'set_cache_settings',
  action_parameters: { cache_reserve: { eligible: false } },
  expression: '(http.request.uri.path matches "^/api/")'
}

// Create via API: PUT to zones/{zone_id}/rulesets/phases/http_request_cache_settings/entrypoint
```

