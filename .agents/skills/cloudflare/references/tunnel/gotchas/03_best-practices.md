## Best Practices

### Security
1. Use token-based tunnels (config source: cloudflare) for centralized control
2. Enable Access policies for sensitive services
3. Rotate tunnel credentials regularly
4. After rotation: stop all old cloudflared processes within 24h grace period
5. Verify TLS certs (`noTLSVerify: false`)
6. Restrict `bastion` service type

### Performance
1. Run multiple replicas for HA (2-4 typical, load balanced automatically)
2. Replicas share same tunnel UUID, get unique connector IDs
3. Place `cloudflared` close to origin (same network)
4. Use HTTP/2 for gRPC (`http2Origin: true`)
5. Tune keepalive for long-lived connections
6. Monitor connection counts

### Configuration
1. Use environment variables for secrets
2. Version control config files
3. Validate before deploying (`cloudflared tunnel ingress validate`)
4. Test rules (`cloudflared tunnel ingress rule <URL>`)
5. Document rule order (first match wins)

### Operations
1. Monitor tunnel health in dashboard (shows active replicas)
2. Set up disconnect alerts (when replica count drops to 0)
3. Graceful shutdown for config updates
4. Update replicas in rolling fashion (update 1, wait, update next)
5. Keep `cloudflared` updated (1 year support window)
6. Use `--no-autoupdate` in prod; control updates manually

