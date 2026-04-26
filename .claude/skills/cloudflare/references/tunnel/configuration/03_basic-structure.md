## Basic Structure

```yaml
tunnel: <UUID>
credentials-file: /path/to/<UUID>.json

ingress:
  - hostname: app.example.com
    service: http://localhost:8000
  - service: http_status:404  # Required catch-all
```

