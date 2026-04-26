## Asset Eligibility

Cache Reserve only stores assets meeting **ALL** criteria:

- Cacheable per Cloudflare's standard rules
- Minimum 10-hour TTL (36000 seconds)
- `Content-Length` header present
- Original files only (not transformed images)

### Eligibility Checklist

Use this checklist to verify if an asset is eligible:

- [ ] Zone has Cache Reserve enabled
- [ ] Zone has Tiered Cache enabled (required)
- [ ] Asset TTL ≥ 10 hours (36,000 seconds)
- [ ] `Content-Length` header present on origin response
- [ ] No `Set-Cookie` header (or uses private directive)
- [ ] `Vary` header is NOT `*` (can be `Accept-Encoding`)
- [ ] Not an image transformation variant (original images OK)
- [ ] Not a range request (no HTTP 206 support)
- [ ] Not O2O (Orange-to-Orange) proxied request

**All boxes must be checked for Cache Reserve eligibility.**

### Not Eligible

- Assets with TTL < 10 hours
- Responses without `Content-Length` header
- Image transformation variants (original images are eligible)
- Responses with `Set-Cookie` headers
- Responses with `Vary: *` header
- Assets from R2 public buckets on same zone
- O2O (Orange-to-Orange) setup requests
- **Range requests** (video seeking, partial content downloads)

