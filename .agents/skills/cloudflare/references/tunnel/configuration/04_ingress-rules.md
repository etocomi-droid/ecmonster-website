## Ingress Rules

Rules evaluated **top to bottom**, first match wins.

```yaml
ingress:
  # Exact hostname + path regex
  - hostname: static.example.com
    path: \.(jpg|png|css|js)$
    service: https://localhost:8001
  
  # Wildcard hostname
  - hostname: "*.example.com"
    service: https://localhost:8002
  
  # Path only (all hostnames)
  - path: /api/.*
    service: http://localhost:9000
  
  # Catch-all (required)
  - service: http_status:404
```

**Validation**:
```bash
cloudflared tunnel ingress validate
cloudflared tunnel ingress rule https://foo.example.com
```

