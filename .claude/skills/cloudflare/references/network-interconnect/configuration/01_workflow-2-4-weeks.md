## Workflow (2-4 weeks)

1. **Submit request** (Week 1): Contact account team, provide type/location/use case
2. **Review config** (Week 1-2, v1 only): Approve IP/VLAN/spec doc
3. **Order connection** (Week 2-3):
   - **Direct**: Get LOA, order cross-connect from facility
   - **Partner**: Order virtual circuit in partner portal
   - **Cloud**: Order Direct Connect/Cloud Interconnect, send LOA+VLAN to CF
4. **Configure** (Week 3): Both sides configure per doc
5. **Test** (Week 3-4): Ping, verify BGP, check routes
6. **Health checks** (Week 4): Configure [Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-tunnel-endpoints/#add-tunnels) or [Magic WAN](https://developers.cloudflare.com/magic-wan/configuration/manually/how-to/configure-tunnel-endpoints/#add-tunnels) health checks
7. **Activate** (Week 4): Route traffic, verify flow
8. **Monitor**: Enable [maintenance notifications](https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/#enable-cloudflare-status-maintenance-notification)

