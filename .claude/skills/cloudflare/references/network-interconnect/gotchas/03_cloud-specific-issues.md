## Cloud-Specific Issues

### AWS Direct Connect: "VLAN not matching"

**Cause:** VLAN ID from AWS LOA doesn't match CNI config  
**Solution:**
1. Get VLAN from AWS Console after ordering
2. Send exact VLAN to CF account team
3. Verify match in CNI object config

### AWS: "Connection stuck in Pending"

**Cause:** LOA not provided to CF or AWS connection not accepted  
**Solution:**
1. Verify AWS connection status is "Available"
2. Confirm LOA sent to CF account team
3. Wait for CF team acceptance (can take days)

### GCP: "BGP routes not propagating"

**Cause:** BGP routes from GCP Cloud Router **ignored by design**  
**Solution:** Use [static routes](https://developers.cloudflare.com/magic-wan/configuration/manually/how-to/configure-routes/#configure-static-routes) in Magic WAN instead

### GCP: "Cannot query VLAN attachment status via API"

**Cause:** GCP Cloud Interconnect Dashboard-only (no API yet)  
**Solution:** Check status in CF Dashboard or GCP Console

