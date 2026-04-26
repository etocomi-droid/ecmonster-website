## Best Practices

**Performance**: Exclude static via `_routes.json`; cache with KV; keep bundle < 1MB  
**Security**: Use secrets (not vars); validate inputs; rate limit with KV/DO  
**Workflow**: Preview per branch; local dev with `wrangler pages dev`; instant rollbacks in Dashboard
