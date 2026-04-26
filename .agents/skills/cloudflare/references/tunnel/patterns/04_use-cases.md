## Use Cases

### Web Application
```yaml
ingress:
  - hostname: myapp.example.com
    service: http://localhost:3000
  - service: http_status:404
```

### SSH Access
```yaml
ingress:
  - hostname: ssh.example.com
    service: ssh://localhost:22
  - service: http_status:404
```

Client: `cloudflared access ssh --hostname ssh.example.com`

### gRPC Service
```yaml
ingress:
  - hostname: grpc.example.com
    service: http://localhost:50051
    originRequest:
      http2Origin: true
  - service: http_status:404
```

