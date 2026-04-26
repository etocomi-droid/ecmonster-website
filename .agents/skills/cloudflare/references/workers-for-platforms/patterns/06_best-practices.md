## Best Practices

### Architecture
- One namespace per environment (production, staging)
- Platform logic in dispatch Worker (auth, rate limiting, validation)
- Isolation automatic (no shared cache, untrusted mode)

### Routing
- Use `*/*` wildcard routes
- Store mappings in KV
- Handle missing Workers gracefully

### Limits & Security
- Set custom limits by plan
- Track violations with Analytics Engine
- Use outbound Workers for egress control
- Sanitize responses

### Tags
- Tag all Workers: customer ID, plan, environment
- Enable bulk operations
- Filter efficiently

See [README.md](./README.md), [configuration.md](./configuration.md), [api.md](./api.md), [gotchas.md](./gotchas.md)
