## High Availability

```yaml
# Same config on multiple servers
tunnel: <UUID>
credentials-file: /path/to/creds.json

ingress:
  - hostname: app.example.com
    service: http://localhost:8000
  - service: http_status:404
```

Run same config on multiple machines. Cloudflare automatically load balances. Long-lived connections (WebSocket, SSH) may drop during updates.

