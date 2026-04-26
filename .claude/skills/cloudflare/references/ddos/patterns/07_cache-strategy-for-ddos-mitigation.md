## Cache Strategy for DDoS Mitigation

Exclude query strings from cache key to counter randomized query parameter attacks.

```typescript
const cacheRule = {
  expression: "http.request.uri.path matches \"^/api/\"",
  action: "set_cache_settings",
  action_parameters: {
    cache: true,
    cache_key: { ignore_query_strings_order: true, custom_key: { query_string: { exclude: { all: true } } } },
  },
};

await client.zones.rulesets.phases.entrypoint.update("http_request_cache_settings", { zone_id: zoneId, rules: [cacheRule] });
```

**Rationale**: Attackers randomize query strings (`?random=123456`) to bypass cache. Excluding query params ensures cache hits absorb attack traffic.

See [configuration.md](./configuration.md) for rule structure details.
