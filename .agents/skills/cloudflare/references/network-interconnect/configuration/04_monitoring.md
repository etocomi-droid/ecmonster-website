## Monitoring

**Dashboard Status:**

| Status | Meaning |
|--------|---------|
| **Healthy** | Link operational, traffic flowing, health checks passing |
| **Active** | Link up, sufficient light, Ethernet negotiated |
| **Unhealthy** | Link down, no/low light (<-20 dBm), can't negotiate |
| **Pending** | Cross-connect incomplete, device unresponsive, RX/TX swapped |
| **Down** | Physical link down, no connectivity |

**Alerts:**

**CNI Connection Maintenance** (Magic Networking only):
```
Dashboard → Notifications → Add
Product: Cloudflare Network Interconnect
Type: Connection Maintenance Alert
```
Warnings up to 2 weeks advance. 6hr delay for new additions.

**Cloudflare Status Maintenance** (entire PoP):
```
Dashboard → Notifications → Add
Product: Cloudflare Status
Filter PoPs: gru,fra,lhr
```

**Find PoP code:**
```
Dashboard → Magic Transit/WAN → Configuration → Interconnects
Select CNI → Note Data Center (e.g., "gru-b")
Use first 3 letters: "gru"
```

