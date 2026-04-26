## Advanced

```jsonc
// Cron Triggers
{ "triggers": { "crons": ["0 0 * * *"] } }

// Observability (tracing)
{ "observability": { "enabled": true, "head_sampling_rate": 0.1 } }

// Runtime Limits
{ "limits": { "cpu_ms": 100 } }

// Browser Rendering
{ "browser": { "binding": "BROWSER" } }

// mTLS Certificates
{ "mtls_certificates": [{ "binding": "CERT", "certificate_id": "cert-uuid" }] }

// Logpush (stream logs to R2/S3)
{ "logpush": true }

// Tail Consumers (process logs with another Worker)
{ "tail_consumers": [{ "service": "log-worker" }] }

// Unsafe bindings (access to arbitrary bindings)
{ "unsafe": { "bindings": [{ "name": "MY_BINDING", "type": "plain_text", "text": "value" }] } }
```

