## BGP Configuration

**v1 Requirements:**
- BGP ASN (provide during setup)
- /31 subnet for peering
- Optional: BGP password

**v2:** Simplified, less BGP config needed.

**BGP over CNI (Dec 2024):** Magic WAN/Transit can now peer BGP directly over CNI v2 (no GRE tunnel required).

**Example v1 BGP:**
```
Router ID: 192.0.2.1
Peer IP: 192.0.2.0
Remote ASN: 13335
Local ASN: 65000
Password: [optional]
VLAN: 100
```

