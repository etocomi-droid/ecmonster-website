## CNI Objects (BGP config)

```http
GET    /accounts/{account_id}/cni/cnis
POST   /accounts/{account_id}/cni/cnis
GET    /accounts/{account_id}/cni/cnis/{cni}
PUT    /accounts/{account_id}/cni/cnis/{cni}
DELETE /accounts/{account_id}/cni/cnis/{cni}
```

Body: `account`, `cust_ip`, `cf_ip`, `bgp_asn`, `bgp_password`, `vlan`

