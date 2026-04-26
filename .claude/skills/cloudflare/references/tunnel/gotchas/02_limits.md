## Limits

| Resource/Limit | Value | Notes |
|----------------|-------|-------|
| Free tier | Unlimited tunnels | Unlimited traffic |
| Tunnel replicas | 1000 per tunnel | Max concurrent |
| Connection duration | No hard limit | Hours to days |
| Long-lived connections | May drop during updates | WebSocket, SSH, UDP |
| Replica registration | ~5s TTL | Old replica dropped after 5s no heartbeat |
| Token rotation grace | 24 hours | Old tokens work during grace period |

