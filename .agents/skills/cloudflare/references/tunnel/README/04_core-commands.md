## Core Commands

```bash
# Tunnel lifecycle
cloudflared tunnel create <name>
cloudflared tunnel list
cloudflared tunnel info <name>
cloudflared tunnel delete <name>

# DNS routing
cloudflared tunnel route dns <tunnel> <hostname>
cloudflared tunnel route list

# Private network
cloudflared tunnel route ip add 10.0.0.0/8 <tunnel>

# Run tunnel
cloudflared tunnel run <name>
```

