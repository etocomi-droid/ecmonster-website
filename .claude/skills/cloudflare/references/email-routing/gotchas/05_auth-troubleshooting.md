## Auth Troubleshooting

### Check Status

```typescript
const auth = message.headers.get("authentication-results") || "";
console.log({
  spf: auth.includes("spf=pass"),
  dkim: auth.includes("dkim=pass"),
  dmarc: auth.includes("dmarc=pass")
});

if (!auth.includes("pass")) {
  message.setReject("Failed auth");
  return;
}
```

### SPF Issues

**Causes:** Forwarding breaks SPF, too many lookups (>10), missing includes

**Solution:**
```dns
; ✅ Good
example.com. IN TXT "v=spf1 include:_spf.google.com ~all"

; ❌ Bad - too many
example.com. IN TXT "v=spf1 include:a.com include:b.com ... ~all"
```

### DMARC Alignment

**Cause:** From domain must match SPF/DKIM domain

