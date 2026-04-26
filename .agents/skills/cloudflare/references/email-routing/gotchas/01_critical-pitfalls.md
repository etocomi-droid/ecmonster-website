## Critical Pitfalls

### Stream Consumption (MOST COMMON)

**Problem:** "stream already consumed" or worker hangs

**Cause:** `message.raw` is `ReadableStream` - consume once only

**Solution:**
```typescript
// ❌ WRONG
const email1 = await parser.parse(await message.raw.arrayBuffer());
const email2 = await parser.parse(await message.raw.arrayBuffer()); // FAILS

// ✅ CORRECT
const raw = await message.raw.arrayBuffer();
const email = await parser.parse(raw);
```

Consume `message.raw` immediately before any async operations.

### Destination Verification

**Problem:** Emails not forwarding

**Cause:** Destination unverified

**Solution:** Add destination, check inbox for verification email, click link. Verify status: `GET /zones/{id}/email/routing/addresses`

### Mail Authentication

**Problem:** Legitimate emails rejected

**Cause:** Missing SPF/DKIM/DMARC on sender domain

**Solution:** Configure sender DNS:
```dns
example.com. IN TXT "v=spf1 include:_spf.example.com ~all"
selector._domainkey.example.com. IN TXT "v=DKIM1; k=rsa; p=..."
_dmarc.example.com. IN TXT "v=DMARC1; p=quarantine"
```

### Envelope vs Header

**Problem:** Filtering on wrong address

**Solution:**
```typescript
// Routing/auth: envelope
if (message.from === "trusted@example.com") { }

// Display: headers
const display = message.headers.get("from");
```

### SendEmail Limits

| Issue | Limit | Solution |
|-------|-------|----------|
| From domain | Must own | Use Email Routing domain |
| Volume | ~100/min Free | Upgrade or throttle |
| Attachments | Not supported | Link to R2 |
| Type | Transactional | No bulk |

