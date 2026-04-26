## Security

### Envelope vs Header From (Spoofing)

```typescript
const envelopeFrom = message.from;               // SMTP MAIL FROM (trusted)
const headerFrom = (await PostalMime.parse(buffer)).from?.address; // (untrusted)
// Use envelope for security decisions
```

### Input Validation

```typescript
if (message.rawSize > 5_000_000) { message.setReject('Too large'); return; }
if ((message.headers.get('Subject') || '').length > 1000) {
  message.setReject('Invalid subject'); return;
}
```

### DMARC for Replies

Replies fail silently without DMARC. Verify: `dig TXT _dmarc.example.com`

