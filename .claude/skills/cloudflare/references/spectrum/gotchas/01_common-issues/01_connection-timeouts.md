### Connection Timeouts

**Problem:** Connections fail or timeout  
**Cause:** Origin firewall blocking Cloudflare IPs, origin service not running, incorrect DNS  
**Solution:**
1. Verify origin firewall allows Cloudflare IP ranges
2. Check origin service running on correct port
3. Ensure DNS record is CNAME (not A/AAAA)
4. Verify origin IP/hostname is correct

```bash
# Test connectivity
nc -zv app.example.com 22
dig app.example.com
```

