## Origin Configuration

### Connection Settings
```yaml
originRequest:
  connectTimeout: 30s
  tlsTimeout: 10s
  tcpKeepAlive: 30s
  keepAliveTimeout: 90s
  keepAliveConnections: 100
```

### TLS Settings
```yaml
originRequest:
  noTLSVerify: true                      # Disable cert verification
  originServerName: "app.internal"       # Override SNI
  caPool: /path/to/ca.pem                # Custom CA
```

### HTTP Settings
```yaml
originRequest:
  disableChunkedEncoding: true
  httpHostHeader: "app.internal"
  http2Origin: true
```

