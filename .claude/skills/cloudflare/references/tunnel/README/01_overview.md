## Overview

Cloudflare Tunnel (formerly Argo Tunnel) enables:
- **Outbound-only connections** - No inbound ports or firewall changes
- **Public hostname routing** - Expose local services to internet
- **Private network access** - Connect internal networks via WARP
- **Zero Trust integration** - Built-in access policies

**Architecture**: Tunnel (persistent object) → Replica (`cloudflared` process) → Origin services

**Terminology:**
- **Tunnel**: Named persistent object with UUID
- **Replica**: Individual `cloudflared` process connected to tunnel
- **Config Source**: Where ingress rules stored (local file vs Cloudflare dashboard)
- **Connector**: Legacy term for replica

