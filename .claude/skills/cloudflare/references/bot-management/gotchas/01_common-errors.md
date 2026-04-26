## Common Errors

### "Bot Score = 0"

**Cause:** Bot Management didn't run (internal Cloudflare request, Worker routing to zone (Orange-to-Orange), or request handled before BM (Redirect Rules, etc.))  
**Solution:** Check request flow and ensure Bot Management runs in request lifecycle

### "JavaScript Detections Not Working"

**Cause:** `js_detection.passed` always false or undefined due to: CSP headers don't allow `/cdn-cgi/challenge-platform/`, using on first page visit (needs HTML page first), ad blockers or disabled JS, JSD not enabled in dashboard, or using Block action (must use Managed Challenge)  
**Solution:** Add CSP header `Content-Security-Policy: script-src 'self' /cdn-cgi/challenge-platform/;` and ensure JSD is enabled with Managed Challenge action

### "False Positives (Legitimate Users Blocked)"

**Cause:** Bot detection incorrectly flagging legitimate users  
**Solution:** Check Bot Analytics for affected IPs/paths, identify detection source (ML, Heuristics, etc.), create exception rule like `(cf.bot_management.score lt 30 and http.request.uri.path eq "/problematic-path")` with Action: Skip (Bot Management), or allowlist by IP/ASN/country

### "False Negatives (Bots Not Caught)"

**Cause:** Bots bypassing detection  
**Solution:** Lower score threshold (30 → 50), enable JavaScript Detections, add JA3/JA4 fingerprinting rules, or use rate limiting as fallback

### "Verified Bot Blocked"

**Cause:** Search engine bot blocked by WAF Managed Rules (not just Bot Management)  
**Solution:** Create WAF exception for specific rule ID and verify bot via reverse DNS

### "Yandex Bot Blocked During IP Update"

**Cause:** Yandex updates bot IPs; new IPs unrecognized for 48h during propagation  
**Solution:** 
1. Check Security Events for specific WAF rule ID blocking Yandex
2. Create WAF exception:
   ```txt
   (http.user_agent contains "YandexBot" and ip.src in {<yandex-ip-range>})
   Action: Skip (WAF Managed Ruleset)
   ```
3. Monitor Bot Analytics for 48h
4. Remove exception after propagation completes

Issue resolves automatically after 48h. Contact Cloudflare Support if persists.

### "JA3/JA4 Missing"

**Cause:** Non-HTTPS traffic, Worker routing traffic, Orange-to-Orange traffic via Worker, or Bot Management skipped  
**Solution:** JA3/JA4 only available for HTTPS/TLS traffic; check request routing

**JA3/JA4 Not User-Unique:** Same browser/library version = same fingerprint
- Don't use for user identification
- Use for client profiling only
- Fingerprints change with browser updates

