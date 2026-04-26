## Service Types

| Protocol | Format | Client Requirement |
|----------|--------|-------------------|
| HTTP | `http://localhost:8000` | Browser |
| HTTPS | `https://localhost:8443` | Browser |
| TCP | `tcp://localhost:2222` | `cloudflared access tcp` |
| SSH | `ssh://localhost:22` | `cloudflared access ssh` |
| RDP | `rdp://localhost:3389` | `cloudflared access rdp` |
| Unix | `unix:/path/to/socket` | Browser |
| Test | `hello_world` | Browser |

