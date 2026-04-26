### SMTP Reverse DNS

**Problem:** Email servers reject SMTP via Spectrum  
**Cause:** Spectrum IPs lack PTR (reverse DNS) records  
**Impact:** Many mail servers require valid rDNS for anti-spam

**Solution:**
- Outbound SMTP: NOT recommended through Spectrum
- Inbound SMTP: Use Cloudflare Email Routing
- Internal relay: Whitelist Spectrum IPs on destination

