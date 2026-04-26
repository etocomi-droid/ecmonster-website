## Limits

| Resource | Lite | Standard | Heavy |
|----------|------|----------|-------|
| RAM | 256MB | 512MB | 1GB |
| vCPU | 0.5 | 1 | 2 |

| Operation | Default Timeout | Override |
|-----------|----------------|----------|
| Container provisioning | 30s | `SANDBOX_INSTANCE_TIMEOUT_MS` |
| Port readiness | 90s | `SANDBOX_PORT_TIMEOUT_MS` |
| exec() | 120s | `timeout` option |
| sleepAfter | 10m | `sleepAfter` option |

**Performance**:
- **First deploy**: 2-3 min for container build
- **Cold start**: 2-3s when waking from sleep
- **Bucket mounting**: Production only (FUSE not in dev)

