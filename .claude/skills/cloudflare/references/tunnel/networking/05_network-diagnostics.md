## Network Diagnostics

### Connection Diagnostics

```bash
# Check edge selection and connection health
cloudflared tunnel info my-tunnel --output json | jq '.connections[]'

# Enable metrics endpoint
cloudflared tunnel --metrics localhost:9090 run my-tunnel
curl localhost:9090/metrics | grep cloudflared_tunnel

# Test latency
curl -w "time_total: %{time_total}\n" -o /dev/null https://myapp.example.com
```

