## Cloud Interconnect Setup

### AWS Direct Connect (Beta)

**Requirements:** Magic WAN, AWS Dedicated Direct Connect 1/10 Gbps.

**Process:**
1. Contact CF account team
2. Choose location
3. Order in AWS portal
4. AWS provides LOA + VLAN ID
5. Send to CF account team
6. Wait ~4 weeks

**Post-setup:** Add [static routes](https://developers.cloudflare.com/magic-wan/configuration/manually/how-to/configure-routes/#configure-static-routes) to Magic WAN. Enable [bidirectional health checks](https://developers.cloudflare.com/magic-wan/configuration/manually/how-to/configure-tunnel-endpoints/#legacy-bidirectional-health-checks).

### GCP Cloud Interconnect (Beta)

**Setup via Dashboard:**
1. Interconnects → Create → Cloud Interconnect → Google
2. Provide name, MTU (match GCP VLAN attachment), speed (50M-50G granular options available for partner interconnects)
3. Enter VLAN attachment pairing key
4. Confirm order

**Routing to GCP:** Add [static routes](https://developers.cloudflare.com/magic-wan/configuration/manually/how-to/configure-routes/#configure-static-routes). BGP routes from GCP Cloud Router **ignored**.

**Routing to CF:** Configure [custom learned routes](https://cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes) in Cloud Router. Request prefixes from CF account team.

