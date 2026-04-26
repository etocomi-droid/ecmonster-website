## Best Practices

- Split full-stack apps: frontend at edge, backend with Smart Placement
- Use fetch-based Service Bindings (not RPC)
- Enable for backend logic: APIs, data aggregation, DB operations
- Don't enable for: static content, edge logic, RPC methods, Pages with `run_worker_first`
- Wait 15+ min for analysis, verify `placement_status = SUCCESS`
