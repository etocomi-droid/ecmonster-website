## Common Errors

### "INSUFFICIENT_INVOCATIONS"

**Cause:** Not enough traffic for Smart Placement to analyze
**Solution:**
- Ensure Worker receives consistent global traffic
- Wait longer (analysis takes up to 15 minutes)
- Send test traffic from multiple global locations
- Check Worker has fetch event handler

### "UNSUPPORTED_APPLICATION"

**Cause:** Smart Placement made Worker slower rather than faster
**Reasons:**
- Worker doesn't make backend calls (runs faster at edge)
- Backend calls are cached (network latency to user more important)
- Backend service has good global distribution
- Worker serves static assets or Pages content

**Solutions:**
- Disable Smart Placement: `{ "placement": { "mode": "off" } }`
- Review whether Worker actually benefits from Smart Placement
- Consider caching strategy to reduce backend calls
- For Pages/Assets Workers, use separate backend Worker with Smart Placement

### "No request duration metrics"

**Cause:** Smart Placement not enabled, insufficient time passed, insufficient traffic, or analysis incomplete
**Solution:**
- Ensure Smart Placement enabled in config
- Wait 15+ minutes after deployment
- Verify Worker has sufficient traffic
- Check `placement_status` is `SUCCESS`

### "cf-placement header missing"

**Cause:** Smart Placement not enabled, beta feature removed, or Worker not analyzed yet
**Solution:** Verify Smart Placement enabled, wait for analysis (15min), check if beta feature still available

