## Quick Start

### Local Config
```bash
# Install cloudflared
brew install cloudflared  # macOS

# Authenticate
cloudflared tunnel login

# Create tunnel
cloudflared tunnel create my-tunnel

# Route DNS
cloudflared tunnel route dns my-tunnel app.example.com

# Run tunnel
cloudflared tunnel run my-tunnel
```

### Dashboard Config (Recommended)
1. **Zero Trust** > **Networks** > **Tunnels** > **Create**
2. Name tunnel, copy token
3. Configure routes in dashboard
4. Run: `cloudflared tunnel --no-autoupdate run --token <TOKEN>`

