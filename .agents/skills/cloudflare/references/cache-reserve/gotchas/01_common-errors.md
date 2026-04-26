## Common Errors

### "Assets Not Being Cached in Cache Reserve"

**Cause:** Asset is not cacheable, TTL < 10 hours, Content-Length header missing, or blocking headers present (Set-Cookie, Vary: *)  
**Solution:** Ensure minimum TTL of 10+ hours (`Cache-Control: public, max-age=36000`), add Content-Length header, remove Set-Cookie header, and set `Vary: Accept-Encoding` (not *)

### "Range Requests Not Working" (Video Seeking Fails)

**Cause:** Cache Reserve does **NOT** support range requests (HTTP 206 Partial Content)  
**Solution:** Range requests bypass Cache Reserve entirely. For video streaming with seeking:
- Use edge cache only (shorter TTLs)
- Consider R2 with direct access for range-heavy workloads
- Accept that seekable content won't benefit from Cache Reserve persistence

### "Origin Bandwidth Higher Than Expected"

**Cause:** Cache Reserve fetches **uncompressed** content from origin, even though it serves compressed to visitors  
**Solution:** 
- If origin charges by bandwidth, factor in uncompressed transfer costs
- Cache Reserve compresses for visitors automatically (saves visitor bandwidth)
- Compare: origin egress savings vs higher uncompressed fetch costs

### "Cloudflare Images Not Caching with Cache Reserve"

**Cause:** Cloudflare Images with `Vary: Accept` header (format negotiation) is incompatible with Cache Reserve  
**Solution:** 
- Cache Reserve silently skips images with Vary for format negotiation
- Original images (non-transformed) may still be eligible
- Use Cloudflare Images variants or edge cache for transformed images

### "High Class A Operations Costs"

**Cause:** Frequent cache misses, short TTLs, or frequent revalidation  
**Solution:** Increase TTL for stable content (24+ hours), enable Tiered Cache to reduce direct Cache Reserve misses, or use stale-while-revalidate

### "Purge Not Working as Expected"

**Cause:** Purge by tag only triggers revalidation but doesn't remove from Cache Reserve storage  
**Solution:** Use purge by URL for immediate removal, or disable Cache Reserve then clear all data for complete removal

### "O2O (Orange-to-Orange) Assets Not Caching"

**Cause:** Orange-to-Orange (proxied zone requesting another proxied zone on Cloudflare) bypasses Cache Reserve  
**Solution:** 
- **What is O2O**: Zone A (proxied) → Zone B (proxied), both on Cloudflare
- **Detection**: Check `cf-cache-status` for `BYPASS` and review request path
- **Workaround**: Use R2 or direct origin access instead of O2O proxy chains

### "Cache Reserve must be OFF before clearing data"

**Cause:** Attempting to clear Cache Reserve data while it's still enabled  
**Solution:** Disable Cache Reserve first, wait briefly for propagation (5s), then clear data (can take up to 24 hours)

