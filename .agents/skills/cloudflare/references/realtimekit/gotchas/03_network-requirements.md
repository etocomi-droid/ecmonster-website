## Network Requirements

### Firewall Rules
Allow outbound UDP/TCP to:
- `*.cloudflare.com` ports 443, 80
- UDP ports 1024-65535 (WebRTC media)

### TURN Service
Enable for users behind restrictive firewalls/proxies:
```jsonc
// wrangler.jsonc
{
  "vars": {
    "TURN_SERVICE_ID": "your_turn_service_id"
  }
  // Set secret: wrangler secret put TURN_SERVICE_TOKEN
}
```

TURN automatically configured in SDK when enabled in account.

