## Troubleshooting

### Issue: TURN credentials not working

**Check:**
- Key ID and secret are correct
- Credentials haven't expired (check TTL)
- TTL doesn't exceed 172800 seconds (48 hours)
- Server can reach rtc.live.cloudflare.com
- Network allows outbound HTTPS

**Solution:**
```typescript
// Validate before using
if (ttl > 172800) {
  throw new Error('TTL cannot exceed 48 hours');
}
```

### Issue: Slow connection establishment

**Solutions:**
- Ensure proper ICE candidate gathering
- Check network latency to Cloudflare edge
- Verify firewall allows WebRTC ports (3478, 5349, 443)
- Consider using TURN over TLS (port 443) for corporate networks

### Issue: High packet loss

**Check:**
- Not exceeding rate limits (5-10k pps)
- Not exceeding bandwidth limits (50-100 Mbps)
- Not connecting to too many unique IPs (>5/sec)
- Client network quality

### Issue: Connection drops after ~48 hours

**Cause**: Credentials expired (48hr max)

**Solution**: 
- Set TTL to expected session duration
- Implement credential refresh with setConfiguration()
- Use ICE restart if connection fails

```typescript
// Refresh credentials before expiry
const refreshInterval = ttl * 1000 - 60000; // 1 min early
setInterval(async () => {
  await refreshTURNCredentials(pc);
}, refreshInterval);
```

### Issue: Port 53 URLs in browser fail silently

**Cause**: Chrome/Firefox block port 53

**Solution**: Filter port 53 URLs server-side:

```typescript
const filtered = urls.filter(url => !url.includes(':53'));
```

### Issue: Hardcoded IPs stop working

**Cause**: Cloudflare changed IP addresses (14-day notice)

**Solution**: 
- Use DNS hostnames (`turn.cloudflare.com`)
- Monitor DNS changes with automated alerts
- Update allowlists within 14 days if using IP allowlisting

